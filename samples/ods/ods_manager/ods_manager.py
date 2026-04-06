r"""On-Demand Scan (ODS) Manager.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |             FalconPy
`-------'                         `-------'

  ___   ___    _____     ___ ___   ____  ____    ____   ____    ___  ____
 /   \ |   \  / ___/    |   T   T /    T|    \  /    T /    T  /  _]|    \
Y     Y|    \(   \_     | _   _ |Y  o  ||  _  YY  o  |Y   __j /  [_ |  D  )
|  O  ||  D  Y\__  T    |  \_/  ||     ||  |  ||     ||  T  |Y    _]|    /
|     ||     |/  \ |    |   |   ||  _  ||  |  ||  _  ||  l_ ||   [_ |    \
l     !|     |\    |    |   |   ||  |  ||  |  ||  |  ||     ||     T|  .  Y
 \___/ l_____j \___j    l___j___jl__j__jl__j__jl__j__jl___,_jl_____jl__j\_j

                    On-Demand Scan (ODS) Manager
                    Uses: ODS
                    Scope: on-demand-scans:read, on-demand-scans:write

A wxPython desktop application for managing CrowdStrike Falcon On-Demand
Scans — launch agent-side AV scans, monitor progress, inspect per-host
results, and cancel or delete scan jobs.

Layout
------
  Top:     toolbar — New Scan, Refresh, Cancel Selected, Delete Selected
                     (Delete explains the API limitation; Cancel changes status to 'canceled')
  Centre:  wx.ListCtrl scan job table (scan ID, status, target count,
           initiated by, start time, findings)
  Bottom:  split panel — per-host progress grid on the left,
           findings summary text on the right
  Polling: wx.Timer fires every 15 s; in-progress rows update in place

Authentication
--------------
  Reads FALCON_CLIENT_ID and FALCON_CLIENT_SECRET from the environment at
  launch.  If either is absent, a wx.MessageDialog is shown and the app
  exits cleanly.

Usage
-----
    FALCON_CLIENT_ID=xxx FALCON_CLIENT_SECRET=yyy pipenv run python3 ods_manager.py

Required API scopes
-------------------
  on-demand-scans:read
  on-demand-scans:write
"""
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals,too-many-statements
# pylint: disable=too-many-instance-attributes,too-many-branches
# pylint: disable=too-few-public-methods

import argparse
import os
import sys
import threading
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

import wx
import wx.lib.mixins.listctrl as listmix
from falconpy import Hosts, ODS

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

APP_TITLE = "ODS Manager — CrowdStrike Falcon On-Demand Scan"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 860

# How often the status-polling timer fires (milliseconds)
POLL_INTERVAL_MS = 15_000

# Default file paths pre-populated in the New Scan dialog
DEFAULT_SCAN_PATHS = ["C:\\", "D:\\", "/"]

# Statuses that are still running and should be polled
ACTIVE_STATUSES = {"pending_stop", "running", "pending", "queued"}

# Colour table used to tint status text in the scan list
STATUS_COLOURS = {
    "running":       wx.Colour(50, 200, 80),
    "complete":      wx.Colour(100, 180, 255),
    "failed":        wx.Colour(220, 50, 50),
    "cancelled":     wx.Colour(180, 130, 50),
    "pending_stop":  wx.Colour(220, 200, 50),
    "queued":        wx.Colour(180, 180, 180),
    "pending":       wx.Colour(180, 180, 180),
}

# Columns for the main scan table
SCAN_COLUMNS = [
    ("Scan ID",       180),
    ("Status",        110),
    ("Targets",        70),
    ("Initiated By",  160),
    ("Started",       160),
    ("Findings",       80),
    ("Description",   220),
]

# Columns for the per-host table in the detail panel
HOST_COLUMNS = [
    ("Host ID",  180),
    ("Status",   110),
    ("Scanned",   80),
    ("Malicious", 80),
    ("Quarant.",  80),
    ("Started",  155),
]


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

class ScanRecord:
    """Holds display-ready data for one ODS scan job."""

    def __init__(self, raw: dict):
        """Initialise from the raw API resource dict for one scan."""
        self.scan_id: str = raw.get("id", "")
        self.status: str = raw.get("status", "unknown")
        self.description: str = raw.get("description", "")
        self.initiated_from: str = raw.get("initiated_from", "")
        self.affected_hosts_count: int = int(raw.get("affected_hosts_count", 0))
        self.created_by: str = raw.get("created_by", "")

        # File-count sub-object
        fc = raw.get("filecount", {})
        self.scanned: int = int(fc.get("scanned", 0))
        self.malicious: int = int(fc.get("malicious", 0))
        self.quarantined: int = int(fc.get("quarantined", 0))

        # Timestamps — keep only the date+time portion
        self.scan_started_on: str = _trim_ts(raw.get("scan_started_on", ""))
        self.scan_completed_on: str = _trim_ts(raw.get("scan_completed_on", ""))
        self.created_on: str = _trim_ts(raw.get("created_on", ""))

        # Host count breakdown for failure diagnosis
        self.targeted_host_count: int = int(raw.get("targeted_host_count", 0))
        self.missing_host_count: int = int(raw.get("missing_host_count", 0))
        self.not_started_host_count: int = int(raw.get("not_started_host_count", 0))

    def list_row(self) -> list:
        """Return values for each column in SCAN_COLUMNS order."""
        started = self.scan_started_on or self.created_on
        findings = self.malicious + self.quarantined
        return [
            self.scan_id[:24] + "…" if len(self.scan_id) > 24 else self.scan_id,
            self.status,
            str(self.affected_hosts_count),
            self.initiated_from or self.created_by,
            started,
            str(findings),
            self.description,
        ]

    @property
    def is_active(self) -> bool:
        """True when the scan is still running and progress should be polled."""
        return self.status.lower() in ACTIVE_STATUSES


