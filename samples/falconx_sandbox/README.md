![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Falcon Intelligence Sandbox examples
The examples within this folder focus on leveraging CrowdStrike's Falcon Intelligence Sandbox and Sample Uploads APIs to analyze potential malware in different environments.

- [Analyze a single file](single_scan)
- [Retrieve all artifacts for all Falcon Intelligence reports](#retrieve-all-artifacts-for-all-falcon-intelligence-reports)

## Analyze a single file using Falcon Intelligence sandbox
Documentation for the single file scan samples can be found [here](single_scan).

## Retrieve all artifacts for all Falcon Intelligence reports
Downloads all artifacts for all Falcon Intelligence reports.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Falcon Intelligence Sandbox | __READ__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Download all report artifacts.

```shell
python3 get_all_artifacts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> GovCloud users can change their CrowdStrike region using the `-b` argument.

```shell
python3 get_all_artifacts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 get_all_artifacts.py -h
usage: get_all_artifacts.py [-h] -k CLIENT_ID -s CLIENT_SECRET [-b BASE_URL]

Retrieve all artifacts from all available Falcon X reports.

 _______       __
|   _   .---.-|  .----.-----.-----.
|.  1___|  _  |  |  __|  _  |     |
|.  __) |___._|__|____|_____|__|__|
|:  |
|::.|
`---'
 ___       __         __ __ __
|   .-----|  |_.-----|  |  |__.-----.-----.-----.----.-----.
|.  |     |   _|  -__|  |  |  |  _  |  -__|     |  __|  -__|
|.  |__|__|____|_____|__|__|__|___  |_____|__|__|____|_____|
|:  |                         |_____|
|::.|
`---'                               CrowdStrike FalconPy

Creation date: 01.12.2021 - jshcodes@CrowdStrike

You will need the following scopes on your API keys:
    Falcon Intelligence Sandbox: READ, WRITE

optional arguments:
  -h, --help            show this help message and exit
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API key secret
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike API region (us1, us2, eu1, usgov1) NOT required unless you are using `usgov1`
```

### Example source code
The source code for this example can be found [here](get_all_artifacts.py).
