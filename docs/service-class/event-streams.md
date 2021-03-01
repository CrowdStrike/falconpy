# Using the Event Streams service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [refreshActiveStreamSession](#refreshactivestreamsession) | Refresh an active event stream. Use the URL shown in a GET /sensors/entities/datafeed/v2 response. |
| [listAvailableStreamsOAuth2](#listavailablestreamsoauth2) | Discover all event streams in your environment |
### refreshActiveStreamSession
Refresh an active event stream. Use the URL shown in a GET /sensors/entities/datafeed/v2 response.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __action_name__ | query | _string_ | Action name. Allowed value is refresh_active_stream_session. |
| :white_check_mark: | __appId__ | query | _string_ | Label that identifies your connection. Max: 32 alphanumeric characters (a-z, A-Z, 0-9). |
| :white_check_mark: | __partition__ | path | _integer_ | Partition to request data for. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import event_streams as FalconES

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconES.Event_Streams(access_token=token)

    PARAMS = {
        'action_name': 'string',
        'appId': 'string'
    }

    PARTITION = 0   #Refresh the partition we are working with

    response = falcon.refreshActiveStreamSession(parameters=PARAMS, partition=PARTITION)
    print(response)

    authorization.revoke(token=token)
```
##### Uber class example
```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

PARAMS = {
    'action_name': 'string',
    'appId': 'string'
}

PARTITION = 0   #Refresh the partition we are working with

response = falcon.command('refreshActiveStreamSession', parameters=PARAMS, partition=PARTITION)
print(response)
falcon.deauthenticate()
```
### listAvailableStreamsOAuth2
Discover all event streams in your environment

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __appId__ | query | _string_ | Label that identifies your connection. Max: 32 alphanumeric characters (a-z, A-Z, 0-9). |
| | __format__ | query | _string_ | Format for streaming events. Valid values: json, flatjson |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import event_streams as FalconES

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconES.Event_Streams(access_token=token)

    PARAMS = {
        'appId': 'string',
        'format': 'string'
    }

    response = falcon.listAvailableStreamsOAuth2(parameters=PARAMS)
    print(response)

    authorization.revoke(token=token)
```
##### Uber class example
```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

PARAMS = {
    'appId': 'string',
    'format': 'string'
}

response = falcon.command('listAvailableStreamsOAuth2', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
