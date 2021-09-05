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
    - [Falcon X Sandbox](#falcon-x-sandbox)
    - [Hosts](#hosts)
    - [IOC](#ioc)
    - [MalQuery](#malquery)
    - [Quick Scan / Sample Uploads](#quick-scan--sample-uploads)
    - [Real Time Response](#real-time-response)
    - [Sample Uploads](#sample-uploads)
+ [Suggestions](#suggestions)

## Authentication for these Examples
In order to expedite sample delivery, we will be following a standard pattern for defining and providing credentials to the API. Credentials are either ingested
at runtime, or consumed via a standardized "credential" file named `config.json`. These are not the only methods for providing these values.  

> Please note: The file `config.json` is __not encrypted__ and may not be suitable for production deployments.

In order to test these samples locally in your development environment, rename the file `config_sample.json` to `config.json` and then
update this file to reflect your current development API credentials.

## Samples by API service collection
These samples are categorized by API service collection.

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

### Falcon X Sandbox
| Service Class | Uber Class |
| :--- | :--- |
| [Analyze a single file](falconx_sandbox/single_scan) | |

### Hosts
| Service Class | Uber Class |
| :--- | :--- |
| [List sensor versions by hostname](hosts#list-sensors-by-hostname) | |
| [List (and optionally remove) stale sensors](hosts#list-stale-sensors) | |


### IOC
| Service Class | Uber Class |
| :--- | :--- |
| [Create an IOC](ioc/create_ioc.py) | [Create an IOC](ioc/create_ioc.py) |

### MalQuery
| Service Class | Uber Class |
| :--- | :--- |
| | [Download MalQuery samples (MalQueryinator)](malquery/malqueryinator.py) |


### Quick Scan / Sample Uploads
| Service Class | Uber Class |
| :--- | :--- |
| [Scan a target folder or bucket](quick_scan/scan_target.py) | |


### Real Time Response
| Service Class | Uber Class |
| :--- | :--- |
| [Dump memory for a running process](rtr/pid-dump) | |
| [Quarantine a host](rtr/quarantine_hosts.py) | |
| [Retrieve basic system information](rtr/pony) | |

### Sample Uploads
| Service Class | Uber Class |
| :--- | :--- |
| [Upload, Retrieve and then Delete a file](sample_uploads/sample_uploads_service.py) | [Upload, Retrieve and then Delete a file](sample_uploads/sample_uploads_uber.py) |

## Suggestions
Got a suggestion for an example you'd like to see? One of the examples not working as expected? Let us know by posting a message to our [discussion board](https://github.com/CrowdStrike/falconpy/discussions).

Have an example you've developed yourself that you'd like to share?  **_Excellent!_** Please review our [contributing guidelines](/CONTRIBUTING.md) and then submit a pull request.
