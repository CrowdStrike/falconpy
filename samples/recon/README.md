![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Falcon Recon samples
The examples within this folder focus on leveraging CrowdStrike's Falcon Recon API.

- [Create email monitoring rule](#create-email-monitoring-rule)

## Create email monitoring rule
Creates an email monitoring rule for a list of email addresses.

Larger lists are broken out into batches of 20.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Recon | __WRITE__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Create an email monitoring rule for a list of email addresses.

```shell
python3 email_monitoring_recon.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f addresses.csv
```

> Change your CrowdStrike region using the `-b` argument. (Only required for GovCloud users.)

```shell
python3 email_monitoring_recon.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f addresses.csv -b usgov1
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 email_monitoring_recon.py -h
usage: email_monitoring_recon.py [-h] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET [-b BASE_URL] -f FILE

Add monitoring rules for email addresses provided in a csv file (1 email address per row).

 _____     _                    ____
|  ___|_ _| | ___ ___  _ __    |  _ \ ___  ___ ___  _ __
| |_ / _` | |/ __/ _ \| '_ \   | |_) / _ \/ __/ _ \| '_ \
|  _| (_| | | (_| (_) | | | |  |  _ <  __/ (_| (_) | | | |
|_|  \__,_|_|\___\___/|_| |_|  |_| \_\___|\___\___/|_| |_|

Creation: 06.21.2022, wozboz@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike base URL (only required for GovCloud, pass usgov1)
  -f FILE, --file FILE  File with email-addresses to use as input

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API Client Secret
```

### Example source code
The source code for this example can be found [here](email_monitoring_recon.py).
