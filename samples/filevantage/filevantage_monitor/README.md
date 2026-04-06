![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# FileVantage Change Monitor

A PyQt6 desktop application for monitoring CrowdStrike Falcon FileVantage file integrity monitoring (FIM) change events. It retrieves change events from the Falcon platform using the FalconPy SDK and displays them in an auto-refreshing live feed with drill-down detail dialogs.

The toolbar provides a server-side FQL filter, a change-type dropdown, and a free-text search field for client-side filtering. The event table auto-refreshes every 30 seconds and colour-codes rows by change type (CREATE, WRITE, DELETE, RENAME, CHMOD, CHOWN, CHATTR) for fast visual scanning. Double-clicking any row opens a detail dialog with the full event summary, before/after SHA-256 hash comparison, the three-level process chain (process, parent, grandparent), and a raw JSON tab. Selected events can be suppressed or purged via the FileVantage `start_actions` API, and all visible rows can be exported to CSV.

If no credentials are set, the application starts in **demo mode** with built-in fixture events so the interface can be explored without API keys.

> **Note:** The `filevantage:write` scope is only required if you intend to suppress or purge change events. Read-only use requires `filevantage:read` only.

## Running the program

In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| FileVantage | __READ__ |
| FileVantage | __WRITE__ _(optional — required for suppress/purge actions)_ |

### Execution syntax

This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown below without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

> Launch with credentials passed via CLI flags.

```shell
python3 filevantage_monitor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Launch using environment variables (no flags needed).

```shell
python3 filevantage_monitor.py
```

> Launch in demo mode (no credentials required — runs automatically when credentials are absent).

```shell
python3 filevantage_monitor.py
```

> Connect to a GovCloud tenant.

```shell
python3 filevantage_monitor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

#### Command-line help

Command-line help is available via the `-h` argument.

```shell
usage: filevantage_monitor.py [-h] [-k CLIENT_ID] [-s CLIENT_SECRET]
                              [-b BASE_URL]

FileVantage Change Monitor — Desktop GUI.

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

options:
  -h, --help            show this help message and exit
  -k CLIENT_ID, --client_id CLIENT_ID
                        Falcon API client ID (overrides FALCON_CLIENT_ID env var)
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        Falcon API client secret (overrides FALCON_CLIENT_SECRET env var)
  -b BASE_URL, --base_url BASE_URL
                        Cloud region base URL (default: auto). Use usgov1 for GovCloud.
```

### Example source code

The source code for this example can be found [here](filevantage_monitor.py).
