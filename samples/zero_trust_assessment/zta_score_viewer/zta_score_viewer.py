r"""Zero Trust Assessment Score Viewer.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |             FalconPy
`-------'                         `-------'

_____  ______   ____       _____   __   ___   ____     ___
|     T|      T /    T     / ___/  /  ] /   \ |    \   /  _]
l__/  ||      |Y  o  |    (   \_  /  / Y     Y|  D  ) /  [_
|   __jl_j  l_j|     |     \__  T/  /  |  O  ||    / Y    _]
|  /  |  |  |  |  _  |     /  \ /   \_ |     ||    \ |   [_
|     |  |  |  |  |  |     \    \     |l     !|  .  Y|     T
l_____j  l__j  l__j__j      \___j\____j \___/ l__j\_jl_____j

 __ __  ____    ___ __    __    ___  ____
|  T  |l    j  /  _]  T__T  T  /  _]|    \
|  |  | |  T  /  [_|  |  |  | /  [_ |  D  )
|  |  | |  | Y    _]  |  |  |Y    _]|    /
l  :  ! |  | |   [_l  `  '  !|   [_ |    \
 \   /  j  l |     T\      / |     T|  .  Y
  \_/  |____jl_____j \_/\_/  l_____jl__j\_j

                    Zero Trust Assessment Score Viewer
                    Uses: ZeroTrustAssessment
                    Scope: zero-trust-assessment:read

A Dear PyGui desktop application for visualising CrowdStrike Falcon
Zero Trust Assessment (ZTA) scores across your fleet.

- Bar chart showing device count per 10-point score bucket (0-9, 10-19 … 90-100)
- Sortable table: device AID prefix, full AID, ZTA score, OS/platform, last seen
- "Worst Offenders" panel: 10 lowest-scoring devices
- Refresh button + auto-refresh interval selector
- Audit tab: aggregate audit report from getAuditV1

Authentication
--------------
  Credentials are resolved in this order (first match wins):
    1. CLI flags: -k / --client_id  and  -s / --client_secret
    2. Environment variables: FALCON_CLIENT_ID / FALCON_CLIENT_SECRET

  If no credentials are found, an error dialog is shown.
  A "Reconnect" button re-authenticates if the token expires mid-session.

Usage
-----
    FALCON_CLIENT_ID=xxx FALCON_CLIENT_SECRET=yyy pipenv run python3 zta_score_viewer.py
    pipenv run python3 zta_score_viewer.py -k KEY -s SECRET

CLI flags
---------
  -k / --client_id      Falcon API client ID (overrides FALCON_CLIENT_ID env var)
  -s / --client_secret  Falcon API client secret (overrides FALCON_CLIENT_SECRET env var)

Required API scope
------------------
  zero-trust-assessment:read
"""
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals,too-many-statements
# pylint: disable=too-many-instance-attributes,too-many-branches

import argparse
import json
import os
import threading
from datetime import datetime
from typing import Optional

import dearpygui.dearpygui as dpg
from falconpy import Hosts, ZeroTrustAssessment

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

APP_TITLE = "Zero Trust Assessment Score Viewer"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 830

# Map ZTA event_platform codes to human-readable names
PLATFORM_NAMES = {
    "Lin": "Linux",
    "Win": "Windows",
    "Mac": "macOS",
    "iOS": "iOS",
    "Android": "Android",
    "Chromium": "ChromeOS",
}

# Score distribution buckets: [0-9], [10-19], …, [90-100]
BUCKET_LABELS = [f"{i*10}-{i*10+9}" if i < 10 else "100" for i in range(11)]
NUM_BUCKETS = 11  # 0-9 through 100 (100 is its own bucket)

AUTO_REFRESH_OPTIONS = ["Off", "30s", "1m", "5m"]
AUTO_REFRESH_SECONDS = {"Off": 0, "30s": 30, "1m": 60, "5m": 300}

PAGE_SIZE_OPTIONS = ["25", "50", "100", "200"]
DEFAULT_PAGE_SIZE = 50

# Severity colour bands (R, G, B, A) mapped to score ranges
SCORE_COLOURS = {
    "critical": (220, 50, 50, 255),   # 0–39
    "high":     (220, 130, 50, 255),  # 40–59
    "medium":   (220, 200, 50, 255),  # 60–79
    "good":     (50, 180, 80, 255),   # 80–100
}


def score_colour(score: float):
    """Return a (R, G, B, A) tuple appropriate for the given ZTA score."""
    if score < 40:
        return SCORE_COLOURS["critical"]
    if score < 60:
        return SCORE_COLOURS["high"]
    if score < 80:
        return SCORE_COLOURS["medium"]
    return SCORE_COLOURS["good"]


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

