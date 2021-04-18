# OAuth2

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the OAuth2 service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [oauth2RevokeToken](oauth2.md#oauth2revoketoken) | Revoke a previously issued OAuth2 access token before the end of its standard 30-minute lifespan. |
| [oauth2AccessToken](oauth2.md#oauth2accesstoken) | Generate an OAuth2 access token |

### oauth2RevokeToken

Revoke a previously issued OAuth2 access token before the end of its standard 30-minute lifespan.

**Content-Type**

* Consumes: _application/x-www-form-urlencoded_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **token** | formData | _string_ | The OAuth2 access token you want to revoke.  Include your API client ID and secret in basic auth format \(`Authorization: basic <encoded API client ID and secret>`\) in your request header. |

**Usage**

**Service class example**

```python
from falconpy import oauth2 as FalconAuth

falcon = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PAYLOAD = {
    'token': 'string'
}

response = falcon.oauth2RevokeToken(data=PAYLOAD)
print(response)
```

**Uber class example**

```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

PAYLOAD = {
    'token': 'string'
}

response = falcon.command('oauth2RevokeToken', data=PAYLOAD)
print(response)
falcon.deauthenticate()
```

### oauth2AccessToken

Generate an OAuth2 access token

**Content-Type**

* Consumes: _application/x-www-form-urlencoded_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **client\_id** | formData | _string_ | The API client ID to authenticate your API requests. For information on generating API clients, see [API documentation inside Falcon](https://falcon.crowdstrike.com/support/documentation/1/crowdstrike-api-introduction-for-developers). |
| :white\_check\_mark: | **client\_secret** | formData | _string_ | The API client secret to authenticate your API requests. For information on generating API clients, see [API documentation inside Falcon](https://falcon.crowdstrike.com/support/documentation/1/crowdstrike-api-introduction-for-developers). |
|  | **member\_cid** | formData | _string_ | For MSSP Master CIDs, optionally lock the token to act on behalf of this member CID |

**Usage**

**Service class example**

```python
from falconpy import oauth2 as FalconAuth

falcon = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PAYLOAD = {
    'client_id': 'string',
    'client_secret': 'string',
    'member_cid': 'string'
}

response = falcon.oauth2AccessToken(data=PAYLOAD)
print(response)
```

**Uber class example**

```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

PAYLOAD = {
    'client_id': 'string',
    'client_secret': 'string',
    'member_cid': 'string'
}

response = falcon.command('oauth2AccessToken', data=PAYLOAD)
print(response)
falcon.deauthenticate()
```

