# Using the Hosts service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [PerformActionV2](#performactionv2) | Take various actions on the hosts in your environment. Contain or lift containment on a host. Delete or restore a host. |
| [GetDeviceDetails](#getdevicedetails) | Get details on one or more hosts by providing agent IDs (AID). You can get a host's agent IDs (AIDs) from the /devices/queries/devices/v1 endpoint, the Falcon console or the Streaming API |
| [QueryHiddenDevices](#queryhiddendevices) | Retrieve hidden hosts that match the provided filter criteria. |
| [QueryDevicesByFilterScroll](#querydevicesbyfilterscroll) | Search for hosts in your environment by platform, hostname, IP, and other criteria with continuous pagination capability (based on offset pointer which expires after 2 minutes with no maximum limit) |
| [QueryDevicesByFilter](#querydevicesbyfilter) | Search for hosts in your environment by platform, hostname, IP, and other criteria. |
### PerformActionV2
Take various actions on the hosts in your environment. Contain or lift containment on a host. Delete or restore a host.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __action_name__ | query | _string_ | Specify one of these actions:  - `contain` - This action contains the host, which stops any network communications to locations other than the CrowdStrike cloud and IPs specified in your [containment policy](https://falcon.crowdstrike.com/support/documentation/11/getting-started-guide#containmentpolicy) - `lift_containment`: This action lifts containment on the host, which returns its network communications to normal - `hide_host`: This action will delete a host. After the host is deleted, no new detections for that host will be reported via UI or APIs - `unhide_host`: This action will restore a host. Detection reporting will resume after the host is restored |
| :white_check_mark: | __body__ | body | _string_ | The host agent ID (AID) of the host you want to contain. Get an agent ID from a detection, the Falcon console, or the Streaming API.  Provide the ID in JSON format with the key `ids` and the value in square brackets, such as:   `"ids": ["123456789"]` |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import hosts as FalconHosts

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHosts.Hosts(access_token=token)

    PARAMS = {
        'action_name': 'string'
    }

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.PerformActionV2(parameters=PARAMS, body=BODY)
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
    'action_name': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.command('PerformActionV2', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```
### GetDeviceDetails
Get details on one or more hosts by providing agent IDs (AID). You can get a host's agent IDs (AIDs) from the /devices/queries/devices/v1 endpoint, the Falcon console or the Streaming API

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The host agentIDs used to get details on |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import hosts as FalconHosts

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHosts.Hosts(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.GetDeviceDetails(ids=IDS)
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

IDS = 'ID1,ID2,ID3'

response = falcon.command('GetDeviceDetails', ids=IDS)
print(response)
falcon.deauthenticate()
```
### QueryHiddenDevices
Retrieve hidden hosts that match the provided filter criteria.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _integer_ | The offset to start retrieving records from |
| | __limit__ | query | _integer_ | The maximum records to return. [1-5000] |
| | __sort__ | query | _string_ | The property to sort by (e.g. status.desc or hostname.asc) |
| | __filter__ | query | _string_ | The filter expression that should be used to limit the results |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import hosts as FalconHosts

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHosts.Hosts(access_token=token)

    PARAMS = {
        'offset': integer,
        'limit': integer,
        'sort': 'string',
        'filter': 'string'
    }

    response = falcon.QueryHiddenDevices(parameters=PARAMS)
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
    'offset': integer,
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.command('QueryHiddenDevices', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### QueryDevicesByFilterScroll
Search for hosts in your environment by platform, hostname, IP, and other criteria with continuous pagination capability (based on offset pointer which expires after 2 minutes with no maximum limit)

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _string_ | The offset to page from, for the next result set |
| | __limit__ | query | _integer_ | The maximum records to return. [1-5000] |
| | __sort__ | query | _string_ | The property to sort by (e.g. status.desc or hostname.asc) |
| | __filter__ | query | _string_ | The filter expression that should be used to limit the results |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import hosts as FalconHosts

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHosts.Hosts(access_token=token)

    PARAMS = {
        'offset': 'string',
        'limit': integer,
        'sort': 'string',
        'filter': 'string'
    }

    response = falcon.QueryDevicesByFilterScroll(parameters=PARAMS)
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
    'offset': 'string',
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.command('QueryDevicesByFilterScroll', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### QueryDevicesByFilter
Search for hosts in your environment by platform, hostname, IP, and other criteria.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _integer_ | The offset to start retrieving records from |
| | __limit__ | query | _integer_ | The maximum records to return. [1-5000] |
| | __sort__ | query | _string_ | The property to sort by (e.g. status.desc or hostname.asc) |
| | __filter__ | query | _string_ | The filter expression that should be used to limit the results |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import hosts as FalconHosts

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHosts.Hosts(access_token=token)

    PARAMS = {
        'offset': integer,
        'limit': integer,
        'sort': 'string',
        'filter': 'string'
    }

    response = falcon.QueryDevicesByFilter(parameters=PARAMS)
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
    'offset': integer,
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.command('QueryDevicesByFilter', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
