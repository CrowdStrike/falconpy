![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)<br/>

# FalconPy<BR/>*The CrowdStrike Falcon SDK for Python 3*
![PyPI - Implementation](https://img.shields.io/pypi/implementation/crowdstrike-falconpy)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/crowdstrike-falconpy)
[![CodeQL](https://github.com/CrowdStrike/falconpy/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/codeql-analysis.yml)
![CI Test Coverage](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/tests/coverage.svg)
![Maintained](https://img.shields.io/maintenance/yes/2021)<br/>
The FalconPy SDK contains a collection of Python classes that abstract CrowdStrike Falcon OAuth2 API interaction, removing duplicative code and allowing developers to focus on just the logic of their solution requirements.

## Table of Contents
+ [Overview](#overview)
    - [Service classes](#service-classes)
    - [The Uber class](#the-uber-class)
+ [Installation & Removal](#installation--removal)
+ [Support & Community Forums](#support--community-forums)
+ [Documentation & Collateral](#documentation--collateral)

## Overview
This SDK provides two distinct methods for interacting with CrowdStrike's Falcon OAuth2 APIs, Service classes and the Uber class.
![Class Types](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/class_types.png)

### Service classes
Representing a single API service collection, each service class has a method defined for every operation available in that service collection.

| OAuth2-Based API<br>![#f03c15](https://via.placeholder.com/10/f03c15/000000?text=+)<small> *Documentation requires a CrowdStrike customer login*</small> | Code Location |
|:-|:-|
| CrowdStrike Device Control API | [device_control_policies.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/device_control_policies.py) |
| CrowdStrike Sensor Policy Management API | [sensor_update_policy.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/sensor_update_policy.py) |
| CrowdStrike Custom Indicators of Attack (IOAs) APIs | [custom_ioa.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/custom_ioa.py) <br/> [ioa_exclusions.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/ioa_exclusions.py)|
| [CrowdStrike Custom Indicators of Compromise (IOCs) API](https://falcon.crowdstrike.com/support/documentation/88/custom-ioc-apis) | [ioc.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/ioc.py) <BR/> [iocs.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/iocs.py) ![#f03c15](https://via.placeholder.com/10/f03c15/000000?text=+) <small>*Deprecated*</small> |
| [CrowdStrike Detections API](https://falcon.crowdstrike.com/support/documentation/85/detection-and-prevention-policies-apis) | [detects.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/detects.py) |
| [CrowdStrike Event Streams API](https://falcon.crowdstrike.com/support/documentation/89/event-streams-apis)| [event_streams.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/event_streams.py) |
| [CrowdStrike Falcon Horizon API](https://falcon.crowdstrike.com/support/documentation/137/falcon-horizon-apis) | [cspm_registration.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/cspm_registration.py) |
| [CrowdStrike Falcon X APIs](https://falcon.crowdstrike.com/support/documentation/92/falcon-x-apis) | [sample_uploads.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/sample_uploads.py) <br/> [falconx_sandbox.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/falconx_sandbox.py) <BR/> [quick_scan.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/quick_scan.py)|
| [CrowdStrike Firewall Management API](https://falcon.crowdstrike.com/support/documentation/107/falcon-firewall-management-apis) | [firewall_management.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/firewall_management.py) |
| [CrowdStrike Firewall Policy Management API](https://falcon.crowdstrike.com/support/documentation/107/falcon-firewall-management-apis) | [firewall_policies.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/firewall_policies.py) |
| CrowdStrike Falcon Complete Dashboard API | [falcon_complete_dashboard.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/falcon_complete_dashboard.py) |
| [CrowdStrike Falcon Flight Control API](https://falcon.crowdstrike.com/support/documentation/154/flight-control-apis) | [mssp.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/mssp.py) |
| [CrowdStrike Host Groups API](https://falcon.crowdstrike.com/support/documentation/84/host-and-host-group-management-apis) | [host_group.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/host_group.py) |
| [CrowdStrike Hosts API](https://falcon.crowdstrike.com/support/documentation/84/host-and-host-group-management-apis) | [hosts.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/hosts.py) |
| [CrowdStrike Incident and Detection Monitoring API](https://falcon.crowdstrike.com/support/documentation/86/detections-monitoring-apis) | [incidents.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/incidents.py) |
| [CrowdStrike Installation Tokens API](https://falcon.crowdstrike.com/support/documentation/120/Installation-token-APIs) | [installation_tokens.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/installation_tokens.py) | 
| [CrowdStrike Intel API](https://falcon.crowdstrike.com/support/documentation/72/intel-apis) | [intel.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/intel.py) | 
| CrowdStrike Kubernetes Protection API | [kubernetes_protection.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/kubernetes_protection.py) | 
| [CrowdStrike MalQuery API](https://falcon.crowdstrike.com/support/documentation/113/malquery-apis) | [malquery.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/malquery.py) |
| CrowdStrike ML Exclusions APIs | [ml_exclusions.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/ml_exclusions.py) |
| [CrowdStrike OAuth2 Auth Token API](https://falcon.crowdstrike.com/support/documentation/93/oauth2-auth-token-apis) | [oauth2.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/oauth2.py) |
| CrowdStrike Overwatch Dashboard API | [overwatch_dashboard.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/overwatch_dashboard.py) | 
| [CrowdStrike Prevention Policy API](https://falcon.crowdstrike.com/support/documentation/85/detection-and-prevention-policies-apis) | [prevention_policy.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/prevention_policy.py) |
| [CrowdStrike Real Time Response (RTR) API](https://falcon.crowdstrike.com/support/documentation/90/real-time-response-apis) | [real_time_response.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/real_time_response.py) |
| [CrowdStrike Realtime Response (RTR) Administration API](https://falcon.crowdstrike.com/support/documentation/90/real-time-response-apis) | [real_time_response_admin.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/real_time_response_admin.py) |
| CrowdStrike Realtime Response (RTR) Policies API | [response_policies.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/response_policies.py) |
| [CrowdStrike Sensor Download API](https://falcon.crowdstrike.com/support/documentation/109/sensor-download-apis) | [sensor_download.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/sensor_download.py) |
| CrowdStrike Sensor Visibility Exclusions API | [sensor_visibility_exclusions.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/sensor_visibility_exclusions.py) |
| [CrowdStrike Spotlight API](https://falcon.crowdstrike.com/support/documentation/98/spotlight-apis) | [spotlight_vulnerabilities.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/spotlight_vulnerabilities.py) |
| [CrowdStrike User and Roles API](https://falcon.crowdstrike.com/support/documentation/87/users-and-roles-apis) | [user_management.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/user_management.py) | 
| [Falcon Discover for Cloud and Containers - AWS Accounts API](https://falcon.crowdstrike.com/support/documentation/91/discover-for-aws-apis) | [cloud_connect_aws.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/cloud_connect_aws.py) |
| [Falcon Discover for Cloud and Containers - Azure Subscriptions API](https://falcon.crowdstrike.com/support/documentation/118/falcon-discover-for-cloud-and-containers-azure-subscription-apis) | [d4c_registration.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/d4c_registration.py) |
| [Falcon Discover for Cloud and Containers - GCP Projects API](https://falcon.crowdstrike.com/support/documentation/117/falcon-discover-for-cloud-and-containers-gcp-projects-apis) | [d4c_registration.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/d4c_registration.py) |
| [CrowdStrike Falcon Zero Trust Assessment API](https://falcon.crowdstrike.com/support/documentation/156/zero-trust-assessment-apis) | [zero_trust_assessment.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/zero_trust_assessment.py) |

### The Uber class
Provides a single harness for interacting with the entire API, covering every available operation within every API service collection.

[api_complete.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/api_complete.py) - The Uber class provides an interface to all CrowdStrike APIs with a single handler. 
This solution supports communicating with API endpoints that do not have an available Service Class or are recently released.

## Installation & Removal
![PyPI - Status](https://img.shields.io/pypi/status/crowdstrike-falconpy)
![PyPI](https://img.shields.io/pypi/v/crowdstrike-falconpy)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/crowdstrike-falconpy) 
![PyPI - Downloads](https://img.shields.io/pypi/dm/crowdstrike-falconpy)
![CI Tests](https://github.com/CrowdStrike/falconpy/workflows/Python%20package/badge.svg)
[![Pylint](https://github.com/CrowdStrike/falconpy/actions/workflows/pylint.yml/badge.svg)](https://github.com/CrowdStrike/falconpy/actions/workflows/pylint.yml)<br/>
Stable releases of FalconPy are available on the Python Package Index:
```shell
python3 -m pip install crowdstrike-falconpy
```

If you'd like to try the *absolute bleeding edge*, an automated GitHub action releases a test package with every merged pull request containing the string
`[DEPLOY]` in the head of the commit. 

To install this testing version of the package, use the command:
```shell
python3 -m pip install -i https://test.pypi.org/simple crowdstrike-falconpy
```

To uninstall and remove FalconPy:
```shell
python3 -m pip uninstall crowdstrike-falconpy
```

## Contributing
There are *many* ways you can contribute to the FalconPy project!
  * ***Providing feedback*** by opening a GitHub ticket. Even a fly-by "Hey, this worked!" is appreciated and helps validate approaches. Ideas on improving the project are most welcome.
  * ***Documenting, blogging, or creating videos***, of how you've used FalconPy! This type of content is *invaluable* and helps communities grow. Open a pull request for inclusion in the [Documentation and Collateral](https://github.com/CrowdStrike/falconpy#documentation-and-collateral) section.
  * ***Fix a bug or implement a new feature***. Check out our [open issues on GitHub](https://github.com/CrowdStrike/falconpy/issues) for inspiration.
  * ***Review pull requests*** by going through the queue of [open pull requests on GitHub](https://github.com/CrowdStrike/falconpy/pulls) and giving feedback to the authors

  > Review [CONTRIBUTING.md](https://github.com/CrowdStrike/falconpy/blob/main/CONTRIBUTING.md) for more details regarding contributing to the FalconPy project.

Open to do something else but not sure where to start? Try [opening an issue](https://github.com/CrowdStrike/falconpy/issues/new), or posting a topic in our [discussion board](https://github.com/CrowdStrike/falconpy/discussions), to introduce yourself and your interests. We look forward to chatting with you!

## Support & Community Forums
FalconPy is an open source project, not a formal CrowdStrike product, to assist developers implement CrowdStrike's APIs within their applications. As such it carries no formal support, express or implied. 

:fire: Is something going wrong? :fire:<br/>
GitHub Issues are used to report bugs. Submit a ticket here:<br/>
[https://github.com/CrowdStrike/falconpy/issues/new/choose](https://github.com/CrowdStrike/falconpy/issues/new/choose)

GitHub Discussions provide the community with means to communicate. There are four discussion categories:
  * :speech_balloon: [**General**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AGeneral) : Catch all for general discussions. 
  * :bulb: [**Ideas**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AIdeas): Have a suggestion for a feature request? Is there something the community or project could improve upon? Let us know here.
  * :pray: [**Q&A**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AQ%26A): Have a question about how to accomplish something? A usability question? Submit them here!
  * :raised_hands: [**Show and Tell**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3A%22Show+and+tell%22): Share with the community what you're up to! Perhaps this is letting everyone know about your upcoming conference talk, share a project that has embedded FalconPy, or your recent blog.


## Documentation & Collateral

### Official Project Documentation
See the wiki for extended documentation: [https://github.com/CrowdStrike/falconpy/wiki](https://github.com/CrowdStrike/falconpy/wiki).

### Videos (Tutorials, Trainings, Overviews)
*Coming soon*.

### Conference Presentations
[![API Office Hour 03.23.21](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/api_office_hour_preso_thumbnail.png)](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/falconpy-api-office-hour_customer_presentation.pdf?raw=true)

### Blogs/Articles/Prose
*Coming soon*.