class DeviceRecord:
    """Holds ZTA data for a single device as returned by getAssessmentV1."""

    def __init__(self, raw: dict):
        """Initialise from the raw API response dict for one device.

        Supports two call shapes:
        - Full record from getAssessmentV1: has 'assessment', 'event_platform',
          'product_type_desc', 'modified_time'.
        - Score-only record from getAssessmentsByScoreV1: has 'aid' and 'score'.
        """
        assessment = raw.get("assessment", {})
        self.aid: str = raw.get("aid", "")
        self.hostname: str = ""  # populated after construction via Hosts API lookup
        # ZTA API does not return hostname; display the full AID as identifier
        # Map short platform code to full name, fall back to raw code
        platform_code = raw.get("event_platform", "")
        platform = PLATFORM_NAMES.get(platform_code, platform_code)
        product = raw.get("product_type_desc", "")
        self.os: str = f"{platform} {product}".strip() if (platform or product) else ""
        # Score is in assessment.overall for full records, or raw.score for score-only records
        self.score: float = float(
            assessment.get("overall", raw.get("score", 0))
        )
        ts = raw.get("modified_time", "")
        self.last_seen: str = ts[:19].replace("T", " ") if ts else ""

    def display_aid(self) -> str:
        """Return 'hostname (AID)' if hostname resolved, else plain AID."""
        if self.hostname:
            return f"{self.hostname} ({self.aid})"
        return self.aid

    def table_row(self) -> list:
        """Return a list of display values suitable for a table row."""
        return [self.display_aid(), f"{self.score:.1f}", self.os, self.last_seen]


# ---------------------------------------------------------------------------
# FalconPy client wrapper
# ---------------------------------------------------------------------------

