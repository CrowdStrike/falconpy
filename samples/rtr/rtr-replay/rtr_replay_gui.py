r"""RTR Session Replay — Desktop GUI.

 _______ _______ ______         _______ _______ _______ _____   _______ ___ ___
|   _   |       |   _  \       |   _   |   _   |   _   |     | |   _   |   Y   |
|.  l   |.|   | |.  l   \      |.  l   |.  1___|.  1   |.    | |.  1   |.  1   |
|.  _   `-|.  |-|.  _   /      |.  l   |.  __) |.  ____|.    | |.  _   |.  _   |
|:  l   | |:  | |:  l   \      |:  l   |:  |   |:  |   |:  . | |:  |   |:  |   |
|::.. . | |::.| |::.. .  /     |::.. . |::.|   |::.|   |::. :| |::.|:. |::.|:. |
`-------' `---' `------^'      `-------`---'   `---'   `--:--' `--- ---`--- ---'

                                    RTR Audit Session Replay — Desktop GUI (v2)
                                    Uses: RealTimeResponseAudit
                                    Scope: real-time-response-audit:read

A PySide6 desktop application for browsing and replaying historical
CrowdStrike Falcon Real Time Response (RTR) sessions. It retrieves
audit data from the Falcon platform using the FalconPy SDK and presents
each session's command history in a scrollable replay view.

Prerequisites
-------------
  pip install crowdstrike-falconpy PySide6
  (or: pipenv install crowdstrike-falconpy PySide6)

Required API scope
------------------
  The API client must have the *real-time-response-audit:read* scope.
  This is separate from the live-session scope (real-time-response:read)
  and must be explicitly enabled in the Falcon API client settings.

Credentials
-----------
  Credentials can be supplied three ways (checked in this order):
    1. CLI flags (-k / -s)
    2. Environment variables FALCON_CLIENT_ID / FALCON_CLIENT_SECRET
    3. Typed directly into the credential panel at runtime

  The --demo flag bypasses credential requirements entirely, loading
  built-in fixture sessions so the UI can be explored without an API key.

Usage
-----
    pipenv run python3 rtr_replay_gui.py
    pipenv run python3 rtr_replay_gui.py --demo
    pipenv run python3 rtr_replay_gui.py -k KEY -s SECRET
    pipenv run python3 rtr_replay_gui.py -k KEY -s SECRET -b eu-1
    pipenv run python3 rtr_replay_gui.py -k KEY -s SECRET -n HOSTNAME
    pipenv run python3 rtr_replay_gui.py -k KEY -s SECRET -i SESSION_ID

CLI flags
---------
  -k / --client_id      Falcon API client ID
  -s / --client_secret  Falcon API client secret
  -b / --base_url       Cloud region (default: auto). Use for GovCloud.
  -n / --hostname       Pre-filter sessions to this hostname on load
  -i / --session_id     Auto-navigate to this session after loading
  --demo                Load fixture data, no credentials required

Architecture overview
---------------------
  RTRReplayWindow (QMainWindow)
  ├── Credential panel (QGroupBox) — API key input + region dropdown
  ├── Session list panel (QGroupBox, left splitter pane)
  │   ├── Filter bar (QLineEdit) — client-side substring filter
  │   ├── Date range row — From/To QDateEdit + Clear — server-side FQL
  │   ├── Session table (QTableView + QSortFilterProxyModel)
  │   └── Pagination row — Prev / Page N of M / Next
  └── Replay panel (QGroupBox, right splitter pane)
      ├── Metadata labels — host, operator, start time, duration
      └── Command log (QTextEdit, read-only monospace)

  API calls are made on a background QThread (FetchSessionsWorker)
  and results are delivered back to the main thread via Qt signals,
  keeping the UI responsive during network I/O.

Created by: Manjula Wickramasuriya (@Manjula101) - Enterprise Security Lab
Ridiculous GUI by: jshcodes@CrowdStrike
"""
# pylint: disable=too-many-lines
# pylint: disable=too-many-arguments,too-many-positional-arguments
# pylint: disable=too-many-locals,too-few-public-methods
# pylint: disable=too-many-instance-attributes,too-many-statements
import math
import os
import sys
from argparse import ArgumentParser, RawTextHelpFormatter
from datetime import datetime

# pylint: disable=import-error
from PySide6.QtCore import (
    Qt, QDate, QEvent, QThread, Signal, QSortFilterProxyModel,
    QMutex, QMutexLocker, QWaitCondition,
)
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDateEdit,
    QDialog,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QSizePolicy,
    QSpinBox,
    QSplitter,
    QStatusBar,
    QPushButton,
    QTableView,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from falconpy import (
    BaseURL, RealTimeResponseAudit, version as _falconpy_version
)
# pylint: enable=import-error

# ── Constants ────────────────────────────────────────────────────────────────

# Source code URL for the FalconPy samples/rtr directory.
_FALCONPY_SOURCE_URL = (
    "https://github.com/CrowdStrike/falconpy/tree/main/samples/rtr"
)

# Number of sessions to fetch per API page.  The RTR audit endpoint
# supports up to 1000.
_PAGE_SIZE = 60

# Preset page-size values for the per-page dropdown.
# The RTR audit API accepts limit 1–1000; presets stay within that range.
_PAGE_SIZE_OPTIONS = [20, 60, 100, 200, 500, 1000]
_PAGE_SIZE_DEFAULT = 60

# Background prefetch rate limit (ms between requests) and cache cap.
_PREFETCH_DELAY_MS = 1_000    # 1 req/second background rate limit
_PREFETCH_CACHE_LIMIT = 50    # max pages of session data held in memory

# Server-side sort options for the sort dropdown.
# Values are FQL sort expressions accepted by RTRAuditSessions
# (valid fields: created_at, updated_at, deleted_at).
_SORT_OPTIONS = [
    ("Newest first (default)", "created_at|desc"),
    ("Oldest first", "created_at|asc"),
    ("Last updated ↓", "updated_at|desc"),
    ("Last updated ↑", "updated_at|asc"),
]


def _asset_path(filename: str) -> str:
    """Return absolute path to a bundled image asset.

    Works in both development (assets next to script) and inside a
    PyInstaller .app bundle (assets extracted to sys._MEIPASS).
    """
    if hasattr(sys, "_MEIPASS"):
        # pylint: disable-next=protected-access
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


# Path to the CrowdStrike logo asset (red variant for dark backgrounds).
# The logo is optional — the UI renders normally if the file is absent.
_LOGO_PATH = _asset_path("cs-logo-red.png")
# FalconPy logo displayed in the upper-right of the credential panel.
_FALCONPY_LOGO_PATH = _asset_path("falconpy-logo.png")
# Punk spider easter-egg image.
_PUNK_SPIDER_PATH = _asset_path("punk-spider.png")

# Human-readable short labels for each CrowdStrike cloud region.
# The dict maps BaseURL enum names (e.g. "US1") to display strings
# (e.g. "US-1") without the full API hostname, keeping the dropdown
# compact.  The SDK value (m.value, e.g. "api.crowdstrike.com") is
# stored as Qt item data and retrieved via QComboBox.currentData().
_BASE_URL_LABELS = {
    "US1": "US-1",
    "US2": "US-2",
    "EU1": "EU-1",
    "USGOV1": "US-GOV-1",
    "USGOV2": "US-GOV-2",
}
# Build the option list at import time so the BaseURL enum is only
# iterated once.  AUTO is excluded because it is represented by the
# explicit "auto (default)" entry at index 0.
_BASE_URL_OPTIONS = [("auto (default)", "auto")] + [
    (_BASE_URL_LABELS.get(m.name, m.name), m.value)
    for m in BaseURL
    if m.name != "AUTO"
]


# ── Demo fixture ─────────────────────────────────────────────────────────────

# Built-in sample sessions used when --demo is passed or no credentials
# are available.  The structure mirrors the domain.Session schema returned
# by the RTRAuditSessions API endpoint (GET
# /real-time-response-audit/combined/sessions/v1 with
# with_command_info=True).  Each session contains:
#   id           — unique session UUID
#   device_id    — 32-hex-char CID of the target endpoint
#   hostname     — display name of the endpoint
#   user_id      — email of the session initiator; for async/offline-queued
#                  sessions CrowdStrike substitutes its internal service
#                  account ("async-rtr@crowdstrike.com"); direct API-client
#                  sessions may return "api-client-<uuid>" format; human
#                  sessions return the analyst email
#   user_uuid    — opaque UUID (not the api-client identifier; not used for
#                  display)
#   created_at   — ISO 8601 session start time
#   updated_at   — ISO 8601 session end time
#   duration     — session length in seconds (float)
#   offline_queued — True if commands were queued for offline execution
#   logs         — list of model.SessionLog command history records
_DEMO_SESSIONS = [
    {
        "id": "demo-session-abc123",
        "device_id": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
        "hostname": "WIN-WORKSTATION-42",
        "user_id": "analyst@example.com",
        "created_at": "2024-11-15T09:12:00Z",
        "updated_at": "2024-11-15T09:18:34Z",
        "duration": 394.0,
        "offline_queued": False,
        "logs": [
            {
                "id": 1,
                "base_command": "pwd",
                "command_string": "pwd",
                "current_directory": "C:\\Windows\\System32",
                "created_at": "2024-11-15T09:12:05Z",
            },
            {
                "id": 2,
                "base_command": "ls",
                "command_string": "ls -la",
                "current_directory": "C:\\Windows\\System32",
                "created_at": "2024-11-15T09:12:18Z",
            },
            {
                "id": 3,
                "base_command": "cd",
                "command_string": "cd C:\\Users\\Suspect\\AppData\\Roaming",
                "current_directory": "C:\\Windows\\System32",
                "created_at": "2024-11-15T09:13:45Z",
            },
            {
                "id": 4,
                "base_command": "ls",
                "command_string": "ls",
                "current_directory": "C:\\Users\\Suspect\\AppData\\Roaming",
                "created_at": "2024-11-15T09:13:47Z",
            },
            {
                "id": 5,
                "base_command": "get",
                "command_string": "get suspicious.exe",
                "current_directory": "C:\\Users\\Suspect\\AppData\\Roaming",
                "created_at": "2024-11-15T09:14:02Z",
            },
        ],
    },
    {
        "id": "demo-session-def456",
        "device_id": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5",
        "hostname": "LINUX-SERVER-07",
        # API client sessions use the "api-client-<uuid>" user_id format.
        # format_operator() strips the prefix and appends "(API)" so these
        # rows are visually distinct from human analyst sessions.
        "user_id": "api-client-abc123def456",
        "created_at": "2024-11-14T14:30:00Z",
        "updated_at": "2024-11-14T14:32:11Z",
        "duration": 131.0,
        "offline_queued": False,
        "logs": [
            {
                "id": 1,
                "base_command": "ls",
                "command_string": "ls /tmp",
                "current_directory": "/root",
                "created_at": "2024-11-14T14:30:08Z",
            },
            {
                "id": 2,
                "base_command": "cat",
                "command_string": "cat /tmp/payload.sh",
                "current_directory": "/root",
                "created_at": "2024-11-14T14:30:22Z",
            },
        ],
    },
]


# ── Argument parsing ─────────────────────────────────────────────────────────


def consume_arguments() -> object:
    """Parse and return command-line arguments for the GUI launcher.

    All arguments are optional — the window can be opened with no
    flags and credentials entered at runtime.  When credentials are
    supplied via flags they are pre-populated in the UI fields and can
    still be edited before clicking Load Sessions.

    Returns:
        argparse.Namespace with attributes: client_id, client_secret,
        base_url, hostname, session_id, demo.
    """
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawTextHelpFormatter
    )
    parser.add_argument(
        "-k", "--client_id",
        help="CrowdStrike Falcon API client ID.\n"
             "Can also be set via FALCON_CLIENT_ID env var.",
        required=False,
        default=os.getenv("FALCON_CLIENT_ID"),
    )
    parser.add_argument(
        "-s", "--client_secret",
        help="CrowdStrike Falcon API client secret.\n"
             "Can also be set via FALCON_CLIENT_SECRET env var.",
        required=False,
        default=os.getenv("FALCON_CLIENT_SECRET"),
    )
    parser.add_argument(
        "-b", "--base_url",
        help="CrowdStrike region base URL (default: auto).\n"
             "Only required for GovCloud tenants.",
        required=False,
        default="auto",
    )
    parser.add_argument(
        "-n", "--hostname",
        help="Filter sessions to this hostname on load.",
        required=False,
        default=None,
    )
    parser.add_argument(
        "-i", "--session_id",
        help="Auto-navigate to this session ID after loading.",
        required=False,
        default=None,
    )
    parser.add_argument(
        "--demo",
        help="Load built-in fixture data without credentials.",
        action="store_true",
        default=False,
    )
    return parser.parse_args()


