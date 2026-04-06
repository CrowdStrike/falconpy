r"""Device Control Policy Manager — Desktop GUI.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |             FalconPy
`-------'                         `-------'

 ___      ___ __ __  ____    __    ___         __   ___   ____   ______  ____    ___   _
|   \    /  _]  T  |l    j  /  ]  /  _]       /  ] /   \ |    \ |      T|    \  /   \ | T
|    \  /  [_|  |  | |  T  /  /  /  [_       /  / Y     Y|  _  Y|      ||  D  )Y     Y| |
|  D  YY    _]  |  | |  | /  /  Y    _]     /  /  |  O  ||  |  |l_j  l_j|    / |  O  || l___
|     ||   [_l  :  ! |  |/   \_ |   [_     /   \_ |     ||  |  |  |  |  |    \ |     ||     T
|     ||     T\   /  j  l\     ||     T    \     |l     !|  |  |  |  |  |  .  Yl     !|     |
l_____jl_____j \_/  |____j\____jl_____j     \____j \___/ l__j__j  l__j  l__j\_j \___/ l_____j

 ____    ___   _      ____    __  __ __      ___ ___   ____  ____    ____   ____    ___  ____
|    \  /   \ | T    l    j  /  ]|  T  T    |   T   T /    T|    \  /    T /    T  /  _]|    \
|  o  )Y     Y| |     |  T  /  / |  |  |    | _   _ |Y  o  ||  _  YY  o  |Y   __j /  [_ |  D  )
|   _/ |  O  || l___  |  | /  /  |  ~  |    |  \_/  ||     ||  |  ||     ||  T  |Y    _]|    /
|  |   |     ||     T |  |/   \_ l___, |    |   |   ||  _  ||  |  ||  _  ||  l_ ||   [_ |    \
|  |   l     !|     | j  l\     ||     !    |   |   ||  |  ||  |  ||  |  ||     ||     T|  .  Y
l__j    \___/ l_____j|____j\____jl____/     l___j___jl__j__jl__j__jl__j__jl___,_jl_____jl__j\_j

                          Device Control Policy Manager — Desktop GUI (v1)
                          Uses: DeviceControlPolicies, HostGroup
                          Scope: device-control-policies:read, device-control-policies:write,
                                 host-group:read

A PySide6 desktop application for managing CrowdStrike Falcon USB Device Control Policies.
Browse, create, edit, enable/disable, and delete device control policies. Assign host groups
to policies via a searchable modal dialog.

Prerequisites
-------------
  pip install crowdstrike-falconpy PySide6
  (or: pipenv install crowdstrike-falconpy PySide6)

Required API scopes
-------------------
  device-control-policies:read   — list and view policies
  device-control-policies:write  — create, update, delete, and perform actions
  host-group:read                — list host groups for assignment dialog

Credentials
-----------
  Resolved in this order (first non-empty value wins):
    1. -k / -s / -b command-line flags
    2. FALCON_CLIENT_ID / FALCON_CLIENT_SECRET / FALCON_BASE_URL environment variables

Usage
-----
    # Via CLI flags:
    pipenv run python3 device_control_policy_manager.py -k CLIENT_ID -s CLIENT_SECRET

    # Via environment variables:
    pipenv run python3 device_control_policy_manager.py

Architecture overview
---------------------
  DeviceControlWindow (QMainWindow)
  ├── Policy list panel (QWidget, left splitter pane)
  │   ├── Toolbar: New, Clone, Delete, Refresh buttons
  │   └── Policy table (QTableView) — ID, Name, Platform, Enabled, Groups
  └── Detail panel (QWidget, right splitter pane)
      ├── General tab — name, description, platform fields
      ├── Device Classes tab — USB class action dropdowns
      └── Exceptions tab — vendor/product ID exception table

  Background workers (QThread subclasses):
    LoadPoliciesWorker   — calls query_combined_policies (paginated)
    SavePolicyWorker     — calls create_policies or update_policies
    DeletePolicyWorker   — calls delete_policies
    ActionWorker         — calls performDeviceControlPoliciesAction (enable/disable/assign group)
    LoadGroupsWorker     — calls HostGroup.query_combined_host_groups
"""
# pylint: disable=too-many-lines
# pylint: disable=too-many-arguments,too-many-positional-arguments
# pylint: disable=too-many-locals,too-few-public-methods
# pylint: disable=too-many-instance-attributes,too-many-statements
# pylint: disable=attribute-defined-outside-init
import argparse
import os
import sys

# pylint: disable=import-error
from PySide6.QtCore import (
    Qt, QThread, Signal, QSortFilterProxyModel,
)
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSplitter,
    QStatusBar,
    QTabWidget,
    QTableView,
    QTableWidget,
    QTableWidgetItem,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from falconpy import DeviceControlPolicies, HostGroup
# pylint: enable=import-error

# ── USB device class identifiers expected by the API ─────────────────────────
DEVICE_CLASSES = [
    "ANY",
    "AUDIO_VIDEO",
    "IMAGING",
    "MASS_STORAGE",
    "MOBILE",
    "PRINTER",
    "WIRELESS",
]

# Actions the API accepts for ALL device classes (FULL_ACCESS / BLOCK_ALL are
# universally valid; MASS_STORAGE also allows BLOCK_EXECUTE / BLOCK_WRITE_EXECUTE
# but those are not exposed here for simplicity).
CLASS_ACTIONS = ["FULL_ACCESS", "BLOCK_ALL"]


# ── Background workers ────────────────────────────────────────────────────────

class LoadPoliciesWorker(QThread):
    """Fetch all device control policies via paginated query_combined_policies."""

    finished = Signal(list, str)   # (policies, error_message)

    def __init__(self, sdk, parent=None):
        """Store the authenticated SDK instance."""
        super().__init__(parent)
        self._sdk = sdk

    def run(self):
        """Page through query_combined_policies and collect all resources."""
        policies = []
        offset = 0
        limit = 100
        try:
            while True:
                response = self._sdk.query_combined_policies(
                    offset=offset,
                    limit=limit,
                    sort="name.asc",
                )
                status = response.get("status_code", 0)
                if status != 200:
                    errors = response.get("body", {}).get("errors", [])
                    msg = errors[0].get("message", "API error") if errors else f"HTTP {status}"
                    self.finished.emit([], msg)
                    return

                resources = response.get("body", {}).get("resources", [])
                policies.extend(resources)

                pagination = response.get("body", {}).get("meta", {}).get("pagination", {})
                total = pagination.get("total", len(policies))
                offset += limit
                if offset >= total:
                    break

            self.finished.emit(policies, "")
        except Exception as exc:  # pylint: disable=broad-except
            self.finished.emit([], str(exc))


