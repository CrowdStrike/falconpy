r"""Spotlight Vulnerability Dashboard — Desktop GUI.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |             FalconPy
`-------'                         `-------'

  _____ ____    ___   ______  _      ____   ____  __ __  ______
 / ___/|    \  /   \ |      T| T    l    j /    T|  T  T|      T
(   \_ |  o  )Y     Y|      || |     |  T Y   __j|  l  ||      |
 \__  T|   _/ |  O  |l_j  l_j| l___  |  | |  T  ||  _  |l_j  l_j
 /  \ ||  |   |     |  |  |  |     T |  | |  l_ ||  |  |  |  |
 \    ||  |   l     !  |  |  |     | j  l |     ||  |  |  |  |
  \___jl__j    \___/   l__j  l_____j|____jl___,_jl__j__j  l__j

 __ __  __ __  _      ____       ___     ____  _____ __ __  ____    ___    ____  ____   ___
|  T  ||  T  T| T    |    \     |   \   /    T/ ___/|  T  T|    \  /   \  /    T|    \ |   \
|  |  ||  |  || |    |  _  Y    |    \ Y  o  (   \_ |  l  ||  o  )Y     YY  o  ||  D  )|    \
|  |  ||  |  || l___ |  |  |    |  D  Y|     |\__  T|  _  ||     T|  O  ||     ||    / |  D  Y
l  :  !|  :  ||     T|  |  |    |     ||  _  |/  \ ||  |  ||  O  ||     ||  _  ||    \ |     |
 \   / l     ||     ||  |  |    |     ||  |  |\    ||  |  ||     |l     !|  |  ||  .  Y|     |
  \_/   \__,_jl_____jl__j__j    l_____jl__j__j \___jl__j__jl_____j \___/ l__j__jl__j\_jl_____j

                    Spotlight Vulnerability Dashboard — Desktop GUI
                    Uses: SpotlightVulnerabilities, Hosts
                    Scope: spotlight-vulnerabilities:read, hosts:read

An interactive PySide6 desktop application for browsing and triaging Falcon
Spotlight vulnerabilities across a protected fleet.

Credentials are accepted at runtime (dialog or environment variables).  They
are never written to disk or emitted in any log output.

Architecture
------------
The application is split into three concerns:

1. FalconDataLayer — pure Python, no Qt imports.  All FalconPy SDK calls
   live here, making it fully unit-testable without a display.  Pagination is
   pipelined via a single-worker ThreadPoolExecutor so the HTTP request for
   the next page starts as soon as the previous cursor token is available.

2. VulnLoader — thin QThread wrapper around FalconDataLayer.  Emits
   page_loaded after each API page (enabling incremental table population)
   and finished / stopped / auth_error / general_error on completion.
   All signal emissions cross the thread boundary to the UI thread.

3. DashboardWindow — QMainWindow owning all widgets.  Divided into:
   - Query panel (left): FQL-generating controls + Search/Cancel.
   - View filter panel (left, below query): in-memory severity/CVE/hostname/OS
     filters that operate on already-loaded records without hitting the API.
   - Table (right): sortable QTableWidget with double-click CVE details.
   - Chart (right, optional): matplotlib severity breakdown bar chart.
   - Status bar: record count + last refresh timestamp.

Filter model
------------
There are two distinct filter stages:

* Query filters (Search Parameters panel) — translated into an FQL string
  and sent to the Spotlight API.  Changing these and clicking Search triggers a
  new API call.  These filter at the source.

* View filters (View Filters panel) — operate in memory on the records
  already loaded; no API call is made.  Instant regardless of dataset size.

Threading
---------
API calls run in a VulnLoader QThread.  Results are posted back to the main
thread via Qt signals, keeping the UI responsive at all times.

Usage
-----
    python3 spotlight_vuln_dashboard.py [--region {us1,us2,eu1,usgov1,usgov2,auto}]
                                        [-k FALCON_CLIENT_ID]
                                        [-s FALCON_CLIENT_SECRET]

Environment variables (optional — skips credential dialog)
    FALCON_CLIENT_ID
    FALCON_CLIENT_SECRET

CLI arguments take precedence over environment variables.
"""

import argparse
import csv
import os
import re
import threading
import time
from concurrent.futures import CancelledError, Future, ThreadPoolExecutor
from dataclasses import dataclass
from datetime import date, datetime
from typing import Dict, List, Optional

# pylint: disable=import-error
from PySide6.QtCore import QDate, Qt, QThread, QTimer, QUrl, Signal
from PySide6.QtGui import QBrush, QColor, QDesktopServices, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFileDialog,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSplitter,
    QStatusBar,
    QTableWidget,
    QTableWidgetItem,
    QToolBox,
    QVBoxLayout,
    QWidget,
)

from falconpy import Hosts, SpotlightVulnerabilities  # pylint: disable=import-error
# pylint: enable=import-error

# ---------------------------------------------------------------------------
# Optional matplotlib dependency — chart is hidden gracefully when absent.
# ---------------------------------------------------------------------------
try:
    import matplotlib

    matplotlib.use("QtAgg")
    from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
    from matplotlib.figure import Figure

    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CVE_ID_PATTERN = re.compile(r"^CVE-\d{4}-\d{4,}$")
NVD_BASE_URL = "https://nvd.nist.gov/vuln/detail/"

# Table foreground colour per severity level.
SEVERITY_COLORS: Dict[str, str] = {
    "CRITICAL": "#d32f2f",
    "HIGH": "#e65100",
    "MEDIUM": "#f9a825",
    "LOW": "#388e3c",
    "UNKNOWN": "#757575",
}

# Canonical OS platform values used by both the query-filter combo (FQL) and
# the view-filter combo (in-memory).  Must match the values returned by the
# Spotlight API in host_info.platform_name.
_OS_PLATFORMS: List[str] = [
    "Windows",
    "Linux",
    "macOS",
    "iOS",
    "Android",
    "ChromeOS",
]

VALID_REGIONS = ("us1", "us2", "eu1", "usgov1", "usgov2", "auto")

# Spotlight API maximum results per combined-query page.
SPOTLIGHT_PAGE_LIMIT = 400

# Maximum host IDs per Hosts.get_device_details batch call.
HOST_BATCH_SIZE = 100

# HTTP 429 retry configuration.
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 2  # seconds; doubled on each subsequent attempt


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class VulnRecord:
    """Normalised representation of a single Spotlight vulnerability finding.

    All string fields default to empty string rather than ``None`` so table
    widgets and CSV export can use them without additional null-checks.

    Attributes:
        vuln_id: Spotlight internal vulnerability ID (Falcon-generated UUID).
        cve_id: CVE identifier (e.g. ``"CVE-2024-1234"``), or ``"UNKNOWN"``.
        severity: Severity label uppercased: CRITICAL / HIGH / MEDIUM / LOW /
            UNKNOWN.  Uppercased at parse time so comparison with
            ``SEVERITY_COLORS`` keys is always consistent.
        cvss_score: CVSS base score as a string (e.g. ``"9.8"``), or ``""``
            when the API does not supply one.
        host_id: CrowdStrike agent ID (AID) of the affected host.
        hostname: Human-readable hostname.  Falls back to ``host_id`` when
            ``host_info.hostname`` is absent in the API response; may be
            further enriched by :meth:`FalconDataLayer._enrich_hostnames`.
        os_platform: Platform name (e.g. ``"Linux"``, ``"Windows"``), or ``""``
            when absent.  Enriched by the Hosts API when available.
        remediation_status: Remediation status string: ``"open"``,
            ``"closed"``, or ``"superseded"`` (derived from the
            ``is_superseded`` flag in the remediation facet).
        first_seen: ISO-8601 timestamp string when the vulnerability was first
            observed (maps to ``created_timestamp`` in the API response).
        last_seen: ISO-8601 timestamp string when the vulnerability was last
            seen (maps to ``updated_timestamp``).
    """

    vuln_id: str
    cve_id: str
    severity: str
    cvss_score: str
    host_id: str
    hostname: str
    os_platform: str
    remediation_status: str
    first_seen: str
    last_seen: str


# ---------------------------------------------------------------------------
# Data layer — no Qt imports; unit-testable without a display.
# ---------------------------------------------------------------------------