class HostRecord:
    """Holds per-host scan progress for the detail panel."""

    def __init__(self, raw: dict):
        """Initialise from one item in the scan-host-metadata resource list."""
        self.host_id: str = raw.get("host_id", "")
        self.status: str = raw.get("status", "unknown")
        self.scan_control_reason: str = raw.get("scan_control_reason", "")
        fc = raw.get("filecount", {})
        self.scanned: int = int(fc.get("scanned", 0))
        self.malicious: int = int(fc.get("malicious", 0))
        self.quarantined: int = int(fc.get("quarantined", 0))
        self.started_on: str = _trim_ts(raw.get("started_on", ""))

    def list_row(self) -> list:
        """Return values for each column in HOST_COLUMNS order."""
        status_display = self.status
        if self.scan_control_reason:
            status_display = f"{self.status} ({self.scan_control_reason})"
        return [
            self.host_id[:24] + "…" if len(self.host_id) > 24 else self.host_id,
            status_display,
            str(self.scanned),
            str(self.malicious),
            str(self.quarantined),
            self.started_on,
        ]


@dataclass
class ScanRequest:
    """Parameters for creating a new ODS scan job."""

    hosts: list[str] = field(default_factory=list)
    host_groups: list[str] = field(default_factory=list)
    description: str = ""
    cpu_priority: int = 2
    quarantine: bool = True
    file_paths: list[str] = field(default_factory=list)
    scan_exclusions: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def _trim_ts(ts: str) -> str:
    """Return the first 19 characters of an ISO-8601 timestamp as 'YYYY-MM-DD HH:MM:SS'."""
    if not ts:
        return ""
    return ts[:19].replace("T", " ")


# ---------------------------------------------------------------------------
# FalconPy client wrapper
# ---------------------------------------------------------------------------

class ODSClient:
    """Thin wrapper around the FalconPy ODS service class."""

    def __init__(self):
        """Construct without authenticating — call connect() first."""
        self._sdk: Optional[ODS] = None
        self._hosts_sdk: Optional[Hosts] = None
        self.status: str = "disconnected"
        self.error: str = ""

    def connect(self, client_id: str = "", client_secret: str = "") -> bool: # nosec - Bandit FP
        """Authenticate against the Falcon API and return True on success.

        *client_id* and *client_secret* override the FALCON_CLIENT_ID /
        FALCON_CLIENT_SECRET environment variables when provided (non-empty).
        Populates self.error on failure.
        """
        client_id = client_id or os.environ.get("FALCON_CLIENT_ID", "")
        client_secret = client_secret or os.environ.get("FALCON_CLIENT_SECRET", "")
        if not client_id or not client_secret:
            self.error = (
                "Credentials not found.\n"
                "Set FALCON_CLIENT_ID / FALCON_CLIENT_SECRET environment variables\n"
                "or pass them with -k / -s command-line arguments."
            )
            self.status = "error"
            return False
        try:
            sdk = ODS(client_id=client_id, client_secret=client_secret)
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

    # ------------------------------------------------------------------
    # Scan operations
    # ------------------------------------------------------------------

    def query_scans(self, fql_filter: str = "", limit: int = 200) -> list[str]:
        """Return a list of scan IDs matching *fql_filter* (up to *limit*)."""
        if self._sdk is None:
            return []
        resp = self._sdk.query_scans(filter=fql_filter, limit=limit, sort="created_on|desc")
        if resp.get("status_code", 0) != 200:
            return []
        return resp.get("body", {}).get("resources", [])

    def get_scans(self, scan_ids: list[str]) -> list[ScanRecord]:
        """Return a list of ScanRecord objects for the given scan IDs."""
        if self._sdk is None or not scan_ids:
            return []
        resp = self._sdk.get_scans(ids=scan_ids)
        if resp.get("status_code", 0) != 200:
            return []
        return [ScanRecord(r) for r in resp.get("body", {}).get("resources", [])]

    def create_scan(self, params: "ScanRequest") -> tuple[bool, str]:
        """Launch a new ODS scan and return (success, message).

        Either params.hosts or params.host_groups must be non-empty.
        """
        if self._sdk is None:
            return False, "Not connected."
        body: dict = {
            "description": params.description,
            "cpu_priority": params.cpu_priority,
            "quarantine": params.quarantine,
            "initiated_from": "ods_manager",
        }
        if params.hosts:
            body["hosts"] = params.hosts
        if params.host_groups:
            body["host_groups"] = params.host_groups
        if params.file_paths:
            body["file_paths"] = params.file_paths
        if params.scan_exclusions:
            body["scan_exclusions"] = params.scan_exclusions

        resp = self._sdk.create_scan(body=body)
        sc = resp.get("status_code", 0)
        if sc in (200, 201, 202):
            return True, "Scan created successfully."
        body_data = resp.get("body", {})
        errors = body_data.get("errors", [])
        trace_id = body_data.get("meta", {}).get("trace_id", "")
        if errors:
            messages = "; ".join(
                e.get("message", f"code {e.get('code', '?')}") for e in errors
            )
        else:
            messages = f"HTTP {sc}"
        if trace_id:
            return False, f"{messages}\n\nTrace ID: {trace_id}"
        return False, messages

    def cancel_scans(self, scan_ids: list[str]) -> tuple[bool, str]:
        """Cancel the specified scans and return (success, message).

        cancel_scans changes the scan status to 'canceled'.  It works on active,
        failed, and completed scans.  It does NOT remove the scan record — the
        ODS API provides no endpoint to delete on-demand scan records.
        """
        if self._sdk is None or not scan_ids:
            return False, "Nothing to cancel."
        resp = self._sdk.cancel_scans(ids=scan_ids)
        sc = resp.get("status_code", 0)
        if sc in (200, 202):
            return True, f"Cancelled {len(scan_ids)} scan(s)."
        errors = resp.get("body", {}).get("errors", [])
        msg = errors[0].get("message", "Unknown error") if errors else f"HTTP {sc}"
        return False, msg

    def get_host_metadata(self, scan_id: str) -> list[HostRecord]:
        """Return per-host metadata for the given scan_id."""
        if self._sdk is None or not scan_id:
            return []
        # First query for host metadata IDs scoped to this scan
        resp_ids = self._sdk.query_scan_host_metadata(
            filter=f"scan_id:'{scan_id}'", limit=500
        )
        if resp_ids.get("status_code", 0) != 200:
            return []
        ids = resp_ids.get("body", {}).get("resources", [])
        if not ids:
            return []
        resp = self._sdk.get_scan_host_metadata_by_ids(ids=ids)
        if resp.get("status_code", 0) != 200:
            return []
        return [HostRecord(r) for r in resp.get("body", {}).get("resources", [])]

    def query_available_hosts(self, limit: int = 500) -> list[dict]:
        """Return a list of available hosts as dicts with hostname, device_id, and status.

        Returns an empty list if the Hosts SDK is unavailable or the query fails.
        """
        if self._hosts_sdk is None:
            return []
        try:
            resp = self._hosts_sdk.query_devices_by_filter(limit=limit)
            if resp.get("status_code", 0) != 200:
                return []
            ids = resp.get("body", {}).get("resources", [])
            if not ids:
                return []
            detail_resp = self._hosts_sdk.get_device_details(ids=ids)
            if detail_resp.get("status_code", 0) != 200:
                return []
            hosts = []
            for device in detail_resp.get("body", {}).get("resources", []):
                hosts.append({
                    "hostname": device.get("hostname", ""),
                    "device_id": device.get("device_id", ""),
                    "status": device.get("status", ""),
                })
            hosts.sort(key=lambda h: h["hostname"].lower())
            return hosts
        except Exception:  # pylint: disable=broad-except
            return []


