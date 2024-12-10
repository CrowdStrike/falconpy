![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

# Falcon Quarantine samples
The examples within this folder focus on leveraging CrowdStrike's Falcon Quarantine API.

- [Get Quarantined Files](#get-quarantine-files)

## Get Quarantined Files
Retrieves all quarantined files within your environment and stores them to a subfolder.
Files can be downloaded raw, or archived with a password (`infected`).

### Dependencies
This solution supports debugging the quarantine file list responses from the API.
Developers may install the `click` library if they wish these debug displays to paginate.
This is not a required dependency.

#### Installing tabulate
Click can be installed using the Python Package Index:

```shell
python3 -m pip install click
```

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Quarantine | __READ__ |


### Execution syntax
This application leverages easy to use command line arguments for demonstrating functionality.
Arguments may be mixed as necessary.

#### Basic usage
Download all quarantined files within your environment.

```shell
python3 get_quarantined_files.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Download quarantined files individually archived with the password `infected`.

```shell
python3 get_quarantined_files.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -p
```

> Debug quarantine file responses from the API.

```shell
python3 get_quarantined_files.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d
```

> Leverage a proxy for API requests.

```shell
python3 get_quarantined_files.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -x "{'https': 'https://my.proxy.url:8888'}"
```

> Execute the sample within GovCloud.

```shell
python3 get_quarantined_files.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 get_quarantined_files.py -h
usage: get_quarantined_files.py [-h] -k KEY -s SECRET [-p] [-b BASE] [-x PROXY] [-d]

Pull samples from CrowdStrike Falcon Quarantine.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |         FalconPy v1.2
`-------'                         `-------'

____ _  _ ____ ____ ____ _  _ ___ _ _  _ ____ ___     ____ _ _    ____ ____
|  | |  | |__| |__/ |__| |\ |  |  | |\ | |___ |  \    |___ | |    |___ [__
|_\| |__| |  | |  \ |  | | \|  |  | | \| |___ |__/    |    | |___ |___ ___]

Leverages the FalconPy Uber Class to retrieves all quarantined files from
Falcon Quarantine and saves them to a subfolder within the current working
directory. Quarantined files can be downloaded as archives with a password
or as regular executables.

Requires: crowdstrike-falconpy
Optional: click

Created: 02.21.23 - tsullivan06@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -p, --protect         Password protect
  -b BASE, --base BASE  Falcon API base url
  -x PROXY, --proxy PROXY
                        Proxy for API requests
  -d, --debug           Display API response for quarantine file request

required arguments:
  -k KEY, --key KEY     Falcon Client API ID
  -s SECRET, --secret SECRET
                        Falcon Client API secret
```

### Example source code
The source code for this example can be found [here](get_quarantined_files.py).
