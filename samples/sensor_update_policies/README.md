![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Sensor Update Policies examples
The examples in this folder focus on leveraging CrowdStrike's Sensor Update Policies API to adjust sensor update policy settings.
- [Create Host Group and attach to policy](#create-host-group-and-attach-to-sensor-update-policy)
- [Sensor Update Policy Cloner](#sensor-update-policy-cloner)
- [Policy Wonk](#manage-sensor-update-policies-with-policy-wonk)


## Sensor Update Policy Cloner
This script will clone one or all sensor update policies from one CID to another.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Sensor Update Policy | __READ__, __WRITE__ |

> [!NOTE]
> You will need __READ__  permissions on the _source_ CID and __WRITE__ permissions on the _destination_ CID.

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Clone all policies from one CID to another CID.

```shell
python3 clone_update_policy.py --source_id $FALCON_CLIENT_ID_SOURCE --source_secret $FALCON_CLIENT_SECRET_SOURCE --dest_id $FALCON_CLIENT_ID_DESTINATION --dest_secret $FALCON_CLIENT_SECRET_DESTINATION
```

> This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute this program without providing credentials for the source CID if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

```shell
python3 clone_update_policy.py --dest_id $FALCON_CLIENT_ID_DESTINATION --dest_secret $FALCON_CLIENT_SECRET_DESTINATION
```

Only clone a specific policy.

```shell
python3 clone_update_policy.py --source_id $FALCON_CLIENT_ID_SOURCE --source_secret $FALCON_CLIENT_SECRET_SOURCE --dest_id $FALCON_CLIENT_ID_DESTINATION --dest_secret $FALCON_CLIENT_SECRET_DESTINATION -n POLICY_NAME
```

> API debugging can be enabled using the `-d` argument.

```shell
python3 clone_update_policy.py -d
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: clone_update_policy.py [-h] [-d] [-n POLICY_NAME] [--source_id SOURCE_ID] [--source_secret SOURCE_SECRET] --dest_id DEST_ID --dest_secret
                              DEST_SECRET

Sensor Update Policy cloner.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

╔═╗┌─┐┌┐┌┌─┐┌─┐┬─┐  ╦ ╦┌─┐┌┬┐┌─┐┌┬┐┌─┐  ╔═╗┌─┐┬  ┬┌─┐┬ ┬
╚═╗├┤ │││└─┐│ │├┬┘  ║ ║├─┘ ││├─┤ │ ├┤   ╠═╝│ ││  ││  └┬┘
╚═╝└─┘┘└┘└─┘└─┘┴└─  ╚═╝┴  ─┴┘┴ ┴ ┴ └─┘  ╩  └─┘┴─┘┴└─┘ ┴

       _..._             .-'''-.
    .-'_..._''. .---.   '   _    \
  .' .'      '.\|   | /   /` '.   \    _..._         __.....__
 / .'           |   |.   |     \  '  .'     '.   .-''         '.
. '             |   ||   '      |  '.   .-.   . /     .-''"'-.  `. .-,.--.
| |             |   |\    \     / / |  '   '  |/     /________\   \|  .-. |
| |             |   | `.   ` ..' /  |  |   |  ||                  || |  | |
. '             |   |    '-...-'`   |  |   |  |\    .-------------'| |  | |
 \ '.          .|   |               |  |   |  | \    '-.____...---.| |  '-
  '. `._____.-'/|   |               |  |   |  |  `.             .' | |
    `-.______ / '---'               |  |   |  |    `''-...... -'   | |
             `                      |  |   |  |                    |_|
                                    '--'   '--'

This script will clone one or all sensor update policies from one CID to another.

Developed by @Don-Swanson-Adobe

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging
  -n POLICY_NAME, --policy_name POLICY_NAME
                        Limit cloning to a specific policy

Required arguments:
  --source_id SOURCE_ID
                        CrowdStrike Falcon API key (Source CID)
  --source_secret SOURCE_SECRET
                        CrowdStrike Falcon API secret (Source CID)
  --dest_id DEST_ID     CrowdStrike Falcon API key (Destination CID)
  --dest_secret DEST_SECRET
                        CrowdStrike Falcon API secret (Destination CID)
```

### Example source code
The source code for this example can be found [here](clone_update_policy.py).

---

## Create Host Group and attach to sensor update policy
This script will create a host group. If a list of sensor update policy IDs are provided, the newly created host group is added to each policy in the list. This can assist with complex group creation that may be difficult to perform in the console.

> [!NOTE]
> If you set custom and/or criteria using the API, editing the group in the Falcon console will remove this criteria upon save.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Host Group | __READ__, __WRITE__ |
| Sensor Update Policy | __READ__, __WRITE__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Create a simple host group with no settings.

```shell
python3 create_attached_group.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -n GROUP_NAME
```

> This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute this program without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

```shell
python3 create_attached_group.py -n GROUP_NAME
```

Attach the newly created group to two sensor update policies.

```shell
python3 create_attached_group.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -n GROUP_NAME -p POLICY_ID_1,POLICY_ID_2
```

Create a host group, setting all available parameters.

```shell
python3 create_attached_group.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -n GROUP_NAME -p POLICY_ID_1,POLICY_ID_2 -e GROUP_DESCRIPTION -t GROUP_TYPE -a ASSIGNMENT_RULE
```

> API debugging can be enabled using the `-d` argument.

```shell
python3 create_attached_group.py -d
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: create_group_add_to_update_policy.py [-h] [-d] [-c CHILD] -n GROUP_NAME
                                            [-e GROUP_DESCRIPTION] [-t {dynamic,static}]
                                            [-a ASSIGNMENT_RULE] [-p POLICIES] [-k CLIENT_ID]
                                            [-s CLIENT_SECRET]

Create Host Groups (and add them to Sensor Update Policies).

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

 __  __                .           ___
 |   |    __.    ____ _/_        .'   \  .___    __.  ,   . \,___,
 |___|  .'   \  (      |         |       /   \ .'   \ |   | |    \
 |   |  |    |  `--.   |         |    _  |   ' |    | |   | |    |
 /   /   `._.' \___.'  \__/       `.___| /      `._.' `._/| |`---'
                                                            \

                     .----------------.
                    | .--------------. |
                    | |      _       | |
                    | |     | |      | |
                    | |  ___| |___   | |
                    | | |___   ___|  | |
                    | |     | |      | |
                    | |     |_|      | |
                    | |              | |
                    | '--------------' |
                     '----------------'

     _______. _______ .__   __.      _______.  ______   .______
    /       ||   ____||  \ |  |     /       | /  __  \  |   _  \
   |   (----`|  |__   |   \|  |    |   (----`|  |  |  | |  |_)  |
    \   \    |   __|  |  . `  |     \   \    |  |  |  | |      /
.----)   |   |  |____ |  |\   | .----)   |   |  `--'  | |  |\  \----.
|_______/    |_______||__| \__| |_______/     \______/  | _| `._____|

 __    __  .______    _______       ___   .___________. _______
|  |  |  | |   _  \  |       \     /   \  |           ||   ____|
|  |  |  | |  |_)  | |  .--.  |   /  ^  \ `---|  |----`|  |__
|  |  |  | |   ___/  |  |  |  |  /  /_\  \    |  |     |   __|
|  `--'  | |  |      |  '--'  | /  _____  \   |  |     |  |____
 \______/  | _|      |_______/ /__/     \__\  |__|     |_______|

.______     ______    __       __    ______  __   _______     _______.
|   _  \   /  __  \  |  |     |  |  /      ||  | |   ____|   /       |
|  |_)  | |  |  |  | |  |     |  | |  ,----'|  | |  |__     |   (----`
|   ___/  |  |  |  | |  |     |  | |  |     |  | |   __|     \   \
|  |      |  `--'  | |  `----.|  | |  `----.|  | |  |____.----)   |
| _|       \______/  |_______||__|  \______||__| |_______|_______/

This script will create a host group. If a list of prevention policy IDs
are provided, the newly created host group is added to each policy in the
list. This can assist with complex group creation that may be difficult
to perform in the console.

Please note: If you set custom and/or criteria using the API, editing the
group in the Falcon console will remove this criteria upon save.

Developed by Don-Swanson-Adobe

Dynamic Host group examples with custom and/or criteria

AND Example (Product is Windows AND Type is Server):
    "platform_name:'Windows'+product_type_desc:'Server'"

OR Example (OS is Win Server 2008 R2 OR OS is Windows 7):
"os_version:'Windows Server 2008 R2',os_version:'Windows 7'"
OR Example (OS is Win Server 2008 R2 OR OS is Windows 7)
"(os_version:'Windows Server 2008 R2',os_version:'Windows 7')"

Mixed Use Example (Must Have a DEV Sensor Tag and a T1 or T2 Sensor Tag)
"(tags:'SensorGroupingTags/DEV'+tags:'SensorGroupingTags/T1),(tags:'SensorGroupingTags/DEV'+tags:'SensorGroupingTags/T2')"
"tags:'SensorGroupingTags/DEV'+(tags:'SensorGroupingTags/T1',tags:'SensorGroupingTags/T2')"

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging
  -c CHILD, --child CHILD
                        Perform update in a specific child CID (MSSP parents only)

Group arguments:
  -n GROUP_NAME, --group_name GROUP_NAME
                        Name to use for newly created Host Group
  -e GROUP_DESCRIPTION, --group_description GROUP_DESCRIPTION
                        Description to use for newly created Host Group
  -t {dynamic,static}, --group_type {dynamic,static}
                        Type of Host Group to create (dynamic or static, defaults to dynamic)
  -a ASSIGNMENT_RULE, --assignment_rule ASSIGNMENT_RULE
                        Assignment rule for the newly created Host Group (enclose in double quotes)
  -p POLICIES, --policies POLICIES
                        Prevention Policies IDs to assign this Host Group to (comma delimit)

Required arguments:
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API secret
```

### Example source code
The source code for this example can be found [here](create_attached_group.py).

---

## Manage sensor update policies with Policy Wonk
Manages CrowdStrike Falcon sensor update policy. Using this tool you can enable and disable policies, and their uninstall protection.
You can create and remove policies. Policies can be updated with new host groups and precedence can be reordered.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Host Group | __READ__ |
| Sensor Update Policy | __READ__, __WRITE__ |

### Execution syntax
This example accepts the following input parameters.
| Parameter | Purpose | Category |
| :--- | :--- | :--- |
|  `-h`, `--help` | Show help message and exit | optional |
|  `-l`, `--list_all` | Show all policies (Default action) | list |
|  `-k`, `--kernels` | Show kernel build compatibility details | list |
|  `-b`, `--builds` | Show available builds | list |
|  `-o`, `--host_groups` | Show available host groups | list |
|  `-m`, `--maintenance` | Show maintenance or a specific uninstall token | list |
|  `-v`, `--show_members` | Show policy members in results | list |
|  `-z`, `--show_groups` | Show host groups assigned to policies in results | list |
|  `-q` SEARCH_STRING,<BR/>`--search_string` SEARCH_STRING | String to match against policy or host group name | search |
|  `-c`, `--create` | Create a new policy | create |
|  `-d`, `--disable` | Disable the policy | update and delete |
|  `-e`, `--enable` | Enable the policy | update and delete |
|  `-x`, `--disable_uninstall_protection` | Disable uninstall protection for the policy | update and delete |
|  `-u`, `--enable_uninstall_protection` | Enable uninstall protection for the policy | update and delete |
|  `-p`, `--precedence`<BR/><img width=700> | Set policy precedence to match the order of the list, use the policy_id argument to provide the list | update and delete |
|  `-r`, `--remove` | Remove the policy | update and delete |
|  `-g` ADD_HOST_GROUP,<BR/>`--add_host_group` ADD_HOST_GROUP | Add host group to the specified policy<BR/>(comma delimit) | update and delete |
|  `-y` YANK_HOST_GROUP,<BR/>`--yank_host_group` YANK_HOST_GROUP | Remove host group from the specified policy<BR/>(comma delimit) | update and delete |
|  `-i` POLICY_ID,<BR/>`--policy_id` POLICY_ID | ID(s) of the policy to update or remove (comma delimit) | required for update and delete |
|  `-n` PLATFORM_NAME,<BR/>`--platform_name` PLATFORM_NAME | Platform name for policy precedence configurations | required for update and delete |
|  `-f` FALCON_CLIENT_ID,<BR/>`--falcon_client_id` FALCON_CLIENT_ID | Falcon Client ID | always required |
|  `-s` FALCON_CLIENT_SECRET,<BR/>`--falcon_client_secret` FALCON_CLIENT_SECRET | Falcon Client Secret | always required |

#### Examples
These examples demonstrate command line usage of this sample. Commands may be chained on the same command line as long as all actions make sense for the arguments provided.

* [Show command line help.](#show-command-line-help)
* [List all sensor update policies.](#list-all-sensor-update-policies)
* [List all sensor update policies (display members and host groups).](#list-all-sensor-update-policies--display-members-and-host-groups-)
* [Search for a specific sensor policy by name.](#search-for-a-specific-sensor-policy-by-name)
* [List all available builds.](#list-all-available-builds)
* [List all available kernels.](#list-all-available-kernels)
* [Show bulk maintenance token.](#show-bulk-maintenance-token)
* [Show uninstall token.](#show-uninstall-token-multiple-device-ids-may-be-specified-by-delimiting-with-a-comma)
* [List all available host groups.](#list-all-available-host-groups)
* [Search for a specific host group by name.](#search-for-a-specific-host-group-by-name)
* [Disable a sensor update policy.](#disable-a-sensor-update-policy-multiple-policy-ids-may-be-specified-by-delimiting-with-a-comma)
* [Enable a sensor update policy.](#enable-a-sensor-update-policy-multiple-policy-ids-may-be-specified-by-delimiting-with-a-comma)
* [Disable uninstall protection on a sensor update policy.](#disable-uninstall-protection-on-a-sensor-update-policy-multiple-policy-ids-may-be-specified-by-delimiting-with-a-comma)
* [Enable uninstall protection on a sensor update policy.](#enable-uninstall-protection-on-a-sensor-update-policy-multiple-policy-ids-may-be-specified-by-delimiting-with-a-comma)
* [Add a host group to a sensor update policy.](#add-a-host-group-to-a-sensor-update-policy-multiple-host-groups-and-policy-ids-may-be-specified-by-delimiting-with-a-comma)
* [Remove a host group from a sensor update policy.](#remove-a-host-group-from-a-sensor-update-policy-multiple-host-groups-and-policy-ids-may-be-specified-by-delimiting-with-a-comma)
* [Set policy precedence.](#set-policy-precedence-precedence-will-be-determined-by-the-order-of-the-list-provided)
* [Delete a sensor update policy.](#delete-a-sensor-update-policy)
* [Create a new sensor update policy.](#create-a-new-sensor-update-policy)


##### Show command line help.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -h
```

[See output example](#command-line-help).

##### List all sensor update policies.

```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

##### Change your base URL
You can change your base URL using the `-t` argument. This is only required for GovCloud users.

```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -t usgov1
```

###### Result

```shell
╒══════════════════════════════════╤════════════╤═══════════╤════════════════════════╤══════════════════╤════════════════════╕
│ Name                             │ Platform   │ Enabled   │ Uninstall Protection   │ Sensor version   │ Build              │
╞══════════════════════════════════╪════════════╪═══════════╪════════════════════════╪══════════════════╪════════════════════╡
│ Latest Greatest for Windows      │ Windows    │ True      │ ENABLED                │ 6.33.14704       │ 14704              │
│ policy_id_4                      │            │           │                        │                  │                    │
├──────────────────────────────────┼────────────┼───────────┼────────────────────────┼──────────────────┼────────────────────┤
│ Josh Test Linux                  │ Linux      │ False     │ IGNORE                 │ Not set          │ Not set            │
│ policy_id_5                      │            │           │                        │                  │                    │
├──────────────────────────────────┼────────────┼───────────┼────────────────────────┼──────────────────┼────────────────────┤
│ platform_default                 │ Mac        │ True      │ ENABLED                │ 6.37.15001       │ 15001|n-1|tagged|3 │
│ policy_id_1                      │            │           │                        │                  │                    │
│ Platform default policy          │            │           │                        │                  │                    │
├──────────────────────────────────┼────────────┼───────────┼────────────────────────┼──────────────────┼────────────────────┤
│ platform_default                 │ Linux      │ True      │ IGNORE                 │ Not set          │ Not set            │
│ policy_id_2                      │            │           │                        │                  │                    │
│ Platform default policy          │            │           │                        │                  │                    │
├──────────────────────────────────┼────────────┼───────────┼────────────────────────┼──────────────────┼────────────────────┤
│ platform_default                 │ Windows    │ True      │ DISABLED               │ 6.33.14704       │ 14704              │
│ policy_id_3                      │            │           │                        │                  │                    │
│ Platform default policy          │            │           │                        │                  │                    │
╘══════════════════════════════════╧════════════╧═══════════╧════════════════════════╧══════════════════╧════════════════════╛
```


##### List all sensor update policies (display members and host groups).
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET --show_groups --show_members
```

##### Search for a specific sensor policy by name.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -q SEARCH_STRING
```

##### List all available builds.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b
```

##### List all available kernels.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -k
```

##### Show bulk maintenance token.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -m
```

##### Show uninstall token. Multiple device IDs may be specified by delimiting with a comma.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -m -i DEVICE_ID_1,DEVICE_ID_2,DEVICE_ID_3
```

##### List all available host groups.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -o
```

##### Search for a specific host group by name.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -o -q SEARCH_STRING
```

##### Disable a sensor update policy. Multiple policy IDs may be specified by delimiting with a comma.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d -i POLICY_ID
```

##### Enable a sensor update policy. Multiple policy IDs may be specified by delimiting with a comma.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -e -i POLICY_ID
```

##### Disable uninstall protection on a sensor update policy. Multiple policy IDs may be specified by delimiting with a comma.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -x -i POLICY_ID
```

##### Enable uninstall protection on a sensor update policy. Multiple policy IDs may be specified by delimiting with a comma.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -u POLICY_ID
```

##### Add a host group to a sensor update policy. Multiple host groups and policy IDs may be specified by delimiting with a comma.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -g HOST_GROUP_ID -i POLICY_ID
```

##### Remove a host group from a sensor update policy. Multiple host groups and policy IDs may be specified by delimiting with a comma.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -y HOST_GROUP_ID -i POLICY_ID
```

##### Set policy precedence. Precedence will be determined by the order of the list provided.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -p -i POLICY_ID_1,POLICY_ID_2,POLICY_ID3 -n PLATFORM_NAME
```

##### Delete a sensor update policy.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -r -i POLICY_ID
```

##### Create a new sensor update policy.
```shell
python3 policy_wonk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c
```


#### Command-line help
Command-line help is available using the `-h` or `--help` parameters.

```shell
% python3 policy_wonk.py -h
usage: policy_wonk.py [-h] [-l] [-k] [-b] [-o] [-m] [-v] [-z] [-q SEARCH_STRING] [-c] [-d] [-e] [-x] [-u] [-p] [-r] [-g ADD_HOST_GROUP] [-y YANK_HOST_GROUP] [-i POLICY_ID] [-n PLATFORM_NAME] -f FALCON_CLIENT_ID -s
                      FALCON_CLIENT_SECRET

CrowdStrike Falcon Sensor Update Policy management utilty.

______     _ _               _    _             _
| ___ \   | (_)             | |  | |           | |
| |_/ /__ | |_  ___ _   _   | |  | | ___  _ __ | | __
|  __/ _ \| | |/ __| | | |  | |/\| |/ _ \| '_ \| |/ /
| | | (_) | | | (__| |_| |  \  /\  / (_) | | | |   <
\_|  \___/|_|_|\___|\__, |   \/  \/ \___/|_| |_|_|\_\
                     __/ |
                    |___/    for Sensor Update Policies

                                   FalconPy v1.0

Creation date: 05.06.2022 - jshcodes@CrowdStrike

Required packages
  crowdstrike-falconpy
  tabulate

Multiple simultaneous actions may be performed against
multiple Sensor Update Policy records using this utility.

optional arguments:
  -h, --help            show this help message and exit

list arguments:
  -l, --list_all        Show all policies (Default action)
  -k, --kernels         Show kernel build compatibility details
  -b, --builds          Show available builds
  -o, --host_groups     Show available host groups
  -m, --maintenance     Show maintenance or a specific uninstall token
  -v, --show_members    Show policy members in results
  -z, --show_groups     Show host groups assigned to policies in results

search arguments:
  -q SEARCH_STRING, --search_string SEARCH_STRING
                        String to match against policy or host group name

create arguments:
  -c, --create          Create a new policy

update and delete arguments:
  -d, --disable         Disable the policy
  -e, --enable          Enable the policy
  -x, --disable_uninstall_protection
                        Disable uninstall protection for the policy
  -u, --enable_uninstall_protection
                        Enable uninstall protection for the policy
  -p, --precedence      Set policy precedence (will apply list in order received)
                        Use the policy_id argument to provide the list
  -r, --remove          Remove the policy
  -g ADD_HOST_GROUP, --add_host_group ADD_HOST_GROUP
                        Add host group to the specified policy
                        (comma delimit)
  -y YANK_HOST_GROUP, --yank_host_group YANK_HOST_GROUP
                        Remove host group from the specified policy
                        (comma delimit)

required arguments for updating or removing policies:
  -i POLICY_ID, --policy_id POLICY_ID
                        ID(s) of the policy to update or remove (comma delimit)
  -n PLATFORM_NAME, --platform_name PLATFORM_NAME
                        Platform name for policy precedence configurations

always required arguments:
  -f FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        Falcon Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        Falcon Client Secret
```

### Example source code
The source code for this example can be found [here](policy_wonk.py).
