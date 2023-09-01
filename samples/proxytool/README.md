![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)
[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# ProxyTool v3.5
This example focuses on leveraging CrowdStrike's Hosts, Host Groups, Sensor Download, and Real-Time Response API.

It is a script that fetches CID or Host Group hosts, and uses the batch command and offline queuing of Real-Time Response API to centrally 
and conveniently issue Falcon sensor proxy configuration changes.

- It uses native RTR commands, which will not trigger a detection/prevention in relation to sensor anti-tampering. 
- Because it uses the RTR API it is run centrally through our cloud, it does NOT need to be distributed to each targeted host. 
- The script uses the queuing feature of RTR, so hosts don't need to be online at the time the script is executed, they will receive the commands if they connect to our cloud within the next 7 days.
- The script checks that the CID provided as a scope_id argument is the same the API client is working with.

‼️WARNING‼️
This script has the potential to disrupt communications between the Falcon sensor and the cloud. It is recommended users test with a limited Host Group first to troubleshoot any issues.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |
| Host Group | __READ__ |
| Real-Time Response | __WRITE, READ__ |
| Sensor Download | __READ__ |

### Execution syntax
This example accepts the following input parameters.
| Parameter | Purpose | Category |
| :--- | :--- | :--- |
| `--falcon_client_id` | Falcon API client ID | required |
| `--falcon_client_secret` | Falcon API client secret | required |
| `--proxy_hostname` | Falcon sensor proxy hostname or FQDN | optional |
| `--proxy_port` | Falcon sensor proxy port | optional |
| `--proxy_disable` | Delete/disable sensor proxy configuration | optional |
| `--scope` | `cid` or `hostgroup` | required |
| `--scope_id` | Either the CID or the Host Group ID | required |
| `--base_url` | CrowdStrike base URL (only required for GovCloud, pass usgov1) | optional |


‼️WARNING‼️
This script can target either a HOST GROUP (passing ´hostgroup´ as scope, and the group ID as scope_id) or the complete CID (passing ´cid´ as scope, and the CID as scope_id).
This script CANNOT target a single HOST. To target a single host, please create a static group with the target host.



If you want to set or change proxy configuration:

```shell
python3 proxytool.py --falcon_client_id FALCON_CLIENT_ID --falcon_client_secret FALCON_CLIENT_SECRET 
                        --proxy_hostname PROXY_HOST --proxy_port PROXY_PORT --scope hostgroup --scope_id HOST_GROUP_ID
```

If you want to disable proxy configuration:

```shell
python3 proxytool.py --falcon_client_id FALCON_CLIENT_ID --falcon_client_secret FALCON_CLIENT_SECRET 
                        --proxy_disable --scope hostgroup --scope_id HOST_GROUP_ID
```

