![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Installation Tokens examples
The examples in this folder focus on leveraging CrowdStrike's Installation Tokens API to manage sensor installation tokens.
- [Token Dispenser](#token-dispenser)

## Token Dispenser
This application displays and manages installation tokens within your CrowdStrike tenant.
> [!NOTE]
> This solution supports Flight Control (MSSP) usage for all functionality, allowing administrators to manage multiple tokens across child tenants with a single command.

- [Requirements](#requirements)
- [Running the program](#running-the-program)
- [Execution syntax](#execution-syntax)
- [Commands](#commands)
- [Source code](#example-source-code)

### Requirements
- [Python 3.7 or greater](https://www.python.org)
- [CrowdStrike FalconPy v1.3.4 or greater](https://github.com/CrowdStrike/falconpy/releases/tag/v1.3.4)
- [pyfiglet](https://pypi.org/project/pyfiglet/)
- [tabulate](https://pypi.org/project/tabulate/)

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scope:
| Service Collection | Scope |
| :---- | :---- |
| Installation Tokens | __READ__, __WRITE__ |

To take advantage of MSSP mode (Flight Control) functionality, you will also need the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Flight Control | __READ__ |
| Sensor Downloads | __READ__ |

> [!NOTE]
> All operations within the Installation Tokens service collection maintain low rate limits. This application automatically backs off and retries the request when these limits are exceeded.

### Execution syntax
This application provides multiple commands, each with unique options.

```shell
python3 token_dispenser.py [-h] command [options]
```

##### Command line help
The menu of commands can be retrieved by providing `-h` on the command line with no other arguments.

```shell
Installation Token management utility.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |       FalconPy v1.3.4
`-------'                         `-------'

_______  _____  _     _ _______ __   _
   |    |     | |____/  |______ | \  |
   |    |_____| |    \_ |______ |  \_|

______  _____ _______  _____  _______ __   _ _______ _______  ______
|     \   |   |______ |_____] |______ | \  | |______ |______ |_____/
|_____/ __|__ ______| |       |______ |  \_| ______| |______ |    \_

               .-------.            with    ________)
               |Jackpot|                   (, /     /) ,     /)
   ____________|_______|____________         /___, //    _  (/  _/_
  |  __    __    ___  _____   __    |     ) /     (/__(_(_/_/ )_(__
  | / _\  / /   /___\/__   \ / _\   |    (_/           .-/
  | \ \  / /   //  //  / /\ \\ \  25|                 (_/  )   ___
  | _\ \/ /___/ \_//  / /  \/_\ \ []|  __                 (__/_____)                   /)
  | \__/\____/\___/   \/     \__/ []| (__)                  /       _____  _/_ __  ___//
  |===_______===_______===_______===|  ||                  /       (_) / (_(__/ (_(_)(/_
  ||*| _____ |*|       |*|  ___  |*||  ||                 (______)
  ||*||     ||*|  /\ _ |*| |_  | |*||  ||
  ||*||*BAR*||*|  \_(_)|*|  / /  |*||  ||
  ||*||_____||*|  (_)  |*| /_/   |*||  ||
  ||*|_______|*|_______|*|_______|*||_//                 Creation date: 11.15.2023
  | \=___________________________=/ |_/                       jshcodes@CrowdStrike
 _|    \_______________________/    |_                            WE STOP BREACHES
(_____________________________________)

positional arguments:
  Token command  Command description
    list (l)     List all tokens [default]
    create (c)   Create tokens
    revoke (x)   Revoke tokens
    restore (r)  Restore tokens
    update (u)   Update tokens
    delete (d)   Delete tokens

optional arguments:
  -h, --help     show this help message and exit
```

### Commands
The token dispenser supports 6 primary commands, each accepting optional arguments that alter how the command is performed.
When using [MSSP mode](#flight-control-mssp-mode-arguments) operations performed cross all tenants.
> Example: Calling the `list` command while also enabling MSSP mode with the `-m` command line argument will show tokens for the parent and all children.

- [List](#list-tokens) - List all tokens within the environment.
- [Create](#create-tokens) - Create one or multiple tokens with a specified expiration and label.
- [Revoke](#revoke-tokens) - Revoke one or multiple tokens by label or ID.
- [Restore](#restore-tokens) - Restore one or multiple tokens by label or ID.
- [Update](#update-tokens) - Update the label or expiration for one or multiple tokens by label or ID.
- [Delete](#delete-tokens) - Delete one or multiple tokens by label or ID.

#### Authentication, display and saving results to a file
All commands accept universal arguments that may be mixed with command-specific arguments.
These arguments control configuration elements that are shared across all available commands such as:
- Authentication
- Flight Control (MSSP mode)
- Display options (such as filtering, sorting and formatting)
- Outputting displayed results to CSV or JSON format

##### Universal arguments
The following options are available as command line arguments regardless of command performed.
Universal arguments may be provided in any order.

###### General, display and output arguments
These arguments allow users to control debug and result display settings.
Results can also be exported to a file in JSON or CSV format using these options.

| Argument | Long Argument | Description | Category |
| :-- | :-- | :-- | :-- |
 | `-h` | `--help` | Show help for the specified command and exit. | General |
 | `-d` | `--debug` | Enable debug. | General |
 | `-f` FILTER | `--filter` FILTER | Filter results by searching token labels (stemmed search). | Display |
 | `-o` ORDER_BY | `--order-by` ORDER_BY | Sort key to use for tabular displays. | Display |
 | `-r` | `--reverse` | Reverses the sort order. | Display |
 | `-t` TABLE_FORMAT | `--table-format` TABLE_FORMAT | Format to use for tabular output. | Display |
 | `-v` | `--show-version` | Show FalconPy version in output. | Display |
 | | `--output-file` OUTPUT_FILE | Output token list results to a CSV or JSON file. | Output |
 | | `--output-format` OUTPUT_FORMAT | Set output file format.<BR/><BR/>Allowed options:<UL><LI>csv</LI><LI>json</LI></UL> | Output |

###### Authentication arguments
> [!NOTE]
> The following arguments are not required when you are using [environment authentication](https://www.falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication).

| Argument | Long Argument | Description | Category |
| :-- | :-- | :-- | :-- |
| `-k` CLIENT_ID | `--client_id` CLIENT_ID | Falcon API client ID. | Authentication |
| `-s` CLIENT_SECRET | `--client_secret` CLIENT_SECRET | Falcon API client secret. | Authentication

###### Flight Control (MSSP mode) arguments
> [!NOTE]
> The following arguments are not required when you are not using Flight Control.

| Argument | Long Argument | Description | Category |
| :-- | :-- | :-- | :-- |
| `-c` CHILD | `--child` CHILD | CID of the child tenant to target. | MSSP |
| `-m` | `--mssp` | Flight Control (MSSP) mode.<BR/>Commands executed are performed within every tenant unless the parent is explicitly skipped. | MSSP |
| | `--skip-parent`| Do not execute commands within the parent tenant. | MSSP |
| | `--show-tenant` | Display tenant CID values as part of execution. | MSSP |

##### Examples
The following examples demonstrate different universal argument variations.

###### Enable debugging
Passing the `-d` (`--debug`) argument will enable API debugging for every operation performed.

```shell
python3 token_dispenser.py -d
```

###### Filter display results by label
The `-f` (`--filter`) option will only display results that include the word "Example" in any position within the label.

```shell
python3 token_dispenser.py -f Example
```

###### Sort display results
You can sort results by any column in the display results using the `-o` (`order-by`) argument.
Using the `-r` (`--reverse`) argument will reverse the sort.

```shell
python3 token_dispenser.py -o status -r
```

###### Change the display table format
You can change the format of the display table to any of the following options using the `-t` (`table-format`) argument.

```shell
python3 token_dispenser.py -t fancy_grid
```

###### *Available table format options*
| | | | | | |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `plain` | `simple` | `github` | `grid` | `simple_grid` | `rounded_grid` |
| `heavy_grid` | `mixed_grid` | `double_grid` | `fancy_grid` | `outline` | `simple_outline` |
| `rounded_outline` | `heavy_outline` | `mixed_outline` | `double_outline` | `fancy_outline` | `pipe` |
| `orgtbl` | `asciidoc` | `jira` | `presto` | `pretty` | `psql` |
| `rst` | `mediawiki` | `moinmoin` | `youtrack` | `html` | `unsafehtml` |
| `latex` | `latex_raw` | `latex_booktabs` | `latex_longtable` | `textile` | `tsv` |


###### Authenticating to a single tenant
If you are not using [Environment Authentication](https://www.falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), you will need to provide authentication detail on the command line using the `-k` (`--client-id`) and `-s` (`--client-secret`) arguments.

```shell
python3 token_dispenser.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

###### Authenticating to a parent tenant and enabling MSSP mode
MSSP mode will perform commands against all child tenants and the parent (if not explicitly skipped using the `--skip-parent` argument).
This includes API calls used to create display results.

```shell
python3 token_dispenser.py -k $PARENT_CLIENT_ID -s $PARENT_CLIENT_SECRET -m
```

###### Authenticating as a parent to a single child
You can also directly authenticate (as a parent) to the child tenant using the `-c` (`--child`) argument.
This argument does not require MSSP mode and may be provided with or without the `-m` argument.

```shell
python3 token_dispenser.py -k $PARENT_CLIENT_ID -s $PARENT_CLIENT_SECRET -c $CHILD_TENANT_CID
```

###### Displaying the tenant ID
You can display the tenant ID for the parent and child tenants before the operation is performed with the `--show-tenant` argument.

```shell
python3 token_dispenser.py --show-tenant
```

---

#### List tokens
The list command is the default command, and is executed when no command is specified.
After the execution of any other command, the list command is executed to display the results generated.

There are no list command-specific arguments. All universal arguments are accepted.

##### Command line help (list)
Command-line help for this command is available when the command is called along with the `-h` argument.

```shell
usage: token_dispenser.py list [-h] [-d] [-f FILTER] [-o ORDER_BY] [-r] [-t TABLE_FORMAT] [-v] [--output-file OUTPUT_FILE] [--output-format {csv,json}] [-k CLIENT_ID] [-s CLIENT_SECRET] [-c CHILD] [-m] [--skip-parent]
                               [--show-tenant]

 _      _     _
| |    (_)   | |
| |     _ ___| |_
| |    | / __| __|
| |____| \__ \ |_
|______|_|___/\__|



optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable debug.
  -f FILTER, --filter FILTER
                        Filter results by searching token labels (stemmed search).
  -o ORDER_BY, --order-by ORDER_BY
                        Sort key to use for tabular displays.
  -r, --reverse         Reverses the sort order.
  -t TABLE_FORMAT, --table-format TABLE_FORMAT
                        Format to use for tabular output.
  -v, --show-version    Show FalconPy version in output.
  --output-file OUTPUT_FILE
                        Output token list results to a CSV or JSON file.
  --output-format {csv,json}
                        Set output file format.

authentication arguments (not required if using environment authentication):
  -k CLIENT_ID, --client_id CLIENT_ID
                        Falcon API client ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        Falcon API client secret

mssp arguments:
  -c CHILD, --child CHILD
                        CID of the child tenant to target.
  -m, --mssp            Flight Control (MSSP) mode.
  --skip-parent         Do not take action within the parent tenant.
  --show-tenant         Display tenant CID values.
```

---

#### Create tokens
Create tokens within your tenant, or across parent and child tenants simultaneously. Supports the creation of multiple tokens with specified expiration dates.
Expiration may be set by number of days or by specifying a specific date in UTC format.

##### Create command arguments
There are two create command-specific required arguments (`token-label` and `expiration`). There are also two optional arguments `count` and `force`.
All [universal arguments](#universal-arguments) are supported and can be mixed with create command arguments in any order or combination.

| Argument | Long Argument | Description | Category |
| :-- | :-- | :-- | :-- |
| | `--force` | Perform the operation without asking for confirmation. | General |
| `-l` TOKEN_LABEL | `--token-label` TOKEN_LABEL | Label for the token. | Create |
| `-e` EXPIRATION | `--expiration` EXPIRATION | Token expiration.<BR/>(number of days or a specific date in `YYYY-mm-ddTHH:MM:SSZ` format). | Create |
| `-n` COUNT | `--count` COUNT | Number of tokens to create. | Create |

##### Examples
The following examples demonstrate different create command variations.

###### Create a single token in a standard tenant
This example will create a token labeled "ExampleToken" with an expiration of 5 days from now.

```shell
python3 token_dispenser.py create -l ExampleToken -e 5
```

##### Flight Control examples
> [!IMPORTANT]
> You must provide either the MSSP mode (`-m`) or the child (`-c`) argument in order to execute operations within child tenants.

###### Create a single token across the parent and child tenants
This example will create a token labeled "ExampleToken" with an expiration 10 days from now in the parent and every child tenant.

```shell
python3 token_dispenser.py create -l ExampleToken -e 10 -m
```

###### Create multiple tokens in all child tenants but do not create one in the parent
This example will create three tokens with a specific expiration date, labeled "ExampleToken1", "ExampleToken2", and "ExampleToken3" within child tenants.
The parent tenant will remain unchanged as the `skip-parent` argument has been provided.

```shell
python3 token_dispenser.py create -l ExampleToken -e 2025-01-01T00:00:01Z -n 3 -m --skip-parent
```

> [!NOTE]
> To skip the confirmation dialog presented when performing multi-tenant operations, provide the `--force` argument. This argument has no impact on operations where a confirmation dialog is not normally presented.

##### Command line help (create)
Command-line help for this command is available when the command is called along with the `-h` argument.

```shell
usage: token_dispenser.py create [-h] -l TOKEN_LABEL -e EXPIRATION [-n COUNT] [--force] [-d] [-f FILTER] [-o ORDER_BY] [-r] [-t TABLE_FORMAT] [-v] [--output-file OUTPUT_FILE] [--output-format {csv,json}] [-k CLIENT_ID]
                                 [-s CLIENT_SECRET] [-c CHILD] [-m] [--skip-parent] [--show-tenant]

  _____                _
 / ____|              | |
| |     _ __ ___  __ _| |_ ___
| |    | '__/ _ \/ _` | __/ _ \
| |____| | |  __/ (_| | ||  __/
 \_____|_|  \___|\__,_|\__\___|



optional arguments:
  -h, --help            show this help message and exit
  -n COUNT, --count COUNT
                        Number of tokens to create
  --force               Perform the operation without asking for confirmation.
  -d, --debug           Enable debug.
  -f FILTER, --filter FILTER
                        Filter results by searching token labels (stemmed search).
  -o ORDER_BY, --order-by ORDER_BY
                        Sort key to use for tabular displays.
  -r, --reverse         Reverses the sort order.
  -t TABLE_FORMAT, --table-format TABLE_FORMAT
                        Format to use for tabular output.
  -v, --show-version    Show FalconPy version in output.
  --output-file OUTPUT_FILE
                        Output token list results to a CSV or JSON file.
  --output-format {csv,json}
                        Set output file format.

required arguments:
  -l TOKEN_LABEL, --token-label TOKEN_LABEL
                        Label for the token.
  -e EXPIRATION, --expiration EXPIRATION
                        Token expiration (number of days or YYYY-mm-ddTHH:MM:SSZ).

authentication arguments (not required if using environment authentication):
  -k CLIENT_ID, --client_id CLIENT_ID
                        Falcon API client ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        Falcon API client secret

mssp arguments:
  -c CHILD, --child CHILD
                        CID of the child tenant to target.
  -m, --mssp            Flight Control (MSSP) mode.
  --skip-parent         Do not take action within the parent tenant.
  --show-tenant         Display tenant CID values.
```

---

#### Revoke tokens
Revoke tokens within your tenant, or across parent and child tenants simultaneously. Supports the revocation of multiple tokens.

##### Revoke command arguments
There are two revoke command-specific required arguments (`token-id` and `token-label`). These arguments are mutually exclusive. There is one optional argument `force`.
All [universal arguments](#universal-arguments) are supported and can be mixed with create command arguments in any order or combination.

| Argument | Long Argument | Description | Category |
| :-- | :-- | :-- | :-- |
| | `--force` | Perform the operation without asking for confirmation. | General |
| `-i` TOKEN_ID | `--token-id` TOKEN_ID | ID of the token to revoke. | Revoke |
| `-l` TOKEN_LABEL | `--token-label` TOKEN_LABEL | Label of the token to revoke (starts with match). | Revoke |

##### Examples
The following examples demonstrate different revoke command variations.

###### Revoke tokens in a standard tenant
This example will revoke any token with a label starting with "ExampleToken".

```shell
python3 token_dispenser.py revoke -l ExampleToken
```

You can also revoke specific tokens by ID.

```shell
python3 token_dispenser.py delete -i $TOKEN_ID
```

##### Flight Control examples
> [!IMPORTANT]
> You must provide the MSSP mode (`-m`) argument in order to access child tenants. If you wish processing to only occur within child tenants, you must provide the `--skip-parent` argument.

###### Revoke a single token in a child tenant
This example will revoke a single token within a child tenant.

```shell
python3 token_dispenser.py revoke -i $TOKEN_ID -c $CHILD_TENANT_CID
```

You can also accomplish this leveraging MSSP mode. All child tenants will be searched for a token that matches the ID.

```shell
python3 token_dispenser.py revoke -i $TOKEN_ID -m
```

###### Revoke tokens in a child tenant that have a label starting with a specific string
This example will revoke tokens labeled "ExampleToken" (or any variation starting with this string) within child tenants.

```shell
python3 token_dispenser.py revoke -l ExampleToken -c $CHILD_TENANT_CID
```

You can also accomplish this leveraging MSSP mode. All child tenants will be searched for labels that match the specified string.

```shell
python3 token_dispenser.py revoke -l ExampleToken -m
```

> [!NOTE]
> To skip the confirmation dialog presented when performing multi-tenant operations, provide the `--force` argument. This argument has no impact on operations where a confirmation dialog is not normally presented.

##### Command line help (revoke)
Command-line help for this command is available when the command is called along with the `-h` argument.

```shell
usage: token_dispenser.py revoke [-h] (-i TOKEN_ID | -l TOKEN_LABEL) [--force] [-d] [-f FILTER] [-o ORDER_BY] [-r] [-t TABLE_FORMAT] [-v] [--output-file OUTPUT_FILE] [--output-format {csv,json}] [-k CLIENT_ID]
                                 [-s CLIENT_SECRET] [-c CHILD] [-m] [--skip-parent] [--show-tenant]

 _____                 _
|  __ \               | |
| |__) |_____   _____ | | _____
|  _  // _ \ \ / / _ \| |/ / _ \
| | \ \  __/\ V / (_) |   <  __/
|_|  \_\___| \_/ \___/|_|\_\___|



optional arguments:
  -h, --help            show this help message and exit
  --force               Perform the operation without asking for confirmation.
  -d, --debug           Enable debug.
  -f FILTER, --filter FILTER
                        Filter results by searching token labels (stemmed search).
  -o ORDER_BY, --order-by ORDER_BY
                        Sort key to use for tabular displays.
  -r, --reverse         Reverses the sort order.
  -t TABLE_FORMAT, --table-format TABLE_FORMAT
                        Format to use for tabular output.
  -v, --show-version    Show FalconPy version in output.
  --output-file OUTPUT_FILE
                        Output token list results to a CSV or JSON file.
  --output-format {csv,json}
                        Set output file format.

required arguments (mutually exclusive):
  -i TOKEN_ID, --token-id TOKEN_ID
                        ID of the token to revoke.
  -l TOKEN_LABEL, --token-label TOKEN_LABEL
                        Label of the token to revoke (starts with match).

authentication arguments (not required if using environment authentication):
  -k CLIENT_ID, --client_id CLIENT_ID
                        Falcon API client ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        Falcon API client secret

mssp arguments:
  -c CHILD, --child CHILD
                        CID of the child tenant to target.
  -m, --mssp            Flight Control (MSSP) mode.
  --skip-parent         Do not take action within the parent tenant.
  --show-tenant         Display tenant CID values.
```

---

#### Restore tokens
Restore tokens within your tenant, or across parent and child tenants simultaneously. Supports the restoration of multiple tokens.

##### Restore command arguments
There are two restore command-specific required arguments (`token-id` and `token-label`). These arguments are mutually exclusive. There is one optional argument `force`.
All [universal arguments](#universal-arguments) are supported and can be mixed with create command arguments in any order or combination.

| Argument | Long Argument | Description | Category |
| :-- | :-- | :-- | :-- |
| | `--force` | Perform the operation without asking for confirmation. | General |
| `-i` TOKEN_ID | `--token-id` TOKEN_ID | ID of the token to restore. | Restore |
| `-l` TOKEN_LABEL | `--token-label` TOKEN_LABEL | Label of the token to restore (starts with match). | Restore |

##### Examples
The following examples demonstrate different restore command variations.

###### Restore tokens in a standard tenant
This example will restore any token with a label starting with "ExampleToken".

```shell
python3 token_dispenser.py restore -l ExampleToken
```

You can also restore specific tokens by ID.

```shell
python3 token_dispenser.py restore -i $TOKEN_ID
```

##### Flight Control examples
> [!IMPORTANT]
> You must provide the MSSP mode (`-m`) argument in order to access child tenants. If you wish processing to only occur within child tenants, you must provide the `--skip-parent` argument.

###### Restore a single token in a child tenant
This example will restore a single token within a child tenant.

```shell
python3 token_dispenser.py restore -i $TOKEN_ID -c $CHILD_TENANT_CID
```

You can also accomplish this leveraging MSSP mode. All child tenants will be searched for a token that matches the ID.

```shell
python3 token_dispenser.py restore -i $TOKEN_ID -m
```

###### Restore tokens in a child tenant that have a label starting with a specific string
This example will restore tokens labeled "ExampleToken" (or any variation starting with this string) within child tenants.

```shell
python3 token_dispenser.py restore -l ExampleToken -c $CHILD_TENANT_CID
```

You can also accomplish this leveraging MSSP mode. All child tenants will be searched for labels that match the specified string.

```shell
python3 token_dispenser.py restore -l ExampleToken -m
```

> [!NOTE]
> To skip the confirmation dialog presented when performing multi-tenant operations, provide the `--force` argument. This argument has no impact on operations where a confirmation dialog is not normally presented.

##### Command line help (restore)
Command-line help for this command is available when the command is called along with the `-h` argument.

```shell
usage: token_dispenser.py restore [-h] (-i TOKEN_ID | -l TOKEN_LABEL) [--force] [-d] [-f FILTER] [-o ORDER_BY] [-r] [-t TABLE_FORMAT] [-v] [--output-file OUTPUT_FILE] [--output-format {csv,json}] [-k CLIENT_ID]
                                  [-s CLIENT_SECRET] [-c CHILD] [-m] [--skip-parent] [--show-tenant]

 _____           _
|  __ \         | |
| |__) |___  ___| |_ ___  _ __ ___
|  _  // _ \/ __| __/ _ \| '__/ _ \
| | \ \  __/\__ \ || (_) | | |  __/
|_|  \_\___||___/\__\___/|_|  \___|



optional arguments:
  -h, --help            show this help message and exit
  --force               Perform the operation without asking for confirmation.
  -d, --debug           Enable debug.
  -f FILTER, --filter FILTER
                        Filter results by searching token labels (stemmed search).
  -o ORDER_BY, --order-by ORDER_BY
                        Sort key to use for tabular displays.
  -r, --reverse         Reverses the sort order.
  -t TABLE_FORMAT, --table-format TABLE_FORMAT
                        Format to use for tabular output.
  -v, --show-version    Show FalconPy version in output.
  --output-file OUTPUT_FILE
                        Output token list results to a CSV or JSON file.
  --output-format {csv,json}
                        Set output file format.

required arguments (mutually exclusive):
  -i TOKEN_ID, --token-id TOKEN_ID
                        ID of the token to restore.
  -l TOKEN_LABEL, --token-label TOKEN_LABEL
                        Label of the token to restore (starts with match).

authentication arguments (not required if using environment authentication):
  -k CLIENT_ID, --client_id CLIENT_ID
                        Falcon API client ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        Falcon API client secret

mssp arguments:
  -c CHILD, --child CHILD
                        CID of the child tenant to target.
  -m, --mssp            Flight Control (MSSP) mode.
  --skip-parent         Do not take action within the parent tenant.
  --show-tenant         Display tenant CID values.
```

---

#### Update tokens
Update tokens within your tenant, or across parent and child tenants simultaneously. Supports the restoration of multiple tokens.

##### Update command arguments
There are two sets of update command-specific required arguments. The first set includes `token-id` and `token-label` which are mutually exclusive to each other.
The second set of required arguments includes `add-days`, `expiration` and `new_token_label`. These three are mutually exclusive to each other. There is one optional argument `force`.
All [universal arguments](#universal-arguments) are supported and can be mixed with create command arguments in any order or combination.

| Argument | Long Argument | Description | Category |
| :-- | :-- | :-- | :-- |
| | `--force` | Perform the operation without asking for confirmation. | General |
| `-i` TOKEN_ID | `--token-id` TOKEN_ID | ID of the token to update. | Update |
| `-l` TOKEN_LABEL | `--token-label` TOKEN_LABEL | Label of the token to update (starts with match). | Update |
| `-a` ADD_DAYS | `--add-days` ADD_DAYS | Add specified number of days to token expiration. |
| `-e` EXPIRATION | `--expiration` EXPIRATION | Token expiration (`YYYY-mm-ddTHH:MM:SSZ` format). | Update |
| `-n` NEW_TOKEN_LABEL | `--new-label` NEW_TOKEN_LABEL | New label for the token. | Update |

##### Examples
The following examples demonstrate different update command variations.

###### Update tokens in a standard tenant to extend the expiration
This example will update all tokens with a label starting with "ExampleToken" and add 5 days to the expiration.

```shell
python3 token_dispenser.py update -l ExampleToken -a 5
```

You can also update specific tokens by ID.

```shell
python3 token_dispenser.py update -i $TOKEN_ID -a 5
```

###### Update tokens in a standard tenant to a specific expiration
This example will update all tokens with a label starting with "ExampleToken" to have the specified expiration date.

```shell
python3 token_dispenser.py update -l ExampleToken -e 2025-01-01T12:01:01Z
```

You can also perform this update on a specific token by providing the ID.

```shell
python3 token_dispenser.py update -i $TOKEN_ID -e 2025-01-01T12:01:01Z
```

###### Change the label of tokens within a standard tenant
This example will change the label for any token with a label starting with "ExampleToken" to be "NewExampleToken". If multiple tokens are renamed within a tenant, a number will be appended at the end of each.

```shell
python3 token_dispenser.py update -l ExampleToken -n NewExampleToken
```

You can also update a token label by providing the specific token ID.

```shell
python3 token_dispenser.py delete -i $TOKEN_ID -n NewExampleToken
```

##### Flight Control examples
> [!IMPORTANT]
> You must provide the MSSP mode (`-m`) argument in order to access child tenants. If you wish processing to only occur within child tenants, you must provide the `--skip-parent` argument.

###### Update a single token to extend the expiration
This example will update a single token within a parent or child tenant to add 5 days to the expiration.

```shell
python3 token_dispenser.py update -i $TOKEN_ID -c $CHILD_TENANT_CID -a 5
```

You can also accomplish this leveraging MSSP mode. All child tenants will be searched for the token with the matching ID.

```shell
python3 token_dispenser.py update -i $TOKEN_ID -m -a 5
```

###### Update tokens that have a label starting with a specific string to a specific expiration
This example will update tokens labeled "ExampleToken" (or any variation starting with this string) within the parent and child tenants to have the specified expiration date.

```shell
python3 token_dispenser.py update -l ExampleToken -c $CHILD_TENANT_CID -e 2025-01-01T12:01:01Z
```

You can also accomplish this leveraging MSSP mode. All child tenants will be searched for labels that match the specified string.

```shell
python3 token_dispenser.py update -l ExampleToken -m -e 2025-01-01T12:01:01Z
```

###### Changing the label of a token
This example will change the label for the token "ExampleToken" to be "NewExampleToken" within the tenant it is found.

```shell
python3 token_dispenser.py update -i $TOKEN_ID -m -n NewExampleToken
```

This example will change the label for any token matching "ExampleToken" to be "NewExampleToken" within the tenant it is found. If multiple tokens are updated within a tenant, a number will be appended to the end of each.

```shell
python3 token_dispenser.py update -l ExampleToken -m -n NewExampleToken
```

> [!NOTE]
> To skip the confirmation dialog presented when performing multi-tenant operations, provide the `--force` argument. This argument has no impact on operations where a confirmation dialog is not normally presented.

##### Command line help (update)
Command-line help for this command is available when the command is called along with the `-h` argument.

```shell
usage: token_dispenser.py update [-h] (-i TOKEN_ID | -l TOKEN_LABEL) (-a ADD_DAYS | -e EXPIRATION | -n NEW_TOKEN_LABEL) [--force] [-d] [-f FILTER] [-o ORDER_BY] [-r] [-t TABLE_FORMAT] [-v] [--output-file OUTPUT_FILE]
                                 [--output-format {csv,json}] [-k CLIENT_ID] [-s CLIENT_SECRET] [-c CHILD] [-m] [--skip-parent] [--show-tenant]

 _    _           _       _
| |  | |         | |     | |
| |  | |_ __   __| | __ _| |_ ___
| |  | | '_ \ / _` |/ _` | __/ _ \
| |__| | |_) | (_| | (_| | ||  __/
 \____/| .__/ \__,_|\__,_|\__\___|
       | |
       |_|

optional arguments:
  -h, --help            show this help message and exit
  --force               Perform the operation without asking for confirmation.
  -d, --debug           Enable debug.
  -f FILTER, --filter FILTER
                        Filter results by searching token labels (stemmed search).
  -o ORDER_BY, --order-by ORDER_BY
                        Sort key to use for tabular displays.
  -r, --reverse         Reverses the sort order.
  -t TABLE_FORMAT, --table-format TABLE_FORMAT
                        Format to use for tabular output.
  -v, --show-version    Show FalconPy version in output.
  --output-file OUTPUT_FILE
                        Output token list results to a CSV or JSON file.
  --output-format {csv,json}
                        Set output file format.

required arguments:
  -i TOKEN_ID, --token-id TOKEN_ID
                        ID of the token to update.
  -l TOKEN_LABEL, --token-label TOKEN_LABEL
                        Label of the token to update (starts with match).
  -a ADD_DAYS, --add-days ADD_DAYS
                        Add specified number of days to token expiration.
  -e EXPIRATION, --expiration EXPIRATION
                        Token expiration (YYYY-mm-ddTHH:MM:SSZ).
  -n NEW_TOKEN_LABEL, --new-label NEW_TOKEN_LABEL
                        New label for the token.

authentication arguments (not required if using environment authentication):
  -k CLIENT_ID, --client_id CLIENT_ID
                        Falcon API client ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        Falcon API client secret

mssp arguments:
  -c CHILD, --child CHILD
                        CID of the child tenant to target.
  -m, --mssp            Flight Control (MSSP) mode.
  --skip-parent         Do not take action within the parent tenant.
  --show-tenant         Display tenant CID values.
```

#### Delete tokens
Delete tokens within your tenant, or across parent and child tenants simultaneously. Supports the restoration of multiple tokens.

##### Delete command arguments
There are two delete command-specific required arguments (`token-id` and `token-label`). These arguments are mutually exclusive. There is one optional argument `force`.
All [universal arguments](#universal-arguments) are supported and can be mixed with create command arguments in any order or combination.

| Argument | Long Argument | Description | Category |
| :-- | :-- | :-- | :-- |
| | `--force` | Perform the operation without asking for confirmation. | General |
| `-i` TOKEN_ID | `--token-id` TOKEN_ID | ID of the token to delete. | Delete |
| `-l` TOKEN_LABEL | `--token-label` TOKEN_LABEL | Label of the token to delete (starts with match). | Delete |

##### Examples
The following examples demonstrate different delete command variations.

###### Delete tokens in a standard tenant
This example will delete any token with a label starting with "ExampleToken".

```shell
python3 token_dispenser.py delete -l ExampleToken
```

You can also delete specific tokens by ID.

```shell
python3 token_dispenser.py delete -i $TOKEN_ID
```

##### Flight Control examples
> [!IMPORTANT]
> You must provide the MSSP mode (`-m`) argument in order to access child tenants. If you wish processing to only occur within child tenants, you must provide the `--skip-parent` argument.

###### Delete a single token in a child tenant
This example will delete a single token within a child tenant.

```shell
python3 token_dispenser.py delete -i $TOKEN_ID -c $CHILD_TENANT_CID
```

You can also accomplish this leveraging MSSP mode. All child tenants will be searched for a token that matches the ID.

```shell
python3 token_dispenser.py delete -i $TOKEN_ID -m
```

###### Delete tokens in a child tenant that have a label starting with a specific string
This example will delete tokens labeled "ExampleToken" (or any variation starting with this string) within child tenants.

```shell
python3 token_dispenser.py delete -l ExampleToken -c $CHILD_TENANT_CID
```

You can also accomplish this leveraging MSSP mode. All child tenants will be searched for labels that match the specified string.

```shell
python3 token_dispenser.py delete -l ExampleToken -m
```

> [!NOTE]
> To skip the confirmation dialog presented when performing multi-tenant operations, provide the `--force` argument. This argument has no impact on operations where a confirmation dialog is not normally presented.

##### Command line help (delete)
Command-line help for this command is available when the command is called along with the `-h` argument.

```shell
usage: token_dispenser.py delete [-h] (-i TOKEN_ID | -l TOKEN_LABEL) [--force] [-d] [-f FILTER] [-o ORDER_BY] [-r] [-t TABLE_FORMAT] [-v] [--output-file OUTPUT_FILE] [--output-format {csv,json}] [-k CLIENT_ID]
                                 [-s CLIENT_SECRET] [-c CHILD] [-m] [--skip-parent] [--show-tenant]

 _____       _      _
|  __ \     | |    | |
| |  | | ___| | ___| |_ ___
| |  | |/ _ \ |/ _ \ __/ _ \
| |__| |  __/ |  __/ ||  __/
|_____/ \___|_|\___|\__\___|



optional arguments:
  -h, --help            show this help message and exit
  --force               Perform the operation without asking for confirmation.
  -d, --debug           Enable debug.
  -f FILTER, --filter FILTER
                        Filter results by searching token labels (stemmed search).
  -o ORDER_BY, --order-by ORDER_BY
                        Sort key to use for tabular displays.
  -r, --reverse         Reverses the sort order.
  -t TABLE_FORMAT, --table-format TABLE_FORMAT
                        Format to use for tabular output.
  -v, --show-version    Show FalconPy version in output.
  --output-file OUTPUT_FILE
                        Output token list results to a CSV or JSON file.
  --output-format {csv,json}
                        Set output file format.

required arguments (mutually exclusive):
  -i TOKEN_ID, --token-id TOKEN_ID
                        ID of the token to remove.
  -l TOKEN_LABEL, --token-label TOKEN_LABEL
                        Label of the token to remove (starts with match).

authentication arguments (not required if using environment authentication):
  -k CLIENT_ID, --client_id CLIENT_ID
                        Falcon API client ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        Falcon API client secret

mssp arguments:
  -c CHILD, --child CHILD
                        CID of the child tenant to target.
  -m, --mssp            Flight Control (MSSP) mode.
  --skip-parent         Do not take action within the parent tenant.
  --show-tenant         Display tenant CID values.
```

### Example source code
The source code for this example can be found [here](token_dispenser.py).