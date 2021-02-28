# Using the CSPM Registration service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-X%20No-red.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [GetCSPMAwsAccount](#getcspmawsaccount) | Returns information about the current status of an AWS account. |
| [CreateCSPMAwsAccount](#createcspmawsaccount) | Creates a new account in our system for a customer and generates a script for them to run in their AWS cloud environment to grant us access. |
| [DeleteCSPMAwsAccount](#deletecspmawsaccount) | Deletes an existing AWS account or organization in our system. |
| [GetCSPMAwsConsoleSetupURLs](#getcspmawsconsolesetupurls) | Return a URL for customer to visit in their cloud environment to grant us access to their AWS environment. |
| [GetCSPMAwsAccountScriptsAttachment](#getcspmawsaccountscriptsattachment) | Return a script for customer to run in their cloud environment to grant us access to their AWS environment as a downloadable attachment. |
| [GetCSPMAzureAccount](#getcspmazureaccount) | Return information about Azure account registration |
| [CreateCSPMAzureAccount](#createcspmazureaccount) | Creates a new account in our system for a customer and generates a script for them to run in their cloud environment to grant us access. |
| [DeleteCSPMAzureAccount](#deletecspmazureaccount) | Deletes an Azure subscription from the system. |
| [UpdateCSPMAzureAccountClientID](#updatecspmazureaccountclientid) | Update an Azure service account in our system by with the user-created client_id created with the public key we've provided |
| [GetCSPMAzureUserScriptsAttachment](#getcspmazureuserscriptsattachment) | Return a script for customer to run in their cloud environment to grant us access to their Azure environment as a downloadable attachment |
| [GetCSPMPolicy](#getcspmpolicy) | Given a policy ID, returns detailed policy information. |
| [GetCSPMPolicySettings](#getcspmpolicysettings) | Returns information about current policy settings. |
| [UpdateCSPMPolicySettings](#updatecspmpolicysettings) | Updates a policy setting - can be used to override policy severity or to disable a policy entirely. |
| [GetCSPMScanSchedule](#getcspmscanschedule) | Returns scan schedule configuration for one or more cloud platforms. |
| [UpdateCSPMScanSchedule](#updatecspmscanschedule) | Updates scan schedule configuration for one or more cloud platforms. |
### GetCSPMAwsAccount
Returns information about the current status of an AWS account.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __scan-type__ | query | _string_ | Type of scan, dry or full, to perform on selected accounts |
| | __ids__ | query | array (_string_) | AWS account IDs |
| | __organization-ids__ | query | array (_string_) | AWS organization IDs |
| | __status__ | query | _string_ | Account status to filter results by. |
| | __limit__ | query | _integer_ | The maximum records to return. Defaults to 100. |
| | __offset__ | query | _integer_ | The offset to start retrieving records from |
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
    'scan-type': 'string',
    'organization-ids': [
       'string',
       'string'
    ],
    'status': 'string',
    'limit': integer,
    'offset': integer
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('GetCSPMAwsAccount', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### CreateCSPMAwsAccount
Creates a new account in our system for a customer and generates a script for them to run in their AWS cloud environment to grant us access.

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

response = falcon.command('CreateCSPMAwsAccount', body=BODY)
print(response)
falcon.deauthenticate()
```
### DeleteCSPMAwsAccount
Deletes an existing AWS account or organization in our system.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __ids__ | query | array (_string_) | AWS account IDs to remove |
| | __organization-ids__ | query | array (_string_) | AWS organization IDs to remove |
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
    'organization-ids': [
       'string',
       'string'
    ]
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('DeleteCSPMAwsAccount', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### GetCSPMAwsConsoleSetupURLs
Return a URL for customer to visit in their cloud environment to grant us access to their AWS environment.

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

response = falcon.command('GetCSPMAwsConsoleSetupURLs')
print(response)
falcon.deauthenticate()
```
### GetCSPMAwsAccountScriptsAttachment
Return a script for customer to run in their cloud environment to grant us access to their AWS environment as a downloadable attachment.

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

response = falcon.command('GetCSPMAwsAccountScriptsAttachment')
print(response)
falcon.deauthenticate()
```
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
| | __status__ | query | _string_ | Account status to filter results by. |
| | __limit__ | query | _integer_ | The maximum records to return. Defaults to 100. |
| | __offset__ | query | _integer_ | The offset to start retrieving records from |
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
    'scan-type': 'string',
    'status': 'string',
    'limit': integer,
    'offset': integer
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
### DeleteCSPMAzureAccount
Deletes an Azure subscription from the system.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | Azure subscription IDs to remove |
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

response = falcon.command('DeleteCSPMAzureAccount', ids=IDS)
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
| | __tenant-id__ | query | _string_ | Tenant ID to update client ID for. Required if multiple tenants are registered. |
| :white_check_mark: | __body__ | body | _string_ | This is a placeholder only. Please ignore this field. |
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
    'tenant-id': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.command('UpdateCSPMAzureAccountClientID', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```
### GetCSPMAzureUserScriptsAttachment
Return a script for customer to run in their cloud environment to grant us access to their Azure environment as a downloadable attachment

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __tenant-id__ | query | _string_ | Tenant ID to generate script for. Defaults to most recently registered tenant. |
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
    'tenant-id': 'string'
}

response = falcon.command('GetCSPMAzureUserScriptsAttachment', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### GetCSPMPolicy
Given a policy ID, returns detailed policy information.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | _string_ | Policy ID |
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

response = falcon.command('GetCSPMPolicy', ids=IDS)
print(response)
falcon.deauthenticate()
```
### GetCSPMPolicySettings
Returns information about current policy settings.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __service__ | query | _string_ | Service type to filter policy settings by. |
| | __policy-id__ | query | _string_ | Policy ID |
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
    'service': 'string',
    'policy-id': 'string'
}

response = falcon.command('GetCSPMPolicySettings', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### UpdateCSPMPolicySettings
Updates a policy setting - can be used to override policy severity or to disable a policy entirely.

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

response = falcon.command('UpdateCSPMPolicySettings', body=BODY)
print(response)
falcon.deauthenticate()
```
### GetCSPMScanSchedule
Returns scan schedule configuration for one or more cloud platforms.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __cloud-platform__ | query | array (_string_) | Cloud Platform |
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
    'cloud-platform': [
       'string',
       'string'
    ]
}

response = falcon.command('GetCSPMScanSchedule', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### UpdateCSPMScanSchedule
Updates scan schedule configuration for one or more cloud platforms.

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

response = falcon.command('UpdateCSPMScanSchedule', body=BODY)
print(response)
falcon.deauthenticate()
```
