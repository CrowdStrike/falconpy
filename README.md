![PyPI - Status](https://img.shields.io/pypi/status/crowdstrike-falconpy)
![PyPI](https://img.shields.io/pypi/v/crowdstrike-falconpy)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/crowdstrike-falconpy)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/crowdstrike-falconpy)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/crowdstrike-falconpy)
![PyPI - Downloads](https://img.shields.io/pypi/dm/crowdstrike-falconpy)
![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)

# FalconPy
FalconPy provides a Python native harness for interacting with the CrowdStrike Falcon OAuth2 API.

## Why FalconPy
This project contains a collection of Python classes that abstract CrowdStrike Falcon API interaction, removing duplicative code and allowing developers to focus on just the logic of their solution requirements.

## Contents
Currently the solution defines a class for each service (_ex: cloud_connect_aws_), with endpoint methods defined as class methods. There is also a single _uber_-class that provides an interface to the entire API with a single handler.

### Available classes
+ [cloud_connect_aws.py](services/cloud_connect_aws.py) - AWS Cloud
+ [detects.py](services/detects.py) - Detections
+ [device_control_policies.py](services/device_control_policies.py) - Device Control
+ [event_streams.py](services/event_streams.py) - Event Streams
+ [falconx_sandbox.py](services/falconx_sandbox.py) - The Falcon Sandbox
+ [firewall_management.py](services/firewall_management.py) - Firewall administration
+ [firewall_policies.py](services/firewall_policies.py) - Firewall policy management
+ [host_group.py](services/host_group.py) - Host groups
+ [hosts.py](services/hosts.py) - Hosts
+ [incidents.py](services/incidents.py) - Incidents
+ [intel.py](services/intel.py) - Threat Intel
+ [iocs.py](services/iocs.py) - Indicators of Compromise
+ [oauth2.py](services/oauth2.py) - OAuth2 authentication
+ [prevention_policy.py](services/prevention_policy.py) - Prevention policies
+ [real_time_response_admin.py](services/real_time_response_admin.py) - Real time response administration
+ [real_time_response.py](services/real_time_response.py) - Real time response
+ [sensor_update_policy.py](services/sensor_update_policy.py) - Sensor policy management
+ [spotlight_vulnerabilities.py](services/spotlight_vulnerabilities.py) - Vulnerabilities
+ [user_management.py](services/user_management.py) - User administration

### Uber-class
+ [api_complete.py](api_complete.py) - CrowdStrike Falcon API full interface harness

## Installation
FalconPy is available on PyPI:
```bash
$ python -m pip install crowdstrike-falconpy
```

## Documentation
Documentation can be found in the [GitHub Wiki](https://github.com/CrowdStrike/falconpy/wiki).

## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

