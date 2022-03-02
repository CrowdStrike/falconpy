![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)

![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)

# User Management examples
The examples in this folder focus on leveraging CrowdStrike's User Management API to perform administrative operations.
- [Bulk import, update and remove users](#bulk-import-update-and-remove-users)

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
