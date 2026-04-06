r"""Alerts Triage Dashboard — Desktop GUI.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |             FalconPy
`-------'                         `-------'

  ____  _        ___  ____  ______  _____     ______  ____   ____   ____   ____    ___
 /    T| T      /  _]|    \|      T/ ___/    |      T|    \ l    j /    T /    T  /  _]
Y  o  || |     /  [_ |  D  )      (   \_     |      ||  D  ) |  T Y  o  |Y   __j /  [_
|     || l___ Y    _]|    /l_j  l_j\__  T    l_j  l_j|    /  |  | |     ||  T  |Y    _]
|  _  ||     T|   [_ |    \  |  |  /  \ |      |  |  |    \  |  | |  _  ||  l_ ||   [_
|  |  ||     ||     T|  .  Y |  |  \    |      |  |  |  .  Y j  l |  |  ||     ||     T
l__j__jl_____jl_____jl__j\_j l__j   \___j      l__j  l__j\_j|____jl__j__jl___,_jl_____j

                                    Alerts Triage Dashboard (v2 — PyQt6)
                                    Uses: Alerts
                                    Scope: alerts:read, alerts:write

A PyQt6 desktop application for triaging CrowdStrike Falcon behavioral
alerts. It retrieves alerts from the Falcon platform using the FalconPy SDK
and presents them in a split-pane interface for efficient triage.

Prerequisites
-------------
  pip install crowdstrike-falconpy pyqt6
  (or: pipenv install crowdstrike-falconpy pyqt6)

Required API scopes
-------------------
  alerts:read   — to query and retrieve alert details
  alerts:write  — to update alert status and assignee

Credentials
-----------
  Reads FALCON_CLIENT_ID and FALCON_CLIENT_SECRET from environment variables
  on startup. The title bar shows connection status.

Usage
-----
    pipenv run python3 alerts_triage.py

Architecture overview
---------------------
  AlertsTriageApp (QMainWindow)
  ├── Filter bar (QWidget toolbar row)
  │   ├── FQL text field (QLineEdit)
  │   ├── Severity dropdown (QComboBox)
  │   ├── Status dropdown (QComboBox)
  │   └── Refresh button (QPushButton)
  ├── Main splitter (QSplitter)
  │   ├── Left panel — alert table (QTableWidget) with severity colour badges
  │   └── Right panel — alert detail view (QTextEdit, read-only)
  ├── Bulk toolbar (QWidget)
  │   ├── Select-all checkbox (QCheckBox)
  │   ├── Status combo (QComboBox)
  │   ├── Assign-to field (QLineEdit)
  │   └── Apply button (QPushButton)
  └── Status bar (QStatusBar)

  API calls run on a background QThread and results are delivered back to
  the main thread via Qt signals, keeping the UI fully responsive.
"""
# pylint: disable=too-many-lines
# pylint: disable=too-many-arguments,too-many-positional-arguments
# pylint: disable=too-many-locals,too-few-public-methods
# pylint: disable=too-many-instance-attributes,too-many-statements
# pylint: disable=line-too-long  # ASCII banner in module docstring exceeds 100 chars
import argparse
import os
import sys
from datetime import datetime, timezone, timedelta

from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QColor, QBrush, QFont, QPalette
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSplitter,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from falconpy import Alerts

# ---------------------------------------------------------------------------
# Visual constants
# ---------------------------------------------------------------------------
SEVERITY_COLORS = {
    # Numeric severity labels (int converted to string)
    "1": "#5B9BD5",   # informational — light blue
    "2": "#F5E642",   # low — yellow
    "3": "#FF8C00",   # medium — orange
    "4": "#E03030",   # high — red
    "5": "#990000",   # critical — dark red
    # Named severity labels (severity_name field)
    "critical":      "#990000",
    "high":          "#E03030",
    "medium":        "#FF8C00",
    "low":           "#F5E642",
    "informational": "#5B9BD5",
    "unknown":       "#8E8E93",
}

# Text colour to use on each severity background (ensures contrast).
SEVERITY_FG_COLORS = {
    "critical":      "#FFFFFF",
    "high":          "#FFFFFF",
    "medium":        "#000000",
    "low":           "#000000",
    "informational": "#000000",
    "unknown":       "#FFFFFF",
    "1": "#000000",
    "2": "#000000",
    "3": "#000000",
    "4": "#FFFFFF",
    "5": "#FFFFFF",
}

STATUS_CHOICES = ["", "new", "in_progress", "closed"]
SEVERITY_CHOICES = ["", "critical", "high", "medium", "low"]

# Max alerts retrieved per page from the API
PAGE_SIZE = 100

# Hard cap on total results fetched in a single query (prevents hang on large envs)
MAX_RESULTS = 200

# Default look-back window when no date filter is specified
DEFAULT_HOURS = 24

# UI pagination: number of rows shown per page in the alert table
DEFAULT_PAGE_SIZE = 50
PAGE_SIZE_CHOICES = ["25", "50", "100", "200"]

# Default filter values applied on startup
DEFAULT_STATUS = ""
DEFAULT_TIME = "24h"

# Column indices for the alert table
COL_SEVERITY = 0
COL_TARGET = 1
COL_TACTIC = 2
COL_STATUS = 3
COL_CREATED = 4

COLUMN_HEADERS = ["Severity", "Target", "Name / Tactic", "Status", "Created"]
COLUMN_WIDTHS = [100, 200, 220, 100, 140]

# Truncation widths
TARGET_MAX = 45
TACTIC_MAX = 40


