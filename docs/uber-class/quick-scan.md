# Using the Quick Scan service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-X%20No-red.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [GetScansAggregates](#getscansaggregates) | Get scans aggregations as specified via json in request body. |
| [GetScans](#getscans) | Check the status of a volume scan. Time required for analysis increases with the number of samples in a volume but usually it should take less than 1 minute |
| [ScanSamples](#scansamples) | Submit a volume of files for ml scanning. Time required for analysis increases with the number of samples in a volume but usually it should take less than 1 minute |
| [QuerySubmissionsMixin0](#querysubmissionsmixin0) | Find IDs for submitted scans by providing an FQL filter and paging details. Returns a set of volume IDs that match your criteria. |
### GetScansAggregates
Get scans aggregations as specified via json in request body.

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

response = falcon.command('GetScansAggregates', body=BODY)
print(response)
falcon.deauthenticate()
```
### GetScans
Check the status of a volume scan. Time required for analysis increases with the number of samples in a volume but usually it should take less than 1 minute

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | ID of a submitted scan |
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

response = falcon.command('GetScans', ids=IDS)
print(response)
falcon.deauthenticate()
```
### ScanSamples
Submit a volume of files for ml scanning. Time required for analysis increases with the number of samples in a volume but usually it should take less than 1 minute

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Submit a batch of SHA256s for ml scanning. The samples must have been previously uploaded through `/samples/entities/samples/v3` |
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

response = falcon.command('ScanSamples', body=BODY)
print(response)
falcon.deauthenticate()
```
### QuerySubmissionsMixin0
Find IDs for submitted scans by providing an FQL filter and paging details. Returns a set of volume IDs that match your criteria.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __filter__ | query | _string_ | Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
| | __offset__ | query | _string_ | The offset to start retrieving submissions from. |
| | __limit__ | query | _integer_ | Maximum number of volume IDs to return. Max: 5000. |
| | __sort__ | query | _string_ | Sort order: `asc` or `desc`. |
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
    'offset': 'string',
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('QuerySubmissionsMixin0', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
