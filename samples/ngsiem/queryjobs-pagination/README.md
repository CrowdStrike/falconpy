![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# QueryJobs API Pagination

Retrieves all results from an NG-SIEM QueryJob using cursor-based pagination via the `around` parameter. The QueryJobs API returns a **200-event result buffer** for filter (non-aggregate) queries; this script automatically paginates through all matching events.

- [ngsiem_queryjob_paginator.py - QueryJob Paginator](#queryjob-paginator)

## QueryJob Paginator

Paginates through NG-SIEM QueryJob results by creating successive cursor-anchored queries. Deduplicates events at page boundaries and writes consolidated results to a JSON file.

> [!IMPORTANT]
> This sample requires CrowdStrike API credentials with **NGSIEM: Read + Write** scope.

### How it works

1. **Create** a QueryJob and poll until done
2. **Collect** the initial 200-event buffer
3. If `hasMoreEvents="true"`, **anchor** on the oldest event and create a new QueryJob with `around` to walk backward through time
4. **Repeat** until no new events are returned, deduplicating at each boundary

### Running the program

In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| NGSIEM | __READ__, __WRITE__ |

### Execution syntax

This sample leverages simple command-line arguments to implement functionality.

#### Basic usage

Set credentials via environment variables or command-line flags:

```shell
export FALCON_CLIENT_ID="your-client-id"
export FALCON_CLIENT_SECRET="your-client-secret"

python3 ngsiem_queryjob_paginator.py -q '#event_simpleName=ProcessRollup2'
```

Specify a time range and repository:

```shell
python3 ngsiem_queryjob_paginator.py -q '#event_simpleName=ProcessRollup2' -r search-all --start 1h --end now
```

Target a specific cloud region:

```shell
python3 ngsiem_queryjob_paginator.py -q '#event_simpleName=ProcessRollup2' -b https://api.us-2.crowdstrike.com
```

MSSP / Flight Control — query a child CID:

```shell
python3 ngsiem_queryjob_paginator.py -q '#event_simpleName=ProcessRollup2' -m CHILD_CID
```

Limit results and write to a custom output file:

```shell
python3 ngsiem_queryjob_paginator.py -q '#event_simpleName=ProcessRollup2' --max-events 5000 -o results.json
```

#### Command-line help

Command-line help is available via the `-h` argument.

```shell
python3 ngsiem_queryjob_paginator.py -h
```

#### Parameters

| Flag | Env Var | Description | Default |
| :---- | :---- | :---- | :---- |
| `-k, --client-id` | `FALCON_CLIENT_ID` | OAuth2 client ID (required) | — |
| `-s, --client-secret` | `FALCON_CLIENT_SECRET` | OAuth2 client secret (required) | — |
| `-q, --query` | — | CQL query string (required) | — |
| `-r, --repo` | — | NG-SIEM repository | `search-all` |
| `--start` | — | Start time | `15m` |
| `--end` | — | End time | `now` |
| `-o, --output` | — | Output JSON file | `ngsiem_queryjob_results.json` |
| `--max-events` | — | Max events to retrieve | unlimited |
| `--page-size` | — | Events per cursor page | `200` |
| `-b, --base-url` | `FALCON_BASE_URL` | CrowdStrike API base URL | US-1 |
| `-m, --member-cid` | `FALCON_MEMBER_CID` | Child CID (MSSP / flight control) | — |

#### Available repositories

`search-all`, `investigate_view`, `third-party`, `falcon_for_it_view`, `forensics_view`

### SSL / Corporate Proxy

For Zscaler or corporate proxy environments, set the `CA_BUNDLE` environment variable pointing to your CA certificate bundle. The script reads this and passes it as `ssl_verify` to FalconPy. If unset, SSL verification is enabled by default.

```shell
export CA_BUNDLE="/path/to/ca-bundle.pem"
```

### Example source code

The source code for this example can be found [here](ngsiem_queryjob_paginator.py).
