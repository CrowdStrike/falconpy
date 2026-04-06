![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Alerts Triage Dashboard

A PyQt6 desktop application for triaging CrowdStrike Falcon behavioral alerts. It retrieves alerts from the Falcon platform using the FalconPy SDK and presents them in a split-pane interface with a severity-color-coded alert table on the left and a detail panel on the right.

The application features a filter bar with FQL input, severity and status dropdowns, and a configurable time-window selector. Alerts are fetched on a background `QThread` to keep the UI fully responsive during API calls. Results are delivered progressively — the table populates as each page arrives, and a **Next** button on the last page fetches additional batches from the API when more results exist. After a bulk status update the table cells refresh in-place without a full API re-query. The application uses the Fusion style with a dark palette.

> **Note:** The `alerts:write` scope is only required if you intend to update alert status or assignee. Read-only use requires `alerts:read` only.

## Running the program

In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Alerts | __READ__ |
| Alerts | __WRITE__ _(optional — required for bulk status/assignee updates)_ |

### Execution syntax

This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown below without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

> Launch with credentials passed via CLI flags.

```shell
python3 alerts_triage.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Launch using environment variables (no flags needed).

```shell
python3 alerts_triage.py
```

#### Command-line help

Command-line help is available via the `-h` argument.

```shell
usage: alerts_triage.py [-h] [-k CLIENT_ID] [-s CLIENT_SECRET]

Alerts Triage Dashboard — CrowdStrike Falcon

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

The source code for this example can be found [here](alerts_triage.py).
