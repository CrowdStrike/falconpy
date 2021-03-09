![PyPI - Status](https://img.shields.io/pypi/status/crowdstrike-falconpy) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/crowdstrike-falconpy) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/crowdstrike-falconpy) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/crowdstrike-falconpy)<br/>
![PyPI](https://img.shields.io/pypi/v/crowdstrike-falconpy) ![PyPI - Downloads](https://img.shields.io/pypi/dm/crowdstrike-falconpy) ![CI Tests](https://github.com/CrowdStrike/falconpy/workflows/Python%20package/badge.svg) ![CI Test Coverage](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/tests/coverage.svg)<br/>
![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)<br/>

# FalconPy
The FalconPy SDK contains a collection of Python classes that abstract CrowdStrike Falcon OAuth2 API interaction, removing duplicative code and allowing developers to focus on just the logic of their solution requirements.

This SDK provides two distinct methods for interacting with CrowdStrike's Falcon OAuth2 APIs:
  * ***Service classes***, representing a single service collection, with methods defined for every available operation.
  * ***The Uber class***, which provides a single harness for interacting with the entire API, covering every available operation within every service collection.

## Quick Install / Uninstall
Stable releases of FalconPy are available on PyPI:
```shell
$ python3 -m pip install crowdstrike-falconpy
```

If you'd like to try the *absolute bleeding edge*, an automated GitHub action releases a test package with every merged pull request. To install the testing version:
```shell
$ python3 -m pip install -i https://test.pypi.org/simple crowdstrike-falconpy
```

To uninstall/remove FalconPy:
```shell
$ python3 -m pip uninstall crowdstrike-falconpy
```

# Service classes
| OAuth2-Based API<br>*(CrowdStrike documentation, requires CrowdStrike customer login)* | Code Location |
|:-|:-|
| CrowdStrike Device Control API | [./src/falconpy/device_control_policies.py](./src/falconpy/device_control_policies.py) |
| CrowdStrike Falcon Sandbox API | [./src/falconpy/falconx_sandbox.py](./src/falconpy/falconx_sandbox.py) |
| CrowdStrike Sensor Policy Management API | [./src/falconpy/sensor_update_policy.py](./src/falconpy/sensor_update_policy.py) |
| [CrowdStrike Custom Indicators of Compromose (IOCs) APIs](https://falcon.crowdstrike.com/support/documentation/88/custom-ioc-apis) | [./src/falconpy/iocs.py](./src/falconpy/iocs.py) |
| [CrowdStrike Detections APIs](https://falcon.crowdstrike.com/support/documentation/85/detection-and-prevention-policies-apis) | [./src/falconpy/detects.py](./src/falconpy/detects.py) |
| [CrowdStrike Event Streams API](https://falcon.crowdstrike.com/support/documentation/89/event-streams-apis)| [./src/falconpy/event_streams.py](./src/falconpy/event_streams.py) |
| [CrowdStrike Falcon Horizon APIs](https://falcon.crowdstrike.com/support/documentation/137/falcon-horizon-apis) | [./src/falconpy/cspm_registration.py](./src/falconpy/cspm_registration.py) |
| [CrowdStrike Falcon X APIs](https://falcon.crowdstrike.com/support/documentation/92/falcon-x-apis) | *Coming Soon* |
| [CrowdStrike Firewall Management API](https://falcon.crowdstrike.com/support/documentation/107/falcon-firewall-management-apis) | [./src/falconpy/firewall_management.py](./src/falconpy/firewall_management.py) |
| [CrowdStrike Firewall Policy Management](https://falcon.crowdstrike.com/support/documentation/107/falcon-firewall-management-apis) | [./src/falconpy/firewall_policies.py](./src/falconpy/firewall_policies.py) |
| [CrowdStrike Host Groups API](https://falcon.crowdstrike.com/support/documentation/84/host-and-host-group-management-apis) | [./src/falconpy/host_group.py](./src/falconpy/host_group.py) |
| [CrowdStrike Hosts API](https://falcon.crowdstrike.com/support/documentation/84/host-and-host-group-management-apis) | [./src/falconpy/hosts.py](./src/falconpy/hosts.py) |
| [CrowdStrike Incident and Detection Monitoring APIs](https://falcon.crowdstrike.com/support/documentation/86/detections-monitoring-apis) | [./src/falconpy/incidents.py](./src/falconpy/incidents.py) |
| [CrowdStrike Installation Token APIs](https://falcon.crowdstrike.com/support/documentation/120/Installation-token-APIs) | *Coming Soon* | 
| [CrowdStrike Intel API](https://falcon.crowdstrike.com/support/documentation/72/intel-apis) | [./src/falconpy/intel.py](./src/falconpy/intel.py) | 
| [CrowdStrike MalQuery API](https://falcon.crowdstrike.com/support/documentation/113/malquery-apis) | *Coming Soon* |
| [CrowdStrike OAuth2 Auth Token APIs](https://falcon.crowdstrike.com/support/documentation/93/oauth2-auth-token-apis) | [./src/falconpy/oauth2.py](./src/falconpy/oauth2.py) |
| [CrowdStrike Prevention Policy APIs](https://falcon.crowdstrike.com/support/documentation/85/detection-and-prevention-policies-apis) | [./src/falconpy/prevention_policy.py](./src/falconpy/prevention_policy.py) |
| [CrowdStrike Real Time Response (RTR) APIs](https://falcon.crowdstrike.com/support/documentation/90/real-time-response-apis) | [./src/falconpy/real_time_response.py](./src/falconpy/real_time_response.py) |
| [CrowdStrike Realtime Response (RTR) Administration API](https://falcon.crowdstrike.com/support/documentation/90/real-time-response-apis) | [./src/falconpy/real_time_response_admin.py](./src/falconpy/real_time_response_admin.py) |
| [CrowdStrike Sensor Download APIs](https://falcon.crowdstrike.com/support/documentation/109/sensor-download-apis) | *Coming Soon* |
| [CrowdStrike Spotlight APIs](https://falcon.crowdstrike.com/support/documentation/98/spotlight-apis) | [./src/falconpy/spotlight_vulnerabilities.py](./src/falconpy/spotlight_vulnerabilities.py) |
| [CrowdStrike User and Roles API](https://falcon.crowdstrike.com/support/documentation/87/users-and-roles-apis) | [./src/falconpy/user_management.py](./src/falconpy/user_management.py) | 
| [Falcon Discover for Cloud and Containers - AWS Accounts APIs](https://falcon.crowdstrike.com/support/documentation/91/discover-for-aws-apis) | [./src/falconpy/cloud_connect_aws.py](./src/falconpy/cloud_connect_aws.py) |
| [Falcon Discover for Cloud and Containers - Azure Subscriptions APIs](https://falcon.crowdstrike.com/support/documentation/118/falcon-discover-for-cloud-and-containers-azure-subscription-apis) | *Coming Soon* |
| [Falcon Discover for Cloud and Containers - GCP Projects APIs](https://falcon.crowdstrike.com/support/documentation/117/falcon-discover-for-cloud-and-containers-gcp-projects-apis) | *Coming Soon* |

## Uber class
+ [./src/falconpy/api_complete.py](./src/falconpy/api_complete.py) - Provides an interface to all CrowdStrike APIs with a single handler.

# Contributing
There are *many* ways you can contribute to the FalconPy project!
  * ***Providing feedback*** by opening a GitHub ticket. Even a fly-by "Hey, this worked!" is appreciated and helps validate approaches. Ideas on improving the project are most welcome.
  * ***Documenting, blogging, or creating videos***, of how you've used FalconPy! This type of content is *invaluable* and helps communities grow. Open a pull request for inclusion in the [Documentation and Collateral](#documentation-and-collateral) section.
  * ***Fix a bug or implement a new feature***. Check out our [open issues on GitHub](https://github.com/CrowdStrike/falconpy/issues) for inspiration.
  * ***Review pull requests*** by going through the queue of [open pull requests on GitHub](https://github.com/CrowdStrike/falconpy/pulls) and giving feedback to the authors

Open to do something else but not sure where to start? Try [opening an issue](https://github.com/CrowdStrike/falconpy/issues/new) and introducing yourself and your interests. We look forward to chatting with you!

# Support & Community Forums
FalconPy is an open source project, not a formal CrowdStrike product, to assist developers implement CrowdStrike's APIs within their applications. As such it carries no formal support, express or implied. 

:fire: Is something going wrong? :fire:<br/>
GitHub Issues are used to report bugs. Submit a ticket here:<br/>
[https://github.com/CrowdStrike/falconpy/issues/new/choose](https://github.com/CrowdStrike/falconpy/issues/new/choose)

GitHub Discussions provide the community with means to communicate. There are four discussion categories:
  * :speech_balloon: [**General**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AGeneral) : Catch all for general discussions. 
  * :bulb: [**Ideas**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AIdeas): Have a suggestion for a feature request? Is there something the community or project could improve upon? Let us know here.
  * :pray: [**Q&A**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AQ%26A): Have a question about how to accomplish something? A usability question? Submit them here!
  * :raised_hands: [**Show and Tell**](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3A%22Show+and+tell%22): Share with the community what you're up to! Perhaps this is letting everyone know about your upcoming conference talk, share a project that has embedded FalconPy, or your recent blog.


# Documentation & Collateral

## Official Project Documentation
See the wiki for extended documentation: [https://github.com/CrowdStrike/falconpy/wiki](https://github.com/CrowdStrike/falconpy/wiki).

## Videos (Tutorials, Trainings, Overviews)
*Coming soon*.

## Conference Presentations
*Coming soon*.

## Blogs/Articles/Prose
*Coming soon*.