def _truncate(text: str, max_len: int) -> str:
    """Truncate a string to max_len, appending '…' if shortened."""
    if not text:
        return ""
    return text if len(text) <= max_len else text[: max_len - 1] + "…"


def _format_ts(iso_string: str) -> str:
    """Reformat an ISO 8601 timestamp to a compact local display string."""
    if not iso_string:
        return ""
    try:
        dt = datetime.fromisoformat(iso_string.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M")
    except ValueError:
        return iso_string


def _extract_error_messages(errors) -> str:
    """Convert a Falcon API errors list/dict into a human-readable string.

    The Falcon API returns errors as a list of dicts, e.g.:
        [{"code": 400, "message": "composite_ids must be specified"}]
    This function extracts just the message text and joins them.
    If the input is already a plain string it is returned as-is.
    """
    if not errors:
        return "unknown error"
    if isinstance(errors, str):
        return errors
    if isinstance(errors, dict):
        return errors.get("message") or str(errors)
    # List of error dicts — extract message from each entry.
    messages = []
    for err in errors:
        if isinstance(err, dict):
            msg = err.get("message") or err.get("msg") or str(err)
        else:
            msg = str(err)
        messages.append(msg)
    return "; ".join(messages) if messages else "unknown error"


# ---------------------------------------------------------------------------
# Background worker (QThread)
# ---------------------------------------------------------------------------

class AlertFetchWorker(QThread):
    """Fetch alerts from the Falcon API on a background QThread.

    Emits ``alerts_batch(alerts)`` for each page of detail results so the UI
    can display results progressively without waiting for the full fetch.
    Emits ``fetch_done(error)`` when all pages are complete or on error.
    Emits ``next_offset(offset, has_more)`` with the API continuation token and
    a flag indicating whether more results exist beyond this batch.
    Respects a cancellation flag set via ``cancel()``.
    """

    alerts_batch = pyqtSignal(list)        # incremental: one chunk of detail records
    fetch_done = pyqtSignal(str)           # final: empty string = success, else error msg
    next_offset = pyqtSignal(int, bool)    # (api_offset, has_more) after batch completes

    def __init__(self, sdk: Alerts, fql_filter: str, severity: str, status: str,
                 hours: int = DEFAULT_HOURS, max_results: int = MAX_RESULTS,
                 start_offset: int = 0):
        """Initialise with SDK instance and filter parameters.

        Args:
            start_offset: API pagination offset (int) to continue from (0 = start fresh).
        """
        super().__init__()
        self._sdk = sdk
        self._fql_filter = fql_filter
        self._severity = severity
        self._status = status
        self._hours = hours
        self._max_results = max_results
        self._start_offset = start_offset
        self._cancelled = False

    def cancel(self) -> None:
        """Request cancellation; worker will stop after the current API call."""
        self._cancelled = True

    def run(self) -> None:  # pylint: disable=too-many-branches
        """Execute the paginated fetch and emit results incrementally."""
        try:
            clauses = []
            if self._fql_filter.strip():
                clauses.append(self._fql_filter.strip())
            if self._severity:
                # severity_name field requires title-case (e.g. "High", not "high")
                clauses.append(f"severity_name:'{self._severity.title()}'")
            if self._status:
                clauses.append(f"status:'{self._status}'")

            # Add default time window unless caller explicitly provided one in FQL
            has_time_filter = any(
                kw in self._fql_filter for kw in ("created_timestamp", "timestamp", "last_")
            )
            if not has_time_filter and self._hours > 0:
                since = datetime.now(timezone.utc) - timedelta(hours=self._hours)
                since_str = since.strftime("%Y-%m-%dT%H:%M:%SZ")
                clauses.append(f"created_timestamp:>'{since_str}'")

            combined = "+".join(clauses) if clauses else None

            composite_ids: list[str] = []
            offset = self._start_offset  # Continue from provided offset (or 0 = fresh)
            last_api_offset = offset
            has_more = False
            while not self._cancelled:
                remaining = self._max_results - len(composite_ids)
                if remaining <= 0:
                    # Hit our local cap — check if API has more beyond this batch.
                    has_more = True
                    break
                page_limit = min(PAGE_SIZE, remaining)
                kwargs: dict = {"limit": page_limit, "filter": combined}
                if offset:
                    kwargs["offset"] = offset
                resp = self._sdk.query_alerts_v2(**kwargs)
                if resp["status_code"] not in (200, 201):
                    raise RuntimeError(
                        f"query_alerts_v2 HTTP {resp['status_code']}: "
                        f"{_extract_error_messages(resp['body'].get('errors', []))}"
                    )
                body = resp["body"]
                resources = body.get("resources") or []
                composite_ids.extend(resources)
                meta = body.get("meta", {}).get("pagination", {})
                total = meta.get("total", 0)
                last_api_offset = meta.get("offset", "")
                if not resources or len(composite_ids) >= total:
                    has_more = False
                    break
                offset = last_api_offset

            if self._cancelled:
                self.fetch_done.emit("")
                return

            if not composite_ids:
                self.next_offset.emit(0, False)
                self.fetch_done.emit("")
                return

            # Fetch details in chunks and emit each chunk immediately
            chunk_size = 100
            for i in range(0, len(composite_ids), chunk_size):
                if self._cancelled:
                    break
                chunk = composite_ids[i : i + chunk_size]
                detail_resp = self._sdk.get_alerts_v2(composite_ids=chunk)
                if detail_resp["status_code"] not in (200, 201):
                    raise RuntimeError(
                        f"get_alerts_v2 HTTP {detail_resp['status_code']}: "
                        f"{_extract_error_messages(detail_resp['body'].get('errors', []))}"
                    )
                batch = detail_resp["body"].get("resources") or []
                if batch:
                    self.alerts_batch.emit(batch)

            # Emit pagination continuation info so the UI can offer "load more".
            self.next_offset.emit(last_api_offset, has_more)
            self.fetch_done.emit("")
        except Exception as exc:  # pylint: disable=broad-except
            self.fetch_done.emit(str(exc))


class AlertUpdateWorker(QThread):
    """Bulk-update alert status / assignee on a background QThread.

    Emits ``update_done(success, error)`` when complete.
    """

    update_done = pyqtSignal(bool, str)

    def __init__(
        self,
        sdk: Alerts,
        composite_ids: list[str],
        new_status: str,
        assignee: str,
    ):
        """Initialise with SDK instance and update parameters."""
        super().__init__()
        self._sdk = sdk
        self._composite_ids = composite_ids
        self._new_status = new_status
        self._assignee = assignee

    def run(self) -> None:
        """Execute the bulk update and emit result."""
        try:
            if not self._composite_ids:
                self.update_done.emit(True, "")
                return

            # update_alerts_v2 expects "ids" (not "composite_ids") and encodes
            # mutations as action_parameters entries, not top-level keys.
            action_params: list[dict] = []
            if self._new_status:
                action_params.append({"name": "update_status", "value": self._new_status})
            if self._assignee.strip():
                action_params.append({"name": "assign_to_name",
                                      "value": self._assignee.strip()})

            request: dict = {
                "ids": self._composite_ids,
                "action_parameters": action_params,
            }

            resp = self._sdk.update_alerts_v2(body=request)
            if resp["status_code"] not in (200, 201):
                sc = resp["status_code"]
                raise RuntimeError(
                    f"update_alerts_v2 HTTP {sc}: "
                    f"{_extract_error_messages(resp['body'].get('errors', []))}"
                )
            self.update_done.emit(True, "")
        except Exception as exc:  # pylint: disable=broad-except
            self.update_done.emit(False, str(exc))


# ---------------------------------------------------------------------------
# Main window
# ---------------------------------------------------------------------------

class AlertsTriageApp(QMainWindow):
    """Main application window for the Alerts Triage Dashboard."""

    def __init__(self, client_id: str, client_secret: str):
        """Build the full UI and auto-run a default filtered query on startup.

        Defaults to last 24 hours + status = New so the user sees results
        immediately without manually selecting filters.
        """
        super().__init__()
        self._sdk = Alerts(client_id=client_id, client_secret=client_secret)
        self._all_alerts: list[dict] = []
        self._selected_ids: set[str] = set()
        # Pagination state
        self._page_index: int = 0        # current 0-based page
        self._page_size: int = DEFAULT_PAGE_SIZE
        # API-level pagination: offset token and whether more results exist beyond current batch
        self._api_next_offset: int = 0
        self._api_has_more: bool = False
        # Current filter snapshot for "fetch more" (must match original query context)
        self._last_fql: str = ""
        self._last_severity: str = ""
        self._last_status: str = ""
        self._last_hours: int = DEFAULT_HOURS
        # Keep a reference to active workers to prevent GC
        self._fetch_worker: AlertFetchWorker | None = None
        self._update_worker: AlertUpdateWorker | None = None

        # Widget references — declared here to satisfy pylint W0201;
        # populated by the _build_* helper methods called from _build_ui().
        self._fql_entry: QLineEdit
        self._severity_combo: QComboBox
        self._status_filter_combo: QComboBox
        self._hours_combo: QComboBox
        self._refresh_btn: QPushButton
        self._cancel_btn: QPushButton
        self._alert_table: QTableWidget
        self._detail_box: QTextEdit
        self._select_all_chk: QCheckBox
        self._bulk_status_combo: QComboBox
        self._assignee_entry: QLineEdit
        self._apply_btn: QPushButton
        self._prev_btn: QPushButton
        self._next_btn: QPushButton
        self._page_label: QLabel
        self._load_more_label: QLabel
        self._page_size_combo: QComboBox

        self.setWindowTitle("Alerts Triage Dashboard — loading…")
        self.resize(1280, 760)
        self.setMinimumSize(900, 600)

        self._build_ui()

        # Apply default filters and trigger initial query
        self._status_filter_combo.setCurrentText(DEFAULT_STATUS)
        self._hours_combo.setCurrentText(DEFAULT_TIME)
        self.statusBar().showMessage("Loading alerts (last 24 h)…")
        self._fetch_alerts()

    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------

    def _build_ui(self) -> None:
        """Assemble every widget in the window."""
        central = QWidget()
        self.setCentralWidget(central)
        root_layout = QVBoxLayout(central)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        root_layout.addWidget(self._build_filter_bar())
        root_layout.addWidget(self._build_main_splitter(), stretch=1)
        root_layout.addWidget(self._build_pagination_bar())
        root_layout.addWidget(self._build_bulk_toolbar())

    def _build_filter_bar(self) -> QWidget:
        """Top bar: FQL input, severity dropdown, status dropdown, time window, Refresh, Cancel."""
        filter_widget = QWidget()
        filter_widget.setObjectName("filterBar")
        layout = QHBoxLayout(filter_widget)
        layout.setContentsMargins(10, 6, 10, 6)
        layout.setSpacing(8)

        layout.addWidget(QLabel("Filter (FQL):"))
        self._fql_entry = QLineEdit()
        self._fql_entry.setPlaceholderText("e.g. agent_id:'abc123'")
        self._fql_entry.setMinimumWidth(200)
        self._fql_entry.returnPressed.connect(self._fetch_alerts)
        layout.addWidget(self._fql_entry, stretch=1)

        layout.addWidget(QLabel("Severity:"))
        self._severity_combo = QComboBox()
        self._severity_combo.addItems(SEVERITY_CHOICES)
        self._severity_combo.setFixedWidth(110)
        layout.addWidget(self._severity_combo)

        layout.addWidget(QLabel("Status:"))
        self._status_filter_combo = QComboBox()
        self._status_filter_combo.addItems(STATUS_CHOICES)
        self._status_filter_combo.setFixedWidth(110)
        layout.addWidget(self._status_filter_combo)

        layout.addWidget(QLabel("Time:"))
        self._hours_combo = QComboBox()
        self._hours_combo.addItems(["1h", "6h", "24h", "48h", "7d", "30d", "All"])
        self._hours_combo.setCurrentText(DEFAULT_TIME)
        self._hours_combo.setFixedWidth(70)
        layout.addWidget(self._hours_combo)

        self._refresh_btn = QPushButton("Refresh")
        self._refresh_btn.setFixedWidth(85)
        self._refresh_btn.clicked.connect(self._fetch_alerts)
        layout.addWidget(self._refresh_btn)

        self._cancel_btn = QPushButton("Cancel")
        self._cancel_btn.setFixedWidth(75)
        self._cancel_btn.setEnabled(False)
        self._cancel_btn.clicked.connect(self._cancel_fetch)
        layout.addWidget(self._cancel_btn)

        return filter_widget

    def _build_main_splitter(self) -> QSplitter:
        """Left = alert table, right = alert detail; separated by a sash."""
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Left: alert table
        self._alert_table = QTableWidget()
        self._alert_table.setColumnCount(len(COLUMN_HEADERS))
        self._alert_table.setHorizontalHeaderLabels(COLUMN_HEADERS)
        self._alert_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self._alert_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self._alert_table.setSelectionMode(QTableWidget.SelectionMode.MultiSelection)
        self._alert_table.verticalHeader().setVisible(False)
        self._alert_table.setAlternatingRowColors(True)
        self._alert_table.setSortingEnabled(True)
        hdr = self._alert_table.horizontalHeader()
        for col, width in enumerate(COLUMN_WIDTHS):
            self._alert_table.setColumnWidth(col, width)
        hdr.setStretchLastSection(False)
        hdr.setSectionResizeMode(COL_TACTIC, QHeaderView.ResizeMode.Stretch)
        self._alert_table.itemSelectionChanged.connect(self._on_table_selection_changed)
        self._alert_table.cellClicked.connect(self._on_cell_clicked)
        splitter.addWidget(self._alert_table)

        # Right: detail panel
        detail_widget = QWidget()
        detail_layout = QVBoxLayout(detail_widget)
        detail_layout.setContentsMargins(8, 8, 8, 8)
        detail_label = QLabel("Alert Detail")
        bold_font = QFont()
        bold_font.setBold(True)
        bold_font.setPointSize(12)
        detail_label.setFont(bold_font)
        detail_layout.addWidget(detail_label)
        self._detail_box = QTextEdit()
        self._detail_box.setReadOnly(True)
        self._detail_box.setFontFamily("Courier New")
        detail_layout.addWidget(self._detail_box)
        splitter.addWidget(detail_widget)

        splitter.setSizes([800, 480])
        return splitter

    def _build_pagination_bar(self) -> QWidget:
        """Thin bar below the alert table: Prev/Next, page counter, page size."""
        pagination_widget = QWidget()
        pagination_widget.setObjectName("paginationBar")
        layout = QHBoxLayout(pagination_widget)
        layout.setContentsMargins(10, 3, 10, 3)
        layout.setSpacing(8)

        self._prev_btn = QPushButton("◀ Prev")
        self._prev_btn.setFixedWidth(75)
        self._prev_btn.setEnabled(False)
        self._prev_btn.clicked.connect(self._go_prev_page)
        layout.addWidget(self._prev_btn)

        self._page_label = QLabel("Page 1 of 1  (0 alerts)")
        layout.addWidget(self._page_label)

        self._next_btn = QPushButton("Next ▶")
        self._next_btn.setFixedWidth(75)
        self._next_btn.setEnabled(False)
        self._next_btn.clicked.connect(self._go_next_page)
        layout.addWidget(self._next_btn)

        # Inline loading indicator shown while a progressive batch is fetching.
        self._load_more_label = QLabel("Loading more…")
        self._load_more_label.setStyleSheet("color: #89b4fa; font-style: italic;")
        self._load_more_label.setVisible(False)
        layout.addWidget(self._load_more_label)

        layout.addStretch()

        layout.addWidget(QLabel("Per page:"))
        self._page_size_combo = QComboBox()
        self._page_size_combo.addItems(PAGE_SIZE_CHOICES)
        self._page_size_combo.setCurrentText(str(DEFAULT_PAGE_SIZE))
        self._page_size_combo.setFixedWidth(65)
        self._page_size_combo.currentTextChanged.connect(self._on_page_size_changed)
        layout.addWidget(self._page_size_combo)

        return pagination_widget

    def _build_bulk_toolbar(self) -> QWidget:
        """Toolbar below main panes: select-all, status update, assign-to."""
        toolbar = QWidget()
        toolbar.setObjectName("bulkToolbar")
        layout = QHBoxLayout(toolbar)
        layout.setContentsMargins(10, 4, 10, 4)
        layout.setSpacing(8)

        self._select_all_chk = QCheckBox("Select all")
        self._select_all_chk.stateChanged.connect(self._on_select_all)
        layout.addWidget(self._select_all_chk)

        layout.addWidget(QLabel("Set status:"))
        self._bulk_status_combo = QComboBox()
        self._bulk_status_combo.addItems(["", "new", "in_progress", "closed"])
        self._bulk_status_combo.setFixedWidth(110)
        layout.addWidget(self._bulk_status_combo)

        layout.addWidget(QLabel("Assign to:"))
        self._assignee_entry = QLineEdit()
        self._assignee_entry.setPlaceholderText("username or email")
        self._assignee_entry.setFixedWidth(200)
        layout.addWidget(self._assignee_entry)

        self._apply_btn = QPushButton("Apply")
        self._apply_btn.setFixedWidth(75)
        self._apply_btn.clicked.connect(self._apply_bulk_action)
        layout.addWidget(self._apply_btn)

        layout.addStretch()
        return toolbar

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

    def _fetch_alerts(self) -> None:
        """Kick off a background alert fetch using current filter values."""
        # Cancel any running fetch before starting a new one
        if self._fetch_worker and self._fetch_worker.isRunning():
            self._fetch_worker.cancel()
            self._fetch_worker.wait(2000)

        # Parse time window from combo
        time_text = self._hours_combo.currentText()
        _time_map = {"1h": 1, "6h": 6, "24h": 24, "48h": 48, "7d": 168, "30d": 720, "All": 0}
        hours = _time_map.get(time_text, DEFAULT_HOURS)

        # Snapshot current filter values for progressive "fetch more" batches.
        self._last_fql = self._fql_entry.text()
        self._last_severity = self._severity_combo.currentText()
        self._last_status = self._status_filter_combo.currentText()
        self._last_hours = hours

        # Reset API continuation state for a fresh query.
        self._api_next_offset = 0
        self._api_has_more = False
        self._load_more_label.setVisible(False)

        # Clear the table for the new fetch
        self._alert_table.setSortingEnabled(False)
        self._alert_table.setRowCount(0)
        self._all_alerts.clear()
        self._selected_ids.clear()
        self._page_index = 0
        self._prev_btn.setEnabled(False)
        self._next_btn.setEnabled(False)
        self._page_label.setText("Page 1 of 1  (0 alerts)")

        self.statusBar().showMessage(f"Fetching alerts (last {time_text}, max {MAX_RESULTS})…")
        self._refresh_btn.setEnabled(False)
        self._cancel_btn.setEnabled(True)

        self._fetch_worker = AlertFetchWorker(
            sdk=self._sdk,
            fql_filter=self._last_fql,
            severity=self._last_severity,
            status=self._last_status,
            hours=self._last_hours,
            max_results=MAX_RESULTS,
        )
        self._fetch_worker.alerts_batch.connect(self._on_alerts_batch)
        self._fetch_worker.next_offset.connect(self._on_next_offset)
        self._fetch_worker.fetch_done.connect(self._on_fetch_done)
        self._fetch_worker.start()

    def _cancel_fetch(self) -> None:
        """Cancel a running fetch."""
        if self._fetch_worker and self._fetch_worker.isRunning():
            self._fetch_worker.cancel()
            self.statusBar().showMessage("Cancelling…")

    def _on_alerts_batch(self, batch: list) -> None:
        """Accumulate a batch of alert records; update progress in status bar."""
        self._all_alerts.extend(batch)
        self.statusBar().showMessage(
            f"Fetching… {len(self._all_alerts)} alert(s) received"
        )

    def _on_fetch_done(self, error: str) -> None:
        """Handle fetch completion on the main thread (Qt signal)."""
        self._refresh_btn.setEnabled(True)
        self._cancel_btn.setEnabled(False)

        if error:
            self.setWindowTitle("Alerts Triage Dashboard — connection error")
            self.statusBar().showMessage(f"Error: {error}")
            QMessageBox.critical(self, "Fetch Error", error)
            return

        self._select_all_chk.setCheckState(Qt.CheckState.Unchecked)
        total = len(self._all_alerts)
        label = f"{total} alert(s)" if total else "no alerts"
        self.setWindowTitle(f"Alerts Triage Dashboard — {label}")
        self._page_index = 0
        self._render_current_page()

    def _on_next_offset(self, offset: int, has_more: bool) -> None:
        """Store the API continuation offset and more-available flag from a completed fetch."""
        self._api_next_offset = offset
        self._api_has_more = has_more

    def _fetch_more_alerts(self) -> None:
        """Fetch the next batch from the API using the stored continuation offset."""
        if not self._api_has_more:
            return
        if self._fetch_worker and self._fetch_worker.isRunning():
            return  # Don't stack requests.

        self._next_btn.setEnabled(False)
        self._load_more_label.setText("Loading more…")
        self._load_more_label.setVisible(True)

        self._fetch_worker = AlertFetchWorker(
            sdk=self._sdk,
            fql_filter=self._last_fql,
            severity=self._last_severity,
            status=self._last_status,
            hours=self._last_hours,
            max_results=MAX_RESULTS,
            start_offset=self._api_next_offset,
        )
        self._fetch_worker.alerts_batch.connect(self._on_more_alerts_batch)
        self._fetch_worker.next_offset.connect(self._on_next_offset)
        self._fetch_worker.fetch_done.connect(self._on_more_fetch_done)
        self._fetch_worker.start()

    def _on_more_alerts_batch(self, batch: list) -> None:
        """Append a batch of additional alert records to the existing list."""
        self._all_alerts.extend(batch)
        self.statusBar().showMessage(
            f"Loading more… {len(self._all_alerts)} alert(s) total"
        )

    def _on_more_fetch_done(self, error: str) -> None:
        """Handle completion of a progressive 'fetch more' operation."""
        self._refresh_btn.setEnabled(True)
        self._load_more_label.setVisible(False)
        if error:
            self.statusBar().showMessage(f"Error loading more: {error}", 8000)
            QMessageBox.critical(self, "Fetch Error", error)
            return

        # Move to the first new page that was just appended.
        total = len(self._all_alerts)
        label = f"{total} alert(s)"
        self.setWindowTitle(f"Alerts Triage Dashboard — {label}")
        self._render_current_page()



    # ------------------------------------------------------------------
    # Pagination helpers
    # ------------------------------------------------------------------

    def _render_current_page(self) -> None:
        """Render the current page of _all_alerts into the table."""
        total = len(self._all_alerts)
        total_pages = max(1, (total + self._page_size - 1) // self._page_size)
        self._page_index = max(0, min(self._page_index, total_pages - 1))

        start = self._page_index * self._page_size
        end = min(start + self._page_size, total)
        page_alerts = self._all_alerts[start:end]

        self._alert_table.setSortingEnabled(False)
        self._alert_table.setRowCount(0)
        self._selected_ids.clear()
        for alert in page_alerts:
            row = self._alert_table.rowCount()
            self._alert_table.insertRow(row)
            self._populate_alert_row(row, alert)
        self._alert_table.setSortingEnabled(True)

        self._prev_btn.setEnabled(self._page_index > 0)
        on_last_page = self._page_index >= total_pages - 1
        # Enable Next if there are more local pages OR more API data to load.
        self._next_btn.setEnabled(not on_last_page or self._api_has_more)
        pages_str = f"{total_pages}+" if self._api_has_more else str(total_pages)
        self._page_label.setText(
            f"Page {self._page_index + 1} of {pages_str}  ({total} alerts)"
        )
        more_hint = " (more available)" if self._api_has_more else ""
        suffix = f" (capped at {MAX_RESULTS})" if total >= MAX_RESULTS else ""
        self.statusBar().showMessage(
            f"Total: {total}{suffix}{more_hint}"
            f"  |  Page {self._page_index + 1}/{pages_str}  |  Selected: 0"
        )

    def _go_prev_page(self) -> None:
        """Navigate to the previous page."""
        if self._page_index > 0:
            self._page_index -= 1
            self._render_current_page()

    def _go_next_page(self) -> None:
        """Navigate to the next page; trigger progressive load if on the last local page."""
        total = len(self._all_alerts)
        total_pages = max(1, (total + self._page_size - 1) // self._page_size)
        if self._page_index < total_pages - 1:
            self._page_index += 1
            self._render_current_page()
        elif self._api_has_more:
            # On the last local page and the API has more — fetch the next batch.
            self._fetch_more_alerts()

    def _on_page_size_changed(self, text: str) -> None:
        """Handle page size combo change — re-render from page 0."""
        try:
            self._page_size = int(text)
        except ValueError:
            self._page_size = DEFAULT_PAGE_SIZE
        self._page_index = 0
        self._render_current_page()

    # ------------------------------------------------------------------
    # Alert table rendering
    # ------------------------------------------------------------------

    def _populate_alert_row(self, row: int, alert: dict) -> None:
        """Fill one table row from an alert dict."""
        # Use severity_name (string) when available; fall back to numeric severity.
        # severity is an int (1–5) from the API; severity_name is e.g. "Informational".
        sev_name = str(alert.get("severity_name") or alert.get("severity") or "unknown").lower()
        color_hex = SEVERITY_COLORS.get(sev_name, SEVERITY_COLORS["unknown"])

        # Target: for CWPP/cloud alerts there is no device/hostname; use image repo:tag.
        # For endpoint alerts fall back to device.hostname or agent_id.
        device = alert.get("device") or {}
        hostname = str(device.get("hostname") or alert.get("hostname") or "")
        aid = str(device.get("agent_id") or device.get("device_id") or
                  alert.get("agent_id") or "")
        if hostname:
            # Endpoint alert — show "hostname (AID)" if AID available.
            raw_target = f"{hostname} ({aid})" if aid else hostname
        else:
            repo = str(alert.get("image_repository") or "")
            tag = str(alert.get("image_tag") or "")
            if repo:
                # CWPP / cloud alert — show "repo:tag (cloud)".
                label = f"{repo}:{tag}" if tag else repo
                raw_target = f"{label} (cloud)"
            else:
                # Fallback: bare AID.
                raw_target = aid or ""
        target = _truncate(raw_target, TARGET_MAX)

        tactic = _truncate(
            str(alert.get("name") or alert.get("tactic") or alert.get("display_name") or ""),
            TACTIC_MAX,
        )
        status = str(alert.get("status") or "")
        created = _format_ts(
            str(alert.get("created_timestamp") or alert.get("timestamp") or "")
        )
        composite_id = str(alert.get("composite_id") or "")

        # Severity badge cell — coloured background, full severity label, contrasting text
        fg_hex = SEVERITY_FG_COLORS.get(sev_name, "#FFFFFF")
        sev_display = sev_name.capitalize() if sev_name != "unknown" else "Unknown"
        sev_item = QTableWidgetItem(sev_display)
        sev_item.setBackground(QBrush(QColor(color_hex)))
        sev_item.setForeground(QBrush(QColor(fg_hex)))
        sev_item.setTextAlignment(int(Qt.AlignmentFlag.AlignCenter))
        sev_item.setData(Qt.ItemDataRole.UserRole, alert)  # store full alert on severity cell
        sev_item.setData(Qt.ItemDataRole.UserRole + 1, composite_id)
        self._alert_table.setItem(row, COL_SEVERITY, sev_item)

        self._alert_table.setItem(row, COL_TARGET, QTableWidgetItem(target))
        self._alert_table.setItem(row, COL_TACTIC, QTableWidgetItem(tactic))
        self._alert_table.setItem(row, COL_STATUS, QTableWidgetItem(status))
        self._alert_table.setItem(row, COL_CREATED, QTableWidgetItem(created))

    # ------------------------------------------------------------------
    # Detail panel
    # ------------------------------------------------------------------

    def _on_table_selection_changed(self) -> None:
        """Update the selected-IDs set when the table selection changes."""
        selected_rows = self._alert_table.selectionModel().selectedRows()
        self._selected_ids.clear()
        for idx in selected_rows:
            sev_item = self._alert_table.item(idx.row(), COL_SEVERITY)
            if sev_item:
                cid = sev_item.data(Qt.ItemDataRole.UserRole + 1)
                if cid:
                    self._selected_ids.add(cid)
        self._update_status_counts()

    def _on_cell_clicked(self, row: int, _col: int) -> None:
        """Show detail for the most recently clicked row, regardless of multi-select state."""
        sev_item = self._alert_table.item(row, COL_SEVERITY)
        if sev_item:
            alert = sev_item.data(Qt.ItemDataRole.UserRole)
            if alert:
                self._show_detail(alert)

    def _show_detail(self, alert: dict) -> None:
        """Populate the right-hand detail panel with the selected alert."""
        lines = []

        def _field(label: str, key: str, src: dict | None = None) -> None:
            """Append 'label: value' using src (or alert) as the dict."""
            d = src if src is not None else alert
            val = d.get(key, "")
            if val:
                lines.append(f"{label}: {val}")

        lines.append("=" * 52)
        lines.append(f"Composite ID:  {alert.get('composite_id', '')}")
        lines.append("=" * 52)
        _field("Severity",     "severity_name")
        _field("Status",       "status")
        _field("Name",         "name")
        _field("Title",        "title")
        _field("Tactic",       "tactic")
        _field("Technique",    "technique")
        _field("Display Name", "display_name")
        _field("Description",  "description")
        lines.append("")
        # Device fields (endpoint alerts)
        device = alert.get("device") or {}
        if device:
            lines.append("--- Device ---")
            _field("Hostname",     "hostname",      device)
            _field("AID",          "device_id",     device)
            _field("OS",           "os_version",    device)
            _field("Platform",     "platform_name", device)
            lines.append("")
        # Cloud / CWPP fields
        if alert.get("image_repository") or alert.get("cwpp_detect_id"):
            lines.append("--- Cloud / Image ---")
            _field("Registry",     "image_registry")
            _field("Repository",   "image_repository")
            _field("Tag",          "image_tag")
            _field("OS Name",      "os_name")
            _field("OS Version",   "os_version")
            _field("CWPP ID",      "cwpp_detect_id")
            lines.append("")
        lines.append("--- Timestamps ---")
        _field("Created",      "created_timestamp")
        _field("Updated",      "updated_timestamp")
        lines.append("")
        lines.append("--- Assignment ---")
        _field("Assigned to",  "assigned_to_name")
        _field("Assigned UID", "assigned_to_uid")
        comments = alert.get("comments") or []
        if comments:
            lines.append("")
            lines.append("--- Comments ---")
            for c in comments:
                author = c.get("author", "?")
                body = c.get("body", "")
                ts = _format_ts(c.get("created_timestamp", ""))
                lines.append(f"  [{ts}] {author}: {body}")

        self._detail_box.setPlainText("\n".join(lines))

    # ------------------------------------------------------------------
    # Selection management
    # ------------------------------------------------------------------

    def _on_select_all(self, state: int) -> None:
        """Toggle selection on all rows when the select-all checkbox changes."""
        if state == Qt.CheckState.Checked.value:
            self._alert_table.selectAll()
        else:
            self._alert_table.clearSelection()
        self._update_status_counts()

    # ------------------------------------------------------------------
    # Bulk actions
    # ------------------------------------------------------------------

    def _apply_bulk_action(self) -> None:
        """Apply the selected status / assignee to all checked alerts."""
        if not self._selected_ids:
            self.statusBar().showMessage("No alerts selected.")
            return
        new_status = self._bulk_status_combo.currentText()
        assignee = self._assignee_entry.text()
        if not new_status and not assignee.strip():
            self.statusBar().showMessage("Set a status or assignee before applying.")
            return

        self._apply_btn.setEnabled(False)
        self.statusBar().showMessage(f"Updating {len(self._selected_ids)} alert(s)…")

        self._update_worker = AlertUpdateWorker(
            sdk=self._sdk,
            composite_ids=list(self._selected_ids),
            new_status=new_status,
            assignee=assignee,
        )
        self._update_worker.update_done.connect(self._on_update_done)
        self._update_worker.start()

    def _on_update_done(self, ok: bool, error: str) -> None:  # pylint: disable=unused-argument
        """Handle bulk-update result on the main thread (Qt signal)."""
        self._apply_btn.setEnabled(True)
        if error:
            self.statusBar().showMessage(f"Update failed: {error}")
            QMessageBox.warning(self, "Update Failed", error)
            return

        new_status = self._bulk_status_combo.currentText()
        count = len(self._selected_ids)
        updated_ids = frozenset(self._selected_ids)
        self._selected_ids.clear()
        self._alert_table.clearSelection()

        # Update _all_alerts in-place so page re-renders show the new status.
        if new_status:
            for alert in self._all_alerts:
                if alert.get("composite_id") in updated_ids:
                    alert["status"] = new_status

        # Update visible table cells without a full API re-query.
        # Iterating the current page rows is enough — off-page rows are covered
        # by the _all_alerts update above (used when page is re-rendered later).
        if new_status:
            for row in range(self._alert_table.rowCount()):
                sev_item = self._alert_table.item(row, COL_SEVERITY)
                if not sev_item:
                    continue
                cid = sev_item.data(Qt.ItemDataRole.UserRole + 1)
                if cid in updated_ids:
                    status_item = self._alert_table.item(row, COL_STATUS)
                    if status_item:
                        status_item.setText(new_status)

        self.statusBar().showMessage(f"Updated {count} alert(s) successfully.")

    # ------------------------------------------------------------------
    # Status bar helpers
    # ------------------------------------------------------------------

    def _update_status_counts(self) -> None:
        """Refresh the status bar with total and selected counts."""
        total = len(self._all_alerts)
        selected = len(self._selected_ids)
        total_pages = max(1, (total + self._page_size - 1) // self._page_size)
        self.statusBar().showMessage(
            f"Total: {total}  |  Page {self._page_index + 1}/{total_pages}  |  Selected: {selected}"
        )


# ---------------------------------------------------------------------------
# Theme
# ---------------------------------------------------------------------------

def _dark_palette() -> QPalette:
    """Return a dark QPalette for use with the Fusion style."""
    p = QPalette()
    # Base colours
    dark        = QColor(45,  45,  45)
    mid_dark    = QColor(55,  55,  55)
    mid         = QColor(65,  65,  65)
    mid_light   = QColor(75,  75,  75)
    light       = QColor(90,  90,  90)
    text        = QColor(210, 210, 210)
    dim_text    = QColor(140, 140, 140)
    highlight   = QColor(42,  130, 218)
    hi_text     = QColor(255, 255, 255)
    link        = QColor(80,  160, 230)

    p.setColor(QPalette.ColorRole.Window,          dark)
    p.setColor(QPalette.ColorRole.WindowText,      text)
    p.setColor(QPalette.ColorRole.Base,            mid_dark)
    p.setColor(QPalette.ColorRole.AlternateBase,   dark)
    p.setColor(QPalette.ColorRole.ToolTipBase,     mid_dark)
    p.setColor(QPalette.ColorRole.ToolTipText,     text)
    p.setColor(QPalette.ColorRole.Text,            text)
    p.setColor(QPalette.ColorRole.Button,          mid)
    p.setColor(QPalette.ColorRole.ButtonText,      text)
    p.setColor(QPalette.ColorRole.BrightText,      hi_text)
    p.setColor(QPalette.ColorRole.Link,            link)
    p.setColor(QPalette.ColorRole.Highlight,       highlight)
    p.setColor(QPalette.ColorRole.HighlightedText, hi_text)
    # Disabled state
    p.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, dim_text)
    p.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text,       dim_text)
    p.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, dim_text)
    p.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button,     mid_light)
    p.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base,       mid_dark)
    # Mid / shadow shades used by Fusion for borders and panel separators
    p.setColor(QPalette.ColorRole.Mid,        light)
    p.setColor(QPalette.ColorRole.Shadow,     QColor(20, 20, 20))
    p.setColor(QPalette.ColorRole.Dark,       mid_dark)
    p.setColor(QPalette.ColorRole.Midlight,   mid_light)
    return p


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Parse credentials from CLI args or environment variables and launch the GUI."""
    parser = argparse.ArgumentParser(
        description="Alerts Triage Dashboard — CrowdStrike Falcon",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Credentials can also be provided via environment variables:\n"
            "  FALCON_CLIENT_ID      API client ID\n"
            "  FALCON_CLIENT_SECRET  API client secret\n\n"
            "CLI arguments take precedence over environment variables."
        ),
    )
    parser.add_argument(
        "-k", "--client-id",
        metavar="CLIENT_ID",
        default="",
        help="Falcon API client ID (overrides FALCON_CLIENT_ID env var)",
    )
    parser.add_argument(
        "-s", "--client-secret",
        metavar="CLIENT_SECRET",
        default="",
        help="Falcon API client secret (overrides FALCON_CLIENT_SECRET env var)",
    )
    args = parser.parse_args()

    client_id = args.client_id or os.environ.get("FALCON_CLIENT_ID", "")
    client_secret = args.client_secret or os.environ.get("FALCON_CLIENT_SECRET", "")

    if not client_id or not client_secret:
        print(
            "ERROR: Falcon credentials not found.\n"
            "Provide them via environment variables or -k / -s arguments:\n"
            "  FALCON_CLIENT_ID=xxx FALCON_CLIENT_SECRET=yyy pipenv run python3 alerts_triage.py\n"
            "  pipenv run python3 alerts_triage.py -k CLIENT_ID -s CLIENT_SECRET",
            file=sys.stderr,
        )
        sys.exit(1)

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette(_dark_palette())
    window = AlertsTriageApp(client_id=client_id, client_secret=client_secret)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
