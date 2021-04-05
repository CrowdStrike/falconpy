![CrowdStrike Falcon](../../docs/asset/cs-logo.png)
# FalconPy - The CrowdStrike Falcon SDK for Python 3
This folder contains the FalconPy project, a Python 3 interface handler for the CrowdStrike Falcon OAuth2 API.

## Service Classes
### Currently implemented:
+ `cloud_connect_aws.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-connect-aws
+ `cspm-registration.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration
+ `detects.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects
+ `device_control_policies.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/device-control-policies
+ `event_streams.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/event-streams
+ `falconx_sandbox.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox
+ `firewall_management.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-management
+ `firewall_policies.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/firewall-policies
+ `host_group.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group
+ `hosts.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts
+ `incidents.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents
+ `intel.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel
+ `iocs.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs
+ `oauth2.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/oauth2
+ `prevention_policy.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/prevention-policies
+ `real_time_response_admin.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response-admin
+ `real_time_response.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/real-time-response
+ `sample_uploads.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sample-uploads
+ `sensor_download.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-download
+ `sensor_update_policy.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies
+ `spotlight_vulnerabilities.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/spotlight-vulnerabilities
+ `user_management.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management

### Planned
+ `d4c_registration.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration
+ `installation_tokens.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens
+ `custom_ioa.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/custom-ioa
+ `malquery.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/malquery
+ `ioa_exclusions.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions
+ `ml_exclusions.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ml-exclusions
+ `sensor_visibility_exclusions.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-visibility-exclusions
+ `quick_scan.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan

## The Uber Class
### A single class to interface with the entire API
+ `api_complete.py` https://assets.falcon.crowdstrike.com/support/api/swagger.html
