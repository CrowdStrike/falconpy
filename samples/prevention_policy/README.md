![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Prevention Policy examples
The examples in this folder focus on leveraging CrowdStrike's Prevention Policy API.
- [Clone Prevention Policy](#clone-prevention-policy)
- [Create Host Group and add to policy](#create-host-group-and-attach-to-prevention-policy)
- [Prevention Policy Hawk](#manage-prevention-policies-with-prevention-policy-hawk)

## Clone Prevention Policy
This script will clone one or all prevention policies from one CID to another.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Prevention Policy | __READ__, __WRITE__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Clone all policies from one CID to another CID.

```shell
python3 clone_prev_policy.py --source_id $FALCON_CLIENT_ID_SOURCE --source_secret $FALCON_CLIENT_SECRET_SOURCE --dest_id $FALCON_CLIENT_ID_DESTINATION --dest_secret $FALCON_CLIENT_SECRET_DESTINATION
```

> This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute this program without providing credentials for the source CID if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

```shell
python3 clone_prev_policy.py --dest_id $FALCON_CLIENT_ID_DESTINATION --dest_secret $FALCON_CLIENT_SECRET_DESTINATION
```

Only clone a specific policy.

```shell
python3 clone_prev_policy.py --source_id $FALCON_CLIENT_ID_SOURCE --source_secret $FALCON_CLIENT_SECRET_SOURCE --dest_id $FALCON_CLIENT_ID_DESTINATION --dest_secret $FALCON_CLIENT_SECRET_DESTINATION -n POLICY_NAME
```

> API debugging can be enabled using the `-d` argument.

```shell
python3 clone_prev_policy.py -d
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: clone_prev_policy.py [-h] [-d] [-n POLICY_NAME] [--source_id SOURCE_ID] [--source_secret SOURCE_SECRET] --dest_id DEST_ID
                            --dest_secret DEST_SECRET

Prevention Policy cloner.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

╔═╗┬─┐┌─┐┬  ┬┌─┐┌┐┌┌┬┐┬┌─┐┌┐┌  ╔═╗┌─┐┬  ┬┌─┐┬ ┬
╠═╝├┬┘├┤ └┐┌┘├┤ │││ │ ││ ││││  ╠═╝│ ││  ││  └┬┘
╩  ┴└─└─┘ └┘ └─┘┘└┘ ┴ ┴└─┘┘└┘  ╩  └─┘┴─┘┴└─┘ ┴

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

This script will clone one or all prevention policies from one CID to another.

Developed by Don-Swanson-Adobe

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
The source code for this example can be found [here](clone_prev_policy.py).

---

## Create Host Group and attach to prevention policy
This script will create a host group. If a list of prevention policy IDs are provided, the newly created host group is added to each policy in the list. This can assist with complex group creation that may be difficult to perform in the console.

> [!NOTE]
> If you set custom and/or criteria using the API, editing the group in the Falcon console will remove this criteria upon save.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Host Group | __READ__, __WRITE__ |
| Prevention Policy | __READ__, __WRITE__ |

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

Attach the newly created group to two prevention policies.

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
usage: create_attached_group.py [-h] [-d] [-c CHILD] -n GROUP_NAME [-e GROUP_DESCRIPTION] [-t {dynamic,static}]
                                [-a ASSIGNMENT_RULE] [-p POLICIES] [-k CLIENT_ID] [-s CLIENT_SECRET]

Create Host Groups (and add them to Prevention Policies).

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
 .___                                     .
 /   \ .___    ___  _   __   ___  , __   _/_   `   __.  , __
 |,_-' /   \ .'   ` |   /  .'   ` |'  `.  |    | .'   \ |'  `.
 |     |   ' |----' `  /   |----' |    |  |    | |    | |    |
 /     /     `.___,  \/    `.___, /    |  \__/ /  `._.' /    |

                .___          .
                /   \   __.   |   `   ___  `   ___    ____
                |,_-' .'   \  |   | .'   ` | .'   `  (
                |     |    |  |   | |      | |----'  `--.
                /      `._.' /\__ /  `._.' / `.___, \___.'

This script will create a host group. If a list of prevention policy IDs
are provided, the newly created host group is added to each policy in the
list. This can assist with complex group creation that may be difficult
to perform in the console.

Please note: If you use custom and/or criteria here, editing the group in
the Falcon console will remove this criteria upon save.

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
                        List exclusions in a specific child CID (MSSP parents only)

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

## Manage prevention policies with Prevention Policy Hawk
Prevention Policy Hawk demonstrates the Prevention Policy service collection by listing available prevention policies and allowing you to:
- enable or disable the policy
- remove the policy
- edit the policy configuration


### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Prevention Policy | __READ__, __WRITE__ |

### Execution syntax
This example accepts the following input parameters.
| Parameter | Purpose | Category |
| :--- | :--- | :--- |
|  `-h`, `--help` | Show help message and exit | optional | 
| `-r`, `--show_settings` | Display policy settings | display |
| `-z`, `--verbose` | Show all settings, including disabled | display |
| `-e`, `--enable` | Enable the policy | administration |
| `-d`, `--disable` | Disable the policy | administration |
| `-x`, `--delete` | Delete the policy | administration |
| `-i` POLICY_ID,<BR/>`--policy_id` POLICY_ID | ID of a policy to update | update |
| `-p` POLICY_SEARCH_STRING,<BR/>`--policy_search_string` POLICY_SEARCH_STRING | String to match against policy name. | update |
| `-t` POLICY_SETTING,<BR/>`--policy_setting` POLICY_SETTING | Policy settings to modify (comma delimit). | update |
| `-v` POLICY_SETTING_VALUE,<BR/>`--policy_setting_value` POLICY_SETTING_VALUE | Enabled / Disable the setting (True / False) | update |
| `-m` POLICY_SENSITIVITY,<BR/>`--policy_sensitivity` POLICY_SENSITIVITY<BR/><img width="500"> | Sensitivity setting for slider policies.<ul><li>Disabled</li><li>Cautious</li><li>Moderate</li><li>Aggressive</li><li>Extra_Aggressive)</li></ul>Case-_insensitive_<BR/>Comma delimited strings accepted (detection,prevention) | update |
| `-o` SCOPE,<BR/>`--scope` SCOPE | Sensitivity scope (detection / prevention / both) | update |
|  `-f` FALCON_CLIENT_ID,<BR/>`--falcon_client_id` FALCON_CLIENT_ID | Falcon Client ID | always required |
|  `-s` FALCON_CLIENT_SECRET,<BR/>`--falcon_client_secret` FALCON_CLIENT_SECRET | Falcon Client Secret | always required |

#### Examples
These examples demonstrate command line usage of this sample. Commands may be chained on the same command line as long as all actions make sense for the arguments provided.

- [Show command line help.](#show-command-line-help)
- [Show a list of available prevention policies](#show-a-list-of-available-prevention-policies)
- [Show policy configuration along with results](#show-policy-configuration-along-with-results)
- [Show policy configuration with all settings, including disabled settings](#show-policy-configuration-with-all-settings--including-disabled-settings)
- [Search for a policy by name](#search-for-a-policy-by-name)
- [Search for a policy by ID](#search-for-a-policy-by-id)
- [Enable a policy](#enable-a-policy)
- [Disable a policy](#disable-a-policy)
- [Delete a policy](#delete-a-policy)
- [Enable a configuration setting](#enable-a-configuration-setting)
- [Disable a configuration setting](#disable-a-configuration-setting)

##### Show command line help.

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -h
```

[See output example](#command-line-help).


##### Show a list of available prevention policies

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

##### Show policy configuration along with results
> This is the default when there is only one record to display

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -r
```

##### Show policy configuration with all settings, including disabled settings

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -r -z
```

##### Search for a policy by name

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -p SEARCH_STRING
```

###### Example result

```shell
╒══════════════════════════════════╤════════════╤═══════════╤════════════════════════════════════════════════════════════════════════════════════════════════╕
│ Policy                           │ Platform   │ Enabled   │ Policy configuration                                                                           │
╞══════════════════════════════════╪════════════╪═══════════╪════════════════════════════════════════════════════════════════════════════════════════════════╡
│ falconpy-unit-test-l8zsfkxiu9    │ Windows    │ False     │ Enhanced Visibility                                                                            │
│ POLICY_ID                        │            │           │ Additional User Mode Data [AdditionalUserModeData] (Enabled)                                   │
│ FalconPy Unit Test l8zsfkxiu9    │            │           │ Redact HTTP Detection Details [RedactHTTPDetectionDetails] (Enabled)                           │
│                                  │            │           │                                                                                                │
│                                  │            │           │ Cloud Machine Learning                                                                         │
│                                  │            │           │ Adware & PUP [AdwarePUP] (Detection is moderate, Prevention is moderate)                       │
│                                  │            │           │                                                                                                │
│                                  │            │           │ Sensor Machine Learning                                                                        │
│                                  │            │           │ Sensor Anti-malware [OnSensorMLSlider] (Detection is extra aggressive, Prevention is moderate) │
│                                  │            │           │                                                                                                │
│                                  │            │           │ On Write                                                                                       │
│                                  │            │           │ Detect on Write [DetectOnWrite] (Enabled)                                                      │
│                                  │            │           │                                                                                                │
│                                  │            │           │ Quarantine                                                                                     │
│                                  │            │           │ Quarantine & Security Center Registration [NextGenAV] (Enabled)                                │
│                                  │            │           │                                                                                                │
│                                  │            │           │ Execution Blocking                                                                             │
│                                  │            │           │ Intelligence-Sourced Threats [IntelPrevention] (Enabled)                                       │
│                                  │            │           │                                                                                                │
│                                  │            │           │ Exploit Mitigation                                                                             │
│                                  │            │           │ NULL Page Allocation [NullPageAllocation] (Enabled)                                            │
│                                  │            │           │                                                                                                │
│                                  │            │           │ Exploitation Behavior                                                                          │
│                                  │            │           │ Code Injection [ProcessHollowing] (Enabled)                                                    │
│                                  │            │           │                                                                                                │
│                                  │            │           │ Lateral Movement and Credential Access                                                         │
│                                  │            │           │ Windows Logon Bypass ("Sticky Keys") [WindowsLogonBypassStickyKeys] (Enabled)                  │
│                                  │            │           │                                                                                                │
│                                  │            │           │ Remediation                                                                                    │
│                                  │            │           │ Advanced Remediation [AutomatedRemediation] (Enabled)                                          │
╘══════════════════════════════════╧════════════╧═══════════╧════════════════════════════════════════════════════════════════════════════════════════════════╛
```

##### Search for a policy by ID

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i POLICY_ID
```

##### Enable a policy
> You may specify a policy by ID or by using a search string. For multiple matches, the first match is returned.

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET [-i POLICY_ID | -p SEARCH_STRING] -e
```

##### Disable a policy
> You may specify a policy by ID or by using a search string. For multiple matches, the first match is returned.

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET [-i POLICY_ID | -p SEARCH_STRING] -d
```

##### Delete a policy
> You may specify a policy by ID or by using a search string. For multiple matches, the first match is returned.

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET [-i POLICY_ID | -p SEARCH_STRING] -x
```

##### Enable a configuration setting
> You may specify a policy by ID or by using a search string. For multiple matches, the first match is returned.

> You may use the strings `enable` or `true` for the `-v` argument.
```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET [-i POLICY_ID | -p SEARCH_STRING] -t SETTING_NAME -v SETTING_VALUE
```

###### Example
```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -p my_policy -t DriveByDownload -v enable
```

##### Disable a configuration setting
> You may specify a policy by ID or by using a search string. For multiple matches, the first match is returned.

> You may use the strings `disable` or `false` for the `-v` argument.
```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET [-i POLICY_ID | -p SEARCH_STRING] -t SETTING_NAME -v SETTING_VALUE
```

###### Examples

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -p my_policy -t DriveByDownload -v disable
```

Multiple settings may be specified at once using a comma delimited string.

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -p my_policy -t DriveByDownload,AdditionalUserModeData -v enable
```

##### Change a slider configuration setting
> You may specify a policy by ID or by using a search string. For multiple matches, the first match is returned.

> You may use any of the following strings for the `-m` argument:
- `disabled`
- `cautious`
- `moderate`
- `aggressive`
- `extra_aggressive`

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET [-i POLICY_ID | -p SEARCH_STRING] -t SETTING_NAME -m SETTING_VALUE
```

###### Examples
```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -p my_policy -t AdwarePIP -m moderate
```

You may pass two sensitivities as a comma delimited string. The first value will be used for detection and the second value will be used for prevention.

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -p my_policy -t AdwarePIP -m aggressive,moderate
```

Slider-style and boolean configuration settings may be change simultaneously as long as the necessary arguments are provided. Please note changes will be applied to each setting specified. (If you set one to enabled, all will be set to enabled.)

```shell
python3 prevention_policy_hawk.py -f $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -p my_policy -t DriveByDownload,AdwarePIP -t enable -m aggressive,moderate
```

#### Command-line help
Command-line help is available using the `-h` or `--help` parameters.

```shell
% python3 prevention_policy_hawk.py -h
usage: prevention_policy_hawk.py [-h] [-r] [-z] [-e] [-d] [-x] [-i POLICY_ID] [-p POLICY_SEARCH_STRING] [-t POLICY_SETTING] [-v POLICY_SETTING_VALUE] [-m POLICY_SENSITIVITY]
                                 [-o SCOPE] -f FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET

CrowdStrike Falcon Prevention Policy Maintenance utility.

CrowdStrike's
 _______                              __   __
|   _   .----.-----.--.--.-----.-----|  |_|__.-----.-----.
|.  1   |   _|  -__|  |  |  -__|     |   _|  |  _  |     |
|.  ____|__| |_____|\___/|_____|__|__|____|__|_____|__|__|
|:  |
|::.|             _______       __ __
`---'            |   _   .-----|  |__.----.--.--.               .  .
                 |.  1   |  _  |  |  |  __|  |  |            .  .  .  .
                 |.  ____|_____|__|__|____|___  |            .  |  |  .
                 |:  |                    |_____|         .  |        |  .
                 |::.|                                    .              .
                 `---'      ___     ___    _________    . |  (\.|\/|./)  | .   ___   ____
                           |   |   |   |  /    _    \   .   (\ |||||| /)   .  |   | /   /
                           |   |___|   | |    /_\    |  |  (\  |/  \|  /)  |  |   |/   /
                           |           | |           |    (\   |    |   /)    |       /
                           |    ___    | |    ___    |   (\   / \  / \   /)   |       \
                           |   |   |   | |   |   |   |    \              /    |   |\   \
                           |___|   |___| |___|   |___|     \____/\/\____/     |___| \___\
                                                               |0\/0|
                                                                \/\/          FalconPy v1.0
                                                                 \/

Creation date: 2022.02.11           Modification: 2022.05.11
    jhseceng@CrowdStrike                jshcodes@CrowdStrike
    jshcodes@CrowdStrike

Leverages the FalconPy API SDK to update prevention policies within CrowdStrike Falcon.

This solution requires the FalconPy SDK. This project
can be accessed here: https://github.com/CrowdStrike/falconpy

optional arguments:
  -h, --help            show this help message and exit

optional display arguments:
  -r, --show_settings   Display policy settings
  -z, --verbose         Show all settings, including disabled

optional management arguments:
  -e, --enable          Enable the policy
  -d, --disable         Disable the policy
  -x, --delete          Delete the policy
  -debug, --debug       Enable API debugging

optional update arguments:
  -i POLICY_ID, --policy_id POLICY_ID
                        ID of a policy to update
  -p POLICY_SEARCH_STRING, --policy_search_string POLICY_SEARCH_STRING
                        String to match against policy name
  -t POLICY_SETTING, --policy_setting POLICY_SETTING
                        Policy settings to modify (Comma delimit)
  -v POLICY_SETTING_VALUE, --policy_setting_value POLICY_SETTING_VALUE
                        Enabled / Disable the setting (True / False)
  -m POLICY_SENSITIVITY, --policy_sensitivity POLICY_SENSITIVITY
                        Sensitivity setting for slider policies.
                        (Disabled, Cautious, Moderate, Aggressive, Extra_Aggressive)
                        Case-insensitive, comma delimited strings accepted (detection,prevention)
  -o SCOPE, --scope SCOPE
                        Sensitivity scope (detection / prevention / both).

required arguments:
  -f FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        Falcon Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        Falcon Client Secret

```

### Example source code
The source code for this example can be found [here](prevention_policy_hawk.py).
