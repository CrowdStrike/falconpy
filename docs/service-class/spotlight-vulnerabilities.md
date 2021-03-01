# Using the Spotlight Vulnerabilities service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [getVulnerabilities](#getvulnerabilities) | Get details on vulnerabilities by providing one or more IDs |
| [queryVulnerabilities](#queryvulnerabilities) | Search for Vulnerabilities in your environment by providing an FQL filter and paging details. Returns a set of Vulnerability IDs which match the filter criteria |
### getVulnerabilities
Get details on vulnerabilities by providing one or more IDs

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | One or more vulnerability IDs (max: 400). Find vulnerability IDs with GET /spotlight/queries/vulnerabilities/v1 |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import spotlight_vulnerabilities as FalconSV

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconSV.Sensor_Vulnerabilities(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.getVulnerabilities(ids=IDS)
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

response = falcon.command('getVulnerabilities', ids=IDS)
print(response)
falcon.deauthenticate()
```
### queryVulnerabilities
Search for Vulnerabilities in your environment by providing an FQL filter and paging details. Returns a set of Vulnerability IDs which match the filter criteria

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __after__ | query | _string_ | A pagination token used with the `limit` parameter to manage pagination of results. On your first request, don't provide an `after` token. On subsequent requests, provide the `after` token from the previous response to continue from that place in the results. |
| | __limit__ | query | _integer_ | The number of items to return in this response (default: 100, max: 400). Use with the after parameter to manage pagination of results. |
| | __sort__ | query | _string_ | Sort vulnerabilities by their properties. Common sort options include:  <ul><li>created_timestamp|desc</li><li>closed_timestamp|asc</li></ul> |
| :white_check_mark: | __filter__ | query | _string_ | Filter items using a query in Falcon Query Language (FQL). Wildcards * are unsupported.   Common filter options include:  <ul><li>created_timestamp:>'2019-11-25T22:36:12Z'</li><li>closed_timestamp:>'2019-11-25T22:36:12Z'</li><li>aid:'8e7656b27d8c49a34a1af416424d6231'</li></ul> |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import spotlight_vulnerabilities as FalconSV

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconSV.Sensor_Vulnerabilities(access_token=token)

    PARAMS = {
        'after': 'string',
        'limit': integer,
        'sort': 'string',
        'filter': 'string'
    }

    response = falcon.queryVulnerabilities(parameters=PARAMS)
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
    'after': 'string',
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.command('queryVulnerabilities', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
