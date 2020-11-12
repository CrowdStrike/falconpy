# falconpy
Falcon-py provides a Python native harness for interacting with the Falcon Complete oAuth2 API.

## Why falconpy
This project contains a collection of Python classes that abstract Falcon Complete API interaction, removing duplicative code and allowing developers to focus on just the logic of their solution requirements.

## Contents
Currently the solution defines a class for each service (_ex: cloud_connect_aws_), with endpoint methods defined as class methods. There is also a single _uber_-class that provides an interface to the entire API with a single handler.

### Available classes
+ [cloud_connect_aws.py](services/cloud_connect_aws.py) - AWS Cloud
+ `detects.py` - Detections
+ `device_control_policies.py` - Device Control
+ `event_streams.py` - Event Streams
+ `falconx_sandbox.py` - The Falcon Sandbox
+ `firewall_management.py` - Firewall administration
+ `firewall_policies.py` - Firewall policy management
+ `host_group.py` - Host groups
+ `hosts.py` - Hosts
+ `incidents.py` - Incidents
+ `intel.py` - Threat Intel
+ `iocs.py` - Indicators of Compromise
+ `oauth2.py` - oAuth2 authentication
+ `prevention_policy.py` - Prevention policies
+ `real_time_response_admin.py` - Real time response administration
+ `real_time_response.py` - Real time response
+ `sensor_update_policy.py` - Sensor policy management
+ `spotlight_vulnerabilities.py` - Vulnerabilities
+ `user_management.py` - User administration

+ `api_complete.py` - Falcon Complete API uber-class