# ── Formatting helpers ───────────────────────────────────────────────────────


def format_datetime(iso_str: str) -> str:
    """Convert an ISO 8601 datetime string to a local human-readable form.

    The Falcon API returns UTC timestamps ending in 'Z'.  Python 3.10
    does not recognise the 'Z' suffix natively, so it is replaced with
    the explicit '+00:00' offset before parsing.  The result is then
    converted to the system's local timezone for readability.

    Args:
        iso_str: ISO 8601 string, e.g. '2024-11-15T09:12:05Z'.
            May be None or empty.

    Returns:
        A local datetime string like '2024-11-15 09:12:05 PST',
        the original string if parsing fails, or '—' for empty input.
    """
    if not iso_str:
        return "—"
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    except ValueError:
        return iso_str


def format_duration(seconds: float) -> str:
    """Format a duration in seconds as a compact human-readable string.

    Args:
        seconds: Duration in seconds (float).  May be None.

    Returns:
        A string like '6m 34s' or '1h 03m 14s', or '—' if None.
    """
    if seconds is None:
        return "—"
    total = int(seconds)
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours}h {minutes:02d}m {secs:02d}s"
    return f"{minutes}m {secs:02d}s"


# The CrowdStrike internal service account that executes async/offline-queued
# RTR sessions.  When `offline_queued` is True, this account's email appears
# as `user_id` instead of the originating API client or human analyst identity.
_ASYNC_RTR_SERVICE_ACCOUNT = "async-rtr@crowdstrike.com"


def _extract_workflow_id(origin: str) -> str:
    """Extract the workflowExecutionId value from a session origin string.

    The ``origin`` field uses comma-separated ``key:value`` pairs::

        "source:async-rtr,deviceId:abc123,workflowExecutionId:uuid-here"

    Args:
        origin: The raw ``origin`` string from the session dict.

    Returns:
        The ``workflowExecutionId`` value, or ``""`` if not found.
    """
    if not origin:
        return ""
    for part in origin.split(","):
        key, sep, value = part.partition(":")
        if sep and key == "workflowExecutionId":
            return value
    return ""


def format_operator(user_id: str, origin: str = None) -> str:
    """Format a session user_id for display in the Operator column.

    The Falcon RTR audit API returns ``user_id`` in three formats:

    * Human analysts:   ``"firstname.lastname@company.com"``
    * Direct API clients: ``"api-client-<uuid32>"``
    * Async/offline sessions: ``"async-rtr@crowdstrike.com"`` — the
      CrowdStrike internal service account that executes commands on behalf
      of an API client when the target device was offline at session time.
      All ``offline_queued: True`` sessions will show this value.  When
      ``origin`` is supplied the ``workflowExecutionId`` is extracted and
      shown as the label.

    Examples::

        "analyst@example.com"            → "analyst@example.com"
        "api-client-abc123def456"        → "abc123def456 (API)"
        "async-rtr@crowdstrike.com"      → "Workflow execution: <id>"
        "async-rtr@crowdstrike.com"      → "Workflow execution"  (no origin)
        None / ""                        → "—"

    Args:
        user_id: The raw ``user_id`` string from the session dict.
        origin: Optional ``origin`` field from the session dict.  When
            provided and the session is async-RTR, the workflow execution
            ID is extracted and included in the display label.

    Returns:
        A display-friendly operator string suitable for table cells.
    """
    if not user_id:
        return "—"
    # Async/offline-queued sessions: show the workflow execution ID from
    # the origin field so each session is individually identifiable.
    if user_id == _ASYNC_RTR_SERVICE_ACCOUNT:
        wf_id = _extract_workflow_id(origin or "")
        if wf_id:
            return f"Workflow execution: {wf_id}"
        return "Workflow execution"
    prefix = "api-client-"
    if user_id.startswith(prefix):
        # Strip the prefix and flag the row as API-initiated.
        return user_id[len(prefix):] + " (API)"
    return user_id


# ── Background worker thread ─────────────────────────────────────────────────


class FetchSessionsWorker(QThread):
    """QThread worker that fetches one page of RTR audit sessions.

    Why a background thread?
    ------------------------
    All network I/O must happen off the Qt main thread to keep the UI
    responsive.  QThread is the standard PySide6 pattern for this: the
    worker is created on the main thread, but its run() method executes
    on a dedicated OS thread.  Results are delivered back to the main
    thread through Qt signals, which are automatically queued across
    thread boundaries by the Qt event loop.

    Signals
    -------
    finished(sessions: list, pagination: dict)
        Emitted on a successful API response.  ``sessions`` is the list
        of session dicts for the current page.  ``pagination`` is a dict
        with keys:
            'total'       (int)  — total sessions matching the filter
            'next_cursor' (str|None) — opaque cursor for the next page,
                                       or None if this is the last page.
    error(message: str)
        Emitted when the API returns a non-200 status or an unexpected
        exception occurs.  ``message`` is a human-readable description
        suitable for display in a QMessageBox.

    Usage
    -----
    Instantiate on the main thread, connect signals, then call start()::

        worker = FetchSessionsWorker(client_id, client_secret)
        worker.finished.connect(self._on_sessions_loaded)
        worker.error.connect(self._on_fetch_error)
        worker.start()
    """

    finished = Signal(list, dict)
    error = Signal(str)

    def __init__(self, client_id: str, client_secret: str,
                 base_url: str = "auto", offset: str = None,
                 fql_filter: str = None, sort: str = None,
                 page_size: int = _PAGE_SIZE_DEFAULT):
        """Initialise the worker with connection parameters.

        Args:
            client_id: CrowdStrike Falcon API client ID.
            client_secret: CrowdStrike Falcon API client secret.
            base_url: SDK base URL; 'auto' resolves to US-1 for standard
                tenants.  Pass an explicit value for GovCloud, e.g.
                'usgov1'.
            offset: Opaque pagination cursor returned by a previous API
                call (None = fetch the first page).  The RTR audit API
                uses string cursors rather than integer offsets, so
                forward-only pagination is maintained via a cursor list.
            fql_filter: Optional FQL filter string applied server-side,
                e.g. "hostname:'WIN-SERVER-01'".  Note: filtering by
                session 'id' via FQL is not supported by this endpoint;
                use client-side filtering instead.
            sort: Optional sort expression in the form
                "<field>|<direction>", e.g. "created_at|desc".  Valid
                sort fields: created_at, updated_at, deleted_at.  When
                None the API returns sessions in its default order.
            page_size: Number of sessions to request per page (1–1000).
                Defaults to ``_PAGE_SIZE_DEFAULT`` (60).
        """
        super().__init__()
        self._client_id = client_id
        self._client_secret = client_secret
        self._base_url = base_url
        self._offset = offset
        self._fql_filter = fql_filter
        self._sort = sort
        self._page_size = page_size

    def run(self):  # pylint: disable=too-many-locals
        """Execute the API call and emit finished or error.

        This method runs on the worker thread.  It:
        1. Instantiates a RealTimeResponseAudit SDK object.
        2. Calls audit_sessions() with with_command_info=True so that
           the command logs (model.SessionLog list) are included in the
           response.  Without this flag, the 'logs' field is absent.
        3. Extracts the pagination cursor from meta.pagination.next for
           use by the next-page fetch.
        4. Emits finished() or error() — never both.
        """
        try:
            # Instantiate the SDK here (on the worker thread) so that
            # the OAuth2 token exchange also happens off the main thread.
            sdk = RealTimeResponseAudit(
                client_id=self._client_id,
                client_secret=self._client_secret,
                base_url=self._base_url,
            )

            # Build the keyword arguments for audit_sessions().
            # with_command_info=True is required — without it the API
            # omits the 'logs' array entirely, returning only session
            # metadata with no command history.
            kwargs = {
                "with_command_info": True,
                "limit": str(self._page_size),
            }
            if self._offset:
                kwargs["offset"] = self._offset
            if self._fql_filter:
                kwargs["filter"] = self._fql_filter
            if self._sort:
                kwargs["sort"] = self._sort

            response = sdk.audit_sessions(**kwargs)
            status = response.get("status_code")

            if status != 200:
                # Surface all error messages from the response body.
                errors = response.get("body", {}).get("errors", [])
                messages = "; ".join(
                    f"[{e.get('code', '?')}] {e.get('message', '?')}"
                    for e in errors
                )
                self.error.emit(
                    f"API error HTTP {status}: "
                    + (messages or "Check credentials and "
                       "real-time-response-audit:read scope.")
                )
                return

            body = response["body"]
            sessions = body.get("resources") or []
            pagination = (body.get("meta") or {}).get("pagination") or {}

            # Emit the sessions and pagination metadata back to the main
            # thread.  The 'next' cursor is an opaque string the API uses
            # for forward-only paging — store it verbatim and pass it
            # back as the 'offset' on the next page fetch.
            self.finished.emit(sessions, {
                "total": pagination.get("total", 0),
                "next_cursor": pagination.get("next"),
            })

        except Exception as exc:  # pylint: disable=broad-except
            self.error.emit(f"Unexpected error: {exc}")


class PrefetchWorker(QThread):
    """Background QThread that walks page cursors ahead of the user.

    Fetches pages sequentially from a given starting cursor, emitting each
    discovered next-cursor (and the page's session data) to the main thread
    via Qt signals.  The main-thread slot is the sole writer to
    ``_page_cursors`` and ``_page_cache``, keeping mutations single-threaded.

    The worker can be paused (between requests) or stopped entirely:
    - ``pause()`` / ``resume()`` are used around foreground fetches so the
      foreground and background never overlap.
    - ``stop()`` is called when the cursor space is invalidated (Load,
      sort/filter/page-size change).

    Signals
    -------
    cursor_discovered(page_idx, next_cursor, sessions, pagination)
        Emitted after each successful page fetch.  ``page_idx`` is the
        0-based index of the page just fetched (whose cursor is
        ``next_cursor``).  ``sessions`` and ``pagination`` are cached by
        the main-thread slot.
    prefetch_done()
        Emitted when no further pages remain (``next_cursor`` is None or
        empty) or after ``stop()`` is acknowledged.
    prefetch_error(message)
        Emitted on a non-200 API response or unexpected exception.
        Non-fatal — the worker halts but the foreground path is unaffected.
    """

    cursor_discovered = Signal(int, str, list, dict)
    prefetch_done = Signal()
    prefetch_error = Signal(str)

    def __init__(self, client_id: str, client_secret: str,
                 base_url: str = "auto",
                 start_page: int = 1, start_cursor: str = None,
                 fql_filter: str = None, sort: str = None,
                 page_size: int = _PAGE_SIZE_DEFAULT):
        """Initialise the prefetch worker.

        Args:
            client_id: Falcon API client ID.
            client_secret: Falcon API client secret.
            base_url: SDK base URL (e.g. ``'auto'``, ``'usgov1'``).
            start_page: 0-based index of the *first* page to fetch.
                The worker walks from here until no more pages exist.
            start_cursor: Opaque cursor string for ``start_page``.
                Must not be None; page 0 (cursor=None) is never prefetched.
            fql_filter: FQL filter string (same as foreground fetch).
            sort: Sort expression (same as foreground fetch).
            page_size: Sessions per page (must match foreground page size).
        """
        super().__init__()
        self._client_id = client_id
        self._client_secret = client_secret
        self._base_url = base_url
        self._start_page = start_page
        self._start_cursor = start_cursor
        self._fql_filter = fql_filter
        self._sort = sort
        self._page_size = page_size

        self._pause_mutex = QMutex()
        self._pause_cond = QWaitCondition()
        self._paused = False
        self._stop = False

    def pause(self):
        """Ask the worker to pause between requests (thread-safe)."""
        with QMutexLocker(self._pause_mutex):
            self._paused = True

    def resume(self):
        """Wake the worker after a pause (thread-safe)."""
        with QMutexLocker(self._pause_mutex):
            self._paused = False
            self._pause_cond.wakeAll()

    def stop(self):
        """Ask the worker to exit at the next opportunity (thread-safe)."""
        with QMutexLocker(self._pause_mutex):
            self._stop = True
            self._paused = False          # wake if currently waiting
            self._pause_cond.wakeAll()

    def run(self):
        """Execute the background prefetch loop.

        Walks pages sequentially: sleep → API call → emit cursor.
        Stops on ``stop()``, a None next_cursor, or an API error.
        """
        cursor = self._start_cursor
        page = self._start_page

        while cursor and not self._stop:
            # ── Pause gate ───────────────────────────────────────────
            self._pause_mutex.lock()
            while self._paused and not self._stop:
                self._pause_cond.wait(self._pause_mutex)
            self._pause_mutex.unlock()
            if self._stop:
                break

            # ── Rate limit ───────────────────────────────────────────
            QThread.msleep(_PREFETCH_DELAY_MS)
            if self._stop:
                break

            # ── API call ─────────────────────────────────────────────
            try:
                sdk = RealTimeResponseAudit(
                    client_id=self._client_id,
                    client_secret=self._client_secret,
                    base_url=self._base_url,
                )
                kwargs = {
                    "with_command_info": True,
                    "limit": str(self._page_size),
                    "offset": cursor,
                }
                if self._fql_filter:
                    kwargs["filter"] = self._fql_filter
                if self._sort:
                    kwargs["sort"] = self._sort

                response = sdk.audit_sessions(**kwargs)
                if response.get("status_code") != 200:
                    self.prefetch_error.emit(
                        f"Prefetch HTTP {response.get('status_code')}"
                    )
                    return

                body = response["body"]
                sessions = body.get("resources") or []
                pagination = (body.get("meta") or {}).get("pagination") or {}
                next_cursor = pagination.get("next")

                self.cursor_discovered.emit(
                    page,
                    next_cursor or "",
                    sessions,
                    {
                        "total": pagination.get("total", 0),
                        "next_cursor": next_cursor,
                    },
                )
                cursor = next_cursor
                page += 1

            except Exception as exc:  # pylint: disable=broad-except
                self.prefetch_error.emit(str(exc))
                return

        self.prefetch_done.emit()