class SavePolicyWorker(QThread):
    """Create or update a single device control policy."""

    finished = Signal(dict, str)   # (saved_resource, error_message)

    def __init__(self, sdk, policy_id, name, description, platform,
                 settings=None, parent=None):
        """Store policy fields; policy_id=None means create, otherwise update."""
        super().__init__(parent)
        self._sdk = sdk
        self._policy_id = policy_id
        self._name = name
        self._description = description
        self._platform = platform
        self._settings = settings  # dict with "classes" list, or None for create

    def run(self):
        """Call create_policies or update_policies depending on whether an ID exists."""
        try:
            if self._policy_id is None:
                # Create new policy with minimal required fields
                response = self._sdk.create_policies(
                    name=self._name,
                    description=self._description,
                    platform_name=self._platform,
                )
            else:
                # Update existing policy name, description, and device class settings
                kwargs = {
                    "id": self._policy_id,
                    "name": self._name,
                    "description": self._description,
                }
                if self._settings is not None:
                    kwargs["settings"] = self._settings
                response = self._sdk.update_policies(**kwargs)

            status = response.get("status_code", 0)
            if status not in (200, 201):
                errors = response.get("body", {}).get("errors", [])
                msg = errors[0].get("message", "API error") if errors else f"HTTP {status}"
                self.finished.emit({}, msg)
                return

            resources = response.get("body", {}).get("resources", [])
            saved = resources[0] if resources else {}
            self.finished.emit(saved, "")
        except Exception as exc:  # pylint: disable=broad-except
            self.finished.emit({}, str(exc))


class DeletePolicyWorker(QThread):
    """Delete one or more device control policies by ID."""

    finished = Signal(bool, str)   # (success, error_message)

    def __init__(self, sdk, policy_ids, parent=None):
        """Store a list of policy IDs to delete."""
        super().__init__(parent)
        self._sdk = sdk
        self._policy_ids = policy_ids

    def run(self):
        """Call delete_policies with the collected IDs."""
        try:
            response = self._sdk.delete_policies(ids=self._policy_ids)
            status = response.get("status_code", 0)
            if status != 200:
                errors = response.get("body", {}).get("errors", [])
                msg = errors[0].get("message", "API error") if errors else f"HTTP {status}"
                self.finished.emit(False, msg)
                return
            self.finished.emit(True, "")
        except Exception as exc:  # pylint: disable=broad-except
            self.finished.emit(False, str(exc))


class ActionWorker(QThread):
    """Perform an action (enable / disable / add-host-group) on a policy."""

    finished = Signal(bool, str)   # (success, error_message)

    def __init__(self, sdk, policy_id, action_name, group_id=None, parent=None):
        """Store action parameters; group_id is required for add-host-group."""
        super().__init__(parent)
        self._sdk = sdk
        self._policy_id = policy_id
        self._action_name = action_name
        self._group_id = group_id

    def run(self):
        """Call performDeviceControlPoliciesAction with the requested action."""
        try:
            kwargs = {
                "action_name": self._action_name,
                "ids": [self._policy_id],
            }
            if self._group_id:
                kwargs["action_parameters"] = [
                    {"name": "group_id", "value": self._group_id}
                ]

            response = self._sdk.performDeviceControlPoliciesAction(**kwargs)
            status = response.get("status_code", 0)
            if status != 200:
                errors = response.get("body", {}).get("errors", [])
                msg = errors[0].get("message", "API error") if errors else f"HTTP {status}"
                self.finished.emit(False, msg)
                return
            self.finished.emit(True, "")
        except Exception as exc:  # pylint: disable=broad-except
            self.finished.emit(False, str(exc))


class LoadGroupsWorker(QThread):
    """Fetch all host groups for the assignment dialog."""

    finished = Signal(list, str)   # (groups, error_message)

    def __init__(self, group_sdk, parent=None):
        """Store the authenticated HostGroup SDK instance."""
        super().__init__(parent)
        self._sdk = group_sdk

    def run(self):
        """Page through query_combined_host_groups and collect all resources."""
        groups = []
        offset = 0
        limit = 100
        try:
            while True:
                response = self._sdk.query_combined_host_groups(
                    offset=offset,
                    limit=limit,
                    sort="name.asc",
                )
                status = response.get("status_code", 0)
                if status != 200:
                    errors = response.get("body", {}).get("errors", [])
                    msg = errors[0].get("message", "API error") if errors else f"HTTP {status}"
                    self.finished.emit([], msg)
                    return

                resources = response.get("body", {}).get("resources", [])
                groups.extend(resources)

                pagination = response.get("body", {}).get("meta", {}).get("pagination", {})
                total = pagination.get("total", len(groups))
                offset += limit
                if offset >= total:
                    break

            self.finished.emit(groups, "")
        except Exception as exc:  # pylint: disable=broad-except
            self.finished.emit([], str(exc))


# ── Host Group assignment dialog ──────────────────────────────────────────────

