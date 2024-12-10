![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Falcon Spotlight Vulnerabilities samples
The examples within this folder focus on leveraging CrowdStrike's Falcon Spotlight Vulnerabilities API.

- [Identify hosts with vulnerabilities by CVE](#identify-hosts-with-vulnerabilities-by-cve)
- [CISA Known exploited vulnerabilities](CISA_known_exploited_vulns)
- [Spotlight Quick Report](#spotlight-quick-report)

## Identify hosts with vulnerabilities by CVE
Retrieves a list of hosts with vulnerabilities matching the CVE(s) specified. Also provides remediation recommendations when available.

### Dependencies
This sample is dependent upon the [`python-tabulate`](https://github.com/gregbanks/python-tabulate) library.

#### Installing tabulate
Tabulate can be installed using the Python Package Index:

```shell
python3 -m pip install tabulate
```

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |
| Spotlight Vulnerabilities | __READ__ |

### Execution syntax
The following command will retrieve a list of hosts matching the specified CVE.

#### Basic usage
```shell
python3 find_hosts_by_cve.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c CVE-2021-22947
```

> You do not need to prepend the `CVE-` string to your CVE ID. Both formats are accepted.
```shell
python3 find_hosts_by_cve.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c 2021-22947
```

> You can search for multiple CVEs by passing a comma delimited string for the `-c` argument.
```shell
python3 find_hosts_by_cve.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c CVE-2021-22947,CVE-2021-36085
```

#### Excluding columns
You can exclude columns from the result display using the `-x` argument.

```shell
python3 find_hosts_by_cve.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c CVE-2021-22947 -x cve_description
```

#### Enabling the progress indicator
To show a progress indicator, use the `-p` option.

```shell
python3 find_hosts_by_cve.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c 2021-22947 -p
```

#### Changing the sort
By default, results are sorted by creation date (`created_on`). You can specify the column to sort by using the `-o` argument.

```shell
python3 find_hosts_by_cve.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c 2021-22947 -o local_ip
```

##### Available sort columns
- cve
- score
- severity
- cve_description
- created_on
- updated_on
- hostname
- local_ip
- os_version
- service_provider
- remediation

By default, results are sorted in ascending order. You can change this behavior using the `-r` argument.

```shell
python3 find_hosts_by_cve.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c 2021-22947 -o local_ip -r
```

#### Changing the tabular display format
Multiple formats are supported for displaying results. You can change format using the `-f` argument. Invalid selections are ignored.

```shell
python3 find_hosts_by_cve.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c 2021-22947 -f simple
```

##### Available table formats
- plain
- simple
- github
- grid (Default)
- fancy_grid
- pipe
- orgtbl
- jira
- presto
- pretty
- psql
- rst
- mediawiki
- moinmoin
- youtrack
- html
- unsafehtml
- latex
- latex_raw
- latex_booktabs
- latex_longtable
- textile
- tsv


#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 find_hosts_by_cve.py -h
usage: find_hosts_by_cve.py [-h] -k CLIENT_ID -s CLIENT_SECRET [-b BASE_URL] -c CVE [-x EXCLUDE] [-f FORMAT] [-o SORT] [-r] [-p]

Retrieve hosts by CVE vulnerability.

 ______                         __ _______ __         __ __
|      |.----.-----.--.--.--.--|  |     __|  |_.----.|__|  |--.-----.
|   ---||   _|  _  |  |  |  |  _  |__     |   _|   _||  |    <|  -__|
|______||__| |_____|________|_____|_______|____|__|  |__|__|__|_____|
                     _______             __   __ __       __    __
                    |   _   .-----.-----|  |_|  |__.-----|  |--|  |_
                    |   1___|  _  |  _  |   _|  |  |  _  |     |   _|
                    |____   |   __|_____|____|__|__|___  |__|__|____|
                    |:  1   |__|                   |_____|
                    |::.. . |
                    `-------'               Find hosts by CVE

Creation date: 01.13.2021 - jshcodes@CrowdStrike

This solution requires the crowdstrike-falconpy (v0.8.6+) and tabulate packages.
    python3 -m pip install crowdstrike-falconpy tabulate

Required API scopes
    Hosts: READ
    Spotlight: READ

optional arguments:
  -h, --help            show this help message and exit
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API key secret
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike API region (us1, us2, eu1, usgov1)
                        NOT required unless you are using `usgov1`
  -c CVE, --cve CVE     CVE IDs to search for. (ex: CVE-2022-12345,CVE-2022-54321)
                        Delimit with a comma (no spaces). The string CVE- is not required.
  -x EXCLUDE, --exclude EXCLUDE
                        List of columns to exclude from the display.
                        Delimit with a comma (no spaces).
                        (cve, score, severity, cve_description, created_on, updated_on,
                        hostname, local_ip, os_version, service_provider, remediation)
  -f FORMAT, --format FORMAT
                        Table format to use for display.
                        (plain, simple, github, grid, fancy_grid, pipe, orgtbl, jira, presto,
                        pretty, psql, rst, mediawiki, moinmoin, youtrack, html, unsafehtml,
                        latext, latex_raw, latex_booktabs, latex_longtable, textile, tsv)
  -o SORT, --sort SORT  Sort results by display column.
                        (cve, score, severity, cve_description, created_on, updated_on,
                        hostname, local_ip, os_version, service_provider, remediation)
  -r, --reverse         Reverse the sort direction.
  -p, --show_progress   Show a progress indicator as data is retrieved.
```

### Example source code
The source code for this example can be found [here](find_hosts_by_cve.py).

## Spotlight Quick Report
Produce a quick report of CVE vulnerabilities discovered within your Falcon tenant.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |
| Spotlight Vulnerabilities | __READ__ |

### Execution syntax
The following command will generate a Spotlight quick report based upon the details available within your tenant.

#### Basic usage
```shell
python3 spotlight_quick_report.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

#### Saving results
Output the results of the report to JSON format using the `-o` argument.

```shell
python3 spotlight_quick_report.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -o report.json
```

#### Reviewing saved results
You can consume a saved report and print the results using the `-f` argument.

```shell
python3 spotlight_quick_report.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f report.json
```

#### Adjusting the date range
Specify the number of days backwards in time to check using the `-d` argument.

```shell
python3 spotlight_quick_report.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d 5
```

#### Duplicates
If you wish to allow duplicate matches to be present within your report, pass the `-a` argument.

```shell
python3 spotlight_quick_report.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -a
```
#### Debugging
If you want to debug code and quickly find errors within code `--debug` argument.

```shell
python3 spotlight_quick_report.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --debug
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 spotlight_quick_report.py -h
usage: spotlight_quick_report.py [-h] -k CLIENT_ID -s CLIENT_SECRET [-d DAYS] [-f FILE] [-o OUTPUT] [-a]

Spotlight results quick report generator.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |      FalconPy SDK
`-------'                         `-------'

       ____          __  ___      __   __
      / __/__  ___  / /_/ (_)__ _/ /  / /_
     _\ \/ _ \/ _ \/ __/ / / _ `/ _ \/ __/
    /___/ .__/\___/\__/_/_/\_, /_//_/\__/
       /_/                /___/
          ____       _     __     ___                    __
         / __ \__ __(_)___/ /__  / _ \___ ___  ___  ____/ /_
        / /_/ / // / / __/  '_/ / , _/ -_) _ \/ _ \/ __/ __/
        \___\_\_,_/_/\__/_/\_\ /_/|_|\__/ .__/\___/_/  \__/
                                       /_/

This example requires crowdstrike-falconpy v1.2.2 or greater.

Easy Object Authentication is also demonstrated in this sample.

optional arguments:
  -h, --help            show this help message and exit
  -d DAYS, --days DAYS  Include days from X days backwards (3-45).
  -f FILE, --file FILE  File to import data from.
                        Data is queried from the API if this argument is not provided.
  -o OUTPUT, --output OUTPUT
                        File to output results to.
                        Output is not performed if this argument is not provided.
  -a, --allow_dupes     Allow duplicates.

required arguments:
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API Client ID.
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API Client Secret.
  --debug               Enables code debugging 
```

### Example source code
The source code for this example can be found [here](spotlight_quick_report.py).