class ZTAClient:
    """Thin wrapper around the FalconPy ZeroTrustAssessment service class."""

    def __init__(self):
        """Construct without authenticating — call connect() first."""
        self._sdk: Optional[ZeroTrustAssessment] = None
        self._hosts_sdk: Optional[Hosts] = None
        self.status: str = "disconnected"
        self.error: str = ""

    def connect(
        self,
        client_id: str = "",
        client_secret: str = "",  # nosec - Bandit FP
    ) -> bool:
        """Authenticate using provided credentials or env-var fallback.

        CLI-supplied *client_id* / *client_secret* take precedence over
        FALCON_CLIENT_ID / FALCON_CLIENT_SECRET environment variables.

        Returns True on success, False on failure.  Sets self.error on failure.
        """
        client_id = client_id or os.environ.get("FALCON_CLIENT_ID", "")
        client_secret = client_secret or os.environ.get("FALCON_CLIENT_SECRET", "")
        if not client_id or not client_secret:
            self.error = "FALCON_CLIENT_ID or FALCON_CLIENT_SECRET not set in environment."
            self.status = "error"
            return False
        try:
            sdk = ZeroTrustAssessment(client_id=client_id, client_secret=client_secret)
            if not sdk.token_valid:
                self.error = f"Authentication failed: {sdk.token_fail_reason}"
                self.status = "error"
                return False
            self._sdk = sdk
            self._hosts_sdk = Hosts(client_id=client_id, client_secret=client_secret)
            self.status = "connected"
            self.error = ""
            return True
        except Exception as exc:  # pylint: disable=broad-except
            self.error = str(exc)
            self.status = "error"
            return False

    def fetch_assessments(
        self, limit: int = 500, after: str = ""
    ) -> tuple[list[DeviceRecord], str]:
        """Return ``(records, next_after_token)`` for up to *limit* devices.

        Two-step process matching the real ZTA API:

        Step 1 — getAssessmentsByScoreV1:
            Returns paginated (aid, score) pairs sorted by score ascending.
            Requires a filter expression; "score:>=0" matches all assessed devices.
            Pass *after* to continue from a previous cursor position.

        Step 2 — getAssessmentV1 (batched):
            Takes a list of AIDs; returns full records including event_platform,
            product_type_desc, modified_time, and assessment.overall.
            Processed in batches of 100 to stay within API limits.

        Returns a tuple of (records, next_after_token).  next_after_token is an
        empty string when no further pages are available.
        """
        if self._sdk is None:
            return [], ""

        # --- Step 1: collect (aid, score) pairs ---
        aid_score: dict[str, int] = {}
        after_token: Optional[str] = after or None

        while len(aid_score) < limit:
            kwargs: dict = {
                "filter": "score:>=0",
                "limit": min(200, limit - len(aid_score)),
            }
            if after_token:
                kwargs["after"] = after_token

            resp = self._sdk.getAssessmentsByScoreV1(**kwargs)
            if resp.get("status_code", 0) != 200:
                break

            body = resp.get("body", {})
            for item in (body.get("resources", []) or []):
                aid_score[item["aid"]] = item.get("score", 0)

            pagination = body.get("meta", {}).get("pagination", {})
            after_token = pagination.get("after")
            total = pagination.get("total", 0)

            if not after_token or len(aid_score) >= total or len(aid_score) >= limit:
                break

        if not aid_score:
            return [], ""

        # --- Step 2: fetch full details for collected AIDs in batches of 100 ---
        records: list[DeviceRecord] = []
        aids = list(aid_score.keys())
        batch_size = 100

        for i in range(0, len(aids), batch_size):
            batch = aids[i:i + batch_size]
            resp2 = self._sdk.getAssessmentV1(ids=batch)
            if resp2.get("status_code", 0) != 200:
                # Fall back: construct minimal records from step-1 data
                for aid in batch:
                    records.append(DeviceRecord({"aid": aid, "score": aid_score[aid]}))
                continue
            for item in (resp2.get("body", {}).get("resources", []) or []):
                records.append(DeviceRecord(item))

        return records, (after_token or "")

    def fetch_bucket_counts(self) -> list[int]:
        """Return accurate per-bucket device counts by querying each score range.

        The standard fetch_assessments() only retrieves up to *limit* devices
        sorted ascending by score, which causes all sampled devices to fall in
        the lowest bucket on large environments.  This method queries each
        10-point range individually to get the true count for every bucket.

        Returns a list of 11 integers: indices 0-9 = ranges 0-9…90-99,
        index 10 = score 100.
        """
        if self._sdk is None:
            return [0] * NUM_BUCKETS

        counts = [0] * NUM_BUCKETS
        for i in range(10):
            lo = i * 10
            hi = lo + 9
            resp = self._sdk.getAssessmentsByScoreV1(
                filter=f"score:>={lo}+score:<={hi}", limit=1
            )
            if resp.get("status_code", 0) == 200:
                total = (
                    resp.get("body", {})
                    .get("meta", {})
                    .get("pagination", {})
                    .get("total", 0)
                )
                counts[i] = total

        # Bucket 10: score exactly 100
        resp100 = self._sdk.getAssessmentsByScoreV1(filter="score:>=100", limit=1)
        if resp100.get("status_code", 0) == 200:
            counts[10] = (
                resp100.get("body", {})
                .get("meta", {})
                .get("pagination", {})
                .get("total", 0)
            )

        return counts

    def fetch_hostnames(self, aids: list[str]) -> dict[str, str]:
        """Return a dict mapping AID → hostname for AIDs that resolve via Hosts API.

        Uses get_device_details_v2 in batches of 20.  AIDs for CWPP/container
        workloads typically return 404 and are silently omitted.
        """
        if self._hosts_sdk is None:
            return {}
        result: dict[str, str] = {}
        batch_size = 20
        for i in range(0, len(aids), batch_size):
            batch = aids[i:i + batch_size]
            try:
                resp = self._hosts_sdk.get_device_details_v2(ids=batch)
            except Exception:  # pylint: disable=broad-except
                continue # nosec - Allow silent 404 failure
            for dev in (resp.get("body", {}).get("resources", []) or []):
                aid = dev.get("device_id", "")
                hostname = dev.get("hostname", "")
                if aid and hostname:
                    result[aid] = hostname
        return result

    def fetch_audit(self) -> dict:
        """Return the raw audit report body dict, or an error body."""
        if self._sdk is None:
            return {}
        resp = self._sdk.get_audit()
        if resp.get("status_code", 0) == 200:
            return resp.get("body", {})
        return resp.get("body", {})


# ---------------------------------------------------------------------------
# Application state (shared between threads via threading.Lock)
# ---------------------------------------------------------------------------

