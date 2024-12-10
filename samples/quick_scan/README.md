![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Quick Scan examples
The examples within this folder focus on leveraging CrowdStrike's Falcon Quick Scan API.

- [Quota Check](#quota-check)
- [Sandbox / Quick Scan demo](#sandbox--quick-scan-demo)

## Quota Check
Displays your current Quick Scan quota.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Quick Scan | __READ__ |

### Execution syntax
You may provide your API keys to this application via the command line (`-k` and `-s`) or by setting
the `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` environment variables.

#### Basic usage
Display your current scan quota usage.

> Retrieving keys using environment variables

```shell
python3 quota_check.py
```

> Providing keys at runtime using the command line

```shell
python3 quota_check.py -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 quota_check.py -h
usage: quota_check.py [-h] [-k FALCON_CLIENT_ID] [-s FALCON_CLIENT_SECRET]

Get Quick Scan quota.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |      FalconPy v1.2.12
`-------'                         `-------'

   ___                  .                  ___  _                    \
 .'   `.  ,   .   __.  _/_     ___       .'   \ /        ___    ___  |   ,
 |     |  |   | .'   \  |     /   `      |      |,---. .'   ` .'   ` |  /
 |  ,_ |  |   | |    |  |    |    |      |      |'   ` |----' |      |-<
  `._.`-. `._/|  `._.'  \__/ `.__/|       `.__, /    | `.___,  `._.' /  \_

Checks your current Quick Scan quota and returns the results.

You must provide your API credentials to this application via the
command line or by setting the following two environment variables:
    FALCON_CLIENT_ID
    FALCON_CLIENT_SECRET

Creation date: 03.10.23 - jshcodes@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API Client secret
```

### Example source code
The source code for this example can be found [here](quota_check.py).

## Sandbox / Quick Scan demo
This is a proof of concept example. Extensive performance testing has not been performed against this code example.

### Dependencies
+ boto3
+ crowdstrike-falconpy 0.4.5+

```shell
python3 -m pip install boto3 crowdstrike-falconpy
```

#### Example config.json file:
```json
{
    "falcon_client_id": "API ID GOES HERE",
    "falcon_client_secret": "API SECRET GOES HERE"
}
```

### Notes
+ A **VOLUME** is a collection of files that are uploaded and then scanned as a singular batch.
+ The log file rotates to prevent file system bloat.

### Local Directory scanning
+ The folder is inventoried and then files are uploaded to the API in a linear fashion.
+ This method is impacted by data transfer speeds from the source file system location to CrowdStrike's cloud. 
+ Supports pattern matching to filter objects scanned using the "--pattern" or "-p" command line parameter.

### S3 Bucket scanning
+ The bucket contents are inventoried, and then the contents are downloaded to local memory and 
uploaded to the Sandbox API in a linear fashion. 
+ This method does NOT store the files on the local file system. 
+ Due to the nature of this solution, the method is heavily impacted by data transfer speeds. 
    - Recommended deployment pattern involves running in AWS within a container, an EC2 instance or as a serverless lambda. 
+ Currently scans the entire bucket only. 
+ You must specify a target that includes the string "s3://" in order to scan a bucket.


### Alpha testing
This solution has been tested on Python 3.7 / 3.9 running under Amazon Linux 2 and MacOS 10.15.

### Example source code
The source code for this example can be found [here](scan_target.py).
