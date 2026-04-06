![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Zero Trust Assessment Score Viewer

A Dear PyGui desktop application for visualising CrowdStrike Falcon Zero Trust Assessment (ZTA) scores across your fleet.

The Dashboard tab shows a score distribution bar chart (devices per 10-point bucket) and a sortable, paginated device table displaying hostname/AID, ZTA score (colour-coded: critical 0–39, high 40–59, medium 60–79, good 80–100), OS/platform, and last seen timestamp. The Worst Offenders tab lists the 10 lowest-scoring devices. The Audit Report tab fetches and displays the aggregate ZTA audit report from `getAuditV1`. A Reconnect button re-authenticates if the token expires mid-session, and an auto-refresh selector (Off / 30s / 1m / 5m) enables periodic background data reloads.

Bucket counts are fetched independently per score range to provide accurate fleet-wide distribution regardless of how many devices are sampled in the table. Hostnames are resolved via the Hosts API (CWPP/container workload AIDs that do not resolve are shown as bare AIDs).

## Running the program

In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Zero Trust Assessment | __READ__ |
| Hosts | __READ__ _(used for hostname resolution)_ |

### Execution syntax

This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown below without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

> Launch with credentials passed via CLI flags.

```shell
python3 zta_score_viewer.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Launch using environment variables (no flags needed).

```shell
python3 zta_score_viewer.py
```

#### Command-line help

Command-line help is available via the `-h` argument.

```shell
usage: zta_score_viewer.py [-h] [-k CLIENT_ID] [-s CLIENT_SECRET]

Zero Trust Assessment Score Viewer.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |             FalconPy
`-------'                         `-------'

_____  ______   ____       _____   __   ___   ____     ___
|     T|      T /    T     / ___/  /  ] /   \ |    \   /  _]
l__/  ||      |Y  o  |    (   \_  /  / Y     Y|  D  ) /  [_
|   __jl_j  l_j|     |     \__  T/  /  |  O  ||    / Y    _]
|  /  |  |  |  |  _  |     /  \ /   \_ |     ||    \ |   [_
|     |  |  |  |  |  |     \    \     |l     !|  .  Y|     T
l_____j  l__j  l__j__j      \___j\____j \___/ l__j\_jl_____j

 __ __  ____    ___ __    __    ___  ____
|  T  |l    j  /  _]  T__T  T  /  _]|    \
|  |  | |  T  /  [_|  |  |  | /  [_ |  D  )
|  |  | |  | Y    _]  |  |  |Y    _]|    /
l  :  ! |  | |   [_l  `  '  !|   [_ |    \
 \   /  j  l |     T\      / |     T|  .  Y
  \_/  |____jl_____j \_/\_/  l_____jl__j\_j

                    Zero Trust Assessment Score Viewer
                    Uses: ZeroTrustAssessment
                    Scope: zero-trust-assessment:read

A Dear PyGui desktop application for visualising CrowdStrike Falcon
Zero Trust Assessment (ZTA) scores across your fleet.

- Bar chart showing device count per 10-point score bucket (0-9, 10-19 … 90-100)
- Sortable table: device AID prefix, full AID, ZTA score, OS/platform, last seen
- "Worst Offenders" panel: 10 lowest-scoring devices
- Refresh button + auto-refresh interval selector
- Audit tab: aggregate audit report from getAuditV1

Authentication
--------------
  Credentials are resolved in this order (first match wins):
    1. CLI flags: -k / --client_id  and  -s / --client_secret
    2. Environment variables: FALCON_CLIENT_ID / FALCON_CLIENT_SECRET

  If no credentials are found, an error dialog is shown.
  A "Reconnect" button re-authenticates if the token expires mid-session.

Usage
-----
    FALCON_CLIENT_ID=xxx FALCON_CLIENT_SECRET=yyy pipenv run python3 zta_score_viewer.py
    pipenv run python3 zta_score_viewer.py -k KEY -s SECRET

CLI flags
---------
  -k / --client_id      Falcon API client ID (overrides FALCON_CLIENT_ID env var)
  -s / --client_secret  Falcon API client secret (overrides FALCON_CLIENT_SECRET env var)

Required API scope
------------------
  zero-trust-assessment:read

options:
  -h, --help            show this help message and exit
  -k CLIENT_ID, --client_id CLIENT_ID
                        Falcon API client ID (overrides FALCON_CLIENT_ID env
                        var)
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        Falcon API client secret (overrides
                        FALCON_CLIENT_SECRET env var)
```

### Example source code

The source code for this example can be found [here](zta_score_viewer.py).
