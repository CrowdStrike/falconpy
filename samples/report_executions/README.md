![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Falcon Report Executions samples
The examples within this folder focus on leveraging CrowdStrike's Falcon Report Executions API.

- [Download all report runs](#download-all-report-runs)

## Download all report runs
Accepts a scheduled report ID and then downloads all successful results from all runs of the report.
Reports are downloaded in either JSON or CSV format depending on report configuration.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Report Executions | __READ__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Download all reports for a specific report ID

```shell
python3 get_report_results.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -r REPORT_ID
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 get_report_results.py -h
usage: get_report_results.py [-h] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET -r REPORT

Retrieve the contents of a scheduled report and save it to a file.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |      FalconPy SDK
`-------'                         `-------'

 _______        __             __         __           __
|     __|.----.|  |--.-----.--|  |.--.--.|  |.-----.--|  |
|__     ||  __||     |  -__|  _  ||  |  ||  ||  -__|  _  |
|_______||____||__|__|_____|_____||_____||__||_____|_____|

             ______                          __
            |   __ \.-----.-----.-----.----.|  |_.-----.
            |      <|  -__|  _  |  _  |   _||   _|__ --|
            |___|__||_____|   __|_____|__|  |____|_____|
                          |__|

____ ____ ____ _  _ _    ___ ____    ___  ____ _ _ _ _  _ _    ____ ____ ___  ____ ____
|__/ |___ [__  |  | |     |  [__     |  \ |  | | | | |\ | |    |  | |__| |  \ |___ |__/
|  \ |___ ___] |__| |___  |  ___]    |__/ |__| |_|_| | \| |___ |__| |  | |__/ |___ |  \

Accepts a Scheduled Report ID and downloads every successful execution result.

Files are saved as [REPORT ID]_[EXECUTION ID].rpt in JSON format.

Requires the Report Executions: READ scope

Creation date: 10.26.22 - jshcodes@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit

required_arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike API Client Secret
  -r REPORT, --report REPORT
                        ID of the report to retrieve
```

### Example source code
The source code for these examples can be found [here](get_report_results.py):
