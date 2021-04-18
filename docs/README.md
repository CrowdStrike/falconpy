# Home

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)

![PyPI - Downloads](https://img.shields.io/pypi/dm/crowdstrike-falconpy) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Welcome to the FalconPy SDK Wiki

This wiki is focused on documenting the FalconPy SDK for the CrowdStrike Falcon OAuth2 API.

### What is the FalconPy SDK for?

The FalconPy SDK contains a collection of Python classes that abstract CrowdStrike Falcon OAuth2 API interaction, removing duplicative code and allowing developers to focus on just the logic of their solution requirements.

### SDK Contents

This SDK provides two distinct methods for interacting with the CrowdStrike Falcon OAuth2 API.

* Service Classes, representing a single service collection, with methods defined for every available operation.
* The Uber Class, which provides a single harness for interacting with the entire API, covering every available operation within every service collection.

> Examples for interacting with service classes are shown when available. Uber class examples are shown for all operations.

#### Service collections with available service classes

There are currently 24 service classes defined that provide an interface to individual service collections within the CrowdStrike Falcon OAuth2 API.

> There are 10 additional service classes planned that will cover remaining available service collections. Customers needing to access service collections that are not covered by one of the existing service classes may make use of the Uber class in order to access these service collections.

| Service Collection | Purpose |
| :--- | :--- |
| [Cloud Connect AWS](service-collections/cloud-connect-aws.md) | Falcon Discover for Cloud and Containers - Amazon Web Services |
| [CSPM Registration](service-collections/cspm-registration.md) | CrowdStrike Falcon Horizon API |
| [Custom IOA](service-collections/custom-ioa.md) | CrowdStrike Custom Indicators of Attack API |
| [Detects](service-collections/detects.md) | CrowdStrike Detections API |
| [Device Control Policies](service-collections/device-control-policies.md) | CrowdStrike Device Control API |
| [Event Streams](service-collections/event-streams.md) | CrowdStrike Event Streams API |
| [FalconX Sandbox](service-collections/falconx-sandbox.md) | CrowdStrike Falcon Sandbox API |
| [Firewall Management](service-collections/firewall-management.md) | CrowdStrike Firewall Management API |
| [Firewall Policies](service-collections/firewall-policies.md) | CrowdStrike Firewall Policy Management API |
| [Falcon Flight Control \(MSSP\)](service-collections/mssp.md) | CrowdStrike Falcon Flight Control API |
| [Host Group](service-collections/host-group.md) | CrowdStrike Host Groups API |
| [Hosts](service-collections/hosts.md) | CrowdStrike Hosts API |
| [Incidents](service-collections/incidents.md) | CrowdStrike Incidents and Detection Monitoring API |
| [Intel](service-collections/intel.md) | CrowdStrike Threat Intel API |
| [IOCs](service-collections/iocs.md) | CrowdStrike Custom Indicators of Compromise API |
| [OAuth2](service-collections/oauth2.md) | CrowdStrike OAuth2 Token API |
| [Prevention Policy](service-collections/prevention-policies.md) | CrowdStrike Prevention Policy API |
| [Quick Scan](service-collections/quick-scan.md) | CrowdStrike Quick Scan API |
| [Real Time Response](service-collections/real-time-response.md) | CrowdStrike Real Time Response \(RTR\) API |
| [Real Time Response Admin](service-collections/real-time-response-admin.md) | CrowdStrike Real Time Response \(RTR\) Administration API |
| [Sample Uploads](service-collections/sample-uploads.md) | CrowdStrike Sample Uploads API |
| [Sensor Download](service-collections/sensor-download.md) | CrowdStrike Sensor Download API |
| [Sensor Update Policy](service-collections/sensor-update-policies.md) | CrowdStrike Sensor Policy Management API |
| [Spotlight Vulnerabilities](service-collections/spotlight-vulnerabilities.md) | CrowdStrike Spotlight API |
| [User Management](service-collections/user-management.md) | CrowdStrike User and Roles API |
| [Zero Trust Assessment](service-collections/zero-trust-assessment.md) | CrowdStrike Zero Trust Assessment API |

#### Service collections only available via the Uber class

| Service Collection | Purpose |
| :--- | :--- |
| [D4C Registration](service-collections/d4c-registration.md) | Falcon Discover for Cloud and Containers - Azure / GCP |
| [Installation Tokens](service-collections/installation-tokens.md) | CrowdStrike Installation Token API |
| [Falcon Complete Dashboard](service-collections/falcon-complete-dashboard.md) | CrowdStrike Falcon Complete Dashboard API |
| [MalQuery](service-collections/malquery.md) | CrowdStrike MalQuery API |
| [IOA Exclusions](service-collections/ioa-exclusions.md) | CrowdStrike Indicators of Attack Exclusions API |
| [ML Exclusions](service-collections/ml-exclusions.md) | CrowdStrike ML Exclusions API |
| [Overwatch Dashboard](service-collections/overwatch-dashboard.md) | CrowdStrike Falcon Overwatch Dashboard API |
| [Sensor Visibility Exclusions](service-collections/sensor-visibility-exclusions.md) | CrowdStrike Sensor Visibility Exclusions API |

### Installation

![Project Status: Active &#x2013; The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg) ![PyPI](https://img.shields.io/pypi/v/crowdstrike-falconpy) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/crowdstrike-falconpy) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/crowdstrike-falconpy) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/crowdstrike-falconpy)

More details regarding installation can be found at [Installation, Upgrades and Removal](installation-upgrades-and-removal.md).

### Basic usage

The following two examples show interaction with the Cloud Connect AWS service collection using the Service Class and the Uber Class. For more detailed examples, please review the service collection wiki pages and the [Samples Collection](https://github.com/CrowdStrike/falconpy/tree/main/samples). If you still have questions, feel free to reach out to us on the [discussion board](https://github.com/CrowdStrike/falconpy/discussions).

* [Basic Service Class usage](basic-service-class-usage.md)
* [Basic Uber Class usage](basic-uber-class-usage.md)

Additionally, code samples are added to the project as the are developed.

* [Code samples](https://github.com/CrowdStrike/falconpy/tree/main/samples)

### CrowdStrike FalconPy is _free_ <a id="crowdstrike-falconpy-is-free"></a>

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to [https://unlicense.org](https://unlicense.org)                       ![PyPI - License](https://img.shields.io/pypi/l/crowdstrike-falconpy)   

