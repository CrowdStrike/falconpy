![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Falcon Flight Control (MSSP) examples
The examples within this folder focus on leveraging CrowdStrike's Falcon Flight Control to interact with child hosts.

- [Retrieve child CID for a host](#retrieve-child-cid-for-a-host)
- [Get Child Prevention Policies](#get-child-prevention-policies)
- [Host Group Duplicator](#host-group-duplicator)
- [Execute a command on hosts across multiple children](#execute-a-command-on-hosts-across-multiple-children)

## Retrieve child CID for a host
Retrieves the child CID for a specified hostname.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Flight Control | __READ__ |
| Hosts | __READ__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Retrieve the CID for a host within a child tenant.

```shell
python3 find_child_cid.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f HOSTNAME
```

> GovCloud users can change their CrowdStrike region using the `-b` argument.

```shell
python3 find_child_cid.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f HOSTNAME -b usgov1
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 find_child_cid.py -h
usage: find_child_cid.py [-h] -k CLIENT_ID -s CLIENT_SECRET [-b BASE_URL] -f FIND_HOST

Falcon Flight Control child host CID lookup.

optional arguments:
  -h, --help            show this help message and exit
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API key secret
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike API region (us1, us2, eu1, usgov1) NOT required unless you are using `usgov1`
  -f FIND_HOST, --find_host FIND_HOST
                        Hostname or Device ID to identify
```

### Example source code
The source code for this example can be found [here](find_child_cid.py).

## Get Child Prevention Policies
Retrieve prevention policies for some or all child tenants.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Flight Control | __READ__ |
| Prevention Policies | __READ__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Retrieve prevention policies for all child tenants.

```shell
python3 get_child_prevention_policies.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Retrieve prevention policies for specific child tenants.

```shell
python3 get_child_prevention_policies.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c CHILD_CID1,CHILD_CID2
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 get_child_prevention_policies.py -h
usage: get_child_prevention_policies.py [-h] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET [-c CHILDREN]

Retrieve child prevention policies.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |         FalconPy v1.2
`-------'                         `-------'

___  ____ ____ _  _ ____ _  _ ___ _ ____ _  _    ___  ____ _    _ ____ _ ____ ____
|__] |__/ |___ |  | |___ |\ |  |  | |  | |\ |    |__] |  | |    | |    | |___ [__
|    |  \ |___  \/  |___ | \|  |  | |__| | \|    |    |__| |___ | |___ | |___ ___]

Retrieve the prevention policies for all (or a subset of) child tenants within the parent.

Creation: 02.19.23 - jshcodes@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -c CHILDREN, --children CHILDREN
                        List of children to retrieve (comma-delimit)

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API client Secret
```

### Example source code
The source code for this example can be found [here](get_child_prevention_policies.py).

## Host Group Duplicator
Duplicates the specified host group within a parent to all child tenants.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Flight Control | __READ__ |
| Host Group | __READ__, __WRITE__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Duplicate the specified host group to all child tenants.

```shell
python3 host_group_duplicator.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f HOSTGROUP_FILTER
```

> GovCloud users can change their CrowdStrike region using the `-b` argument.

```shell
python3 host_group_duplicator.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -f HOSTGROUP_FILTER -b usgov1
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 host_group_duplicator.py -h
usage: host_group_duplicator.py [-h] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET [-r REGION] -f HOSTGROUP_FILTER

Duplicate host groups from a parent down to the children.

 _   _           _      ____                         ____              _ _           _
| | | | ___  ___| |_   / ___|_ __ ___  _   _ _ __   |  _ \ _   _ _ __ | (_) ___ __ _| |_ ___  _ __
| |_| |/ _ \/ __| __| | |  _| '__/ _ \| | | | '_ \  | | | | | | | '_ \| | |/ __/ _` | __/ _ \| '__|
|  _  | (_) \__ \ |_  | |_| | | | (_) | |_| | |_) | | |_| | |_| | |_) | | | (_| (_| | || (_) | |
|_| |_|\___/|___/\__|  \____|_|  \___/ \__,_| .__/  |____/ \__,_| .__/|_|_|\___\__,_|\__\___/|_|
                                            |_|                 |_|

optional arguments:
  -h, --help            show this help message and exit
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API Client secret
  -r REGION, --region REGION
                        CrowdStrike Region (us1, us2, eu1, usgov1). Required for usgov1.
  -f HOSTGROUP_FILTER, --hostgroup_filter HOSTGROUP_FILTER
                        String to use to search for host groups within the parent.
```

### Example source code
The source code for this example can be found [here](host_group_duplicator.py).


## Execute a command on hosts across multiple children
Execute a single RTR command across multiple hosts within multiple child tenants.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Flight Control | __READ__ |
| Hosts | __READ__ |
| Real Time Response | __READ__, __WRITE__ |
| Real Time Response Admin | __READ__, __WRITE__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Execute a Real Time Response command across hosts within all child tenants.

```shell
python3 multicid.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c ls
```

> GovCloud users can change their CrowdStrike region using the `-b` argument.

```shell
python3 multicid.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c ls -b usgov1
```

> Filter targeted hosts with a FQL filter.

```shell
python3 multicid.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c ls -f "hostname:'HOSTNAME'"
```

> Sort returned host results to alter the order of execution.

```shell
python3 multicid.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c ls -o "hostname.asc"
```

> Perform more complex commands leveraging raw format using the `-x` argument.

```shell
python3 multicid.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c "ls -al" -x
```

> Use multiple threads to perform processing.

```shell
python3 multicid.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c ls -m
```

> Thread count can be specified with the `-n` argument. (Ignored when not multithreaded.)

```shell
python3 multicid.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c ls -m -n 10
```

> Specify the output folder for execution results.

```shell
python3 multicid.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c ls -m -o OUTPUT_FOLDER
```

> Limit the number of hosts returned per child CID.

```shell
python3 multicid.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c ls -m -l 500
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 multicid.py -h
usage: multicid.py [-h] [-k FALCON_CLIENT_ID] [-s FALCON_CLIENT_SECRET] [-m] [-d OUTPUT_FOLDER] [-f FILTER] [-o SORT] [-l LIMIT] [-c COMMAND] [-t TIMEOUT] [-n NUMBER_OF_THREADS] [-x]

Execute a single RTR command across multiple hosts within multiple child tenants.

 _______ __            ______                         __ _______ __         __ __
|_     _|  |--.-----. |      |.----.-----.--.--.--.--|  |     __|  |_.----.|__|  |--.-----.
  |   | |     |  -__| |   ---||   _|  _  |  |  |  |  _  |__     |   _|   _||  |    <|  -__|
  |___| |__|__|_____| |______||__| |_____|________|_____|_______|____|__|  |__|__|__|_____|

     ___ ___       __ __   __  _______ ___ ______
    |   Y   .--.--|  |  |_|__||   _   |   |   _  \
    |.      |  |  |  |   _|  ||.  1___|.  |.  |   \
    |. \_/  |_____|__|____|__||.  |___|.  |.  |    \
    |:  |   |                 |:  1   |:  |:  1    /
    |::.|:. |                 |::.. . |::.|::.. . /
    `--- ---'                 `-------`---`------'

 ______  _______ _______ _______ _     _
 |_____] |_____|    |    |       |_____|
 |_____] |     |    |    |_____  |     |

            _______  _____  _______ _______ _______ __   _ ______
            |       |     | |  |  | |  |  | |_____| | \  | |     \
            |_____  |_____| |  |  | |  |  | |     | |  \_| |_____/

                        _______ _     _ _______ _______ _     _ _______  _____   ______
                        |______  \___/  |______ |       |     |    |    |     | |_____/
                        |______ _/   \_ |______ |_____  |_____|    |    |_____| |    \_

                                                                    FalconPy v1.1.5

optional arguments:
  -h, --help            show this help message and exit
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API Client Secret
  -m, --multithread     Leverage multiprocessing when executing the demonstration
  -d OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                        Folder to output saved results
  -f FILTER, --filter FILTER
                        FQL string to use to limit target hosts. (Defaults to all Windows hosts.)
  -o SORT, --sort SORT  FQL string to use to sort returned host results.
  -l LIMIT, --limit LIMIT
                        Number of hosts to return per CID. (Maximum: 5000)
  -c COMMAND, --command COMMAND
                        Command to execute across all targeted hosts. (Defaults to return environment details.)
  -t TIMEOUT, --timeout TIMEOUT
                        Batch execution timeout in seconds. (Defaults to 120.)
  -n NUMBER_OF_THREADS, --number_of_threads NUMBER_OF_THREADS
                        Number of threads to spawn, ignored when not multithreaded. Not required.
  -x, --script_execution
                        Executes the command in raw format using runscript.(Defaults to regular execution.)
```

### Example source code
The source code for this example can be found [here](multicid.py).
