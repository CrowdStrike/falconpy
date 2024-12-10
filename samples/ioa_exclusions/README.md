![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# IOA Exclusions samples
The examples within this folder focus on leveraging CrowdStrike Falcon IOA Exclusions collection.

- [IOA Audit](#ioa-audit)

## IOA Audit
This program will output a list of IOA exclusions and their details for either the current CID or in each Child CID (Flight Control scenarios).
This can be used for regular audits of IOA exclusions across multiple CIDs.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| IOA Exclusions | __READ__ |
| Flight Control | __READ__ |
| Sensor Download | __READ__ |

> [!NOTE]
> This program can be executed using an API key that is not scoped for the Flight Control (MSSP) and Sensor Download service collections, but will be unable to lookup the current CID (Sensor Download) or access child CIDs (Flight Control).

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Execute the default example. This will output results to a CSV file named `ioa_exclusions.txt`.

```shell
python3 ioa_audit.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> This sample supports [Environment Authentication](https://falconpy.io/Usage/Authenticating-to-the-API.html#environment-authentication), meaning you can execute any of the command lines shown below without providing credentials if you have the values `FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET` defined in your environment.

```shell
python3 ioa_audit.py
```

Change the output destination with the `-o` argument.

```shell
python3 ioa_audit.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -o new_ioa_exclusions.txt
```

Enable MSSP mode and audit all Flight Control children with the `-m` argument.

```shell
python3 ioa_audit.py -k $FALCON_CLIENT_ID_PARENT -s $FALCON_CLIENT_SECRET_PARENT -m
```

Enable MSSP mode and audit a specific Flight Control child with the `-c` argument.

```shell
python3 ioa_audit.py -k $FALCON_CLIENT_ID_PARENT -s $FALCON_CLIENT_SECRET_PARENT -c CHILD_CID
```

> API debugging can be enabled using the `-d` argument.

```shell
python3 ioa_audit.py -d
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: ioa_audit.py [-h] [-d] [-m] [-c CHILD] [-o OUTPUT_FILE] [-k CLIENT_ID] [-s CLIENT_SECRET]

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

          _____                   _______                   _____
         /\    \                 /::\    \                 /\    \
        /::\    \               /::::\    \               /::\    \
        \:::\    \             /::::::\    \             /::::\    \
         \:::\    \           /::::::::\    \           /::::::\    \
          \:::\    \         /:::/~~\:::\    \         /:::/\:::\    \
           \:::\    \       /:::/    \:::\    \       /:::/__\:::\    \
           /::::\    \     /:::/    / \:::\    \     /::::\   \:::\    \
  ____    /::::::\    \   /:::/____/   \:::\____\   /::::::\   \:::\    \
 /\   \  /:::/\:::\    \ |:::|    |     |:::|    | /:::/\:::\   \:::\    \
/::\   \/:::/  \:::\____\|:::|____|     |:::|    |/:::/  \:::\   \:::\____\
\:::\  /:::/    \::/    / \:::\    \   /:::/    / \::/    \:::\  /:::/    /
 \:::\/:::/    / \/____/   \:::\    \ /:::/    /   \/____/ \:::\/:::/    /
  \::::::/    /             \:::\    /:::/    /             \::::::/    /
   \::::/____/               \:::\__/:::/    /               \::::/    /
    \:::\    \                \::::::::/    /                /:::/    /
     \:::\    \                \::::::/    /                /:::/    /
      \:::\    \                \::::/    /                /:::/    /
       \:::\____\                \::/____/                /:::/    /
        \::/    /                 ¯¯                      \::/    /
         \/____/  ▄▄▄          █           ▀               \/____/
                  █▄▄ ▀▄▀ █▀▀  █  █ █ █▀▀  █  █▀█ █▀█ █▀▀
                  █▄▄ ▄▀▄ █▄▄  █▄ █▄█ ▄▄█  █  █▄█ █ █ ▄▄█

This program will output a list of IOA exclusions and their details for
either the current CID or in each Child CID (Flight Control scenarios).
This can be used for regular audits of IOA exclusions across multiple CIDs.

Developed by @Don-Swanson-Adobe

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging
  -m, --mssp            List groups in all child CIDs (MSSP parents only)
  -c CHILD, --child CHILD
                        List groups in a specific child CID (MSSP parents only)
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        File to output results to

Required arguments:
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API secret
```

### Example source code
The source code for this example can be found [here](ioa_audit.py).