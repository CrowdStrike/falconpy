# falconpy
Falcon-py provides a Python native harness for interacting with the Falcon Complete oAuth2 API.

## Why falconpy
This project contains a collection of Python classes that abstract Falcon Complete API interaction, removing duplicative code and allowing developers to focus on just the logic of their solution requirements.

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

+ [api_complete.py](api_complete.py) - Falcon Complete API uber-class





