# Using the D4C Registration service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-X%20No-red.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [GetCSPMAzureAccount](#getcspmazureaccount) | Return information about Azure account registration |
| [CreateCSPMAzureAccount](#createcspmazureaccount) | Creates a new account in our system for a customer and generates a script for them to run in their cloud environment to grant us access. |
| [UpdateCSPMAzureAccountClientID](#updatecspmazureaccountclientid) | Update an Azure service account in our system by with the user-created client_id created with the public key we've provided |
| [GetCSPMAzureUserScriptsAttachment](#getcspmazureuserscriptsattachment) | Return a script for customer to run in their cloud environment to grant us access to their Azure environment as a downloadable attachment |
| [GetCSPMAzureUserScripts](#getcspmazureuserscripts) | Return a script for customer to run in their cloud environment to grant us access to their Azure environment |
| [GetCSPMCGPAccount](#getcspmcgpaccount) | Returns information about the current status of an GCP account. |
| [CreateCSPMGCPAccount](#createcspmgcpaccount) | Creates a new account in our system for a customer and generates a new service account for them to add access to in their GCP environment to grant us access. |
| [GetCSPMGCPUserScriptsAttachment](#getcspmgcpuserscriptsattachment) | Return a script for customer to run in their cloud environment to grant us access to their GCP environment as a downloadable attachment |
| [GetCSPMGCPUserScripts](#getcspmgcpuserscripts) | Return a script for customer to run in their cloud environment to grant us access to their GCP environment |
### GetCSPMAzureAccount
Return information about Azure account registration

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __ids__ | query | array (_string_) | SubscriptionIDs of accounts to select for this status operation. If this is empty then all accounts are returned. |
| | __scan-type__ | query | _string_ | Type of scan, dry or full, to perform on selected accounts |
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
    'scan-type': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('GetCSPMAzureAccount', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### CreateCSPMAzureAccount
Creates a new account in our system for a customer and generates a script for them to run in their cloud environment to grant us access.

#### Content-Type
- Consumes: _application/json_
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

response = falcon.command('CreateCSPMAzureAccount', body=BODY)
print(response)
falcon.deauthenticate()
```
### UpdateCSPMAzureAccountClientID
Update an Azure service account in our system by with the user-created client_id created with the public key we've provided

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __id__ | query | _string_ | ClientID to use for the Service Principal associated with the customer's Azure account |
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
    'id': 'string'
}

response = falcon.command('UpdateCSPMAzureAccountClientID', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### GetCSPMAzureUserScriptsAttachment
Return a script for customer to run in their cloud environment to grant us access to their Azure environment as a downloadable attachment

#### Content-Type
- Produces: _application/json_
#### Parameters
No parameters
#### Usage
##### Uber class example
```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

response = falcon.command('GetCSPMAzureUserScriptsAttachment')
print(response)
falcon.deauthenticate()
```
### GetCSPMAzureUserScripts
Return a script for customer to run in their cloud environment to grant us access to their Azure environment

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
No parameters
#### Usage
##### Uber class example
```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

response = falcon.command('GetCSPMAzureUserScripts')
print(response)
falcon.deauthenticate()
```
### GetCSPMCGPAccount
Returns information about the current status of an GCP account.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __scan-type__ | query | _string_ | Type of scan, dry or full, to perform on selected accounts |
| | __ids__ | query | array (_string_) | Parent IDs of accounts |
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
    'scan-type': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('GetCSPMCGPAccount', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### CreateCSPMGCPAccount
Creates a new account in our system for a customer and generates a new service account for them to add access to in their GCP environment to grant us access.

#### Content-Type
- Consumes: _application/json_
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

response = falcon.command('CreateCSPMGCPAccount', body=BODY)
print(response)
falcon.deauthenticate()
```
### GetCSPMGCPUserScriptsAttachment
Return a script for customer to run in their cloud environment to grant us access to their GCP environment as a downloadable attachment

#### Content-Type
- Produces: _application/json_
#### Parameters
No parameters
#### Usage
##### Uber class example
```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

response = falcon.command('GetCSPMGCPUserScriptsAttachment')
print(response)
falcon.deauthenticate()
```
### GetCSPMGCPUserScripts
Return a script for customer to run in their cloud environment to grant us access to their GCP environment

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
No parameters
#### Usage
##### Uber class example
```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

response = falcon.command('GetCSPMGCPUserScripts')
print(response)
falcon.deauthenticate()
```
