![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# NG-SIEM samples
The examples within this folder focus on leveraging CrowdStrike Falcon Next-Gen SIEM and the NGSIEM service collection.

- [What the HEC?](#what-the-hec)
- [QueryJob Paginator](#queryjob-paginator)

## What the HEC?
This sample discusses ingestion into Falcon Next-Gen SIEM. The solution demonstrates singular, list, file and raw ingest. Events can be randomly generated or provided via a file.

> [!IMPORTANT]
> This solution demonstrates ingestion but does not discuss parsing. Parsers should be developed specifically to handle the data being ingested.
> More information regarding parsers can be found by navigating to Support and Resources -> Documentation in the Falcon console and selecting "Falcon Next-Gen SIEM".

### Running the program
In order to run this demonstration, you you will need to create a _HEC / HTTP Event Connector_ data connection within the Falcon Console (Next-Gen SIEM).
The API and URL key associated with this data connection will be required to successfully ingest data.

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Ingest one thousand randomly generated JSON formatted events.

```shell
python3 what_the_hec.py -u $NGSIEM_URL_KEY -a $NGSIEM_API_KEY -g -n 1000 -f json
```

Debugging can be enabled using the `-d` argument.

```shell
python3 what_the_hec.py -u $NGSIEM_URL_KEY -a $NGSIEM_API_KEY -g -n 1000 -f json -d
```

Enable a progress indicator using the `-p` argument.

```shell
python3 what_the_hec.py -u $NGSIEM_URL_KEY -a $NGSIEM_API_KEY -g -n 1000 -f json -p
```

Ingest events as a list.

```shell
python3 what_the_hec.py -u $NGSIEM_URL_KEY -a $NGSIEM_API_KEY -g -n 1000 -l
```

Ingest a file containing events.

```shell
python3 what_the_hec.py -u $NGSIEM_URL_KEY -a $NGSIEM_API_KEY -fn testfile.json -f json
```

#### Advanced usage

Process events asynchronously with fifty threads.

```shell
python3 what_the_hec.py -u $NGSIEM_URL_KEY -a $NGSIEM_API_KEY -g -n 1000 -l -tc 50
```

Ingest a raw file of events.

```shell
python3 what_the_hec.py -u $NGSIEM_URL_KEY -a $NGSIEM_API_KEY -fn raw_file.json -f json -r
```

Adjust the timeout for API response.

```shell
python3 what_the_hec.py -u $NGSIEM_URL_KEY -a $NGSIEM_API_KEY -g -n 100000 -f json -to 30
```


#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: what_the_hec.py [-h] [-t] [-tc THREADS] [-as] [-p] [-s] [-l] [-n NUMBER] [-j | -r] [-fn FILENAME] [-g] [-w] -a NGSIEM_API_KEY -u NGSIEM_URL_KEY
                       [-f {json,csv,yaml,xml}] [-c {us1,us2,eu1,gov1}] [-tu {seconds,milliseconds,nanoseconds}] [-to TIMEOUT] [-rc RETRY_COUNT] [-d] [-df DEBUGFILE] [-cl]
                       [--no_sanitize]

FalconPy NG-SIEM HEC tester and event simulator.

██╗    ██╗██╗  ██╗ █████╗ ████████╗    ████████╗██╗  ██╗███████╗
██║    ██║██║  ██║██╔══██╗╚══██╔══╝    ╚══██╔══╝██║  ██║██╔════╝
██║ █╗ ██║███████║███████║   ██║          ██║   ███████║█████╗
██║███╗██║██╔══██║██╔══██║   ██║          ██║   ██╔══██║██╔══╝
╚███╔███╔╝██║  ██║██║  ██║   ██║          ██║   ██║  ██║███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝          ╚═╝   ╚═╝  ╚═╝╚══════╝

                ██╗  ██╗███████╗ ██████╗██████╗ ██╗
                ██║  ██║██╔════╝██╔════╝╚════██╗██║
                ███████║█████╗  ██║       ▄███╔╝██║
                ██╔══██║██╔══╝  ██║       ▀▀══╝ ╚═╝
                ██║  ██║███████╗╚██████╗  ██╗   ██╗
                ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═╝   ╚═╝

                                                🦅 FalconPy v1.5.1

This sample simulates events and imports them into a CrowdStrike Falcon NGSIEM tenant.

The sample can be used to demonstrate importing standard JSON events and raw new line
delimited JSON, XML and CSV files. This sample is intended to provide developers with a
starting point to begin working with the HTTP event collector that is provided by the
CrowdStrike FalconPy library.

Creation date: 05.02.2025 - jshcodes@CrowdStrike

██  ███ █ █ ███ █   ███ ███ ███ ███   █   █ ███ ███ ███
█ █ █   █ █ █   █   █ █ █ █ █   █ █   ██  █ █ █  █  █
█ █ ███ █ █ ███ █   █ █ ███ ███ ██    █ █ █ █ █  █  ███
█ █ █   █ █ █   █   █ █ █   █   █ █   █  ██ █ █  █  █
██  ███  █  ███ ███ ███ █   ███ █ █   █   █ ███  █  ███

This solution demonstrates HTTP event ingestion, but does not discuss parsing. Parsers
should be developed specifically to handle the data being ingested. More information
regarding parsers can be found by navigating to Support and Resources -> Documentation
in the Falcon console and selecting "Falcon Next-Gen SIEM".

options:
  -h, --help            show this help message and exit
  -t, --test_connection
                        Run API connectivity test

asynchronous processing configuration:
  -tc, --threads THREADS
                        Set the number of asynchronous threads to use (applies to single [-as], list and json file processing)
  -as, --asynchronous   Run single event simulation asynchronously (applies to single processing only)
  -p, --progress        Show asynchronous progress (applies to list and json processing only)

event simulation configuration:
  -s, --single          Import simulated events individually
  -l, --list            Import a list of simulated events
  -n, --number NUMBER   Number of host messages to simulate (applies to single and list processing only)

file import configuration:
  -j, --json            Import a JSON file of events
  -r, --raw             Import a raw file of events
  -fn, --filename FILENAME
                        Filename to import
  -g, --generate_file   Generate the raw file to be loaded (raw import only)
  -w, --wrap            Disable wrapping of individual events with an event delimiter.
                        CSV formatting does not support event wrapping.
                        XML documents without a root element are not considered well-formed.

ingest configuration:
  -a, --ngsiem_api_key NGSIEM_API_KEY
                        CrowdStrike Falcon NGSIEM API key
  -u, --ngsiem_url_key NGSIEM_URL_KEY
                        CrowdStrike Falcon NGSIEM URL key
  -f, --format {json,csv,yaml,xml}
                        Ingest format
                        Defaults to "json"
  -c, --cloud_region {us1,us2,eu1,gov1}
                        CrowdStrike Falcon cloud region
                        Defaults to "us1"
  -tu, --timeunit {seconds,milliseconds,nanoseconds}
                        Set the time unit used for timestamps
                        Defaults to "nanoseconds"
  -to, --timeout TIMEOUT
                        Set the request timeout
  -rc, --retry_count RETRY_COUNT
                        Set the request retry count

logging configuration:
  -d, --debug           Enable API debugging
  -df, --debugfile DEBUGFILE
                        Write debug logs to a file
  -cl, --clear_log      Clear the debug log file before processing
  --no_sanitize         Disable log sanitization
```

### Example source code
The source code for this example can be found [here](what_the_hec.py).

## QueryJob Paginator
Paginates through NG-SIEM QueryJob results by creating successive cursor-anchored queries. The QueryJobs API returns a **200-event result buffer** for filter (non-aggregate) queries. This script automatically walks through all matching events using the `around` parameter, deduplicating at page boundaries, and writes consolidated results to a JSON file.

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

#### SSL / Corporate Proxy
For Zscaler or corporate proxy environments, set the `CA_BUNDLE` environment variable pointing to your CA certificate bundle. The script reads this and passes it as `ssl_verify` to FalconPy. If unset, SSL verification is enabled by default.

```shell
export CA_BUNDLE="/path/to/ca-bundle.pem"
```

### Example source code
The source code for this example can be found [here](ngsiem_queryjob_paginator.py).
