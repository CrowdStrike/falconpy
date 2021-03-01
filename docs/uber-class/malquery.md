# Using the Malquery service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-X%20No-red.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [GetMalQueryQuotasV1](#getmalqueryquotasv1) | Get information about search and download quotas in your environment |
| [PostMalQueryFuzzySearchV1](#postmalqueryfuzzysearchv1) | Search Falcon MalQuery quickly, but with more potential for false positives. Search for a combination of hex patterns and strings in order to identify samples based upon file content at byte level granularity. |
| [GetMalQueryDownloadV1](#getmalquerydownloadv1) | Download a file indexed by MalQuery. Specify the file using its SHA256. Only one file is supported at this time |
| [GetMalQueryMetadataV1](#getmalquerymetadatav1) | Retrieve indexed files metadata by their hash |
| [GetMalQueryRequestV1](#getmalqueryrequestv1) | Check the status and results of an asynchronous request, such as hunt or exact-search. Supports a single request id at this time. |
| [GetMalQueryEntitiesSamplesFetchV1](#getmalqueryentitiessamplesfetchv1) | Fetch a zip archive with password 'infected' containing the samples. Call this once the /entities/samples-multidownload request has finished processing |
| [PostMalQueryEntitiesSamplesMultidownloadV1](#postmalqueryentitiessamplesmultidownloadv1) | Schedule samples for download. Use the result id with the /request endpoint to check if the download is ready after which you can call the /entities/samples-fetch to get the zip |
| [PostMalQueryExactSearchV1](#postmalqueryexactsearchv1) | Search Falcon MalQuery for a combination of hex patterns and strings in order to identify samples based upon file content at byte level granularity. You can filter results on criteria such as file type, file size and first seen date. Returns a request id which can be used with the /request endpoint |
| [PostMalQueryHuntV1](#postmalqueryhuntv1) | Schedule a YARA-based search for execution. Returns a request id which can be used with the /request endpoint |
### GetMalQueryQuotasV1
Get information about search and download quotas in your environment

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

response = falcon.command('GetMalQueryQuotasV1')
print(response)
falcon.deauthenticate()
```
### PostMalQueryFuzzySearchV1
Search Falcon MalQuery quickly, but with more potential for false positives. Search for a combination of hex patterns and strings in order to identify samples based upon file content at byte level granularity.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Fuzzy search parameters. See model for more details. |
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

response = falcon.command('PostMalQueryFuzzySearchV1', body=BODY)
print(response)
falcon.deauthenticate()
```
### GetMalQueryDownloadV1
Download a file indexed by MalQuery. Specify the file using its SHA256. Only one file is supported at this time

#### Content-Type
- Produces: _application/octet-stream_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The file SHA256. |
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

response = falcon.command('GetMalQueryDownloadV1', ids=IDS)
print(response)
falcon.deauthenticate()
```
### GetMalQueryMetadataV1
Retrieve indexed files metadata by their hash

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The file SHA256. |
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

response = falcon.command('GetMalQueryMetadataV1', ids=IDS)
print(response)
falcon.deauthenticate()
```
### GetMalQueryRequestV1
Check the status and results of an asynchronous request, such as hunt or exact-search. Supports a single request id at this time.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | Identifier of a MalQuery request |
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

response = falcon.command('GetMalQueryRequestV1', ids=IDS)
print(response)
falcon.deauthenticate()
```
### GetMalQueryEntitiesSamplesFetchV1
Fetch a zip archive with password 'infected' containing the samples. Call this once the /entities/samples-multidownload request has finished processing

#### Content-Type
- Produces: _application/zip_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | _string_ | Multidownload job id |
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

response = falcon.command('GetMalQueryEntitiesSamplesFetchV1', ids=IDS)
print(response)
falcon.deauthenticate()
```
### PostMalQueryEntitiesSamplesMultidownloadV1
Schedule samples for download. Use the result id with the /request endpoint to check if the download is ready after which you can call the /entities/samples-fetch to get the zip

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Download request. See model for more details. |
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

response = falcon.command('PostMalQueryEntitiesSamplesMultidownloadV1', body=BODY)
print(response)
falcon.deauthenticate()
```
### PostMalQueryExactSearchV1
Search Falcon MalQuery for a combination of hex patterns and strings in order to identify samples based upon file content at byte level granularity. You can filter results on criteria such as file type, file size and first seen date. Returns a request id which can be used with the /request endpoint

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Exact search parameters. See model for more details. |
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

response = falcon.command('PostMalQueryExactSearchV1', body=BODY)
print(response)
falcon.deauthenticate()
```
### PostMalQueryHuntV1
Schedule a YARA-based search for execution. Returns a request id which can be used with the /request endpoint

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Hunt parameters. See model for more details. |
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

response = falcon.command('PostMalQueryHuntV1', body=BODY)
print(response)
falcon.deauthenticate()
```
