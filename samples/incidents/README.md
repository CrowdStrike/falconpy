![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Incidents examples
The examples in this folder focus on leveraging CrowdStrike's Incidents API.
- [CrowdScore QuickChart](#chart-your-crowdscore-for-the-past-day)
- [Incident Triage](#incident-triage)

## Chart your CrowdScore for the past day
This example demonstrates retrieving CrowdScore detail and then charting it a simple histogram.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Incidents | __READ__ |

### Execution syntax
This example accepts the following input parameters.
| Parameter | Purpose | Category |
| :--- | :--- | :--- |
|  `-h`, `--help` | Show help message and exit | optional |
| `-c`, `--hide-chart` | Hides the chart display | optional |
| `-d`, `--show-data` | Shows the data table display | optional |
| `-r`, `--reverse` | Reverse the data table sort<BR/>Will not impact chart display | optional |
| `-n`, `--no-color` | Disable color output | optional |
| `-x` CHART_SIZE,<BR/>`--chart-size` CHART_SIZE | Size of the chart to display (Max: 100, Default: 25) | optional |
| `-m` MAX_ROWS,<BR/>`--max-rows` MAX_ROWS | Maximum number of rows to return (5 - 250, Default: 100) | optional |
| `-b` BASE_URL,<BR/>`--base-url` BASE_URL | CrowdStrike cloud region. (auto or usgov1, Default: auto) | optional |
|  `-f` FALCON_CLIENT_ID,<BR/>`--falcon_client_id` FALCON_CLIENT_ID | Falcon Client ID | always required |
|  `-s` FALCON_CLIENT_SECRET,<BR/>`--falcon_client_secret` FALCON_CLIENT_SECRET | Falcon Client Secret | always required |

#### Examples
These examples demonstrate command line usage of this sample. Commands may be chained on the same command line as long as all actions make sense for the arguments provided.

- [Show command line help.](#show-command-line-help)
- [Show your current CrowdScore and plot the past 24 hours](#show-your-current-crowdscore-and-plot-the-past-24-hours)
- [Show the data table for the chart display](#show-the-data-table-for-the-chart-display)
- [Reverse the table sort](#reverse-the-table-sort)
- [Create a chart in the US-GOV-1 region](#create-a-chart-in-the-us-gov-1-region)
- [Increase the number of rows returned](#increase-the-number-of-rows-returned)
- [Increase the chart size](#increase-the-chart-size)
- [Disable color output](#disable-color-output)
- [Disable chart display](#disable-chart-display)



##### Show command line help.
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -h
```

[See output example](#command-line-help).

##### Show your current CrowdScore and plot the past 24 hours
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

###### Result
```shell
            _______                        __ _______                        __    _______
           |   _   .----.-----.--.--.--.--|  |   _   .----.-----.----.-----.|__|  |   _   |
           |.  1___|   _|  _  |  |  |  |  _  |   1___|  __|  _  |   _|  -__| __   |.  |   |
           |.  |___|__| |_____|________|_____|____   |____|_____|__| |_____||__|  |.  |   |
           |:  1   |                         |:  1   |                            |:  1   |
           |::.. . |                         |::.. . |                            |::.. . |
           `-------'                         `-------'                            `-------'


   72.00  ┼   ╭────────────────╮
   69.12  ┤   │                ╰──────────╮
   66.24  ┤   │                           ╰────╮
   63.36  ┤   │                                ╰──╮
   60.48  ┤  ╭╯                                   ╰─╮
   57.60  ┤  │                                      ╰──╮
   54.72  ┼──╯                                         ╰─╮
   51.84  ┤                                              ╰─╮
   48.96  ┤                                                ╰──╮
   46.08  ┤                                                   ╰─╮
   43.20  ┤                                                     ╰─╮
   40.32  ┤                                                       ╰─╮
   37.44  ┤                                                         ╰╮
   34.56  ┤                                                          ╰─╮
   31.68  ┤                                                            ╰─╮
   28.80  ┤                                                              ╰╮
   25.92  ┤                                                               ╰─╮
   23.04  ┤                                                                 ╰─╮
   20.16  ┤                                                                   ╰─╮
   17.28  ┤                                                                     ╰──╮
   14.40  ┤                                                                        ╰─╮
   11.52  ┤                                                                          ╰─╮
    8.64  ┤                                                                            ╰──╮
    5.76  ┤                                                                               ╰────╮
    2.88  ┤                                                                                    ╰──────╮
    0.00  ┤                                                                                           ╰───────
```

##### Show the data table for the chart display
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d
```

##### Reverse the table sort
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -r
```

##### Create a chart in the `US-GOV-1` region
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

##### Increase the number of rows returned
This argument has a range of 5 - 250.
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -m 200
```

##### Increase the chart size
This argument has a range of 5 - 100.
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -x 100
```

##### Disable color output
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -n
```

##### Disable chart display
```shell
python3 crowdscore_quickchart.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c
```

#### Command-line help
Command-line help is available using the `-h` or `--help` parameters.

```shell
% python3 crowdscore_quickchart.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -h
usage: crowdscore_quickchart.py [-h] [-c] [-d] [-r] [-n] [-x CHART_SIZE] [-m MAX_ROWS] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET

CrowdScore QuickChart.

  ___   __ __  ____    __  __  _     __  __ __   ____  ____  ______
 /   \ |  T  Tl    j  /  ]|  l/ ]   /  ]|  T  T /    T|    \|      T
Y     Y|  |  | |  T  /  / |  ' /   /  / |  l  |Y  o  ||  D  )      |
|  Q  ||  |  | |  | /  /  |    \  /  /  |  _  ||     ||    /l_j  l_j
|     ||  :  | |  |/   \_ |     Y/   \_ |  |  ||  _  ||    \  |  |
l     |l     | j  l\     ||  .  |\     ||  |  ||  |  ||  .  Y |  |
 \__,_j \__,_j|____j\____jl__j\_j \____jl__j__jl__j__jl__j\_j l__j

                                                for your CrowdScore

Quickly displays your current CrowdScore and charts a histogram
of your score over the past 24 to 36 hours.

Requirements
  asciichartpy
  crowdstrike-falconpy
  pyfiglet
  tabulate

optional arguments:
  -h, --help            show this help message and exit
  -c, --hide-chart      Hides the chart display
  -d, --show-data       Shows the data table display
  -r, --reverse         Reverse the data table sort
                        Will not impact chart display
  -n, --no-color        Disable color output
  -x CHART_SIZE, --chart-size CHART_SIZE
                        Size of the chart to display (Max: 100, Default: 25)
  -m MAX_ROWS, --max-rows MAX_ROWS
                        Maximum number of rows to return (5 - 250, Default: 100)
  -b BASE_URL, --base-url BASE_URL
                        CrowdStrike cloud region. (auto or usgov1, Default: auto)

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        Search string
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        Search string
```

### Example source code
The source code for this example can be found [here](crowdscore_quickchart.py).


## Incident Triage
This example demonstrates triaging Incidents. You can assign / unassign responders, add / remove tags, and change name, description and status of an incident using this utility.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Incidents | __READ__, __WRITE__ |
| User Management | __READ__ |

### Execution syntax
This example accepts the following input parameters.
| Parameter | Purpose | Category |
| :--- | :--- | :--- |
|  `-h`, `--help` | Show help message and exit | optional |
| `-a` ASSIGN, `--assign` ASSIGN | Email of the user to assign this incident to | modify |
| `-d` DESCRIPTION, `--description` DESCRIPTION | Description to apply to the incident | modify |
| `-i` INCIDENT, `--incident` INCIDENT | Incident ID to modify | modify |
| `-n` NAME, `--name` NAME | Name to apply to the incident | modify |
| `-r` REMOVE_TAGS, `--remove_tags` REMOVE_TAGS | Tags to remove (comma delimit)<BR/>Case sensitive | modify |
| `-t` ADD_TAGS, `--add_tags` ADD_TAGS | Tags to add (comma delimit) | modify |
| `-u` STATUS, `--status` STATUS | Status to change to (Integer or String) | modify |
| `-x`, `--unassign` | Remove the assignment from the incident | modify |
| `-f` FILTER, `--filter` FILTER | FQL string to use to filter incidents | search |
| `-k` FALCON_CLIENT_ID,<BR/>`--falcon_client_id` FALCON_CLIENT_ID | Falcon Client ID | always required |
| `-s` FALCON_CLIENT_SECRET,<BR/>`--falcon_client_secret` FALCON_CLIENT_SECRET | Falcon Client Secret | always required |

#### Examples
These examples demonstrate command line usage of this sample. Commands may be chained on the same command line as long as all actions make sense for the arguments provided.

- [Show command line help.](#show-command-line-help)
- [List all incidents available (Up to maximum limit)](#list-all-incidents-available-up-to-maximum-limit)
- [Search for an incident by host ID](#search-for-an-incident-by-host-id)
- [Change the status of an incident](#change-the-status-of-an-incident)
- [Assign a responder to an incident](#assign-a-responder-to-an-incident)
- [Unassign a responder from an incident](#unassign-a-responder-from-an-incident)
- [Add tags to an incident](#add-tags-to-an-incident)
- [Remove tags from an incident](#remove-tags-from-an-incident)
- [Change the name of an incident](#change-the-name-of-an-incident)
- [Change the description of an incident](#change-the-description-of-an-incident)

##### Show command line help.

```shell
python3 incident_triage.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -h
```

[See output example](#command-line-help).

##### List all incidents available (Up to maximum limit)

```shell
python3 incident_triage.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -h
```

##### Search for an incident by host ID
> For a complete list of available incident filters you can use for the `--filter` argument, please check [this page](https://falconpy.io/Service-Collections/Incidents.html#available-filters).

```shell
python3 incident_triage.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f "host_ids:['ID1', 'ID2']"
```

##### Change the status of an incident

> You may specify a status value of `20`, `25`, `30` or `40`. You may also use the names `New`, `Reopened`, `InProgress` and `Closed`.

```shell
python3 incident_triage.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i INCIDENT_ID -u STATUS_VALUE
```

##### Assign a responder to an incident

> The responder assigned must have an existing user account within your Falcon tenant.

```shell
python3 incident_triage.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i INCIDENT_ID -a responder_email@yourcompany.com
```

##### Unassign a responder from an incident

```shell
python3 incident_triage.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i INCIDENT_ID -x
```

##### Add tags to an incident

> Multiple tags may be specified by delimiting with a comma.

```shell
python3 incident_triage.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i INCIDENT_ID -t TAG1,TAG2,TAG3
```

##### Remove tags from an incident

> Multiple tags may be specified by delimiting with a comma.

```shell
python3 incident_triage.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i INCIDENT_ID -r TAG1,TAG2,TAG3
```

##### Change the name of an incident

> To delete the name, update it to `" "`.

```shell
python3 incident_triage.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i INCIDENT_ID -n "Name goes here"
```

##### Change the description of an incident

> To delete the description, update it to `" "`.

```shell
python3 incident_triage.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i INCIDENT_ID -d "Description goes here"
```

#### Command-line help
Command-line help is available using the `-h` or `--help` parameters.

```shell
usage: incident_triage.py [-h] [-a ASSIGN] [-d DESCRIPTION] [-i INCIDENT] [-n NAME] [-r REMOVE_TAGS] [-t ADD_TAGS] [-u STATUS] [-x] [-f FILTER] [-k FALCON_CLIENT_ID] [-s FALCON_CLIENT_SECRET]

CrowdStrike incident triage.

  _____            _     _            _
  \_   \_ __   ___(_) __| | ___ _ __ | |_ ___
   / /\/ '_ \ / __| |/ _` |/ _ \ '_ \| __/ __|
/\/ /_ | | | | (__| | (_| |  __/ | | | |_\__ \
\____/ |_| |_|\___|_|\__,_|\___|_| |_|\__|___/

            _____      _
           /__   \_ __(_) __ _  __ _  ___
             / /\/ '__| |/ _` |/ _` |/ _ \
            / /  | |  | | (_| | (_| |  __/
            \/   |_|  |_|\__,_|\__, |\___|
                               |___/

                        for FalconPy v1.1.1

Requirements
    - crowdstrike-falconpy (v1.1.1+)
    - tabulate

Search, review and modify incidents within a CrowdStrike Falcon tenant.

A complete list of available incident filters can be found at:
https://falconpy.io/Service-Collections/Incidents.html#available-filters

optional arguments:
  -h, --help            show this help message and exit

update arguments:
  -a ASSIGN, --assign ASSIGN
                        Email of the user to assign this incident to
  -d DESCRIPTION, --description DESCRIPTION
                        Description to apply to the incident
  -i INCIDENT, --incident INCIDENT
                        Incident ID to modify
  -n NAME, --name NAME  Name to apply to the incident
  -r REMOVE_TAGS, --remove_tags REMOVE_TAGS
                        Tags to remove (comma delimit)
                        Case sensitive
  -t ADD_TAGS, --add_tags ADD_TAGS
                        Tags to add (comma delimit)
  -u STATUS, --status STATUS
                        Status to change to (Integer or String)
  -x, --unassign        Remove the assignment from the incident

search arguments:
  -f FILTER, --filter FILTER
                        FQL string to use to filter incidents

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API Client Secret
```

### Example source code
The source code for this example can be found [here](incident_triage.py).