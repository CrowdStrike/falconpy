![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# ODS Manager

A wxPython desktop application for managing CrowdStrike Falcon On-Demand Scans — launch agent-side AV scans, monitor progress, inspect per-host results, and cancel scan jobs.

The main window shows a colour-coded scan job list with 15-second auto-polling for active scans. Selecting a scan loads a per-host progress grid and a findings summary panel. The New Scan dialog provides a searchable live host list (populated from the Hosts API), file path management with add/remove controls, optional glob-pattern exclusions, CPU priority, and quarantine settings. If a scan submission fails, the dialog re-opens with all previously entered values preserved.

> **Note:** The Falcon ODS API does not provide an endpoint to delete on-demand scan records. The **Delete Selected** toolbar button explains this limitation and offers to cancel active scans instead.

## Running the program

In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| On-Demand Scans (ODS) | __READ__, __WRITE__ |
| Hosts | __READ__ _(used to populate the host selector in the New Scan dialog)_ |

### Execution syntax

This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown below without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

> Launch with credentials passed via CLI flags.

```shell
python3 ods_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Launch using environment variables (no flags needed).

```shell
python3 ods_manager.py
```

#### Command-line help

Command-line help is available via the `-h` argument.

```shell
usage: ods_manager.py [-h] [-k CLIENT_ID] [-s CLIENT_SECRET]

On-Demand Scan (ODS) Manager.

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

options:
  -h, --help            show this help message and exit
  -k CLIENT_ID, --client-id CLIENT_ID
                        Falcon API client ID (overrides FALCON_CLIENT_ID env
                        var)
  -s CLIENT_SECRET, --client-secret CLIENT_SECRET
                        Falcon API client secret (overrides
                        FALCON_CLIENT_SECRET env var)

Credentials can also be provided via environment variables:
  FALCON_CLIENT_ID      API client ID
  FALCON_CLIENT_SECRET  API client secret

CLI arguments take precedence over environment variables.
```

### Example source code

The source code for this example can be found [here](ods_manager.py).
