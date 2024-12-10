![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Container examples
The examples in this folder focus on leveraging CrowdStrike's Container APIs to discover and manage your container assets.
- [kube_map - Discover your Kubernetes Attack Surface](#Discover-your-Kubernetes-Attack-Surface)

## Discover your Kubernetes Attack Surface
Discovers Kubernetes assets that are monitored by the Falcon Sensor (clusters, nodes, pods, and containers).

> [!IMPORTANT]
> Installing the __Kubernetes Protection Agent (KPA)__ on your clusters will result in the most accurate information. 


### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Kubernetes Protection | __READ__|

### Execution syntax
This example accepts the following input parameters.
| Parameter | Purpose |
| :--- | :--- |
| `-d`, `--debug` | Enable API debugging. |
| `-c`, `--cluster` | Display all clusters and the number of attached nodes. |
| `-n`, `--node` | Display all nodes including the number of attached, active pods. |
| `-nn`, `--node_name` | Displays pods connected to a specific node. |
| `-t`, `--thread` | Enables asynchronous API calls for faster returns. |
| `-k`, `--key` | Your CrowdStrike Falcon API Client ID |
| `-s`, `--secret` | Your CrowdStrike Falcon API Client Secret |

Displays the number of clusters, nodes, pods, and containers detected by the Falcon Sensor.
```shell
python3 kube_map.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET
```

Displays a table of cluster information.
```shell
python3 kube_map.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -c
```

Displays a table of node information.
```shell
python3 kube_map.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -n
```

Displays a table of pods based on it's parent node name using the optional threading feature.
```shell
python3 kube_map.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -nn "node_name" -t
```

Displays API debug logging.
```shell
python3 kube_map.py -k $FALCON_CLIENT_ID -s $FALCON_CLIENT_SECRET -d
```

#### Command-line help
Command-line help is available using the `-h` or `--help` parameters.

```shell
% python3 kube_map.py -h
usage: kube_map.py [-h] -k CLIENT_ID -s CLIENT_SECRET [-d] [-c] [-n] [-nn NODE_NAME] [-t]

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

         _  ___   _ ____  _____
        | |/ / | | | __ )| ____|
        | ' /| | | |  _ \|  _|
        | . \| |_| | |_) | |___
  __  __|_|\_\\___/|____/|_____|__ ____
 |  \/  |  / \  |  _ \|  _ \| ____|  _ \
 | |\/| | / _ \ | |_) | |_) |  _| | |_) |
 | |  | |/ ___ \|  __/|  __/| |___|  _ <
 |_|  |_/_/   \_\_|   |_|   |_____|_| \_\

This sample utilizes the Kubernetes Protection service collection to map out
your kubernetes assets. Kubernetes assets are found via the Falcon Sensor.

Creation date: 06.26.23 - alhumaw

options:
  -h, --help            show this help message and exit
  -d, --debug           Enable API debugging
  -c, --cluster         Display clusters and it's nodes
  -n, --node            Display nodes and it's pods
  -nn NODE_NAME, --node_name NODE_NAME
                        Display pods connected to a specific node
  -t, --thread          Enables asynchronous API calls for faster returns

required arguments:
  -k CLIENT_ID, --client_id CLIENT_ID
                        CrowdStrike API client ID
  -s CLIENT_SECRET, --client_secret CLIENT_SECRET
                        CrowdStrike API client secret
```

### Example source code
The source code for this example can be found [here](kube_map.py).
