![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Spotlight Vulnerability Dashboard

A PySide6 desktop application for browsing and triaging CrowdStrike Falcon Spotlight vulnerabilities across a protected fleet. It provides a live, filterable table with severity color-coding, incremental loading, in-memory view filters, CSV export with formula-injection protection, and an optional matplotlib severity breakdown chart.

The application uses a two-stage filter model: **query filters** (Search Parameters panel) generate FQL and trigger API calls, while **view filters** (severity checkboxes, CVE search, hostname, OS) operate in-memory on already-loaded records for instant filtering. API calls run on a `VulnLoader` QThread with pipelined cursor-based pagination and results are delivered incrementally via Qt signals. Hostnames are back-filled from the Hosts API after all vulnerability pages complete.

Credentials are accepted via CLI arguments, environment variables, or a runtime credential dialog. They are never written to disk.

## Running the program

In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Spotlight Vulnerabilities | __READ__ |
| Hosts | __READ__ _(used for hostname enrichment)_ |

### Execution syntax

This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown below without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

> Launch with the credential dialog (prompted at startup).

```shell
python3 spotlight_vuln_dashboard.py
```

> Launch with credentials passed via CLI flags (dialog is skipped).

```shell
python3 spotlight_vuln_dashboard.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Connect to a specific cloud region.

```shell
python3 spotlight_vuln_dashboard.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --region eu1
```

> Connect to a GovCloud tenant.

```shell
python3 spotlight_vuln_dashboard.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --region usgov1
```

#### Command-line help

Command-line help is available via the `-h` argument.

```shell
usage: spotlight_vuln_dashboard.py [-h]
                                   [--region {us1,us2,eu1,usgov1,usgov2,auto}]
                                   [-k FALCON_CLIENT_ID]
                                   [-s FALCON_CLIENT_SECRET]

Spotlight Vulnerability Dashboard — Desktop GUI.

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

options:
  -h, --help            show this help message and exit
  --region {us1,us2,eu1,usgov1,usgov2,auto}
                        Falcon cloud region (default: auto)
  -k, --falcon_client_id FALCON_CLIENT_ID
                        Falcon API client ID. Overrides the FALCON_CLIENT_ID
                        environment variable. If neither is set, the
                        credential dialog will prompt at startup.
  -s, --falcon_client_secret FALCON_CLIENT_SECRET
                        Falcon API client secret. Overrides the
                        FALCON_CLIENT_SECRET environment variable. If neither
                        is set, the credential dialog will prompt at startup.
```

### Example source code

The source code for this example can be found [here](spotlight_vuln_dashboard.py).
