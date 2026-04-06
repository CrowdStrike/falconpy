r"""FileVantage Change Monitor — Desktop GUI.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |             FalconPy
`-------'                         `-------'

 _____  ____  _        ___ __ __   ____  ____   ______   ____   ____    ___
|     |l    j| T      /  _]  T  | /    T|    \ |      T /    T /    T  /  _]
|   __j |  T | |     /  [_|  |  |Y  o  ||  _  Y|      |Y  o  |Y   __j /  [_
|  l_   |  | | l___ Y    _]  |  ||     ||  |  |l_j  l_j|     ||  T  |Y    _]
|   _]  |  | |     T|   [_l  :  !|  _  ||  |  |  |  |  |  _  ||  l_ ||   [_
|  T    j  l |     ||     T\   / |  |  ||  |  |  |  |  |  |  ||     ||     T
l__j   |____jl_____jl_____j \_/  l__j__jl__j__j  l__j  l__j__jl___,_jl_____j

    __  __ __   ____  ____    ____    ___      ___ ___   ___   ____   ____  ______   ___   ____
   /  ]|  T  T /    T|    \  /    T  /  _]    |   T   T /   \ |    \ l    j|      T /   \ |    \
  /  / |  l  |Y  o  ||  _  YY   __j /  [_     | _   _ |Y     Y|  _  Y |  T |      |Y     Y|  D  )
 /  /  |  _  ||     ||  |  ||  T  |Y    _]    |  \_/  ||  O  ||  |  | |  | l_j  l_j|  O  ||    /
/   \_ |  |  ||  _  ||  |  ||  l_ ||   [_     |   |   ||     ||  |  | |  |   |  |  |     ||    \
\     ||  |  ||  |  ||  |  ||     ||     T    |   |   |l     !|  |  | j  l   |  |  l     !|  .  Y
 \____jl__j__jl__j__jl__j__jl___,_jl_____j    l___j___j \___/ l__j__j|____j  l__j   \___/ l__j\_j

                            FileVantage Change Monitor — Desktop GUI
                            Uses: FileVantage
                            Scope: filevantage:read, filevantage:write

A PyQt6 desktop application for monitoring CrowdStrike Falcon FileVantage
file integrity monitoring (FIM) events. It retrieves change events from
the Falcon platform using the FalconPy SDK and displays them in an
auto-refreshing live feed with drill-down detail dialogs.

Prerequisites
-------------
  pip install crowdstrike-falconpy PyQt6
  (or: pipenv install crowdstrike-falconpy PyQt6)

Required API scopes
-------------------
  filevantage:read   — query and retrieve change events, action status
  filevantage:write  — suppress / purge changes via start_actions

Credentials
-----------
  Credentials are read from environment variables at startup:
    FALCON_CLIENT_ID     — Falcon API client ID
    FALCON_CLIENT_SECRET — Falcon API client secret

  An optional FALCON_BASE_URL environment variable selects the cloud region
  (defaults to "auto" which targets the US-1 commercial cloud).

Usage
-----
    pipenv run python3 filevantage_monitor.py
    pipenv run python3 filevantage_monitor.py -k CLIENT_ID -s CLIENT_SECRET
    FALCON_CLIENT_ID=xxx FALCON_CLIENT_SECRET=yyy pipenv run python3 filevantage_monitor.py

CLI flags
---------
  -k / --client_id      Falcon API client ID (overrides FALCON_CLIENT_ID env var)
  -s / --client_secret  Falcon API client secret (overrides FALCON_CLIENT_SECRET env var)
  -b / --base_url       Cloud region base URL (default: auto). Use usgov1 for GovCloud.

Architecture overview
---------------------
  FileVantageWindow (QMainWindow)
  ├── Toolbar — FQL filter bar, severity/type filters, Refresh + Export buttons
  ├── Auth status indicator in toolbar
  ├── Event table (QTableView + QSortFilterProxyModel) — auto-refreshes every 30s
  │   Columns: Timestamp, Hostname, File Path, Change Type, User, Process
  └── Status bar — total / filtered / selected counts + last-refresh time

  Detail dialog (QDialog, opened on row double-click):
  ├── Summary fields: file path, host, action type, user, process
  ├── Hashes tab: before/after SHA256 file hash comparison
  ├── Event JSON tab: raw API response formatted as indented JSON
  └── Suppress / Purge buttons → calls start_actions for selected change IDs

  API calls run on a background QThread (FetchChangesWorker) and deliver
  results back to the main thread via Qt signals, keeping the UI responsive.
"""
# pylint: disable=too-many-lines
# pylint: disable=too-many-arguments,too-many-positional-arguments
# pylint: disable=too-many-locals,too-few-public-methods
# pylint: disable=too-many-instance-attributes,too-many-statements
import csv
import json
import math
import os
import sys
from argparse import ArgumentParser, RawTextHelpFormatter
from datetime import datetime

