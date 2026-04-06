![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Device Control Policy Manager

A PySide6 desktop application for managing CrowdStrike Falcon USB Device Control Policies. Browse, create, edit, enable/disable, and delete device control policies. Assign host groups to policies via a searchable modal dialog. The detail panel provides tabbed views for general policy settings, per-class USB device actions, vendor/product ID exceptions, and assigned host groups.

API calls run on background `QThread` workers and results are delivered back to the main thread via Qt signals, keeping the UI fully responsive during network I/O.

## Running the program

In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Device Control Policies | __READ__, __WRITE__ |
| Host Group | __READ__ |

### Execution syntax

This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown below without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

> Launch with credentials passed via CLI flags.

```shell
python3 device_control_policy_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Launch using environment variables (no flags needed).

```shell
python3 device_control_policy_manager.py
```

> Connect to a specific cloud region.

```shell
python3 device_control_policy_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

#### Command-line help

Command-line help is available via the `-h` argument.

```shell
usage: device_control_policy_manager.py [-h] [-k CLIENT_ID] [-s CLIENT_SECRET]
                                        [-b BASE_URL]

Device Control Policy Manager — Desktop GUI.

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

options:
  -h, --help            show this help message and exit
  -k CLIENT_ID, --client_id CLIENT_ID
                        Falcon API client ID (overrides FALCON_CLIENT_ID env
                        var)
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        Falcon API client secret (overrides
                        FALCON_CLIENT_SECRET env var)
  -b BASE_URL, --base_url BASE_URL
                        Cloud region base URL (overrides FALCON_BASE_URL env
                        var, default: auto)
```

### Example source code

The source code for this example can be found [here](device_control_policy_manager.py).
