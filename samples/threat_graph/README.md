![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Threat Graph examples
The examples in this folder focus on leveraging CrowdStrike's Falcon Threat Graph service collection.
- [threat_finder - Discover IOCs in your Environment](#Discover-IOCs-in-your-Environment)

## Discover IOCs in your Environment
Ingests IOCs from STIX2 formatted files and identifies if they exist within your environment using the Threat Graph API.

> [!IMPORTANT]
> This sample only accepts STIX2.x format for IOC files and ingests IP addresses (IPv4, IPv6), domain names, and hashes (MD5, SHA256).

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Threat Graph | __READ__ |
| Hosts | __READ__ |

### Execution syntax
This example accepts the following input parameters.
| Parameter | Purpose |
| :--- | :--- |
| `-d`, `--debug` | Enable API debugging. |
| `-f`, `--file` | The file containing the IOCs (STIX2 format). |
| `-o`, `--output` | File name to output results. |
| `--type` | Type of export: `csv` or `json` (default). |
| `-k`, `--client_id` | Your CrowdStrike Falcon API Client ID |
| `-s`, `--client_secret` | Your CrowdStrike Falcon API Client Secret |

Display findings in terminal.
```shell
python3 threat_finder.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f stix2_example.json
```

Export findings to JSON format.
```shell
python3 threat_finder.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f stix2_example.json -o results.json --type json
```

Export findings to CSV format.
```shell
python3 threat_finder.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f stix2_example.json -o results.csv --type csv
```

Enable API debugging.
```shell
python3 threat_finder.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f stix2_example.json -d
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 threat_finder.py -h
usage: threat_finder.py [-h] -k CLIENT_ID -s CLIENT_SECRET [-d] -f FILE [-o OUTPUT]
                        [--type {json,csv}]

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

This sample utilizes the Threat Graph service collection
to ingest IOCs, then identify if they exist within your environment.

This project only accepts STIX2.x format for the IOC file.
This project only ingests IP addresses (IPv4, IPv6), domain names, and hashes (MD5, SHA256).

USAGE EXAMPLES:
    # Display findings in terminal
    python3 threat_finder.py -k $KEY -s $SECRET -o stix2_example.json

    # Export findings to JSON
    python3 threat_finder.py -k $KEY -s $SECRET -o stix2_example.json -e json

    # Export findings to CSV
    python3 threat_finder.py -k $KEY -s $SECRET -o stix2_example.json -e csv

Creation date: 12.9.25 - alhumaw

required arguments:
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike API client ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike API client secret
  -f FILE, --file FILE  The file containing the IOCs

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging
  -o OUTPUT, --output OUTPUT
                        File name to output results.
  --type {json,csv}     Type of export: csv, json(default).
```

### Example source code
The source code for this example can be found [here](threat_finder.py).