# Column index constants.
# platform_name is intentionally omitted — the RTR audit API always
# returns None for this field; showing it would add an empty column.
COL_HOST = 0        # Endpoint hostname
COL_OPERATOR = 1    # Analyst email or API client ID (formatted)
COL_STARTED = 2     # Session start time (local timezone)
COL_DURATION = 3    # Session length (formatted as Xm YYs)
COL_CMDS = 4        # Number of commands recorded (column label: "Commands")
COL_SESSION_ID = 5  # Full RTR session UUID (stretched to fill remaining width)


def build_session_model(sessions: list) -> QStandardItemModel:
    """Build a QStandardItemModel populated with one row per session.

    QTableView requires a model; QStandardItemModel is the simplest
    item-based model in Qt.  Each cell is a QStandardItem with editing
    disabled.  The model is later wrapped in a QSortFilterProxyModel
    by the caller so the user can sort and filter without mutating the
    underlying data.

    Numeric columns (Duration, Commands) use Qt.AlignRight so values line
    up cleanly.  All items use Qt.AlignVCenter for vertical centering.

    Args:
        sessions: List of session dicts from the RTR audit API.  Each
            dict should conform to the domain.Session schema.

    Returns:
        A fully populated QStandardItemModel ready to pass to
        QSortFilterProxyModel.setSourceModel().
    """
    headers = [
        "Host", "Operator", "Started", "Duration", "Commands", "Session ID"
    ]
    model = QStandardItemModel(len(sessions), len(headers))
    model.setHorizontalHeaderLabels(headers)

    for row, session in enumerate(sessions):
        # Count commands from the nested logs list.  The API returns []
        # when no commands were issued during the session.
        cmd_count = len(session.get("logs") or [])

        def make_item(text, align=Qt.AlignLeft):
            """Create a non-editable, aligned QStandardItem."""
            item = QStandardItem(str(text))
            item.setEditable(False)
            item.setTextAlignment(align | Qt.AlignVCenter)
            return item

        model.setItem(row, COL_HOST,
                      make_item(session.get("hostname") or "—"))
        model.setItem(row, COL_OPERATOR,
                      make_item(format_operator(
                          session.get("user_id"), session.get("origin")
                      )))
        model.setItem(row, COL_STARTED,
                      make_item(format_datetime(session.get("created_at"))))
        model.setItem(row, COL_DURATION, make_item(
            format_duration(session.get("duration")), Qt.AlignRight,
        ))
        model.setItem(
            row, COL_CMDS, make_item(str(cmd_count), Qt.AlignRight)
        )
        model.setItem(row, COL_SESSION_ID,
                      make_item(session.get("id") or "—"))

    return model


# ── Main window ──────────────────────────────────────────────────────────────


class _ClickableLabel(QLabel):
    """QLabel that emits a ``ctrl_shift_clicked`` signal on Ctrl+Shift+click.

    Used for the FalconPy logo to trigger the easter-egg dialog without
    affecting normal label behaviour for plain clicks.
    """

    ctrl_shift_clicked = Signal()

    def mousePressEvent(self, event):  # pylint: disable=invalid-name
        """Emit ctrl_shift_clicked when both Ctrl and Shift are held."""
        mods = event.modifiers()
        if (mods & Qt.ControlModifier) and (mods & Qt.ShiftModifier):
            self.ctrl_shift_clicked.emit()
        else:
            super().mousePressEvent(event)


class _SmartDateEdit(QDateEdit):
    """QDateEdit that opens its calendar popup at the current month.

    The standard ``QDateEdit`` always opens the calendar popup at the page
    corresponding to its current value.  When the sentinel "no date" value
    (``minimumDate()``) is active, the popup would open in January 2000 —
    unhelpful for users who want to pick a recent date.

    This subclass installs an event filter on the embedded
    ``QCalendarWidget`` so that whenever the popup *shows* while the
    widget is still at its minimum (sentinel) value, the calendar page is
    automatically advanced to the current month.  The selected date is not
    changed, so the widget still reads "(any)" and no ``dateChanged``
    signal fires.

    Usage is identical to ``QDateEdit``; the calendar popup is enabled
    automatically in ``__init__``.
    """

    def __init__(self, parent=None):
        """Initialise with calendar popup and patch the embedded calendar."""
        super().__init__(parent)
        self.setCalendarPopup(True)
        # The QCalendarWidget is created lazily by Qt on first popup open,
        # so calendarWidget() may return None here.  We install the filter
        # eagerly if the widget already exists; otherwise we patch it on
        # the first showEvent (see below).
        self._cal_filter_installed = False
        cal = self.calendarWidget()
        if cal is not None:
            cal.installEventFilter(self)
            self._cal_filter_installed = True

    def showEvent(self, event):  # pylint: disable=invalid-name
        """Ensure the calendar event filter is installed before first show."""
        if not self._cal_filter_installed:
            cal = self.calendarWidget()
            if cal is not None:
                cal.installEventFilter(self)
                self._cal_filter_installed = True
        super().showEvent(event)

    def eventFilter(self, watched, event):  # pylint: disable=invalid-name
        """Navigate calendar to today's month when sentinel value is active.

        Args:
            watched: The object being watched (the embedded QCalendarWidget).
            event: The Qt event to inspect.

        Returns:
            False — the event is never consumed; Qt continues processing.
        """
        if (
            event.type() == QEvent.Type.Show
            and watched is self.calendarWidget()
            and self.date() == self.minimumDate()
        ):
            today = QDate.currentDate()
            watched.setCurrentPage(today.year(), today.month())
        return False


class SessionFilterProxy(QSortFilterProxyModel):
    """QSortFilterProxyModel with case-insensitive substring matching.

    Wraps the built-in ``setFilterFixedString`` / ``setFilterKeyColumn``
    behaviour with a convenient subclass so future filter extensions have
    a natural home.

    Usage::

        proxy = SessionFilterProxy()
        proxy.setSourceModel(source_model)
        proxy.setFilterKeyColumn(-1)          # all-column text filter
        proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)
        proxy.setFilterFixedString("WIN")
    """


