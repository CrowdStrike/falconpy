# Using the ML Exclusions service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-X%20No-red.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [getMLExclusionsV1](#getmlexclusionsv1) | Get a set of ML Exclusions by specifying their IDs |
| [createMLExclusionsV1](#createmlexclusionsv1) | Create the ML exclusions |
| [deleteMLExclusionsV1](#deletemlexclusionsv1) | Delete the ML exclusions by id |
| [updateMLExclusionsV1](#updatemlexclusionsv1) | Update the ML exclusions |
| [queryMLExclusionsV1](#querymlexclusionsv1) | Search for ML exclusions. |
### getMLExclusionsV1
Get a set of ML Exclusions by specifying their IDs

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The ids of the exclusions to retrieve |
#### Usage
##### Uber class example
```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

IDS = 'ID1,ID2,ID3'

response = falcon.command('getMLExclusionsV1', ids=IDS)
print(response)
falcon.deauthenticate()
```
### createMLExclusionsV1
Create the ML exclusions

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
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

response = falcon.command('createMLExclusionsV1', body=BODY)
print(response)
falcon.deauthenticate()
```
### deleteMLExclusionsV1
Delete the ML exclusions by id

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The ids of the exclusions to delete |
| | __comment__ | query | _string_ | Explains why this exclusions was deleted |
#### Usage
##### Uber class example
```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

PARAMS = {
    'comment': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('deleteMLExclusionsV1', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### updateMLExclusionsV1
Update the ML exclusions

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
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

response = falcon.command('updateMLExclusionsV1', body=BODY)
print(response)
falcon.deauthenticate()
```
### queryMLExclusionsV1
Search for ML exclusions.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __filter__ | query | _string_ | The filter expression that should be used to limit the results. |
| | __offset__ | query | _integer_ | The offset to start retrieving records from |
| | __limit__ | query | _integer_ | The maximum records to return. [1-500] |
| | __sort__ | query | _string_ | The sort expression that should be used to sort the results. |
#### Usage
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

response = falcon.command('queryMLExclusionsV1', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
