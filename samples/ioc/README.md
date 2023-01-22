![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)

# Falcon IOC samples
The examples within this folder focus on leveraging CrowdStrike's Falcon IOC API.

- [Create Indicator of Compromise](#create-indicator-of-compromise)

## Create Indicator of Compromise
Demonstrates the creation of a single IOC using either the Service or Uber Class. 
Indicator detail is loaded from an external file that can be specified via the command line.

### Running the program
In order to run this demonstration, you you will need access to CrowdStrike API keys with the following scopes:

| Service Collection | Scope |
| :---- | :---- |
| IOC | __WRITE__ |

### Execution syntax
This sample leverages simple command-line arguments to implement functionality.

#### Basic usage
Create an indicator using sample indicator file `example_indicator.json`. The default method uses the Service Class to interact with the CrowdStrike API.

```shell
python3 create_ioc.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

> Perform the operation using the Uber class instead with the `-m` argument.

```shell
python3 create_ioc.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -m uber
```

> Load a custom indicator file with the `-i` argument. (Indicator should be in JSON format.)

```shell
python3 create_ioc.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -i custom_indicator.json
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
python3 create_ioc.py -h
usage: create_ioc.py [-h] -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET [-m METHOD] [-i INDICATOR]

 ___  _______  _______
|   ||   _   ||   _   |
|.  ||.  |   ||.  1___|
|.  ||.  |   ||.  |___
|:  ||:  1   ||:  1   |
|::.||::.. . ||::.. . |
`---'`-------'`-------'

Create IOC Example - @jshcodes 06.23.21

FalconPy v.0.8.6+

INDICATOR FILE FORMAT EXAMPLE (JSON)
{
    "source": "Test",
    "action": "detect",
    "expiration": "2023-01-22T15:00:00.000Z",
    "description": "Testing",
    "type": "ipv4",
    "value": "4.1.42.34",
    "platforms": ["linux"],
    "severity": "LOW",
    "applied_globally": true
}

optional arguments:
  -h, --help            show this help message and exit
  -k FALCON_CLIENT_ID, --falcon_client_id FALCON_CLIENT_ID
                        Falcon API Client ID
  -s FALCON_CLIENT_SECRET, --falcon_client_secret FALCON_CLIENT_SECRET
                        Falcon API Client Secret
  -m METHOD, --method METHOD
                        SDK method to use ('service' or 'uber').
  -i INDICATOR, --indicator INDICATOR
                        Path to the file representing the indicator (JSON format).
```

### Example source code
The source code for this example can be found [here](create_ioc.py).
