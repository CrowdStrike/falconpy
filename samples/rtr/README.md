![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Real Time Response examples
The examples within this folder focus on leveraging CrowdStrike's Real Time Response API to respond to security events.

- [Bulk Execute](#bulk-execute-a-command-on-matched-hosts) - Bulk execute a command on multiple hosts that you select by using a search string.
- [Queued Execute](#bulk-execute-a-command-on-matched-hosts-with-queuing) - Bulk execute a command on multiple hosts that are selected by using a search string or a provided list of host AIDs. Execution is queued for offline hosts with request IDs stored to an external file for later result retrieval.
- [Get file from multiple hosts](#get-file-from-multiple-hosts) - Retrieve a file of the same name from multiple hosts.
- [Get host uptime](#get-host-uptime) - Retrieve the uptime for a host using a RTR session and a script command.
- [Get RTR result](#get-rtr-result) - Retrieve the results for previously executed RTR batch commands.
- [Restart Sensor](#restart-sensor) - Restarts the sensor while taking a TCP dump.
- [Script Manager](#script-manager) - Upload and delete RTR scripts for use on endpoints.
- [Dump Process Memory](pid-dump) - Dumps the memory for a running process on a target system.
- [My Little RTR](pony) - Retrieve System Information and draws ASCII art.


## Bulk execute a command on matched hosts
This simple example demonstrates performing batch administrative commands against
multiple hosts. The host list is calculated based upon a string match between the
hostname and a search string you provide at runtime. The command executed is also
provided at runtime, and passed to the target host in Raw format. (Default command: `ls -al`)

You must provide your credentials to the program at runtime, or have them pre-defined within your environment. These
environment variables are called `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET`.

Results are output to the screen broken out by host.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |
| Real Time Response | __READ__, __WRITE__ |
| Real Time Response Admin | __READ__, __WRITE__ |

### Execution syntax
The following command line arguments are accepted.

| Argument | Long argument | Description |
| :-- | :-- | :-- |
|  `-h` | `--help` | Show help message and exit |
|  `-k` _FALCON_CLIENT_ID_ | `--falcon_client_id` _FALCON_CLIENT_ID_ | CrowdStrike Falcon API Client ID |
|  `-s` _FALCON_CLIENT_SECRET_ | `--falcon_client_secret` _FALCON_CLIENT_SECRET_ | CrowdStrike Falcon API Client Secret |
|  `-c` _COMMAND_ | `--command` _COMMAND_ | Command to perform. Defaults to `ls -al`. |
|  `-f` _FIND_ | `--find` _FIND_ | String to match against hostname to select hosts. |
|  `-t` _TIMEOUT_ | `--timeout` _TIMEOUT_ | Timeout duration for command execution in seconds. (Max: 600) |

The only required argument is _find_ (`-f`) which provides the search string to use to match against host names. If you do not have the `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` environment variables defined, then the `-k` and `-s` arguments are also required.

#### Example
This example will return the root directory contents for every host that matches the search string.

```shell
python3 bulk_execute.py -k CLIENT_ID -s CLIENT_SECRET -f search-string
```

You can specify a command to perform with the `-c` argument.

#### Example
This example will return the contents of `/etc/resolv.conf` for each host matched to the search string.

> This example command will only work on Linux or macOS host targets as this file does not exist in this location on Windows hosts.

```shell
python3 bulk_execute.py -k CLIENT_ID -s CLIENT_SECRET -f target -c "cat /etc/resolv.conf"
```

#### Example result

```shell
Starting sessions with target hosts.
Session with target-host-one started successfully. [42025f36-dcc1-4a3d-b4d6-5bed22944c1d]
Session with target-host-two started successfully. [33a06b79-0909-4c25-b51c-ed8a9d7f99f9]
Session with target-host-three started successfully. [a7696c1f-bb01-45be-873d-f98cbab07720]
Session with target-host-four started successfully. [1a61a71b-3f4e-4797-bd3a-cdcdd7ce165f]
Session with target-host-five started successfully. [9d7e1c3f-4bd0-4d0a-95b4-8e4c6b44caa6]

Executing command (`cat /etc/resolv.conf`) against target hosts.

Closing sessions with target hosts.
Session 42025f36-dcc1-4a3d-b4d6-5bed22944c1d deleted successfully.
Session 33a06b79-0909-4c25-b51c-ed8a9d7f99f9 deleted successfully.
Session a7696c1f-bb01-45be-873d-f98cbab07720 deleted successfully.
Session 1a61a71b-3f4e-4797-bd3a-cdcdd7ce165f deleted successfully.
Session 9d7e1c3f-4bd0-4d0a-95b4-8e4c6b44caa6 deleted successfully.

target-host-one
; generated by /usr/sbin/dhclient-script
search us-east-2.compute.internal
options timeout:2 attempts:5
nameserver 10.12.0.2

target-host-two
; generated by /usr/sbin/dhclient-script
search ap-southeast-2.compute.internal
options timeout:2 attempts:5
nameserver 10.7.0.12

target-host-three
; generated by /usr/sbin/dhclient-script
search eu-central-1.compute.internal
options timeout:2 attempts:5
nameserver 10.0.0.2

target-host-four
; generated by /usr/sbin/dhclient-script
search us-east-1.compute.internal
options timeout:2 attempts:5
nameserver 10.40.10.5

target-host-five
; generated by /usr/sbin/dhclient-script
search us-west-2.compute.internal
options timeout:2 attempts:5
nameserver 10.0.1.3
```

### Example source code
The source code for this example can be found [here](bulk_execute.py).

## Bulk execute a command on matched hosts (with queuing)
This simple example demonstrates performing batch administrative commands against
multiple hosts. The host list is calculated based upon a string match between the
hostname and a search string you provide at runtime. The command executed is also
provided at runtime, and passed to the target host in Raw format. (Default command: `ls -al`)
Commands sent to offline hosts are queued for execution when the host is returned
to service. (Expires after 7 days.)

You must provide your credentials to the program at runtime, or have them pre-defined within your environment. These
environment variables are called `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET`.

Results are output to the screen broken out by host.

Queued results are stored to standalone files for consumption using the [Get RTR result](#get-rtr-result) sample.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |
| Real Time Response | __READ__, __WRITE__ |
| Real Time Response Admin | __READ__, __WRITE__ |

### Execution syntax
The following command line arguments are accepted.

| Argument | Long argument | Description |
| :-- | :-- | :-- |
|  `-h` | `--help` | Show help message and exit |
|  `-k` _FALCON_CLIENT_ID_ | `--falcon_client_id` _FALCON_CLIENT_ID_ | CrowdStrike Falcon API Client ID |
|  `-s` _FALCON_CLIENT_SECRET_ | `--falcon_client_secret` _FALCON_CLIENT_SECRET_ | CrowdStrike Falcon API Client Secret |
|  `-c` _COMMAND_ | `--command` _COMMAND_ | Command to perform. Defaults to `ls -al`. |
|  `-f` _FIND_ | `--find` _FIND_ | String to match against hostname to select hosts. |
|  `-l` _LOAD_FILE_ | `--load_file` _LOAD_FILE_ | File containing a list of AIDs to target (JSON or ASCII list). When not provided, the value of _FIND_ will be used to target hosts. |

The only required argument is _find_ (`-f`) which provides the search string to use to match against host names. If you do not have the `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` environment variables defined, then the `-k` and `-s` arguments are also required.

#### Example
This example will return the root directory contents for every host that matches the search string.

```shell
python3 queud_execute.py -k CLIENT_ID -s CLIENT_SECRET -f search-string
```

You can specify a command to perform with the `-c` argument.

#### Example
This example will return the contents of `/etc/resolv.conf` for each host matched to the search string.

> This example command will only work on Linux or macOS host targets as this file does not exist in this location on Windows hosts.

```shell
python3 queued_execute.py -k CLIENT_ID -s CLIENT_SECRET -f target -c "cat /etc/resolv.conf"
```

### Example source code
The source code for this example can be found [here](queued_execute.py).

---

## Get file from multiple hosts
This sample demonstrates retrieving a file of the same name from multiple hosts.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |
| Real Time Response | __READ__, __WRITE__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Retrieve a file from multiple hosts.

```shell
python3 get_file_from_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -n HOSTNAME_SEARCH -f FILENAME
```

> [!TIP]
> Hostname is a stemmed search.

GovCloud users can change their CrowdStrike region using the `-b` argument.

```shell
python3 get_file_from_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -n HOSTNAME_SEARCH -f FILENAME -b usgov1
```

Environment authentication is supported, so this solution can be executed without providing credentials if the environment variables `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` are defined.

```shell
python3 get_file_from_hosts.py -n HOSTNAME_SEARCH -f FILENAME
```

Activate API debug logging with the `-d` argument.

```shell
python3 get_file_from_hosts.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -n HOSTNAME_SEARCH -f FILENAME -d
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: get_file_from_hosts.py [-h] [-d] [-n HOSTNAME] [-b BASE_URL] [-k CLIENT_ID] [-s CLIENT_SECRET] -f FILEPATH

Retrieve a file from multiple hosts.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |        FalconPy v1.3
`-------'                         `-------'
        ____             __   _______
       / __ \___  ____ _/ /  /_  __(_)___ ___  ___
      / /_/ / _ \/ __ `/ /    / / / / __ `__ \/ _ \
     / _, _/  __/ /_/ / /    / / / / / / / / /  __/
    /_/ |_|\___/\__,_/_/    /_/ /_/_/ /_/ /_/\___/
            ____
           / __ \___  _________  ____  ____  ________
          / /_/ / _ \/ ___/ __ \/ __ \/ __ \/ ___/ _ \
         / _, _/  __(__  ) /_/ / /_/ / / / (__  )  __/
        /_/ |_|\___/____/ .___/\____/_/ /_/____/\___/
                       /_/

This program will retrieve a single file of the same name
from multiple hosts. Files will be saved as 7zip archives
named after the host's AID.

Creation date: 11.30.23 - jshcodes@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging
  -n HOSTNAME, --hostname HOSTNAME
                        Hostname to target (stemmed search)
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike API base URL

authentication arguments:
  -k CLIENT_ID, --client-id CLIENT_ID
                        Falcon API client ID
  -s CLIENT_SECRET, --client-secret CLIENT_SECRET
                        Falcon API client ID

required arguments:
  -f FILEPATH, --filepath FILEPATH
                        Filename and path of the file to be downloaded
```

### Example source code
The source code for this example can be found [here](get_file_from_hosts.py).

---

## Get host uptime
Leverages the `runscript` RTR command to retrieve the uptime for host(s) within your environment.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Real Time Response | __WRITE__ |
| Real Time Response Admin | __WRITE__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Retrieve the total running time for one or more hosts within your environment.

> Retrieve all host uptimes (up to 5,000).

```shell
python3 get_host_uptime.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Retrieve the uptime for hosts that match a hostname filter.

```shell
python3 get_host_uptime.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -n HOSTNAME_STRING
```

> Retrieve the uptime for hosts last seen within a certain number of minutes.

```shell
python3 get_host_uptime.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -l 15
```

> GovCloud users can change their CrowdStrike region using the `-b` argument.

```shell
python3 get_host_uptime.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```


#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 get_host_uptime.py -h
usage: get_host_uptime.py [-h] [-n HOSTNAME] [-b BASE_URL] [-l LAST_SEEN] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET

Retrieve uptime using CrowdStrike Falcon Real Time Response.

 ___ ___ _______ __   __
|   Y   |   _   |  |_|__.--------.-----.
|.  |   |.  1   |   _|  |        |  -__|
|.  |   |.  ____|____|__|__|__|__|_____|
|:  1   |:  |
|::.. . |::.|  CrowdStrike FalconPy v1.2
`-------`---'

01.23.23 - Creation date, jshcodes@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -n HOSTNAME, --hostname HOSTNAME
                        Hostname to target.
                        Will handled multiple matches.
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike region.
                        Only required for GovCloud users.
  -l LAST_SEEN, --last_seen LAST_SEEN
                        Amount of time (in minutes) since the host was last seen.

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API client ID.
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API client secret.
```

### Example source code
The source code for this example can be found [here](get_host_uptime.py).

---

## Get RTR result
Retrieve the results for previously executed RTR commands.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Real Time Response Admin | __WRITE__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Retrieve the result for previously executed RTR batch admin commands.

```shell
python3 get_rtr_result.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> GovCloud users can change their CrowdStrike region using the `-b` argument.

```shell
python3 get_rtr_result.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

> Specify the child CID where the commands where executed.

```shell
python3 get_rtr_result.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -m CHILD_CID
```

> Specify a specific cloud request ID.

```shell
python3 get_rtr_result.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c CLOUD_REQUEST_ID
```

> Specify a specific sequence of a specific cloud request ID.

```shell
python3 get_rtr_result.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c CLOUD_REQUEST_ID -q 1
```

> Specify a custom output folder where execution request IDs are stored.

```shell
python3 get_rtr_result.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f results
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 get_rtr_result.py -h
usage: get_rtr_result.py [-h] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET [-m MEMBER_CID] [-b BASE_URL] [-c CLOUD_REQUEST_ID] [-q SEQUENCE] [-f QUEUE_FILE_FOLDER]

Retrieve the results of a command executed via Real Time Response.

 _______             __  _______ __
|   _   .-----.---.-|  ||       |__.--------.-----.
|.  l   |  -__|  _  |  ||.|   | |  |        |  -__|
|.  _   |_____|___._|__|`-|.  |-|__|__|__|__|_____|
|:  |   |                 |:  |
|::.|:. |                 |::.|
`--- ---'                 `---'
             _______
            |   _   .-----.-----.-----.-----.-----.-----.-----.
            |.  l   |  -__|__ --|  _  |  _  |     |__ --|  -__|
            |.  _   |_____|_____|   __|_____|__|__|_____|_____|
            |:  |   |           |__|
            |::.|:. |                       FalconPy v1.1
            `--- ---'

optional arguments:
  -h, --help            show this help message and exit
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API Client Secret
  -m MEMBER_CID, --member_cid MEMBER_CID
                        Child CID for MSSP scenarios
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike Base URL (Only required for GovCloud: usgov1)
  -c CLOUD_REQUEST_ID, --cloud_request_id CLOUD_REQUEST_ID
                        Cloud Request ID to retrieve, accepts comma-delimited lists
  -q SEQUENCE, --sequence SEQUENCE
                        Command result sequence ID, defaults to 0
  -f QUEUE_FILE_FOLDER, --queue_file_folder QUEUE_FILE_FOLDER
                        Load a directory of save files or a single save file for processing
```

### Example source code
The source code for this example can be found [here](get_rtr_result.py).

---

## Restart Sensor
This program creates a RTR Session, drops a script on the host, runs the script, and then finally retrieves the output. The script will start TCPdump and perform a capture while the Falcon Sensor is restarted.

> [!WARNING]
> This example only supports endpoints running Linux operating systems.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| ML Exclusions | __READ__ |
| Flight Control | __READ__ |
| Sensor Download | __READ__ |

> [!NOTE]
> This program can be executed using an API key that is not scoped for the Flight Control (MSSP) service collection, but will be unable to access hosts within child CIDs.

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Execute the example against a specific hostname.

```shell
python3 restart_sensor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -n HOSTNAME
```

Execute the example against a specific AID.

```shell
python3 restart_sensor.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -a AID
```

> This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

```shell
python3 restart_sensor.py
```

> [!TIP]
> This example will automatically identify and restart sensors on hosts within child tenants when provided valid parent API keys.

Activate debugging with the `-d` argument.

```shell
python3 restart_sensor.py -d
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: restart_sensor.py [-h] [-d] [-k CLIENT_ID] [-s CLIENT_SECRET] (-a AID | -n HOSTNAME)

Sensor restart utility.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

  )\.--.   )\.---.   )\  )\    )\.--.     .-./(     /`-.
 (   ._.' (   ,-._( (  \, /   (   ._.'  ,'     )  ,' _  \
  `-.`.    \  '-,    ) \ (     `-.`.   (  .-, (  (  '-' (
 ,_ (  \    ) ,-`   ( ( \ \   ,_ (  \   ) '._\ )  ) ,_ .'
(  '.)  )  (  ``-.   `.)/  ) (  '.)  ) (  ,   (  (  ' ) \
 '._,_.'    )..-.(      '.(   '._,_.'   )/ ._.'   )/   )/

   /`-.   )\.---.    )\.--.  .-,.-.,-.    /`-.      /`-.  .-,.-.,-.
 ,' _  \ (   ,-._(  (   ._.' ) ,, ,. (  ,' _  \   ,' _  \ ) ,, ,. (
(  '-' (  \  '-,     `-.`.   \( |(  )/ (  '-' (  (  '-' ( \( |(  )/
 ) ,_ .'   ) ,-`    ,_ (  \     ) \     )   _  )  ) ,_ .'    ) \
(  ' ) \  (  ``-.  (  '.)  )    \ (    (  ,' ) \ (  ' ) \    \ (
 )/   )/   )..-.(   '._,_.'      )/     )/    )/  )/   )/     )/