# pylint: disable=import-error
from PyQt6.QtCore import (
    Qt, QThread, pyqtSignal, QTimer, QSortFilterProxyModel,
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QFont, QColor
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStatusBar,
    QTabWidget,
    QTableView,
    QTextEdit,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from falconpy import FileVantage
# pylint: enable=import-error

# ── Constants ────────────────────────────────────────────────────────────────

_APP_TITLE = "FileVantage Change Monitor"
_APP_VERSION = "1.0.0"

# Auto-refresh interval in milliseconds (30 seconds).
_AUTO_REFRESH_MS = 30_000

# Maximum change IDs fetched per API page.
_PAGE_SIZE = 100

# Maximum change IDs to retrieve per progressive-load batch.
# Set high enough to allow full coverage of large environments (88k+ records).
_MAX_CHANGES = 2000

# Change type values returned by the FileVantage API.
_CHANGE_TYPES = ["All", "CREATE", "WRITE", "DELETE", "RENAME", "CHMOD", "CHOWN", "CHATTR"]

# Rows-per-page options for the pagination page-size selector.
_PAGE_SIZE_OPTIONS = [25, 50, 100]
# Default rows per page on first launch.
_DEFAULT_PAGE_SIZE = 50

# Column indices for the event table model.
_COL_TIMESTAMP = 0
_COL_HOSTNAME = 1
_COL_FILE_PATH = 2
_COL_CHANGE_TYPE = 3
_COL_USER = 4
_COL_PROCESS = 5
_COL_CHANGE_ID = 6   # Hidden column — stores raw change ID for API calls.

# Background colours keyed by change type for quick visual scanning.
_CHANGE_TYPE_COLOURS: dict[str, str] = {
    "CREATE": "#1a3a1a",
    "WRITE": "#1a2b3a",
    "DELETE": "#3a1a1a",
    "RENAME": "#2e2a1a",
    "CHMOD": "#2a1a3a",
    "CHOWN": "#1a2e2e",
    "CHATTR": "#2a2a2a",
}

# Demo fixture data shown when credentials are absent or when the API returns
# no results.  Structure mirrors the FileVantage getChanges response body.
_DEMO_CHANGES = [
    {
        "id": "demo-change-001",
        "action_timestamp": "2026-03-15T08:00:01Z",
        "host": {"name": "WIN-SERVER-01"},
        "action_type": "WRITE",
        "ingestion_timestamp": "2026-03-15T08:00:05Z",
        "diff_type": "BINARY",
        "entity_type": "FILE",
        "severity": "HIGH",
        "file_name": "svchost.dll",
        "file_path": "C:\\Windows\\System32\\svchost.dll",
        "process_image_file_name": "installer.exe",
        "user_name": "SYSTEM",
        "sha256_hash_before": "abc123def456abc123def456abc123def456abc123def456abc123def456abc1",
        "sha256_hash_after": "999aaabbbccc999aaabbbccc999aaabbbccc999aaabbbccc999aaabbbccc9999",
        "raw_json": {},
    },
    {
        "id": "demo-change-002",
        "action_timestamp": "2026-03-15T08:02:30Z",
        "host": {"name": "LINUX-WEB-03"},
        "action_type": "DELETE",
        "ingestion_timestamp": "2026-03-15T08:02:34Z",
        "diff_type": "TEXT",
        "entity_type": "FILE",
        "severity": "MEDIUM",
        "file_name": "passwd",
        "file_path": "/etc/passwd",
        "process_image_file_name": "rm",
        "user_name": "root",
        "sha256_hash_before": "111222333444111222333444111222333444111222333444111222333444111f",
        "sha256_hash_after": "",
        "raw_json": {},
    },
    {
        "id": "demo-change-003",
        "action_timestamp": "2026-03-15T08:05:10Z",
        "host": {"name": "LINUX-WEB-03"},
        "action_type": "CREATE",
        "ingestion_timestamp": "2026-03-15T08:05:14Z",
        "diff_type": "BINARY",
        "entity_type": "FILE",
        "severity": "LOW",
        "file_name": "backdoor.sh",
        "file_path": "/tmp/backdoor.sh", # nosec - Ridiculous Bandit FP
        "process_image_file_name": "bash",
        "user_name": "www-data",
        "sha256_hash_before": "",
        "sha256_hash_after": "deadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef",
        "raw_json": {},
    },
    {
        "id": "demo-change-004",
        "action_timestamp": "2026-03-15T08:10:45Z",
        "host": {"name": "WIN-WORKSTATION-07"},
        "action_type": "RENAME",
        "ingestion_timestamp": "2026-03-15T08:10:49Z",
        "diff_type": "TEXT",
        "entity_type": "FILE",
        "severity": "MEDIUM",
        "file_name": "config.bak",
        "file_path": "C:\\Users\\alice\\Documents\\config.bak",
        "process_image_file_name": "explorer.exe",
        "user_name": "alice",
        "sha256_hash_before": "aaaa1111bbbb2222cccc3333dddd4444aaaa1111bbbb2222cccc3333dddd4444",
        "sha256_hash_after": "aaaa1111bbbb2222cccc3333dddd4444aaaa1111bbbb2222cccc3333dddd4444",
        "raw_json": {},
    },
]


# ── Argument parsing ──────────────────────────────────────────────────────────


def consume_arguments() -> object:
    """Parse command-line arguments for credential and region overrides.

    CLI flags take precedence over environment variables.  If neither is
    provided the application falls back to demo mode.
    """
    parser = ArgumentParser(
        description=__doc__,
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument(
        "-k", "--client_id",
        help="Falcon API client ID (overrides FALCON_CLIENT_ID env var)",
        default=None,
    )
    parser.add_argument(
        "-s", "--client_secret",
        help="Falcon API client secret (overrides FALCON_CLIENT_SECRET env var)",
        default=None,
    )
    parser.add_argument(
        "-b", "--base_url",
        help="Cloud region base URL (default: auto). Use usgov1 for GovCloud.",
        default=None,
    )
    return parser.parse_args()


# ── Helpers ───────────────────────────────────────────────────────────────────


def _fmt_ts(ts: str) -> str:
    """Reformat an ISO-8601 timestamp to a shorter local display string.

    Returns the original string unchanged if parsing fails, so callers
    never have to guard against None or empty strings.
    """
    if not ts:
        return ""
    try:
        dt = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ")
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return ts


def _get_nested(obj: dict, *keys: str, default: str = "") -> str:
    """Safely extract a nested value from a dict, returning default if absent."""
    current = obj
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key, default)
    return current if current is not None else default


def _resolve_file_path(change: dict) -> str:
    """Extract the file path from a change resource.

    The FileVantage getChanges API returns the path in ``entity_path``
    (confirmed against live API — field contains the full device path,
    e.g. '\\Device\\HarddiskVolume6\\...\\file.txt').

    Fallback chain retained for robustness against schema variations:
      1. entity_path       — primary field (confirmed in production API)
      2. file_path         — v1 schema / demo data
      3. filepath / path   — alternative spellings
      4. entity_attributes — nested variants seen in some responses
      5. directory+file_name — constructed path as last resort

    Returns the first non-empty value found, or an empty string.
    """
    # Primary: entity_path (confirmed field name from live API)
    val = change.get("entity_path", "")
    if val:
        return str(val)

    # Fallback: legacy / alternative top-level field names.
    for key in ("file_path", "filepath", "path"):
        val = change.get(key, "")
        if val:
            return str(val)

    # Try nested under entity_attributes (seen in some API variant responses).
    attrs = change.get("entity_attributes", {})
    if isinstance(attrs, dict):
        for key in ("entity_path", "file_path", "filepath", "path"):
            val = attrs.get(key, "")
            if val:
                return str(val)

    # Build path from directory + file name as last resort.
    directory = change.get("directory", "") or _get_nested(change, "entity_attributes", "directory")
    file_name = change.get("file_name", "") or _get_nested(change, "entity_attributes", "file_name")
    if directory or file_name:
        sep = "" if directory.endswith(("/", "\\")) else "/"
        return f"{directory}{sep}{file_name}".lstrip("/")

    return ""


def _make_item(text: str, colour: str = "") -> QStandardItem:
    """Create a non-editable table cell item with an optional background colour."""
    item = QStandardItem(str(text))
    item.setEditable(False)
    if colour:
        item.setBackground(QColor(colour))
    return item


# ── Background worker ─────────────────────────────────────────────────────────


class FetchChangesWorker(QThread):
    """Background thread that pages through FileVantage change events.

    Emits:
        finished(list[dict], int, bool) — hydrated change dicts, next API offset,
                                          and whether more results are available.
        error(str)                      — human-readable error message on failure.
    """

    finished = pyqtSignal(list, int, bool)
    error = pyqtSignal(str)

    def __init__(self, client_id: str, client_secret: str, base_url: str,
                 fql_filter: str, start_offset: int = 0, parent=None) -> None:
        """Initialise the worker with Falcon API credentials and an optional FQL filter.

        *start_offset* is the API offset to begin from (0 for a fresh load,
        non-zero to continue fetching after a previous batch).
        """
        super().__init__(parent)
        self._client_id = client_id
        self._client_secret = client_secret
        self._base_url = base_url
        self._fql_filter = fql_filter
        self._start_offset = start_offset

    def run(self) -> None:  # pylint: disable=too-many-branches
        """Authenticate, paginate through FileVantage change IDs, hydrate, and emit results."""
        try:
            sdk = FileVantage(
                client_id=self._client_id,
                client_secret=self._client_secret,
                base_url=self._base_url,
            )

            # Page through query_changes in _PAGE_SIZE chunks until we have
            # _MAX_CHANGES IDs or the API signals no more results.
            all_ids: list[str] = []
            offset = self._start_offset
            while len(all_ids) < _MAX_CHANGES:
                if self.isInterruptionRequested():
                    return
                remaining = _MAX_CHANGES - len(all_ids)
                page_limit = min(_PAGE_SIZE, remaining)
                kwargs: dict = {
                    "limit": page_limit,
                    "offset": offset,
                    "sort": "action_timestamp|desc",
                }
                if self._fql_filter:
                    kwargs["filter"] = self._fql_filter

                resp = sdk.query_changes(**kwargs)
                status = resp.get("status_code", 0)
                body = resp.get("body", {})

                if status != 200:
                    errors = body.get("errors", [])
                    msg = (errors[0].get("message", "Unknown error")
                           if errors else f"HTTP {status}")
                    self.error.emit(f"query_changes failed: {msg}")
                    return

                page_ids: list[str] = body.get("resources", []) or []
                if not page_ids:
                    break  # No more results.

                all_ids.extend(page_ids)
                offset += len(page_ids)

                # Stop early if the API returned fewer results than the page limit
                # (signals end of result set).
                if len(page_ids) < page_limit:
                    break

            # has_more is True when we filled the batch exactly (may be more beyond).
            has_more = len(all_ids) == _MAX_CHANGES
            next_offset = offset

            if not all_ids:
                self.finished.emit([], next_offset, False)
                return

            # Hydrate IDs in batches of 100 (get_changes API limit).
            changes: list[dict] = []
            debug_printed = False
            for i in range(0, len(all_ids), _PAGE_SIZE):
                if self.isInterruptionRequested():
                    return
                batch = all_ids[i : i + _PAGE_SIZE]
                resp = sdk.get_changes(ids=batch)
                status = resp.get("status_code", 0)
                body = resp.get("body", {})

                if status != 200:
                    errors = body.get("errors", [])
                    msg = (errors[0].get("message", "Unknown error")
                           if errors else f"HTTP {status}")
                    self.error.emit(f"get_changes failed: {msg}")
                    return

                resources = body.get("resources", []) or []

                # Debug: print the first raw resource so field names can be verified
                # if unexpected columns appear empty.
                if not debug_printed and resources:
                    debug_printed = True
                    print("[FileVantage DEBUG] First change keys:", list(resources[0].keys()))
                    truncated = dict(list(resources[0].items())[:15])
                    print("[FileVantage DEBUG] First change (truncated):",
                          json.dumps(truncated, indent=2, default=str))

                for resource in resources:
                    # Attach raw JSON for the detail dialog's JSON tab.
                    resource["raw_json"] = resource.copy()
                    changes.append(resource)

            self.finished.emit(changes, next_offset, has_more)

        except Exception as exc:  # pylint: disable=broad-except
            self.error.emit(str(exc))


class SuppressWorker(QThread):
    """Background thread that calls start_actions then polls get_actions for status.

    Workflow:
        1. start_actions  — initiate suppress/purge/unsuppress on the given change IDs.
        2. get_actions    — retrieve the resulting action record(s) to confirm status.

    Emits:
        finished(str)   — human-readable success message including action status.
        error(str)      — human-readable error message if either call fails.
    """

    # Maximum number of get_actions polls before giving up on status confirmation.
    _MAX_POLLS = 5
    # Seconds to wait between each poll attempt.
    _POLL_INTERVAL_S = 2

    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, client_id: str, client_secret: str, base_url: str,
                 change_ids: list, operation: str, comment: str, parent=None) -> None:
        """Initialise with credentials, change IDs, operation name, and comment."""
        super().__init__(parent)
        self._client_id = client_id
        self._client_secret = client_secret
        self._base_url = base_url
        self._change_ids = change_ids
        self._operation = operation
        self._comment = comment

    def run(self) -> None:
        """Submit the action via start_actions, then poll get_actions for status."""
        import time  # pylint: disable=import-outside-toplevel
        try:
            sdk = FileVantage(
                client_id=self._client_id,
                client_secret=self._client_secret,
                base_url=self._base_url,
            )

            # ── Step 1: start_actions ─────────────────────────────────────────
            resp = sdk.start_actions(
                change_ids=self._change_ids,
                operation=self._operation,
                comment=self._comment,
            )
            status = resp.get("status_code", 0)
            body = resp.get("body", {})

            if status not in (200, 202):
                errors = body.get("errors", [])
                msg = errors[0].get("message", "Unknown error") if errors else f"HTTP {status}"
                self.error.emit(f"start_actions failed: {msg}")
                return

            action_ids: list[str] = body.get("resources", []) or []
            if not action_ids:
                # API accepted the request but returned no action IDs — report as accepted.
                self.finished.emit(
                    f"Action '{self._operation}' accepted for {len(self._change_ids)} "
                    "change(s). No action ID returned by API."
                )
                return

            # ── Step 2: get_actions — poll until complete or max attempts ─────
            # The API processes actions asynchronously; status may initially be
            # "pending" or "running" before transitioning to "completed"/"failed".
            final_status = "unknown"
            for attempt in range(self._MAX_POLLS):
                if attempt > 0:
                    time.sleep(self._POLL_INTERVAL_S)

                poll_resp = sdk.get_actions(ids=action_ids)
                poll_status = poll_resp.get("status_code", 0)
                poll_body = poll_resp.get("body", {})

                if poll_status != 200:
                    # get_actions failure is non-fatal — we already submitted the action.
                    break

                action_resources = poll_body.get("resources", []) or []
                if action_resources:
                    # Use the status of the first action record as representative.
                    final_status = action_resources[0].get("status", "unknown")
                    if final_status in ("completed", "failed", "error"):
                        break  # Terminal state reached — no further polling needed.

            self.finished.emit(
                f"Action '{self._operation}' submitted for {len(self._change_ids)} "
                f"change(s). Action ID(s): {', '.join(action_ids)}. "
                f"Status: {final_status}."
            )

        except Exception as exc:  # pylint: disable=broad-except
            self.error.emit(str(exc))


