![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)
![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)

# ProxyTool v3
This example focuses on leveraging CrowdStrike's Hosts, Host Groups, and Real-Time Response API.

It is a script that fetches CID or Host Group hosts, and uses the batch command and offline queuing of Real-Tike Response API to centrally 
and conveniently issue Falcon sensor proxy configuration changes.

- It uses native RTR commands, which will not trigger a detection/prevention in relation to sensor anti-tampering. 
- Because it uses the RTR API it is run centrally through our cloud, it does NOT need to be distributed to each targeted host. 
- The script uses the queuing feature of RTR, so hosts don't need to be online at the time the script is executed, they will receive the commands if they connect to our cloud within the next 7 days. 


> __WARNING: This script has the potential to disrupt the communications between the Falcon sensor and the cloud. It is suggested to test with a limited Host Group first to troubleshoot any issues.__

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |
| Host Group | __READ__ |
| Real-Time Response | __WRITE, READ__ |

### Execution syntax
This example accepts the following input parameters.
| Parameter | Purpose | Category |
| :--- | :--- | :--- |
| `--falcon_client_id` | Falcon API client ID | required |
| `--falcon_client_secret` | Falcon API client secret | required |
| `--proxy_hostname` | Falcon sensor proxy hostname or FQDN | required |
| `--proxy_port` | Falcon sensor proxy port | required |
| `--scope` | `cid` or `hostgroup` | required |
| `--scope_id` | Either the CID or the Host Group ID | required |
| `--base_url` | CrowdStrike base URL (only required for GovCloud, pass usgov1) | optional |


##### Show command line help.
```shell
python3 proxytool_3.3.py --falcon_client_id FALCON_CLIENT_ID --falcon_client_secret FALCON_CLIENT_SECRET 
                        --proxy_hostname PROXY_HOST --proxy_port PROXY_PORT --scope hostgroup --scope_id HOST_GROUP_ID
```
