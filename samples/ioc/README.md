![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Falcon IOC samples
The examples within this folder focus on leveraging CrowdStrike's Falcon IOC API.

- [Create Indicator of Compromise](#create-indicator-of-compromise)
- [IOC Audit](#ioc-audit)
- [IOC Restore](#ioc-restore)

## Create Indicator of Compromise
Demonstrates the creation of a single IOC using either the Service or Uber Class. 
Indicator detail is loaded from an external file that can be specified via the command line.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| IOC | __WRITE__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Create an indicator using sample indicator file `example_indicator.json`. The default method uses the Service Class to interact with the CrowdStrike API.

```shell
python3 create_ioc.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Perform the operation using the Uber class instead with the `-m` argument.

```shell
python3 create_ioc.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -m uber
```

> Load a custom indicator file with the `-i` argument. (Indicator should be in JSON format.)

```shell
python3 create_ioc.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i custom_indicator.json
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 create_ioc.py -h
usage: create_ioc.py [-h] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET [-m METHOD] [-i INDICATOR]

 ___  _______  _______
|   ||   _   ||   _   |
|.  ||.  |   ||.  1___|
|.  ||.  |   ||.  |___
|:  ||:  1   ||:  1   |
|::.||::.. . ||::.. . |
`---'`-------'`-------'

Create IOC Example - @jshcodes 06.23.21

FalconPy v.0.8.6+

INDICATOR FILE FORMAT EXAMPLE (JSON)
{
    "source": "Test",
    "action": "detect",
    "expiration": "2023-01-22T15:00:00.000Z",
    "description": "Testing",
    "type": "ipv4",
    "value": "4.1.42.34",
    "platforms": ["linux"],
    "severity": "LOW",
    "applied_globally": true
}

optional arguments:
  -h, --help            show this help message and exit
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        Falcon API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        Falcon API Client Secret
  -m METHOD, --method METHOD
                        SDK method to use ('service' or 'uber').
  -i INDICATOR, --indicator INDICATOR
                        Path to the file representing the indicator (JSON format).
```

### Example source code
The source code for this example can be found [here](create_ioc.py).

---

## IOC Audit
This program will output a list of IOCs and their details for either the current CID or in each Child CID (Flight Control scenarios).
This can be used for regular audits of IOCs across multiple CIDs.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| IOC | __READ__ |
| Flight Control | __READ__ |
| Sensor Download | __READ__ |

> [!NOTE]
> This program can be executed using an API key that is not scoped for the Flight Control (MSSP) and Sensor Download service collections, but will be unable to lookup the current CID (Sensor Download) or access child CIDs (Flight Control).

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Execute the default example. This will output results to a CSV file named `iocs.txt`.

```shell
python3 ioc_audit.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown below without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

```shell
python3 ioc_audit.py
```

Change the output destination with the `-o` argument.

```shell
python3 ioc_audit.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -o new_iocs.txt
```

Enable MSSP mode and audit all Flight Control children with the `-m` argument.

```shell
python3 ioc_audit.py -k $FALCON_CLIENT_ID_PARENT -s $FALCON_CLIENT_SECRET_PARENT -m
```

Enable MSSP mode and audit a specific Flight Control child with the `-c` argument.

```shell
python3 ioc_audit.py -k $FALCON_CLIENT_ID_PARENT -s $FALCON_CLIENT_SECRET_PARENT -c CHILD_CID
```

> API debugging can be enabled using the `-d` argument.

```shell
python3 ioc_audit.py -d
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: ioc_audit.py [-h] [-d] [-m] [-c CHILD] [-o OUTPUT_FILE] [-k CLIENT_ID] [-s CLIENT_SECRET]

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀
     ▐░▌     ▐░▌       ▐░▌▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌
 ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀
▄▄▄          █           ▀
█▄▄ ▀▄▀ █▀▀  █  █ █ █▀▀  █  █▀█ █▀█ █▀▀
█▄▄ ▄▀▄ █▄▄  █▄ █▄█ ▄▄█  █  █▄█ █ █ ▄▄█

This program will output a list of IOCs and their details for either the
current CID or in each Child CID (Flight Control scenarios). This can be
used for regular audits of indicators of compromise across multiple CIDs.

Developed by @Don-Swanson-Adobe

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging
  -m, --mssp            List exclusions in all child CIDs (MSSP parents only)
  -c CHILD, --child CHILD
                        List exclusions in a specific child CID (MSSP parents only)
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        File to output results to

Required arguments:
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API secret
```

### Example source code
The source code for this example can be found [here](ioc_audit.py).

---

## IOC Restore
This program will restore deleted IOCs based upon specified filter criteria.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| IOC | __READ__, __WRITE__ |

#### Required packages
In order to run this sample, you will need to have the [`tabulate`](https://pypi.org/project/tabulate/) package installed.

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Execute the default example. This will default to looking for IOCs that were applied globally and deleted as of today's date.

> [!NOTE]
> Times are in UTC.

```shell
python3 ioc_restore.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown below without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

```shell
python3 ioc_restore.py
```

Change the CrowdStrike region with the `-b` argument.

```shell
python3 ioc_restore.py -b usgov1
```

Search for deleted IOCs modified by a specific user with the `-m` argument.

```shell
python3 ioc_restore.py -m username@domain.com
```

Search for deleted IOCs on a specific day using the `-dt` argument.

> [!TIP]
> This argument should be in YYYY-mm-dd format.

```shell
python3 ioc_restore.py -dt 2024-10-27
```

Search for deleted IOCs targeting a specific Host Group (by ID) using the `-hg` argument.

```shell
python3 ioc_restore.py -hg $HOST_GROUP_ID
```

Search for deleted IOCs targeting a specific Host Group (by Host Group name) using the `-g` argument.

```shell
python3 ioc_restore.py -g $HOST_GROUP_NAME
```

List all deleted IOCs discovered but take no action with the `-l` argument.

```shell
python3 ioc_restore.py -l
```

> [!TIP]
> Multiple command line parameters may be provided to refine search results.

API debugging can be enabled using the `-d` argument.

```shell
python3 ioc_restore.py -d
```

Adjust the output table format using the `-t` argument.

```shell
python3 ioc_restore.py -l -t fancy_grid
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: ioc_restore.py [-h] [-d] [-c CLIENT_ID] [-k CLIENT_SECRET] [-b BASE_URL] [-dt DATE]
                      [-m MODIFIED_BY] [-hg HOSTGROUP] [-g GROUPNAME] [-l] [-t TABLE_FORMAT]

Restore deleted IOCs.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

╦╔═╗╔═╗  ╦═╗┌─┐┌─┐┌┬┐┌─┐┬─┐┌─┐
║║ ║║    ╠╦╝├┤ └─┐ │ │ │├┬┘├┤
╩╚═╝╚═╝  ╩╚═└─┘└─┘ ┴ └─┘┴└─└─┘

This sample demonstrates restoring previously deleted IOCs.

~~~ API Scope Requirements ~~~
IOC Management - Read / Write
IOCs (Indicators of Compromise) - Read / Write

Creation date: 11.06.2024 - am-cs-se@CrowdStrike
Modification: 11.07.2024 - jshcodes@CrowdStrike

options:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging
  -c, --client_id CLIENT_ID
                        CrowdStrike API client ID
  -k, --client_secret CLIENT_SECRET
                        CrowdStrike API client secret
  -b, --base_url BASE_URL
                        CrowdStrike Region (US1, US2, EU1, USGOV1, USGOV2) Full URL is also supported.
  -dt, --date DATE      Date to target (YYYY-MM-DD)
  -m, --modified_by MODIFIED_BY
                        User who modified the deleted IOCs
  -hg, --hostgroup HOSTGROUP
                        ID of the Host Group associated with the IOC Not required when --groupname is
                        specified.
  -g, --groupname GROUPNAME
                        Name of the Host Group associated with the IOC Not required when --hostgroup is
                        specified.
  -l, --list            List deleted IOCs but take no action
  -t, --table-format TABLE_FORMAT
                        Tabular display format
```

### Example source code
The source code for this example can be found [here](ioc_restore.py).