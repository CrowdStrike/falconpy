![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) 

[![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

# FalconPy Sample Library

<!--![Adversary Bust Museum](../docs/asset/musee-des-origines.png)-->

These examples are provided as a quick start for your project.

+ [Authentication for Examples](#authentication-for-these-examples)
+ [Samples by API service collection](#samples-by-api-service-collection)
    - [Event Streams](#event-streams)
    - [Falcon Discover](#falcon-discover)
    - [Falcon Horizon](#falcon-horizon)
    - [Falcon Flight Control](#falcon-flight-control)
    - [Falcon X Sandbox](#falcon-x-sandbox)
    - [Hosts](#hosts)
    - [IOC](#ioc)
    - [MalQuery](#malquery)
    - [Quick Scan / Sample Uploads](#quick-scan--sample-uploads)
    - [Real Time Response](#real-time-response)
    - [Sample Uploads](#sample-uploads)
    - [Sensor Download](#sensor-download)
    - [Spotlight Vulnerabilities](#spotlight-vulnerabilities)
+ [Suggestions](#suggestions)

![Turbine Panda](../docs/asset/turbine-panda-fullcolor.png)

## Authentication for these Examples
In order to expedite sample delivery, examples will following one of three standard patterns for defining and providing credentials for API access. 

| Pattern | Usage detail |
| :--- | :--- |
| Environment variables | Credentials are retrieved from the local environment of the machine the example is executed on.<BR/><BR/>These values are named:<ul><li>`FALCON_CLIENT_ID`</li><li>`FALCON_CLIENT_SECRET`</li></ul> |
| Runtime (Command line arguments) | Credentials are consumed at runtime via command line parameters. Typically this handled via the [`argparse`](https://docs.python.org/3/library/argparse.html) module. |
| Standardized "credential" file | This file is named `config.json`, and is in JSON format. A sample of this file, [`config_sample.json`](config_sample.json) is provided within this folder. Rename this file to `config.json`, and then update it's contents to reflect your current development API credentials.  |

> Please note: These are not the only methods for providing these values. The file `config.json` is __not encrypted__ and may not be suitable for production deployments.

## Samples by API service collection
These samples are categorized by API service collection.

### Event Streams
| Service Class | Uber Class |
| :--- | :--- |
| | [Send Event Streams Detections to AWS Security Hub](https://github.com/CrowdStrike/Cloud-AWS/tree/main/Security-Hub) |

### Falcon Discover
| Service Class | Uber Class |
| :--- | :--- |
| [Register, delete, update and check accounts](discover_aws/manage_discover_accounts_service.py) | [Register, delete, update and check accounts](discover_aws/manage_discover_accounts_uber.py) |

### Falcon Horizon
| Service Class | Uber Class |
| :--- | :--- |
| [Report or export as CSV, all or selective CSP Falcon CSPM Policies](cspm_registration/get_cspm_policies.py) | |

### Falcon Flight Control
| Service Class | Uber Class |
| :--- | :--- |
| [Find child CID](flight_control/find_child_cid.py)

### Falcon X Sandbox
| Service Class | Uber Class |
| :--- | :--- |
| [Analyze a single file](falconx_sandbox/single_scan) | [Analyze a single file](falconx_sandbox/single_scan) |
| [Retrieve all artifacts for all reports](falconx_sandbox/get_all_artifacts.py) | |

### Hosts
| Service Class | Uber Class |
| :--- | :--- |
| [List sensor versions by hostname](hosts#list-sensors-by-hostname) | |
| [List (and optionally remove) stale sensors](hosts#list-stale-sensors) | |
| [Offset vs. Token](hosts#comparing-querydevicesbyfilter-and-querydevicesbyfilterscroll-offset-vs-token) | |


### IOC
| Service Class | Uber Class |
| :--- | :--- |
| [Create an IOC](ioc/create_ioc.py) | [Create an IOC](ioc/create_ioc.py) |

### MalQuery
| Service Class | Uber Class |
| :--- | :--- |
| | [Download MalQuery samples (MalQueryinator)](malquery#search-and-download-samples-from-malquery) |


### Quick Scan / Sample Uploads
| Service Class | Uber Class |
| :--- | :--- |
| [Scan a target folder or bucket](quick_scan/scan_target.py) | |
| [Scan files as they are uploaded to an AWS bucket](https://github.com/CrowdStrike/Cloud-AWS/tree/main/s3-bucket-protection) | |


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

### Sensor Download
| Service Class | Uber Class |
| :--- | :--- |
| | [List or download sensor by operating system and version](sensor_download/download_sensor.py) |

### Spotlight Vulnerabilities
| Service Class | Uber Class |
| :--- | :--- |
| [Identify hosts with vulnerabilities by CVE](spotlight#identify-hosts-with-vulnerabilities-by-cve) | |


## Suggestions
Got a suggestion for an example you'd like to see? One of the examples not working as expected? Let us know by posting a message to our [discussion board](https://github.com/CrowdStrike/falconpy/discussions).

Have an example you've developed yourself that you'd like to share?  **_Excellent!_** Please review our [contributing guidelines](/CONTRIBUTING.md) and then submit a pull request.



---

<p align="center"><img src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-footer.png"><BR/><img width="450px" src="../docs/asset/turbine-panda-lines.png"></P>
<h3><P align="center">WE STOP BREACHES</P></h3>