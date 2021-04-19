# Uber Class basics

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Basic Uber class usage

The Uber class abstracts token administration allowing the developer to skip this step entirely if desired.

> You will not authenticate until your first request to the API is made. If you check your authentication status, your token or your token_expiration before doing so, the results will be \_False_.

```python
from falconpy import api_complete as FalconSDK
falcon = FalconSDK.APIHarness(creds={
        'client_id': falcon_client_id,
        'client_secret': falcon_client_secret
    }
)
account_list = falcon.command(action="QueryAWSAccounts", parameters={ "limit" : "100" })
print(account_list)
falcon.deauthenticate()
```

### Example result

```javascript
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

Authorization status and the token are still available via the Uber class as constants.

```python
from falconpy import api_complete as FalconSDK
falcon = FalconSDK.APIHarness(creds={
        'client_id': falcon_client_id,
        'client_secret': falcon_client_secret
    }
)
falcon.authenticate()
if falcon.authenticated:
    print(falcon.token)
```

### Example result

```bash
$ eyJhbGciOiJSUzI1NiIsImtpZCI6InB1YmxpYzph...really long token string
```

