![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# RTR Session Replay
Retrieve and replay the full command history of historical CrowdStrike Falcon Real Time Response (RTR) sessions. Two interfaces are provided:

- **Terminal** (`rtr_replay.py`) — Replay a specific session, or list recent sessions with a summary, directly in the console.
- **Desktop GUI** (`rtr_replay_gui.py`) — A PySide6 application for browsing, filtering, and replaying RTR sessions with a dark CrowdStrike-branded interface.

Both tools query the RTR Audit API (`RealTimeResponseAudit`) to retrieve session metadata and the full command log (timestamps, working directories, and command strings) for each session. A `--demo` flag is available on both tools to explore the output using built-in fixture data without API credentials.

> **Note:** The required API scope is `real-time-response-audit:read`. This is distinct from the `real-time-response:read` scope used for live RTR sessions and must be explicitly enabled in the Falcon API client settings.

## Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Real Time Response Audit | __READ__ |

### Requirements

| Package | Required by |
| :---- | :---- |
| crowdstrike-falconpy | Both tools |
| PySide6 | GUI only (`rtr_replay_gui.py`) |

## Terminal — `rtr_replay.py`

The terminal tool operates in three modes: replay a specific session by ID, list recent sessions, or display demo data.

For each replayed session the tool displays a formatted header (session ID, hostname, device ID, operator, platform, start/end time, duration, queued status) followed by the chronological command log showing the timestamp, working directory, and full command string for each entry.

### Execution syntax

> Replay a specific RTR session by its session ID.

```shell
python3 rtr_replay.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i SESSION_ID
```

> Both tools support [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown below without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

```shell
python3 rtr_replay.py -i SESSION_ID
```

> List recent RTR sessions with a one-line summary per session.

```shell
python3 rtr_replay.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --list
```

> List the 25 most recent sessions.

```shell
python3 rtr_replay.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --list --limit 25
```

> Run in demo mode with built-in fixture data (no credentials required).

```shell
python3 rtr_replay.py --demo
```

> Connect to a GovCloud tenant.

```shell
python3 rtr_replay.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1 --list
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: rtr_replay.py [-h] [-k FALCON_CLIENT_ID] [-s FALCON_CLIENT_SECRET]
                     [-b BASE_URL] [-i SESSION_ID] [--list] [--limit LIMIT]
                     [--demo]

Replay the command history of a historical CrowdStrike Falcon RTR session.

 _______ _______ ______         _______ _______ _______ _____   _______ ___ ___
|   _   |       |   _  \       |   _   |   _   |   _   |     | |   _   |   Y   |
|.  l   |.|   | |.  l   \      |.  l   |.  1___|.  1   |.    | |.  1   |.  1   |
|.  _   `-|.  |-|.  _   /      |.  l   |.  __) |.  ____|.    | |.  _   |.  _   |
|:  l   | |:  | |:  l   \      |:  l   |:  |   |:  |   |:  . | |:  |   |:  |   |
|::.. . | |::.| |::.. .  /     |::.. . |::.|   |::.|   |::. :| |::.|:. |::.|:. |
`-------' `---' `------^'      `-------`---'   `---'   `--:--' `--- ---`--- ---'

                                                     RTR Audit Session Replay
                                                     Uses: RealTimeResponseAudit
                                                     Scope: real-time-response-audit:read

Retrieve and display the full command history of a historical RTR session.

Modes:
  Replay a specific session:   rtr_replay.py -k KEY -s SECRET -i SESSION_ID
  List recent sessions:        rtr_replay.py -k KEY -s SECRET --list [--limit N]
  Demo (no credentials):       rtr_replay.py --demo

Credentials may also be supplied via environment variables:
  FALCON_CLIENT_ID / FALCON_CLIENT_SECRET

NOTE: The real-time-response-audit:read API scope is required. This is distinct
from the real-time-response:read scope used for live RTR sessions.

Created by: Manjula Wickramasuriya (@Manjula101) - Enterprise Security Lab
Modified by: jshcodes@CrowdStrike

options:
  -h, --help            show this help message and exit
  -k, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API client ID.
                        Can also be set via FALCON_CLIENT_ID env var.
  -s, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API client secret.
                        Can also be set via FALCON_CLIENT_SECRET env var.
  -b, --base_url BASE_URL
                        CrowdStrike region base URL.
                        Only required for GovCloud users (usgov1).
  -i, --session_id SESSION_ID
                        RTR session ID to replay.
  --list                List recent RTR sessions instead of replaying one.
  --limit LIMIT         Maximum number of sessions to return when using --list (default: 10).
  --demo                Run in demo mode using built-in fixture data (no credentials required).
```

### Example source code
The source code for this example can be found [here](rtr_replay.py).

---

## Desktop GUI — `rtr_replay_gui.py`

A PySide6 desktop application for browsing and replaying RTR sessions. The GUI features a dark CrowdStrike-branded theme, paginated session browsing with background prefetch, client-side filtering, server-side date range and sort controls, and a replay panel that displays session metadata and a formatted command log.

### Architecture

```
RTRReplayWindow (QMainWindow)
├── Credential panel (QGroupBox) — API key input + region dropdown
├── Session list panel (QGroupBox, left splitter pane)
│   ├── Filter bar (QLineEdit) — client-side substring filter
│   ├── Sort / Per-page / Date range row — server-side controls
│   ├── Session table (QTableView + QSortFilterProxyModel)
│   └── Pagination row — Prev / Page N of M / Next / Go to page
└── Replay panel (QGroupBox, right splitter pane)
    ├── Metadata labels — host, operator, start time, duration
    └── Command log (QTextEdit, read-only monospace)
```

API calls are made on background QThreads (`FetchSessionsWorker` for foreground page fetches, `PrefetchWorker` for background cursor walking) and results are delivered to the main thread via Qt signals, keeping the UI responsive during network I/O.

Credentials can be supplied via CLI flags, environment variables, or entered directly into the credential panel at runtime.

### Execution syntax

> Launch the GUI with no pre-filled credentials (enter them in the UI).

```shell
python3 rtr_replay_gui.py
```

> Launch in demo mode with built-in fixture data (no credentials required).

```shell
python3 rtr_replay_gui.py --demo
```

> Launch with pre-filled credentials from the command line.

```shell
python3 rtr_replay_gui.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Launch against a GovCloud tenant.

```shell
python3 rtr_replay_gui.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

> Pre-filter sessions to a specific hostname on load.

```shell
python3 rtr_replay_gui.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -n WIN-WORKSTATION-42
```

> Auto-navigate to a specific session after loading.

```shell
python3 rtr_replay_gui.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i SESSION_ID
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: rtr_replay_gui.py [-h] [-k CLIENT_ID] [-s CLIENT_SECRET] [-b BASE_URL]
                         [-n HOSTNAME] [-i SESSION_ID] [--demo]

RTR Session Replay — Desktop GUI.

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

options:
  -h, --help            show this help message and exit
  -k, --client_id CLIENT_ID
                        CrowdStrike Falcon API client ID.
                        Can also be set via FALCON_CLIENT_ID env var.
  -s, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API client secret.
                        Can also be set via FALCON_CLIENT_SECRET env var.
  -b, --base_url BASE_URL
                        CrowdStrike region base URL (default: auto).
                        Only required for GovCloud tenants.
  -n, --hostname HOSTNAME
                        Filter sessions to this hostname on load.
  -i, --session_id SESSION_ID
                        Auto-navigate to this session ID after loading.
  --demo                Load built-in fixture data without credentials.
```

### Example source code
The source code for this example can be found here:

- [RTR Replay (Terminal)](rtr_replay.py)
- [RTR Replay (Desktop GUI)](rtr_replay_gui.py)
