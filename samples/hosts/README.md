![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)

![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)

# Hosts examples
The examples in this folder focus on leveraging CrowdStrike's Hosts API to perform administrative operations.
- [List sensor versions by Hostname](#list-sensors-by-hostname)
- [List (and optionally remove) stale sensors](#list-stale-sensors)
- [Match usernames to Hosts](#match-usernames-to-hosts)
- [Offset vs. Offset Tokens](#comparing-querydevicesbyfilter-and-querydevicesbyfilterscroll-offset-vs-token)

## List sensors by hostname
Loops through all hosts and displays the hostname and sensor version.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |

### Execution syntax
This example requires no input parameters.

```shell
python3 sensor_versions_by_hostname.py
```

### Example source code
The source code for this example can be found [here](sensor_versions_by_hostname.py).

---

## List stale sensors
Retrieves a list of hosts that have not been seen since the number of days specified. Can optionally hide the hosts identified.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__, __WRITE__ |

### Execution syntax
The following command will retrieve a list of hosts that haven't checked in to CrowdStrike in 30 days or more.

```shell
python3 stale_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d 30
```

This variation will retrieve a list of hosts that haven't checked in to CrowdStrike in 30 days or more that have the tag `testtag`.

```shell
python3 stale_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d 30 -g testtag
```

You can reverse the list sort with the `-r` or `--reverse` argument.

```shell
python3 stale_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d 30 --reverse
```

The following command will hide any hosts that haven't checked in to CrowdStrike in 30 days or more. You may also use `-x` to accomplish this.
```shell
python3 stale_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d 30 --remove
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
% python3 stale_sensors.py -h
usage: stale_sensors.py [-h] -k CLIENT_ID -s CLIENT_SECRET [-m MSSP] [-b BASE_URL] [-d DAYS] [-r] [-x] [-g GROUPING_TAG]

         _______ ___ ___ _______ _______ _______ ______
        |   _   |   Y   |   _   |   _   |   _   |   _  \
        |.  1___|.  |   |   1___|   1___|.  1___|.  |   \
        |.  |___|.  |   |____   |____   |.  __)_|.  |    \
        |:  1   |:  1   |:  1   |:  1   |:  1   |:  1    /
        |::.. . |::.. . |::.. . |::.. . |::.. . |::.. . /
        `-------`-------`-------`-------`-------`------'

    CrowdStrike Unattended Stale Sensor Environment Detector


optional arguments:
  -h, --help            show this help message and exit
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API key secret
  -m MSSP, --mssp MSSP  Child CID to access (MSSP only)
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike API region (us1, us2, eu1, usgov1) NOT required unless you are using `usgov1`
  -d DAYS, --days DAYS  Number of days since a host was seen before it is considered stale
  -r, --reverse         Reverse sort (defaults to ASC)
  -x, --remove          Remove hosts identified as stale
  -g GROUPING_TAG, --grouping_tag GROUPING_TAG
                        Falcon Grouping Tag name for the hosts
```

### Example source code
The source code for this example can be found [here](stale_sensors.py).

---

## Match usernames to hosts
Submitted by `@micgoetz`, this example demonstrates leveraging the [QueryDeviceLoginHistory](https://www.falconpy.io/Service-Collections/Hosts.html#querydeviceloginhistory) method to identify the most common username for hosts within a Falcon tenant. Hosts are then tagged with a Falcon Grouping Tag to reflect this identified user.

### Running the program.
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__, __WRITE__ |

### Execution syntax

Generic execution.

```shell
python3 match_username_to_hosts.py -c APIClientID -s APISecretID
```

Test the results of execution without taking action.

```shell
python3 match_username_to_hosts.py -c APIClientID -s APISecretID -t
```

Load a username to host mapping file.

```shell
python3 match_username_to_hosts.py -c APIClientID -s APISecretID -i PathToMyCSV.csv -t
```

Remove grouping tags set by this routine.

```shell
python3 match_username_to_hosts.py -c APIClientID -s APISecretID -r
```

Change your BASE_URL to point to GovCloud.

```shell
python3 match_username_to_hosts.py -c APIClientID -s APISecretID -b usgov1
```

### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: match_username_to_host.py [-h] -c CLIENT_ID -s CLIENT_SECRET [-b BASE_URL] [-m MSSP] [-i INPUT_FILE] [-t] [-r]

Identify usernames for specific hosts.

                                                                  88                                  88  88
                                                                  88               ,d                 ""  88
                                                                  88               88                     88
 ,adPPYba,  8b,dPPYba,   ,adPPYba,   8b      db      d8   ,adPPYb,88  ,adPPYba,  MM88MMM  8b,dPPYba,  88  88   ,d8   ,adPPYba,
a8"     ""  88P'   "Y8  a8"     "8a  `8b    d88b    d8'  a8"    `Y88  I8[    ""    88     88P'   "Y8  88  88 ,a8"   a8P_____88
8b          88          8b       d8   `8b  d8'`8b  d8'   8b       88   `"Y8ba,     88     88          88  8888[     8PP"
"8a,   ,aa  88          "8a,   ,a8"    `8bd8'  `8bd8'    "8a,   ,d88  aa    ]8I    88,    88          88  88`"Yba,  "8b,   ,aa
 `"Ybbd8"'  88           `"YbbdP"'       YP      YP       `"8bbdP"Y8  `"YbbdP"'    "Y888  88          88  88   `Y8a  `"Ybbd8"'

Created: 05/08/2022, micgoetz@CrowdStrike
Updated: 05/24/2022, micgoetz@CrowdStrike

This script will grab ALL (max 5000) of your CrowdStrike-installed devices and auto-tag each one based upon the most common
username seen. Or, provide a csv file with hosts and usernames you want to tag each with.

Most common username is determined by looking at the last 10 logins.

Requires: crowdstrike-falconpy
    python3 -m pip install crowdstrike-falconpy

This program requires your:
    - API Client ID
    - API Secret ID

With permissions:
    Hosts: Read + Write

optional arguments:
  -h, --help            show this help message and exit
  -c CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API key secret
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike API region (us1, us2, eu1, usgov1). NOT required unless you are using `usgov1`.
  -m MSSP, --mssp MSSP  Child CID to access (MSSP only)
  -i INPUT_FILE, --input_file INPUT_FILE
                        The path to a csv with only hostnames & usernames. Expected format: 'hostname, username'
  -t, --test            run the program and output the results that would take place but take no action
  -r, --remove          remove falcon grouping tags, undoing whatever was originally done by this script
```

### Example source code
The source code for this example can be found [here](match_username_to_host.py).

---

## Comparing QueryDevicesByFilter and QueryDevicesByFilterScroll (Offset vs. Token)
This routine queries all of the hosts in your environment using the [QueryDevicesByFilter](https://github.com/CrowdStrike/falconpy/wiki/Hosts#querydevicesbyfilter) and the [QueryDevicesByFilterScroll](https://github.com/CrowdStrike/falconpy/wiki/Hosts#querydevicesbyfilterscroll) operations. The results of the two methods are then compared for equivalency. This sample demonstrates how to use both operations to paginate through large result sets, and discusses the inherent limitations of the QueryDevicesByFilter operation.

### Running the program.
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |

### Execution syntax
This example requires no input parameters.

```shell
python3 offset_vs_token.py
```

### Example source code
The source code for this example can be found [here](offset_vs_token.py).
