![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Hosts examples
The examples in this folder focus on leveraging CrowdStrike's Hosts API to perform administrative operations.
- [Add Falcon Tags in bulk](#add-falcon-tags-in-bulk)
- [Default Groups](#default-groups)
- [Get Host Groups](#get-host-groups)
- [Host Report](#host-report)
- [Host Search](#host-search)
- [List sensor versions by Hostname](#list-sensors-by-hostname)
- [List (and optionally remove) duplicate sensors](#list-duplicate-sensors)
- [List (and optionally remove) stale sensors](#list-stale-sensors)
- [Mass assignment check](#mass-assignment-check)
- [Match usernames to Hosts](#match-usernames-to-hosts)
- [Offset vs. Offset Tokens](#comparing-querydevicesbyfilter-and-querydevicesbyfilterscroll-offset-vs-token)
- [Prune Hosts by Hostname or AID](#prune-hosts-by-hostname-or-aid)
- [RFM Report](#rfm-report)
- [Serial Search](#serial-search)

## Add Falcon Tags in bulk
Bulk assign a Falcon Grouping Tag to a list of hosts based on their serial number. This solution updates the tags of hosts in batches of 20.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |

### Execution syntax
This samples leverages simple command-line arguments to implement functionality.

> Execute the default example. This will assume the file containing serial numbers is called "serials.txt" and is stored in the same folder. That tag that will be added will have a value of "TEST_TAG".

```shell
python3 bulk_add_falcon_tag.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown below without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

```shell
python3 bulk_add_falcon_tag.py
```

> Read the file "new_serials.txt" and apply the tag "NEW_TAG" to all devices identified.

```shell
python3 bulk_add_falcon_tag.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f new_serials.txt -t NEW_TAG
```

> Remove the tag "NEW_TAG" from all hosts identified in the file "new_serials.txt".

```shell
python3 bulk_add_falcon_tag.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f new_serials.txt -t NEW_TAG -r
```

> API debugging can be enabled using the `-d` argument.

```shell
python3 rfm_report.py -d
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: bulk_add_falcon_tag.py [-h] [-d] [-f SERIAL_FILE] [-t TAG] [-r] [-k CLIENT_ID] [-s CLIENT_SECRET]

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |             FalconPy
`-------'                         `-------'
 __ __   ___    _____ ______  _____     ______   ____   ____   ____    ___  ____
|  T  T /   \  / ___/|      T/ ___/    |      T /    T /    T /    T  /  _]|    \
|  l  |Y     Y(   \_ |      (   \_     |      |Y  o  |Y   __jY   __j /  [_ |  D  )
|  _  ||  O  | \__  Tl_j  l_j\__  T    l_j  l_j|     ||  T  ||  T  |Y    _]|    /
|  |  ||     | /  \ |  |  |  /  \ |      |  |  |  _  ||  l_ ||  l_ ||   [_ |    \
|  |  |l     ! \    |  |  |  \    |      |  |  |  |  ||     ||     ||     T|  .  Y
l__j__j \___/   \___j  l__j   \___j      l__j  l__j__jl___,_jl___,_jl_____jl__j\_j

This script was developed by @Don-Swanson-Adobe to bulk assign or remove a Falcon
Grouping Tag against a list of hosts based on their serial number.

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging
  -f SERIAL_FILE, --serial_file SERIAL_FILE
                        Text file contain serial numbers of hosts to tag
  -t TAG, --tag TAG     String to use for the Falcon Tag
  -r, --remove          Remove tag instead of applying it

Required arguments:
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API secret
```

### Example source code
The source code for these examples can be found [here](bulk_add_falcon_tag.py).

---

## List sensors by hostname
Loops through all hosts and displays the hostname and sensor version.

There are multiple variations of this sample demonstrating different options for achieving the same goals.

| Sample | Notes |
| :-- | :-- |
| [Sensor version by hostname](sensor_versions_by_hostname.py) | Displays all hosts along with their sensor version. Maximum number of results returned: __10,000__ |
| [Sensor version by hostname (Scrolling)](sensor_versions_by_hostname_scrolling.py) | Displays all hosts along with their sensor version. No maximum on number of hosts returned. |
| [Sensor version by hostname (Advanced)](sensor_versions_by_hostname_advanced.py) | Displays all hosts along with their sensor version. No maximum on number of hosts returned. Leverages multiple threads to speed up results processing. |

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |

### Execution syntax
These samples leverage simple command-line arguments to implement functionality.

All keywords are available in all three samples.

> Execute the simple example.

```shell
python3 sensor_versions_by_hostname.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Execute the scrolling example, reversing the sort.

```shell
python3 sensor_versions_by_hostname_scrolling.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -r
```

> Execute the advanced example and return results for a child tenant.

```shell
python3 sensor_versions_by_hostname_advanced.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -m $CHILD_CID
```

> Execute the advanced example for a GovCloud tenant.

```shell
python3 sensor_versions_by_hostname_advanced.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 sensor_versions_by_hostname.py -h
usage: sensor_versions_by_hostname.py [-h] -k CLIENT_ID -s CLIENT_SECRET [-m MSSP] [-b BASE_URL] [-r]

List sensors versions by hostname

optional arguments:
  -h, --help            show this help message and exit
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API key secret
  -m MSSP, --mssp MSSP  Child CID to access (MSSP only)
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike API region (us1, us2, eu1, usgov1). NOT required unless you are using `usgov1`.
  -r, --reverse         Reverse sort (defaults to ASC)
```

### Example source code
The source code for these examples can be found here:

- [Sensor versions by hostname](sensor_versions_by_hostname.py)
- [Sensor versions by hostname (Scrolling)](sensor_versions_by_hostname_scrolling.py)
- [Sensor versions by hostname (Advanced)](sensor_versions_by_hostname_advanced.py)

---


## List duplicate sensors
Retrieves a list of duplicate sensors across all hosts within your tenant. Can optionally hide (and then restore) duplicate sensors identified.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__, __WRITE__ |

### Execution syntax
This application leverages easy to use command line arguments to implement functionality.

> List just duplicate sensors. 
```shell
python3 duplicate_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Perform the same lookup against a tenant within GovCloud.

```shell
python3 duplicate_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

> List all hosts (including duplicates).

```shell
python3 duplicate_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -a
```

> Search a child tenant.

```shell
python3 duplicate_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -a -m CHILD_CID
```

> Hide duplicate sensors identified.

```shell
python3 duplicate_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d
```

> Restore previously removed duplicates.

```shell
python3 duplicate_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -r HOST_LIST_FILE
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
% python3 duplicate_sensors.py -h
usage: duplicate_sensors.py [-h] [-b BASE_URL] [-d] [-r RESTORE_DUPLICATES] [-a] [-m MSSP] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET

Duplicate sensor detection and removal.

 ______               __ __            __           ______         __              __
|   _  \ .--.--.-----|  |__.----.---.-|  |_.-----. |   _  \ .-----|  |_.-----.----|  |_.-----.----.
|.  |   \|  |  |  _  |  |  |  __|  _  |   _|  -__| |.  |   \|  -__|   _|  -__|  __|   _|  _  |   _|
|.  |    |_____|   __|__|__|____|___._|____|_____| |.  |    |_____|____|_____|____|____|_____|__|
|:  1    /     |__|                                |:  1    /
|::.. . /                                          |::.. . /            CrowdStrike FalconPy v1.2
`------'                                           `------'

01.25.23 - jshcodes@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike Region (us1, us2, eu1, usgov1)
                        Only required for GovCloud users.
  -d, --delete_duplicates
                        Remove duplicate hosts from the CrowdStrike console.
  -r RESTORE_DUPLICATES, --restore_duplicates RESTORE_DUPLICATES
                        Restores prevously deleted duplicates using a save file.
  -a, --all             Display all hosts, not just duplicates.
  -m MSSP, --mssp MSSP  CID of a child tenant to access.

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API client ID.
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API client secret.
```

### Example source code
The source code for this example can be found [here](duplicate_sensors.py).

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

Perform the same lookup against a tenant within GovCloud.

```shell
python3 stale_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d 30 -g
```

This variation will retrieve a list of hosts that haven't checked in to CrowdStrike in 30 days or more that have the tag `testtag`.

```shell
python3 stale_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d 30 -t testtag
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
usage: stale_sensors.py [-h] -k CLIENT_ID -s CLIENT_SECRET [-m MSSP] [-g] [-d DAYS] [-r] [-x] [-t TAG]

CrowdStrike Unattended Stale Sensor Environment Detector.

         _______ ___ ___ _______ _______ _______ ______
        |   _   |   Y   |   _   |   _   |   _   |   _  \
        |.  1___|.  |   |   1___|   1___|.  1___|.  |   \
        |.  |___|.  |   |____   |____   |.  __)_|.  |    \
        |:  1   |:  1   |:  1   |:  1   |:  1   |:  1    /
        |::.. . |::.. . |::.. . |::.. . |::.. . |::.. . /
        `-------`-------`-------`-------`-------`------'

stale_sensors.py - Detects devices that haven't checked into
                   CrowdStrike for a specified period of time.

REQUIRES: crowdstrike-falconpy v0.9.0+, python-dateutil, tabulate

This example will work for all CrowdStrike regions. In order to produce
results for the US-GOV-1 region, pass the '-g' argument.

- jshcodes@CrowdStrike; 09.01.21
- ray.heffer@crowdstrike.com; 03.29.22 - Added new argument for Grouping Tags (--grouping, -g)
- @morcef, jshcodes@CrowdStrike; 06.05.22 - More reasonable date calcs, Linting, Easier arg parsing
                                            Easier base_url handling, renamed grouping_tag to tag

optional arguments:
  -h, --help            show this help message and exit
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API key secret
  -m MSSP, --mssp MSSP  Child CID to access (MSSP only)
  -g, --govcloud        Use the US-GOV-1 region
  -d DAYS, --days DAYS  Number of days since a host was seen before it is considered stale
  -r, --reverse         Reverse sort (defaults to ASC)
  -x, --remove          Remove hosts identified as stale
  -t TAG, --tag TAG     Falcon Grouping Tag name for the hosts
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

---

## Prune Hosts by Hostname or AID
Search for and optionally remove hosts by hostname or AID. Removed host AIDs are saved to a file which can be leveraged to restore removed hosts.

### Running the program.
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__, __WRITE__ |

### Execution syntax

List hosts by hostname or AID.

```shell
python3 prune_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f HOSTNAME
```

Remove identified hosts.

```shell
python3 prune_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f HOSTNAME -d
```

Restore previously deleted hosts from the restore file.

```shell
python3 prune_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -r -a RESTORE_FILENAME
```

Restore previously deleted hosts by AID.

```shell
python3 prune_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -r -a AID1,AID2,AID3
```

Change your BASE_URL to point to GovCloud.

```shell
python3 prune_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

Search a child tenant for hosts to remove.

```shell
python3 prune_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f HOSTNAME -m CHILD_CID
```

### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 prune_hosts.py -h
usage: prune_hosts.py [-h] [-b BASE_URL] [-f FIND] [-r] [-a AIDS] [-d] [-m MSSP] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET

Remove sensors by name or AID sample.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |        FalconPy v1.2
`-------'                         `-------'

 __ __   ___    _____ ______      ____  ____   __ __  ____     ___  ____
|  T  T /   \  / ___/|      T    |    \|    \ |  T  T|    \   /  _]|    \
|  l  |Y     Y(   \_ |      |    |  o  )  D  )|  |  ||  _  Y /  [_ |  D  )
|  _  ||  O  | \__  Tl_j  l_j    |   _/|    / |  |  ||  |  |Y    _]|    /
|  |  ||     | /  \ |  |  |      |  |  |    \ |  :  ||  |  ||   [_ |    \
|  |  |l     ! \    |  |  |      |  |  |  .  Yl     ||  |  ||     T|  .  Y
l__j__j \___/   \___j  l__j      l__j  l__j\_j \__,_jl__j__jl_____jl__j\_j

Removes hosts by hostname or AID. Can restore hosts that have been removed.

02.11.23 - jshcodes@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike Region (us1, us2, eu1, usgov1)
                        Only required for GovCloud users.
  -f FIND, --find FIND  Hostname or AID string to use to identify hosts for removal.
                        Hostname searches are stemmed, AID searches must be an exact match.
  -r, --restore         Restores prevously deleted hosts using a save file or list of AIDs.
                        Specify the AID list or filename using the `-a` command line argument.
  -a AIDS, --aids AIDS  List of AIDs to restore (comma delimited string or a filename).
  -d, --delete          Perform the delete, default behavior is to list only.
  -m MSSP, --mssp MSSP  CID of a child tenant to access (MSSP only).

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API client ID.
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API client secret.
```

### Example source code
The source code for this example can be found [here](prune_hosts.py).

---

## RFM Report
This script determines the number of hosts in RFM (Up for more than 24 hours and seen within the last 24 hours) in your tenant or every child tenant attached to your parent.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |
| Flight Control | __READ__ (MSSP usage only) |

### Execution syntax
This samples leverages simple command-line arguments to implement functionality.

> Execute the default example. This will output results for your tenant (only) to a CSV file called `RFM_Report.csv`.

```shell
python3 rfm_report.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown below without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

```shell
python3 rfm_report.py
```

> The output file name can be changed using the `-o` argument.

```shell
python3 rfm_report.py -o my_rfm_report.csv
```

> For MSSP scenarios, provide your parent credentials and activate MSSP mode with the `-m` argument.

```shell
python3 rfm_report.py -k $FALCON_CLIENT_ID_PARENT -s $FALCON_CLIENT_SECRET_PARENT -m
```

> API debugging can be enabled using the `-d` argument.

```shell
python3 rfm_report.py -d
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: rfm_report.py [-h] [-d] [-m] [-o OUTPUT_PATH] [-k CLIENT_ID] [-s CLIENT_SECRET]

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |             FalconPy
`-------'                         `-------'

██████  ███████ ███    ███     ██████  ███████ ██████   ██████  ██████  ████████
██   ██ ██      ████  ████     ██   ██ ██      ██   ██ ██    ██ ██   ██    ██
██████  █████   ██ ████ ██     ██████  █████   ██████  ██    ██ ██████     ██
██   ██ ██      ██  ██  ██     ██   ██ ██      ██      ██    ██ ██   ██    ██
██   ██ ██      ██      ██     ██   ██ ███████ ██       ██████  ██   ██    ██

This script was developed by @Developed by Don-Swanson-Adobe to determine the
number of hosts in RFM (Up for more than 24 hours and seen within the last 24
hours) in your tenant or every child tenant attached to your parent.

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging
  -m, --mssp            Return RFM details for child CIDs (MSSP parents only).
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        Location to store CSV output

Required arguments:
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API secret
```

### Example source code
The source code for these examples can be found [here](rfm_report.py).

---