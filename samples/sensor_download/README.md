![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Sensor Download examples
The examples within this folder focus on leveraging CrowdStrike's Falcon Sensor Download API to list and retrieve versions of the CrowdStrike agent.

- [List or download the Falcon agent by operating system and version]()

## Sensor Download by Operating System or Version
This sample demonstrates how to list and download sensors by operating system and versions.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :-- | :-- |
| Sensor Download | __READ__ |

### Execution syntax
This demonstration was developed to leverage easy to use command-line arguments.

- [Command line arguments](#command-line-arguments)
- [Basic usage](#basic-usage)
- [Filtering by operating system](#filtering-by-operating-system)
- [Showing all available detail](#showing-all-available-detail)
- [Filtering by Operating System version](#filtering-by-operating-system-version)
- [Downloading a sensor](#downloading-a-sensor)

#### Command line arguments
This program accepts the following command-line arguments.

| Argument | Long Argument | Description |
| :-- | :-- | :-- |
| `-h` | `--help` | show help message and exit |
| `-k` _KEY_ | `--key` _KEY_ | CrowdStrike API Key |
| `-s` _SECRET_ | `--secret` _SECRET_ | CrowdStrike API Secret |
| `-a` | `--all` | Show all columns / Download all versions |
| `-d` | `--download` | Shortcut for `--command download` |
| `-n` _NMINUS_ | `--nminus` _NMINUS_ | Download previous version (n-1, n-2, 0 = current, 2 = n-2) |
| `-c` _COMMAND_ | `--command` _COMMAND_ | Command to perform. (list or download, defaults to list) |
| `-o` _OS_ | `--os` _OS_ | Sensor operating system |
| `-v` _OSVER_ | `--osver` _OSVER_ | Sensor operating system version |
| `-f` _FILENAME_ | `--filename` _FILENAME_ | Name to use for downloaded file |
| `-t` _TABLE_FORMAT_ | `--table_format` _TABLE_FORMAT_ | Table format to use for display.
|`-debug`|`--debug`|`Enable API debugging`|
|`-b`|`--base-url`|`GovCloud access to Crowdstrike API`|<ul><li>plain</li><li>simple</li><li>github</li><li>grid</li><li>fancy_grid</li><li>pipe</li><li>orgtbl</li><li>jira</li><li>presto</li><li>pretty</li><li>psql</li><li>rst</li><li>mediawiki</li><li>moinmoin</li><li>youtrack</li><li>html</li><li>unsafehtml</li><li>latext</li><li>latex_raw</li><li>latex_booktabs</li><li>latex_longtable</li><li>textile</li><li>tsv</li></ul> |

#### Basic usage
The only required command line arguments are `-k` (CrowdStrike Falcon API Client ID) and `-s` (CrowdStrike Falcon API Client Secret).

The default command is "list" with no filters specified, which displays all sensor versions for all available operating systems.

```shell
python3 download_sensor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

#### Filtering by operating system
You can filter results by operating system with the `-o` argument.

```shell
python3 download_sensor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -o ubuntu
```

#### Showing all available detail
Extended detail for the versions listed can be shown by using the `-a` argument.

```shell
python3 download_sensor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -o ubuntu -a
```

#### Filtering by Operating System version
You can additionally filter by operating system version using the `-v` argument.

```shell
python3 download_sensor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -o centos -v 7
```

#### Downloading a sensor
Downloading is performed using the `-d` argument. (Defaults to __Windows__.)

##### Simple example
This example will download the latest sensor version for Windows.

```shell
python3 download_sensor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d
```

##### Filtering by Operating System and Version
Filters described above are applied to select the appropriate version to download.

```shell
python3 download_sensor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -o centos -v 7 -d
```
##### Activating Debugging 
This example shows how you can activate debugging functionality when you run download_senor.py.

```shell
python3 download_sensor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -debug 
```
##### Allowing Access to GovCloud Users 
This example shows how you GovCloud user can access sensor_download.py.

```shell
python3 download_sensor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b 
```
##### Specifying `N-1` or `N-2` versions.
You can specify the previous, or 2nd previous version to download by leveraging the `-n` argument.

| Argument value | Result |
| :-: | :-- |
| 0 | Current |
| 1 | `N-1` (previous) |
| 2 | `N-2` (second previous) |

```shell
python3 download_sensor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d -n 2
```

##### Downloading all
You can download all available versions, or all versions for a specific Operating System using the `-a` argument. Passing the `-n` argument here will also be respected, and only download versions that are `N-1` or `N-2`.

```shell
python3 download_sensor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d -a
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: download_sensor.py [-h] -k KEY -s SECRET [-a] [-d] [-n NMINUS] [-c COMMAND] [-o OS] [-v OSVER] [-f FILENAME] [-t TABLE_FORMAT]

CrowdStrike Falcon Sensor Download utility.

            CrowdStrike Falcon
 _______                               ______                        __                __
|   _   .-----.-----.-----.-----.----.|   _  \ .-----.--.--.--.-----|  .-----.---.-.--|  |
|   1___|  -__|     |__ --|  _  |   _||.  |   \|  _  |  |  |  |     |  |  _  |  _  |  _  |
|____   |_____|__|__|_____|_____|__|  |.  |    |_____|________|__|__|__|_____|___._|_____|
|:  1   |                             |:  1    /
|::.. . |                             |::.. . /                 - jshcodes@CrowdStrike
`-------'                             `------'

This example requires the crowdstrike-falconpy (0.6.2+) and tabulate packages.

Required API Scope - Sensor Download: READ

optional arguments:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     CrowdStrike API Key
  -s SECRET, --secret SECRET
                        CrowdStrike API Secret
  -a, --all             Show all columns / Download all versions
  -d, --download        Shortcut for '--command download'
  -b, --base-url        Allows access to usgov1
  -n NMINUS, --nminus NMINUS
                        Download previous version (n-1, n-2, 0 = current, 2 = n-2)
  -c COMMAND, --command COMMAND
                        Command to perform. (list or download, defaults to list)
  -o OS, --os OS        Sensor operating system
  -debug, --debug       Command to activate debugging 
  -v OSVER, --osver OSVER
                        Sensor operating system version
  -f FILENAME, --filename FILENAME
                        Name to use for downloaded file
  -t TABLE_FORMAT, --table_format TABLE_FORMAT
                        Table format to use for display.
                        (plain, simple, github, grid, fancy_grid, pipe, orgtbl, jira, presto,
                        pretty, psql, rst, mediawiki, moinmoin, youtrack, html, unsafehtml,
                        latext, latex_raw, latex_booktabs, latex_longtable, textile, tsv)
            
```

### Example source code
Source code for this example can be found [here](download_sensor.py).