This program creates a RTR Session, drops a script on the host, runs
the script, and then finally retrieves the output. The script will start
TCPdump and perform a capture while the Falcon Sensor is restarted.

Developed by @Don-Swanson-Adobe, modified by jshcodes@CrowdStrike

Requirements:
    crowdstrike-falconpy >= 1.3.0
    py7zr

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging

Required arguments:
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API secret
  -a AID, --aid AID     Endpoint AID
  -n HOSTNAME, --hostname HOSTNAME
                        Endpoint Hostname
```

### Example source code
The source code for this example can be found [here](restart_sensor.py).

---

## Script Manager
This program creates a RTR Session, drops a script on the host, runs the script, and then finally retrieves the output. The script will start TCPdump and perform a capture while the Falcon Sensor is restarted.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| ML Exclusions | __READ__ |
| Flight Control | __READ__ |

> [!NOTE]
> This program can be executed using an API key that is not scoped for the Flight Control (MSSP) service collection, but will be unable to upload scripts to child CIDs.

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Upload a script to your tenant.

```shell
python3 script_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -p FILEPATH
```

> [!NOTE]
> `c` will also be accepted for "create".  Create is the default action, and does not need to be specified.

Set script specific parameters.

```shell
python3 script_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -p FILEPATH -n SCRIPT_NAME -x SCRIPT_DESCRIPTION -o PLATFORM -y COMMENTS -z PERMISSIONS
```

> [!TIP]
> The only required argument is `filepath` (`-p` or `--filepath`) when uploading a script.

Delete a script from your tenant.

```shell
python3 script_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -n SCRIPT_NAME -a remove
```

> [!NOTE]
> `r` will also be accepted for "remove".

List all scripts within your tenant.

```shell
python3 script_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -a list
```

> [!NOTE]
> `l` will also be accepted for "list".

> Change the format of the output tabular display with the `-t` argument.

```shell
python3 script_manager.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -t fancy_grid
```

##### Accepted formats
The following table formats are supported:
- `plain`
- `simple`
- `github`
- `grid`
- `simple_grid`
- `rounded_grid`
- `heavy_grid`
- `mixed_grid`
- `double_grid`
- `fancy_grid`
- `outline`
- `simple_outline`
- `rounded_outline`
- `heavy_outline`
- `mixed_outline`
- `double_outline`
- `fancy_outline`
- `pipe`
- `orgtbl`
- `asciidoc`
- `jira`
- `presto`
- `pretty`
- `psql`
- `rst`
- `mediawiki`
- `moinmoin`
- `youtrack`
- `html`
- `unsafehtml`
- `latex`
- `latex_raw`
- `latex_booktabs`
- `latex_longtable`
- `textile`
- `tsv`


Activate MSSP mode with the `-m` argument. This will upload or delete the script within all child CIDs.

```shell
python3 script_manager.py -k $FALCON_CLIENT_ID_PARENT -s $FALCON_CLIENT_SECRET_PARENT -p FILEPATH -m
```

Perform an upload, delete or list operation within a specific child CID using the `-c` argument.

```shell
python3 script_manager.py -k $FALCON_CLIENT_ID_PARENT -s $FALCON_CLIENT_SECRET_PARENT -p FILEPATH -m -c CHILD_CID
```

> This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

```shell
python3 script_manager.py
```

> Activate debugging with the `-d` argument.

```shell
python3 script_manager.py -d
```

> [!TIP]
> This example will automatically identify and restart sensors on hosts within child tenants when provided valid parent API keys.

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: script_manager.py [-h] [-a {create,c,remove,r,list,l}] [-d] [-m] [-c CHILD] [-t TABLE_FORMAT] -p FILEPATH
                         [-n FILENAME] [-x DESCRIPTION] [-o {windows,linux,mac}] [-y COMMENT] [-z {public,private,group}]
                         [-k CLIENT_ID] [-s CLIENT_SECRET]

RTR Script manager.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

      ()                      _ _ _
      /\                _/_  ' ) ) )
     /  )  _. __  o _   /     / / / __.  ____  __.  _,  _  __
    /__/__(__/ (_<_/_)_<__   / ' (_(_/|_/ / <_(_/|_(_)_</_/ (_
                  /                                 /|
                 '                                 |/

This program can upload and delete RTR scripts from your CrowdStrike tenant.
For MSSP scenarios, scripts can be uploaded and removed from all tenants,
or a specific child.

Developed by @Don-Swanson-Adobe, modified by jshcodes@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -a {create,c,remove,r,list,l}, --action {create,c,remove,r,list,l}
                        Action to perform (default is 'create')
  -d, --debug           Enable API debugging
  -m, --mssp            Handle script within all child CIDs (MSSP parents only)
  -c CHILD, --child CHILD
                        Handle scripts within in a specific child CID (MSSP parents only)
  -t TABLE_FORMAT, --table_format TABLE_FORMAT
                        Output table format

File arguments:
  -p FILEPATH, --filepath FILEPATH
                        Path to the script to be uploaded
  -n FILENAME, --filename FILENAME
                        Name for the uploaded script (defaults to script filename)
  -x DESCRIPTION, --description DESCRIPTION
                        Script description
  -o {windows,linux,mac}, --platform {windows,linux,mac}
                        Script platform (defaults to Windows)
  -y COMMENT, --comment COMMENT
                        Script upload comment
  -z {public,private,group}, --permission {public,private,group}
                        Script permissions (public, private, group, defaults to private)

Required arguments:
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API secret
```

### Example source code
The source code for this example can be found [here](script_manager.py).

---