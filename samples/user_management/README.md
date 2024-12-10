![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# User Management examples
The examples in this folder focus on leveraging CrowdStrike's User Management API to perform administrative operations.
- [Bulk import, update and remove users](#bulk-import-update-and-remove-users)
- [Find Users](#find-users)
- [Get user grants](#get-user-grants)

## Bulk import, update, and remove users
Consumes a provided user list (JSON format) and creates the user accounts as specified in your Falcon tenant.
User roles are assigned as detailed within the file, and can be updated based upon changes made.

A sample of this file (`users.json`) is included in this folder.

### Sample import file format

```json
{
  "resources": [
    {
        "first_name": "User",
        "last_name": "One",
        "uid": "user.one@my-company.com",
        "role_list": ["security_lead", "remote_responder", "image_admin"]
    },
    {
        "first_name": "User",
        "last_name": "Two",
        "uid": "user.two@my-company.com",
        "role_list": ["dashboard_admin"]
    },
    {
        "first_name": "User",
        "last_name": "Three",
        "uid": "user.three@my-company.com",
        "role_list": []
    }
  ]
}

```

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scope:
| Service Collection | Scope |
| :---- | :---- |
| User Management | __READ__, __WRITE__ |

### Execution syntax
The following arguments are accepted at run time.

| Argument | Long Argument | Description |
| :-- | :-- | :-- |
| `-h` | `--help` | show this help message and exit |
| `-d` DATA_FILE | `--data_file` DATA_FILE | File name of user data file |
| `-c` COMMAND | `--command` COMMAND | Action to perform<ul><li>list</li><li>add</li><li>remove</li><li>update</li><li>getroles</li></ul>Defaults to __list__ |
| `-k` FALCON_CLIENT_ID | `--falcon_client_id` FALCON_CLIENT_ID | Falcon Client ID |
| `-s` FALCON_CLIENT_SECRET | `--falcon_client_secret` FALCON_CLIENT_SECRET | Falcon Client Secret |
| `-m` CHILD_CID | `--mssp` CHILD_CID | CID for the child instance you wish to access. (MSSP scenarios only) |
| `-o` SORT | `--sort` SORT  | Field to sort by, one of:<ul><li>firstName</li><li>lastName</li><li>roles</li><li>uid</li><li>uuid</li></ul>Defaults to __lastName__ (_asc_) |
| `-r` | `--reverse` | Reverse the sort order |
| `-n` | `--no_color` | Disable color output in result displays |
| `-t` TABLE_FORMAT | `--table_format` TABLE_FORMAT | Table format to use for display, one of:<ul><li>plain</li><li>simple</li><li>github</li><li>grid</li><li>fancy_grid</li><li>pipe</li><li>orgtbl</li><li>jira</li><li>presto</li><li>pretty</li><li>psql</li><li>rst</li><li>mediawiki</li><li>moinmoin</li><li>youtrack</li><li>html</li><li>unsafehtml</li><li>latext</li><li>latex_raw</li><li>latex_booktabs</li><li>latex_longtable</li><li>textile</li><li>tsv</li></ul> |

```shell
python3 bulk_user.py [-h] -c COMMAND -k CLIENT_ID -s CLIENT_SECRET [-d DATA_FILE] [-o SORT] [-r] [-n] [-t TABLE_FORMAT]
```

#### Listing users
The default command is _list_ which requires no additional input.

```shell
python3 bulk_user.py -k CLIENT_ID -s CLIENT_SECRET
```

#### MSSP access
To access child user data, you will need to provide the child CID when you execute the program.

```shell
python3 bulk_user.py -k CLIENT_ID -s CLIENT_SECRET -m CHILD_CID
```

#### Sorting results
Results may be sorted by column in ascending or descending order using the `-o` and `-r` arguments.

```shell
python3 bulk_user.py -k CLIENT_ID -s CLIENT_SECRET -o roles -r
```

#### Changing table formatting
Table formatting can be adjusted using the `-t` argument. A complete list of available formats can be found in the arguments table above, or by using the `-h` argument to pull up command-line help.


#### Adding users
If your user import file is properly formatted, you can import the entire file with the following command.

```shell
python3 bulk_user.py -k CLIENT_ID -s CLIENT_SECRET -c add -d users.json
```

> You must provide the location of your input file using the `-d` argument.

#### Removing users
Removing users can also be performed based upon your import file contents.

```shell
python3 bulk_user.py -k CLIENT_ID -s CLIENT_SECRET -c remove -d users.json
```

> You must provide the location of your input file using the `-d` argument.

#### Updating users
You can update the roles for users within your input file using the _update_ command.

```shell
python3 bulk_user.py -k CLIENT_ID -s CLIENT_SECRET -c update -d users.json
```

> You must provide the location of your input file using the `-d` argument.

#### Listing available roles
A complete listing of available roles within your tenant can be retrieved using the _getroles_ command.

```shell
python3 bulk_user.py -k CLIENT_ID -s CLIENT_SECRET -c getroles
```

#### Disabling color formatting
Color formatting may be disabled using the `-n` argument. This argument may be mixed with any other command line argument.

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
CrowdStrike Falcon Bulk User Maintenance utility.

 ___ ___                   ___ ___                                                    __
|   Y   .-----.-----.----.|   Y   .---.-.-----.---.-.-----.-----.--------.-----.-----|  |_
|.  |   |__ --|  -__|   _||.      |  _  |     |  _  |  _  |  -__|        |  -__|     |   _|
|.  |   |_____|_____|__|  |. \_/  |___._|__|__|___._|___  |_____|__|__|__|_____|__|__|____|
|:  1   |                 |:  |   |                 |_____|
|::.. . |                 |::.|:. |                          CrowdStrike FalconPy v1.0
`-------'                 `--- ---'

Creation date: 2020.11.06 - jhseceng@CrowdStrike
Modification date: 2022.02.10 - jshcodes@CrowdStrike

Leverages the FalconPy API SDK to add and remove users within Falcon.
Accepts the commands add, remove, update, getroles

This solution requires the FalconPy SDK. This project
can be accessed here: https://github.com/CrowdStrike/falconpy

optional arguments:
  -h, --help            show this help message and exit
  -d DATA_FILE, --data_file DATA_FILE
                        File name of user data file
  -c COMMAND, --command COMMAND
                        Action to perform (add/remove/update/getroles)
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        Falcon Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        Falcon Client Secret
  -o SORT, --sort SORT  Field to sort by, one of:
                        firstName, lastName, uid, uuid
                        Defaults to lastName (asc)
  -r, --reverse         Reverse the sort order
  -n, --no_color        Disable color output in result displays
  -t TABLE_FORMAT, --table_format TABLE_FORMAT
                        Table format to use for display, one of:
                        plain, simple, github, grid, fancy_grid, pipe, orgtbl,
                        jira, presto, pretty, psql, rst, mediawiki, moinmoin,
                        youtrack, html, unsafehtml, latext, latex_raw,
                        latex_booktabs, latex_longtable, textile, or tsv.
```

### Example source code
The source code for this example can be found [here](bulk_user.py).

---

## Find Users
This program will output a list of sensor visibility exclusions and their details for either the current CID or in a specific / each Child CID (Flight Control scenarios).
This can be used for regular audits of sensor visibility exclusions across multiple CIDs.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| ML Exclusions | __READ__ |
| Flight Control | __READ__ |
| Sensor Download | __READ__ |

> [!NOTE]
> This program can be executed using an API key that is not scoped for the Flight Control (MSSP) and Sensor Download service collections, but will be unable to lookup the current CID (Sensor Download) or access child CIDs (Flight Control).

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Execute the default example. This will output results in a tabular format for the local tenant only.

```shell
python3 find_users.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown below without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

```shell
python3 find_users.py
```

Enable MSSP mode and audit all Flight Control children with the `-m` argument.

```shell
python3 find_users.py -k $FALCON_CLIENT_ID_PARENT -s $FALCON_CLIENT_SECRET_PARENT -m
```

Enable MSSP mode and audit a specific Flight Control child with the `-c` argument.

```shell
python3 find_users.py -k $FALCON_CLIENT_ID_PARENT -s $FALCON_CLIENT_SECRET_PARENT -c CHILD_CID
```

> API debugging can be enabled using the `-d` argument.

```shell
python3 find_users.py -d
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: find_users.py [-h] [-d] [-m] [-c CHILD] [-t TABLE_FORMAT] [-k CLIENT_ID] [-s CLIENT_SECRET]

User lookup utility.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

            (`-').->(`-')  _   (`-')  (`-').->
     .->    ( OO)_  ( OO).-/<-.(OO )  ( OO)_
,--.(,--.  (_)--\_)(,------.,------,)(_)--\_)
|  | |(`-')/    _ / |  .---'|   /`. '/    _ /
|  | |(OO )\_..`--.(|  '--. |  |_.' |\_..`--.
|  | | |  \.-._)   \|  .--' |  .   .'.-._)   \
\  '-'(_ .'\       /|  `---.|  |\  \ \       /
 `-----'    `-----' `------'`--' '--' `-----'

This script will list all users in a CID, or child CID(s).

Developed by @Don-Swanson-Adobe

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging
  -m, --mssp            List users in all child CIDs (MSSP parents only)
  -c CHILD, --child CHILD
                        List users in a specific child CID (MSSP parents only)
  -t TABLE_FORMAT, --table_format TABLE_FORMAT
                        Output table format

Required arguments:
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API secret
```

### Example source code
The source code for this example can be found [here](find_users.py).

---

## Get user grants
Asynchronously retrieve a list of all users within the tenant, along with their grants and then
write the results to a comma-delimited text file. This solution is automatically Flight Control
aware and supports API debugging.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scope:
| Service Collection | Scope |
| :---- | :---- |
| User Management | __READ__ |

### Execution syntax
The following arguments are accepted at run time.

| Argument | Long Argument | Description |
| :-- | :-- | :-- |
| `-h` | `--help` | show this help message and exit |
| `-d` | `--debug` | Enable API debugging |
| `-o` OUTPUT | `--output` OUTPUT | CSV output file name |
| `-k` FALCON_CLIENT_ID | `--falcon_client_id` FALCON_CLIENT_ID | Falcon Client ID |
| `-s` FALCON_CLIENT_SECRET | `--falcon_client_secret` FALCON_CLIENT_SECRET | Falcon Client Secret |

```shell
python3 get_user_grants.py [-h] [-d] [-o OUTPUT] [-k CLIENT_ID] [-s CLIENT_SECRET]
```

#### Authentication
For users that have the environment variables `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined, you
do not need to provide authentication detail on the command line.

```shell
python3 get_user_grants.py
```

If you do not have these values defined, you may provide them at runtime via the command line using the `-k` and `-s` arguments.

```shell
python3 get_user_grants.py -k CLIENT_ID -s CLIENT_SECRET
```

#### Outputting results to a different location
You may define the name and location of the resulting output CSV file using the `-o` command line argument.
> Please note: You must provide the trailing slash to specify a directory. (`/` = Mac / Linux, `\` = Windows)

##### Output to a file
```shell
python3 get_user_grants.py -o /path/to/output/file.csv
```

##### Output to a directory
```shell
python3 get_user_grants.py -o /path/to/directory/
```

#### Enabling API debugging.
API debugging may be enabled with the `-d` command line argument.

```shell
python3 get_user_grants.py -d
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: get_user_grants.py [-h] [-d] [-o OUTPUT] [-k CLIENT_ID] [-s CLIENT_SECRET]

Threaded user grant lookup sample.

 ______                         __ _______ __         __ __
|      |.----.-----.--.--.--.--|  |     __|  |_.----.|__|  |--.-----.
|   ---||   _|  _  |  |  |  |  _  |__     |   _|   _||  |    <|  -__|
|______||__| |_____|________|_____|_______|____|__|  |__|__|__|_____|
      ___ ___                   ___ ___                                                    __
     |   Y   .-----.-----.----.|   Y   .---.-.-----.---.-.-----.-----.--------.-----.-----|  |_
     |.  |   |__ --|  -__|   _||.      |  _  |     |  _  |  _  |  -__|        |  -__|     |   _|
     |.  |   |_____|_____|__|  |. \_/  |___._|__|__|___._|___  |_____|__|__|__|_____|__|__|____|
     |:  1   |                 |:  |   |                 |_____|
     |::.. . |                 |::.|:. |                               with Flight Control!
     `-------'                 `--- ---'                                (FalconPy v1.3.0+)

Asynchronously retrieve all user grants for every user defined within the tenant and output
the results to a comma-delimited text file. When not specified, this file is named user_grants.csv.

Creation date: 11.13.2023 - jshcodes@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable debug.
  -o OUTPUT, --output OUTPUT
                        CSV output filename.

authentication arguments (not required if using environment authentication):
  -k CLIENT_ID, --client_id CLIENT_ID
                        Falcon API client ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        Falcon API client secret
```


### Example source code
The source code for this example can be found [here](get_user_grants.py).

---
