![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Alerts examples
The examples in this folder focus on leveraging CrowdStrike's Falcon Alerts service collection.
- [alert_manager - Query and Manage Security Alerts](#Query-and-Manage-Security-Alerts)
- [Alerts Triage Dashboard](alerts_triage) - PyQt6 desktop GUI for triaging behavioral alerts with severity color-coding, bulk status updates, and progressive loading.

## Query and Manage Security Alerts
Query, retrieve, and manage security alerts from your CrowdStrike Falcon environment. This sample provides functionality to list alerts with filters, view detailed alert information, update alert statuses, and export results.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Alerts | __READ__, __WRITE__ |

### Execution syntax
This example accepts the following input parameters.
| Parameter | Purpose |
| :--- | :--- |
| `-d`, `--debug` | Enable API debugging. |
| `-l`, `--list` | List alerts (mutually exclusive with --view and --update). |
| `-v`, `--view` | View specific alert by composite ID (mutually exclusive with --list and --update). |
| `-u`, `--update` | Update alert by composite ID (mutually exclusive with --list and --view). |
| `-f`, `--filter` | FQL filter string to narrow results. |
| `--status` | New status when updating (new, in_progress, reopened, closed, ignored). |
| `-e`, `--export` | Export results to JSON file (optionally specify filename). |
| `--limit` | Maximum number of alerts to return (default: 100). |
| `-a`, `--all` | Fetch all alerts with automatic pagination (ignore limit). |
| `-k`, `--client_id` | Your CrowdStrike Falcon API Client ID |
| `-s`, `--client_secret` | Your CrowdStrike Falcon API Client Secret |

List alerts with a filter.
```shell
python3 alert_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --list --filter "product:'automated-lead'"
```

View specific alert details.
```shell
python3 alert_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --view <composite_id>
```

Update alert status.
```shell
python3 alert_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --update <composite_id> --status closed
```

Export high severity alerts to JSON with custom filename.
```shell
python3 alert_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --list --filter "severity:'High'" --export alerts.json
```

Fetch all alerts with automatic pagination.
```shell
python3 alert_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --list --all
```

Identify CAP_SYS_ADMIN alerts for vulnerable containers.
```shell
python3 alert_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --filter "description:*'*CAP_SYS_ADMIN*'" --list
```

Enable API debugging.
```shell
python3 alert_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --list -d
```

#### Command-line help
Command-line help is available using the `-h` or `--help` parameters.

```shell
python3 alert_manager.py -h
usage: alert_manager.py [-h] -k CLIENT_ID -s CLIENT_SECRET [-d] (-l | -v COMPOSITE_ID | -u COMPOSITE_ID)
                        [-f FILTER] [--status STATUS] [-e [FILENAME]] [--limit LIMIT] [-a]

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

This sample utilizes the Alerts service collection
to query, retrieve, and manage security alerts.

USAGE EXAMPLES:
    # List alerts with filter
    python3 alert_manager.py -k $KEY -s $SECRET --list --filter "product:'automated-lead'"

    # View specific alert details
    python3 alert_manager.py -k $KEY -s $SECRET --view <composite_id>

    # Update alert status
    python3 alert_manager.py -k $KEY -s $SECRET --update <composite_id> --status closed

    # Export to JSON with custom filename
    python3 alert_manager.py -k $KEY -s $SECRET --list --filter "severity:'High'" --export alerts.json

    # Fetch all alerts (with pagination)
    python3 alert_manager.py -k $KEY -s $SECRET --list --all

    # Identify CAP_SYS_ADMIN alerts for vulnerable containers
    python3 alert_manager.py -k $KEY -s $SECRET --filter "description:*'*CAP_SYS_ADMIN*'" -l

Creation date: 12.4.25 - alhumaw

required arguments:
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike API client ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike API client secret

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging
  -l, --list            List alerts
  -v COMPOSITE_ID, --view COMPOSITE_ID
                        View specific alert by composite ID
  -u COMPOSITE_ID, --update COMPOSITE_ID
                        Update alert by composite ID
  -f FILTER, --filter FILTER
                        FQL filter string
  --status STATUS       New status when updating:
                          Strings: new, in_progress, reopened, closed, ignored
                          Numbers: 20 (new), 25 (reopened), 30 (in_progress), 40 (closed)
  -e [FILENAME], --export [FILENAME]
                        Export results to JSON file (optionally specify filename)
  --limit LIMIT         Maximum number of alerts to return (default: 100)
  -a, --all             Fetch all alerts (ignore limit)
```

### Example source code
The source code for this example can be found [here](alert_manager.py).