# ---------------------------------------------------------------------------
# wx.ListCtrl subclass with auto-resize columns
# ---------------------------------------------------------------------------

class AutoListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    """wx.ListCtrl with auto-width for the last column."""

    def __init__(self, parent, style):
        """Initialise parent classes in the required order."""
        wx.ListCtrl.__init__(self, parent, style=style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)


# ---------------------------------------------------------------------------
# New Scan dialog
# ---------------------------------------------------------------------------

class NewScanDialog(wx.Dialog):
    """Modal dialog for creating a new ODS scan job."""

    def __init__(self, parent, available_hosts: list[dict] | None = None,
                 prefill: dict | None = None):
        """Build the dialog controls.

        available_hosts is a list of dicts with keys 'hostname', 'device_id', 'status'.
        When provided, the host-AID panel shows a searchable list instead of a freeform field.

        prefill is an optional dict with keys: 'use_groups' (bool), 'aids' (str),
        'groups' (str), 'description' (str), 'cpu_priority' (int), 'quarantine' (bool),
        'file_paths' (list[str]), 'scan_exclusions' (str).  When provided, the dialog
        opens pre-filled with the previous values (used after a failed scan submission).
        """
        super().__init__(parent, title="New On-Demand Scan", size=(580, 780),
                         style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self._available_hosts: list[dict] = available_hosts or []
        self._filtered_hosts: list[dict] = list(self._available_hosts)
        self._selected_aids: list[str] = []
        self._prefill: dict = prefill or {}

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Target type radio
        vbox.Add(wx.StaticText(panel, label="Target type:"), 0, wx.LEFT | wx.TOP, 10)
        self._radio_hosts = wx.RadioButton(panel, label="Host AIDs", style=wx.RB_GROUP)
        self._radio_groups = wx.RadioButton(panel, label="Host Group IDs")
        rb_box = wx.BoxSizer(wx.HORIZONTAL)
        rb_box.Add(self._radio_hosts, 0, wx.LEFT, 10)
        rb_box.Add(self._radio_groups, 0, wx.LEFT, 20)
        vbox.Add(rb_box, 0, wx.TOP, 4)

        # ---- Host selector panel (visible when "Host AIDs" is selected) ----
        self._host_panel = wx.Panel(panel)
        host_vbox = wx.BoxSizer(wx.VERTICAL)

        search_row = wx.BoxSizer(wx.HORIZONTAL)
        search_row.Add(
            wx.StaticText(self._host_panel, label="Search:"),
            0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 6,
        )
        self._search_entry = wx.TextCtrl(self._host_panel)
        self._search_entry.SetHint("Filter by hostname or AID…")
        search_row.Add(self._search_entry, 1)
        host_vbox.Add(search_row, 0, wx.EXPAND | wx.TOP, 4)

        self._host_list = wx.ListCtrl(
            self._host_panel,
            style=wx.LC_REPORT | wx.BORDER_SUNKEN,
        )
        self._host_list.InsertColumn(0, "Hostname", width=200)
        self._host_list.InsertColumn(1, "AID", width=260)
        self._host_list.InsertColumn(2, "Status", width=80)
        self._populate_host_list(self._filtered_hosts)
        host_vbox.Add(self._host_list, 1, wx.EXPAND | wx.TOP, 4)

        host_vbox.Add(
            wx.StaticText(
                self._host_panel,
                label="Selected AIDs (auto-filled from list, or type manually):",
            ),
            0, wx.TOP, 6,
        )
        self._aids_text = wx.TextCtrl(
            self._host_panel, style=wx.TE_MULTILINE, size=(-1, 70),
        )
        self._aids_text.SetHint("AID values, one per line or comma-separated")
        host_vbox.Add(self._aids_text, 0, wx.EXPAND | wx.TOP, 2)

        self._host_panel.SetSizer(host_vbox)
        vbox.Add(self._host_panel, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        # ---- Group ID panel (visible when "Host Group IDs" is selected) ----
        self._group_panel = wx.Panel(panel)
        group_vbox = wx.BoxSizer(wx.VERTICAL)
        group_vbox.Add(
            wx.StaticText(self._group_panel, label="Group IDs (one per line or comma-separated):"),
            0, wx.TOP, 4,
        )
        self._group_text = wx.TextCtrl(self._group_panel, style=wx.TE_MULTILINE, size=(-1, 140))
        group_vbox.Add(self._group_text, 1, wx.EXPAND | wx.TOP, 4)
        self._group_panel.SetSizer(group_vbox)
        self._group_panel.Show(False)
        vbox.Add(self._group_panel, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        # Description
        vbox.Add(wx.StaticText(panel, label="Description (optional):"), 0, wx.LEFT | wx.TOP, 10)
        self._desc_text = wx.TextCtrl(panel, size=(-1, -1))
        vbox.Add(self._desc_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        # ---- File paths (required by the ODS API) ----
        vbox.Add(
            wx.StaticText(panel, label="File paths to scan (at least one required):"),
            0, wx.LEFT | wx.TOP, 10,
        )

        # List showing current paths
        self._paths_listbox = wx.ListBox(panel, style=wx.LB_EXTENDED, size=(-1, 90))
        # Pre-populate with sensible cross-platform defaults
        for p in DEFAULT_SCAN_PATHS:
            self._paths_listbox.Append(p)
        vbox.Add(self._paths_listbox, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        # Add / Remove row
        path_btn_row = wx.BoxSizer(wx.HORIZONTAL)
        self._path_entry = wx.TextCtrl(panel)
        self._path_entry.SetHint("Enter path (e.g. C:\\ or /home/user)")
        path_btn_row.Add(self._path_entry, 1, wx.RIGHT, 6)
        add_path_btn = wx.Button(panel, label="Add")
        add_path_btn.Bind(wx.EVT_BUTTON, self._on_add_path)
        path_btn_row.Add(add_path_btn, 0, wx.RIGHT, 4)
        remove_path_btn = wx.Button(panel, label="Remove Selected")
        remove_path_btn.Bind(wx.EVT_BUTTON, self._on_remove_path)
        path_btn_row.Add(remove_path_btn, 0)
        vbox.Add(path_btn_row, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        # ---- Scan exclusions (optional glob patterns) ----
        vbox.Add(
            wx.StaticText(panel, label="Exclusions — glob patterns (optional, one per line):"),
            0, wx.LEFT | wx.TOP, 10,
        )
        self._exclusions_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(-1, 55))
        self._exclusions_text.SetHint(
            "e.g. C:\\Windows\\Temp\\* or /tmp/*"
        )
        vbox.Add(self._exclusions_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 4)

        # CPU priority
        vbox.Add(wx.StaticText(panel, label="CPU priority (1 = low, 4 = high):"), 0,
                 wx.LEFT | wx.TOP, 10)
        self._cpu_spin = wx.SpinCtrl(panel, min=1, max=4, initial=2)
        vbox.Add(self._cpu_spin, 0, wx.LEFT | wx.TOP, 10)

        # Quarantine checkbox
        self._quarantine_cb = wx.CheckBox(panel, label="Quarantine malicious files")
        self._quarantine_cb.SetValue(True)
        vbox.Add(self._quarantine_cb, 0, wx.LEFT | wx.TOP, 10)

        # Buttons
        btn_sizer = wx.StdDialogButtonSizer()
        ok_btn = wx.Button(panel, wx.ID_OK, label="Start Scan")
        ok_btn.SetDefault()
        btn_sizer.AddButton(ok_btn)
        btn_sizer.AddButton(wx.Button(panel, wx.ID_CANCEL))
        btn_sizer.Realize()
        vbox.Add(btn_sizer, 0, wx.ALL | wx.EXPAND, 10)

        panel.SetSizer(vbox)

        # Bind events (before prefill so Layout() calls are valid)
        self._radio_hosts.Bind(wx.EVT_RADIOBUTTON, self._on_radio_changed)
        self._radio_groups.Bind(wx.EVT_RADIOBUTTON, self._on_radio_changed)
        self._search_entry.Bind(wx.EVT_TEXT, self._on_search_changed)
        self._host_list.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_host_list_selected)
        self._host_list.Bind(wx.EVT_LIST_ITEM_DESELECTED, self._on_host_list_deselected)

        # Restore previous values when re-opening after a failed submission
        if self._prefill:
            self._apply_prefill()

        self.Centre()

    # ------------------------------------------------------------------
    # Host list helpers
    # ------------------------------------------------------------------

    def _populate_host_list(self, hosts: list[dict]) -> None:
        """Rebuild the host list control from *hosts*."""
        self._host_list.DeleteAllItems()
        for host in hosts:
            idx = self._host_list.InsertItem(
                self._host_list.GetItemCount(), host.get("hostname", "")
            )
            self._host_list.SetItem(idx, 1, host.get("device_id", ""))
            self._host_list.SetItem(idx, 2, host.get("status", ""))

    def _on_search_changed(self, _event) -> None:
        """Filter the host list as the user types in the search field."""
        query = self._search_entry.GetValue().strip().lower()
        if query:
            self._filtered_hosts = [
                h for h in self._available_hosts
                if query in h.get("hostname", "").lower()
                or query in h.get("device_id", "").lower()
            ]
        else:
            self._filtered_hosts = list(self._available_hosts)
        self._populate_host_list(self._filtered_hosts)

    def _on_host_list_selected(self, event) -> None:
        """Auto-populate AIDs text area; auto-select AID radio when a host row is selected."""
        idx = event.GetIndex()
        if 0 <= idx < len(self._filtered_hosts):
            aid = self._filtered_hosts[idx].get("device_id", "")
            if aid and aid not in self._selected_aids:
                self._selected_aids.append(aid)
                self._aids_text.SetValue("\n".join(self._selected_aids))
        # Always ensure the Host AIDs radio is active when the user interacts with the list
        if not self._radio_hosts.GetValue():
            self._radio_hosts.SetValue(True)
            self._host_panel.Show(True)
            self._group_panel.Show(False)
            self.Layout()

    def _on_host_list_deselected(self, event) -> None:
        """Remove AID from the text area when a host row is deselected."""
        idx = event.GetIndex()
        if 0 <= idx < len(self._filtered_hosts):
            aid = self._filtered_hosts[idx].get("device_id", "")
            if aid in self._selected_aids:
                self._selected_aids.remove(aid)
                self._aids_text.SetValue("\n".join(self._selected_aids))

    def _on_radio_changed(self, _event) -> None:
        """Toggle between the host selector panel and the group ID panel."""
        show_hosts = self._radio_hosts.GetValue()
        self._host_panel.Show(show_hosts)
        self._group_panel.Show(not show_hosts)
        self.Layout()

    def _apply_prefill(self) -> None:
        """Restore form values from a previous (failed) submission."""
        pf = self._prefill
        if pf.get("use_groups"):
            self._radio_groups.SetValue(True)
            self._host_panel.Show(False)
            self._group_panel.Show(True)
            self.Layout()
        if pf.get("aids"):
            self._aids_text.SetValue(pf["aids"])
        if pf.get("groups"):
            self._group_text.SetValue(pf["groups"])
        if pf.get("description"):
            self._desc_text.SetValue(pf["description"])
        if "cpu_priority" in pf:
            self._cpu_spin.SetValue(pf["cpu_priority"])
        if "quarantine" in pf:
            self._quarantine_cb.SetValue(pf["quarantine"])
        if pf.get("file_paths"):
            self._paths_listbox.Clear()
            for p in pf["file_paths"]:
                self._paths_listbox.Append(p)
        if pf.get("scan_exclusions"):
            self._exclusions_text.SetValue(pf["scan_exclusions"])

    # ------------------------------------------------------------------
    # Accessors called by the parent frame after OK
    # ------------------------------------------------------------------

    def get_hosts(self) -> list[str]:
        """Return the list of host AIDs to scan, or empty list if groups chosen."""
        if not self._radio_hosts.GetValue():
            return []
        # Reads from the text area (supports auto-filled selections and manual entry)
        return _parse_ids(self._aids_text.GetValue())

    def get_host_groups(self) -> list[str]:
        """Return the list of host group IDs entered, or empty list if hosts chosen."""
        if not self._radio_groups.GetValue():
            return []
        return _parse_ids(self._group_text.GetValue())

    def get_description(self) -> str:
        """Return the description string from the text field."""
        return self._desc_text.GetValue().strip()

    def get_cpu_priority(self) -> int:
        """Return the selected CPU priority integer."""
        return self._cpu_spin.GetValue()

    def get_quarantine(self) -> bool:
        """Return True if the quarantine checkbox is checked."""
        return self._quarantine_cb.GetValue()

    def get_file_paths(self) -> list[str]:
        """Return the list of file paths from the paths list box."""
        return [
            self._paths_listbox.GetString(i)
            for i in range(self._paths_listbox.GetCount())
        ]

    def get_scan_exclusions(self) -> list[str]:
        """Return the list of exclusion glob patterns from the exclusions text area."""
        return _parse_ids(self._exclusions_text.GetValue())

    # ------------------------------------------------------------------
    # File path list helpers
    # ------------------------------------------------------------------

    def _on_add_path(self, _event) -> None:
        """Add the path from the entry field to the list box."""
        path = self._path_entry.GetValue().strip()
        if not path:
            return
        # Avoid duplicate entries
        existing = [self._paths_listbox.GetString(i)
                    for i in range(self._paths_listbox.GetCount())]
        if path not in existing:
            self._paths_listbox.Append(path)
        self._path_entry.SetValue("")

    def _on_remove_path(self, _event) -> None:
        """Remove all selected paths from the list box (supports multi-select)."""
        selections = self._paths_listbox.GetSelections()
        for idx in sorted(selections, reverse=True):
            self._paths_listbox.Delete(idx)


def _parse_ids(raw: str) -> list[str]:
    """Split a newline- or comma-separated string of IDs into a clean list."""
    parts = []
    for token in raw.replace(",", "\n").splitlines():
        stripped = token.strip()
        if stripped:
            parts.append(stripped)
    return parts


# ---------------------------------------------------------------------------
# Main application frame
# ---------------------------------------------------------------------------

class ODSManagerFrame(wx.Frame):
    """Main window for the ODS Manager application."""

    def __init__(self, client: ODSClient):
        """Build all widgets, bind events, and perform the first data load."""
        super().__init__(None, title=APP_TITLE, size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        self._client = client
        self._scans: list[ScanRecord] = []
        self._lock = threading.Lock()
        self._loading = False

        self._build_ui()
        self._bind_events()

        # Populate the scan list in the background
        self._async_refresh()

        # Status-polling timer — fires every POLL_INTERVAL_MS
        self._poll_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._on_poll_timer, self._poll_timer)
        self._poll_timer.Start(POLL_INTERVAL_MS)

    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------

    def _build_ui(self):
        """Construct all panels, sizers, and controls."""
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # ---- Toolbar row ----
        toolbar_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self._new_btn = wx.Button(panel, label="New Scan")
        self._refresh_btn = wx.Button(panel, label="Refresh")
        self._cancel_btn = wx.Button(panel, label="Cancel Selected")
        self._delete_btn = wx.Button(panel, label="Delete Selected")
        self._delete_btn.SetToolTip(
            "The ODS API does not support deleting on-demand scan records.\n"
            "Clicking this will explain what options are available."
        )

        for btn in (self._new_btn, self._refresh_btn, self._cancel_btn, self._delete_btn):
            toolbar_sizer.Add(btn, 0, wx.RIGHT, 8)

        toolbar_sizer.Add(wx.StaticLine(panel, style=wx.LI_VERTICAL), 0,
                          wx.EXPAND | wx.LEFT | wx.RIGHT, 6)

        self._status_label = wx.StaticText(panel, label="")
        self._ts_label = wx.StaticText(panel, label="")
        toolbar_sizer.Add(self._status_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 12)
        toolbar_sizer.Add(self._ts_label, 0, wx.ALIGN_CENTER_VERTICAL)

        main_sizer.Add(toolbar_sizer, 0, wx.ALL | wx.EXPAND, 8)
        main_sizer.Add(wx.StaticLine(panel), 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 4)

        # ---- Main scan list ----
        self._scan_list = AutoListCtrl(
            panel,
            style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.BORDER_SUNKEN,
        )
        for col_idx, (label, width) in enumerate(SCAN_COLUMNS):
            self._scan_list.InsertColumn(col_idx, label, width=width)
        main_sizer.Add(self._scan_list, 2, wx.EXPAND | wx.ALL, 6)

        # ---- Detail split panel ----
        splitter = wx.SplitterWindow(panel, style=wx.SP_LIVE_UPDATE | wx.SP_3D)
        splitter.SetMinimumPaneSize(200)

        # Left pane: per-host table
        host_panel = wx.Panel(splitter)
        host_sizer = wx.BoxSizer(wx.VERTICAL)
        host_sizer.Add(wx.StaticText(host_panel, label="Per-Host Progress"), 0,
                       wx.LEFT | wx.TOP, 4)
        self._host_list = AutoListCtrl(
            host_panel,
            style=wx.LC_REPORT | wx.BORDER_SUNKEN,
        )
        for col_idx, (label, width) in enumerate(HOST_COLUMNS):
            self._host_list.InsertColumn(col_idx, label, width=width)
        host_sizer.Add(self._host_list, 1, wx.EXPAND | wx.ALL, 4)
        host_panel.SetSizer(host_sizer)

        # Right pane: findings summary
        findings_panel = wx.Panel(splitter)
        findings_sizer = wx.BoxSizer(wx.VERTICAL)
        findings_sizer.Add(wx.StaticText(findings_panel, label="Findings Summary"), 0,
                           wx.LEFT | wx.TOP, 4)
        self._findings_text = wx.TextCtrl(
            findings_panel,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_SUNKEN,
        )
        findings_sizer.Add(self._findings_text, 1, wx.EXPAND | wx.ALL, 4)
        findings_panel.SetSizer(findings_sizer)

        splitter.SplitVertically(host_panel, findings_panel, sashPosition=640)
        main_sizer.Add(splitter, 1, wx.EXPAND | wx.ALL, 6)

        panel.SetSizer(main_sizer)
        self.Centre()

    def _bind_events(self):
        """Attach event handlers to controls."""
        self._new_btn.Bind(wx.EVT_BUTTON, self._on_new_scan)
        self._refresh_btn.Bind(wx.EVT_BUTTON, self._on_refresh)
        self._cancel_btn.Bind(wx.EVT_BUTTON, self._on_cancel_selected)
        self._delete_btn.Bind(wx.EVT_BUTTON, self._on_delete_selected)
        self._scan_list.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_scan_selected)

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

    def _async_refresh(self):
        """Kick off a background thread to reload the scan list."""
        if self._loading:
            return
        self._loading = True
        self._set_status("Loading…", wx.Colour(180, 180, 180))
        t = threading.Thread(target=self._worker_refresh, daemon=True)
        t.start()

    def _worker_refresh(self):
        """Background worker: fetch scan IDs then full scan records."""
        try:
            scan_ids = self._client.query_scans(limit=200)
            if scan_ids:
                scans = self._client.get_scans(scan_ids)
            else:
                scans = []
            ts = datetime.now().strftime("%H:%M:%S")
            with self._lock:
                self._scans = scans
            # All wx UI updates must run on the main thread
            wx.CallAfter(self._populate_scan_list, scans, ts)
        except Exception as exc:  # pylint: disable=broad-except
            wx.CallAfter(self._set_status, f"Error: {exc}", wx.Colour(220, 50, 50))
        finally:
            self._loading = False

    def _populate_scan_list(self, scans: list[ScanRecord], ts: str):
        """Rebuild the scan list control from *scans* (runs on main thread)."""
        # Remember selected scan ID so we can restore selection after repopulation
        selected_id = self._get_selected_scan_id()

        self._scan_list.DeleteAllItems()
        for scan in scans:
            row = scan.list_row()
            idx = self._scan_list.InsertItem(self._scan_list.GetItemCount(), row[0])
            for col_idx, value in enumerate(row[1:], start=1):
                self._scan_list.SetItem(idx, col_idx, value)
            # Tint the status cell
            colour = STATUS_COLOURS.get(scan.status.lower(), wx.Colour(200, 200, 200))
            self._scan_list.SetItemTextColour(idx, colour)

        # Restore previous selection
        if selected_id:
            self._reselect_scan(selected_id)

        count = len(scans)
        active = sum(1 for s in scans if s.is_active)
        self._set_status(
            f"Connected — {count} scan(s), {active} active",
            wx.Colour(50, 200, 80),
        )
        self._ts_label.SetLabel(f"  Last refreshed: {ts}")

    def _get_selected_scan_id(self) -> Optional[str]:
        """Return the scan_id of the currently selected row, or None."""
        idx = self._scan_list.GetFirstSelected()
        if idx == -1:
            return None
        return self._scan_list.GetItemText(idx, 0)

    def _reselect_scan(self, scan_id: str):
        """Restore selection to the row whose first column starts with *scan_id*."""
        for i in range(self._scan_list.GetItemCount()):
            cell = self._scan_list.GetItemText(i, 0)
            # Truncated IDs end with '…'; match on prefix
            if scan_id.startswith(cell.rstrip("…")):
                self._scan_list.Select(i)
                self._scan_list.EnsureVisible(i)
                return

    # ------------------------------------------------------------------
    # Detail panel
    # ------------------------------------------------------------------

    def _load_detail(self, scan: ScanRecord):
        """Populate the per-host table and findings summary for *scan*."""
        self._host_list.DeleteAllItems()
        self._findings_text.SetValue("Loading host metadata…")

        def _worker():
            hosts = self._client.get_host_metadata(scan.scan_id)
            wx.CallAfter(self._populate_detail, scan, hosts)

        threading.Thread(target=_worker, daemon=True).start()

    def _populate_detail(self, scan: ScanRecord, hosts: list[HostRecord]):
        """Fill the host table and findings text area (main thread)."""
        self._host_list.DeleteAllItems()
        for host in hosts:
            row = host.list_row()
            idx = self._host_list.InsertItem(self._host_list.GetItemCount(), row[0])
            for col_idx, value in enumerate(row[1:], start=1):
                self._host_list.SetItem(idx, col_idx, value)
            colour = STATUS_COLOURS.get(host.status.lower(), wx.Colour(200, 200, 200))
            self._host_list.SetItemTextColour(idx, colour)

        # Build findings summary text
        lines = [
            f"Scan ID:          {scan.scan_id}",
            f"Status:           {scan.status}",
            f"Description:      {scan.description or '(none)'}",
            f"Initiated from:   {scan.initiated_from or scan.created_by}",
            f"Started:          {scan.scan_started_on or scan.created_on}",
            f"Completed:        {scan.scan_completed_on or '—'}",
            "",
            "File Counts",
            f"  Scanned:        {scan.scanned}",
            f"  Malicious:      {scan.malicious}",
            f"  Quarantined:    {scan.quarantined}",
            "",
            "Host Summary",
            f"  Targeted:       {scan.targeted_host_count}",
            f"  Affected:       {scan.affected_hosts_count}",
            f"  Missing:        {scan.missing_host_count}",
            f"  Not Started:    {scan.not_started_host_count}",
            f"  Loaded:         {len(hosts)}",
        ]

        # Surface failure reasons when scan failed and hosts did not start
        if scan.status == "failed" and scan.missing_host_count > 0:
            lines.append("")
            lines.append("FAILURE REASON")
            lines.append(
                f"  {scan.missing_host_count} of {scan.targeted_host_count} host(s) "
                "were unreachable or unresponsive."
            )
            reasons = {h.scan_control_reason for h in hosts if h.scan_control_reason}
            if reasons:
                lines.append(f"  Reasons: {', '.join(sorted(reasons))}")
            else:
                lines.append("  Check host online status and sensor health.")

        if hosts:
            lines.append("")
            lines.append("Host Breakdown")
            for host in hosts:
                reason = f" [{host.scan_control_reason}]" if host.scan_control_reason else ""
                lines.append(
                    f"  {host.host_id[:20]:<20}  {host.status:<12}{reason}"
                    f"  scanned={host.scanned}  malicious={host.malicious}"
                )
        self._findings_text.SetValue("\n".join(lines))

    # ------------------------------------------------------------------
    # Status helpers
    # ------------------------------------------------------------------

    def _set_status(self, text: str, colour: wx.Colour):
        """Update the status label text and colour."""
        self._status_label.SetLabel(text)
        self._status_label.SetForegroundColour(colour)
        self._status_label.GetParent().Layout()

    # ------------------------------------------------------------------
    # Event handlers
    # ------------------------------------------------------------------

    def _on_refresh(self, _event):
        """Handle Refresh button click."""
        self._async_refresh()

    def _on_poll_timer(self, _event):
        """Handle wx.Timer tick — refresh in-progress scans every POLL_INTERVAL_MS."""
        with self._lock:
            has_active = any(s.is_active for s in self._scans)
        if has_active:
            self._async_refresh()

    def _on_scan_selected(self, event):
        """Handle a row being selected in the scan list."""
        idx = event.GetIndex()
        with self._lock:
            if idx < len(self._scans):
                scan = self._scans[idx]
            else:
                return
        self._load_detail(scan)

    def _on_new_scan(self, _event):
        """Fetch available hosts in background, then open the New Scan dialog."""
        self._set_status("Loading hosts…", wx.Colour(180, 180, 180))
        self._new_btn.Enable(False)
        threading.Thread(target=self._load_hosts_for_dialog, daemon=True).start()

    def _load_hosts_for_dialog(self):
        """Background worker: query available hosts, then open the dialog on the main thread."""
        hosts = self._client.query_available_hosts()
        wx.CallAfter(self._open_new_scan_dialog, hosts)

    def _open_new_scan_dialog(self, available_hosts: list[dict]):
        """Open the New Scan dialog with the pre-fetched host list (main thread)."""
        self._new_btn.Enable(True)
        self._set_status("", wx.Colour(180, 180, 180))
        self._show_new_scan_dialog(available_hosts, prefill=None)

    def _show_new_scan_dialog(self, available_hosts: list[dict], prefill: dict | None):
        """Internal: display the New Scan dialog; re-opens with prefill if scan fails."""
        dlg = NewScanDialog(self, available_hosts=available_hosts, prefill=prefill)
        if dlg.ShowModal() != wx.ID_OK:
            dlg.Destroy()
            return

        hosts = dlg.get_hosts()
        groups = dlg.get_host_groups()
        description = dlg.get_description()
        cpu_priority = dlg.get_cpu_priority()
        quarantine = dlg.get_quarantine()
        file_paths = dlg.get_file_paths()
        scan_exclusions = dlg.get_scan_exclusions()
        dlg.Destroy()

        if not hosts and not groups:
            wx.MessageDialog(
                self,
                "Please enter at least one host AID or host group ID.",
                "Validation Error",
                wx.OK | wx.ICON_WARNING,
            ).ShowModal()
            # Re-open with same values so user can correct
            self._show_new_scan_dialog(available_hosts, prefill={
                "use_groups": bool(groups),
                "aids": "\n".join(hosts),
                "groups": "\n".join(groups),
                "description": description,
                "cpu_priority": cpu_priority,
                "quarantine": quarantine,
                "file_paths": file_paths,
                "scan_exclusions": "\n".join(scan_exclusions),
            })
            return

        if not file_paths:
            wx.MessageDialog(
                self,
                "At least one file path is required.\n"
                "Add a path (e.g. C:\\ or /) before starting the scan.",
                "Validation Error",
                wx.OK | wx.ICON_WARNING,
            ).ShowModal()
            self._show_new_scan_dialog(available_hosts, prefill={
                "use_groups": bool(groups),
                "aids": "\n".join(hosts),
                "groups": "\n".join(groups),
                "description": description,
                "cpu_priority": cpu_priority,
                "quarantine": quarantine,
                "file_paths": file_paths,
                "scan_exclusions": "\n".join(scan_exclusions),
            })
            return

        ok, msg = self._client.create_scan(
            ScanRequest(
                hosts=hosts,
                host_groups=groups,
                description=description,
                cpu_priority=cpu_priority,
                quarantine=quarantine,
                file_paths=file_paths,
                scan_exclusions=scan_exclusions,
            )
        )
        icon = wx.ICON_INFORMATION if ok else wx.ICON_ERROR
        wx.MessageDialog(self, msg, "New Scan", wx.OK | icon).ShowModal()
        if ok:
            self._async_refresh()
        else:
            # Re-open dialog with all previous values preserved so user can retry
            self._show_new_scan_dialog(available_hosts, prefill={
                "use_groups": bool(groups),
                "aids": "\n".join(hosts),
                "groups": "\n".join(groups),
                "description": description,
                "cpu_priority": cpu_priority,
                "quarantine": quarantine,
                "file_paths": file_paths,
                "scan_exclusions": "\n".join(scan_exclusions),
            })

    def _on_cancel_selected(self, _event):
        """Cancel the selected scan if it is active."""
        scan_id = self._get_selected_scan_id()
        if not scan_id:
            wx.MessageDialog(self, "No scan selected.", "Cancel Scan",
                             wx.OK | wx.ICON_WARNING).ShowModal()
            return

        # Resolve truncated ID against the full list
        full_id = self._resolve_full_id(scan_id)
        if not full_id:
            return

        dlg = wx.MessageDialog(
            self,
            f"Cancel scan:\n{full_id}\n\nThis will abort the running scan.",
            "Confirm Cancel",
            wx.YES_NO | wx.ICON_WARNING,
        )
        if dlg.ShowModal() != wx.ID_YES:
            return

        ok, msg = self._client.cancel_scans([full_id])
        icon = wx.ICON_INFORMATION if ok else wx.ICON_ERROR
        wx.MessageDialog(self, msg, "Cancel Scan", wx.OK | icon).ShowModal()
        if ok:
            self._async_refresh()

    def _on_delete_selected(self, _event):
        """Explain the ODS API delete limitation to the user.

        The Falcon ODS API provides no endpoint to delete on-demand scan records.
        The only delete endpoint (delete_scheduled_scans) is for *scheduled* scans
        only — it returns HTTP 200 on ad-hoc scan IDs but does not remove the record.
        Confirmed via direct API testing: completed, failed, and cancelled on-demand
        scans remain permanently visible in query_scans regardless of what is called.

        The closest available action is cancel_scans, which changes a scan's status
        to 'canceled' and is already available via the 'Cancel Selected' button.
        """
        scan_id = self._get_selected_scan_id()
        full_id = self._resolve_full_id(scan_id) if scan_id else None

        # Determine the current scan status so we can offer the right alternative
        status = ""
        if full_id:
            with self._lock:
                for s in self._scans:
                    if s.scan_id == full_id:
                        status = s.status
                        break

        if status in ACTIVE_STATUSES:
            # Active scan: offer to cancel it
            reply = wx.MessageDialog(
                self,
                "On-demand scan records cannot be deleted — the Falcon ODS API does not\n"
                "provide a delete endpoint for on-demand scans.\n\n"
                f"This scan is currently '{status}'.\n"
                "Would you like to cancel it instead?",
                "Delete Not Supported — Cancel Instead?",
                wx.YES_NO | wx.ICON_INFORMATION,
            )
            if reply.ShowModal() == wx.ID_YES:
                self._on_cancel_selected(_event)
        else:
            # Completed/failed/cancelled scan: nothing can be done
            wx.MessageDialog(
                self,
                "On-demand scan records cannot be deleted.",
                "Delete Not Supported",
                wx.OK | wx.ICON_INFORMATION,
            ).ShowModal()

    def _resolve_full_id(self, truncated: str) -> Optional[str]:
        """Find the full scan_id in self._scans matching the (possibly truncated) display value."""
        prefix = truncated.rstrip("…")
        with self._lock:
            for scan in self._scans:
                if scan.scan_id.startswith(prefix) or scan.scan_id == truncated:
                    return scan.scan_id
        return None


# ---------------------------------------------------------------------------
# Application entry point
# ---------------------------------------------------------------------------

def main():
    """Parse CLI credentials, authenticate against the Falcon API, and launch the ODS Manager UI."""
    parser = argparse.ArgumentParser(
        description=__doc__,
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

    app = wx.App(False)

    client = ODSClient()
    ok = client.connect(client_id=args.client_id, client_secret=args.client_secret)
    if not ok:
        # Show the auth error before opening the main window
        wx.MessageDialog(
            None,
            f"Authentication failed:\n\n{client.error}\n\n"
            "Provide credentials via environment variables or -k / -s arguments:\n"
            "  FALCON_CLIENT_ID=xxx FALCON_CLIENT_SECRET=yyy pipenv run python3 ods_manager.py\n"
            "  pipenv run python3 ods_manager.py -k CLIENT_ID -s CLIENT_SECRET",
            "ODS Manager — Auth Error",
            wx.OK | wx.ICON_ERROR,
        ).ShowModal()
        sys.exit(1)

    frame = ODSManagerFrame(client)
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
