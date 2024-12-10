![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Real Time Response - Dump memory for a running process
This sample leverages CrowdStrike's Hosts and Real Time Response APIs to dump the memory for a process running in memory.

> This example requires FalconPy v0.6.0+

## Procedure
1. The AID for the provided hostname is retrieved.
    - If not found, the routine will stop at this point.
2. A Real Time Response session is initialized between your host and the target host.
    - If a session cannot be instantiated, the routine will stop processing.
3. The requested command is analyzed:
    * Command of "ps"
        - The list of running processes is requested.
        - The resulting output is displayed to the screen.
        - Procedure terminates
    * Command of "dump"
        - Process ID is confirmed to be provided by the end user.
        - If process ID has not been provided, the routine terminates with an error.
4. The `dump-pid-memory.sh` utility script is uploaded to CrowdStrike cloud.

    **Script contents**
    ```
    #!/bin/bash

    grep rw-p /proc/$1/maps \
    | sed -n 's/^\([0-9a-f]*\)-\([0-9a-f]*\) .*$/\1 \2/p' \
    | while read start stop; do \
        gdb --batch --pid $1 -ex \
            "dump memory $1-$start-$stop.dump 0x$start 0x$stop"; \
    done
    ```
5. A _put_ command is issued, requesting the `dump-pid-memory.sh` utility be dropped on the target machine.
6. Two helper scripts are uploaded to CrowdStrike cloud.
    - `pid-memdump` - Installs __gdb__, calls the `memdump` utility to perform the memory dump of the specified PID and then zips up the generated dump files.
    - `pid-memdump-cleanup` - Removes the dump archive, dump files, and all remaining artifacts on the target machine.
7. The `dump-pid-memory.sh` utility script is executed on the target machine.
    - The routine waits for this execution to complete.
8. The archive containing the generated dump files is retrieved using a _get_ command. This file is uploaded to CrowdStrike cloud.
    - The routine waits for this upload to complete.
9. The routine then requests a list of all available files for the current RTR session. This will contain only the one file that was just requested with _get_.
10. The file is retrieved and downloaded to your local machine.
    - On download error, the routine will display the detail that it has and then stop processing.
11. The downloaded file is a 7-zip archive containing our regular archive of dump files. This archive is extracted into a temporary folder. Since this file was downloaded from the target system with _get_, we use the password of "_infected_" to open the archive.
12. The regular archive is then extracted to the current directory.
13. All temporary download files and folders are removed from your local system.
14. The `pip-memdump-cleanup` command is executed, removing all artifacts from the target system.
15. The helper scripts `pid-memdump` and `pid-memdump-cleanup` are removed from CrowdStrike cloud.
16. The `dump-pid-memory.sh` utility script is removed from CrowdStrike cloud.
17. The Real Time Response session is closed and deleted.
18. All remaining local temporary files are removed.


## Running the program
In order to run this demonstration, you will need a partial hostname for the target system and access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |
| Real Time Response | __READ__, __WRITE__ |
| Real Time Response Admin | __READ__, __WRITE__ |

### Execution syntax
The following command will request a process list for the target system.

```shell
python3 rtr_dump_memory.py -t HOSTNAME -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET -c ps
```

Once you have determined the Process ID you wish to dump, you can do so with the following command.

```shell
python3 rtr_dump_memory.py -t HOSTNAME -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET -c dump -p PROCESS_ID
```

Command-line help is available using the `-h` flag.

```shell
% python3 rtr_dump_memory.py -h
usage: rtr_dump_memory.py [-h] -t TARGET -c COMMAND [-p PID] -k KEY -s SECRET

FalconPy RTR demo

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Hostname of your target. Must be part of your CID.
  -c COMMAND, --command COMMAND
                        Command to perform against the host (ps or dump)
  -p PID, --pid PID     Process ID to dump
  -k KEY, --key KEY     Your CrowdStrike API key ID Required Scopes Hosts: READ RTR: WRITE RTR Admin: WRITE
  -s SECRET, --secret SECRET
                        Your CrowdStrike API key secret
```

## Example source code
The source code for this example is available [here](rtr_dump_memory.py)