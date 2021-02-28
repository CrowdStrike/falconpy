# Using the Intel service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [QueryIntelActorEntities](#queryintelactorentities) | Get info about actors that match provided FQL filters. |
| [QueryIntelIndicatorEntities](#queryintelindicatorentities) | Get info about indicators that match provided FQL filters. |
| [QueryIntelReportEntities](#queryintelreportentities) | Get info about reports that match provided FQL filters. |
| [GetIntelActorEntities](#getintelactorentities) | Retrieve specific actors using their actor IDs. |
| [GetIntelIndicatorEntities](#getintelindicatorentities) | Retrieve specific indicators using their indicator IDs. |
| [GetIntelReportPDF](#getintelreportpdf) | Return a Report PDF attachment |
| [GetIntelReportEntities](#getintelreportentities) | Retrieve specific reports using their report IDs. |
| [GetIntelRuleFile](#getintelrulefile) | Download earlier rule sets. |
| [GetLatestIntelRuleFile](#getlatestintelrulefile) | Download the latest rule set. |
| [GetIntelRuleEntities](#getintelruleentities) | Retrieve details for rule sets for the specified ids. |
| [QueryIntelActorIds](#queryintelactorids) | Get actor IDs that match provided FQL filters. |
| [QueryIntelIndicatorIds](#queryintelindicatorids) | Get indicators IDs that match provided FQL filters. |
| [QueryIntelReportIds](#queryintelreportids) | Get report IDs that match provided FQL filters. |
| [QueryIntelRuleIds](#queryintelruleids) | Search for rule IDs that match provided filter criteria. |
### QueryIntelActorEntities
Get info about actors that match provided FQL filters.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _integer_ | Set the starting row number to return actors from. Defaults to 0. |
| | __limit__ | query | _integer_ | Set the number of actors to return. The value must be between 1 and 5000. |
| | __sort__ | query | _string_ | Order fields in ascending or descending order.  Ex: created_date|asc. |
| | __filter__ | query | _string_ | Filter your query by specifying FQL filter parameters. Filter parameters include:  actors, actors.id, actors.name, actors.slug, actors.url, created_date, description, id, last_modified_date, motivations, motivations.id, motivations.slug, motivations.value, name, name.raw, short_description, slug, sub_type, sub_type.id, sub_type.name, sub_type.slug, tags, tags.id, tags.slug, tags.value, target_countries, target_countries.id, target_countries.slug, target_countries.value, target_industries, target_industries.id, target_industries.slug, target_industries.value, type, type.id, type.name, type.slug, url. |
| | __q__ | query | _string_ | Perform a generic substring search across all fields. |
| | __fields__ | query | array (_string_) | The fields to return, or a predefined set of fields in the form of the collection name surrounded by two underscores like:  __<collection>__.  Ex: slug __full__.  Defaults to __basic__. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    PARAMS = {
        'offset': integer,
        'limit': integer,
        'sort': 'string',
        'filter': 'string',
        'q': 'string',
        'fields':     [
           'string',
           'string'
    ]
    }

    response = falcon.QueryIntelActorEntities(parameters=PARAMS)
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
    'filter': 'string',
    'q': 'string',
    'fields': [
       'string',
       'string'
    ]
}

response = falcon.command('QueryIntelActorEntities', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### QueryIntelIndicatorEntities
Get info about indicators that match provided FQL filters.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _integer_ | Set the starting row number to return indicators from. Defaults to 0. |
| | __limit__ | query | _integer_ | Set the number of indicators to return. The number must be between 1 and 50000 |
| | __sort__ | query | _string_ | Order fields in ascending or descending order.  Ex: published_date|asc. |
| | __filter__ | query | _string_ | Filter your query by specifying FQL filter parameters. Filter parameters include:  _marker, actors, deleted, domain_types, id, indicator, ip_address_types, kill_chains, labels, labels.created_on, labels.last_valid_on, labels.name, last_updated, malicious_confidence, malware_families, published_date, reports, targets, threat_types, type, vulnerabilities. |
| | __q__ | query | _string_ | Perform a generic substring search across all fields. |
| | __include_deleted__ | query | _boolean_ | If true, include both published and deleted indicators in the response. Defaults to false. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    PARAMS = {
        'offset': integer,
        'limit': integer,
        'sort': 'string',
        'filter': 'string',
        'q': 'string',
        'include_deleted': boolean
    }

    response = falcon.QueryIntelIndicatorEntities(parameters=PARAMS)
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
    'filter': 'string',
    'q': 'string',
    'include_deleted': boolean
}

response = falcon.command('QueryIntelIndicatorEntities', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### QueryIntelReportEntities
Get info about reports that match provided FQL filters.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _integer_ | Set the starting row number to return reports from. Defaults to 0. |
| | __limit__ | query | _integer_ | Set the number of reports to return. The value must be between 1 and 5000. |
| | __sort__ | query | _string_ | Order fields in ascending or descending order. Ex: created_date|asc. |
| | __filter__ | query | _string_ | Filter your query by specifying FQL filter parameters. Filter parameters include:  actors, actors.id, actors.name, actors.slug, actors.url, created_date, description, id, last_modified_date, motivations, motivations.id, motivations.slug, motivations.value, name, name.raw, short_description, slug, sub_type, sub_type.id, sub_type.name, sub_type.slug, tags, tags.id, tags.slug, tags.value, target_countries, target_countries.id, target_countries.slug, target_countries.value, target_industries, target_industries.id, target_industries.slug, target_industries.value, type, type.id, type.name, type.slug, url. |
| | __q__ | query | _string_ | Perform a generic substring search across all fields. |
| | __fields__ | query | array (_string_) | The fields to return, or a predefined set of fields in the form of the collection name surrounded by two underscores like:  __<collection>__.  Ex: slug __full__.  Defaults to __basic__. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    PARAMS = {
        'offset': integer,
        'limit': integer,
        'sort': 'string',
        'filter': 'string',
        'q': 'string',
        'fields':     [
           'string',
           'string'
    ]
    }

    response = falcon.QueryIntelReportEntities(parameters=PARAMS)
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
    'filter': 'string',
    'q': 'string',
    'fields': [
       'string',
       'string'
    ]
}

response = falcon.command('QueryIntelReportEntities', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### GetIntelActorEntities
Retrieve specific actors using their actor IDs.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the actors you want to retrieve. |
| | __fields__ | query | array (_string_) | The fields to return, or a predefined set of fields in the form of the collection name surrounded by two underscores like:  __<collection>__.  Ex: slug __full__.  Defaults to __basic__. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    PARAMS = {
        'fields':     [
           'string',
           'string'
    ]
    }

    IDS = 'ID1,ID2,ID3'

    response = falcon.GetIntelActorEntities(parameters=PARAMS, ids=IDS)
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
    'fields': [
       'string',
       'string'
    ]
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('GetIntelActorEntities', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### GetIntelIndicatorEntities
Retrieve specific indicators using their indicator IDs.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.GetIntelIndicatorEntities(body=BODY)
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

response = falcon.command('GetIntelIndicatorEntities', body=BODY)
print(response)
falcon.deauthenticate()
```
### GetIntelReportPDF
Return a Report PDF attachment

#### Content-Type
- Produces: _application/octet-stream_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __id__ | query | _string_ | The ID of the report you want to download as a PDF. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    PARAMS = {
        'id': 'string'
    }

    response = falcon.GetIntelReportPDF(parameters=PARAMS)
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
    'id': 'string'
}

response = falcon.command('GetIntelReportPDF', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### GetIntelReportEntities
Retrieve specific reports using their report IDs.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the reports you want to retrieve. |
| | __fields__ | query | array (_string_) | The fields to return, or a predefined set of fields in the form of the collection name surrounded by two underscores like:  __<collection>__.  Ex: slug __full__.  Defaults to __basic__. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    PARAMS = {
        'fields':     [
           'string',
           'string'
    ]
    }

    IDS = 'ID1,ID2,ID3'

    response = falcon.GetIntelReportEntities(parameters=PARAMS, ids=IDS)
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
    'fields': [
       'string',
       'string'
    ]
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('GetIntelReportEntities', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### GetIntelRuleFile
Download earlier rule sets.

#### Content-Type
- Produces: _application/zip_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __Accept__ | header | _string_ | Choose the format you want the rule set in. |
| :white_check_mark: | __id__ | query | _integer_ | The ID of the rule set. |
| | __format__ | query | _string_ | Choose the format you want the rule set in. Valid formats are zip and gzip. Defaults to zip. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    PARAMS = {
        'id': integer,
        'format': 'string'
    }

    HEADERS = {
        'Accept': 'string'
    }

    response = falcon.GetIntelRuleFile(parameters=PARAMS, headers=HEADERS)
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
    'id': integer,
    'format': 'string'
}

HEADERS = {
    'Accept': 'string'
}

response = falcon.command('GetIntelRuleFile', parameters=PARAMS, headers=HEADERS)
print(response)
falcon.deauthenticate()
```
### GetLatestIntelRuleFile
Download the latest rule set.

#### Content-Type
- Produces: _application/zip_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __Accept__ | header | _string_ | Choose the format you want the rule set in. |
| :white_check_mark: | __type__ | query | _string_ | The rule news report type. Accepted values:  snort-suricata-master  snort-suricata-update  snort-suricata-changelog  yara-master  yara-update  yara-changelog  common-event-format  netwitness |
| | __format__ | query | _string_ | Choose the format you want the rule set in. Valid formats are zip and gzip. Defaults to zip. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    PARAMS = {
        'type': 'string',
        'format': 'string'
    }

    HEADERS = {
        'Accept': 'string'
    }

    response = falcon.GetLatestIntelRuleFile(parameters=PARAMS, headers=HEADERS)
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
    'type': 'string',
    'format': 'string'
}

HEADERS = {
    'Accept': 'string'
}

response = falcon.command('GetLatestIntelRuleFile', parameters=PARAMS, headers=HEADERS)
print(response)
falcon.deauthenticate()
```
### GetIntelRuleEntities
Retrieve details for rule sets for the specified ids.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The ids of rules to return. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.GetIntelRuleEntities(ids=IDS)
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

response = falcon.command('GetIntelRuleEntities', ids=IDS)
print(response)
falcon.deauthenticate()
```
### QueryIntelActorIds
Get actor IDs that match provided FQL filters.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _integer_ | Set the starting row number to return actors IDs from. Defaults to 0. |
| | __limit__ | query | _integer_ | Set the number of actor IDs to return. The value must be between 1 and 5000. |
| | __sort__ | query | _string_ | Order fields in ascending or descending order.  Ex: created_date|asc. |
| | __filter__ | query | _string_ | Filter your query by specifying FQL filter parameters. Filter parameters include:  actors, actors.id, actors.name, actors.slug, actors.url, created_date, description, id, last_modified_date, motivations, motivations.id, motivations.slug, motivations.value, name, name.raw, short_description, slug, sub_type, sub_type.id, sub_type.name, sub_type.slug, tags, tags.id, tags.slug, tags.value, target_countries, target_countries.id, target_countries.slug, target_countries.value, target_industries, target_industries.id, target_industries.slug, target_industries.value, type, type.id, type.name, type.slug, url. |
| | __q__ | query | _string_ | Perform a generic substring search across all fields. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    PARAMS = {
        'offset': integer,
        'limit': integer,
        'sort': 'string',
        'filter': 'string',
        'q': 'string'
    }

    response = falcon.QueryIntelActorIds(parameters=PARAMS)
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
    'filter': 'string',
    'q': 'string'
}

response = falcon.command('QueryIntelActorIds', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### QueryIntelIndicatorIds
Get indicators IDs that match provided FQL filters.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _integer_ | Set the starting row number to return indicator IDs from. Defaults to 0. |
| | __limit__ | query | _integer_ | Set the number of indicator IDs to return. The number must be between 1 and 50000 |
| | __sort__ | query | _string_ | Order fields in ascending or descending order.  Ex: published_date|asc. |
| | __filter__ | query | _string_ | Filter your query by specifying FQL filter parameters. Filter parameters include:  _marker, actors, deleted, domain_types, id, indicator, ip_address_types, kill_chains, labels, labels.created_on, labels.last_valid_on, labels.name, last_updated, malicious_confidence, malware_families, published_date, reports, targets, threat_types, type, vulnerabilities. |
| | __q__ | query | _string_ | Perform a generic substring search across all fields. |
| | __include_deleted__ | query | _boolean_ | If true, include both published and deleted indicators in the response. Defaults to false. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    PARAMS = {
        'offset': integer,
        'limit': integer,
        'sort': 'string',
        'filter': 'string',
        'q': 'string',
        'include_deleted': boolean
    }

    response = falcon.QueryIntelIndicatorIds(parameters=PARAMS)
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
    'filter': 'string',
    'q': 'string',
    'include_deleted': boolean
}

response = falcon.command('QueryIntelIndicatorIds', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### QueryIntelReportIds
Get report IDs that match provided FQL filters.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _integer_ | Set the starting row number to return report IDs from. Defaults to 0. |
| | __limit__ | query | _integer_ | Set the number of report IDs to return. The value must be between 1 and 5000. |
| | __sort__ | query | _string_ | Order fields in ascending or descending order.  Ex: created_date|asc. |
| | __filter__ | query | _string_ | Filter your query by specifying FQL filter parameters. Filter parameters include:  actors, actors.id, actors.name, actors.slug, actors.url, created_date, description, id, last_modified_date, motivations, motivations.id, motivations.slug, motivations.value, name, name.raw, short_description, slug, sub_type, sub_type.id, sub_type.name, sub_type.slug, tags, tags.id, tags.slug, tags.value, target_countries, target_countries.id, target_countries.slug, target_countries.value, target_industries, target_industries.id, target_industries.slug, target_industries.value, type, type.id, type.name, type.slug, url. |
| | __q__ | query | _string_ | Perform a generic substring search across all fields. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    PARAMS = {
        'offset': integer,
        'limit': integer,
        'sort': 'string',
        'filter': 'string',
        'q': 'string'
    }

    response = falcon.QueryIntelReportIds(parameters=PARAMS)
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
    'filter': 'string',
    'q': 'string'
}

response = falcon.command('QueryIntelReportIds', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### QueryIntelRuleIds
Search for rule IDs that match provided filter criteria.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _integer_ | Set the starting row number to return reports from. Defaults to 0. |
| | __limit__ | query | _integer_ | The number of rule IDs to return. Defaults to 10. |
| | __sort__ | query | _string_ | Order fields in ascending or descending order.  Ex: created_date|asc. |
| | __name__ | query | array (_string_) | Search by rule title. |
| :white_check_mark: | __type__ | query | _string_ | The rule news report type. Accepted values:  snort-suricata-master  snort-suricata-update  snort-suricata-changelog  yara-master  yara-update  yara-changelog  common-event-format  netwitness |
| | __description__ | query | array (_string_) | Substring match on description field. |
| | __tags__ | query | array (_string_) | Search for rule tags. |
| | __min_created_date__ | query | _integer_ | Filter results to those created on or after a certain date. |
| | __max_created_date__ | query | _string_ | Filter results to those created on or before a certain date. |
| | __q__ | query | _string_ | Perform a generic substring search across all fields. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import intel as FalconIntel

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconIntel.Intel(access_token=token)

    PARAMS = {
        'offset': integer,
        'limit': integer,
        'sort': 'string',
        'name':     [
           'string',
           'string'
    ],
        'type': 'string',
        'description':     [
           'string',
           'string'
    ],
        'tags':     [
           'string',
           'string'
    ],
        'min_created_date': integer,
        'max_created_date': 'string',
        'q': 'string'
    }

    response = falcon.QueryIntelRuleIds(parameters=PARAMS)
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
    'name': [
       'string',
       'string'
    ],
    'type': 'string',
    'description': [
       'string',
       'string'
    ],
    'tags': [
       'string',
       'string'
    ],
    'min_created_date': integer,
    'max_created_date': 'string',
    'q': 'string'
}

response = falcon.command('QueryIntelRuleIds', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
