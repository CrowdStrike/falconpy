# Using the Host Group service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [queryCombinedGroupMembers](#querycombinedgroupmembers) | Search for members of a Host Group in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedHostGroups](#querycombinedhostgroups) | Search for Host Groups in your environment by providing an FQL filter and paging details. Returns a set of Host Groups which match the filter criteria |
| [performGroupAction](#performgroupaction) | Perform the specified action on the Host Groups specified in the request |
| [getHostGroups](#gethostgroups) | Retrieve a set of Host Groups by specifying their IDs |
| [createHostGroups](#createhostgroups) | Create Host Groups by specifying details about the group to create |
| [deleteHostGroups](#deletehostgroups) | Delete a set of Host Groups by specifying their IDs |
| [updateHostGroups](#updatehostgroups) | Update Host Groups by specifying the ID of the group and details to update |
| [queryGroupMembers](#querygroupmembers) | Search for members of a Host Group in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [queryHostGroups](#queryhostgroups) | Search for Host Groups in your environment by providing an FQL filter and paging details. Returns a set of Host Group IDs which match the filter criteria |
### queryCombinedGroupMembers
Search for members of a Host Group in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __id__ | query | _string_ | The ID of the Host Group to search for members of |
| | __filter__ | query | _string_ | The filter expression that should be used to limit the results |
| | __offset__ | query | _integer_ | The offset to start retrieving records from |
| | __limit__ | query | _integer_ | The maximum records to return. [1-5000] |
| | __sort__ | query | _string_ | The property to sort by |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import host_group as FalconHG

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHG.Host_Group(access_token=token)

    PARAMS = {
        'id': 'string',
        'filter': 'string',
        'offset': integer,
        'limit': integer,
        'sort': 'string'
    }

    response = falcon.queryCombinedGroupMembers(parameters=PARAMS)
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
    'id': 'string',
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('queryCombinedGroupMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### queryCombinedHostGroups
Search for Host Groups in your environment by providing an FQL filter and paging details. Returns a set of Host Groups which match the filter criteria

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __filter__ | query | _string_ | The filter expression that should be used to limit the results |
| | __offset__ | query | _integer_ | The offset to start retrieving records from |
| | __limit__ | query | _integer_ | The maximum records to return. [1-5000] |
| | __sort__ | query | _string_ | The property to sort by |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import host_group as FalconHG

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHG.Host_Group(access_token=token)

    PARAMS = {
        'filter': 'string',
        'offset': integer,
        'limit': integer,
        'sort': 'string'
    }

    response = falcon.queryCombinedHostGroups(parameters=PARAMS)
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
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('queryCombinedHostGroups', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### performGroupAction
Perform the specified action on the Host Groups specified in the request

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __action_name__ | query | _string_ | The action to perform |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import host_group as FalconHG

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHG.Host_Group(access_token=token)

    PARAMS = {
        'action_name': 'string'
    }

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.performGroupAction(parameters=PARAMS, body=BODY)
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

response = falcon.command('performGroupAction', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```
### getHostGroups
Retrieve a set of Host Groups by specifying their IDs

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the Host Groups to return |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import host_group as FalconHG

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHG.Host_Group(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.getHostGroups(ids=IDS)
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

response = falcon.command('getHostGroups', ids=IDS)
print(response)
falcon.deauthenticate()
```
### createHostGroups
Create Host Groups by specifying details about the group to create

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import host_group as FalconHG

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHG.Host_Group(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.createHostGroups(body=BODY)
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

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.command('createHostGroups', body=BODY)
print(response)
falcon.deauthenticate()
```
### deleteHostGroups
Delete a set of Host Groups by specifying their IDs

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the Host Groups to delete |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import host_group as FalconHG

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHG.Host_Group(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.deleteHostGroups(ids=IDS)
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

response = falcon.command('deleteHostGroups', ids=IDS)
print(response)
falcon.deauthenticate()
```
### updateHostGroups
Update Host Groups by specifying the ID of the group and details to update

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import host_group as FalconHG

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHG.Host_Group(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.updateHostGroups(body=BODY)
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

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.command('updateHostGroups', body=BODY)
print(response)
falcon.deauthenticate()
```
### queryGroupMembers
Search for members of a Host Group in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __id__ | query | _string_ | The ID of the Host Group to search for members of |
| | __filter__ | query | _string_ | The filter expression that should be used to limit the results |
| | __offset__ | query | _integer_ | The offset to start retrieving records from |
| | __limit__ | query | _integer_ | The maximum records to return. [1-5000] |
| | __sort__ | query | _string_ | The property to sort by |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import host_group as FalconHG

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHG.Host_Group(access_token=token)

    PARAMS = {
        'id': 'string',
        'filter': 'string',
        'offset': integer,
        'limit': integer,
        'sort': 'string'
    }

    response = falcon.queryGroupMembers(parameters=PARAMS)
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
    'id': 'string',
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('queryGroupMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### queryHostGroups
Search for Host Groups in your environment by providing an FQL filter and paging details. Returns a set of Host Group IDs which match the filter criteria

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __filter__ | query | _string_ | The filter expression that should be used to limit the results |
| | __offset__ | query | _integer_ | The offset to start retrieving records from |
| | __limit__ | query | _integer_ | The maximum records to return. [1-5000] |
| | __sort__ | query | _string_ | The property to sort by |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import host_group as FalconHG

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconHG.Host_Group(access_token=token)

    PARAMS = {
        'filter': 'string',
        'offset': integer,
        'limit': integer,
        'sort': 'string'
    }

    response = falcon.queryHostGroups(parameters=PARAMS)
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
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('queryHostGroups', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