class HostGroupDialog(QDialog):
    """Modal dialog for selecting a host group to assign to a policy."""

    def __init__(self, group_sdk, policy_name, parent=None):
        """Build the dialog; group_sdk is an authenticated HostGroup SDK instance."""
        super().__init__(parent)
        self.setWindowTitle(f"Assign Host Group — {policy_name}")
        self.setMinimumWidth(500)
        self.setMinimumHeight(400)

        self._group_sdk = group_sdk
        self._selected_group_id = None
        self._selected_group_name = None

        # ── Layout ──────────────────────────────────────────────────────────
        layout = QVBoxLayout(self)

        search_row = QHBoxLayout()
        search_row.addWidget(QLabel("Filter:"))
        self._search_field = QLineEdit()
        self._search_field.setPlaceholderText("Type to filter groups…")
        self._search_field.textChanged.connect(self._apply_filter)
        search_row.addWidget(self._search_field)
        layout.addLayout(search_row)

        # Groups table
        self._model = QStandardItemModel(0, 3, self)
        self._model.setHorizontalHeaderLabels(["Name", "Type", "Description"])

        self._proxy = QSortFilterProxyModel(self)
        self._proxy.setSourceModel(self._model)
        self._proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self._proxy.setFilterKeyColumn(-1)  # search all columns

        self._table = QTableView()
        self._table.setModel(self._proxy)
        self._table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self._table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self._table.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self._table.selectionModel().selectionChanged.connect(self._on_selection_changed)
        layout.addWidget(self._table)

        # Status label
        self._status_label = QLabel("Loading groups…")
        layout.addWidget(self._status_label)

        # Dialog buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self._ok_button = buttons.button(QDialogButtonBox.StandardButton.Ok)
        self._ok_button.setEnabled(False)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        # Load groups asynchronously
        self._worker = LoadGroupsWorker(self._group_sdk, parent=self)
        self._worker.finished.connect(self._on_groups_loaded)
        self._worker.start()

    def _on_groups_loaded(self, groups, error):
        """Populate table once the worker delivers results."""
        if error:
            self._status_label.setText(f"Error: {error}")
            return

        self._model.setRowCount(0)
        for group in groups:
            row = [
                QStandardItem(group.get("name", "")),
                QStandardItem(group.get("group_type", "")),
                QStandardItem(group.get("description", "")),
            ]
            # Stash the group ID in the first column's UserRole
            row[0].setData(group.get("id", ""), Qt.ItemDataRole.UserRole)
            for item in row:
                item.setEditable(False)
            self._model.appendRow(row)

        count = len(groups)
        self._status_label.setText(f"{count} group{'s' if count != 1 else ''} available.")

    def _apply_filter(self, text):
        """Forward text filter to the proxy model."""
        self._proxy.setFilterFixedString(text)

    def _on_selection_changed(self):
        """Enable OK button only when a row is selected."""
        indexes = self._table.selectionModel().selectedRows()
        self._ok_button.setEnabled(bool(indexes))

    @property
    def selected_group_id(self):
        """Return the ID of the group the user selected, or None."""
        indexes = self._table.selectionModel().selectedRows()
        if not indexes:
            return None
        source_index = self._proxy.mapToSource(indexes[0])
        item = self._model.item(source_index.row(), 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    @property
    def selected_group_name(self):
        """Return the display name of the selected group, or None."""
        indexes = self._table.selectionModel().selectedRows()
        if not indexes:
            return None
        source_index = self._proxy.mapToSource(indexes[0])
        item = self._model.item(source_index.row(), 0)
        return item.text() if item else None


# ── Add / edit exception dialog ───────────────────────────────────────────────

class ExceptionDialog(QDialog):
    """Dialog for adding a new USB device exception to a policy class."""

    def __init__(self, class_ids, parent=None):
        """Build form fields.  class_ids is the list of valid device class IDs."""
        super().__init__(parent)
        self.setWindowTitle("Add Exception")
        self.setMinimumWidth(440)

        layout = QVBoxLayout(self)

        # ── Class ────────────────────────────────────────────────────────────
        layout.addWidget(QLabel("Device Class *"))
        self._class_combo = QComboBox()
        self._class_combo.addItems(class_ids)
        layout.addWidget(self._class_combo)

        # ── Vendor ───────────────────────────────────────────────────────────
        layout.addWidget(QLabel("Vendor ID  (4-digit hex, e.g. ffff)"))
        self._vendor_id = QLineEdit()
        self._vendor_id.setPlaceholderText("ffff")
        layout.addWidget(self._vendor_id)

        layout.addWidget(QLabel("Vendor Name"))
        self._vendor_name = QLineEdit()
        self._vendor_name.setPlaceholderText("e.g. Acme Corp")
        layout.addWidget(self._vendor_name)

        # ── Product ──────────────────────────────────────────────────────────
        layout.addWidget(QLabel("Product ID  (4-digit hex, e.g. abcd)"))
        self._product_id = QLineEdit()
        self._product_id.setPlaceholderText("abcd")
        layout.addWidget(self._product_id)

        layout.addWidget(QLabel("Product Name"))
        self._product_name = QLineEdit()
        self._product_name.setPlaceholderText("e.g. USB Drive")
        layout.addWidget(self._product_name)

        # ── Action ───────────────────────────────────────────────────────────
        layout.addWidget(QLabel("Action *"))
        self._action_combo = QComboBox()
        self._action_combo.addItems(CLASS_ACTIONS)
        layout.addWidget(self._action_combo)

        # ── Optional fields ──────────────────────────────────────────────────
        layout.addWidget(QLabel("Serial Number  (optional)"))
        self._serial = QLineEdit()
        self._serial.setPlaceholderText("Leave blank to match any serial")
        layout.addWidget(self._serial)

        layout.addWidget(QLabel("Description  (optional)"))
        self._description = QLineEdit()
        layout.addWidget(self._description)

        self._use_wildcard = QCheckBox("Use wildcard matching")
        layout.addWidget(self._use_wildcard)

        # ── Buttons ──────────────────────────────────────────────────────────
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self._on_accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def _on_accept(self):
        """Validate that at least vendor ID is provided before accepting."""
        if not self._vendor_id.text().strip():
            QMessageBox.warning(self, "Validation", "Vendor ID is required.")
            return
        self.accept()

    # ── Properties used by caller ─────────────────────────────────────────────

    @property
    def class_id(self):
        """Return the selected device class ID."""
        return self._class_combo.currentText()

    @property
    def vendor_id(self):
        """Return the entered vendor ID string."""
        return self._vendor_id.text().strip()

    @property
    def vendor_name(self):
        """Return the entered vendor name."""
        return self._vendor_name.text().strip()

    @property
    def product_id(self):
        """Return the entered product ID string."""
        return self._product_id.text().strip()

    @property
    def product_name(self):
        """Return the entered product name."""
        return self._product_name.text().strip()

    @property
    def action(self):
        """Return the selected action string."""
        return self._action_combo.currentText()

    @property
    def serial_number(self):
        """Return the entered serial number (empty string if blank)."""
        return self._serial.text().strip()

    @property
    def description(self):
        """Return the entered description."""
        return self._description.text().strip()

    @property
    def use_wildcard(self):
        """Return True if the wildcard checkbox is checked."""
        return self._use_wildcard.isChecked()


# ── New / Edit policy dialog ──────────────────────────────────────────────────

class PolicyEditDialog(QDialog):
    """Dialog for creating a new policy or editing the name/description of an existing one."""

    def __init__(self, policy=None, parent=None):
        """Build form fields; policy=None means new, otherwise pre-populate from existing data."""
        super().__init__(parent)
        creating = policy is None
        self.setWindowTitle("New Policy" if creating else "Edit Policy")
        self.setMinimumWidth(420)

        layout = QVBoxLayout(self)

        # ── Name ────────────────────────────────────────────────────────────
        layout.addWidget(QLabel("Policy Name *"))
        self._name_field = QLineEdit()
        self._name_field.setPlaceholderText("e.g. USB Block — Workstations")
        if not creating:
            self._name_field.setText(policy.get("name", ""))
        layout.addWidget(self._name_field)

        # ── Description ─────────────────────────────────────────────────────
        layout.addWidget(QLabel("Description"))
        self._desc_field = QLineEdit()
        self._desc_field.setPlaceholderText("Optional description")
        if not creating:
            self._desc_field.setText(policy.get("description", ""))
        layout.addWidget(self._desc_field)

        # ── Platform ────────────────────────────────────────────────────────
        layout.addWidget(QLabel("Platform *"))
        self._platform_combo = QComboBox()
        self._platform_combo.addItems(["Windows", "Mac", "Linux"])
        if not creating:
            # Editing: platform is fixed after creation
            platform = policy.get("platform_name", "Windows")
            idx = self._platform_combo.findText(platform)
            if idx >= 0:
                self._platform_combo.setCurrentIndex(idx)
            self._platform_combo.setEnabled(False)
        layout.addWidget(self._platform_combo)

        # ── Buttons ─────────────────────────────────────────────────────────
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self._on_accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def _on_accept(self):
        """Validate required fields before accepting."""
        if not self._name_field.text().strip():
            QMessageBox.warning(self, "Validation", "Policy name is required.")
            return
        self.accept()

    @property
    def name(self):
        """Return the entered policy name."""
        return self._name_field.text().strip()

    @property
    def description(self):
        """Return the entered policy description."""
        return self._desc_field.text().strip()

    @property
    def platform(self):
        """Return the selected platform name."""
        return self._platform_combo.currentText()


# ── Main window ───────────────────────────────────────────────────────────────

class DeviceControlWindow(QMainWindow):
    """Main application window for the Device Control Policy Manager."""

    def __init__(self, sdk, group_sdk):
        """Build the full UI; sdk and group_sdk are authenticated FalconPy instances."""
        super().__init__()
        self._sdk = sdk
        self._group_sdk = group_sdk

        # Currently selected policy data dict (raw API resource)
        self._current_policy = None
        # Full policy list from last load
        self._all_policies = []
        # Track unsaved edits to current policy name/description
        self._dirty = False
        # Active background workers; kept as instance variables to prevent GC
        self._active_workers = []
        # Policy ID to re-select after the next list refresh (enable/disable/save)
        self._pending_reselect_id = None

        self.setWindowTitle("Device Control Policy Manager — CrowdStrike Falcon")
        self.setMinimumSize(1100, 650)
        self._build_ui()
        self._load_policies()

    # ── UI construction ───────────────────────────────────────────────────────

    def _build_ui(self):
        """Construct the complete widget hierarchy."""
        central = QWidget()
        self.setCentralWidget(central)
        root_layout = QVBoxLayout(central)
        root_layout.setContentsMargins(6, 6, 6, 6)

        # ── Toolbar ─────────────────────────────────────────────────────────
        toolbar = QToolBar("Actions")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        self._btn_new = QPushButton("New Policy")
        self._btn_new.clicked.connect(self._on_new_policy)
        toolbar.addWidget(self._btn_new)

        toolbar.addSeparator()

        self._btn_delete = QPushButton("Delete")
        self._btn_delete.setEnabled(False)
        self._btn_delete.clicked.connect(self._on_delete_policy)
        toolbar.addWidget(self._btn_delete)

        toolbar.addSeparator()

        self._btn_assign_group = QPushButton("Assign Host Group…")
        self._btn_assign_group.setEnabled(False)
        self._btn_assign_group.clicked.connect(self._on_assign_group)
        toolbar.addWidget(self._btn_assign_group)

        toolbar.addSeparator()

        self._btn_refresh = QPushButton("Refresh")
        self._btn_refresh.clicked.connect(self._load_policies)
        toolbar.addWidget(self._btn_refresh)

        # ── Main splitter ────────────────────────────────────────────────────
        splitter = QSplitter(Qt.Orientation.Horizontal)
        root_layout.addWidget(splitter)

        splitter.addWidget(self._build_policy_list_panel())
        splitter.addWidget(self._build_detail_panel())
        splitter.setSizes([380, 720])

        # ── Status bar ───────────────────────────────────────────────────────
        self._status_bar = QStatusBar()
        self.setStatusBar(self._status_bar)
        self._status_bar.showMessage("Connecting…")

    def _build_policy_list_panel(self):
        """Construct the left panel: filter bar + policy table."""
        panel = QGroupBox("Policies")
        layout = QVBoxLayout(panel)

        # Filter bar
        filter_row = QHBoxLayout()
        filter_row.addWidget(QLabel("Filter:"))
        self._filter_field = QLineEdit()
        self._filter_field.setPlaceholderText("Name or platform…")
        self._filter_field.textChanged.connect(self._apply_filter)
        filter_row.addWidget(self._filter_field)
        layout.addLayout(filter_row)

        # Policy table model
        self._policy_model = QStandardItemModel(0, 4, self)
        self._policy_model.setHorizontalHeaderLabels(
            ["Name", "Platform", "Enabled", "ID"]
        )

        self._proxy_model = QSortFilterProxyModel(self)
        self._proxy_model.setSourceModel(self._policy_model)
        self._proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self._proxy_model.setFilterKeyColumn(-1)

        self._policy_table = QTableView()
        self._policy_table.setModel(self._proxy_model)
        self._policy_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self._policy_table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self._policy_table.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self._policy_table.selectionModel().selectionChanged.connect(
            self._on_policy_selection_changed
        )
        layout.addWidget(self._policy_table)

        return panel

    def _build_detail_panel(self):
        """Construct the right panel: tabbed detail view + Save button."""
        panel = QGroupBox("Policy Details")
        layout = QVBoxLayout(panel)

        # ── Unsaved changes indicator ────────────────────────────────────────
        self._dirty_label = QLabel("")
        self._dirty_label.setStyleSheet("color: orange; font-weight: bold;")
        layout.addWidget(self._dirty_label)

        # ── Tabs ─────────────────────────────────────────────────────────────
        self._tabs = QTabWidget()
        layout.addWidget(self._tabs)

        self._tabs.addTab(self._build_general_tab(), "General")
        self._tabs.addTab(self._build_classes_tab(), "Device Classes")
        self._tabs.addTab(self._build_exceptions_tab(), "Exceptions")
        self._tabs.addTab(self._build_groups_tab(), "Host Groups")

        # ── Save / Enable / Disable row ───────────────────────────────────────
        action_row = QHBoxLayout()

        self._btn_save = QPushButton("Save Changes")
        self._btn_save.setEnabled(False)
        self._btn_save.clicked.connect(self._on_save_policy)
        action_row.addWidget(self._btn_save)

        self._btn_enable = QPushButton("Enable")
        self._btn_enable.setEnabled(False)
        self._btn_enable.clicked.connect(lambda: self._on_toggle_enabled(True))
        action_row.addWidget(self._btn_enable)

        self._btn_disable = QPushButton("Disable")
        self._btn_disable.setEnabled(False)
        self._btn_disable.clicked.connect(lambda: self._on_toggle_enabled(False))
        action_row.addWidget(self._btn_disable)

        layout.addLayout(action_row)

        return panel

    def _build_general_tab(self):
        """Build the General tab: name, description, platform, enabled."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout.addWidget(QLabel("Policy Name"))
        self._detail_name = QLineEdit()
        self._detail_name.setReadOnly(True)
        self._detail_name.textChanged.connect(self._mark_dirty)
        layout.addWidget(self._detail_name)

        layout.addWidget(QLabel("Description"))
        self._detail_desc = QLineEdit()
        self._detail_desc.setReadOnly(True)
        self._detail_desc.textChanged.connect(self._mark_dirty)
        layout.addWidget(self._detail_desc)

        layout.addWidget(QLabel("Platform"))
        self._detail_platform = QLineEdit()
        self._detail_platform.setReadOnly(True)
        layout.addWidget(self._detail_platform)

        status_row = QHBoxLayout()
        status_row.addWidget(QLabel("Status:"))
        self._detail_enabled = QLabel("—")
        font = QFont()
        font.setBold(True)
        self._detail_enabled.setFont(font)
        status_row.addWidget(self._detail_enabled)
        status_row.addStretch()
        layout.addLayout(status_row)

        layout.addWidget(QLabel("Policy ID"))
        self._detail_id = QLineEdit()
        self._detail_id.setReadOnly(True)
        layout.addWidget(self._detail_id)

        layout.addStretch()
        return widget

    def _build_classes_tab(self):
        """Build the Device Classes tab: one action dropdown per USB class."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout.addWidget(QLabel(
            "Configure the action applied to each USB device class.\n"
            "Changes take effect when you click Save Changes."
        ))

        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.StyledPanel)
        frame_layout = QVBoxLayout(frame)

        self._class_combos = {}
        for class_id in DEVICE_CLASSES:
            row = QHBoxLayout()
            label = QLabel(class_id.replace("_", " ").title())
            label.setFixedWidth(200)
            row.addWidget(label)

            combo = QComboBox()
            combo.addItems(CLASS_ACTIONS)
            combo.setEnabled(False)
            combo.currentIndexChanged.connect(self._mark_dirty)
            self._class_combos[class_id] = combo
            row.addWidget(combo)
            row.addStretch()
            frame_layout.addLayout(row)

        layout.addWidget(frame)
        layout.addStretch()
        return widget

    def _build_exceptions_tab(self):
        """Build the Exceptions tab: table of vendor/product ID exceptions."""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        layout.addWidget(QLabel(
            "Vendor/product ID exceptions allow specific USB devices to bypass class rules."
        ))

        self._exceptions_table = QTableWidget(0, 6)
        self._exceptions_table.setHorizontalHeaderLabels(
            ["Class", "Vendor Name", "Vendor ID", "Product Name", "Product ID", "Action"]
        )
        self._exceptions_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self._exceptions_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self._exceptions_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self._exceptions_table.selectionModel().selectionChanged.connect(
            self._on_exceptions_table_selection_changed
        )
        layout.addWidget(self._exceptions_table)

        btn_row = QHBoxLayout()
        self._btn_add_exception = QPushButton("Add Exception…")
        self._btn_add_exception.setEnabled(False)
        self._btn_add_exception.clicked.connect(self._on_add_exception)
        btn_row.addWidget(self._btn_add_exception)

        self._btn_delete_exception = QPushButton("Delete Selected Exception")
        self._btn_delete_exception.setEnabled(False)
        self._btn_delete_exception.clicked.connect(self._on_delete_exception)
        btn_row.addWidget(self._btn_delete_exception)
        btn_row.addStretch()
        layout.addLayout(btn_row)

        return widget

    def _build_groups_tab(self):
        """Build the Host Groups tab: list of assigned groups + remove button."""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        layout.addWidget(QLabel(
            "Host groups currently assigned to this policy.\n"
            "Use 'Assign Host Group…' in the toolbar to add a group."
        ))

        self._groups_table = QTableWidget(0, 3)
        self._groups_table.setHorizontalHeaderLabels(["Name", "Type", "Description"])
        self._groups_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self._groups_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self._groups_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self._groups_table.selectionModel().selectionChanged.connect(
            self._on_groups_table_selection_changed
        )
        layout.addWidget(self._groups_table)

        self._btn_remove_group = QPushButton("Remove Selected Host Group")
        self._btn_remove_group.setEnabled(False)
        self._btn_remove_group.clicked.connect(self._on_remove_group)
        layout.addWidget(self._btn_remove_group)

        return widget

    # ── Policy loading ────────────────────────────────────────────────────────

    def _load_policies(self):
        """Start background load of all policies; disable UI while loading."""
        self._set_ui_loading(True)
        self._status_bar.showMessage("Loading policies…")
        worker = LoadPoliciesWorker(self._sdk, parent=self)
        worker.finished.connect(self._on_policies_loaded)
        self._active_workers.append(worker)
        worker.start()

    def _on_policies_loaded(self, policies, error):
        """Populate the policy table once the worker delivers results."""
        self._set_ui_loading(False)
        # Remove finished worker from tracking list
        sender = self.sender()
        if sender in self._active_workers:
            self._active_workers.remove(sender)

        if error:
            self._status_bar.showMessage(f"Error loading policies: {error}")
            QMessageBox.critical(self, "Load Error", error)
            return

        self._all_policies = policies
        self._populate_policy_table(policies)
        if self._pending_reselect_id:
            self._reselect_policy_by_id(self._pending_reselect_id)
            self._pending_reselect_id = None
        count = len(policies)
        self._status_bar.showMessage(
            f"{count} polic{'ies' if count != 1 else 'y'} loaded."
        )

    def _populate_policy_table(self, policies):
        """Rebuild the policy table model from a list of policy resources."""
        self._policy_model.setRowCount(0)
        for policy in policies:
            enabled = "Yes" if policy.get("enabled", False) else "No"
            row = [
                QStandardItem(policy.get("name", "")),
                QStandardItem(policy.get("platform_name", "")),
                QStandardItem(enabled),
                QStandardItem(policy.get("id", "")),
            ]
            # Store the full policy dict on the first item for retrieval later
            row[0].setData(policy, Qt.ItemDataRole.UserRole)
            for item in row:
                item.setEditable(False)
            self._policy_model.appendRow(row)

    def _reselect_policy_by_id(self, policy_id):
        """Re-select the table row whose policy ID matches policy_id.

        Iterates the source model to find the row, then translates the index
        through the proxy and scrolls the view to it.  Called after a list
        refresh when we want to preserve the user's selection.
        """
        if not policy_id:
            return
        for row in range(self._policy_model.rowCount()):
            item = self._policy_model.item(row, 0)
            if item and item.data(Qt.ItemDataRole.UserRole).get("id") == policy_id:
                proxy_index = self._proxy_model.mapFromSource(
                    self._policy_model.index(row, 0)
                )
                if proxy_index.isValid():
                    self._policy_table.selectionModel().select(
                        proxy_index,
                        self._policy_table.selectionModel().SelectionFlag.ClearAndSelect
                        | self._policy_table.selectionModel().SelectionFlag.Rows,
                    )
                    self._policy_table.scrollTo(proxy_index)
                return

    # ── Policy selection ──────────────────────────────────────────────────────

    def _on_policy_selection_changed(self):
        """Update the detail panel when the user selects a different policy."""
        indexes = self._policy_table.selectionModel().selectedRows()
        has_selection = bool(indexes)

        self._btn_delete.setEnabled(has_selection)
        self._btn_assign_group.setEnabled(has_selection)
        self._btn_enable.setEnabled(has_selection)
        self._btn_disable.setEnabled(has_selection)
        self._btn_save.setEnabled(has_selection)

        if not has_selection:
            self._clear_detail_panel()
            self._current_policy = None
            return

        source_index = self._proxy_model.mapToSource(indexes[0])
        item = self._policy_model.item(source_index.row(), 0)
        policy = item.data(Qt.ItemDataRole.UserRole) if item else None
        if policy:
            self._current_policy = policy
            self._populate_detail_panel(policy)

    def _populate_detail_panel(self, policy):
        """Fill all detail tab fields from a policy resource dict."""
        # Block dirty tracking while programmatically setting values
        self._dirty = False

        # General tab
        self._detail_name.setReadOnly(False)
        self._detail_desc.setReadOnly(False)

        # Temporarily disconnect signals to avoid spurious dirty marks
        self._detail_name.blockSignals(True)
        self._detail_desc.blockSignals(True)

        self._detail_name.setText(policy.get("name", ""))
        self._detail_desc.setText(policy.get("description", ""))
        self._detail_platform.setText(policy.get("platform_name", ""))
        self._detail_id.setText(policy.get("id", ""))

        enabled = policy.get("enabled", False)
        self._detail_enabled.setText("Enabled" if enabled else "Disabled")
        self._detail_enabled.setStyleSheet(
            "color: green; font-weight: bold;" if enabled
            else "color: gray; font-weight: bold;"
        )

        self._detail_name.blockSignals(False)
        self._detail_desc.blockSignals(False)

        # Device Classes tab — read the classes list from settings
        for combo in self._class_combos.values():
            combo.setEnabled(True)

        # Exceptions tab — enable Add button now that a policy is loaded
        self._btn_add_exception.setEnabled(True)
        self._btn_delete_exception.setEnabled(False)  # enabled on row selection

        settings = policy.get("settings") or {}
        classes = settings.get("classes") or []
        class_map = {c.get("id", ""): c.get("action", "FULL_ACCESS") for c in classes}

        for class_id, combo in self._class_combos.items():
            combo.blockSignals(True)
            action = class_map.get(class_id, "FULL_ACCESS")
            idx = combo.findText(action)
            combo.setCurrentIndex(idx if idx >= 0 else 0)
            combo.blockSignals(False)

        # Exceptions tab
        self._populate_exceptions(classes)

        # Host Groups tab
        self._populate_groups_tab(policy)

        self._dirty = False
        self._dirty_label.setText("")

    def _populate_exceptions(self, classes):
        """Fill the exceptions table from the classes list in policy settings."""
        self._exceptions_table.setRowCount(0)
        for cls in classes:
            class_id = cls.get("id", "")
            for exc in cls.get("exceptions") or []:
                row_idx = self._exceptions_table.rowCount()
                self._exceptions_table.insertRow(row_idx)
                class_item = QTableWidgetItem(class_id)
                # Store (exception_id, class_id) tuple for use by delete handler.
                class_item.setData(
                    Qt.ItemDataRole.UserRole, (exc.get("id", ""), class_id)
                )
                self._exceptions_table.setItem(row_idx, 0, class_item)
                self._exceptions_table.setItem(
                    row_idx, 1, QTableWidgetItem(exc.get("vendor_name", ""))
                )
                self._exceptions_table.setItem(
                    row_idx, 2, QTableWidgetItem(exc.get("vendor_id", ""))
                )
                self._exceptions_table.setItem(
                    row_idx, 3, QTableWidgetItem(exc.get("product_name", ""))
                )
                self._exceptions_table.setItem(
                    row_idx, 4, QTableWidgetItem(exc.get("product_id", ""))
                )
                self._exceptions_table.setItem(
                    row_idx, 5, QTableWidgetItem(exc.get("action", ""))
                )

    def _on_exceptions_table_selection_changed(self):
        """Enable Delete button when an exception row is selected."""
        self._btn_delete_exception.setEnabled(
            bool(self._exceptions_table.selectionModel().selectedRows())
        )

    def _on_add_exception(self):
        """Open the Add Exception dialog and send the new exception to the API."""
        if not self._current_policy:
            return

        dlg = ExceptionDialog(DEVICE_CLASSES, parent=self)
        if dlg.exec() != QDialog.DialogCode.Accepted:
            return

        policy_id = self._current_policy.get("id")
        # Build classes list: the target class gets the new exception appended;
        # all other classes are passed through with their existing exceptions
        # so the API does not discard them.
        original_classes = (
            (self._current_policy.get("settings") or {}).get("classes") or []
        )
        orig_map = {c.get("id", ""): dict(c) for c in original_classes}

        new_exc = {
            "vendor_id": dlg.vendor_id,
            "vendor_name": dlg.vendor_name,
            "product_id": dlg.product_id,
            "product_name": dlg.product_name,
            "action": dlg.action,
            "use_wildcard": dlg.use_wildcard,
        }
        if dlg.serial_number:
            new_exc["serial_number"] = dlg.serial_number
        if dlg.description:
            new_exc["description"] = dlg.description

        target_class_id = dlg.class_id
        if target_class_id not in orig_map:
            orig_map[target_class_id] = {"id": target_class_id, "action": "FULL_ACCESS"}

        target_entry = orig_map[target_class_id]
        existing_excs = list(target_entry.get("exceptions") or [])
        existing_excs.append(new_exc)
        target_entry["exceptions"] = existing_excs

        # Ensure all known class IDs appear in the payload (preserving combos).
        classes = []
        for class_id, combo in self._class_combos.items():
            entry = dict(orig_map.get(class_id) or {"id": class_id})
            entry["action"] = combo.currentText()
            classes.append(entry)

        self._pending_reselect_id = policy_id
        self._status_bar.showMessage("Adding exception…")
        worker = SavePolicyWorker(
            self._sdk,
            policy_id=policy_id,
            name=self._current_policy.get("name", ""),
            description=self._current_policy.get("description", ""),
            platform=self._current_policy.get("platform_name", "Windows"),
            settings={"classes": classes},
            parent=self,
        )
        worker.finished.connect(self._on_policy_saved)
        self._active_workers.append(worker)
        worker.start()

    def _on_delete_exception(self):
        """Delete the selected exception via the API's delete_exceptions payload."""
        if not self._current_policy:
            return
        rows = self._exceptions_table.selectionModel().selectedRows()
        if not rows:
            return

        row_idx = rows[0].row()
        class_item = self._exceptions_table.item(row_idx, 0)
        if not class_item:
            return

        exc_id, _ = class_item.data(Qt.ItemDataRole.UserRole) or ("", "")
        if not exc_id:
            QMessageBox.warning(
                self, "Cannot Delete",
                "This exception has no ID — it may not have been saved to the API yet."
            )
            return

        vendor_name = (self._exceptions_table.item(row_idx, 1) or QTableWidgetItem("")).text()
        product_name = (self._exceptions_table.item(row_idx, 3) or QTableWidgetItem("")).text()
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Delete exception for '{vendor_name}' / '{product_name}'?\n\nThis cannot be undone.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

        policy_id = self._current_policy.get("id")
        self._pending_reselect_id = policy_id
        self._status_bar.showMessage("Deleting exception…")
        worker = SavePolicyWorker(
            self._sdk,
            policy_id=policy_id,
            name=self._current_policy.get("name", ""),
            description=self._current_policy.get("description", ""),
            platform=self._current_policy.get("platform_name", "Windows"),
            settings={"delete_exceptions": [exc_id]},
            parent=self,
        )
        worker.finished.connect(self._on_policy_saved)
        self._active_workers.append(worker)
        worker.start()

    def _populate_groups_tab(self, policy):
        """Fill the Host Groups table from the groups list in the policy resource."""
        self._groups_table.setRowCount(0)
        self._btn_remove_group.setEnabled(False)
        for group in policy.get("groups") or []:
            row_idx = self._groups_table.rowCount()
            self._groups_table.insertRow(row_idx)
            name_item = QTableWidgetItem(group.get("name", ""))
            # Stash the group ID so we can use it for the remove action
            name_item.setData(Qt.ItemDataRole.UserRole, group.get("id", ""))
            self._groups_table.setItem(row_idx, 0, name_item)
            self._groups_table.setItem(
                row_idx, 1, QTableWidgetItem(group.get("group_type", ""))
            )
            self._groups_table.setItem(
                row_idx, 2, QTableWidgetItem(group.get("description", ""))
            )

    def _clear_detail_panel(self):
        """Reset all detail fields to empty / disabled state."""
        for field in (self._detail_name, self._detail_desc, self._detail_platform, self._detail_id):
            field.blockSignals(True)
            field.setText("")
            field.setReadOnly(True)
            field.blockSignals(False)

        self._detail_enabled.setText("—")
        self._detail_enabled.setStyleSheet("")

        for combo in self._class_combos.values():
            combo.setEnabled(False)

        self._exceptions_table.setRowCount(0)
        self._btn_add_exception.setEnabled(False)
        self._btn_delete_exception.setEnabled(False)
        self._groups_table.setRowCount(0)
        self._btn_remove_group.setEnabled(False)
        self._dirty = False
        self._dirty_label.setText("")

    # ── Dirty tracking ────────────────────────────────────────────────────────

    def _mark_dirty(self):
        """Record that the user has made unsaved changes."""
        if self._current_policy is not None:
            self._dirty = True
            self._dirty_label.setText("● Unsaved changes")

    # ── Policy actions ────────────────────────────────────────────────────────

    def _on_new_policy(self):
        """Open the New Policy dialog and create the policy if confirmed."""
        dlg = PolicyEditDialog(parent=self)
        if dlg.exec() != QDialog.DialogCode.Accepted:
            return

        self._status_bar.showMessage("Creating policy…")
        worker = SavePolicyWorker(
            self._sdk,
            policy_id=None,
            name=dlg.name,
            description=dlg.description,
            platform=dlg.platform,
            parent=self,
        )
        worker.finished.connect(self._on_policy_saved)
        self._active_workers.append(worker)
        worker.start()

    def _on_save_policy(self):
        """Save name / description edits for the currently selected policy."""
        if not self._current_policy:
            return

        if not self._detail_name.text().strip():
            QMessageBox.warning(self, "Validation", "Policy name cannot be empty.")
            return

        policy_id = self._current_policy.get("id")
        # Capture ID so we can re-select the same row after the list refreshes.
        self._pending_reselect_id = policy_id

        # Build the device class settings payload from the combo boxes, preserving
        # any existing exceptions inside each class entry.
        original_classes = (
            (self._current_policy.get("settings") or {}).get("classes") or []
        )
        orig_map = {c.get("id", ""): c for c in original_classes}
        classes = []
        for class_id, combo in self._class_combos.items():
            entry = dict(orig_map.get(class_id) or {"id": class_id})
            entry["action"] = combo.currentText()
            classes.append(entry)
        settings = {"classes": classes}

        self._status_bar.showMessage("Saving changes…")
        worker = SavePolicyWorker(
            self._sdk,
            policy_id=policy_id,
            name=self._detail_name.text().strip(),
            description=self._detail_desc.text().strip(),
            platform=self._current_policy.get("platform_name", "Windows"),
            settings=settings,
            parent=self,
        )
        worker.finished.connect(self._on_policy_saved)
        self._active_workers.append(worker)
        worker.start()

    def _on_policy_saved(self, saved_resource, error):
        """Refresh the policy list after a successful save or report the error."""
        sender = self.sender()
        if sender in self._active_workers:
            self._active_workers.remove(sender)

        if error:
            self._status_bar.showMessage(f"Save failed: {error}")
            QMessageBox.critical(self, "Save Error", error)
            return

        # For new policy creation _pending_reselect_id is not pre-set; use the
        # returned resource ID so the new row is selected after the list refreshes.
        if not self._pending_reselect_id and saved_resource:
            self._pending_reselect_id = saved_resource.get("id")

        self._dirty = False
        self._dirty_label.setText("")
        self._status_bar.showMessage("Policy saved. Refreshing…")
        self._load_policies()

    def _on_delete_policy(self):
        """Confirm and then delete the selected policy."""
        if not self._current_policy:
            return

        policy_name = self._current_policy.get("name", "this policy")
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Permanently delete policy '{policy_name}'?\n\nThis action cannot be undone.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

        policy_id = self._current_policy.get("id")
        self._status_bar.showMessage("Deleting policy…")
        worker = DeletePolicyWorker(self._sdk, [policy_id], parent=self)
        worker.finished.connect(self._on_policy_deleted)
        self._active_workers.append(worker)
        worker.start()

    def _on_policy_deleted(self, success, error):
        """Handle result of delete operation."""
        sender = self.sender()
        if sender in self._active_workers:
            self._active_workers.remove(sender)

        if not success:
            self._status_bar.showMessage(f"Delete failed: {error}")
            QMessageBox.critical(self, "Delete Error", error)
            return

        self._current_policy = None
        self._clear_detail_panel()
        self._btn_delete.setEnabled(False)
        self._btn_assign_group.setEnabled(False)
        self._btn_save.setEnabled(False)
        self._btn_enable.setEnabled(False)
        self._btn_disable.setEnabled(False)
        self._status_bar.showMessage("Policy deleted. Refreshing…")
        self._load_policies()

    def _on_toggle_enabled(self, enable):
        """Enable or disable the currently selected policy."""
        if not self._current_policy:
            return

        action_name = "enable" if enable else "disable"
        policy_id = self._current_policy.get("id")
        # Capture ID so we can re-select the same row after the list refreshes.
        self._pending_reselect_id = policy_id

        self._status_bar.showMessage(f"{'Enabling' if enable else 'Disabling'} policy…")
        worker = ActionWorker(self._sdk, policy_id, action_name, parent=self)
        worker.finished.connect(lambda ok, err: self._on_action_done(ok, err, action_name))
        self._active_workers.append(worker)
        worker.start()

    def _on_action_done(self, success, error, action_name):
        """Handle result of enable/disable/assign-group action."""
        sender = self.sender()
        if sender in self._active_workers:
            self._active_workers.remove(sender)

        if not success:
            self._status_bar.showMessage(f"Action failed: {error}")
            QMessageBox.critical(self, "Action Error", error)
            return

        self._status_bar.showMessage(f"Action '{action_name}' applied. Refreshing…")
        self._load_policies()

    def _on_assign_group(self):
        """Open the Host Group assignment dialog and assign the chosen group."""
        if not self._current_policy:
            return

        policy_name = self._current_policy.get("name", "")
        dlg = HostGroupDialog(self._group_sdk, policy_name, parent=self)
        if dlg.exec() != QDialog.DialogCode.Accepted:
            return

        group_id = dlg.selected_group_id
        group_name = dlg.selected_group_name
        if not group_id:
            return

        policy_id = self._current_policy.get("id")
        # Capture ID so we can re-select the same row after the list refreshes.
        self._pending_reselect_id = policy_id
        self._status_bar.showMessage(f"Assigning host group '{group_name}'…")
        worker = ActionWorker(
            self._sdk, policy_id, "add-host-group", group_id=group_id, parent=self
        )
        worker.finished.connect(
            lambda ok, err: self._on_action_done(ok, err, "add-host-group")
        )
        self._active_workers.append(worker)
        worker.start()

    def _on_groups_table_selection_changed(self):
        """Enable the Remove button when a host group row is selected."""
        self._btn_remove_group.setEnabled(
            bool(self._groups_table.selectionModel().selectedRows())
        )

    def _on_remove_group(self):
        """Remove the selected host group from the current policy."""
        if not self._current_policy:
            return
        rows = self._groups_table.selectionModel().selectedRows()
        if not rows:
            return

        row_idx = rows[0].row()
        name_item = self._groups_table.item(row_idx, 0)
        if not name_item:
            return

        group_id = name_item.data(Qt.ItemDataRole.UserRole)
        group_name = name_item.text()
        if not group_id:
            return

        reply = QMessageBox.question(
            self,
            "Confirm Remove",
            f"Remove host group '{group_name}' from this policy?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

        policy_id = self._current_policy.get("id")
        # Capture ID so we can re-select the same row after the list refreshes.
        self._pending_reselect_id = policy_id
        self._status_bar.showMessage(f"Removing host group '{group_name}'…")
        worker = ActionWorker(
            self._sdk, policy_id, "remove-host-group", group_id=group_id, parent=self
        )
        worker.finished.connect(
            lambda ok, err: self._on_action_done(ok, err, "remove-host-group")
        )
        self._active_workers.append(worker)
        worker.start()

    # ── Filter ────────────────────────────────────────────────────────────────

    def _apply_filter(self, text):
        """Forward the filter text to the proxy model for client-side filtering."""
        self._proxy_model.setFilterFixedString(text)

    # ── Loading state helpers ─────────────────────────────────────────────────

    def _set_ui_loading(self, loading):
        """Disable interactive controls while a network operation is in progress."""
        self._btn_new.setEnabled(not loading)
        self._btn_refresh.setEnabled(not loading)
        if loading:
            self._btn_delete.setEnabled(False)
            self._btn_assign_group.setEnabled(False)
            self._btn_save.setEnabled(False)
            self._btn_enable.setEnabled(False)
            self._btn_disable.setEnabled(False)


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    """Parse CLI credentials, build SDK instances, and launch the GUI."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-k", "--client_id",
        default=None,
        metavar="CLIENT_ID",
        help="Falcon API client ID (overrides FALCON_CLIENT_ID env var)",
    )
    parser.add_argument(
        "-s", "--client_secret",
        default=None,
        metavar="CLIENT_SECRET",
        help="Falcon API client secret (overrides FALCON_CLIENT_SECRET env var)",
    )
    parser.add_argument(
        "-b", "--base_url",
        default=None,
        metavar="BASE_URL",
        help="Cloud region base URL (overrides FALCON_BASE_URL env var, default: auto)",
    )
    args = parser.parse_args()

    # CLI flags take precedence over environment variables.
    client_id = args.client_id or os.environ.get("FALCON_CLIENT_ID", "")
    client_secret = args.client_secret or os.environ.get("FALCON_CLIENT_SECRET", "")
    base_url = args.base_url or os.environ.get("FALCON_BASE_URL", "auto")

    # Validate credentials before creating the window
    if not client_id or not client_secret:
        # Still launch the app so we can show a meaningful error dialog
        app = QApplication(sys.argv)
        QMessageBox.critical(
            None,
            "Missing Credentials",
            "Credentials must be supplied via -k/-s flags or environment variables.\n\n"
            "CLI flags:\n"
            "  -k CLIENT_ID   -s CLIENT_SECRET\n\n"
            "Environment variables:\n"
            "  export FALCON_CLIENT_ID=your_id\n"
            "  export FALCON_CLIENT_SECRET=your_secret",
        )
        sys.exit(1)

    # Build SDK instances; both share the same credential pair
    sdk = DeviceControlPolicies(
        client_id=client_id,
        client_secret=client_secret,
        base_url=base_url,
    )
    group_sdk = HostGroup(
        client_id=client_id,
        client_secret=client_secret,
        base_url=base_url,
    )

    app = QApplication(sys.argv)
    app.setApplicationName("Device Control Policy Manager")

    window = DeviceControlWindow(sdk, group_sdk)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
