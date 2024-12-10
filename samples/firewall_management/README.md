![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Falcon Firewall Management samples
The examples within this folder focus on leveraging CrowdStrike's Falcon Firewall Management API.

- [Export firewall events](#export-firewall-events)

## Export firewall events
Exports CrowdStrike firewall events to a file.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Firewall Management | __READ__ |


### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Export firewall events.

```shell
python3 get_firewall_events.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Limit the number of events returned with the `-l` argument.

```shell
python3 get_firewall_events.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -l 500
```

> Change your CrowdStrike region using the `-b` argument. (Only required for GovCloud users.)

```shell
python3 get_firewall_events.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 get_firewall_events.py -h
usage: get_firewall_events.py [-h] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET [-b BASE_URL] [-l LIMIT]

Dump CrowdStrike Firewall events to a file.

 _______ __                           __ __
|   _   |__.----.-----.--.--.--.---.-|  |  |
|.  1___|  |   _|  -__|  |  |  |  _  |  |  |
|.  __) |__|__| |_____|________|___._|__|__|
|:  |
|::.|        ___ ___                                                    __
`---'       |   Y   .---.-.-----.---.-.-----.-----.--------.-----.-----|  |_
            |.      |  _  |     |  _  |  _  |  -__|        |  -__|     |   _|
            |. \_/  |___._|__|__|___._|___  |_____|__|__|__|_____|__|__|____|
            |:  |   |                 |_____|
            |::.|:. |                               FalconPy v1.0
            `--- ---'

Creation: 05.13.2022, wozboz@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike base URL (only required for GovCloud, pass usgov1)
  -l LIMIT, --limit LIMIT
                        FQL filter to use to filter detections

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API Client Secret
```

### Example source code
The source code for this example can be found [here](get_firewall_events.py).
