# Service Class basics

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Basic Service Class usage

Service Classes support multiple methods of authentication depending on the needs of your solution.

* [Credential Authentication](basic-service-class-usage.md#credential-authentication)
* [Object Authentication](basic-service-class-usage.md#object-authentication)
* [Legacy Authentication](basic-service-class-usage.md#legacy-authentication)
* [Example Results](basic-service-class-usage.md#example-result)

### Credential Authentication

Credential Authentication allows you to pass your credentials directly to the Service Class when you create it.

```python
from falconpy import cloud_connect_aws as FalconAWS
authorization = FalconAWS.Cloud_Connect_AWS(creds={
        'client_id': falcon_client_id,
        'client_secret': falcon_client_secret
    }
)
```

### Object Authentication

Object Authentication allows you to create an instance of the OAuth2 Service Class, authenticate, and then use this object to interact with other API service collections.

```python
from falconpy import oauth2 as FalconAuth
from falconpy import cloud_connect_aws as FalconAWS
authorization = FalconAuth.OAuth2(creds={
        'client_id': falcon_client_id,
        'client_secret': falcon_client_secret
    }
)
falcon = FalconAWS.Cloud_Connect_AWS(auth_object=authorization)
```

### Legacy Authentication

In order to make use of legacy authentication, you will first need to create an instance of the OAuth2 class in order to generate a token.

```python
from falconpy import oauth2 as FalconAuth
from falconpy import cloud_connect_aws as FalconAWS   
authorization = FalconAuth.OAuth2(creds={
        'client_id': falcon_client_id,
        'client_secret': falcon_client_secret
    }
)
try:
    token = authorization.token()["body"]["access_token"]
    falcon = FalconAWS.Cloud_Connect_AWS(access_token=token)

except:
    token = False
```

### Performing a request

Once you have provided your API credentials \(and authenticated if necessary\) you are ready to interact with different API service collections.

> This examples leverages the Cloud Connect AWS service class to interact with the CrowdStrike Falcon OAuth2 API regarding Amazon Web Service deployments.

```python
account_list = falcon.QueryAWSAccounts(parameters={ "limit" : "100" })
print(account_list)
```

### Example result

```javascript
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