class AppState:
    """Mutable application state accessed from both the UI thread and worker threads."""

    def __init__(self):
        """Initialise all state fields to safe defaults."""
        self.lock = threading.Lock()
        self.devices: list[DeviceRecord] = []
        self.bucket_counts: list[int] = [0] * NUM_BUCKETS
        self.audit_data: dict = {}
        self.loading: bool = False
        self._refresh_pending: bool = False
        self.last_refreshed: str = ""
        self.error_message: str = ""
        self.auto_refresh_seconds: int = 0
        self._stop_event = threading.Event()
        self._refresh_thread: Optional[threading.Thread] = None

    def stop_refresh(self):
        """Signal the auto-refresh loop to stop and wait for it to exit."""
        self._stop_event.set()
        if self._refresh_thread and self._refresh_thread.is_alive():
            self._refresh_thread.join(timeout=1)

    def start_refresh_loop(self, interval_seconds: int, callback):
        """Stop any existing refresh loop then start a new one with *callback*.

        *callback* is called once per *interval_seconds* until stop_refresh()
        is called.  Has no effect when *interval_seconds* is 0.
        """
        self.stop_refresh()
        self._stop_event.clear()
        if interval_seconds == 0:
            return

        def _loop():
            while not self._stop_event.wait(timeout=interval_seconds):
                callback()

        self._refresh_thread = threading.Thread(target=_loop, daemon=True)
        self._refresh_thread.start()


# ---------------------------------------------------------------------------
# GUI helpers
# ---------------------------------------------------------------------------

