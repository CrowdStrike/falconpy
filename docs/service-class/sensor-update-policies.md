# Using the Sensor Update Policies service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-X%20No-red.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [revealUninstallToken](#revealuninstalltoken) | Reveals an uninstall token for a specific device. To retrieve the bulk maintenance token pass the value 'MAINTENANCE' as the value for 'device_id' |
| [queryCombinedSensorUpdateBuilds](#querycombinedsensorupdatebuilds) | Retrieve available builds for use with Sensor Update Policies |
| [queryCombinedSensorUpdatePolicyMembers](#querycombinedsensorupdatepolicymembers) | Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedSensorUpdatePolicies](#querycombinedsensorupdatepolicies) | Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria |
| [queryCombinedSensorUpdatePoliciesV2](#querycombinedsensorupdatepoliciesv2) | Search for Sensor Update Policies with additional support for uninstall protection in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria |
| [performSensorUpdatePoliciesAction](#performsensorupdatepoliciesaction) | Perform the specified action on the Sensor Update Policies specified in the request |
| [setSensorUpdatePoliciesPrecedence](#setsensorupdatepoliciesprecedence) | Sets the precedence of Sensor Update Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence |
| [getSensorUpdatePolicies](#getsensorupdatepolicies) | Retrieve a set of Sensor Update Policies by specifying their IDs |
| [createSensorUpdatePolicies](#createsensorupdatepolicies) | Create Sensor Update Policies by specifying details about the policy to create |
| [deleteSensorUpdatePolicies](#deletesensorupdatepolicies) | Delete a set of Sensor Update Policies by specifying their IDs |
| [updateSensorUpdatePolicies](#updatesensorupdatepolicies) | Update Sensor Update Policies by specifying the ID of the policy and details to update |
| [getSensorUpdatePoliciesV2](#getsensorupdatepoliciesv2) | Retrieve a set of Sensor Update Policies with additional support for uninstall protection by specifying their IDs |
| [createSensorUpdatePoliciesV2](#createsensorupdatepoliciesv2) | Create Sensor Update Policies by specifying details about the policy to create with additional support for uninstall protection |
| [updateSensorUpdatePoliciesV2](#updatesensorupdatepoliciesv2) | Update Sensor Update Policies by specifying the ID of the policy and details to update with additional support for uninstall protection |
| [querySensorUpdatePolicyMembers](#querysensorupdatepolicymembers) | Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [querySensorUpdatePolicies](#querysensorupdatepolicies) | Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policy IDs which match the filter criteria |
### revealUninstallToken
Reveals an uninstall token for a specific device. To retrieve the bulk maintenance token pass the value 'MAINTENANCE' as the value for 'device_id'

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

response = falcon.command('revealUninstallToken', body=BODY)
print(response)
falcon.deauthenticate()
```
### queryCombinedSensorUpdateBuilds
Retrieve available builds for use with Sensor Update Policies

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __platform__ | query | _string_ | The platform to return builds for |
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
    'platform': 'string'
}

response = falcon.command('queryCombinedSensorUpdateBuilds', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### queryCombinedSensorUpdatePolicyMembers
Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __id__ | query | _string_ | The ID of the Sensor Update Policy to search for members of |
| | __filter__ | query | _string_ | The filter expression that should be used to limit the results |
| | __offset__ | query | _integer_ | The offset to start retrieving records from |
| | __limit__ | query | _integer_ | The maximum records to return. [1-5000] |
| | __sort__ | query | _string_ | The property to sort by |
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
    'id': 'string',
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('queryCombinedSensorUpdatePolicyMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### queryCombinedSensorUpdatePolicies
Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria

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

response = falcon.command('queryCombinedSensorUpdatePolicies', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### queryCombinedSensorUpdatePoliciesV2
Search for Sensor Update Policies with additional support for uninstall protection in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria

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

response = falcon.command('queryCombinedSensorUpdatePoliciesV2', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### performSensorUpdatePoliciesAction
Perform the specified action on the Sensor Update Policies specified in the request

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __action_name__ | query | _string_ | The action to perform |
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

PARAMS = {
    'action_name': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.command('performSensorUpdatePoliciesAction', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```
### setSensorUpdatePoliciesPrecedence
Sets the precedence of Sensor Update Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence

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

response = falcon.command('setSensorUpdatePoliciesPrecedence', body=BODY)
print(response)
falcon.deauthenticate()
```
### getSensorUpdatePolicies
Retrieve a set of Sensor Update Policies by specifying their IDs

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the Sensor Update Policies to return |
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

response = falcon.command('getSensorUpdatePolicies', ids=IDS)
print(response)
falcon.deauthenticate()
```
### createSensorUpdatePolicies
Create Sensor Update Policies by specifying details about the policy to create

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

response = falcon.command('createSensorUpdatePolicies', body=BODY)
print(response)
falcon.deauthenticate()
```
### deleteSensorUpdatePolicies
Delete a set of Sensor Update Policies by specifying their IDs

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the Sensor Update Policies to delete |
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

response = falcon.command('deleteSensorUpdatePolicies', ids=IDS)
print(response)
falcon.deauthenticate()
```
### updateSensorUpdatePolicies
Update Sensor Update Policies by specifying the ID of the policy and details to update

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

response = falcon.command('updateSensorUpdatePolicies', body=BODY)
print(response)
falcon.deauthenticate()
```
### getSensorUpdatePoliciesV2
Retrieve a set of Sensor Update Policies with additional support for uninstall protection by specifying their IDs

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the Sensor Update Policies to return |
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

response = falcon.command('getSensorUpdatePoliciesV2', ids=IDS)
print(response)
falcon.deauthenticate()
```
### createSensorUpdatePoliciesV2
Create Sensor Update Policies by specifying details about the policy to create with additional support for uninstall protection

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

response = falcon.command('createSensorUpdatePoliciesV2', body=BODY)
print(response)
falcon.deauthenticate()
```
### updateSensorUpdatePoliciesV2
Update Sensor Update Policies by specifying the ID of the policy and details to update with additional support for uninstall protection

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

response = falcon.command('updateSensorUpdatePoliciesV2', body=BODY)
print(response)
falcon.deauthenticate()
```
### querySensorUpdatePolicyMembers
Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __id__ | query | _string_ | The ID of the Sensor Update Policy to search for members of |
| | __filter__ | query | _string_ | The filter expression that should be used to limit the results |
| | __offset__ | query | _integer_ | The offset to start retrieving records from |
| | __limit__ | query | _integer_ | The maximum records to return. [1-5000] |
| | __sort__ | query | _string_ | The property to sort by |
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
    'id': 'string',
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('querySensorUpdatePolicyMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### querySensorUpdatePolicies
Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policy IDs which match the filter criteria

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

response = falcon.command('querySensorUpdatePolicies', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
