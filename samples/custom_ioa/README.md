![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Custom IOA examples
The examples in this folder focus on leveraging CrowdStrike's Custom IOA API to manage Indicators of Attack within your Falcon Tenant.

> This solution supports MSSP scenarios and can clone rules to and delete rules from children.

- [Custom IOA Cloner](#custom-ioa-cloner) - Clone, delete and display Custom IOA rule groups.

## Custom IOA Cloner

+ [Running the program](#running-the-program)
+ [Execution syntax](#execution-syntax)
+ [Example source code](#example-source-code)

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Custom IOA | __READ__, __WRITE__ |


### Execution syntax
This demonstration was developed to leverage easy to use command-line arguments.

- [Command line arguments](#command-line-arguments)
- [Basic usage](#basic-usage)
- [Filtering by name](#filtering-by-name)
- [Cloning IOA rule groups](#cloning-ioa-rule-groups)
- [Cloning IOA rule groups to a child](#cloning-ioa-rule-groups-to-a-child)
- [Deleting IOA rule groups](#deleting-ioa-rule-groups)
- [Deleting IOA rule groups within a child](#deleting-ioa-rule-groups-within-a-child)
- [Command-line help](#command-line-help)


#### Command line arguments
This program accepts the following command line arguments.

| Argument | Long Argument | Description |
| :-- | :-- | :-- |
| `-h` | `--help` | Display command line help and exit |
| `-n` | `--no_color` | Disable color output in result displays |
| `-b` | `--base_url` | Base URL |
| `-t` _TABLE_FORMAT_ | `--table_format` _TABLE_FORMAT_ | Table format to use for display, one of: <BR/>`plain`, `simple`, `github`, `grid`, `fancy_grid`, `pipe`, `orgtbl`, `jira`, `presto`, `pretty`, `psql`, `rst`, `mediawiki`, `moinmoin`, `youtrack`, `html`, `unsafehtml`, `latext`, `latex_raw`, `latex_booktabs`, `latex_longtable`, `textile`, or `tsv`. |
| `-f` _FILTER_ | `--filter` _FILTER_ | String to filter results (IOA rule group name) |
| `-c` | `--clone` | Clone all IOA rule group matches to new rule groups |
| `-d` _DELETE_LIST_ | `--delete` _DELETE_LIST_ | List of rule group IDs to delete (comma-delimit) |
| `-m` _MANAGED_TARGETS_ | `--managed_targets` _MANAGED_TARGETS_ | List of child CIDs to target for cloning / deletions (comma-delimit) |
| `-k` _FALCON_CLIENT_ID_ | `--falcon_client_id` _FALCON_CLIENT_ID_ | CrowdStrike Falcon API Client ID |
| `-s` _FALCON_CLIENT_SECRET_ | `--falcon_client_secret` _FALCON_CLIENT_SECRET_ | CrowdStrike Falcon API Client Secret |

#### Basic usage
The only required command line arguments are `-k` (CrowdStrike Falcon API Client ID) and `-s` (CrowdStrike Falcon API Client Secret).

The default command is "list" with no filters specified, which displays all Custom IOA rule groups within your tenant.

##### Example

```shell
python3 custom_ioa_clone.py -k CLIENT_ID_HERE -s CLIENT_SECRET_HERE
```

##### Example result

```shell
_______ _     _ _______ _______  _____  _______      _____  _____  _______
|       |     | |______    |    |     | |  |  |        |   |     | |_____|
|_____  |_____| ______|    |    |_____| |  |  |      __|__ |_____| |     |

╒══════════════════════════════════╤══════════════════════════════════════════╤════════════╤═════════════════════════════════╕
│ Custom IOA Name                  │ Description                              │ Platform   │ Rules                           │
╞══════════════════════════════════╪══════════════════════════════════════════╪════════════╪═════════════════════════════════╡
│ Windows Test IOA                 │ Test IOA for windows                     │ windows    │ windows custom IOA (ver: 2)     │
│ abc1d2ef3g456ab7cd89e0fa1b23cd4e │                                          │ Enabled    │                                 │
│                                  │                                          │ Version: 1 │                                 │
├──────────────────────────────────┼──────────────────────────────────────────┼────────────┼─────────────────────────────────┤
│ Linux Test IOA                   │ Validation test policy for custom IOA to │ linux      │                                 │
│ 1bc1f2ec3a426ab7cd89e0fa1b23cd4f │ test linux                               │ Disabled   │                                 │
│                                  │                                          │ Version: 1 │                                 │
├──────────────────────────────────┼──────────────────────────────────────────┼────────────┼─────────────────────────────────┤
│ test IOA                         │ test IOA                                 │ windows    │                                 │
│ abc1d2ef3g4c4cba4d89e02a1b23cd4a │                                          │ Disabled   │                                 │
│                                  │                                          │ Version: 1 │                                 │
├──────────────────────────────────┼──────────────────────────────────────────┼────────────┼─────────────────────────────────┤
│ Exploit Demo                     │ Exploit Demo                             │ linux      │ SecFrameWork (ver: 4)           │
│ 6bc1d2ef3g456ab83d8ae0ba1b23cd4b │                                          │ Disabled   │                                 │
│                                  │                                          │ Version: 1 │                                 │
├──────────────────────────────────┼──────────────────────────────────────────┼────────────┼─────────────────────────────────┤
│ Sec Framework IOA's              │ Security Framework Custom IOAs           │ linux      │ SecFrameWork (ver: 20)          │
│ abc1d2ef3a453ab1cd89e0f41b23cd4c │                                          │ Enabled    │ Detect Shell Shoveling (ver: 4) │
│                                  │                                          │ Version: 1 │                                 │
╘══════════════════════════════════╧══════════════════════════════════════════╧════════════╧═════════════════════════════════╛
```

#### Filtering by name
You can filter results down using the `-f` argument to filter by name.
```shell
python3 custom_ioa_clone.py -k CLIENT_ID_HERE -s CLIENT_SECRET_HERE -f SEARCH_STRING
```

#### Cloning IOA rule groups
Cloning IOA rule groups can be performed by passing the `-c` argument. Any matches to the filter string (`-f`) are cloned.

```shell
python3 custom_ioa_clone.py -k CLIENT_ID_HERE -s CLIENT_SECRET_HERE -f SEARCH_STRING -c
```

#### Cloning IOA rule groups to a child
Cloning IOA rule groups to a child can be performed by passing the `-c` argument along with the `-m` argument. Any matches to the filter string (`-f`) are cloned into valid children specified within the comma delimited list provided.

```shell
python3 custom_ioa_clone.py -k CLIENT_ID_HERE -s CLIENT_SECRET_HERE -f SEARCH_STRING -c -m TARGET_CID_1,TARGET_CID_2
```

#### Deleting IOA rule groups
You must provide the exact rule group ID in order to delete using the `-d` argument. Multiple IDs may be specified at the
same time if you provide these as a comma-delimited list.

```shell
python3 custom_ioa_clone.py -k CLIENT_ID_HERE -s CLIENT_SECRET_HERE -d RULE_GROUP_ID1,RULE_GROUP_ID2
```

#### Deleting IOA rule groups within a child
You may delete rule groups from within a single child by passing the child CID with the `-m` argument. You must provide the exact rule group ID in order to delete using the `-d` argument. Multiple IDs may be specified at the same time if you provide these as a comma-delimited list.

```shell
python3 custom_ioa_clone.py -k CLIENT_ID_HERE -s CLIENT_SECRET_HERE -m TARGET_CID_1 -d RULE_GROUP_ID1,RULE_GROUP_ID2
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: custom_ioa_clone.py [-h] [-n] [-b BASE_URL] [-t TABLE_FORMAT] [-f FILTER] [-c] [-d DELETE] [-m MANAGED_TARGETS] [-k FALCON_CLIENT_ID] [-s FALCON_CLIENT_SECRET]

Custom IOA duplicator.

 ______                         __ _______ __         __ __
|      |.----.-----.--.--.--.--|  |     __|  |_.----.|__|  |--.-----.
|   ---||   _|  _  |  |  |  |  _  |__     |   _|   _||  |    <|  -__|
|______||__| |_____|________|_____|_______|____|__|  |__|__|__|_____|

 ____                     __                           ______   _____   ______
/\  _`\                  /\ \__                       /\__  _\ /\  __`\/\  _  \
\ \ \/\_\  __  __    ____\ \ ,_\   ___     ___ ___    \/_/\ \/ \ \ \/\ \ \ \L\ \
 \ \ \/_/_/\ \/\ \  /',__\\ \ \/  / __`\ /' __` __`\     \ \ \  \ \ \ \ \ \  __ \
  \ \ \L\ \ \ \_\ \/\__, `\\ \ \_/\ \L\ \/\ \/\ \/\ \     \_\ \__\ \ \_\ \ \ \/\ \
   \ \____/\ \____/\/\____/ \ \__\ \____/\ \_\ \_\ \_\    /\_____\\ \_____\ \_\ \_\
    \/___/  \/___/  \/___/   \/__/\/___/  \/_/\/_/\/_/    \/_____/ \/_____/\/_/\/_/

                                                 ______ __
                                                |      |  |.-----.-----.-----.----.
                                                |   ---|  ||  _  |     |  -__|   _|
                                                |______|__||_____|__|__|_____|__|

                                                 CrowdStrike FalconPy v.1.1

optional arguments:
  -h, --help            show this help message and exit
  -n, --nocolor         Disable color output
  -b BASE_URL, --base_url BASE_URL
                        Base URL
  -t TABLE_FORMAT, --table_format TABLE_FORMAT
                        Tabular display format

search arguments:
  -f FILTER, --filter FILTER
                        String to filter results (IOA rule group name)

action arguments:
  -c, --clone           Clone all IOA rule group matches to new rule groups
  -d DELETE, --delete DELETE
                        List of rule group IDs to delete (comma-delimit)

mssp arguments:
  -m MANAGED_TARGETS, --managed_targets MANAGED_TARGETS
                        Comma delimited list of children to clone rules to.

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API Client Secret
```

### Example source code
Source code for this example can be found [here](custom_ioa_clone.py).