def _build_buckets(devices: list[DeviceRecord]) -> list[int]:
    """Count devices per 10-point score bucket (index 0 = scores 0-9, index 10 = 100)."""
    buckets = [0] * NUM_BUCKETS
    for dev in devices:
        # Score 100 goes in the last bucket (index 10)
        idx = min(int(dev.score) // 10, 10)
        buckets[idx] += 1
    return buckets


def _worst_offenders(devices: list[DeviceRecord], n: int = 10) -> list[DeviceRecord]:
    """Return the *n* devices with the lowest ZTA score."""
    return sorted(devices, key=lambda d: d.score)[:n]


# ---------------------------------------------------------------------------
# Main application class
# ---------------------------------------------------------------------------

class ZTAScoreViewerApp:
    """Dear PyGui application for visualising Zero Trust Assessment scores."""

    def __init__(self, client_id: str = "", client_secret: str = ""): # nosec - Bandit FP
        """Initialise the application, client, and state.

        *client_id* and *client_secret* are CLI-supplied credential overrides.
        When empty the client falls back to environment variables at connect time.
        """
        self.client = ZTAClient()
        self.state = AppState()
        # CLI credential overrides — forwarded to connect() and reconnect
        self._client_id = client_id
        self._client_secret = client_secret
        # Dear PyGui item tags — populated during setup
        self._tags: dict = {}
        # Pagination state for device table
        self._page_index: int = 0
        self._page_size: int = DEFAULT_PAGE_SIZE
        # Sorted device list (may differ from state.devices after column sort)
        self._sorted_devices: list[DeviceRecord] = []
        # Progressive API pagination state
        self._api_after_token: str = ""
        self._has_more_api_data: bool = False
        self._api_fetching_more: bool = False
        self._load_more_pending: bool = False  # set True when _worker_load_more completes

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def run(self):
        """Authenticate, build the UI, then start the Dear PyGui event loop."""
        dpg.create_context()
        dpg.create_viewport(title=APP_TITLE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        dpg.setup_dearpygui()

        self._build_ui()

        # Authenticate and do first data load
        ok = self.client.connect(
            client_id=self._client_id,
            client_secret=self._client_secret,
        )
        if ok:
            self._set_title_status("connected")
            self._async_refresh()
        else:
            self._set_title_status("error")
            self._show_error(self.client.error)

        dpg.set_frame_callback(1, self._update_device_table_height)
        dpg.set_viewport_resize_callback(self._update_device_table_height)

        dpg.show_viewport()
        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
            needs = False
            with self.state.lock:
                if self.state._refresh_pending:
                    self.state._refresh_pending = False
                    needs = True
            if needs:
                self._hide_loading()
                self._refresh_ui()

        # Clean up auto-refresh thread
        self.state.stop_refresh()
        dpg.destroy_context()

    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------

    def _build_ui(self):
        """Construct all Dear PyGui windows and widgets."""
        with dpg.window(tag="primary", label=APP_TITLE, no_title_bar=True,
                        no_move=True, no_resize=True, no_scrollbar=True):
            dpg.set_primary_window("primary", True)

            # ---- Toolbar row ----
            with dpg.group(horizontal=True):
                dpg.add_button(label="Refresh", callback=self._on_refresh_click)
                dpg.add_text("Auto-refresh:")
                dpg.add_combo(
                    items=AUTO_REFRESH_OPTIONS,
                    default_value="Off",
                    width=80,
                    tag="auto_refresh_combo",
                    callback=self._on_auto_refresh_change,
                )
                dpg.add_button(
                    label="Reconnect",
                    callback=self._on_reconnect_click,
                    tag="reconnect_btn",
                )
                dpg.add_text("", tag="status_text")
                dpg.add_text("", tag="last_refreshed_text")

            dpg.add_separator()

            # ---- Tab bar ----
            with dpg.tab_bar(tag="main_tabs"):
                with dpg.tab(label="Dashboard", tag="tab_dashboard"):
                    self._build_dashboard_tab()
                with dpg.tab(label="Worst Offenders", tag="tab_worst"):
                    self._build_worst_offenders_tab()
                with dpg.tab(label="Audit Report", tag="tab_audit"):
                    self._build_audit_tab()

            # Loading overlay is a separate modal window — see _show_loading/_hide_loading

    def _build_dashboard_tab(self):
        """Build the score distribution chart and full device table."""
        # Score distribution bar chart
        with dpg.collapsing_header(label="Score Distribution", default_open=True):
            with dpg.plot(
                label="Devices per Score Bucket",
                height=220,
                width=-1,
                tag="dist_plot",
            ):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="Score Range", tag="dist_x_axis")
                dpg.set_axis_ticks("dist_x_axis", tuple(
                    (BUCKET_LABELS[i], float(i)) for i in range(NUM_BUCKETS)
                ))
                with dpg.plot_axis(dpg.mvYAxis, label="Device Count", tag="dist_y_axis"):
                    dpg.add_bar_series(
                        x=[float(i) for i in range(NUM_BUCKETS)],
                        y=[0.0] * NUM_BUCKETS,
                        weight=0.8,
                        tag="dist_bars",
                        label="Devices",
                    )

        dpg.add_separator()

        # Full device table
        dpg.add_text("All Devices", tag="device_count_label")
        with dpg.table(
            tag="device_table",
            header_row=True,
            borders_outerH=True,
            borders_innerV=True,
            borders_innerH=True,
            borders_outerV=True,
            scrollY=True,
            height=460,
            sortable=True,
            policy=dpg.mvTable_SizingStretchProp,
            callback=self._on_table_sort,
        ):
            dpg.add_table_column(label="AID / Hostname", width_stretch=True)
            dpg.add_table_column(label="Score", width_fixed=True, init_width_or_weight=70,
                                 default_sort=True, prefer_sort_ascending=True)
            dpg.add_table_column(label="OS", width_stretch=True)
            dpg.add_table_column(label="Last Seen", width_fixed=True, init_width_or_weight=160)

        # Pagination controls below device table
        with dpg.group(horizontal=True, tag="pagination_bar"):
            dpg.add_button(label="< Prev", tag="page_prev_btn",
                           callback=self._on_page_prev, enabled=False)
            dpg.add_text("Page 1 of 1", tag="page_label")
            dpg.add_button(label="Next >", tag="page_next_btn",
                           callback=self._on_page_next, enabled=False)
            dpg.add_text("  Rows/page:")
            dpg.add_combo(
                items=PAGE_SIZE_OPTIONS,
                default_value=str(DEFAULT_PAGE_SIZE),
                width=70,
                tag="page_size_combo",
                callback=self._on_page_size_change,
            )

    def _update_device_table_height(self, *_args) -> None:
        """Resize the All Devices table to fill the remaining vertical space.

        dpg.get_item_rect_min() requires at least one rendered frame before
        rect state is populated.  If called too early it raises KeyError, so
        we retry on the next frame until geometry is available.
        """
        if not (dpg.does_item_exist("device_table") and dpg.does_item_exist("pagination_bar")):
            return
        try:
            table_y = dpg.get_item_rect_min("device_table")[1]
            pagination_h = dpg.get_item_rect_size("pagination_bar")[1]
        except KeyError:
            # Rect state not ready yet — retry on the very next frame.
            dpg.set_frame_callback(dpg.get_frame_count() + 1,
                                   self._update_device_table_height)
            return
        viewport_h = dpg.get_viewport_client_height()
        new_height = max(100, viewport_h - table_y - pagination_h)
        dpg.configure_item("device_table", height=new_height)

    def _build_worst_offenders_tab(self):
        """Build the top-10 lowest-scoring devices panel."""
        dpg.add_text("10 Lowest-Scoring Devices", color=(220, 200, 50, 255))
        dpg.add_separator()
        with dpg.table(
            tag="worst_table",
            header_row=True,
            borders_outerH=True,
            borders_innerV=True,
            borders_innerH=True,
            borders_outerV=True,
            scrollY=True,
            height=680,
            policy=dpg.mvTable_SizingStretchProp,
        ):
            dpg.add_table_column(label="Rank", width_fixed=True, init_width_or_weight=50)
            dpg.add_table_column(label="AID", width_stretch=True)
            dpg.add_table_column(label="Score", width_fixed=True, init_width_or_weight=70)
            dpg.add_table_column(label="OS", width_stretch=True)
            dpg.add_table_column(label="Last Seen", width_fixed=True, init_width_or_weight=160)

    def _build_audit_tab(self):
        """Build the audit report viewer."""
        with dpg.group(horizontal=True):
            dpg.add_button(label="Fetch Audit Report", callback=self._on_fetch_audit)
        dpg.add_separator()
        dpg.add_input_text(
            tag="audit_text",
            multiline=True,
            readonly=True,
            width=-1,
            height=700,
            default_value="Click 'Fetch Audit Report' to load audit data.",
        )

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

    def _async_refresh(self):
        """Kick off a background thread to reload device data."""
        if self.state.loading:
            return
        self.state.loading = True
        self._show_loading()
        t = threading.Thread(target=self._worker_refresh, daemon=True)
        t.start()

    def _worker_refresh(self):
        """Background worker: fetch assessments and update UI."""
        try:
            devices, next_after = self.client.fetch_assessments()
            bucket_counts = self.client.fetch_bucket_counts()
            # Resolve hostnames for endpoint AIDs (CWPP AIDs will not resolve)
            aids = [d.aid for d in devices]
            hostname_map = self.client.fetch_hostnames(aids)
            for dev in devices:
                dev.hostname = hostname_map.get(dev.aid, "")
            ts = datetime.now().strftime("%H:%M:%S")
            self._api_after_token = next_after
            self._has_more_api_data = bool(next_after)
            with self.state.lock:
                self.state.devices = devices
                self.state.bucket_counts = bucket_counts
                self.state.last_refreshed = ts
                self.state.error_message = ""
        except Exception as exc:  # pylint: disable=broad-except
            with self.state.lock:
                self.state.error_message = str(exc)
        finally:
            with self.state.lock:
                self.state.loading = False
                self.state._refresh_pending = True

    def _async_load_more(self):
        """Fetch the next batch of devices using the saved API cursor."""
        if self._api_fetching_more or not self._api_after_token:
            return
        self._api_fetching_more = True
        self._show_loading()
        t = threading.Thread(target=self._worker_load_more, daemon=True)
        t.start()

    def _worker_load_more(self):
        """Background worker: append the next page of assessments to state.devices."""
        try:
            new_devices, next_after = self.client.fetch_assessments(
                after=self._api_after_token
            )
            aids = [d.aid for d in new_devices]
            hostname_map = self.client.fetch_hostnames(aids)
            for dev in new_devices:
                dev.hostname = hostname_map.get(dev.aid, "")
            self._api_after_token = next_after
            self._has_more_api_data = bool(next_after)
            self._load_more_pending = True
            with self.state.lock:
                self.state.devices = self.state.devices + new_devices
                self.state.error_message = ""
        except Exception as exc:  # pylint: disable=broad-except
            with self.state.lock:
                self.state.error_message = str(exc)
        finally:
            self._api_fetching_more = False
            with self.state.lock:
                self.state.loading = False
                self.state._refresh_pending = True

    def _refresh_ui(self):
        """Rebuild all data-driven widgets from self.state.devices."""
        with self.state.lock:
            devices = list(self.state.devices)
            bucket_counts = list(self.state.bucket_counts)
            ts = self.state.last_refreshed
            err = self.state.error_message

        if err:
            self._show_error(err)
            return

        # Update status labels
        dpg.set_value("last_refreshed_text", f"  Last refreshed: {ts}")

        if self._load_more_pending:
            # Load-more: append new devices, advance to next page
            self._load_more_pending = False
            prev_total = len(self._sorted_devices)
            self._sorted_devices = devices
            total_pages = max(1, (len(devices) + self._page_size - 1) // self._page_size)
            # Advance to the page that shows the first new device
            self._page_index = prev_total // self._page_size
            self._page_index = min(self._page_index, total_pages - 1)
            self._render_device_page()
        else:
            # Full refresh: update chart, reset pagination, rebuild worst offenders
            dpg.set_value("dist_bars", [[float(i) for i in range(NUM_BUCKETS)],
                                        [float(b) for b in bucket_counts]])
            dpg.fit_axis_data("dist_y_axis")
            self._sorted_devices = devices
            self._page_index = 0
            self._render_device_page()
            self._repopulate_worst_table(_worst_offenders(devices))

    def _render_device_page(self):
        """Render the current page of the device table and update pagination controls."""
        total = len(self._sorted_devices)
        total_pages = max(1, (total + self._page_size - 1) // self._page_size)
        self._page_index = max(0, min(self._page_index, total_pages - 1))
        start = self._page_index * self._page_size
        end = min(start + self._page_size, total)
        page_devices = self._sorted_devices[start:end]

        # Update count label
        with self.state.lock:
            fleet_total = sum(self.state.bucket_counts)
        more_hint = "  (more available)" if self._has_more_api_data else ""
        dpg.set_value(
            "device_count_label",
            f"All Devices - showing {start + 1}-{end} of {total} fetched"
            f"  ({fleet_total} total in fleet){more_hint}",
        )

        # Update pagination controls
        on_last_page = self._page_index >= total_pages - 1
        dpg.set_value(
            "page_label",
            f"Page {self._page_index + 1} of {total_pages}",
        )
        dpg.configure_item("page_prev_btn", enabled=self._page_index > 0)
        dpg.configure_item(
            "page_next_btn",
            enabled=(not on_last_page) or self._has_more_api_data,
        )

        # Repopulate table rows for this page
        for child in dpg.get_item_children("device_table", 1) or []:
            dpg.delete_item(child)

        for dev in page_devices:
            colour = score_colour(dev.score)
            with dpg.table_row(parent="device_table"):
                dpg.add_text(dev.display_aid())
                dpg.add_text(f"{dev.score:.1f}", color=colour)
                dpg.add_text(dev.os)
                dpg.add_text(dev.last_seen)

    def _repopulate_device_table(self, devices: list[DeviceRecord]):
        """Clear and repopulate the main device table (used by sort handler)."""
        self._sorted_devices = devices
        self._page_index = 0
        self._render_device_page()

    def _repopulate_worst_table(self, worst: list[DeviceRecord]):
        """Clear and repopulate the worst offenders table."""
        for child in dpg.get_item_children("worst_table", 1) or []:
            dpg.delete_item(child)

        for rank, dev in enumerate(worst, start=1):
            colour = score_colour(dev.score)
            with dpg.table_row(parent="worst_table"):
                dpg.add_text(str(rank))
                dpg.add_text(dev.aid)
                dpg.add_text(f"{dev.score:.1f}", color=colour)
                dpg.add_text(dev.os)
                dpg.add_text(dev.last_seen)

    # ------------------------------------------------------------------
    # Auto-refresh loop
    # ------------------------------------------------------------------

    def _start_auto_refresh(self, interval_seconds: int):
        """Delegate to AppState to (re)start the background auto-refresh loop."""
        self.state.start_refresh_loop(interval_seconds, self._async_refresh)

    # ------------------------------------------------------------------
    # Status / error helpers
    # ------------------------------------------------------------------

    def _set_title_status(self, status: str):
        """Update the status label colour and text."""
        colours = {
            "connected": (50, 200, 80, 255),
            "error": (220, 50, 50, 255),
            "disconnected": (180, 180, 180, 255),
        }
        labels = {
            "connected": " Connected",
            "error": " Auth Error",
            "disconnected": " Disconnected",
        }
        colour = colours.get(status, colours["disconnected"])
        label = labels.get(status, " Unknown")
        dpg.configure_item("status_text", color=colour)
        dpg.set_value("status_text", label)

    def _show_loading(self):
        """Show a centered modal loading overlay."""
        if dpg.does_item_exist("loading_popup"):
            return
        with dpg.window(
            label="Loading",
            modal=True,
            tag="loading_popup",
            width=220,
            height=100,
            no_resize=True,
            no_close=True,
            pos=(WINDOW_WIDTH // 2 - 110, WINDOW_HEIGHT // 2 - 50),
        ):
            dpg.add_loading_indicator()
            dpg.add_text("Fetching data, please wait...")

    def _hide_loading(self):
        """Dismiss the loading overlay if present."""
        if dpg.does_item_exist("loading_popup"):
            dpg.delete_item("loading_popup")

    def _show_error(self, message: str):
        """Display a modal error popup."""
        if dpg.does_item_exist("error_popup"):
            dpg.delete_item("error_popup")
        with dpg.window(
            label="Error",
            modal=True,
            tag="error_popup",
            width=420,
            height=160,
            no_resize=True,
            pos=(WINDOW_WIDTH // 2 - 210, WINDOW_HEIGHT // 2 - 80),
        ):
            dpg.add_text(message, wrap=400)
            dpg.add_spacer(height=12)
            dpg.add_button(
                label="OK",
                callback=lambda: dpg.delete_item("error_popup"),
            )

    # ------------------------------------------------------------------
    # Event callbacks
    # ------------------------------------------------------------------

    def _on_refresh_click(self, _sender, _app_data):
        """Handle manual Refresh button click."""
        self._async_refresh()

    def _on_reconnect_click(self, _sender, _app_data):
        """Handle Reconnect button: re-authenticate and reload data."""
        ok = self.client.connect(
            client_id=self._client_id,
            client_secret=self._client_secret,
        )
        if ok:
            self._set_title_status("connected")
            self._async_refresh()
        else:
            self._set_title_status("error")
            self._show_error(self.client.error)

    def _on_auto_refresh_change(self, _sender, app_data):
        """Handle auto-refresh interval combo box change."""
        seconds = AUTO_REFRESH_SECONDS.get(app_data, 0)
        self.state.auto_refresh_seconds = seconds
        self._start_auto_refresh(seconds)

    def _on_table_sort(self, _sender, sort_specs):
        """Re-sort the device table when a column header is clicked."""
        if sort_specs is None:
            return
        with self.state.lock:
            devices = list(self.state.devices)
        if not devices:
            return

        # sort_specs is a list of (column_id, direction) tuples
        col_id, direction = sort_specs[0]

        # Map column index to DeviceRecord attribute
        col_map = {0: "aid", 1: "score", 2: "os", 3: "last_seen"}

        # Determine column index from the column tag/id
        columns = dpg.get_item_children("device_table", 0) or []
        col_index = 0
        for i, col in enumerate(columns):
            if col == col_id:
                col_index = i
                break

        attr = col_map.get(col_index, "score")
        reverse = direction < 0
        devices.sort(key=lambda d: getattr(d, attr), reverse=reverse)
        self._repopulate_device_table(devices)

    def _on_page_prev(self, _sender, _app_data):
        """Handle Prev page button click."""
        if self._page_index > 0:
            self._page_index -= 1
            self._render_device_page()

    def _on_page_next(self, _sender, _app_data):
        """Handle Next page button click."""
        total = len(self._sorted_devices)
        total_pages = max(1, (total + self._page_size - 1) // self._page_size)
        if self._page_index < total_pages - 1:
            self._page_index += 1
            self._render_device_page()
        elif self._has_more_api_data:
            # On last page and more API data exists — fetch next batch
            self._async_load_more()

    def _on_page_size_change(self, _sender, app_data):
        """Handle page size combo change."""
        try:
            self._page_size = int(app_data)
        except ValueError:
            return
        self._page_index = 0
        self._render_device_page()

    def _on_fetch_audit(self, _sender, _app_data):
        """Fetch the audit report in a background thread and display it."""
        def _fmt(v):
            """Return a readable, indented string for any value."""
            if isinstance(v, (dict, list)):
                return json.dumps(v, indent=4, default=str)
            return str(v)

        def _worker():
            audit = self.client.fetch_audit()
            if not audit:
                dpg.set_value("audit_text", "No audit data returned or not authenticated.")
                return
            lines = []
            resources = audit.get("resources") or []
            if resources:
                for idx, entry in enumerate(resources, 1):
                    lines.append("=" * 50)
                    lines.append(f"  Audit Entry {idx} of {len(resources)}")
                    lines.append("=" * 50)
                    for k, v in entry.items():
                        if isinstance(v, (dict, list)):
                            lines.append(f"  {k}:")
                            for line in _fmt(v).splitlines():
                                lines.append(f"    {line}")
                        else:
                            lines.append(f"  {k}: {v}")
                    lines.append("")
            else:
                errors = audit.get("errors") or []
                if errors:
                    lines.append("API Error:")
                    for e in errors:
                        code = e.get("code", "")
                        msg = e.get("message", str(e))
                        lines.append(f"  [{code}] {msg}")
                else:
                    lines.append("No audit entries returned.")
            dpg.set_value("audit_text", "\n".join(lines))

        threading.Thread(target=_worker, daemon=True).start()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    """Parse CLI arguments and launch the ZTA Score Viewer application."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-k", "--client_id",
        default="",
        help="Falcon API client ID (overrides FALCON_CLIENT_ID env var)",
    )
    parser.add_argument(
        "-s", "--client_secret",
        default="",
        help="Falcon API client secret (overrides FALCON_CLIENT_SECRET env var)",
    )
    args = parser.parse_args()

    app = ZTAScoreViewerApp(
        client_id=args.client_id,
        client_secret=args.client_secret,
    )
    app.run()


if __name__ == "__main__":
    main()
