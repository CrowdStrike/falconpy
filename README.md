![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)

[![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)<br/>

# The CrowdStrike Falcon SDK for Python (FalconPy)

![Repo status](https://img.shields.io/osslifecycle/crowdstrike/falconpy?label=repo%20status)
![Package Status](https://img.shields.io/pypi/status/crowdstrike-falconpy?label=package%20status)
![PyPI](https://img.shields.io/pypi/v/crowdstrike-falconpy?label=current%20version)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/crowdstrike-falconpy)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/crowdstrike-falconpy)
![PyPI - Downloads](https://img.shields.io/pypi/dm/crowdstrike-falconpy)

The FalconPy SDK contains a collection of Python classes that abstract CrowdStrike Falcon OAuth2 API interaction, removing duplicative code and allowing developers to focus on just the logic of their solution requirements.

+ [Overview](#overview)
    - [Service Classes](#service-classes)
    - [The Uber Class](#the-uber-class)
+ [Quick Start](#quick-start)
+ [Documentation and Support](#documentation-and-support)
+ [Contribute to FalconPy](#contribute-to-falconpy)

## Overview :mag_right:
There are currently 45 CrowdStrike Falcon API service collections containing 397 individual operations, all of which are accessible via FalconPy.

FalconPy also supports interaction with all CrowdStrike regions (`US-1`, `US-2`, `EU-1` and `US-GOV-1`), custom connection and response timeouts, routing requests thru a list of proxies, and disabling SSL verification when required.

#### Supported versions of Python
FalconPy has been tested for functionality using the following versions of Python.

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/crowdstrike-falconpy?logo=python&label=Supported%20versions&logoColor=white)

#### Supported Operating Systems
FalconPy has been tested on the following operating systems.

![Amazon Linux](https://img.shields.io/badge/-Amazon-darkgreen?logo=amazon)
![Arch Linux](https://img.shields.io/badge/-Arch-tan?logo=archlinux)
![CentOS](https://img.shields.io/badge/-CentOS-purple?logo=centos)
![Debian](https://img.shields.io/badge/-Debian-darkred?logo=debian)
![Fedora](https://img.shields.io/badge/-Fedora-darkblue?logo=fedora)
![Kali](https://img.shields.io/badge/-Kali-black?logo=kalilinux&logoColor=white)
![macOS](https://img.shields.io/badge/-macOS-silver?logo=apple)
![Pop! OS](https://img.shields.io/badge/-Pop!%20OS-orange?logo=popos&logoColor=black)
![RedHat](https://img.shields.io/badge/-RedHat-maroon?logo=redhat)
![Ubuntu](https://img.shields.io/badge/-Ubuntu-964?logo=ubuntu)
![Windows](https://img.shields.io/badge/-Windows-blue?logo=windows)

Details regarding supported operating systems and Python versions, and project security and testing procedures can be found [here](https://github.com/CrowdStrike/falconpy/blob/main/SECURITY.md).

### Components
The CrowdStrike Falcon SDK for Python provides two distinct methods for interacting with CrowdStrike's Falcon APIs: 

- [Service Classes](#service-classes) - each Service Class represents a single CrowdStrike API service collection providing an interface to the operations available within that service collection.
- [The Uber Class](#the-uber-class) - an all-in-one class that provides a singular interface for all operations in every CrowdStrike API service collection.

![Class Types](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/class_types.png)

### Service Classes
Representing a single API service collection, each service class has a method defined for every operation available within that service collection.

#### Available Service Classes
For each CrowdStrike API service collection, a matching Service Class is available in the FalconPy library.

| Service Collection | Code Location | Class Name |
|:-| :-| :-|
| [CrowdStrike Device Control](https://falcon.crowdstrike.com/documentation/167/usb-device-control-policy-apis) | [device_control_policies.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/device_control_policies.py) | DeviceControlPolicies |
| CrowdStrike Custom Indicators of Attack (IOAs) | [custom_ioa.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/custom_ioa.py) <br/> [ioa_exclusions.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/ioa_exclusions.py)| CustomIOA<BR/>IOAExclusions |
| [CrowdStrike Custom Indicators of Compromise (IOCs)](https://falcon.crowdstrike.com/support/documentation/88/custom-ioc-apis) | [ioc.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/ioc.py) <BR/> [iocs.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/iocs.py) ![#f03c15](https://via.placeholder.com/10/f03c15/000000?text=+) <small>*Deprecated*</small> | IOC<BR/>Iocs |
| [CrowdStrike Detections](https://falcon.crowdstrike.com/support/documentation/85/detection-and-prevention-policies-apis) | [detects.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/detects.py) | Detects |
| [CrowdStrike Falcon Discover](https://falcon.crowdstrike.com/documentation/197/falcon-discover-apis) | [discover.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/discover.py) | Discover |
| [CrowdStrike Event Streams](https://falcon.crowdstrike.com/support/documentation/89/event-streams-apis)| [event_streams.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/event_streams.py) | EventStreams |
| [CrowdStrike Falcon Container](https://falcon.crowdstrike.com/documentation/146/falcon-container-sensor-for-linux) | [falcon_container.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/falcon_container.py) | FalconContainer |
| [CrowdStrike Falcon Horizon](https://falcon.crowdstrike.com/support/documentation/137/falcon-horizon-apis) | [cspm_registration.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/cspm_registration.py) | CSPMRegistration |
| [CrowdStrike Falcon X](https://falcon.crowdstrike.com/support/documentation/92/falcon-x-apis) | [sample_uploads.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/sample_uploads.py) <br/> [falconx_sandbox.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/falconx_sandbox.py) <BR/> [quick_scan.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/quick_scan.py)| SampleUploads<BR/>FalconXSandbox<BR/>QuickScan |
| CrowdStrike FileVantage | [filevantage.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/filevantage.py) | FileVantage |
| [CrowdStrike Firewall Management](https://falcon.crowdstrike.com/support/documentation/107/falcon-firewall-management-apis) | [firewall_management.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/firewall_management.py) | FirewallManagement |
| [CrowdStrike Firewall Policy Management](https://falcon.crowdstrike.com/support/documentation/107/falcon-firewall-management-apis) | [firewall_policies.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/firewall_policies.py) | FirewallPolicies |
| [CrowdStrike Falcon Complete Dashboard](https://falcon.crowdstrike.com/documentation/151/falcon-complete-dashboard-apis) | [falcon_complete_dashboard.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/falcon_complete_dashboard.py) | FalconCompleteDashboard |
| [CrowdStrike Falcon Flight Control](https://falcon.crowdstrike.com/support/documentation/154/flight-control-apis) | [mssp.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/mssp.py) | FlightControl |
| [CrowdStrike Host Groups](https://falcon.crowdstrike.com/support/documentation/84/host-and-host-group-management-apis) | [host_group.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/host_group.py) | HostGroup |
| [CrowdStrike Hosts](https://falcon.crowdstrike.com/support/documentation/84/host-and-host-group-management-apis) | [hosts.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/hosts.py) | Hosts |
| [CrowdStrike Incident and Detection Monitoring](https://falcon.crowdstrike.com/support/documentation/86/detections-monitoring-apis) | [incidents.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/incidents.py) | Incidents |
| CrowdStrike Identity Protections | [identity_protection.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/identity_protection.py) | IdentityProtection |
| [CrowdStrike Installation Tokens](https://falcon.crowdstrike.com/support/documentation/120/Installation-token-APIs) | [installation_tokens.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/installation_tokens.py) | InstallationTokens |
| [CrowdStrike Intel](https://falcon.crowdstrike.com/support/documentation/72/intel-apis) | [intel.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/intel.py) | Intel |
| [CrowdStrike Kubernetes Protection](https://falcon.crowdstrike.com/documentation/177/kubernetes-protection) | [kubernetes_protection.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/kubernetes_protection.py) | KubernetesProtection |
| [CrowdStrike MalQuery](https://falcon.crowdstrike.com/support/documentation/113/malquery-apis) | [malquery.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/malquery.py) | MalQuery |
| CrowdStrike Message Center | [message_center.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/message_center.py) | MessageCenter |
| CrowdStrike ML Exclusions | [ml_exclusions.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/ml_exclusions.py) | MLExclusions |
| [CrowdStrike OAuth2 Auth Token](https://falcon.crowdstrike.com/support/documentation/93/oauth2-auth-token-apis) | [oauth2.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/oauth2.py) | OAuth2 |
| [CrowdStrike Overwatch Dashboard](https://falcon.crowdstrike.com/documentation/155/falcon-overwatch-dashboard-apis) | [overwatch_dashboard.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/overwatch_dashboard.py) | OverwatchDashboard |
| [CrowdStrike Prevention Policy](https://falcon.crowdstrike.com/support/documentation/85/detection-and-prevention-policies-apis) | [prevention_policy.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/prevention_policy.py) | PreventionPolicy |
| CrowdStrike Quarantine | [quarantine.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/quarantine.py) | Quarantine |
| [CrowdStrike Real Time Response (RTR)](https://falcon.crowdstrike.com/support/documentation/90/real-time-response-apis) | [real_time_response.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/real_time_response.py) | RealTimeResponse |
| [CrowdStrike Realtime Response (RTR) Administration](https://falcon.crowdstrike.com/support/documentation/90/real-time-response-apis) | [real_time_response_admin.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/real_time_response_admin.py) | RealTimeResponseAdmin |
| [CrowdStrike Realtime Response (RTR) Policies](https://falcon.crowdstrike.com/documentation/161/real-time-response-policy-apis) | [response_policies.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/response_policies.py) | ResponsePolicies |
| CrowdStrike Recon | [recon.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/recon.py) | Recon |
| CrowdStrike Report Executions | [report_executions.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/report_executions.py) | ReportExecutions |
| CrowdStrike Scheduled Reports | [scheduled_reports.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/scheduled_reports.py) | ScheduledReports |
| [CrowdStrike Sensor Download](https://falcon.crowdstrike.com/support/documentation/109/sensor-download-apis) | [sensor_download.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/sensor_download.py) | SensorDownload |
| CrowdStrike Sensor Visibility Exclusions | [sensor_visibility_exclusions.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/sensor_visibility_exclusions.py) | SensorVisibilityExclusions |
| [CrowdStrike Sensor Update Policy Management](https://falcon.crowdstrike.com/documentation/201/sensor-update-policy-apis) | [sensor_update_policy.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/sensor_update_policy.py) | SensorUpdatePolicy |
| [CrowdStrike Spotlight](https://falcon.crowdstrike.com/support/documentation/98/spotlight-apis) | [spotlight_vulnerabilities.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/spotlight_vulnerabilities.py) | SpotlightVulnerabilities |
| [CrowdStrike User and Roles](https://falcon.crowdstrike.com/support/documentation/87/users-and-roles-apis) | [user_management.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/user_management.py) | UserManagement |
| [Falcon Discover for Cloud and Containers - AWS Accounts](https://falcon.crowdstrike.com/support/documentation/91/discover-for-aws-apis) | [cloud_connect_aws.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/cloud_connect_aws.py) | CloudConnectAWS |
| [Falcon Discover for Cloud and Containers - Azure Subscriptions](https://falcon.crowdstrike.com/support/documentation/118/falcon-discover-for-cloud-and-containers-azure-subscription-apis) <BR/> [Falcon Discover for Cloud and Containers - GCP Projects](https://falcon.crowdstrike.com/support/documentation/117/falcon-discover-for-cloud-and-containers-gcp-projects-apis) | [d4c_registration.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/d4c_registration.py) | D4CRegistration |
| [CrowdStrike Falcon Zero Trust Assessment](https://falcon.crowdstrike.com/support/documentation/156/zero-trust-assessment-apis) | [zero_trust_assessment.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/zero_trust_assessment.py) | ZeroTrustAssessment |

> ![#f03c15](https://via.placeholder.com/10/f03c15/000000?text=+)<small> *Documentation links shown in the table above require a CrowdStrike customer login. Check [falconpy.io](https://falconpy.io) or the [FalconPy wiki](https://github.com/CrowdStrike/falconpy/wiki) for library-specific documentation.*</small>


#### Service Class benefits

- Closesly follows Python / OpenAPI best practices for code style and syntax. PEP-8 compliant.
- Completely abstracts token management, automatically refreshing your token when it expires.
- Provides simple programmatic patterns for interacting with CrowdStrike Falcon APIs.
- Supports [cloud region autodiscovery](https://www.falconpy.io/Usage/Environment-Configuration.html#cloud-region-autodiscovery) for the CrowdStrike `US-1`, `US-2` and `EU-1` regions.
- Supports dynamic [configuration](https://www.falconpy.io/Usage/Environment-Configuration.html) based upon the needs of your environment.
- Supports FalconPy [parameter abstraction](https://www.falconpy.io/Usage/Payload-Handling.html#parameter-abstraction) functionality.
- Supports FalconPy [body payload abstraction](https://www.falconpy.io/Usage/Payload-Handling.html#body-payload-abstraction) functionality.

### The Uber Class
Operating as a single harness for interacting with the entire CrowdStrike Falcon API, the _Uber Class_ can access every available operation within every API service collection.

| Code Location | |
| :--- | :--- |
| [api_complete.py](https://github.com/CrowdStrike/falconpy/blob/main/src/falconpy/api_complete.py) | The Uber Class provides an interface to all CrowdStrike APIs with a single handler. This solution supports communicating with API endpoints that do not have an available Service Class or are recently released. |

#### Uber Class benefits

- Access the entire API with only one import and only one class.
- Completely abstracts token management, automatically refreshing your token when it expires.
- Provides the `override` keyword, allowing you to specify new endpoints that are not yet available within the library.
- Supports [cloud region autodiscovery](https://www.falconpy.io/Usage/Environment-Configuration.html#cloud-region-autodiscovery) for the CrowdStrike `US-1`, `US-2` and `EU-1` regions.
- Supports FalconPy [parameter abstraction](https://www.falconpy.io/Usage/Payload-Handling.html#parameter-abstraction) functionality.
- Supports all [environment configuration](https://www.falconpy.io/Usage/Environment-Configuration.html) options supported by FalconPy Service Classes.


### Comparing FalconPy class types
The Uber Class provides the same performance and output as FalconPy Service Classes, and can perform all of the same operations. The Uber Class does **not** support [body payload abstraction](https://www.falconpy.io/Usage/Payload-Handling.html#body-payload-abstraction) but does provide unique [`override`](https://www.falconpy.io/Usage/Basic-Uber-Class-usage.html#the-command-method) functionality not found within Service Classes.


<img width="1" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==">

![CrowdStrike Divider](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/adversary-lineup-1.png)


## Quick Start :dizzy:

Stable releases of FalconPy are available on the Python Package Index:

```shell
python3 -m pip install crowdstrike-falconpy
```

Once installed, you can immediately begin using CrowdStrike functionality in your Python projects.

```python
"""CrowdStrike FalconPy Quick Start."""
from falconpy import Hosts

hosts = Hosts(client_id="CROWDSTRIKE_API_CLIENT_ID", client_secret="CROWDSTRIKE_API_SECRET")

SEARCH_FILTER = "hostname-search-string"

# Retrieve a list of hosts that have a hostname that matches our search filter
hosts_search_result = hosts.query_devices_by_filter(filter=f"hostname:'{SEARCH_FILTER}'")

# Confirm we received a success response back from the CrowdStrike API
if hosts_search_result["status_code"] == 200:
    hosts_found = hosts_search_result["body"]["resources"]
    # Confirm our search produced results
    if hosts_found:
        # Retrieve the details for all matches
        hosts_detail = hosts.get_device_details(ids=hosts_found)["body"]["resources"]
        for detail in hosts_detail:
            # Display the AID and hostname for this match
            aid = detail["device_id"]
            hostname = detail["hostname"]
            print(f"{hostname} ({aid})")
    else:
        print("No hosts found matching that hostname within your Falcon tenant.")
else:
    # Retrieve the details of the error response
    error_detail = hosts_search_result["body"]["errors"]
    for error in error_detail:
        # Display the API error detail
        error_code = error["code"]
        error_message = error["message"]
        print(f"[Error {error_code}] {error_message}")
```

## Documentation and Support :book:
FalconPy is a community-driven open source project designed to assist developers with implementing CrowdStrike's APIs within their applications, and is not a formal CrowdStrike product. As such it carries no formal support, expressed or implied.

### Official Project Documentation: [falconpy.io](https://falconpy.io)
Extended documentation is also available via the [wiki](https://github.com/CrowdStrike/falconpy/wiki) for this repository.

### Sample code
This repository also maintains a collection of [samples](https://github.com/CrowdStrike/falconpy/tree/main/samples) for use as examples to get you started with integrating CrowdStrike Falcon into your DevOps processes.

### Issues and Questions

Is something going wrong? :fire:

GitHub Issues are used to report bugs and errors.

[![Report Issue](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/report-issue.png)](https://github.com/CrowdStrike/falconpy/issues/new/choose)

Have a question you can't find answered in the documentation?

Please submit usage questions to the Q&A section of our discussion board.

[![Discussions](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/ask-a-question.png)](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AQ%26A)

### Community forums

The discussion board for this repository also provides the community with means to communicate regarding [enhancements ideas](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AIdeas), [integration examples](https://github.com/CrowdStrike/falconpy/discussions/496) and [new releases](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3A%22Show+and+tell%22).

[![Discussions](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/join-the-discussion.png)](https://github.com/CrowdStrike/falconpy/discussions)

### Additional content
Community materials discussing FalconPy are linked below.

[![API Office Hour 03.23.21](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/api_office_hour_preso_thumbnail.png)](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/falconpy-api-office-hour_customer_presentation.pdf?raw=true) 
<img width="50" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==">
[![Fal.Con 2021](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/fal.con-2021-presentation.png)](https://www.crowdstrike.com/falcon/video-on-demand-2021/?wchannelid=w0jyzi2b8e&wmediaid=z5jymvzhyu)

**API Office Hour 03-23-21** <img width="156" height="1" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="> **Fal.Con 2021** 


More information regarding FalconPy documentation and support can be found [here](https://github.com/CrowdStrike/falconpy/blob/main/SUPPORT.md).


## Contribute to FalconPy :coffee:
Interested in joining an elite community of security-focused Python developers and earning your place on our [contributors list](https://github.com/CrowdStrike/falconpy/blob/main/AUTHORS.md#contributors)? 

There are *many* ways you can contribute to the FalconPy project! 

_Providing feedback_ by opening a GitHub ticket. Even a fly-by "hey, this worked..." is appreciated and helps validate approaches. Ideas on improving the project are most welcome.

_Documenting, blogging, or creating videos_, of how you've used FalconPy! This type of content is *invaluable* and helps our community grow. Open a pull request for inclusion in the [Additional content](https://github.com/CrowdStrike/falconpy#additional-content) section of this page.

_Fix a bug or implement a new feature_. Check out our [open issues on GitHub](https://github.com/CrowdStrike/falconpy/issues) or our [discussion board](https://github.com/CrowdStrike/falconpy/discussions) for inspiration.

_Review pull requests_ by going through the queue of [open pull requests on GitHub](https://github.com/CrowdStrike/falconpy/pulls) and giving feedback to the authors.

To become a member of the community, review the [Code of Conduct](https://github.com/CrowdStrike/falconpy/blob/main/CODE_OF_CONDUCT.md) for community guidelines, and the [contribution guide](https://github.com/CrowdStrike/falconpy/blob/main/CONTRIBUTING.md) for more detail regarding contributing to the CrowdStrike FalconPy project.


---


<p align="center"><img src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-footer.png"><BR/><img width="250px" src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/adversary-red-eyes.png"></P>
<h3><P align="center">WE STOP BREACHES <BR/><small><small>(and we can do it using Python)</small></small></P></h3>