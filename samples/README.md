![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) 

[![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

# FalconPy usage examples
These examples are provided as a quick start for your project.

+ [Authentication for Examples](#authentication-for-these-examples)
+ [Samples by API service collection](#samples-by-api-service-collection)
    - [Detections](#detections)
    - [Event Streams](#event-streams)
    - [Falcon Discover](#falcon-discover)
    - [Falcon Horizon](#falcon-horizon)
    - [Hosts](#hosts)
    - [Quick Scan / Sample Uploads](#quick-scan)
    - [Real Time Response](#real-time-response)
    - [Sample Uploads](#sample-uploads)
+ [Suggestions](#suggestions)

## Authentication for these Examples
In order to expedite sample delivery, we will be following a standard pattern for defining and providing credentials to the API.
This is not the only method of providing these values, and not recommended for production deployments as the config.json file is
**not encrypted**.

In order to test these samples locally in your development environment, rename the file `config_sample.json` to `config.json` and then
update this file to reflect your current development API credentials.

## Samples by API service collection
These samples are categorized by API service collection. The list below will grow as more samples are planned.

### Detections
_Coming Soon_

### Event Streams
_Coming Soon_

### Falcon Discover
| Service Class | Uber Class |
| :--- | :--- |
| [Register, delete, update and check accounts](discover_aws/manage_discover_accounts_service.py) | [Register, delete, update and check accounts](discover_aws/manage_discover_accounts_uber.py) |

### Falcon Horizon
| Service Class | Uber Class |
| :--- | :--- |
| [Report or export as CSV, all or selective CSP Falcon CSPM Policies](cspm_registration/get_cspm_policies.py) | |


### Hosts
| Service Class | Uber Class |
| :--- | :--- |
| [List sensor versions by hostname](hosts/sensor_versions_by_hostname.py)


### Quick Scan / Sample Uploads
| Service Class | Uber Class |
| :--- | :--- |
| [Scan a target folder or bucket](quick_scan/scan_target.py) | |


### Real Time Response
| Service Class | Uber Class |
| :--- | :--- |
| [Quarantine a host](real_time_response/quarantine_hosts.py) | |

### Sample Uploads
| Service Class | Uber Class |
| :--- | :--- |
| [Upload, Retrieve and then Delete a file](sample_uploads/sample_uploads_service.py) | [Upload, Retrieve and then Delete a file](sample_uploads/sample_uploads_uber.py) |

## Suggestions
Got a suggestion for an example you'd like to see? Let us know by posting a message to our [discussion board](https://github.com/CrowdStrike/falconpy/discussions).

Have an example you've developed yourself that you'd like to share?  **_Excellent!_** Please review our [contributing guidelines](/CONTRIBUTING.md) and then submit a pull request.
