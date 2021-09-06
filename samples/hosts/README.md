![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)
![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)

# Hosts examples
The examples in this folder focus on leveraging CrowdStrike's Hosts API to perform administrative operations.
- [List sensor versions by Hostname](#list-sensors-by-hostname)
- [List (and optionally remove) stale sensors](#list-stale-sensors)
- [Offset vs. Offset Tokens](#comparing-querydevicesbyfilter-and-querydevicesbyfilterscroll-offset-vs-token)

## List sensors by hostname
Loops through all hosts and displays the hostname and sensor version.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |

### Execution syntax
This example requires no input parameters.

```shell
python3 sensor_versions_by_hostname.py
```

### Example source code
The source code for this example can be found [here](sensor_versions_by_hostname.py).

---

## List stale sensors
Retrieves a list of hosts that have not been seen since the number of days specified. Can optionally hide the hosts identified.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__, __WRITE__ |

### Execution syntax
The following command will retrieve a list of hosts that haven't checked in to CrowdStrike in 30 days or more.

```shell
python3 stale_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d 30
```

You can reverse the list sort with the `-r` or `--reverse` argument.

```shell
python3 stale_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d 30 --reverse
```

The following command will hide any hosts that haven't checked in to CrowdStrike in 30 days or more. You may also use `-x` to accomplish this.
```shell
python3 stale_sensors.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d 30 --remove
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
% python3 stale_sensors.py -h
usage: stale_sensors.py [-h] -k CLIENT_ID -s CLIENT_SECRET [-d DAYS] [-r] [-x]

         _______ ___ ___ _______ _______ _______ ______
        |   _   |   Y   |   _   |   _   |   _   |   _  \
        |.  1___|.  |   |   1___|   1___|.  1___|.  |   \
        |.  |___|.  |   |____   |____   |.  __)_|.  |    \
        |:  1   |:  1   |:  1   |:  1   |:  1   |:  1    /
        |::.. . |::.. . |::.. . |::.. . |::.. . |::.. . /
        `-------`-------`-------`-------`-------`------'

    CrowdStrike Unmonitored Stale Sensor Environment Detector


optional arguments:
  -h, --help            show this help message and exit
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike Falcon API key ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike Falcon API key secret
  -d DAYS, --days DAYS  Number of days since a host was seen before it is considered stale
  -r, --reverse         Reverse sort (defaults to ASC)
  -x, --remove          Remove hosts identified as stale
```

### Example source code
The source code for this example can be found [here](stale_sensors.py).

---

## Comparing QueryDevicesByFilter and QueryDevicesByFilterScroll (Offset vs. Token)
This routine queries all of the hosts in your environment using the QueryDevicesByFilter operation and the QueryDevicesByFilterScroll operation. The results of the two methods are then compared for equivalency. This sample demonstrates how to use both operations to paginate through large result sets, and discusses the inherent limitations of the QueryDevicesByFilter operation.

### Running the program.
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |

### Execution syntax
This example requires no input parameters.

```shell
python3 offset_vs_token.py
```

### Example source code
The source code for this example can be found [here](offset_vs_token.py)
