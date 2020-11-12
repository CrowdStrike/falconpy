# falconpy
Falconpy provides a Python native harness for interacting with the Falcon Complete oAuth2 API.

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

### Uber-class
+ [api_complete.py](api_complete.py) - Falcon Complete API interface harness

## Usage examples
For all examples excluding the uber-class, you will first need to create an instance of the OAuth2 class in order to generate a token.

### Regular classes
```python
import falconpy.services.oauth2 as FalconAuth
authorization = FalconAuth.OAuth2(creds={
    'client_id': falcon_client_id,
    'client_secret': falcon_client_secret
    }
)
try:
    token = authorized.token()["body"]["access_token"]
except:
    token = False
```

Once retrieved, the token is leveraged in subsequent requests to different API services. 
> This examples leverages the cloud_connect_aws.py class to interact with the API and AWS.

```python
import falcon_sdk.services.cloud_connect_aws as FalconAWS
falcon = FalconAWS.Cloud_Connect_AWS(access_token=token)
account_list = falcon.QueryAWSAccounts(parameters={ "limit" : "100" })
```

#### Example result
```json
{
    "status_code": 200,
    "headers": {
        "Content-Encoding": "gzip",
        "Content-Length": "699",
        "Content-Type": "application/json",
        "Date": "Thu, 12 Nov 2020 20:18:29 GMT",
        "X-Cs-Region": "us-1",
        "X-Ratelimit-Limit": "6000",
        "X-Ratelimit-Remaining": "5987"
    },
    "body": {
        "meta": {
            "query_time": 0.003052599,
            "pagination": {
                "offset": 3,
                "limit": 100,
                "total": 3
            },
            "powered_by": "cloud-connect-manager",
            "trace_id": "7c182b49-fe3c-4704-9042-12345678e8d3"
        },
        "errors": [],
        "resources": [
            {
                "cid": "123456-redacted-cid",
                "id": "987654321098",
                "iam_role_arn": "arn:aws:iam::987654321098:role/FalconDiscover",
                "external_id": "IwXe54tosfaSDfsE32dS",
                "policy_version": "1",
                "cloudtrail_bucket_owner_id": "987654321098",
                "cloudtrail_bucket_region": "eu-west-1",
                "created_timestamp": "2020-11-12T20:18:28Z",
                "last_modified_timestamp": "2020-11-12T20:18:28Z",
                "last_scanned_timestamp": "2020-11-12T20:18:28Z",
                "provisioning_state": "registered"
            },
            {
                "cid": "123456-redacted-cid",
                "id": "2109876543210",
                "iam_role_arn": "arn:aws:iam::2109876543210:role/CrowdStrikeFalcon",
                "external_id": "AnotherExternalID",
                "policy_version": "1",
                "cloudtrail_bucket_owner_id": "2109876543210",
                "cloudtrail_bucket_region": "eu-west-1",
                "created_timestamp": "2020-10-08T12:44:49Z",
                "last_modified_timestamp": "2020-10-08T12:44:49Z",
                "last_scanned_timestamp": "2020-11-01T00:14:13Z",
                "provisioning_state": "registered",
                "access_health": {
                    "api": {
                        "valid": true,
                        "last_checked": "2020-11-12T20:18:00Z"
                    }
                }
            },
            {
                "cid": "123456-redacted-cid",
                "id": "0123456789012",
                "iam_role_arn": "arn:aws:iam::0123456789012:role/FalconDiscover",
                "external_id": "CrossAccountExternalID",
                "policy_version": "1",
                "cloudtrail_bucket_owner_id": "0123456789012",
                "cloudtrail_bucket_region": "us-east-1",
                "created_timestamp": "2020-08-12T12:43:16Z",
                "last_modified_timestamp": "2020-10-07T09:44:00Z",
                "last_scanned_timestamp": "2020-11-01T00:13:12Z",
                "provisioning_state": "registered",
                "access_health": {
                    "api": {
                        "valid": false,
                        "last_checked": "2020-11-12T20:18:00Z",
                        "reason": "Assume role failed. IAM role arn and/or external is invalid."
                    }
                }
            }
        ]
    }
}
```
### The uber-class
This class farther abstracts token administration allowing the developer to skip this step entirely if desired.

```python
import falconpy.api_complete as FalconSDK
falcon = FalconSDK.APIHarness(creds={'client_id': falcon_client_id,'client_secret': falcon_client_secret})
account_list = falcon.command(action="QueryAWSAccounts", parameters={"limit":"100"})
```

#### Example result
```json
{
    "status_code": 200,
    "headers": {
        "Content-Encoding": "gzip",
        "Content-Length": "699",
        "Content-Type": "application/json",
        "Date": "Thu, 12 Nov 2020 22:34:47 GMT",
        "X-Cs-Region": "us-1",
        "X-Ratelimit-Limit": "6000",
        "X-Ratelimit-Remaining": "5954"
    },
    "body": {
        "meta": {
            "query_time": 0.0030413,
            "pagination": {
                "offset": 3,
                "limit": 100,
                "total": 3
            },
            "powered_by": "cloud-connect-manager",
            "trace_id": "7c182b49-fe3c-4704-9042-12345678e8d3"
        },
        "errors": [],
        "resources": [
            {
                "cid": "123456-redacted-cid",
                "id": "987654321098",
                "iam_role_arn": "arn:aws:iam::987654321098:role/FalconDiscover",
                "external_id": "IwXe54tosfaSDfsE32dS",
                "policy_version": "1",
                "cloudtrail_bucket_owner_id": "987654321098",
                "cloudtrail_bucket_region": "eu-west-1",
                "created_timestamp": "2020-11-12T20:18:28Z",
                "last_modified_timestamp": "2020-11-12T20:18:28Z",
                "last_scanned_timestamp": "2020-11-12T20:18:28Z",
                "provisioning_state": "registered"
            },
            {
                "cid": "123456-redacted-cid",
                "id": "2109876543210",
                "iam_role_arn": "arn:aws:iam::2109876543210:role/CrowdStrikeFalcon",
                "external_id": "AnotherExternalID",
                "policy_version": "1",
                "cloudtrail_bucket_owner_id": "2109876543210",
                "cloudtrail_bucket_region": "eu-west-1",
                "created_timestamp": "2020-10-08T12:44:49Z",
                "last_modified_timestamp": "2020-10-08T12:44:49Z",
                "last_scanned_timestamp": "2020-11-01T00:14:13Z",
                "provisioning_state": "registered",
                "access_health": {
                    "api": {
                        "valid": true,
                        "last_checked": "2020-11-12T22:34:00Z"
                    }
                }
            },
            {
                "cid": "123456-redacted-cid",
                "id": "0123456789012",
                "iam_role_arn": "arn:aws:iam::0123456789012:role/FalconDiscover",
                "external_id": "CrossAccountExternalID",
                "policy_version": "1",
                "cloudtrail_bucket_owner_id": "0123456789012",
                "cloudtrail_bucket_region": "us-east-1",
                "created_timestamp": "2020-08-12T12:43:16Z",
                "last_modified_timestamp": "2020-10-07T09:44:00Z",
                "last_scanned_timestamp": "2020-11-01T00:13:12Z",
                "provisioning_state": "registered",
                "access_health": {
                    "api": {
                        "valid": false,
                        "last_checked": "2020-11-12T22:34:00Z",
                        "reason": "Assume role failed. IAM role arn and/or external is invalid."
                    }
                }
            }
        ]
    }
}
```