class RTRReplayWindow(QMainWindow):  # pylint: disable=too-few-public-methods
    """Main application window for the RTR Session Replay GUI.

    Layout
    ------
    The window is divided into three visual zones:

    1. **Credential panel** (top, fixed height): QLineEdit fields for
       client ID and secret, a QComboBox for cloud region, and action
       buttons.  Credentials can be pre-populated from CLI args or env
       vars, or entered manually at runtime.

    2. **Splitter** (centre, fills remaining height):
       - *Left pane* — Session list: a filter bar, a sortable/filterable
         QTableView showing sessions from the current page, and a
         pagination row with Prev / Page N of M / Next controls.
       - *Right pane* — Replay panel: metadata labels (host, operator,
         start time, duration) and a read-only monospace QTextEdit that
         shows the command log for the selected session.

    3. **Status bar** (bottom): a single-line message strip showing the
       current action state (loading, error, row count, etc.).

    State management
    ----------------
    Pagination uses a cursor list rather than integer page offsets
    because the RTR audit API returns opaque string cursors::

        _page_cursors[0] = None          # first page (no cursor)
        _page_cursors[1] = "eyJh..."     # cursor for page 2
        _page_cursors[2] = "eyJi..."     # cursor for page 3
        ...

    The list grows as the user navigates forward.  Going back simply
    re-uses the already-stored cursor.  The total session count is
    obtained from meta.pagination.total in the first API response.

    Attributes
    ----------
    _sessions : list
        Session dicts for the currently displayed page.
    _worker : FetchSessionsWorker | None
        Active background fetch thread, or None when idle.
    _demo_mode : bool
        True when running with built-in fixture data.
    _proxy_model : QSortFilterProxyModel | None
        The sort/filter proxy wrapping the current page's model.
    _auto_session_id : str | None
        Session ID to auto-select on first page load (from -i flag).
    _auto_hostname : str | None
        Hostname FQL filter to apply on load (from -n flag).
    _page_cursors : list[str | None]
        Accumulated pagination cursors; index == page number.
    _current_page : int
        Zero-based index of the currently displayed page.
    _total_sessions : int
        Total sessions matching the current filter (from API metadata).
    _date_from : QDateEdit
        Start date of the date range filter (inclusive).  Null date
        (isValid() == False) means no lower bound.
    _date_to : QDateEdit
        End date of the date range filter (inclusive).  Null date means
        no upper bound.
    _current_session : dict | None
        The session dict most recently displayed in the replay panel.
        Used by _on_copy_commands to extract command strings without
        re-parsing the QTextEdit content.
    """

    def __init__(self, demo_mode: bool = False, prefill_id: str = "",
                 prefill_secret: str = "", prefill_base_url: str = "auto",  # nosec - FP from bandit
                 auto_hostname: str = None, auto_session_id: str = None):
        """Initialise the main window, build widgets, and load demo data.

        Widget attributes (e.g. _id_field, _session_table) are declared
        as None here and assigned in the _build_* methods.  This keeps
        the constructor short and satisfies pylint's attribute-defined-
        outside-init check.

        Args:
            demo_mode: If True, load fixture sessions on startup without
                requiring API credentials.
            prefill_id: Client ID pre-populated into the ID field
                (from -k CLI flag or FALCON_CLIENT_ID env var).
            prefill_secret: Client secret pre-populated into the secret
                field (from -s flag or FALCON_CLIENT_SECRET env var).
            prefill_base_url: SDK base URL to pre-select in the region
                dropdown (from -b flag, default 'auto').
            auto_hostname: When set, builds an FQL filter
                "hostname:'<value>'" that is passed to every API fetch.
                Also pre-populates the UI filter field for visibility.
            auto_session_id: When set, the matching session row is
                automatically selected after the first page loads.
                Only works if the session is on the first page.
        """
        super().__init__()

        # ── Pagination state ──────────────────────────────────────────
        # _page_cursors[i] is the cursor needed to fetch page i.
        # Index 0 is always None (first page needs no cursor).
        self._sessions = []
        self._worker = None
        self._prefetch_worker: PrefetchWorker | None = None
        self._stopping_workers: set = set()
        self._demo_mode = demo_mode
        self._proxy_model = None
        self._auto_session_id = auto_session_id
        self._auto_hostname = auto_hostname
        self._page_cursors = [None]
        self._current_page = 0
        self._total_sessions = 0
        # Target page for a jump-to-page request that requires auto-fetching
        # forward through uncached pages.  None when no jump is in progress.
        self._jump_target_page: int | None = None
        # Cache of already-fetched page data keyed by page index.
        # Allows prev/next navigation without re-querying the API.
        self._page_cache: dict = {}
        # Tracks whether at least one successful API load has occurred,
        # used to update the Load button label to "Reload Sessions".
        self._has_loaded = False
        # Page size is configurable via the per-page dropdown.
        # Initialised to the default; updated when the dropdown changes.
        self._page_size = _PAGE_SIZE_DEFAULT

        # ── Credential pre-fill values ────────────────────────────────
        self._prefill_id = prefill_id
        self._prefill_secret = prefill_secret
        self._prefill_base_url = prefill_base_url

        # ── Widget attribute declarations ─────────────────────────────
        # All set to None here; assigned in the _build_* methods below.
        self._id_field = None
        self._secret_field = None
        self._base_url_combo = None
        self._load_btn = None
        self._demo_btn = None
        self._filter_field = None
        self._sort_combo = None
        self._page_size_combo = None
        self._date_from = None
        self._date_to = None
        self._session_table = None
        self._session_count_label = None
        self._prev_btn = None
        self._next_btn = None
        self._page_label = None
        self._page_jump = None
        self._go_btn = None
        self._cancel_btn = None
        self._prefetch_label = None
        self._meta_host = None
        self._meta_operator = None
        self._meta_started = None
        self._meta_duration = None
        self._meta_session_id = None
        self._command_log = None
        self._copy_cmds_btn = None
        self._copy_log_btn = None
        self._current_session = None
        self._status_bar = None

        self.setWindowTitle(
            "CrowdStrike Falcon - Real Time Response Session Replay"
        )
        self.resize(1200, 720)
        self._build_ui()

        # Load fixture data immediately if demo mode is active.
        if demo_mode:
            self._load_demo()

    # ── UI construction ──────────────────────────────────────────────────────

    def _build_ui(self):
        """Construct the top-level layout and assemble all panels.

        The credential panel is pinned to the top (fixed height).
        A QSplitter fills the remaining space with a 3:2 ratio between
        the session list (left) and the replay panel (right).
        The status bar is registered with QMainWindow for automatic
        bottom-edge placement.
        """
        central = QWidget()
        self.setCentralWidget(central)
        root_layout = QVBoxLayout(central)
        root_layout.setSpacing(6)
        root_layout.setContentsMargins(10, 8, 10, 6)

        root_layout.addWidget(self._build_credential_panel())

        # QSplitter lets the user resize both panes at runtime.
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self._build_session_list_panel())
        splitter.addWidget(self._build_replay_panel())
        # 3:2 default split — session list gets more space initially.
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 2)
        root_layout.addWidget(splitter)

        self._status_bar = QStatusBar()
        self.setStatusBar(self._status_bar)
        self._status_bar.showMessage(
            "Enter credentials and click Load Sessions, or use Demo."
        )

    def _build_credential_panel(self) -> QGroupBox:
        """Build the branded header + API credential panel at the top.

        The panel has two rows:

        Row 1 — Branded header
            Logo (if present) | "Real Time Response Replay" title in CS red
        Row 2 — Credentials
            Client ID | Secret | Region ▼ | Load Sessions | Demo

        Separating the logo and title into their own row frees horizontal
        space for the credential row, eliminating button text clipping.

        Returns:
            A configured QGroupBox widget.
        """
        group = QGroupBox("API Credentials")
        group.setMaximumHeight(120)
        # Outer layout: left content (2 rows) | gap | falconpy logo stack
        # root has stretch=0 so it stays at its natural minimum width (the
        # width of the credential row).  right_layout is placed 60px to the
        # right of root's right edge — i.e. 60px past the Demo button.
        # outer.addStretch() absorbs the remaining window width on the right.
        outer = QHBoxLayout(group)
        outer.setContentsMargins(8, 4, 8, 4)
        outer.setSpacing(20)

        # Left side: two rows stacked in a QVBoxLayout
        root = QVBoxLayout()
        root.setSpacing(4)
        # stretch=0: root stays at its natural minimum width so the logo
        # is placed relative to the Demo button, not the window edge.
        outer.addLayout(root, stretch=0)

        # ── Row 1: Logo + title ───────────────────────────────────────
        header_layout = QHBoxLayout()
        header_layout.setSpacing(10)

        if os.path.exists(_LOGO_PATH):
            logo_pixmap = QPixmap(_LOGO_PATH)
            scaled = logo_pixmap.scaledToHeight(32, Qt.SmoothTransformation)
            logo_label = QLabel()
            logo_label.setPixmap(scaled)
            logo_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            header_layout.addWidget(logo_label)

        title_label = QLabel("Real Time Response Session Replay")
        title_font = QFont()
        title_font.setPointSize(21)
        title_font.setBold(True)
        title_label.setFont(title_font)
        # CS primary red for the branded title; pull up 12 px via margin.
        title_label.setStyleSheet("color: #ec0000; margin-top: -13px;")
        title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        root.addLayout(header_layout)

        # ── Row 2: Credentials ────────────────────────────────────────
        cred_layout = QHBoxLayout()
        cred_layout.setSpacing(8)

        # Client ID
        cred_layout.addWidget(QLabel("Client ID:"))
        self._id_field = QLineEdit()
        self._id_field.setPlaceholderText("FALCON_CLIENT_ID")
        # Prefer explicitly passed value, fall back to env var.
        self._id_field.setText(
            self._prefill_id or os.getenv("FALCON_CLIENT_ID") or ""
        )
        self._id_field.setMinimumWidth(220)
        cred_layout.addWidget(self._id_field)

        # Client Secret
        cred_layout.addWidget(QLabel("Secret:"))
        self._secret_field = QLineEdit()
        self._secret_field.setPlaceholderText("FALCON_CLIENT_SECRET")
        self._secret_field.setText(
            self._prefill_secret or os.getenv("FALCON_CLIENT_SECRET") or ""
        )
        # Password mode hides the secret from shoulder-surfing.
        self._secret_field.setEchoMode(QLineEdit.Password)
        self._secret_field.setMinimumWidth(220)
        cred_layout.addWidget(self._secret_field)

        # Region dropdown — populated from FalconPy BaseURL enum.
        # Short label displayed; SDK hostname stored as item data.
        cred_layout.addWidget(QLabel("Region:"))
        self._base_url_combo = QComboBox()
        self._base_url_combo.setMinimumWidth(130)
        self._base_url_combo.setToolTip("Select your CrowdStrike region.")
        default_idx = 0
        for idx, (label, value) in enumerate(_BASE_URL_OPTIONS):
            self._base_url_combo.addItem(label, value)
            if value == self._prefill_base_url:
                default_idx = idx
        self._base_url_combo.setCurrentIndex(default_idx)
        cred_layout.addWidget(self._base_url_combo)

        # Vertical divider
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        cred_layout.addWidget(line)

        # Action buttons
        self._load_btn = QPushButton("Load Sessions")
        self._load_btn.setMinimumWidth(135)
        self._load_btn.setMinimumHeight(28)
        self._load_btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self._load_btn.clicked.connect(self._on_load_clicked)
        cred_layout.addWidget(self._load_btn)

        self._demo_btn = QPushButton("Demo")
        self._demo_btn.setMinimumWidth(70)
        self._demo_btn.setMinimumHeight(28)
        self._demo_btn.clicked.connect(self._load_demo)
        cred_layout.addWidget(self._demo_btn)
        root.addLayout(cred_layout)

        # ── Right side: FalconPy logo + text to the right ────────────
        # right_layout sits 60px to the right of root's right edge (the
        # Demo button), controlled by outer.setSpacing(60).
        # outer.addStretch() below absorbs remaining window width.
        #
        # Logo is on the LEFT; source link and version label stack
        # vertically to the RIGHT with an 8px horizontal gap.
        if os.path.exists(_FALCONPY_LOGO_PATH):
            fp_pixmap = QPixmap(_FALCONPY_LOGO_PATH)
            # Available height: 120 (max) - ~20 (title bar) - 8 (outer
            # top+bottom) - 16 (right_layout top+bottom) = ~76px.
            # Use 70px display height (140px supersample) for a clean fit.
            fp_big = fp_pixmap.scaledToHeight(
                160, Qt.SmoothTransformation
            )
            fp_scaled = fp_big.scaledToHeight(
                80, Qt.SmoothTransformation
            )
            fp_label = _ClickableLabel(self)
            fp_label.setPixmap(fp_scaled)
            fp_label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            fp_label.setContentsMargins(0, 0, 0, 0)
            fp_label.ctrl_shift_clicked.connect(self._show_easter_egg)

            # Clickable "Source code" hyperlink.
            link_label = QLabel(
                f'<a href="{_FALCONPY_SOURCE_URL}" '
                f'style="color:#0066cc; font-size:9pt; '
                f'font-weight:bold;">Source code</a>'
            )
            link_label.setOpenExternalLinks(True)
            link_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            # Installed FalconPy version in CS red.
            version_label = QLabel(f"FalconPy v{_falconpy_version()}")
            version_label.setStyleSheet(
                "color: #ec0000; font-size: 9pt; font-weight: bold;"
            )
            version_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            # Text stacked vertically to the right of the logo image.
            text_vbox = QVBoxLayout()
            text_vbox.setContentsMargins(0, 0, 0, 0)
            text_vbox.setSpacing(4)
            text_vbox.addStretch()
            text_vbox.addWidget(link_label)
            text_vbox.addWidget(version_label)
            text_vbox.addStretch()

            # HBox: logo | 8px gap | text column
            logo_hbox = QHBoxLayout()
            logo_hbox.setContentsMargins(0, 0, 0, 0)
            logo_hbox.setSpacing(8)
            logo_hbox.addWidget(fp_label)
            logo_hbox.addLayout(text_vbox)

            right_layout = QVBoxLayout()
            right_layout.setSpacing(0)
            right_layout.setContentsMargins(0, 8, 0, 8)
            right_layout.addLayout(logo_hbox)
            right_layout.addStretch()
            outer.addLayout(right_layout)
            # Absorb remaining horizontal space so right_layout stays close
            # to the Demo button rather than floating to the window edge.
            outer.addStretch()

        return group

    def _build_session_list_panel(self) -> QGroupBox:
        """Build the left splitter pane: filters, table, and pagination.

        Row 1 — Text filter
        -------------------
        A QLineEdit provides real-time client-side substring search across
        all visible columns (hostname, operator, session ID, etc.).

        Row 2 — Sort order + Per-page size + Date range
        ------------------------------------------------
        A sort QComboBox lets the user choose the server-side sort order
        (e.g. "Newest first", "Oldest first").  The selection is passed
        as the ``sort`` parameter to the API on the next load, so it
        applies to all results — not just the current page.  Column-
        header sorting is intentionally disabled to avoid the confusing
        "sorts current page only" behaviour; the sort dropdown is the
        single clear control for result ordering.

        A per-page QComboBox sets how many sessions are fetched per API
        call (presets: 20 / 40 / 60 / 100 / 200; API max: 1000).
        Changing either control triggers an automatic reset + re-fetch
        if sessions are already loaded.

        Two QDateEdit widgets (calendar popup) for From / To date
        bounds follow inline on the same row.  Applied server-side as
        FQL created_at range on the next Load Sessions call.

        Row 3 — Session table
        ----------------------
        QTableView backed by SessionFilterProxy.  Column-header sorting
        is disabled to avoid per-page-only confusion.

        Row 4 — Pagination row
        -----------------------
        Count label | Prev | Page N of M | Next | Go to: N [Go]

        The "Go to page" spinbox jumps directly to a cached page (one
        whose cursor is already stored in ``_page_cursors``).  Jumping
        to pages not yet fetched is blocked with a status bar message,
        since the RTR audit API uses opaque forward-only cursors.

        Returns:
            A configured QGroupBox widget.
        """
        group = QGroupBox("Sessions")
        layout = QVBoxLayout(group)

        # ── Row 1: Text filter + Operator dropdown ────────────────────
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Filter:"))
        self._filter_field = QLineEdit()
        self._filter_field.setPlaceholderText(
            "hostname, operator, or session ID…"
        )
        if self._auto_hostname:
            self._filter_field.setText(self._auto_hostname)
        self._filter_field.textChanged.connect(self._on_filter_changed)
        filter_layout.addWidget(self._filter_field)
        layout.addLayout(filter_layout)

        # ── Row 2: Sort order + Per-page size ─────────────────────────
        sort_paging_layout = QHBoxLayout()
        sort_paging_layout.addWidget(QLabel("Sort:"))
        self._sort_combo = QComboBox()
        self._sort_combo.setMinimumWidth(200)
        for label, value in _SORT_OPTIONS:
            self._sort_combo.addItem(label, value)
        self._sort_combo.setToolTip(
            "Server-side sort order applied to all results. "
            "Changing this reloads from page 1 if sessions are loaded."
        )
        self._sort_combo.currentIndexChanged.connect(
            self._on_sort_changed
        )
        sort_paging_layout.addWidget(self._sort_combo)

        sort_paging_layout.addSpacing(16)
        sort_paging_layout.addWidget(QLabel("Per page:"))
        self._page_size_combo = QComboBox()
        for size in _PAGE_SIZE_OPTIONS:
            self._page_size_combo.addItem(str(size), size)
        # Pre-select the default page size.
        default_idx = _PAGE_SIZE_OPTIONS.index(_PAGE_SIZE_DEFAULT)
        self._page_size_combo.setCurrentIndex(default_idx)
        self._page_size_combo.setMinimumWidth(80)
        self._page_size_combo.setToolTip(
            "Records per page (API max: 1000). "
            "Changing this reloads from page 1 if sessions are loaded."
        )
        self._page_size_combo.currentIndexChanged.connect(
            self._on_page_size_changed
        )
        sort_paging_layout.addWidget(self._page_size_combo)

        sort_paging_layout.addSpacing(16)
        sort_paging_layout.addWidget(QLabel("From:"))
        self._date_from = _SmartDateEdit()
        self._date_from.setDisplayFormat("yyyy-MM-dd")
        self._date_from.setSpecialValueText("(any)")
        self._date_from.setMinimumDate(QDate(2000, 1, 1))
        # Default to minimumDate() so the filter starts blank/inactive.
        # _SmartDateEdit navigates the calendar popup to today's month
        # automatically, so the user does not have to scroll from year 2000.
        self._date_from.setDate(self._date_from.minimumDate())
        self._date_from.setToolTip(
            "Start date filter (inclusive). Leave at (any) for no lower "
            "bound. Applied server-side via FQL; changing the date "
            "automatically re-fetches results."
        )
        sort_paging_layout.addWidget(self._date_from)

        sort_paging_layout.addWidget(QLabel("To:"))
        self._date_to = _SmartDateEdit()
        self._date_to.setDisplayFormat("yyyy-MM-dd")
        self._date_to.setSpecialValueText("(any)")
        self._date_to.setMinimumDate(QDate(2000, 1, 1))
        # Default to minimumDate() so the filter starts blank/inactive.
        self._date_to.setDate(self._date_to.minimumDate())
        self._date_to.setToolTip(
            "End date filter (inclusive, extended to 23:59:59 UTC). "
            "Leave at (any) for no upper bound. Changing the date "
            "automatically re-fetches results."
        )
        sort_paging_layout.addWidget(self._date_to)

        # Re-fetch whenever either date picker changes so the server-side
        # FQL created_at filter is applied automatically.
        self._date_from.dateChanged.connect(self._on_date_changed)
        self._date_to.dateChanged.connect(self._on_date_changed)

        clear_date_btn = QPushButton("Clear Dates")
        clear_date_btn.setToolTip("Remove the date range filter.")
        clear_date_btn.clicked.connect(self._on_clear_dates)
        sort_paging_layout.addWidget(clear_date_btn)
        sort_paging_layout.addStretch()
        layout.addLayout(sort_paging_layout)

        # ── Row 4: Session table ───────────────────────────────────────
        self._session_table = QTableView()
        # Column sorting is intentionally disabled: QSortFilterProxyModel
        # only sorts the current page (60 records), which misleads users
        # into thinking all results are reordered.  Use the Sort dropdown
        # above for server-side ordering of the full result set instead.
        self._session_table.setSortingEnabled(False)
        self._session_table.setSelectionBehavior(QTableView.SelectRows)
        self._session_table.setSelectionMode(QTableView.SingleSelection)
        self._session_table.setEditTriggers(QTableView.NoEditTriggers)
        self._session_table.setAlternatingRowColors(True)
        self._session_table.verticalHeader().setVisible(False)
        header = self._session_table.horizontalHeader()
        header.setStretchLastSection(True)
        self._session_table.setShowGrid(False)
        self._session_table.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        layout.addWidget(self._session_table)

        # ── Row 5: Pagination controls ────────────────────────────────
        paging_layout = QHBoxLayout()
        self._session_count_label = QLabel("No sessions loaded.")
        paging_layout.addWidget(self._session_count_label)
        paging_layout.addStretch()

        self._prev_btn = QPushButton("◀ Prev")
        self._prev_btn.setEnabled(False)
        self._prev_btn.setMaximumWidth(80)
        self._prev_btn.clicked.connect(self._on_prev_page)
        paging_layout.addWidget(self._prev_btn)

        self._page_label = QLabel("Page — of —")
        self._page_label.setAlignment(Qt.AlignCenter)
        self._page_label.setMinimumWidth(100)
        paging_layout.addWidget(self._page_label)

        self._next_btn = QPushButton("Next ▶")
        self._next_btn.setEnabled(False)
        self._next_btn.setMaximumWidth(80)
        self._next_btn.clicked.connect(self._on_next_page)
        paging_layout.addWidget(self._next_btn)

        # Go-to-page: a QSpinBox + button for direct page navigation.
        # Jumping to a page is only possible if its cursor is already
        # cached (i.e. the user navigated forward through prior pages).
        paging_layout.addSpacing(12)
        paging_layout.addWidget(QLabel("Go to:"))
        self._page_jump = QSpinBox()
        self._page_jump.setMinimum(1)
        self._page_jump.setMaximum(1)
        self._page_jump.setMinimumWidth(80)
        self._page_jump.setMinimumHeight(36)
        self._page_jump.setAlignment(Qt.AlignCenter)
        spinbox_font = QFont()
        spinbox_font.setPointSize(12)
        self._page_jump.setFont(spinbox_font)
        self._page_jump.setToolTip(
            "Jump directly to a page number. Pages beyond the furthest "
            "fetched will be auto-fetched by chaining API calls."
        )
        paging_layout.addWidget(self._page_jump)

        self._go_btn = QPushButton("Go")
        self._go_btn.setMaximumWidth(44)
        self._go_btn.setEnabled(False)
        self._go_btn.clicked.connect(self._on_jump_to_page)
        paging_layout.addWidget(self._go_btn)

        self._cancel_btn = QPushButton("Cancel")
        self._cancel_btn.setMaximumWidth(70)
        self._cancel_btn.setEnabled(False)
        self._cancel_btn.setToolTip(
            "Cancel the current in-progress fetch / page-jump chain."
        )
        self._cancel_btn.clicked.connect(self._on_cancel_fetch)
        paging_layout.addWidget(self._cancel_btn)

        self._prefetch_label = QLabel("")
        self._prefetch_label.setStyleSheet("color: grey; font-size: 10px;")
        self._prefetch_label.setToolTip(
            "Number of pages with cached cursors. "
            "Background prefetch is loading ahead."
        )
        paging_layout.addSpacing(12)
        paging_layout.addWidget(self._prefetch_label)

        layout.addLayout(paging_layout)
        return group

    def _build_replay_panel(self) -> QGroupBox:
        r"""Build the right splitter pane: session metadata and command log.

        The metadata section shows five fixed labels (host/device ID,
        operator, start time, duration, session UUID) in a monospace
        font so the values align vertically across sessions.

        The command log is a read-only QTextEdit in monospace with
        horizontal scrolling (NoWrap mode) so wide command strings
        don't get truncated.  Each entry is formatted as:

            [2024-11-15 09:12:05 PST]
              cwd : C:\\Windows\\System32
              cmd : ls -la

        Returns:
            A configured QGroupBox widget.
        """
        group = QGroupBox("Session Replay")
        layout = QVBoxLayout(group)

        # Monospace font ensures metadata labels and command log lines
        # are aligned vertically.  Menlo (macOS), Consolas (Windows),
        # and the generic 'monospace' family name are tried in order.
        mono_font = QFont("Menlo, Consolas, monospace")
        mono_font.setStyleHint(QFont.Monospace)
        mono_font.setPointSize(11)

        # ── Metadata labels ───────────────────────────────────────────
        meta_layout = QVBoxLayout()
        self._meta_host = QLabel("Host: —")
        self._meta_operator = QLabel("Operator: —")
        self._meta_started = QLabel("Started: —")
        self._meta_duration = QLabel("Duration: —")
        self._meta_session_id = QLabel("Session ID: —")
        # Allow the session UUID to wrap if the panel is very narrow.
        self._meta_session_id.setWordWrap(True)

        for lbl in (self._meta_host, self._meta_operator,
                    self._meta_started, self._meta_duration,
                    self._meta_session_id):
            lbl.setFont(mono_font)
            meta_layout.addWidget(lbl)

        layout.addLayout(meta_layout)

        # Horizontal rule between metadata and command log.
        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setFrameShadow(QFrame.Sunken)
        layout.addWidget(sep)

        # ── Command log ───────────────────────────────────────────────
        # Row: "Command Log:" label (left) + Copy + Copy Commands (right)
        cmd_header = QHBoxLayout()
        cmd_header.addWidget(QLabel("Command Log:"))
        cmd_header.addStretch()
        self._copy_log_btn = QPushButton("Copy")
        self._copy_log_btn.setToolTip(
            "Copy the full formatted command log to the clipboard "
            "(timestamps, cwd, and commands)."
        )
        # Disabled until a session is selected in the table.
        self._copy_log_btn.setEnabled(False)
        self._copy_log_btn.clicked.connect(self._on_copy_log)
        cmd_header.addWidget(self._copy_log_btn)
        self._copy_cmds_btn = QPushButton("Copy Commands")
        self._copy_cmds_btn.setToolTip(
            "Copy all commands to the clipboard (one per line, "
            "chronological order)."
        )
        # Disabled until a session is selected in the table.
        self._copy_cmds_btn.setEnabled(False)
        self._copy_cmds_btn.clicked.connect(self._on_copy_commands)
        cmd_header.addWidget(self._copy_cmds_btn)
        layout.addLayout(cmd_header)

        self._command_log = QTextEdit()
        self._command_log.setReadOnly(True)
        self._command_log.setFont(mono_font)
        # NoWrap + horizontal scroll bar keeps long commands visible.
        self._command_log.setLineWrapMode(QTextEdit.NoWrap)
        self._command_log.setPlaceholderText(
            "Select a session from the list to view its command history."
        )
        layout.addWidget(self._command_log)
        return group

    # ── Credential helpers ───────────────────────────────────────────────────

    def _current_credentials(self) -> tuple:
        """Read the current credential values from the UI panel.

        Returns:
            A 3-tuple (client_id, client_secret, base_url).  All values
            are stripped of surrounding whitespace.  base_url falls back
            to 'auto' if the combo box has no selection.
        """
        return (
            self._id_field.text().strip(),
            self._secret_field.text().strip(),
            self._base_url_combo.currentData() or "auto",
        )

    # ── Fetch helpers ────────────────────────────────────────────────────────

    def _set_fetch_active(self, active: bool):
        """Enable or disable all interactive controls during a fetch.

        When ``active`` is True (fetch in flight) ALL controls that could
        mutate fetch parameters or trigger a new fetch are disabled, and
        the Cancel button is enabled.  This prevents the QThread crash that
        occurs when the user changes sort/page-size while a worker is
        running.

        When ``active`` is False (fetch complete or cancelled) the controls
        are restored to their natural enabled state and Cancel is hidden.

        Args:
            active: True to lock controls, False to unlock.
        """
        # Controls that change fetch parameters — must be locked.
        for widget in (
            self._load_btn, self._demo_btn,
            self._sort_combo, self._page_size_combo,
            self._date_from, self._date_to,
            self._filter_field,
        ):
            if widget is not None:
                widget.setEnabled(not active)

        # Navigation buttons have their own enable logic — only unlock;
        # _update_paging_controls handles them when active is False.
        if active:
            for btn in (self._prev_btn, self._next_btn,
                        self._go_btn, self._page_jump):
                if btn is not None:
                    btn.setEnabled(False)

        # Cancel button is only useful while a fetch is running.
        if self._cancel_btn is not None:
            self._cancel_btn.setEnabled(active)

    def _start_fetch(self, offset: str = None):
        """Spawn a FetchSessionsWorker for the given page cursor.

        All interactive controls are disabled during the fetch to prevent
        double-submission.  They are re-enabled by _on_sessions_loaded()
        or _on_fetch_error().

        FQL filter construction
        -----------------------
        Up to three FQL fragments are ANDed together:
        1. Hostname fragment — if ``-n`` was passed on the CLI.
        2. Date-from fragment — if the From date picker is set.
        3. Date-to fragment — if the To date picker is set.

        The API uses ``created_at`` as an ISO 8601 datetime field.  The
        To date is extended to 23:59:59Z (end of day, UTC) so the filter
        is inclusive of the selected day.

        Sort order
        ----------
        Sessions are always fetched newest-first (``created_at|desc``).
        This is the most useful default for audit review because the
        most recent sessions appear on page 1.  Column-header clicks in
        the table provide ascending/descending client-side resorting
        within the loaded page.

        Args:
            offset: Opaque pagination cursor from the previous API
                response (None = first page).
        """
        client_id, client_secret, base_url = self._current_credentials()

        # ── Build FQL filter ──────────────────────────────────────────
        # Individual FQL fragments are collected and joined with '+' (AND).
        fql_parts = []

        # 1. Hostname filter from -n CLI flag (highest priority).
        if self._auto_hostname:
            fql_parts.append(f"hostname:'{self._auto_hostname}'")

        # 2-3. Date range from picker widgets.
        # minimumDate() is the sentinel "no date set" value (year 2000-01-01).
        min_date = self._date_from.minimumDate()
        if self._date_from.date() != min_date:
            iso = self._date_from.date().toString("yyyy-MM-dd")
            fql_parts.append(f"created_at:>'{iso}T00:00:00Z'")
        if self._date_to.date() != min_date:
            iso = self._date_to.date().toString("yyyy-MM-dd")
            # End-of-day so the selected date is fully included.
            fql_parts.append(f"created_at:<'{iso}T23:59:59Z'")

        fql_filter = "+".join(fql_parts) if fql_parts else None

        # Pause any running background prefetch before locking UI controls
        # to prevent cursor-append races with the foreground worker.
        self._pause_prefetch()

        # Lock all interactive controls while the fetch is in flight.
        # This prevents the QThread crash from sort/page-size changes
        # arriving while a worker is running.
        self._set_fetch_active(True)
        self._status_bar.showMessage("Fetching sessions…")
        self._session_count_label.setText("Loading…")

        # Create the worker, wire its signals, and start it.
        # The finished/error signals are emitted on the worker thread
        # but Qt automatically queues them to the main thread's event
        # loop, so the connected slots execute safely on the main thread.
        self._worker = FetchSessionsWorker(
            client_id, client_secret, base_url,
            offset=offset,
            fql_filter=fql_filter,
            sort=self._sort_combo.currentData(),
            page_size=self._page_size,
        )
        self._worker.finished.connect(self._on_sessions_loaded)
        self._worker.error.connect(self._on_fetch_error)
        self._worker.start()

    # ── Event handlers ───────────────────────────────────────────────────────

    def _on_load_clicked(self):
        """Validate credentials and start a fresh first-page fetch.

        Resets all pagination state so Load Sessions always starts from
        page 1.  A modal warning is shown if either credential field is
        empty, because the SDK would return a 401 otherwise.
        """
        client_id, client_secret, _ = self._current_credentials()
        if not client_id or not client_secret:
            QMessageBox.warning(
                self,
                "Missing Credentials",
                "Enter both Client ID and Client Secret, or click Demo.",
            )
            return

        # Reset pagination state for a fresh load.
        self._stop_prefetch()
        self._page_cursors = [None]
        self._current_page = 0
        self._total_sessions = 0
        self._jump_target_page = None
        self._page_cache = {}
        self._start_fetch(offset=None)

    def _on_prev_page(self):
        """Navigate to the previous page using the stored cursor.

        Serves from the page cache when available to avoid an API round-trip.
        Decrements _current_page and re-fetches using the cursor stored
        at that index in _page_cursors.  The button is already disabled
        on page 0 so the guard here is defensive only.
        """
        if self._current_page <= 0:
            return
        self._current_page -= 1
        if self._current_page in self._page_cache:
            cached = self._page_cache[self._current_page]
            self._on_sessions_loaded(
                cached["sessions"], cached["pagination"]
            )
        else:
            self._start_fetch(
                offset=self._page_cursors[self._current_page]
            )

    def _on_next_page(self):
        """Navigate to the next page using the stored cursor.

        Serves from the page cache when available to avoid an API round-trip.
        The cursor for page N+1 is appended to _page_cursors by
        _on_sessions_loaded() when the API returns it.  If the cursor
        list doesn't yet contain the next page (e.g. the user reached
        the end), the button is disabled and this handler is never called.
        """
        next_page = self._current_page + 1
        if next_page >= len(self._page_cursors):
            return
        self._current_page = next_page
        if self._current_page in self._page_cache:
            cached = self._page_cache[self._current_page]
            self._on_sessions_loaded(
                cached["sessions"], cached["pagination"]
            )
        else:
            self._start_fetch(
                offset=self._page_cursors[self._current_page]
            )

    def _on_sessions_loaded(self, sessions: list, pagination: dict):
        """Handle a successful API response from the worker thread.

        Accumulates the next-page cursor, repopulates the table, updates
        the pagination controls, and (if applicable) auto-selects the
        session specified by the -i CLI flag.

        The cursor list is append-only: once a cursor for page N is
        stored it never changes.  Going back to page N always uses the
        same cursor, giving consistent results even if new sessions are
        created between navigations.

        Args:
            sessions: Session dicts for the current page (up to
                _PAGE_SIZE entries).
            pagination: Dict with 'total' (int) and
                'next_cursor' (str or None).
        """
        self._sessions = sessions
        self._total_sessions = pagination.get("total", 0)
        next_cursor = pagination.get("next_cursor")

        # Append the next-page cursor only if we haven't stored it yet.
        # This condition is True exactly on the first visit to each new
        # page; revisiting a page (via Prev/Next) skips this block.
        if next_cursor and len(self._page_cursors) == self._current_page + 1:
            self._page_cursors.append(next_cursor)

        # Cache this page's data so back/forward navigation doesn't
        # need to re-query the API for already-visited pages.
        self._page_cache[self._current_page] = {
            "sessions": sessions,
            "pagination": pagination,
        }

        # If a jump-to-page chain is in progress, continue fetching forward
        # until we reach the target page, then land and display normally.
        if self._jump_target_page is not None:
            target = self._jump_target_page
            if self._current_page < target and next_cursor:
                # Still short of target — advance one more page.
                self._current_page += 1
                remaining = target - self._current_page
                self._status_bar.showMessage(
                    f"Jumping to page {target + 1} — "
                    f"fetching page {self._current_page + 1} "
                    f"({remaining} page(s) remaining). "
                    "Click Cancel to stop."
                )
                self._start_fetch(self._page_cursors[self._current_page])
                return
            # Arrived at target (or ran out of pages).
            self._jump_target_page = None

        self._populate_session_table(sessions)
        self._update_paging_controls()

        self._set_fetch_active(False)
        self._resume_prefetch()
        self._update_prefetch_indicator()
        # After the first successful load, relabel the button.
        if not self._has_loaded:
            self._has_loaded = True
            self._load_btn.setText("Reload Sessions")
        self._status_bar.showMessage(
            f"Showing {len(sessions)} session(s) "
            f"(page {self._current_page + 1} of {self._page_count()}). "
            "Click a row to replay."
        )

        # Auto-navigate to a session ID provided via -i CLI flag.
        # Only searches the current page — deep pagination is not
        # performed automatically.
        if self._auto_session_id:
            self._try_auto_select(self._auto_session_id)

    def _on_fetch_error(self, message: str):
        """Handle an error emitted by the worker thread.

        Displays both a modal dialog (for immediate attention) and a
        status bar message (persistent reference).  Controls are
        re-enabled so the user can correct credentials and retry.

        Args:
            message: Human-readable error description from the worker.
        """
        self._set_fetch_active(False)
        self._resume_prefetch()
        self._jump_target_page = None  # abort any in-progress jump chain
        self._session_count_label.setText("Load failed.")
        self._status_bar.showMessage(f"Error: {message}")
        QMessageBox.critical(self, "API Error", message)

    def _on_filter_changed(self, text: str):
        """Apply or clear the client-side substring filter in real time.

        The SessionFilterProxy re-evaluates every row against the filter
        string on each keystroke.  Filtering is case-insensitive and
        matches any column (filterKeyColumn == -1).  Clearing the field
        restores all rows immediately.

        Note: this is a purely client-side operation — it only filters
        the sessions already loaded for the current page.  It does not
        re-query the API.

        Args:
            text: Current contents of the filter input field.
        """
        if self._proxy_model is None:
            return
        self._proxy_model.setFilterFixedString(text)

    def _on_sort_changed(self, _index: int):
        """Re-fetch from page 1 when the sort order changes.

        The sort parameter is a server-side control, so changing it
        invalidates all cached page cursors (they were obtained under
        the old sort order).  Pagination state is fully reset and a
        fresh load begins.  In demo mode, sorting has no effect because
        the fixture data is not API-backed.

        Args:
            _index: Combo box index (unused; sort value read in
                _start_fetch via currentData()).
        """
        if self._total_sessions > 0 and not self._demo_mode:
            self._stop_prefetch()
            self._page_cursors = [None]
            self._page_cache = {}
            self._current_page = 0
            self._total_sessions = 0
            self._start_fetch(None)

    def _on_page_size_changed(self, _index: int):
        """Update page size and re-fetch from page 1.

        Changing the per-page count invalidates all cached cursors
        (cursor granularity changes with page size), so pagination state
        is reset and a fresh first-page load begins.  The new page size
        is read from the combo box's item data and stored in
        self._page_size before the fetch is triggered.  In demo mode,
        page size has no effect.

        Args:
            _index: Combo box index (unused; size read via currentData()).
        """
        size = self._page_size_combo.currentData()
        if size:
            self._page_size = int(size)
        if self._total_sessions > 0 and not self._demo_mode:
            self._stop_prefetch()
            self._page_cursors = [None]
            self._page_cache = {}
            self._current_page = 0
            self._total_sessions = 0
            self._start_fetch(None)

    def _on_jump_to_page(self):
        """Navigate directly to the page number entered in the spinbox.

        If the target page's cursor is already cached in _page_cursors,
        navigation is immediate.  If the target page is beyond the furthest
        cached page, the method chains API calls automatically — each
        response appends the next cursor, then _on_sessions_loaded continues
        the chain until the target page is reached.

        The spinbox is 1-based; _page_cursors is 0-based.
        """
        target = self._page_jump.value() - 1  # convert to 0-based
        if target == self._current_page:
            return
        if target < len(self._page_cursors):
            # Cursor already cached — jump directly.
            self._jump_target_page = None
            self._current_page = target
            self._start_fetch(self._page_cursors[target])
        else:
            # Need to auto-fetch forward to build up the cursor chain.
            self._jump_target_page = target
            total_pages = self._page_count()
            if total_pages and target >= total_pages:
                self._status_bar.showMessage(
                    f"Page {target + 1} exceeds total pages ({total_pages})."
                )
                self._jump_target_page = None
                return
            self._status_bar.showMessage(
                f"Fetching pages to reach page {target + 1}…"
            )
            # Advance one page beyond the furthest cached to continue chain.
            next_uncached = len(self._page_cursors) - 1
            self._current_page = next_uncached
            self._start_fetch(self._page_cursors[next_uncached])

    def _on_clear_dates(self):
        """Reset both date pickers to their sentinel 'no date' state.

        Sets both QDateEdit widgets back to their minimumDate() value,
        which renders as '(any)' via specialValueText.  The dateChanged
        signal fires after each setDate, which triggers _on_date_changed
        and a server-side re-fetch when sessions are loaded.
        """
        self._date_from.setDate(self._date_from.minimumDate())
        self._date_to.setDate(self._date_to.minimumDate())

    def _on_date_changed(self, _date: QDate):
        """Re-fetch from page 1 when either date picker value changes.

        The date range is a server-side FQL filter (``created_at``), so
        changing it invalidates all cached page cursors.  Pagination state
        is fully reset and a fresh load begins.  In demo mode or before
        any load has occurred this is a no-op; the filter will be applied
        on the next explicit Load Sessions click instead.

        Args:
            _date: The new date value (unused; both pickers are read in
                _start_fetch via ``self._date_from``/``self._date_to``).
        """
        if self._has_loaded and not self._demo_mode:
            self._stop_prefetch()
            self._page_cursors = [None]
            self._page_cache = {}
            self._current_page = 0
            self._total_sessions = 0
            self._start_fetch(None)

    def _on_cancel_fetch(self):
        """Abort the current in-progress worker and any jump-to-page chain.

        Signals the worker to stop (Qt will clean it up when it finishes
        its current blocking call), clears the jump target so the chain
        does not continue, and re-enables controls via _set_fetch_active.
        """
        self._jump_target_page = None
        if self._worker is not None and self._worker.isRunning():
            # QThread has no cooperative cancel; disconnect signals so stale
            # results don't affect the UI, then leave the reference alive.
            # Nulling _worker here would drop the Python ref while the OS
            # thread is still blocked — the C++ QThread object would be
            # destroyed mid-run, causing "QThread: Destroyed while running".
            # closeEvent() uses isRunning() to wait for the thread to finish.
            try:
                self._worker.finished.disconnect()
                self._worker.error.disconnect()
            except RuntimeError:
                pass
        self._set_fetch_active(False)
        self._stop_prefetch()
        self._status_bar.showMessage("Fetch cancelled.")

    # ── Background prefetch helpers ──────────────────────────────────────────

    def _pause_prefetch(self):
        """Pause the background prefetch worker between requests."""
        if self._prefetch_worker and self._prefetch_worker.isRunning():
            self._prefetch_worker.pause()

    def _resume_prefetch(self):
        """Resume an existing prefetch worker, or start one if warranted.

        Called after every foreground fetch completes (success or error).
        If a worker is already paused it is simply resumed; otherwise a new
        worker is spawned from the last known cursor onward.
        """
        if self._prefetch_worker and self._prefetch_worker.isRunning():
            self._prefetch_worker.resume()
            return
        # Clear a stale reference: worker exists but thread has already exited
        # (finished signal posted but _on_prefetch_done not yet processed).
        # Without this, the fall-through below would skip spawning a new worker
        # at the correct page boundary and silently do nothing.
        if self._prefetch_worker is not None:
            self._prefetch_worker = None
        # Don't prefetch in demo mode or before any sessions are loaded.
        if self._demo_mode or not self._total_sessions:
            return
        known_pages = len(self._page_cursors)
        total_pages = self._page_count()
        if known_pages >= total_pages:
            return                           # all cursors already known
        last_cursor = self._page_cursors[-1]
        if not last_cursor:
            return
        client_id, client_secret, base_url = self._current_credentials()
        fql_filter = self._current_fql()
        self._prefetch_worker = PrefetchWorker(
            client_id, client_secret, base_url,
            start_page=known_pages - 1,
            start_cursor=last_cursor,
            fql_filter=fql_filter,
            sort=self._sort_combo.currentData(),
            page_size=self._page_size,
        )
        self._prefetch_worker.cursor_discovered.connect(
            self._on_cursor_prefetched
        )
        self._prefetch_worker.prefetch_done.connect(self._on_prefetch_done)
        self._prefetch_worker.prefetch_error.connect(self._on_prefetch_error)
        self._prefetch_worker.start()

    def _stop_prefetch(self):
        """Signal the background prefetch worker to stop and park it.

        Park it in the zombie-worker set until the OS thread has exited.

        Design:
        - The worker reference is moved from ``_prefetch_worker`` to
          ``_stopping_workers`` so Python's refcount stays ≥ 1 while the OS
          thread is still alive.  Dropping the reference immediately (as the
          old code did) caused Python GC to run ``QThread.__del__`` while the
          thread was mid-API-call → ``QThread: Destroyed while running`` abort.
        - ``deleteLater`` does NOT protect against Python GC: it schedules a
          C++ ``delete`` via the event loop but does not touch the Python
          wrapper's refcount.  The zombie-set is the only safe mechanism.
        - A ``finished → lambda → discard`` connection removes the worker from
          the set once the OS thread has exited.  At that point it is safe for
          Python GC to destroy the C++ object.
        - UI-facing slots are disconnected so stale signals from the stopping
          worker do not mutate ``_page_cursors`` or ``_page_cache``.
        - ``wait()`` and ``terminate()`` are intentionally omitted.
          ``QThread::terminate()`` sends ``pthread_cancel()`` to the OS
          thread, which corrupts Python's GIL or allocator when the thread is
          inside a C extension (urllib3/SSL), causing a segfault.
        """
        if self._prefetch_worker is not None:
            worker = self._prefetch_worker
            self._prefetch_worker = None
            try:
                worker.cursor_discovered.disconnect(self._on_cursor_prefetched)
            except (TypeError, RuntimeError):
                pass
            try:
                worker.prefetch_done.disconnect(self._on_prefetch_done)
            except (TypeError, RuntimeError):
                pass
            try:
                worker.prefetch_error.disconnect(self._on_prefetch_error)
            except (TypeError, RuntimeError):
                pass
            # Transfer ownership to zombie set — Python refcount stays > 0
            # until the OS thread exits and finished fires.
            self._stopping_workers.add(worker)
            worker.finished.connect(
                lambda w=worker: self._stopping_workers.discard(w)
            )
            worker.stop()

    def _current_fql(self) -> str | None:
        """Return the current FQL filter string (mirrors _start_fetch logic).

        Returns:
            FQL filter string or None if no filter is active.
        """
        fql_parts = []
        if self._auto_hostname:
            fql_parts.append(f"hostname:'{self._auto_hostname}'")
        min_date = self._date_from.minimumDate()
        if self._date_from.date() != min_date:
            iso = self._date_from.date().toString("yyyy-MM-dd")
            fql_parts.append(f"created_at:>'{iso}T00:00:00Z'")
        if self._date_to.date() != min_date:
            iso = self._date_to.date().toString("yyyy-MM-dd")
            fql_parts.append(f"created_at:<'{iso}T23:59:59Z'")
        return "+".join(fql_parts) if fql_parts else None

    # ── Background prefetch slots (main thread via Qt queued signal) ─────────

    def _on_cursor_prefetched(self, page_idx: int, next_cursor: str,
                              sessions: list, pagination: dict):
        """Receive a prefetched page from the background worker.

        Extends ``_page_cursors`` with the new cursor and caches session
        data (with LRU eviction) so the background-fetched pages are
        instantly navigable.  Updates the spinbox maximum and prefetch
        indicator.

        Args:
            page_idx: 0-based index of the page that was just fetched.
                      The cursor for the *next* page is ``next_cursor``.
            next_cursor: Opaque cursor string for ``page_idx + 1``, or
                         empty string if this was the last page.
            sessions: Session dicts for ``page_idx``.
            pagination: Pagination metadata dict (``total``, ``next_cursor``).
        """
        # Extend the cursor list only if this is the strictly next index.
        # page_idx is the 0-based index of the page just fetched; its
        # next_cursor belongs at position page_idx+1 in _page_cursors.
        if next_cursor and page_idx + 1 == len(self._page_cursors):
            self._page_cursors.append(next_cursor)

        # Cache sessions for the just-fetched page (page_idx), with LRU
        # eviction to stay within the memory cap.
        if sessions and page_idx not in self._page_cache:
            if len(self._page_cache) >= _PREFETCH_CACHE_LIMIT:
                evict_key = max(
                    (k for k in self._page_cache
                     if k != self._current_page),
                    key=lambda k: abs(k - self._current_page),
                    default=None,
                )
                if evict_key is not None:
                    del self._page_cache[evict_key]
            self._page_cache[page_idx] = {
                "sessions": sessions,
                "pagination": pagination,
            }

        self._update_paging_controls()
        self._update_prefetch_indicator()

    def _on_prefetch_done(self):
        """Background worker exhausted all pages — no more cursors to fetch."""
        self._prefetch_worker = None
        self._update_prefetch_indicator()

    def _on_prefetch_error(self, message: str):
        """Non-fatal background prefetch error — show in status bar only."""
        self._status_bar.showMessage(
            f"Background prefetch stopped: {message}", 5000
        )
        self._prefetch_worker = None

    def _update_prefetch_indicator(self):
        """Refresh the 'Pages ready: N/M' label in the pagination row."""
        if self._prefetch_label is None:
            return
        if self._demo_mode or self._total_sessions == 0:
            self._prefetch_label.setText("")
            return
        cached = len(self._page_cursors)
        total = self._page_count()
        if cached >= total:
            self._prefetch_label.setText(f"All {total} pages ready")
        else:
            self._prefetch_label.setText(f"Pages ready: {cached}/{total}")

    def _on_copy_commands(self):
        """Copy the command strings of the current session to the clipboard.

        Extracts only the ``command_string`` values (the full command with
        arguments) from the selected session's log entries, sorts them
        chronologically, and joins them with newlines before writing to
        the system clipboard via QApplication.clipboard().

        This intentionally omits timestamps, working directory context,
        and other metadata that appear in the command log display — the
        goal is a clean, pasteable command list.  If ``command_string``
        is absent for an entry, ``base_command`` is used as a fallback
        (matches the display logic in _display_session).

        The command log display in the UI is left unchanged.  After a
        successful copy the status bar shows a brief confirmation.
        """
        if self._current_session is None:
            return

        logs = self._current_session.get("logs") or []
        ordered = sorted(
            logs,
            key=lambda e: (e.get("created_at") or "", e.get("id") or 0)
        )

        # Extract the same command text used in the display.
        cmds = [
            e.get("command_string") or e.get("base_command") or ""
            for e in ordered
        ]
        # Filter out blank entries (defensive — should not occur).
        cmds = [c for c in cmds if c]

        QApplication.clipboard().setText("\n".join(cmds))
        self._status_bar.showMessage(
            f"Copied {len(cmds)} command(s) to clipboard."
        )

    def _on_copy_log(self):
        """Copy the full formatted command log text to the clipboard.

        Copies exactly what is displayed in the command log QTextEdit —
        timestamps, cwd context, and command strings in monospace format.
        Use this when you need the complete audit-style output rather than
        just the raw command list.
        """
        if self._command_log is None:
            return
        text = self._command_log.toPlainText()
        QApplication.clipboard().setText(text)
        lines = text.count("\n") + 1 if text else 0
        self._status_bar.showMessage(
            f"Copied command log ({lines} line(s)) to clipboard."
        )

    def _show_easter_egg(self):
        """Display the easter-egg dialog (Ctrl+Shift+click on FalconPy logo).

        Shows the CrowdStrike logo, the punk spider image, and the text
        "WE STOP BREACHES" in a simple modal dialog.
        """
        dlg = QDialog(self)
        dlg.setWindowTitle("CrowdStrike")
        layout = QVBoxLayout(dlg)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        if os.path.exists(_LOGO_PATH):
            cs_pixmap = QPixmap(_LOGO_PATH)
            cs_label = QLabel()
            cs_label.setPixmap(
                cs_pixmap.scaledToHeight(80, Qt.SmoothTransformation)
            )
            cs_label.setAlignment(Qt.AlignHCenter)
            layout.addWidget(cs_label)

        if os.path.exists(_PUNK_SPIDER_PATH):
            spider_pixmap = QPixmap(_PUNK_SPIDER_PATH)
            spider_label = QLabel()
            spider_label.setPixmap(
                spider_pixmap.scaledToHeight(180, Qt.SmoothTransformation)
            )
            spider_label.setAlignment(Qt.AlignHCenter)
            layout.addWidget(spider_label)

        tagline = QLabel("WE STOP BREACHES")
        tagline.setAlignment(Qt.AlignHCenter)
        tagline.setStyleSheet(
            "font-size: 18pt; font-weight: bold; color: #ec0000;"
        )
        layout.addWidget(tagline)

        dlg.exec()

    def _on_session_selected(self, selected, _deselected):
        """Populate the replay panel when the user selects a table row.

        The table is backed by a QSortFilterProxyModel, so the visual
        row index (proxy row) may differ from the index into _sessions
        (source row) after sorting or filtering.  The proxy model's
        mapToSource() method translates between the two.

        Args:
            selected: QItemSelection containing the newly selected
                indexes in proxy-model coordinates.
            _deselected: Previously selected indexes (unused).
        """
        indexes = selected.indexes()
        if not indexes:
            return

        # Translate the proxy-model row to the source-model row so we
        # can look up the correct session in self._sessions.
        proxy_row = indexes[0].row()
        source_index = self._proxy_model.mapToSource(
            self._proxy_model.index(proxy_row, COL_SESSION_ID)
        )
        source_row = source_index.row()

        if source_row < 0 or source_row >= len(self._sessions):
            return

        self._display_session(self._sessions[source_row])

    def closeEvent(self, event):  # pylint: disable=invalid-name
        """Stop the fetch worker thread and close unconditionally.

        Attempts a graceful shutdown (``quit()`` + 500 ms wait) for the
        fetch worker thread.  If the thread does not exit in time it is
        force-killed via ``terminate()``.  ``super().closeEvent(event)``
        is always called so the user can close the window without
        interference.

        Args:
            event: The QCloseEvent from the window manager.
        """
        all_workers = (
            [self._worker, self._prefetch_worker]
            + list(self._stopping_workers)
        )
        for worker in all_workers:
            if worker is not None and worker.isRunning():
                # Blanket disconnect via QObject.disconnect() to silence
                # RuntimeWarning from signals that may already be disconnected.
                try:
                    worker.disconnect()
                except (TypeError, RuntimeError):
                    pass
                # PrefetchWorker has no Qt event loop so quit() is a no-op
                # for it; call stop() on any worker that supports it so the
                # thread wakes from its sleep/pause-wait and exits cleanly.
                if hasattr(worker, 'stop'):
                    worker.stop()
                else:
                    worker.quit()
                if not worker.wait(500):
                    # Graceful exit timed out — force-kill the OS thread.
                    worker.terminate()
                    worker.wait()

        super().closeEvent(event)

    # ── Pagination helpers ───────────────────────────────────────────────────

    def _page_count(self) -> int:
        """Return total number of pages for the current total session count.

        Returns 1 when total is 0 so the page label always shows a
        valid "Page 1 of 1" rather than "Page 1 of 0".

        Returns:
            Total page count as a positive integer.
        """
        if self._total_sessions == 0:
            return 1
        return math.ceil(self._total_sessions / self._page_size)

    def _update_paging_controls(self):
        """Refresh the prev/next buttons, page indicator, and jump spinbox.

        Prev is enabled when we are past page 0.
        Next is enabled when the cursor list contains an entry for
        page N+1, which means the API returned a next_cursor for that
        page during a previous fetch.
        The jump spinbox maximum is set to the total page count;
        its value is synced to the current page (with signals blocked
        to avoid triggering a spurious jump navigation).
        The Go button is enabled whenever sessions are loaded.
        """
        total_pages = self._page_count()
        current = self._current_page + 1
        self._page_label.setText(f"Page {current} of {total_pages}")
        self._prev_btn.setEnabled(self._current_page > 0)
        # Next is only available if the server reported more pages AND
        # we have already fetched the cursor needed to load the next page.
        has_next = (
            self._current_page + 1 < self._page_count()
            and len(self._page_cursors) > self._current_page + 1
        )
        self._next_btn.setEnabled(has_next)
        # Sync the jump spinbox without firing _on_jump_to_page.
        # Cap at the lesser of cached pages and total pages so the spinbox
        # never allows jumping beyond what the server reported as existing.
        cached_max = max(min(len(self._page_cursors), total_pages), 1)
        self._page_jump.blockSignals(True)
        self._page_jump.setMaximum(cached_max)
        self._page_jump.setValue(current)
        self._page_jump.blockSignals(False)
        self._page_jump.setToolTip(
            f"Jump to any cached page (1\u2013{cached_max}). "
            f"Background prefetch extends reach as it runs."
        )
        # Re-enable the spinbox here; _set_fetch_active(True) disables it
        # but the restore loop only handles prev/next/go, not the spinbox.
        self._page_jump.setEnabled(True)
        self._go_btn.setEnabled(True)

    # ── Data display ─────────────────────────────────────────────────────────

    def _populate_session_table(self, sessions: list):
        """Replace the table model with a fresh model for the given sessions.

        A new QSortFilterProxyModel is created on every page load
        because QSortFilterProxyModel does not support replacing its
        source model once the view has connected to it.  The selection
        model signal is reconnected each time so row-click events
        continue to work after navigation.

        Any active filter text in the filter bar is re-applied to the
        new model so the filter persists across page changes.

        Column resize modes:
          - Most columns: ResizeToContents (compact, data-driven width)
          - Session ID: Stretch (fills the remaining horizontal space)

        Args:
            sessions: Session dicts to display (current page only).
        """
        source_model = build_session_model(sessions)

        # Wrap in SessionFilterProxy to enable text filter across all columns.
        self._proxy_model = SessionFilterProxy()
        self._proxy_model.setSourceModel(source_model)
        # filterKeyColumn(-1) searches across all columns simultaneously.
        self._proxy_model.setFilterKeyColumn(-1)
        self._proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)

        # Re-apply the active text filter.
        if self._filter_field.text():
            self._proxy_model.setFilterFixedString(self._filter_field.text())

        self._session_table.setModel(self._proxy_model)
        # Reconnect the selection signal after replacing the model.
        self._session_table.selectionModel().selectionChanged.connect(
            self._on_session_selected
        )

        # Fit data columns to their content; stretch the session ID
        # column to fill any remaining width.
        header = self._session_table.horizontalHeader()
        for col in (
            COL_HOST, COL_OPERATOR, COL_STARTED, COL_DURATION, COL_CMDS
        ):
            header.setSectionResizeMode(col, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(COL_SESSION_ID, QHeaderView.Stretch)

        noun = "session" if len(sessions) == 1 else "sessions"
        self._session_count_label.setText(
            f"{len(sessions)} {noun} on this page."
        )

    def _display_session(self, session: dict):
        """Populate the replay panel with a session's metadata and commands.

        Metadata labels are updated with values from the session dict.
        The command log is rebuilt from the session's logs list, sorted
        chronologically by created_at timestamp (with log entry id as a
        tie-breaker for commands issued in the same second).

        Each command entry is formatted as three lines:

            [<local timestamp>]
              cwd : <current_directory>
              cmd : <command_string>

        The full command_string is preferred over the shorter
        base_command because it includes arguments.  base_command is
        used as a fallback if command_string is absent.

        Args:
            session: Session dict conforming to domain.Session schema.
        """
        self._current_session = session
        self._copy_cmds_btn.setEnabled(True)
        self._copy_log_btn.setEnabled(True)

        self._meta_host.setText(
            f"Host:      {session.get('hostname', '—')} "
            f"({session.get('device_id', '—')})"
        )
        self._meta_operator.setText(
            "Operator:  " + format_operator(
                session.get('user_id'), session.get('origin')
            )
        )
        self._meta_started.setText(
            f"Started:   {format_datetime(session.get('created_at'))}"
        )
        self._meta_duration.setText(
            f"Duration:  {format_duration(session.get('duration'))}"
        )
        self._meta_session_id.setText(
            f"Session:   {session.get('id', '—')}"
        )

        logs = session.get("logs") or []
        # Sort by timestamp first, then by id within the same second.
        # The API should return logs in order, but sorting defensively
        # ensures correct replay even if the API changes.
        ordered = sorted(
            logs,
            key=lambda e: (e.get("created_at") or "", e.get("id") or 0)
        )

        if not ordered:
            self._command_log.setPlainText(
                "[no commands recorded for this session]"
            )
            return

        lines = []
        for entry in ordered:
            ts = format_datetime(entry.get("created_at"))
            cwd = entry.get("current_directory") or "—"
            # Prefer command_string (includes args) over base_command.
            cmd = (entry.get("command_string")
                   or entry.get("base_command") or "—")
            lines.append(f"[{ts}]")
            lines.append(f"  cwd : {cwd}")
            lines.append(f"  cmd : {cmd}")
            lines.append("")

        self._command_log.setPlainText("\n".join(lines))

    def _try_auto_select(self, session_id: str):
        """Select the table row whose session id matches session_id.

        Called after the first page loads when -i SESSION_ID was passed
        on the command line.  Performs a linear scan of the current page
        because _sessions is a plain list.  If the session is on a
        later page, the user must navigate manually.

        Args:
            session_id: The RTR session UUID to locate and select.
        """
        for row, session in enumerate(self._sessions):
            if session.get("id") == session_id:
                # selectRow() triggers the selectionChanged signal,
                # which calls _on_session_selected() and populates the
                # replay panel automatically.
                self._session_table.selectRow(row)
                return

    def _load_demo(self):
        """Load built-in fixture sessions without making any API calls.

        Used when --demo is passed or the Demo button is clicked.
        Resets pagination state, populates the table with _DEMO_SESSIONS,
        updates the window title to show [DEMO MODE], and auto-selects
        the first row.
        """
        self._sessions = _DEMO_SESSIONS
        self._total_sessions = len(_DEMO_SESSIONS)
        self._current_page = 0
        self._page_cursors = [None]
        self._populate_session_table(_DEMO_SESSIONS)
        self._update_paging_controls()
        self._status_bar.showMessage(
            "Demo mode — showing fixture data. No API calls made."
        )
        self.setWindowTitle(
            "CrowdStrike Falcon — RTR Session Replay  [DEMO MODE]"
        )
        if _DEMO_SESSIONS:
            self._session_table.selectRow(0)


# ── Entry point ──────────────────────────────────────────────────────────────


if __name__ == "__main__":
    args = consume_arguments()

    app = QApplication(sys.argv)
    app.setApplicationName("RTR Session Replay")
    app.setOrganizationName("CrowdStrike")

    # ── Dark CrowdStrike-branded theme ───────────────────────────────────────
    # The stylesheet uses CrowdStrike's primary red (#ec0000) as the accent
    # colour on interactive elements (buttons, borders, selections, scrollbars)
    # against a dark background palette (#1a1a1a / #242424 / #2a2a2a) that
    # matches the VS Code dark theme aesthetic.
    app.setStyleSheet("""
        QMainWindow, QWidget {
            background-color: #1a1a1a;
            color: #d4d4d4;
        }
        QGroupBox {
            border: 1px solid #3a3a3a;
            border-top: 2px solid #ec0000;
            border-radius: 4px;
            margin-top: 8px;
            padding-top: 4px;
            font-weight: bold;
            color: #f0f0f0;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 8px;
            padding: 0 4px;
            color: #ec0000;
        }
        QTableView {
            background-color: #242424;
            alternate-background-color: #2c2c2c;
            gridline-color: #3a3a3a;
            color: #d4d4d4;
            selection-background-color: #6b0000;
            selection-color: #ffffff;
            border: 1px solid #3a3a3a;
        }
        QHeaderView::section {
            background-color: #2a2a2a;
            color: #f0f0f0;
            padding: 4px 8px;
            border: none;
            border-right: 1px solid #3a3a3a;
            border-bottom: 2px solid #ec0000;
            font-weight: bold;
        }
        QLineEdit {
            background-color: #2e2e2e;
            border: 1px solid #555;
            border-radius: 3px;
            padding: 4px 6px;
            color: #d4d4d4;
        }
        QLineEdit:focus {
            border-color: #ec0000;
        }
        QDateEdit {
            background-color: #2e2e2e;
            border: 1px solid #555;
            border-radius: 3px;
            padding: 4px 6px;
            color: #d4d4d4;
        }
        QDateEdit:focus {
            border-color: #ec0000;
        }
        QDateEdit::drop-down {
            subcontrol-origin: border;
            subcontrol-position: center right;
            width: 20px;
            border-left: 1px solid #555;
        }
        QDateEdit::down-arrow {
            image: none;
            width: 8px;
            height: 8px;
            border-left: 4px solid transparent;
            border-right: 4px solid transparent;
            border-top: 6px solid #d4d4d4;
        }
        QComboBox {
            background-color: #2e2e2e;
            border: 1px solid #555;
            border-radius: 3px;
            padding: 4px 6px;
            color: #d4d4d4;
        }
        QComboBox:focus {
            border-color: #ec0000;
        }
        QComboBox::drop-down {
            border: none;
        }
        QComboBox QAbstractItemView {
            background-color: #2a2a2a;
            color: #d4d4d4;
            selection-background-color: #6b0000;
        }
        QPushButton {
            background-color: #ec0000;
            color: #ffffff;
            border: none;
            border-radius: 3px;
            padding: 6px 14px;
            font-weight: bold;
            min-height: 26px;
        }
        QPushButton:hover {
            background-color: #c80000;
        }
        QPushButton:pressed {
            background-color: #a00000;
        }
        QPushButton:disabled {
            background-color: #444;
            color: #888;
        }
        QTextEdit {
            background-color: #1a1a1a;
            color: #e0e0e0;
            border: 1px solid #3a3a3a;
            border-radius: 3px;
        }
        QStatusBar {
            background-color: #ec0000;
            color: #ffffff;
            font-weight: bold;
        }
        QLabel {
            color: #d4d4d4;
        }
        QScrollBar:vertical {
            background: #2a2a2a;
            width: 12px;
        }
        QScrollBar::handle:vertical {
            background: #ec0000;
            border-radius: 6px;
            min-height: 20px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0;
        }
        QSpinBox {
            background-color: #2e2e2e;
            border: 1px solid #555;
            border-radius: 3px;
            padding: 4px 6px;
            color: #d4d4d4;
        }
        QSpinBox:focus {
            border-color: #ec0000;
        }
        QSpinBox::up-button {
            subcontrol-origin: border;
            subcontrol-position: top right;
            width: 18px;
            border-left: 1px solid #555;
            border-bottom: 1px solid #555;
            background-color: #3a3a3a;
        }
        QSpinBox::up-button:hover {
            background-color: #ec0000;
        }
        QSpinBox::up-arrow {
            image: none;
            width: 6px;
            height: 6px;
            border-left: 4px solid transparent;
            border-right: 4px solid transparent;
            border-bottom: 5px solid #d4d4d4;
        }
        QSpinBox::down-button {
            subcontrol-origin: border;
            subcontrol-position: bottom right;
            width: 18px;
            border-left: 1px solid #555;
            border-top: 1px solid #555;
            background-color: #3a3a3a;
        }
        QSpinBox::down-button:hover {
            background-color: #ec0000;
        }
        QSpinBox::down-arrow {
            image: none;
            width: 6px;
            height: 6px;
            border-left: 4px solid transparent;
            border-right: 4px solid transparent;
            border-top: 5px solid #d4d4d4;
        }
    """)

    window = RTRReplayWindow(
        demo_mode=args.demo,
        prefill_id=args.client_id or "",
        prefill_secret=args.client_secret or "",
        prefill_base_url=args.base_url or "auto",
        auto_hostname=args.hostname,
        auto_session_id=args.session_id,
    )
    window.show()
    sys.exit(app.exec())
