# Authenticating to the API

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Authenticating to the API

FalconPy is designed to make authentication and token management easy and supports multiple methods of providing your API credentials.

> The Uber class only supports `Credential Authentication`.

* [Credential Authentication](authenticating-to-the-api.md#credential-authentication)
* [Object Authentication](authenticating-to-the-api.md#object-authentication)
* [Legacy Authentication](authenticating-to-the-api.md#legacy-authentication)

### Credential Authentication

As of [version 0.4.0](../releases/tag/v0.4.0), `Credential Authentication` is the standard method used for authenticating.

* This method is supported in Service Classes and the Uber class.
* You do not need to call the `authenticate()` method before making your first request.
* Your token and your authentication status will not be valid / True until the first request is made.

#### Service Class Example \(Cloud Connect AWS\)

```python
from falconpy import cloud_connect_aws as FalconAWS

falcon = FalconAWS.Cloud_Connect_AWS(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

response = falcon.QueryAWSAccounts()
print(response)
```

#### Uber Class Example \(Cloud Connect AWS\)

```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

response = falcon.command('QueryAWSAccounts')
print(response)
```

### Object Authentication

`Object Authentication` allows you to authenticate to the API, and then pass the returned authentication object to other Service Classes, allowing developers to easily authenticate to multiple API service collection with the same token.

* Object Authentication is only supported in **Service Classes**.

#### Example \(Cloud Connect AWS and Detects\)

```python
from falconpy import oauth2 as FalconAuth
from falconpy import cloud_connect_aws as FalconAWS

auth = FalconAuth.OAuth2(creds={
        'client_id': client_id,
        'client_secret': client_secret
    }
)

falconAWS = FalconAWS.Cloud_Connect_AWS(auth_object=auth)
print(json.dumps(falconAWS.QueryAWSAccounts(), indent=4))

falconDetects = FalconDetects.Detects(auth_object=auth)
print(json.dumps(falconDetects.QueryDetects(), indent=4))
```

### Legacy Authentication

Prior to [version 0.4.0](../releases/tag/v0.4.0), FalconPy Service Classes authenticated using `Legacy Authentication`. This method authenticates by providing the token directly to the Service Class and requires the developer to handle authentication using the [OAuth2](oauth2) Service Class.

* Legacy Authentication is only supported in **Service Classes**.
* This method of authentication **does not** support automatic token refresh.
* This method of authentication **cannot** automatically authenticate your first request.
* Developers _can_ authenticate to multiple Service Classes using the same token utilizing this method.

#### Example \(FalconX Sandbox\)

```python
from falconpy import oauth2 as FalconAuth
from falconpy import falconx_sandbox as FalconX

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconX.FalconX_Sandbox(access_token=token)

    response = falcon.QueryReports()
    print(response)
```

