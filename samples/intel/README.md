![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)
![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)

# Intel examples
The examples within this folder focus on leveraging CrowdStrike Falcon Intel service collection.

- [Get MITRE ATT&CK reports](#get-mitre-attck-reports)

## Get MITRE ATT&CK Reports
Retrieves MITRE ATT&CK reports for specified adversaries.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| Intel | __READ__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Retrieve all available MITRE ATT&CK reports.

```shell
python3 get_mitre_reports.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Execute the routine for GovCloud customers.

```shell
python3 get_mitre_reports.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -g
```

> Only retrieve available kitten reports.

```shell
python3 get_mitre_reports.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i kitten
```

> Retrieve all available reports for bears, jackals, spiders and also grab Stardust Chollima.

```shell
python3 get_mitre_reports.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i bear,jackal,spider,stardust
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 get_mitre_reports.py -h
usage: get_mitre_reports.py [-h] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET [-g] [-f FORMAT] [-i ID_SEARCH]

Retrieve MITRE reports for adversaries.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |       FalconPy v1.2.10
`-------'                         `-------'

 _   _  _  ___  ___ ___      _  ___  ___ _    __  _  _
| \_/ || ||_ _|| o \ __|    / \|_ _||_ _(o)  / _|| |//
| \_/ || | | | |   / _|    | o || |  | |/oV7( (_ |  (
|_| |_||_| |_| |_|\\___|   |_n_||_|  |_|\_n\ \__||_|\\

____ ____ ___  ____ ____ ___   ___  ____ _ _ _ _  _ _    ____ ____ ___
|__/ |___ |__] |  | |__/  |    |  \ |  | | | | |\ | |    |  | |__| |  \
|  \ |___ |    |__| |  \  |    |__/ |__| |_|_| | \| |___ |__| |  | |__/

Download MITRE ATT&CK reports for specified (or all) adversaries.

This application requires:
    colorama
    crowdstrike-falconpy v1.2.10+

Created: 02.24.23 - jshcodes@CrowdStrike

optional arguments:
  -h, --help            show this help message and exit
  -g, --usgov           US GovCloud customers
  -f FORMAT, --format FORMAT
                        Report format (csv [default] or json)
  -i ID_SEARCH, --id_search ID_SEARCH
                        Filter by actor slug (stemmed search, comma delimit)

required arguments:
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        CrowdStrike Falcon API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        CrowdStrike Falcon API Client Secret
```

### Example source code
The source code for this example can be found [here](get_mitre_reports.py).
