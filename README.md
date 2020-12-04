# FalconPy
FalconPy provides a Python native harness for interacting with the CrowdStrike Falcon oAuth2 API.

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
+ [oauth2.py](services/oauth2.py) - oAuth2 authentication
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
$ python -m pip install falconpy
```

## Documentation
Documentation can be found in the [GitHub Wiki](https://github.com/CrowdStrike/falconpy/wiki).

## License
Copyright CrowdStrike 2020

By accessing or using this script, sample code, application programming interface, tools, 
and/or associated documentation (if any) (collectively, “Tools”), You (i) represent and 
warrant that You are entering into this Agreement on behalf of a company, organization 
or another legal entity (“Entity”) that is currently a customer or partner of 
CrowdStrike, Inc. (“CrowdStrike”), and (ii) have the authority to bind such Entity and 
such Entity agrees to be bound by this Agreement.

CrowdStrike grants Entity a non-exclusive, non-transferable, non-sublicensable, royalty 
free and limited license to access and use the Tools solely for Entity’s internal business 
purposes and in accordance with its obligations under any agreement(s) it may have with 
CrowdStrike. Entity acknowledges and agrees that CrowdStrike and its licensors retain all 
right, title and interest in and to the Tools, and all intellectual property rights 
embodied therein, and that Entity has no right, title or interest therein except for the 
express licenses granted hereunder and that Entity will treat such Tools as CrowdStrike’s 
confidential information.

THE TOOLS ARE PROVIDED “AS-IS” WITHOUT WARRANTY OF ANY KIND, WHETHER EXPRESS, IMPLIED OR 
STATUTORY OR OTHERWISE. CROWDSTRIKE SPECIFICALLY DISCLAIMS ALL SUPPORT OBLIGATIONS AND 
ALL WARRANTIES, INCLUDING WITHOUT LIMITATION, ALL IMPLIED WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR PARTICULAR PURPOSE, TITLE, AND NON-INFRINGEMENT. IN NO EVENT SHALL CROWDSTRIKE 
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THE TOOLS, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
