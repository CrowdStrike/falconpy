![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Falcon Sample Uploads samples
The examples within this folder focus on leveraging CrowdStrike's Falcon Sample Uploads API.

- [Sample Uploads demonstration](#sample-uploads-demonstration)

## Sample Uploads demonstration
This sample demonstrates interactions with the Falcon Intelligence Sandbox by uploading a file,
downloading the file, then removing the file from the sandbox.

There are two samples provided, one demonstrating Service Class usage and one demonstrating Uber Class usage.

Both samples implement equivalent functionality.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Sample Uploads | __READ__, __WRITE__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Execute the demonstration.

> Using the default credentials file (`../config.json`)

```shell
python3 sample_uploads_service.py
```

> Using a custom credentials file.

```shell
python3 sample_uploads_service.py -c custom_creds.json
```

> Passing credentials on the command line.

```shell
python3 sample_uploads_service.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Change your CrowdStrike region using the `-b` argument. (Only required for GovCloud users.)

```shell
python3 sample_uploads_service.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -b usgov1
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 sample_uploads_service.py -h
usage: sample_uploads_service.py [-h] [-k FALCON_CLIENT_ID] [-s FALCON_CLIENT_SECRET] [-c CONFIG_FILE] [-b BASE_URL]

Sample Uploads Service Collection example, Service Class version.

 ____                        _        _   _       _                 _
/ ___|  __ _ _ __ ___  _ __ | | ___  | | | |_ __ | | ___   __ _  __| |___
\___ \ / _` | '_ ` _ \| '_ \| |/ _ \ | | | | '_ \| |/ _ \ / _` |/ _` / __|
 ___) | (_| | | | | | | |_) | |  __/ | |_| | |_) | | (_) | (_| | (_| \__ \
|____/ \__,_|_| |_| |_| .__/|_|\___|  \___/| .__/|_|\___/ \__,_|\__,_|___/
                      |_|                  |_|
 ____                  _             ____ _
/ ___|  ___ _ ____   _(_) ___ ___   / ___| | __ _ ___ ___
\___ \ / _ \ '__\ \ / / |/ __/ _ \ | |   | |/ _` / __/ __|
 ___) |  __/ |   \ V /| | (_|  __/ | |___| | (_| \__ \__ \
|____/ \___|_|    \_/ |_|\___\___|  \____|_|\__,_|___/___/

The following demonstrates how to interact with the Sample Uploads API using the Service Class.
This example uses Direct Authentication and supports token refresh / authentication free usage.

This sample requires FalconPy v0.8.6+

optional arguments:
  -h, --help            show this help message and exit
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        API Client ID (required if not using a configuration file).
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        API Client Secret (required if not using a configuration file).
  -c CONFIG_FILE, --config_file CONFIG_FILE
                        Credential configuration file (required if not using command line arguments).
  -b BASE_URL, --base_url BASE_URL
                        CrowdStrike Region (only required for GovCloud users).
```

### Example source code
The source code for these examples can be found here:

- [Service Class Example](sample_uploads_service.py)
- [Uber Class Example](sample_uploads_uber.py)