class FalconDataLayer:
    """Handles all FalconPy SDK interactions.

    Intentionally free of Qt imports so it can be instantiated and unit-tested
    without a display server.  The :class:`VulnLoader` QThread owns an instance
    and calls :meth:`get_vulnerabilities_paged` from its worker thread.

    Credentials are stored only in memory as instance attributes and are never
    written to disk or included in log messages.

    Raises at construction time on bad credentials so callers can handle the
    failure before building any UI.

    Attributes:
        _spotlight: FalconPy ``SpotlightVulnerabilities`` service collection.
        _hosts: FalconPy ``Hosts`` service collection used for hostname
            enrichment (requires Hosts: READ scope).
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        region: str = "auto",
    ) -> None:
        """Initialise SDK clients and immediately validate credentials.

        Args:
            client_id: Falcon API client identifier.
            client_secret: Falcon API client secret.
            region: Cloud region keyword or "auto" (default).

        Raises:
            ValueError: Credentials rejected by the API (HTTP 401).
            RuntimeError: Probe failed for a non-authentication reason.
        """
        if region == "auto":
            base_url = "https://api.crowdstrike.com"
        else:
            base_url = f"https://api.{region}.crowdstrike.com"

        self._spotlight = SpotlightVulnerabilities(
            client_id=client_id,
            client_secret=client_secret,
            base_url=base_url,
        )
        self._hosts = Hosts(
            client_id=client_id,
            client_secret=client_secret,
            base_url=base_url,
        )

        # Fail fast: verify credentials before the caller builds any UI.
        self._validate_credentials()

    def _validate_credentials(self) -> None:
        """Probe the Spotlight API with a minimal query to verify credentials.

        Raises:
            ValueError: On HTTP 401 (authentication failure).
            RuntimeError: On any other non-success response.
        """
        response = self._spotlight.query_vulnerabilities(
            filter="status:'open'",
            limit=1,
        )
        status_code = response.get("status_code", 0)
        if status_code == 401:
            raise ValueError(
                "Authentication failed (HTTP 401). "
                "Verify CLIENT_ID and CLIENT_SECRET."
            )
        if status_code not in (200, 201):
            errors = response.get("body", {}).get("errors") or []
            msg = (
                errors[0].get("message", "Unknown error") if errors else "Unknown error"
            )
            raise RuntimeError(f"API probe failed (HTTP {status_code}): {msg}")

    def _call_with_retry(self, fn, *args, **kwargs):
        """Invoke a FalconPy SDK method with exponential-backoff on HTTP 429.

        Args:
            fn: Callable SDK method to invoke.
            *args: Positional arguments forwarded to fn.
            **kwargs: Keyword arguments forwarded to fn.

        Returns:
            The raw SDK response dict on success.

        Raises:
            ValueError: On HTTP 401 (credentials expired or revoked).
            RuntimeError: On rate-limit exhaustion or any other API error.
        """
        for attempt in range(MAX_RETRIES):
            response = fn(*args, **kwargs)
            status_code = response.get("status_code", 0)

            if status_code == 429:
                if attempt < MAX_RETRIES - 1:
                    wait = RETRY_BACKOFF_BASE ** attempt
                    time.sleep(wait)
                    continue
                raise RuntimeError(
                    "API rate limit exceeded after retries. "
                    "Wait a moment then click Refresh."
                )

            if status_code == 401:
                raise ValueError("Credentials expired or revoked (HTTP 401).")

            if status_code not in (200, 201):
                errors = response.get("body", {}).get("errors") or []
                msg = (
                    errors[0].get("message", "Unknown error")
                    if errors
                    else "Unknown error"
                )
                raise RuntimeError(f"API error (HTTP {status_code}): {msg}")

            return response

        raise RuntimeError("Maximum retries exceeded.")

    def get_vulnerabilities(self) -> List[VulnRecord]:
        """Retrieve all open vulnerabilities (blocking, no progress callbacks).

        Delegates to :meth:`get_vulnerabilities_paged` with a no-op callback.
        Retained for backward compatibility with tests and callers that do not
        need per-page progress notifications.

        Returns:
            List of VulnRecord instances for all open vulnerabilities.

        Raises:
            ValueError: On authentication failure.
            RuntimeError: On rate-limit exhaustion or other API errors.
        """
        return self.get_vulnerabilities_paged(on_page=lambda *_: None)

    def get_vulnerabilities_paged(
        self,
        on_page,
        stop_event: Optional[threading.Event] = None,
        fql_filter: str = "status:'open'",
    ) -> List[VulnRecord]:
        """Retrieve vulnerabilities matching *fql_filter*, calling *on_page* after each page.

        Uses a ``ThreadPoolExecutor`` to pipeline page fetches: the HTTP request
        for page N+1 starts as soon as page N's cursor is known, overlapping
        network I/O with result processing.  Because the Spotlight API uses
        opaque cursor tokens (each cursor is derived from the previous response),
        true parallel dispatch is not possible; the pipeline is the maximum
        achievable concurrency for cursor-based pagination.

        Args:
            on_page: Callable invoked after each page is parsed, with signature
                ``on_page(page_records, page_number, cumulative_total)``.
            stop_event: Optional :class:`threading.Event`.  When set, stops
                fetching new pages after the current in-flight request resolves.
            fql_filter: FQL filter string sent to the Spotlight API.  Defaults
                to ``"status:'open'"`` for backward compatibility.

        Returns:
            Fully enriched list of all VulnRecord instances (or partial list if
            *stop_event* was set).

        Raises:
            ValueError: On authentication failure.
            RuntimeError: On rate-limit exhaustion or other API errors.
        """
        records: List[VulnRecord] = []
        host_id_set: Dict[str, None] = {}
        page_number = 0

        def _fetch(after_token: Optional[str]) -> dict:
            """Submit one Spotlight page request and return the raw response."""
            kwargs: dict = {
                "filter": fql_filter,
                "facet": ["host_info", "cve", "remediation"],
                "limit": SPOTLIGHT_PAGE_LIMIT,
            }
            if after_token:
                kwargs["after"] = after_token
            return self._call_with_retry(
                self._spotlight.query_vulnerabilities_combined, **kwargs
            )

        def _parse_response(response: dict) -> tuple:
            """Parse a raw Spotlight response into (page_records, next_cursor)."""
            body = response.get("body", {})
            resources = body.get("resources") or []
            meta = body.get("meta") or {}
            pagination = meta.get("pagination") or {}
            next_after = pagination.get("after") if resources else None

            page_recs: List[VulnRecord] = []
            for item in resources:
                cve = item.get("cve") or {}
                host_info = item.get("host_info") or {}
                remediation = item.get("remediation") or {}

                host_id = item.get("aid", "")
                if host_id:
                    host_id_set[host_id] = None

                if remediation.get("is_superseded"):
                    status_str = "superseded"
                else:
                    status_str = item.get("status", "open")

                page_recs.append(
                    VulnRecord(
                        vuln_id=item.get("id", ""),
                        cve_id=cve.get("id", "UNKNOWN"),
                        severity=cve.get("severity", "UNKNOWN").upper(),
                        cvss_score=str(cve.get("base_score") or ""),
                        host_id=host_id,
                        hostname=host_info.get("hostname") or host_id,
                        os_platform=host_info.get("platform") or "",
                        remediation_status=status_str,
                        first_seen=item.get("created_timestamp", ""),
                        last_seen=item.get("updated_timestamp", ""),
                    )
                )
            return page_recs, next_after

        executor = ThreadPoolExecutor(max_workers=1)
        try:
            # Submit the first page fetch immediately.
            # max_workers=1 is intentional: Spotlight pagination is cursor-based
            # (each cursor comes from the previous response), so true parallel
            # fetching is impossible.  A single worker overlaps the *next* HTTP
            # request with the *current* page's parse/notify work, which is the
            # maximum pipeline depth achievable under cursor pagination.
            pending: Future = executor.submit(_fetch, None)
            _after_token: Optional[str] = None

            while True:
                # Poll with a short timeout so a stop request is honoured within
                # ~100 ms rather than waiting for the full HTTP response.
                while True:
                    if stop_event is not None and stop_event.is_set():
                        pending.cancel()
                        break
                    try:
                        response = pending.result(timeout=0.1)
                        break
                    except CancelledError:
                        break  # future was cancelled; treat as stop
                    except TimeoutError:
                        continue  # keep polling

                # If stop was requested while waiting, abandon pagination.
                if stop_event is not None and stop_event.is_set():
                    break

                page_recs, next_after = _parse_response(response)

                # Pre-flight stop check: if stop was requested, abandon before
                # submitting the next page and before notifying the caller.
                if stop_event is not None and stop_event.is_set():
                    break

                # Submit the next page fetch while we process the current page.
                if next_after:
                    pending = executor.submit(_fetch, next_after)

                page_number += 1
                records.extend(page_recs)

                if page_recs:
                    on_page(page_recs, page_number, len(records))

                if not next_after:
                    break

                _after_token = next_after  # noqa: F841  (kept for clarity)

                # Post-processing stop check: avoid submitting the just-queued
                # next fetch if a stop was requested while we were processing.
                if stop_event is not None and stop_event.is_set():
                    pending.cancel()
                    break
        finally:
            # cancel_futures=True drops any pending (not-yet-running) futures.
            # wait=False means we do not block waiting for the currently-running
            # worker thread (an in-flight HTTP request) to finish — it will
            # complete and be garbage-collected once the response arrives.
            executor.shutdown(wait=False, cancel_futures=True)

        missing = list(host_id_set.keys())
        if missing and not (stop_event is not None and stop_event.is_set()):
            self._enrich_hostnames(records, missing)

        return records

    def _enrich_hostnames(
        self,
        records: List[VulnRecord],
        host_ids: List[str],
    ) -> None:
        """Back-fill hostname and OS fields from the Hosts API.

        Operates in place on *records*.  Failures are silently suppressed so
        that a missing Hosts: READ scope degrades gracefully (agent IDs are
        shown instead of hostnames) rather than aborting the vulnerability load.

        Args:
            records: Vulnerability records to enrich.
            host_ids: Agent IDs to look up.
        """
        host_map: Dict[str, dict] = {}

        for i in range(0, len(host_ids), HOST_BATCH_SIZE):
            batch = host_ids[i : i + HOST_BATCH_SIZE]
            try:
                resp = self._call_with_retry(
                    self._hosts.get_device_details, ids=batch
                )
                for device in resp.get("body", {}).get("resources") or []:
                    aid = device.get("device_id", "")
                    host_map[aid] = {
                        "hostname": device.get("hostname") or aid,
                        "os_platform": device.get("platform_name") or "",
                    }
            except (ValueError, RuntimeError):
                # Enrichment is best-effort; abort remaining batches on error.
                break

        for record in records:
            if record.host_id in host_map:
                info = host_map[record.host_id]
                if record.hostname == record.host_id:
                    record.hostname = info["hostname"]
                if not record.os_platform:
                    record.os_platform = info["os_platform"]


# ---------------------------------------------------------------------------
# CVE ID normalisation helper — module-level so it is testable independently.
# ---------------------------------------------------------------------------


def normalise_cve_id(raw: str) -> str:
    """Normalise a user-supplied CVE ID string to ``CVE-YYYY-NNNNN`` form.

    Accepts all of the following input forms (case-insensitive):

    - ``CVE-2024-12345``      → returned as-is (uppercased)
    - ``2024-12345``          → ``CVE-2024-12345``
    - ``2024 12345``          → ``CVE-2024-12345``

    Returns an empty string when the input cannot be parsed into a valid CVE
    ID so callers can treat that as "no CVE filter".

    Args:
        raw: Raw string entered by the user.

    Returns:
        Normalised ``CVE-YYYY-NNNNN`` string, or ``""`` if unparseable.
    """
    raw = raw.strip().upper()
    if not raw:
        return ""
    # Already canonical form.
    if CVE_ID_PATTERN.match(raw):
        return raw
    # Bare YYYY-NNNNN or YYYY NNNNN.
    m = re.match(r"^(\d{4})[-\s](\d{4,})$", raw)
    if m:
        return f"CVE-{m.group(1)}-{m.group(2)}"
    return ""


# ---------------------------------------------------------------------------
# FQL builder — module-level so it is testable without Qt.
# ---------------------------------------------------------------------------

_FQL_INJECTION_RE = re.compile(r"['\"]")


def _build_fql(
    *,
    status: str = "open",
    cve_id: str = "",
    severity: str = "",
    cvss_min: float = 0.0,
    cvss_max: float = 10.0,
    created_after: str = "",
    created_before: str = "",
) -> str:
    """Build a Spotlight FQL filter string from UI widget values.

    All string inputs are sanitised: single-quotes and double-quotes are
    stripped to prevent FQL injection.

    Args:
        status: Remediation status — ``"open"``, ``"closed"``, or ``""``
            for no status filter.
        cve_id: CVE ID fragment to match (partial allowed); already
            normalised by ``normalise_cve_id()`` before being passed here.
        severity: Severity level — ``"CRITICAL"``, ``"HIGH"``, etc., or
            ``""`` for no severity filter.
        cvss_min: Minimum CVSS score (inclusive).
        cvss_max: Maximum CVSS score (inclusive).
        created_after: ISO date string ``YYYY-MM-DD`` for lower bound on
            ``created_timestamp``, or ``""`` to omit.
        created_before: ISO date string ``YYYY-MM-DD`` for upper bound, or
            ``""`` to omit.

    Returns:
        FQL filter string, e.g.
        ``"status:'open'+cve.id:'CVE-2024-*'+cve.base_score:>=7.0"``.
        Returns ``""`` when no filters are active (Spotlight returns all
        records).
    """

    def _sanitise(s: str) -> str:
        return _FQL_INJECTION_RE.sub("", s)

    parts: List[str] = []

    if status:
        parts.append(f"status:'{_sanitise(status)}'")

    if cve_id:
        safe_cve = _sanitise(cve_id)
        # Append wildcard to support partial prefix matches (e.g. CVE-2024-*).
        if not safe_cve.endswith("*"):
            safe_cve += "*"
        parts.append(f"cve.id:'{safe_cve}'")

    if severity:
        parts.append(f"cve.severity:'{_sanitise(severity)}'")

    # CVSS range — only emit when non-default.
    if cvss_min > 0.0:
        parts.append(f"cve.base_score:>={cvss_min:.1f}")
    if cvss_max < 10.0:
        parts.append(f"cve.base_score:<={cvss_max:.1f}")

    if created_after:
        parts.append(f"created_timestamp:>'{_sanitise(created_after)}T00:00:00Z'")
    if created_before:
        parts.append(f"created_timestamp:<'{_sanitise(created_before)}T23:59:59Z'")

    return "+".join(parts)


# ---------------------------------------------------------------------------
# CSV formula-injection helper — module-level so it is testable without a
# display and without instantiating any Qt class.
# ---------------------------------------------------------------------------


def safe_csv_value(value: str) -> str:
    """Wrap *value* in ``="…"`` syntax to prevent CSV formula injection.

    Spreadsheet applications (Excel, Sheets) evaluate cells starting with
    ``=``, ``+``, ``-``, or ``@`` as formulas.  Wrapping the value as
    ``="<value>"`` forces evaluation to a static string even if the raw
    value begins with one of those characters.

    Double-quote characters inside *value* are escaped as ``""`` (the
    standard CSV double-quote escape) before the outer ``="…"`` wrapper is
    applied, so a value like ``foo"bar`` becomes ``="foo""bar"`` rather than
    producing malformed CSV.

    Args:
        value: The raw string value to protect.

    Returns:
        A formula-safe string ready for ``csv.writer``.
    """
    escaped = value.replace('"', '""')
    return f'="{escaped}"'


# ---------------------------------------------------------------------------
# Background worker thread
# ---------------------------------------------------------------------------


class VulnLoader(QThread):
    """QThread that loads vulnerability data from the Spotlight API.

    Emits ``page_loaded`` after each API page so the UI can populate
    incrementally.  Emits ``finished`` when all pages complete normally, or
    ``stopped`` when a stop was requested mid-load (cancelled search).  Emits
    ``auth_error`` on HTTP 401 and ``general_error`` on any other failure.
    All signal emissions occur from the worker thread; connected slots execute
    on the receiving thread (typically the main/UI thread).

    Call :meth:`request_stop` to signal the worker to abandon further page
    fetches after the current in-flight request completes.

    Signals:
        page_loaded(list, int, int): Emitted after each page; args are
            ``(page_records, page_number, cumulative_total)``.
        finished(list, float): All pages + enrichment done; args are
            ``(all_records, elapsed_seconds)``.
        stopped(list, float): Load was cancelled mid-way; args are
            ``(partial_records, elapsed_seconds)``.
        auth_error(str): HTTP 401 received; arg is the error message.
        general_error(str): Other API error; arg is the error message.
    """

    # Emitted after each page: (page_records, page_number, cumulative_total)
    page_loaded = Signal(list, int, int)
    # Emitted when all pages + enrichment complete: (all_records, elapsed_secs)
    finished = Signal(list, float)
    # Emitted when load was cancelled mid-way: (partial_records, elapsed_secs)
    stopped = Signal(list, float)
    auth_error = Signal(str)
    general_error = Signal(str)

    def __init__(
        self,
        data_layer: "FalconDataLayer",
        fql_filter: str = "status:'open'",
        parent=None,
    ) -> None:
        """Initialise the loader with a data layer and FQL filter string.

        Args:
            data_layer: Authenticated :class:`FalconDataLayer` instance.
            fql_filter: FQL filter string to pass to the Spotlight API.
                Built by :meth:`DashboardWindow._collect_fql`.
            parent: Optional Qt parent object for ownership/cleanup.
        """
        super().__init__(parent)
        self._data_layer = data_layer
        self._fql_filter = fql_filter
        # threading.Event is used (not a Qt mechanism) because it must be
        # checked inside get_vulnerabilities_paged which has no Qt event loop.
        self._stop_event = threading.Event()

    def request_stop(self) -> None:
        """Signal the worker to stop after the current in-flight page resolves."""
        self._stop_event.set()

    def run(self) -> None:
        """Fetch vulnerabilities page-by-page, emitting page_loaded after each.

        Runs on the worker thread.  Signals are emitted here and dispatched to
        slots on the main thread by Qt's queued connection mechanism.
        """
        start = time.monotonic()
        try:
            records = self._data_layer.get_vulnerabilities_paged(
                on_page=self.page_loaded.emit,
                stop_event=self._stop_event,
                fql_filter=self._fql_filter,
            )
            elapsed = time.monotonic() - start
            # Distinguish a normal finish from a user-initiated cancel so the
            # UI can display an appropriate status message for each case.
            if self._stop_event.is_set():
                self.stopped.emit(records, elapsed)
            else:
                self.finished.emit(records, elapsed)
        except ValueError as exc:
            self.auth_error.emit(str(exc))
        except RuntimeError as exc:
            self.general_error.emit(str(exc))


# ---------------------------------------------------------------------------
# Credential dialog
# ---------------------------------------------------------------------------


class CredentialDialog(QDialog):
    """Modal dialog for entering CrowdStrike API credentials.

    After exec() returns, check ``self.result``:
    - ``None``: the user cancelled.
    - ``dict``: keys are ``client_id``, ``client_secret``, and ``region``.
    """

    def __init__(self, parent=None, region_default: str = "auto") -> None:
        super().__init__(parent)
        self.setWindowTitle("Falcon API Credentials")
        self.setModal(True)
        self.setMinimumWidth(420)

        self._cred_result: Optional[dict] = None
        self._build_ui(region_default)
        self._prefill_from_env()

    @property
    def result(self) -> Optional[dict]:
        """Credential dict on success, None if the user cancelled."""
        return self._cred_result

    def _build_ui(self, region_default: str) -> None:
        """Lay out credential entry fields and action buttons."""
        form = QFormLayout()

        self._id_edit = QLineEdit()
        self._id_edit.setPlaceholderText("Enter Client ID")
        form.addRow("Client ID:", self._id_edit)

        self._secret_edit = QLineEdit()
        self._secret_edit.setEchoMode(QLineEdit.Password)
        self._secret_edit.setPlaceholderText("Enter Client Secret")
        form.addRow("Client Secret:", self._secret_edit)

        self._region_combo = QComboBox()
        self._region_combo.addItems(list(VALID_REGIONS))
        self._region_combo.setCurrentText(region_default)
        form.addRow("Region:", self._region_combo)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self._on_accept)
        buttons.rejected.connect(self.reject)

        outer = QVBoxLayout()
        outer.addLayout(form)
        outer.addWidget(buttons)
        self.setLayout(outer)

    def _prefill_from_env(self) -> None:
        """Populate fields from environment variables when available."""
        env_id = os.environ.get("FALCON_CLIENT_ID", "")
        env_secret = os.environ.get("FALCON_CLIENT_SECRET", "")
        if env_id:
            self._id_edit.setText(env_id)
        if env_secret:
            self._secret_edit.setText(env_secret)

    def _on_accept(self) -> None:
        """Validate inputs, store result, and close."""
        client_id = self._id_edit.text().strip()
        client_secret = self._secret_edit.text().strip()
        if not client_id or not client_secret:
            QMessageBox.warning(
                self,
                "Missing credentials",
                "Client ID and Client Secret are both required.",
            )
            return
        self._cred_result = {
            "client_id": client_id,
            "client_secret": client_secret,
            "region": self._region_combo.currentText(),
        }
        self.accept()


# ---------------------------------------------------------------------------
# CVE detail dialog
# ---------------------------------------------------------------------------


class CveDetailDialog(QDialog):
    """Non-modal dialog showing full CVE detail for a double-clicked table row.

    Opened by :meth:`DashboardWindow._on_cell_double_clicked`.  Multiple
    instances can be open simultaneously — each is independent and destroys
    itself when closed (``Qt.WA_DeleteOnClose``).
    """

    def __init__(self, rec: "VulnRecord", parent=None) -> None:
        """Build the detail dialog for *rec*.

        Args:
            rec: The vulnerability record whose fields are displayed.
            parent: Optional Qt parent widget (typically the main window).
        """
        super().__init__(parent)
        self.setWindowTitle(f"CVE Detail — {rec.cve_id}")
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setMinimumWidth(400)

        form = QFormLayout()
        for label, value in [
            ("CVE ID", rec.cve_id),
            ("Severity", rec.severity),
            ("CVSS Score", rec.cvss_score),
            ("Hostname", rec.hostname),
            ("OS Platform", rec.os_platform),
            ("Status", rec.remediation_status),
            ("First Seen", rec.first_seen),
            ("Last Seen", rec.last_seen),
        ]:
            lbl = QLabel(value)
            lbl.setTextInteractionFlags(Qt.TextSelectableByMouse)
            form.addRow(f"{label}:", lbl)

        nvd_btn = QPushButton("Open in NVD")
        nvd_btn.clicked.connect(self._open_nvd)
        self._cve_id = rec.cve_id

        buttons = QDialogButtonBox(QDialogButtonBox.Close)
        buttons.rejected.connect(self.close)

        outer = QVBoxLayout()
        outer.addLayout(form)
        outer.addWidget(nvd_btn)
        outer.addWidget(buttons)
        self.setLayout(outer)

    def _open_nvd(self) -> None:
        """Open the NVD page for this CVE in the system browser."""
        if CVE_ID_PATTERN.match(self._cve_id):
            QDesktopServices.openUrl(QUrl(NVD_BASE_URL + self._cve_id))


# ---------------------------------------------------------------------------
# Table column definitions
# ---------------------------------------------------------------------------

_COLUMNS = [
    ("cve_id", "CVE ID", 155),
    ("severity", "Severity", 78),
    ("cvss_score", "CVSS", 54),
    ("hostname", "Hostname", 185),
    ("os_platform", "OS", 90),
    ("remediation_status", "Status", 90),
    ("first_seen", "First Seen", 155),
    ("last_seen", "Last Seen", 155),
]


# ---------------------------------------------------------------------------
# Main window
# ---------------------------------------------------------------------------


class DashboardWindow(QMainWindow):
    """Falcon Spotlight Vulnerability Dashboard main window.

    Owns the full widget hierarchy and coordinates between the background
    :class:`VulnLoader` thread and the UI.  Notable design decisions:

    * **Two-panel left sidebar**: *Query panel* (FQL-generating controls) sits
      above *View filter panel* (in-memory filters).  Both are wrapped in a
      ``QScrollArea`` so they remain accessible on small screens.
    * **Incremental loading**: :meth:`_on_page_loaded` appends rows as each
      API page arrives so the table fills progressively rather than all at once.
    * **Full-replace on finish**: :meth:`_on_refresh_success` replaces all rows
      after enrichment completes so that back-filled hostnames are shown.
    * **Cancel/restart**: :meth:`_on_search_clicked` stops any running loader
      before starting a new one, preventing concurrent loads.

    Attributes:
        _default_region: Cloud region passed to :class:`FalconDataLayer` and
            pre-selected in the credential dialog.
        _prefilled_client_id: Client ID resolved from CLI args or env var; when
            both id and secret are set the credential dialog is skipped.
        _prefilled_client_secret: Client secret resolved from CLI args or env var.
        _data_layer: Active :class:`FalconDataLayer`, or ``None`` before first
            successful authentication.
        _all_records: Complete list of records from the last successful (or
            partial) load — used as the source for view filtering.
        _filtered_records: Subset of ``_all_records`` that passes the current
            view filters — maps 1-to-1 with visible table rows.
        _loader: The currently running (or most recently completed)
            :class:`VulnLoader` thread, or ``None``.
    """

    def __init__(
        self,
        default_region: str = "auto",
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ) -> None:
        """Initialise the main window.

        Args:
            default_region: Cloud region to pre-select in the credential dialog.
            client_id: Optional pre-resolved Falcon client ID (from CLI arg or
                env var). When both client_id and client_secret are provided the
                credential dialog is skipped entirely.
            client_secret: Optional pre-resolved Falcon client secret (same
                source precedence as client_id).
        """
        super().__init__()
        self.setWindowTitle("Falcon Spotlight Vulnerability Dashboard")
        self.resize(1280, 760)
        self.setMinimumSize(920, 550)

        self._default_region = default_region
        self._prefilled_client_id = client_id
        self._prefilled_client_secret = client_secret
        self._data_layer: Optional[FalconDataLayer] = None
        self._all_records: List[VulnRecord] = []
        self._filtered_records: List[VulnRecord] = []
        self._loader: Optional[VulnLoader] = None  # Active worker thread or None.

        self._build_ui()
        # Defer credential initialisation until the event loop is running.
        QTimer.singleShot(100, self._initialise_credentials)

    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------

    def _build_ui(self) -> None:
        """Construct the full window layout."""
        splitter = QSplitter(Qt.Horizontal)

        # Left column: fixed logo + accordion below.
        left_col = QWidget()
        left_col.setFixedWidth(270)
        left_col_layout = QVBoxLayout(left_col)
        left_col_layout.setContentsMargins(4, 6, 4, 4)
        left_col_layout.setSpacing(6)

        # Logo fixed above the accordion so it stays visible at all window heights.
        logo_label = QLabel()
        logo_label.setAlignment(Qt.AlignHCenter)
        logo_label.setContentsMargins(0, 8, 0, 10)
        logo_path = os.path.join(os.path.dirname(__file__), "..", "cs-logo-red.png")
        pixmap = QPixmap(logo_path)
        if not pixmap.isNull():
            pixmap = pixmap.scaledToWidth(230, Qt.SmoothTransformation)
            logo_label.setPixmap(pixmap)
        else:
            logo_label.setText("CrowdStrike")
            logo_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #E3001B;")
        left_col_layout.addWidget(logo_label)

        # QToolBox accordion: "Search Parameters" and "View Filters" as collapsible sections.
        self._toolbox = QToolBox()
        self._toolbox.addItem(self._make_query_panel(), "Search Parameters")
        self._toolbox.addItem(self._make_filter_panel(), "View Filters")
        left_col_layout.addWidget(self._toolbox, stretch=1)

        splitter.addWidget(left_col)
        splitter.setStretchFactor(0, 0)

        # Right: action bar + table + optional chart.
        right = QWidget()
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.addLayout(self._make_action_bar())
        right_layout.addWidget(self._make_table(), stretch=1)
        if MATPLOTLIB_AVAILABLE:
            right_layout.addWidget(self._make_chart())
        splitter.addWidget(right)
        splitter.setStretchFactor(1, 1)

        self.setCentralWidget(splitter)

        # Status bar.
        self._status_bar = QStatusBar()
        self._status_bar.showMessage("Ready — connect to load data.")
        self.setStatusBar(self._status_bar)

    def _make_query_panel(self) -> QWidget:
        """Build the 'Search Parameters' content widget: FQL-generating controls + Search/Cancel.

        Returns a plain QWidget suitable for use as a QToolBox item.
        The QToolBox tab label provides the section title.
        """
        panel = QWidget()
        form = QFormLayout(panel)
        form.setLabelAlignment(Qt.AlignRight)
        form.setContentsMargins(4, 4, 4, 4)

        # CVE ID — normalised on editing finished.
        self._q_cve_edit = QLineEdit()
        self._q_cve_edit.setPlaceholderText("e.g. CVE-2024-1234")
        self._q_cve_edit.editingFinished.connect(self._normalise_cve_input)
        form.addRow("CVE ID:", self._q_cve_edit)

        # OS platform combo.
        self._q_os_combo = QComboBox()
        self._q_os_combo.addItems(["All"] + _OS_PLATFORMS)
        form.addRow("OS:", self._q_os_combo)

        # Status combo.
        self._q_status_combo = QComboBox()
        self._q_status_combo.addItems(["All", "open", "closed"])
        self._q_status_combo.setCurrentText("open")
        form.addRow("Status:", self._q_status_combo)

        # Severity combo.
        self._q_severity_combo = QComboBox()
        self._q_severity_combo.addItems(
            ["All", "CRITICAL", "HIGH", "MEDIUM", "LOW", "UNKNOWN"]
        )
        form.addRow("Severity:", self._q_severity_combo)

        # CVSS range (two spin boxes on one row).
        cvss_row = QWidget()
        cvss_layout = QHBoxLayout(cvss_row)
        cvss_layout.setContentsMargins(0, 0, 0, 0)
        self._q_cvss_min = QDoubleSpinBox()
        self._q_cvss_min.setRange(0.0, 10.0)
        self._q_cvss_min.setSingleStep(0.1)
        self._q_cvss_min.setValue(0.0)
        self._q_cvss_min.setMinimumWidth(62)
        self._q_cvss_max = QDoubleSpinBox()
        self._q_cvss_max.setRange(0.0, 10.0)
        self._q_cvss_max.setSingleStep(0.1)
        self._q_cvss_max.setValue(10.0)
        self._q_cvss_max.setMinimumWidth(62)
        cvss_layout.addWidget(self._q_cvss_min)
        cvss_layout.addWidget(QLabel("–"))
        cvss_layout.addWidget(self._q_cvss_max)
        form.addRow("CVSS:", cvss_row)

        # Date field selector — maps to FQL timestamp fields supported by the
        # Spotlight combined endpoint: created_timestamp, updated_timestamp,
        # closed_timestamp.  (first_seen/last_seen are Hosts API fields and are
        # not valid Spotlight FQL filter fields.)
        self._q_date_field_combo = QComboBox()
        self._q_date_field_combo.addItems(["created", "updated", "closed"])
        form.addRow("Date field:", self._q_date_field_combo)

        # Date range pickers.
        today = QDate.currentDate()
        month_start = QDate(today.year(), today.month(), 1)

        self._q_date_from = QDateEdit(month_start)
        self._q_date_from.setCalendarPopup(True)
        self._q_date_from.setDisplayFormat("yyyy-MM-dd")
        form.addRow("From:", self._q_date_from)

        self._q_date_to = QDateEdit(today)
        self._q_date_to.setCalendarPopup(True)
        self._q_date_to.setDisplayFormat("yyyy-MM-dd")
        form.addRow("To:", self._q_date_to)

        # Warning label.
        warn_label = QLabel(
            "\u26a0 Large environments may return thousands of results. "
            "Set filters to narrow results before searching."
        )
        warn_label.setWordWrap(True)
        warn_label.setStyleSheet("color: #b8860b; font-size: 10px;")
        form.addRow(warn_label)

        # Search / Cancel buttons.
        btn_row = QWidget()
        btn_layout = QHBoxLayout(btn_row)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        self._search_btn = QPushButton("Search")
        self._search_btn.setDefault(True)
        self._search_btn.clicked.connect(self._on_search_clicked)
        self._cancel_btn = QPushButton("Cancel")
        self._cancel_btn.setEnabled(False)
        self._cancel_btn.clicked.connect(self._on_cancel_clicked)
        btn_layout.addWidget(self._search_btn)
        btn_layout.addWidget(self._cancel_btn)
        form.addRow(btn_row)

        return panel

    def _make_filter_panel(self) -> QWidget:
        """View Filters content widget: in-memory filters, disabled until first page loads.

        Returns a plain QWidget suitable for use as a QToolBox item.
        The QToolBox tab label provides the section title.
        """
        self._view_filter_group = QWidget()
        self._view_filter_group.setEnabled(False)
        layout = QVBoxLayout(self._view_filter_group)
        layout.setAlignment(Qt.AlignTop)

        # Severity checkboxes.
        sev_group = QGroupBox("Severity")
        sev_layout = QVBoxLayout(sev_group)
        self._severity_checks: Dict[str, QCheckBox] = {}
        for sev, color in SEVERITY_COLORS.items():
            cb = QCheckBox(sev)
            cb.setChecked(True)
            cb.setStyleSheet(f"color: {color}; font-weight: bold;")
            cb.stateChanged.connect(self._apply_filters)
            self._severity_checks[sev] = cb
            sev_layout.addWidget(cb)
        layout.addWidget(sev_group)

        # CVE search.
        search_group = QGroupBox("CVE Search")
        search_layout = QVBoxLayout(search_group)
        self._search_edit = QLineEdit()
        self._search_edit.setPlaceholderText("e.g. CVE-2024")
        self._search_edit.textChanged.connect(self._apply_filters)
        search_layout.addWidget(self._search_edit)
        layout.addWidget(search_group)

        # Hostname filter.
        host_group = QGroupBox("Hostname")
        host_layout = QVBoxLayout(host_group)
        self._hostname_edit = QLineEdit()
        self._hostname_edit.setPlaceholderText("e.g. web-prod")
        self._hostname_edit.textChanged.connect(self._apply_filters)
        host_layout.addWidget(self._hostname_edit)
        layout.addWidget(host_group)

        # OS filter (combo — populated from loaded data).
        os_group = QGroupBox("Operating System")
        os_layout = QVBoxLayout(os_group)
        self._os_combo = QComboBox()
        self._os_combo.addItems(["All"] + _OS_PLATFORMS)
        self._os_combo.currentTextChanged.connect(self._apply_filters)
        os_layout.addWidget(self._os_combo)
        layout.addWidget(os_group)

        clear_btn = QPushButton("Clear View Filters")
        clear_btn.clicked.connect(self._clear_filters)
        layout.addWidget(clear_btn)

        return self._view_filter_group

    def _make_action_bar(self) -> QHBoxLayout:
        """Refresh and Export CSV buttons."""
        hbox = QHBoxLayout()
        hbox.setContentsMargins(4, 4, 4, 2)

        self._refresh_btn = QPushButton("Refresh")
        self._refresh_btn.clicked.connect(self._start_refresh)
        hbox.addWidget(self._refresh_btn)

        export_btn = QPushButton("Export CSV")
        export_btn.clicked.connect(self._export_csv)
        hbox.addWidget(export_btn)

        hbox.addStretch()
        return hbox

    def _make_table(self) -> QTableWidget:
        """Scrollable table with sortable column headers."""
        self._table = QTableWidget()
        self._table.setColumnCount(len(_COLUMNS))
        self._table.setHorizontalHeaderLabels([col[1] for col in _COLUMNS])
        self._table.setEditTriggers(QTableWidget.NoEditTriggers)
        self._table.setSelectionBehavior(QTableWidget.SelectRows)
        self._table.setSelectionMode(QTableWidget.SingleSelection)
        self._table.setAlternatingRowColors(True)
        self._table.setSortingEnabled(True)
        self._table.verticalHeader().setVisible(False)

        header = self._table.horizontalHeader()
        for i, (_, _, width) in enumerate(_COLUMNS):
            self._table.setColumnWidth(i, width)
        header.setStretchLastSection(True)

        self._table.cellDoubleClicked.connect(self._on_cell_double_clicked)
        return self._table

    def _make_chart(self) -> QWidget:
        """Severity breakdown bar chart (only when matplotlib is installed)."""
        container = QGroupBox("Severity Breakdown")
        container.setMaximumHeight(180)
        layout = QVBoxLayout(container)

        self._fig = Figure(figsize=(8, 1.6), dpi=90, tight_layout=True)
        self._ax = self._fig.add_subplot(111)
        self._canvas = FigureCanvasQTAgg(self._fig)
        layout.addWidget(self._canvas)

        self._chart_widget = container
        return container

    # ------------------------------------------------------------------
    # Credential flow
    # ------------------------------------------------------------------

    def _initialise_credentials(self) -> None:
        """Connect with pre-resolved credentials or fall back to the dialog.

        If both client_id and client_secret were supplied (via CLI or env var),
        the credential dialog is skipped and the data layer is initialised
        directly.  Otherwise the dialog is shown so the user can supply them.
        """
        if self._prefilled_client_id and self._prefilled_client_secret:
            self._set_status("Connecting…")
            QApplication.processEvents()
            try:
                self._data_layer = FalconDataLayer(
                    client_id=self._prefilled_client_id,
                    client_secret=self._prefilled_client_secret,
                    region=self._default_region,
                )
            except ValueError as exc:
                QMessageBox.critical(self, "Authentication Failed", str(exc))
                self._set_status("Authentication failed. Click Refresh to retry.")
                return
            except RuntimeError as exc:
                QMessageBox.critical(self, "Connection Error", str(exc))
                self._set_status("Connection error. Click Refresh to retry.")
                return
            self._set_status("Connected. Press Search to load vulnerabilities.")
        else:
            self._prompt_credentials()

    def _prompt_credentials(self) -> None:
        """Show the credential dialog and initialise the data layer on success."""
        dlg = CredentialDialog(self, region_default=self._default_region)
        if dlg.exec() != QDialog.Accepted or dlg.result is None:
            self._set_status("Not connected. Click Refresh to enter credentials.")
            return

        creds = dlg.result
        self._set_status("Connecting…")
        QApplication.processEvents()

        try:
            self._data_layer = FalconDataLayer(
                client_id=creds["client_id"],
                client_secret=creds["client_secret"],
                region=creds["region"],
            )
        except ValueError as exc:
            QMessageBox.critical(self, "Authentication Failed", str(exc))
            self._set_status("Authentication failed. Click Refresh to retry.")
            return
        except RuntimeError as exc:
            QMessageBox.critical(self, "Connection Error", str(exc))
            self._set_status("Connection error. Click Refresh to retry.")
            return

        self._set_status("Connected. Press Search to load vulnerabilities.")

    # ------------------------------------------------------------------
    # Window lifecycle
    # ------------------------------------------------------------------

    def closeEvent(self, event) -> None:
        """Gracefully stop any running loader thread before closing.

        If the ``VulnLoader`` thread is still running when the user closes the
        window, stopping it immediately via Qt's default behaviour causes the
        crash ``QThread: Destroyed while thread '' is still running``.  This
        override signals the worker to stop fetching new pages and then blocks
        with ``QThread.wait()`` until the thread exits cleanly before allowing
        the window to close.
        """
        if self._loader is not None and self._loader.isRunning():
            self._loader.request_stop()
            self._loader.quit()
            self._loader.wait()
        event.accept()

    # ------------------------------------------------------------------
    # Data loading (QThread)
    # ------------------------------------------------------------------

    def _normalise_cve_input(self) -> None:
        """Normalise the CVE ID field in-place when the user finishes editing."""
        raw = self._q_cve_edit.text().strip()
        if raw:
            normalised = normalise_cve_id(raw)
            if normalised:
                self._q_cve_edit.setText(normalised)

    def _collect_fql(self) -> str:
        """Assemble an FQL filter string from the current query panel widgets.

        Reads every query-panel widget, sanitises string values against FQL
        injection (strips ``'`` and ``"``), and builds a ``+``-joined FQL
        expression.  The date-range clause is always appended so results are
        bounded by the chosen window even when all other filters are at default.

        Note: hostname is intentionally excluded from FQL.  The Spotlight
        combined endpoint does not expose ``hostname`` as a filterable FQL
        field; hostname substring filtering is handled in-memory by the view
        filter panel after data is loaded.

        Returns:
            FQL filter string ready to pass to :class:`VulnLoader`, e.g.
            ``"status:'open'+cve.id:'CVE-2024-*'
            +created_timestamp:>='2025-01-01T00:00:00Z'"``.
        """
        cve_raw = self._q_cve_edit.text().strip()
        # normalise_cve_id converts bare "YYYY-NNNNN" into "CVE-YYYY-NNNNN"
        # and returns "" for unparseable input (treated as "no CVE filter").
        cve_norm = normalise_cve_id(cve_raw) if cve_raw else ""

        os_val = self._q_os_combo.currentText()
        sev_val = self._q_severity_combo.currentText()
        status_val = self._q_status_combo.currentText()

        # Map the human-readable date-field label to the actual Spotlight FQL
        # field name.  All three are valid filter fields on the combined endpoint.
        _date_field_map = {
            "created": "created_timestamp",
            "updated": "updated_timestamp",
            "closed": "closed_timestamp",
        }
        date_field = _date_field_map.get(
            self._q_date_field_combo.currentText(), "created_timestamp"
        )
        date_from = self._q_date_from.date().toString("yyyy-MM-dd")
        date_to = self._q_date_to.date().toString("yyyy-MM-dd")

        parts: List[str] = []

        # Omit "All" combos — they mean "no restriction on this field".
        if status_val != "All":
            parts.append(f"status:'{_FQL_INJECTION_RE.sub('', status_val)}'")
        if cve_norm:
            # Append wildcard so "CVE-2024" matches all CVE-2024-* identifiers.
            norm_star = cve_norm if cve_norm.endswith("*") else cve_norm + "*"
            parts.append(f"cve.id:'{norm_star}'")
        if os_val != "All":
            # Spotlight FQL field is host_info.platform_name (not host_info.platform).
            parts.append(f"host_info.platform_name:'{_FQL_INJECTION_RE.sub('', os_val)}'")
        if sev_val != "All":
            parts.append(f"cve.severity:'{_FQL_INJECTION_RE.sub('', sev_val)}'")

        # CVSS range — only emit a clause when the user moved the spin box away
        # from its default (0.0 min / 10.0 max) to avoid a no-op filter.
        cvss_min = self._q_cvss_min.value()
        cvss_max = self._q_cvss_max.value()
        if cvss_min > 0.0:
            parts.append(f"cve.base_score:>={cvss_min:.1f}")
        if cvss_max < 10.0:
            parts.append(f"cve.base_score:<={cvss_max:.1f}")

        # Date range is always included — anchors results to the selected window.
        # T00:00:00Z / T23:59:59Z ensure the full boundary day is included.
        parts.append(f"{date_field}:>='{date_from}T00:00:00Z'")
        parts.append(f"{date_field}:<='{date_to}T23:59:59Z'")

        # FQL clauses are joined with "+" (logical AND in Spotlight FQL).
        return "+".join(parts)

    def _on_search_clicked(self) -> None:
        """Start (or restart) a data load using the current FQL query parameters.

        If a load is already running it is stopped synchronously before the new
        one begins.  Stopping is safe because :meth:`VulnLoader.request_stop`
        sets a threading.Event that the worker checks between pages, and
        ``QThread.wait()`` blocks until the thread exits cleanly.  This prevents
        two concurrent loads from racing to write to ``_all_records``.
        """
        if self._data_layer is None:
            # No authenticated session yet — show the credential dialog first.
            self._prompt_credentials()
            return

        # Cancel any in-flight load before starting a new one.
        if self._loader is not None and self._loader.isRunning():
            self._loader.request_stop()
            self._loader.quit()
            self._loader.wait()

        fql = self._collect_fql()

        # Clear previous results before the new load so stale rows are not
        # visible while the first page of the new query is in flight.
        self._all_records = []
        self._filtered_records = []
        self._table.setRowCount(0)
        # Disable view filters until the first page arrives so the user cannot
        # filter an empty table and wonder why nothing appears.
        self._view_filter_group.setEnabled(False)

        # Swap button states: Search disabled, Cancel enabled for the duration.
        self._search_btn.setEnabled(False)
        self._cancel_btn.setEnabled(True)
        # Switch accordion to "View Filters" (index 1) so the user can
        # immediately apply post-load filters as data arrives.
        self._toolbox.setCurrentIndex(1)
        self._set_status("Loading vulnerabilities…")

        # Wire up all signals before calling start() to avoid a race where the
        # thread emits a signal before the slot is connected.
        self._loader = VulnLoader(self._data_layer, fql_filter=fql, parent=self)
        self._loader.page_loaded.connect(self._on_page_loaded)
        self._loader.finished.connect(self._on_refresh_success)
        self._loader.stopped.connect(self._on_search_cancelled)
        self._loader.auth_error.connect(self._on_refresh_auth_error)
        self._loader.general_error.connect(self._on_refresh_error)
        self._loader.start()

    def _on_cancel_clicked(self) -> None:
        """Cancel the active data load; partial results are retained."""
        if self._loader is not None and self._loader.isRunning():
            self._loader.request_stop()
        self._cancel_btn.setEnabled(False)
        self._set_status("Cancelling…")

    def _on_search_cancelled(self, records: List[VulnRecord], elapsed: float) -> None:
        """Slot for VulnLoader.stopped — display partial results after cancel."""
        self._all_records = records
        self._apply_filters()
        self._search_btn.setEnabled(True)
        self._cancel_btn.setEnabled(False)
        if records:
            self._view_filter_group.setEnabled(True)
        self._set_status(
            f"Search cancelled — {len(records)} results shown ({elapsed:.1f}s)"
        )

    def _start_refresh(self) -> None:
        """Begin a background data refresh — delegates to _on_search_clicked.

        The Refresh button (and credential-prompt callback) calls this method.
        It simply forwards to the search flow so the query filters are always
        respected, even on the initial auto-refresh after login.
        """
        self._on_search_clicked()

    def _on_page_loaded(
        self, page_records: List[VulnRecord], page_num: int, cumulative_total: int
    ) -> None:
        """Slot called after each API page; appends matching rows incrementally."""
        self._all_records.extend(page_records)
        self._append_rows([r for r in page_records if self._passes_filter(r)])
        if not self._view_filter_group.isEnabled():
            self._view_filter_group.setEnabled(True)
        self._set_status(
            f"Loading page {page_num}… ({cumulative_total} vulnerabilities so far)"
        )

    def _on_refresh_success(self, records: List[VulnRecord], elapsed: float) -> None:
        """Slot called on the main thread when the loader finishes successfully.

        Replaces the incrementally-loaded rows with the fully-enriched record
        list so that hostnames (populated after all pages are fetched by
        :meth:`FalconDataLayer._enrich_hostnames`) are shown correctly.
        Incremental rows may still show raw agent IDs for hosts not yet enriched;
        this full-replace ensures the final view is accurate.

        Also repopulates the OS combo from the loaded data so the view filter
        reflects only platforms actually present in the result set.
        """
        self._all_records = records
        self._populate_os_combo(records)
        self._apply_filters()
        ts = datetime.now().strftime("%H:%M:%S")
        self._set_status(
            f"{len(records)} vulnerabilities loaded — "
            f"last refresh {ts} ({elapsed:.1f}s)"
        )
        if MATPLOTLIB_AVAILABLE:
            self._update_chart(records)
        self._search_btn.setEnabled(True)
        self._cancel_btn.setEnabled(False)
        if records:
            self._view_filter_group.setEnabled(True)

    def _on_refresh_auth_error(self, message: str) -> None:
        """Slot called on the main thread when the loader encounters HTTP 401."""
        self._search_btn.setEnabled(True)
        self._cancel_btn.setEnabled(False)
        self._set_status("Authentication error — re-enter credentials.")
        reply = QMessageBox.question(
            self,
            "Authentication Error",
            f"{message}\n\nRe-enter credentials?",
            QMessageBox.Retry | QMessageBox.Cancel,
        )
        if reply == QMessageBox.Retry:
            self._data_layer = None
            self._prompt_credentials()

    def _on_refresh_error(self, message: str) -> None:
        """Slot called on the main thread when the loader encounters a general error."""
        self._search_btn.setEnabled(True)
        self._cancel_btn.setEnabled(False)
        self._set_status(f"Error: {message}")
        QMessageBox.critical(self, "API Error", message)

    # ------------------------------------------------------------------
    # Filtering (in-memory — no API calls on filter changes)
    # ------------------------------------------------------------------

    def _passes_filter(self, rec: VulnRecord) -> bool:
        """Return True if *rec* satisfies the current view filter controls."""
        enabled_severities = {
            sev for sev, cb in self._severity_checks.items() if cb.isChecked()
        }
        cve_search = self._search_edit.text().strip().upper()
        hostname_search = self._hostname_edit.text().strip().upper()
        os_filter = self._os_combo.currentText()

        if rec.severity not in enabled_severities:
            return False
        if cve_search and cve_search not in rec.cve_id.upper():
            return False
        if hostname_search and hostname_search not in rec.hostname.upper():
            return False
        if os_filter != "All" and rec.os_platform != os_filter:
            return False
        return True

    def _append_rows(self, records: List[VulnRecord]) -> None:
        """Append *records* to the table without clearing existing rows.

        Used by :meth:`_on_page_loaded` for incremental table population.
        Sorting is temporarily disabled during the insert to prevent Qt from
        re-sorting the entire table after every cell write, which would be
        O(n²) in the number of rows for large datasets.
        """
        col_attrs = [
            "cve_id", "severity", "cvss_score", "hostname",
            "os_platform", "remediation_status", "first_seen", "last_seen",
        ]
        # Disable sorting to avoid O(n²) re-sort on every cell insert.
        self._table.setSortingEnabled(False)
        start_row = self._table.rowCount()
        self._table.setRowCount(start_row + len(records))
        for i, rec in enumerate(records):
            row = start_row + i
            fallback = SEVERITY_COLORS["UNKNOWN"]
            color = QColor(SEVERITY_COLORS.get(rec.severity, fallback))
            brush = QBrush(color)
            for col, attr in enumerate(col_attrs):
                item = QTableWidgetItem(getattr(rec, attr))
                item.setForeground(brush)
                # Prevent in-place cell editing — table is read-only.
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self._table.setItem(row, col, item)
        # Re-enable sorting after all rows are inserted.
        self._table.setSortingEnabled(True)

    def _apply_filters(self) -> None:
        """Filter ``_all_records`` in memory and repopulate the table.

        This method does **not** contact the API.  See the module docstring
        for the filter model rationale.
        """
        results = [rec for rec in self._all_records if self._passes_filter(rec)]
        self._filtered_records = results
        self._populate_table(results)

    def _clear_filters(self) -> None:
        """Reset all view filter controls to their default (show everything) state.

        Checking all severity boxes and clearing text fields re-triggers the
        ``stateChanged`` / ``textChanged`` signals connected to
        :meth:`_apply_filters`, so the table updates automatically — no
        explicit ``_apply_filters()`` call is needed here.
        """
        for cb in self._severity_checks.values():
            cb.setChecked(True)
        self._search_edit.clear()
        self._hostname_edit.clear()
        self._os_combo.setCurrentIndex(0)
        # _apply_filters is triggered automatically by the signal connections above.

    # ------------------------------------------------------------------
    # Table population
    # ------------------------------------------------------------------

    def _populate_table(self, records: List[VulnRecord]) -> None:
        """Clear the table and insert *records*, preserving sort order.

        Called by :meth:`_apply_filters` after every view-filter change and by
        :meth:`_on_refresh_success` after the full enriched result set arrives.

        Args:
            records: Records to display; must be the same list assigned to
                ``_filtered_records`` so that row-index lookups in
                :meth:`_on_cell_double_clicked` remain valid.
        """
        # Temporarily disable sorting to avoid per-row re-sort overhead.
        self._table.setSortingEnabled(False)
        self._table.setRowCount(0)
        self._table.setRowCount(len(records))

        col_attrs = [
            "cve_id", "severity", "cvss_score", "hostname",
            "os_platform", "remediation_status", "first_seen", "last_seen",
        ]
        for row, rec in enumerate(records):
            fallback = SEVERITY_COLORS["UNKNOWN"]
            color = QColor(SEVERITY_COLORS.get(rec.severity, fallback))
            brush = QBrush(color)
            for col, attr in enumerate(col_attrs):
                item = QTableWidgetItem(getattr(rec, attr))
                item.setForeground(brush)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self._table.setItem(row, col, item)

        self._table.setSortingEnabled(True)

    # ------------------------------------------------------------------
    # Row interaction
    # ------------------------------------------------------------------

    def _on_cell_double_clicked(self, row: int, _col: int) -> None:
        """Open a CVE detail dialog for the selected row.

        The row index maps directly into ``_filtered_records`` — the same list
        that ``_populate_table`` iterated over to build the current table view.
        """
        if row < 0 or row >= len(self._filtered_records):
            return
        rec = self._filtered_records[row]
        dlg = CveDetailDialog(rec, parent=self)
        dlg.show()  # Non-modal — user can open multiple dialogs.

    # ------------------------------------------------------------------
    # CSV export
    # ------------------------------------------------------------------

    def _export_csv(self) -> None:
        """Save the current filtered view to a user-chosen CSV file."""
        if not self._filtered_records:
            QMessageBox.information(self, "No data", "No vulnerabilities to export.")
            return

        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save vulnerability report",
            "",
            "CSV files (*.csv);;All files (*.*)",
        )
        if not path:
            return

        headers = [
            "CVE ID", "Severity", "CVSS Score", "Hostname", "OS Platform",
            "Status", "First Seen", "Last Seen",
        ]
        try:
            with open(path, "w", newline="", encoding="utf-8") as fh:
                writer = csv.writer(fh)
                writer.writerow(headers)
                for rec in self._filtered_records:
                    writer.writerow(
                        [
                            safe_csv_value(rec.cve_id),
                            safe_csv_value(rec.severity),
                            safe_csv_value(rec.cvss_score),
                            safe_csv_value(rec.hostname),
                            safe_csv_value(rec.os_platform),
                            safe_csv_value(rec.remediation_status),
                            safe_csv_value(rec.first_seen),
                            safe_csv_value(rec.last_seen),
                        ]
                    )
            QMessageBox.information(
                self,
                "Export complete",
                f"Saved {len(self._filtered_records)} rows to:\n{path}",
            )
        except OSError as exc:
            QMessageBox.critical(self, "Export failed", str(exc))

    # ------------------------------------------------------------------
    # Severity chart (optional — only when matplotlib is installed)
    # ------------------------------------------------------------------

    def _update_chart(self, records: List[VulnRecord]) -> None:
        """Redraw the severity breakdown bar chart with current data."""
        counts: Dict[str, int] = {sev: 0 for sev in SEVERITY_COLORS}
        for rec in records:
            if rec.severity in counts:
                counts[rec.severity] += 1

        self._ax.clear()
        severities = list(counts.keys())
        values = [counts[s] for s in severities]
        colours = [SEVERITY_COLORS[s] for s in severities]

        bars = self._ax.bar(severities, values, color=colours)
        for rect, val in zip(bars, values):
            if val > 0:
                self._ax.text(
                    rect.get_x() + rect.get_width() / 2.0,
                    rect.get_height() + 0.3,
                    str(val),
                    ha="center",
                    va="bottom",
                    fontsize=8,
                )

        self._ax.set_ylabel("Count", fontsize=8)
        self._ax.tick_params(labelsize=8)
        self._fig.patch.set_alpha(0.0)
        self._canvas.draw()

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _populate_os_combo(self, records: List[VulnRecord]) -> None:
        """Populate the OS view-filter combo with distinct platform values.

        Starts from the canonical _OS_PLATFORMS list so options always match the
        query-filter combo.  Any extra platform values seen in the loaded data
        that are not in the canonical list are appended in sorted order.

        Blocks the combo's ``currentTextChanged`` signal while rebuilding to
        avoid triggering :meth:`_apply_filters` once per item during the clear/
        re-add cycle.  The previous selection is restored if the platform is
        still present; otherwise the combo falls back to index 0 ("All").
        """
        current = self._os_combo.currentText()
        data_platforms = {r.os_platform for r in records if r.os_platform}
        extra = sorted(data_platforms - set(_OS_PLATFORMS))
        self._os_combo.blockSignals(True)
        self._os_combo.clear()
        self._os_combo.addItems(["All"] + _OS_PLATFORMS + extra)
        # Restore previous selection if still present; -1 from findText means
        # not found, so max(..., 0) safely falls back to "All".
        idx = self._os_combo.findText(current)
        self._os_combo.setCurrentIndex(max(idx, 0))
        self._os_combo.blockSignals(False)

    def _set_status(self, message: str) -> None:
        """Update the status bar message."""
        self._status_bar.showMessage(message)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def _parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--region",
        choices=VALID_REGIONS,
        default="auto",
        help="Falcon cloud region (default: auto)",
    )
    parser.add_argument(
        "-k",
        "--falcon_client_id",
        default=None,
        help=(
            "Falcon API client ID. "
            "Overrides the FALCON_CLIENT_ID environment variable. "
            "If neither is set, the credential dialog will prompt at startup."
        ),
    )
    parser.add_argument(
        "-s",
        "--falcon_client_secret",
        default=None,
        help=(
            "Falcon API client secret. "
            "Overrides the FALCON_CLIENT_SECRET environment variable. "
            "If neither is set, the credential dialog will prompt at startup."
        ),
    )
    return parser.parse_args()


def _resolve_credentials(args: argparse.Namespace) -> tuple:
    """Return (client_id, client_secret) by merging CLI args with env var fallback.

    Precedence: CLI argument > environment variable > None (dialog will prompt).

    Args:
        args: Parsed argparse namespace from _parse_args().

    Returns:
        Tuple of (client_id, client_secret), each of which may be None or an
        empty string when not supplied by either source.
    """
    client_id = args.falcon_client_id or os.environ.get("FALCON_CLIENT_ID") or None
    client_secret = (
        args.falcon_client_secret or os.environ.get("FALCON_CLIENT_SECRET") or None
    )
    return client_id, client_secret


def main() -> None:
    """Launch the dashboard application.

    Parses CLI arguments, resolves credentials from args or environment
    variables, creates the Qt application and main window, then enters the
    Qt event loop.  Returns when the user closes the window.
    """
    args = _parse_args()
    client_id, client_secret = _resolve_credentials(args)
    # Re-use an existing QApplication if one is already running (e.g. in tests).
    app = QApplication.instance() or QApplication([])
    window = DashboardWindow(
        default_region=args.region,
        client_id=client_id,
        client_secret=client_secret,
    )
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