# ── Detail dialog ─────────────────────────────────────────────────────────────


class ChangeDetailDialog(QDialog):
    """Modal dialog showing full detail for a single FileVantage change event.

    Tabs:
        Summary — human-readable fields (file path, host, user, process, hashes)
        Raw JSON — indented JSON dump of the raw API resource

    Signals:
        refresh_requested() — emitted after a successful suppress/unsuppress/purge
                              so the parent window can reload the change list.
    """

    # Emitted after any successful action so the parent window can refresh.
    refresh_requested = pyqtSignal()
    # Emitted after a successful purge carrying the purged change ID so the
    # parent can remove it client-side (purge deletion is async on the API).
    purge_completed = pyqtSignal(str)

    def __init__(self, change: dict, client_id: str, client_secret: str,
                 base_url: str, parent=None) -> None:
        """Build the dialog from a hydrated change dict."""
        super().__init__(parent)
        self._change = change
        self._client_id = client_id
        self._client_secret = client_secret
        self._base_url = base_url
        self._suppress_worker: SuppressWorker | None = None
        self._last_operation: str = ""   # Tracks the in-flight action name.

        self.setWindowTitle(f"Change Detail — {change.get('id', '')}")
        self.setMinimumSize(700, 500)
        self._build_ui()

    def _build_ui(self) -> None:
        """Construct all widgets."""
        root = QVBoxLayout(self)

        self._tabs = QTabWidget()
        self._tabs.addTab(self._build_summary_tab(), "Summary")
        self._tabs.addTab(self._build_json_tab(), "Raw JSON")
        root.addWidget(self._tabs)

        # Action buttons row.
        btn_row = QHBoxLayout()
        btn_row.addStretch()

        self._suppress_btn = QPushButton("Suppress")
        self._suppress_btn.setToolTip("Suppress this change event via FileVantage start_actions")
        self._suppress_btn.clicked.connect(lambda: self._start_action("suppress"))
        btn_row.addWidget(self._suppress_btn)

        self._unsuppress_btn = QPushButton("Unsuppress")
        self._unsuppress_btn.setToolTip("Remove suppression from this change event")
        self._unsuppress_btn.clicked.connect(lambda: self._start_action("unsuppress"))
        btn_row.addWidget(self._unsuppress_btn)

        self._purge_btn = QPushButton("Purge")
        self._purge_btn.setToolTip("Purge this change event via FileVantage start_actions")
        self._purge_btn.clicked.connect(lambda: self._start_action("purge"))
        btn_row.addWidget(self._purge_btn)

        close_btn = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        close_btn.rejected.connect(self.reject)
        btn_row.addWidget(close_btn)

        # Disable action buttons when no real credentials are present.
        has_creds = bool(self._client_id and self._client_secret)
        if not has_creds:
            for btn in (self._suppress_btn, self._unsuppress_btn, self._purge_btn):
                btn.setEnabled(False)
                btn.setToolTip("Credentials required")
        else:
            # Show the correct action button based on current suppression state.
            self._sync_suppress_buttons()

        root.addLayout(btn_row)

    def _build_summary_tab(self) -> QWidget:
        """Build the human-readable summary tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        host = _get_nested(self._change, "host", "name")

        # The FileVantage API returns a three-level process chain when available:
        # process_image_file_name -> parent_image_file_name -> grandparent_image_file_name.
        is_suppressed = self._change.get("is_suppressed", False)
        fields = [
            ("Change ID", self._change.get("id", "")),
            ("Timestamp", _fmt_ts(self._change.get("action_timestamp", ""))),
            ("Hostname", host),
            ("File Path", _resolve_file_path(self._change)),
            ("File Name", self._change.get("file_name", "")),
            ("Change Type", self._change.get("action_type", "")),
            ("Entity Type", self._change.get("entity_type", "")),
            ("Severity", self._change.get("severity", "")),
            ("Suppressed", "Yes" if is_suppressed else "No"),
            ("User", self._change.get("user_name", "")),
            ("Process", self._change.get("process_image_file_name", "")),
            ("Parent Process", self._change.get("parent_image_file_name", "")),
            ("Grandparent Process", self._change.get("grandparent_image_file_name", "")),
            ("Diff Type", self._change.get("diff_type", "")),
        ]

        grid = QGroupBox("Event Details")
        grid_layout = QVBoxLayout(grid)
        for label, value in fields:
            row = QHBoxLayout()
            lbl = QLabel(f"<b>{label}:</b>")
            lbl.setFixedWidth(120)
            val = QLabel(str(value))
            val.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
            val.setWordWrap(True)
            row.addWidget(lbl)
            row.addWidget(val, 1)
            grid_layout.addLayout(row)
        layout.addWidget(grid)

        # Hash comparison section.
        hash_box = QGroupBox("File Hashes")
        hash_layout = QVBoxLayout(hash_box)

        before = self._change.get("sha256_hash_before", "") or "(none)"
        after = self._change.get("sha256_hash_after", "") or "(none)"
        changed = before != after

        for label, value in [("SHA256 Before:", before), ("SHA256 After:", after)]:
            row = QHBoxLayout()
            lbl = QLabel(f"<b>{label}</b>")
            lbl.setFixedWidth(120)
            val = QLabel(value)
            val.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
            font = QFont("Courier New", 9)
            val.setFont(font)
            if changed and label == "SHA256 After:" and value != "(none)":
                val.setStyleSheet("color: #ff6b6b;")  # Red tint to highlight hash change.
            row.addWidget(lbl)
            row.addWidget(val, 1)
            hash_layout.addLayout(row)

        layout.addWidget(hash_box)
        layout.addStretch()
        return widget

    def _build_json_tab(self) -> QWidget:
        """Build the raw JSON dump tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        text = QTextEdit()
        text.setReadOnly(True)
        font = QFont("Courier New", 10)
        text.setFont(font)

        raw = self._change.get("raw_json", self._change)
        text.setPlainText(json.dumps(raw, indent=2, default=str))
        layout.addWidget(text)
        return widget

    def _sync_suppress_buttons(self) -> None:
        """Show Suppress or Unsuppress depending on current is_suppressed state."""
        suppressed = bool(self._change.get("is_suppressed", False))
        self._suppress_btn.setVisible(not suppressed)
        self._unsuppress_btn.setVisible(suppressed)

    def _start_action(self, operation: str) -> None:
        """Kick off a suppress, unsuppress, or purge action for this change ID."""
        change_id = self._change.get("id", "")
        if not change_id or change_id.startswith("demo-"):
            QMessageBox.information(self, "Demo Mode",
                                    "Actions are disabled in demo mode.")
            return

        reply = QMessageBox.question(
            self,
            f"Confirm {operation.title()}",
            f"Apply '{operation}' to change ID:\n{change_id}\n\nContinue?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

        self._last_operation = operation
        self._suppress_btn.setEnabled(False)
        self._unsuppress_btn.setEnabled(False)
        self._purge_btn.setEnabled(False)

        self._suppress_worker = SuppressWorker(
            client_id=self._client_id,
            client_secret=self._client_secret,
            base_url=self._base_url,
            change_ids=[change_id],
            operation=operation,
            comment=f"Submitted via FileVantage Change Monitor {_APP_VERSION}",
            parent=self,
        )
        self._suppress_worker.finished.connect(self._on_action_done)
        self._suppress_worker.error.connect(self._on_action_error)
        self._suppress_worker.start()

    def _on_action_done(self, message: str) -> None:
        """Handle successful action completion.

        - purge: close the dialog (record no longer exists) and ask parent to refresh.
        - suppress/unsuppress: update is_suppressed in the cached change dict, rebuild
          the Summary tab in-place so the user sees the new state immediately, then
          ask the parent window to refresh its change list.
        """
        QMessageBox.information(self, "Action Complete", message)

        op = self._last_operation
        if op == "purge":
            # Purge is async on the API side — the record remains in query_changes
            # until index deletion propagates (may be minutes).  Calling _refresh()
            # would re-fetch and redisplay the same record.  Instead, signal the
            # parent to remove it client-side immediately, then close the dialog.
            change_id = self._change.get("id", "")
            self.purge_completed.emit(change_id)
            self.accept()
            return

        # suppress / unsuppress — update cached state and rebuild summary tab.
        self._change["is_suppressed"] = op == "suppress"
        # Replace the Summary tab widget in-place.
        self._tabs.removeTab(0)
        self._tabs.insertTab(0, self._build_summary_tab(), "Summary")
        self._tabs.setCurrentIndex(0)
        self._sync_suppress_buttons()
        self._suppress_btn.setEnabled(True)
        self._unsuppress_btn.setEnabled(True)
        self._purge_btn.setEnabled(True)

        # Notify the parent window so the change list reflects the new state.
        self.refresh_requested.emit()

    def _on_action_error(self, message: str) -> None:
        """Show error message and re-enable action buttons."""
        QMessageBox.critical(self, "Action Failed", message)
        self._suppress_btn.setEnabled(True)
        self._unsuppress_btn.setEnabled(True)
        self._purge_btn.setEnabled(True)


# ── Main window ───────────────────────────────────────────────────────────────


class FileVantageWindow(QMainWindow):
    """Main application window.

    Responsibilities:
    - Build and own all UI widgets.
    - Read FALCON_CLIENT_ID / FALCON_CLIENT_SECRET from the environment.
    - Trigger background refreshes every 30 seconds.
    - Populate the table model from FetchChangesWorker results.
    - Handle filter bar changes (client-side proxy filter).
    - Dispatch Suppress / Export actions.
    """

    def __init__(self, client_id: str = "", client_secret: str = "", # nosec - Bandit FP
                 base_url: str = "") -> None:
        """Initialise window, read credentials, build UI, trigger first load.

        Credential resolution order (first non-empty value wins):
          1. cli_client_id / cli_client_secret arguments (from -k / -s flags)
          2. FALCON_CLIENT_ID / FALCON_CLIENT_SECRET environment variables
        """
        super().__init__()
        self._client_id = client_id or os.environ.get("FALCON_CLIENT_ID", "")
        self._client_secret = client_secret or os.environ.get("FALCON_CLIENT_SECRET", "")
        self._base_url = base_url or os.environ.get("FALCON_BASE_URL", "auto")

        # All loaded change objects keyed by change ID for fast lookup.
        self._changes_by_id: dict[str, dict] = {}

        # Worker references — held to prevent premature garbage collection.
        self._fetch_worker: FetchChangesWorker | None = None
        self._suppress_worker: SuppressWorker | None = None

        # Pagination state: current 0-based page index and rows per page.
        self._current_page: int = 0
        self._ui_page_size: int = _DEFAULT_PAGE_SIZE

        # When True the current page index is preserved across the next
        # _on_fetch_done call (used by auto-refresh so timer ticks don't
        # jump the user back to page 1 mid-navigation).
        self._preserve_page_on_refresh: bool = False

        # Progressive API pagination state.
        # _api_offset tracks the next offset to pass to query_changes for a
        # "load more" request; _has_more_api_data is True when the last batch
        # returned a full _MAX_CHANGES result set (there may be more).
        self._api_offset: int = 0
        self._has_more_api_data: bool = False

        # True once the user has loaded progressive batches beyond the first
        # fetch.  While True, the auto-refresh timer is suppressed to avoid
        # wiping progressive rows and resetting the page counter to 1.
        self._progressive_loaded: bool = False

        # Guard flag that is True from the moment _load_more() dispatches a
        # worker until _on_fetch_more_done() (or _on_fetch_error()) runs on
        # the main thread.  This closes the TOCTOU race window where the
        # worker's QThread.isRunning() returns False before its finished()
        # signal has been delivered, allowing _refresh() to sneak in and wipe
        # the table.
        self._load_more_in_flight: bool = False

        # Bulk action state — stored so _on_action_done can dispatch to the
        # correct handler (purge: client-side removal vs suppress: refresh).
        self._bulk_operation: str = ""
        self._bulk_change_ids: list[str] = []

        self._demo_mode = not (self._client_id and self._client_secret)

        self._build_ui()
        self._start_auto_refresh()

        # Load data immediately on startup.
        self._refresh()

    # ── UI construction ───────────────────────────────────────────────────────

    def _build_ui(self) -> None:
        """Assemble the full window layout."""
        credential_status = "DEMO MODE — set FALCON_CLIENT_ID / FALCON_CLIENT_SECRET" \
            if self._demo_mode else f"Connected ({self._client_id[:8]}…)"
        self.setWindowTitle(f"{_APP_TITLE} v{_APP_VERSION} — {credential_status}")
        self.setMinimumSize(1100, 600)

        # ── Toolbar ───────────────────────────────────────────────────────────
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        # Auth status chip — saved as instance attribute so _update_auth_indicator()
        # can update it when auto-refresh is toggled.
        self._auth_label = QLabel()
        if self._demo_mode:
            self._auth_label.setText("🔴 Demo")
            self._auth_label.setStyleSheet("color: #ff6b6b; font-weight: bold; padding: 0 8px;")
        else:
            self._auth_label.setText("🟢 Live")
            self._auth_label.setStyleSheet("color: #6bff6b; font-weight: bold; padding: 0 8px;")
        toolbar.addWidget(self._auth_label)
        toolbar.addSeparator()

        # Auto-refresh toggle checkbox — controls the 30-second timer and dims
        # the Live indicator when paused.  Defaults to ON to match startup behaviour.
        self._auto_refresh_checkbox = QCheckBox("Auto-refresh")
        self._auto_refresh_checkbox.setChecked(True)
        self._auto_refresh_checkbox.setToolTip(
            "When checked: refresh every 30 s and keep the Live indicator lit.\n"
            "When unchecked: timer pauses; loaded data is preserved."
        )
        self._auto_refresh_checkbox.toggled.connect(self._toggle_auto_refresh)
        toolbar.addWidget(self._auto_refresh_checkbox)
        toolbar.addSeparator()

        # FQL filter input.
        toolbar.addWidget(QLabel("FQL Filter:"))
        self._fql_input = QLineEdit()
        self._fql_input.setPlaceholderText(
            'e.g. host.name:"win-server-01"+action_type:"WRITE"'
        )
        self._fql_input.setFixedWidth(380)
        self._fql_input.setToolTip(
            "FileVantage FQL filter applied server-side on next refresh.\n"
            "Available fields: action_timestamp, host.name, ingestion_timestamp"
        )
        toolbar.addWidget(self._fql_input)
        toolbar.addSeparator()

        # Change type filter — applied client-side.
        toolbar.addWidget(QLabel("Type:"))
        self._type_combo = QComboBox()
        for ct in _CHANGE_TYPES:
            self._type_combo.addItem(ct)
        self._type_combo.setSizeAdjustPolicy(
            QComboBox.SizeAdjustPolicy.AdjustToContents
        )
        self._type_combo.setMinimumWidth(110)
        self._type_combo.currentTextChanged.connect(self._apply_type_filter)
        toolbar.addWidget(self._type_combo)
        toolbar.addSeparator()

        # Quick text search — applied client-side across all visible columns.
        toolbar.addWidget(QLabel("Search:"))
        self._search_input = QLineEdit()
        self._search_input.setPlaceholderText("hostname, path, user…")
        self._search_input.setFixedWidth(200)
        self._search_input.textChanged.connect(self._apply_search_filter)
        toolbar.addWidget(self._search_input)
        toolbar.addSeparator()

        # Refresh button.
        self._refresh_btn = QPushButton("⟳ Refresh")
        self._refresh_btn.setToolTip("Fetch latest changes from the Falcon API")
        self._refresh_btn.clicked.connect(self._refresh)
        toolbar.addWidget(self._refresh_btn)

        # Suppress selected button.
        self._suppress_btn = QPushButton("🚫 Suppress")
        self._suppress_btn.setToolTip("Suppress selected change events")
        self._suppress_btn.setEnabled(not self._demo_mode)
        self._suppress_btn.clicked.connect(lambda: self._bulk_action("suppress"))
        toolbar.addWidget(self._suppress_btn)

        # Export CSV button.
        self._export_btn = QPushButton("⬇ Export CSV")
        self._export_btn.setToolTip("Export all visible rows to a CSV file")
        self._export_btn.clicked.connect(self._export_csv)
        toolbar.addWidget(self._export_btn)

        # ── Central widget: event table ───────────────────────────────────────
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(6, 6, 6, 6)

        # Table model + proxy (for client-side filtering and sorting).
        self._model = QStandardItemModel(0, 7, self)
        self._model.setHorizontalHeaderLabels([
            "Timestamp", "Hostname", "File Path", "Change Type", "User", "Process", "ID",
        ])

        self._proxy = QSortFilterProxyModel(self)
        self._proxy.setSourceModel(self._model)
        self._proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

        self._table = QTableView()
        self._table.setModel(self._proxy)
        self._table.setSortingEnabled(True)
        self._table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self._table.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self._table.doubleClicked.connect(self._open_detail)
        self._table.horizontalHeader().setSectionResizeMode(
            _COL_FILE_PATH, QHeaderView.ResizeMode.Stretch
        )
        # Hide the raw ID column from the user.
        self._table.setColumnHidden(_COL_CHANGE_ID, True)

        layout.addWidget(self._table)

        # ── Pagination row ────────────────────────────────────────────────────
        # Sits between the table and the status bar.  Controls which slice of
        # the (filtered) result set is visible in the table view.
        pagination_row = QHBoxLayout()

        self._prev_btn = QPushButton("← Prev")
        self._prev_btn.setToolTip("Go to previous page")
        self._prev_btn.setEnabled(False)
        self._prev_btn.clicked.connect(self._prev_page)
        pagination_row.addWidget(self._prev_btn)

        self._page_label = QLabel("Page 1 of 1")
        self._page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._page_label.setMinimumWidth(200)
        pagination_row.addWidget(self._page_label)

        self._next_btn = QPushButton("Next →")
        self._next_btn.setToolTip("Go to next page")
        self._next_btn.setEnabled(False)
        self._next_btn.clicked.connect(self._next_page)
        pagination_row.addWidget(self._next_btn)

        pagination_row.addStretch()

        pagination_row.addWidget(QLabel("Rows per page:"))
        self._page_size_combo = QComboBox()
        for opt in _PAGE_SIZE_OPTIONS:
            self._page_size_combo.addItem(str(opt), opt)
        self._page_size_combo.setSizeAdjustPolicy(
            QComboBox.SizeAdjustPolicy.AdjustToContents
        )
        self._page_size_combo.setMinimumWidth(70)
        # Select the default page size in the combo.
        default_idx = _PAGE_SIZE_OPTIONS.index(_DEFAULT_PAGE_SIZE) \
            if _DEFAULT_PAGE_SIZE in _PAGE_SIZE_OPTIONS else 0
        self._page_size_combo.setCurrentIndex(default_idx)
        self._page_size_combo.currentIndexChanged.connect(self._on_page_size_changed)
        pagination_row.addWidget(self._page_size_combo)

        layout.addLayout(pagination_row)

        # ── Status bar ────────────────────────────────────────────────────────
        self._status_bar = QStatusBar()
        self.setStatusBar(self._status_bar)
        self._total_label = QLabel("Total: 0")
        self._filtered_label = QLabel("Filtered: 0")
        self._selected_label = QLabel("Selected: 0")
        self._last_refresh_label = QLabel("Last refresh: —")
        self._status_bar.addPermanentWidget(self._total_label)
        self._status_bar.addPermanentWidget(QLabel("|"))
        self._status_bar.addPermanentWidget(self._filtered_label)
        self._status_bar.addPermanentWidget(QLabel("|"))
        self._status_bar.addPermanentWidget(self._selected_label)
        self._status_bar.addPermanentWidget(QLabel("|"))
        self._status_bar.addPermanentWidget(self._last_refresh_label)

        self._table.selectionModel().selectionChanged.connect(self._update_status)

    # ── Window lifecycle ──────────────────────────────────────────────────────

    def closeEvent(self, event) -> None:  # pylint: disable=invalid-name
        """Stop the auto-refresh timer and join all background threads before closing.

        ``quit()`` only works when a thread is spinning a Qt event loop, which
        ``FetchChangesWorker`` and ``SuppressWorker`` do not (they run blocking
        SDK calls).  Instead we signal interruption so the worker loops bail out
        on their next iteration, then ``wait()`` indefinitely until each thread
        actually exits — preventing the "QThread destroyed while running" abort.
        """
        self._timer.stop()
        for worker in (self._fetch_worker, self._suppress_worker):
            if worker and worker.isRunning():
                worker.requestInterruption()
                worker.wait()  # Block until the thread exits (no timeout — must finish).
        super().closeEvent(event)

    # ── Auto-refresh timer ────────────────────────────────────────────────────

    def _start_auto_refresh(self) -> None:
        """Set up a QTimer to trigger a background fetch every 30 seconds."""
        self._timer = QTimer(self)
        self._timer.setInterval(_AUTO_REFRESH_MS)
        self._timer.timeout.connect(self._auto_refresh)
        self._timer.start()

    def _toggle_auto_refresh(self, enabled: bool) -> None:
        """Start or stop the auto-refresh timer and update the Live indicator.

        Called when the Auto-refresh checkbox is toggled.  Enabling triggers an
        immediate refresh so the display is current before the next 30-second tick.
        Disabling preserves all loaded data — nothing is cleared.
        """
        if enabled:
            self._timer.start()
            self._auto_refresh()    # Not _refresh() — respects _progressive_loaded guard
        else:
            self._timer.stop()
        self._update_auth_indicator()

    def _update_auth_indicator(self) -> None:
        """Refresh the auth status chip to reflect the current auto-refresh state.

        In demo mode the indicator is fixed at "🔴 Demo" and is not changed.
        In live mode the indicator is green when auto-refresh is on and grey when off.
        """
        if self._demo_mode:
            return
        if self._auto_refresh_checkbox.isChecked():
            self._auth_label.setText("🟢 Live")
            self._auth_label.setStyleSheet("color: #6bff6b; font-weight: bold; padding: 0 8px;")
        else:
            self._auth_label.setText("⚫ Live")
            self._auth_label.setStyleSheet("color: #585b70; font-weight: bold; padding: 0 8px;")

    def _auto_refresh(self) -> None:
        """Periodic auto-refresh — suppressed while progressive data is loaded.

        When the user has navigated into progressively-loaded batches, a full
        refresh would wipe those records and reset the page counter to 1.
        We pause auto-refresh until the user manually triggers a full reload
        via the Refresh button, at which point ``_progressive_loaded`` is reset.
        """
        if self._progressive_loaded or self._load_more_in_flight:
            self._last_refresh_label.setText(
                f"Last refresh: {datetime.now().strftime('%H:%M:%S')} (paused)"
            )
            return
        self._refresh(preserve_page=True)

    # ── Pagination ────────────────────────────────────────────────────────────

    def _page_count(self) -> int:
        """Return total number of pages given current filtered row count and page size."""
        filtered = self._proxy.rowCount()
        if filtered == 0 or self._ui_page_size <= 0:
            return 1
        return max(1, math.ceil(filtered / self._ui_page_size))

    def _update_page_visibility(self) -> None:
        """Show only the rows that belong to the current page; hide all others.

        Iterates the proxy model's rows and calls setRowHidden() on the table
        view for each, so only the current page's slice is visible.  Also
        refreshes the Prev/Next button states and the page label.
        """
        page_count = self._page_count()
        # Clamp current page to a valid range in case filtered rows decreased.
        self._current_page = max(0, min(self._current_page, page_count - 1))

        start = self._current_page * self._ui_page_size
        end = start + self._ui_page_size
        total_filtered = self._proxy.rowCount()

        for row in range(total_filtered):
            self._table.setRowHidden(row, row < start or row >= end)

        on_last_page = self._current_page >= page_count - 1
        if on_last_page and self._has_more_api_data:
            page_text = f"Page {self._current_page + 1} of {page_count} (more available)"
        else:
            page_text = f"Page {self._current_page + 1} of {page_count}"
        self._page_label.setText(page_text)

        self._prev_btn.setEnabled(self._current_page > 0)
        # Next is enabled when there is a next UI page OR more API data to load.
        self._next_btn.setEnabled(
            self._current_page < page_count - 1 or (on_last_page and self._has_more_api_data)
        )
        self._update_status()

    def _prev_page(self) -> None:
        """Navigate to the previous page."""
        if self._current_page > 0:
            self._current_page -= 1
            self._update_page_visibility()

    def _next_page(self) -> None:
        """Navigate to the next page, fetching more from the API if needed."""
        page_count = self._page_count()
        on_last_page = self._current_page >= page_count - 1
        if on_last_page and self._has_more_api_data:
            # Trigger a background fetch for the next API batch, then advance.
            self._load_more()
        elif self._current_page < page_count - 1:
            self._current_page += 1
            self._update_page_visibility()

    def _on_page_size_changed(self) -> None:
        """Update rows-per-page and reset to page 0 when the selector changes."""
        self._ui_page_size = self._page_size_combo.currentData()
        self._current_page = 0
        self._update_page_visibility()

    # ── Data loading ──────────────────────────────────────────────────────────

    def _refresh(self, preserve_page: bool = False) -> None:
        """Start a background fetch if no fetch is already in progress.

        *preserve_page* – when True (auto-refresh path) the current page index
        is saved before the fetch and restored afterwards so the user's view
        does not jump back to page 1 on every 30-second timer tick.
        """
        if self._fetch_worker and self._fetch_worker.isRunning():
            return  # Debounce: skip if previous request is still in flight.
        if self._load_more_in_flight:
            return  # Prevent wiping table while load-more signal is queued.

        self._refresh_btn.setEnabled(False)
        self._status_bar.showMessage("Fetching changes…")
        # Stash the current page so _on_fetch_done can restore it when
        # this refresh was triggered by the auto-refresh timer.
        self._preserve_page_on_refresh = preserve_page

        if self._demo_mode:
            # Load demo fixtures synchronously — no network call needed.
            self._on_fetch_done(_DEMO_CHANGES, 0, False)
            return

        fql = self._fql_input.text().strip()
        self._fetch_worker = FetchChangesWorker(
            client_id=self._client_id,
            client_secret=self._client_secret,
            base_url=self._base_url,
            fql_filter=fql,
            start_offset=0,
            parent=self,
        )
        self._fetch_worker.finished.connect(self._on_fetch_done)
        self._fetch_worker.error.connect(self._on_fetch_error)
        self._fetch_worker.start()

    def _load_more(self) -> None:
        """Fetch the next batch of API results and append them to the table."""
        if self._fetch_worker and self._fetch_worker.isRunning():
            return

        # Set the in-flight guard before starting the worker.  This prevents
        # _refresh() from wiping the table in the race window between the
        # worker's run() returning and its finished() signal being delivered.
        self._load_more_in_flight = True
        self._next_btn.setEnabled(False)
        self._status_bar.showMessage("Loading more changes…")

        fql = self._fql_input.text().strip()
        self._fetch_worker = FetchChangesWorker(
            client_id=self._client_id,
            client_secret=self._client_secret,
            base_url=self._base_url,
            fql_filter=fql,
            start_offset=self._api_offset,
            parent=self,
        )
        self._fetch_worker.finished.connect(self._on_fetch_more_done)
        self._fetch_worker.error.connect(self._on_fetch_error)
        self._fetch_worker.start()

    def _on_fetch_done(self, changes: list[dict], next_offset: int, has_more: bool) -> None:
        """Populate the table model from the fresh change list (replaces existing rows)."""
        self._api_offset = next_offset
        self._has_more_api_data = has_more
        # Manual refresh always starts fresh — clear progressive mode flag so
        # auto-refresh resumes and page counter resets to 1.
        self._progressive_loaded = False
        self._changes_by_id = {c.get("id", ""): c for c in changes}
        self._model.removeRows(0, self._model.rowCount())

        for change in changes:
            self._append_change_row(change)

        self._last_refresh_label.setText(
            f"Last refresh: {datetime.now().strftime('%H:%M:%S')}"
        )
        self._refresh_btn.setEnabled(True)
        self._status_bar.clearMessage()
        # Preserve the current page on timer-triggered refreshes so the user's
        # view doesn't jump back to page 1 mid-navigation.  Always reset to
        # page 0 when the user manually clicks Refresh.
        if self._preserve_page_on_refresh:
            self._preserve_page_on_refresh = False
            # Clamp in case the new result set is smaller than the saved page.
        else:
            self._current_page = 0
        self._update_page_visibility()

    def _on_fetch_more_done(self, changes: list[dict], next_offset: int, has_more: bool) -> None:
        """Append a new batch of changes to the existing table rows."""
        self._load_more_in_flight = False  # Signal delivered — race window closed.
        self._api_offset = next_offset
        self._has_more_api_data = has_more
        # Mark that progressive data has been loaded so auto-refresh is suppressed.
        self._progressive_loaded = True
        for change in changes:
            if change.get("id", "") not in self._changes_by_id:
                self._changes_by_id[change.get("id", "")] = change
                self._append_change_row(change)

        self._status_bar.clearMessage()
        # Update visibility first so _page_count() reflects the newly appended rows,
        # then advance one page forward into the fresh data.
        self._update_page_visibility()
        self._current_page += 1
        self._update_page_visibility()

    def _append_change_row(self, change: dict) -> None:
        """Append one change record as a new row in the table model."""
        host = _get_nested(change, "host", "name")
        change_type = change.get("action_type", "")
        bg = _CHANGE_TYPE_COLOURS.get(change_type, "")
        row = [
            _make_item(_fmt_ts(change.get("action_timestamp", "")), bg),
            _make_item(host, bg),
            _make_item(_resolve_file_path(change), bg),
            _make_item(change_type, bg),
            _make_item(change.get("user_name", ""), bg),
            _make_item(change.get("process_image_file_name", ""), bg),
            _make_item(change.get("id", ""), bg),
        ]
        self._model.appendRow(row)

    def _on_fetch_error(self, message: str) -> None:
        """Show an error dialog and re-enable the Refresh button."""
        self._refresh_btn.setEnabled(True)
        if self._load_more_in_flight:
            # Load-more failed: clear the guard and restore Next so the user
            # can retry rather than being left with a permanently disabled button.
            self._load_more_in_flight = False
            self._update_page_visibility()  # re-enables Next if more data available
        self._status_bar.showMessage(f"Error: {message}", 10_000)
        QMessageBox.critical(self, "Fetch Error", message)

    # ── Filtering ─────────────────────────────────────────────────────────────

    def _apply_type_filter(self, change_type: str) -> None:
        """Filter table rows by change type (client-side proxy filter).

        Clears the search bar and resets to page 1 to avoid silent
        double-filter override and stale page state.
        """
        self._search_input.blockSignals(True)
        self._search_input.clear()
        self._search_input.blockSignals(False)
        if change_type == "All":
            self._proxy.setFilterKeyColumn(-1)
            self._proxy.setFilterFixedString("")
        else:
            self._proxy.setFilterKeyColumn(_COL_CHANGE_TYPE)
            self._proxy.setFilterFixedString(change_type)
        self._current_page = 0
        self._update_page_visibility()

    def _apply_search_filter(self, text: str) -> None:
        """Filter table rows by free-text across all visible columns.

        Resets the type dropdown to "All" and returns to page 1 when a search
        term is entered so both filters don't silently compete.
        """
        self._type_combo.blockSignals(True)
        self._type_combo.setCurrentIndex(0)  # "All"
        self._type_combo.blockSignals(False)
        self._proxy.setFilterKeyColumn(-1)
        self._proxy.setFilterFixedString(text)
        self._current_page = 0
        self._update_page_visibility()

    # ── Detail dialog ─────────────────────────────────────────────────────────

    def _open_detail(self, proxy_index) -> None:
        """Open the detail dialog for the double-clicked row."""
        source_index = self._proxy.mapToSource(proxy_index)
        id_item = self._model.item(source_index.row(), _COL_CHANGE_ID)
        if not id_item:
            return
        change_id = id_item.text()
        change = self._changes_by_id.get(change_id)
        if not change:
            return
        dialog = ChangeDetailDialog(
            change=change,
            client_id=self._client_id,
            client_secret=self._client_secret,
            base_url=self._base_url,
            parent=self,
        )
        # Refresh the main change list whenever a suppress/unsuppress/purge succeeds.
        dialog.refresh_requested.connect(self._refresh)
        # Purge is async on the API — remove the record client-side immediately
        # rather than re-fetching (which would still return the not-yet-deleted row).
        dialog.purge_completed.connect(lambda cid: self._remove_change_ids([cid]))
        dialog.exec()

    # ── Bulk actions ──────────────────────────────────────────────────────────

    def _bulk_action(self, operation: str) -> None:
        """Suppress or purge all selected rows via start_actions."""
        selected_rows = self._table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.information(self, "No Selection", "Select one or more rows first.")
            return

        # Collect change IDs from the hidden ID column.
        change_ids: list[str] = []
        for proxy_row in selected_rows:
            source_row = self._proxy.mapToSource(proxy_row).row()
            id_item = self._model.item(source_row, _COL_CHANGE_ID)
            if id_item and id_item.text() and not id_item.text().startswith("demo-"):
                change_ids.append(id_item.text())

        if not change_ids:
            QMessageBox.information(self, "Demo Mode",
                                    "Actions are disabled for demo data rows.")
            return

        reply = QMessageBox.question(
            self,
            f"Confirm {operation.title()}",
            f"Apply '{operation}' to {len(change_ids)} selected change(s)?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

        self._suppress_btn.setEnabled(False)
        self._status_bar.showMessage(f"Submitting {operation} action…")
        # Store for use in _on_action_done (needed by bulk purge client-side removal).
        self._bulk_operation = operation
        self._bulk_change_ids = list(change_ids)

        self._suppress_worker = SuppressWorker(
            client_id=self._client_id,
            client_secret=self._client_secret,
            base_url=self._base_url,
            change_ids=change_ids,
            operation=operation,
            comment=f"Bulk {operation} via FileVantage Change Monitor {_APP_VERSION}",
            parent=self,
        )
        self._suppress_worker.finished.connect(self._on_action_done)
        self._suppress_worker.error.connect(self._on_action_error)
        self._suppress_worker.start()

    def _on_action_done(self, message: str) -> None:
        """Handle successful bulk action completion.

        For purge: remove affected records client-side immediately (API deletion is
        async — calling _refresh() re-fetches from the API, which still returns the
        record until index propagation completes).

        For suppress/unsuppress: call _refresh() so the change list reflects the
        updated is_suppressed state on each record.
        """
        self._suppress_btn.setEnabled(True)
        self._status_bar.showMessage(message, 8_000)
        if self._bulk_operation == "purge":
            self._remove_change_ids(self._bulk_change_ids)
        else:
            self._refresh()

    def _on_action_error(self, message: str) -> None:
        """Show error dialog and re-enable action buttons."""
        self._suppress_btn.setEnabled(True)
        self._status_bar.showMessage(f"Action failed: {message}", 10_000)
        QMessageBox.critical(self, "Action Error", message)

    def _remove_change_ids(self, change_ids: list[str]) -> None:
        """Remove purged change records from the local model immediately.

        Purge deletion is async on the API — calling _refresh() after a purge
        re-fetches from query_changes, which still returns the not-yet-deleted
        record until index propagation completes.  Remove the records client-side
        instead so the user sees the effect immediately.
        """
        id_set = set(change_ids)
        for cid in id_set:
            self._changes_by_id.pop(cid, None)
        # Scan rows in reverse order (safe for removeRow) and remove matches.
        for row in range(self._model.rowCount() - 1, -1, -1):
            id_item = self._model.item(row, _COL_CHANGE_ID)
            if id_item and id_item.text() in id_set:
                self._model.removeRow(row)
        self._update_page_visibility()

    # ── Export ────────────────────────────────────────────────────────────────

    def _export_csv(self) -> None:
        """Export all currently-visible rows to a user-selected CSV file."""
        path, _ = QFileDialog.getSaveFileName(
            self, "Export to CSV", "filevantage_changes.csv",
            "CSV Files (*.csv);;All Files (*)"
        )
        if not path:
            return

        headers = ["Timestamp", "Hostname", "File Path", "Change Type", "User", "Process", "ID"]
        try:
            with open(path, "w", newline="", encoding="utf-8") as fh:
                writer = csv.writer(fh)
                writer.writerow(headers)
                for proxy_row in range(self._proxy.rowCount()):
                    row_data = []
                    for col in range(self._model.columnCount()):
                        source_index = self._proxy.mapToSource(
                            self._proxy.index(proxy_row, col)
                        )
                        item = self._model.item(source_index.row(), col)
                        row_data.append(item.text() if item else "")
                    writer.writerow(row_data)
            self._status_bar.showMessage(
                f"Exported {self._proxy.rowCount()} rows to {path}", 6_000
            )
        except OSError as exc:
            QMessageBox.critical(self, "Export Error", str(exc))

    # ── Status bar update ─────────────────────────────────────────────────────

    def _update_status(self) -> None:
        """Refresh the counts in the status bar."""
        total = self._model.rowCount()
        filtered = self._proxy.rowCount()
        selected = len(self._table.selectionModel().selectedRows())
        self._total_label.setText(f"Total: {total}")
        self._filtered_label.setText(f"Filtered: {filtered}")
        self._selected_label.setText(f"Selected: {selected}")


# ── Entry point ───────────────────────────────────────────────────────────────


def main() -> None:
    """Parse CLI arguments and environment, build QApplication, run event loop."""
    cmd = consume_arguments()

    app = QApplication(sys.argv)
    app.setApplicationName(_APP_TITLE)
    app.setApplicationVersion(_APP_VERSION)

    # Dark stylesheet for a Falcon-style dark UI.
    app.setStyleSheet("""
        QMainWindow, QDialog, QWidget {
            background-color: #1e1e2e;
            color: #cdd6f4;
        }
        QToolBar {
            background-color: #181825;
            border-bottom: 1px solid #313244;
            spacing: 4px;
            padding: 4px;
        }
        QToolBar QLabel {
            color: #bac2de;
        }
        QLineEdit, QComboBox {
            background-color: #313244;
            color: #cdd6f4;
            border: 1px solid #45475a;
            border-radius: 4px;
            padding: 3px 6px;
        }
        QPushButton {
            background-color: #313244;
            color: #cdd6f4;
            border: 1px solid #45475a;
            border-radius: 4px;
            padding: 4px 10px;
        }
        QPushButton:hover {
            background-color: #45475a;
        }
        QPushButton:disabled {
            color: #585b70;
            border-color: #313244;
        }
        QTableView {
            background-color: #181825;
            alternate-background-color: #1e1e2e;
            color: #cdd6f4;
            gridline-color: #313244;
            selection-background-color: #4c4f69;
        }
        QHeaderView::section {
            background-color: #313244;
            color: #cdd6f4;
            border: 1px solid #45475a;
            padding: 4px;
        }
        QStatusBar {
            background-color: #181825;
            color: #bac2de;
        }
        QTabWidget::pane {
            border: 1px solid #45475a;
        }
        QTabBar::tab {
            background-color: #313244;
            color: #cdd6f4;
            padding: 6px 14px;
        }
        QTabBar::tab:selected {
            background-color: #45475a;
        }
        QTextEdit, QGroupBox {
            background-color: #181825;
            color: #cdd6f4;
            border: 1px solid #313244;
            border-radius: 4px;
        }
        QGroupBox::title {
            color: #89b4fa;
            padding: 0 4px;
        }
        QScrollBar:vertical {
            background: #181825;
            width: 10px;
        }
        QScrollBar::handle:vertical {
            background: #45475a;
            border-radius: 4px;
        }
    """)

    window = FileVantageWindow(
        client_id=cmd.client_id or "",
        client_secret=cmd.client_secret or "",
        base_url=cmd.base_url or "",
    )
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
