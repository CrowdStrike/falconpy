# Intel

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Intel service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [QueryIntelActorEntities](intel.md#queryintelactorentities) | Get info about actors that match provided FQL filters. |
| [QueryIntelIndicatorEntities](intel.md#queryintelindicatorentities) | Get info about indicators that match provided FQL filters. |
| [QueryIntelReportEntities](intel.md#queryintelreportentities) | Get info about reports that match provided FQL filters. |
| [GetIntelActorEntities](intel.md#getintelactorentities) | Retrieve specific actors using their actor IDs. |
| [GetIntelIndicatorEntities](intel.md#getintelindicatorentities) | Retrieve specific indicators using their indicator IDs. |
| [GetIntelReportPDF](intel.md#getintelreportpdf) | Return a Report PDF attachment |
| [GetIntelReportEntities](intel.md#getintelreportentities) | Retrieve specific reports using their report IDs. |
| [GetIntelRuleFile](intel.md#getintelrulefile) | Download earlier rule sets. |
| [GetLatestIntelRuleFile](intel.md#getlatestintelrulefile) | Download the latest rule set. |
| [GetIntelRuleEntities](intel.md#getintelruleentities) | Retrieve details for rule sets for the specified ids. |
| [QueryIntelActorIds](intel.md#queryintelactorids) | Get actor IDs that match provided FQL filters. |
| [QueryIntelIndicatorIds](intel.md#queryintelindicatorids) | Get indicators IDs that match provided FQL filters. |
| [QueryIntelReportIds](intel.md#queryintelreportids) | Get report IDs that match provided FQL filters. |
| [QueryIntelRuleIds](intel.md#queryintelruleids) | Search for rule IDs that match provided filter criteria. |

### QueryIntelActorEntities

Get info about actors that match provided FQL filters.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |  |
| :---: | :--- | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | Set the starting row number to return actors from. Defaults to 0. |  |
|  | **limit** | query | _integer_ | Set the number of actors to return. The value must be between 1 and 5000. |  |
|  | **sort** | query | _string_ | Order fields in ascending or descending order.  Ex: created\_date | asc. |
|  | **filter** | query | _string_ | Filter your query by specifying FQL filter parameters. Filter parameters include:  actors, actors.id, actors.name, actors.slug, actors.url, created\_date, description, id, last\_modified\_date, motivations, motivations.id, motivations.slug, motivations.value, name, name.raw, short\_description, slug, sub\_type, sub\_type.id, sub\_type.name, sub\_type.slug, tags, tags.id, tags.slug, tags.value, target\_countries, target\_countries.id, target\_countries.slug, target\_countries.value, target\_industries, target\_industries.id, target\_industries.slug, target\_industries.value, type, type.id, type.name, type.slug, url. |  |
|  | **q** | query | _string_ | Perform a generic substring search across all fields. |  |
|  | **fields** | query | array \(_string_\) | The fields to return, or a predefined set of fields in the form of the collection name surrounded by two underscores like:  .  Ex: slug **full**.  Defaults to **basic**. |  |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

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

response = falcon.QueryIntelActorEntities(parameters=PARAMS)
print(response)
```

**Uber class example**

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

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |  |
| :---: | :--- | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | Set the starting row number to return indicators from. Defaults to 0. |  |
|  | **limit** | query | _integer_ | Set the number of indicators to return. The number must be between 1 and 50000 |  |
|  | **sort** | query | _string_ | Order fields in ascending or descending order.  Ex: published\_date | asc. |
|  | **filter** | query | _string_ | Filter your query by specifying FQL filter parameters. Filter parameters include:  \_marker, actors, deleted, domain\_types, id, indicator, ip\_address\_types, kill\_chains, labels, labels.created\_on, labels.last\_valid\_on, labels.name, last\_updated, malicious\_confidence, malware\_families, published\_date, reports, targets, threat\_types, type, vulnerabilities. |  |
|  | **q** | query | _string_ | Perform a generic substring search across all fields. |  |
|  | **include\_deleted** | query | _boolean_ | If true, include both published and deleted indicators in the response. Defaults to false. |  |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

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
```

**Uber class example**

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

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |  |
| :---: | :--- | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | Set the starting row number to return reports from. Defaults to 0. |  |
|  | **limit** | query | _integer_ | Set the number of reports to return. The value must be between 1 and 5000. |  |
|  | **sort** | query | _string_ | Order fields in ascending or descending order. Ex: created\_date | asc. |
|  | **filter** | query | _string_ | Filter your query by specifying FQL filter parameters. Filter parameters include:  actors, actors.id, actors.name, actors.slug, actors.url, created\_date, description, id, last\_modified\_date, motivations, motivations.id, motivations.slug, motivations.value, name, name.raw, short\_description, slug, sub\_type, sub\_type.id, sub\_type.name, sub\_type.slug, tags, tags.id, tags.slug, tags.value, target\_countries, target\_countries.id, target\_countries.slug, target\_countries.value, target\_industries, target\_industries.id, target\_industries.slug, target\_industries.value, type, type.id, type.name, type.slug, url. |  |
|  | **q** | query | _string_ | Perform a generic substring search across all fields. |  |
|  | **fields** | query | array \(_string_\) | The fields to return, or a predefined set of fields in the form of the collection name surrounded by two underscores like:  .  Ex: slug **full**.  Defaults to **basic**. |  |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

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

response = falcon.QueryIntelReportEntities(parameters=PARAMS)
print(response)
```

**Uber class example**

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

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | The IDs of the actors you want to retrieve. |
|  | **fields** | query | array \(_string_\) | The fields to return, or a predefined set of fields in the form of the collection name surrounded by two underscores like:  .  Ex: slug **full**.  Defaults to **basic**. |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'fields': [
       'string',
       'string'
    ]
}

IDS = 'ID1,ID2,ID3'

response = falcon.GetIntelActorEntities(parameters=PARAMS, ids=IDS)
print(response)
```

**Uber class example**

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

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.GetIntelIndicatorEntities(body=BODY)
print(response)
```

**Uber class example**

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

**Content-Type**

* Produces: _application/octet-stream_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **id** | query | _string_ | The ID of the report you want to download as a PDF. |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'id': 'string'
}

response = falcon.GetIntelReportPDF(parameters=PARAMS)
print(response)
```

**Uber class example**

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

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | The IDs of the reports you want to retrieve. |
|  | **fields** | query | array \(_string_\) | The fields to return, or a predefined set of fields in the form of the collection name surrounded by two underscores like:  .  Ex: slug **full**.  Defaults to **basic**. |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'fields': [
       'string',
       'string'
    ]
}

IDS = 'ID1,ID2,ID3'

response = falcon.GetIntelReportEntities(parameters=PARAMS, ids=IDS)
print(response)
```

**Uber class example**

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

**Content-Type**

* Produces: _application/zip_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **Accept** | header | _string_ | Choose the format you want the rule set in. |
| :white\_check\_mark: | **id** | query | _integer_ | The ID of the rule set. |
|  | **format** | query | _string_ | Choose the format you want the rule set in. Valid formats are zip and gzip. Defaults to zip. |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'id': integer,
    'format': 'string'
}

HEADERS = {
    'Accept': 'string'
}

response = falcon.GetIntelRuleFile(parameters=PARAMS, headers=HEADERS)
print(response)
```

**Uber class example**

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

**Content-Type**

* Produces: _application/zip_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **Accept** | header | _string_ | Choose the format you want the rule set in. |
| :white\_check\_mark: | **type** | query | _string_ | The rule news report type. Accepted values:  snort-suricata-master  snort-suricata-update  snort-suricata-changelog  yara-master  yara-update  yara-changelog  common-event-format  netwitness |
|  | **format** | query | _string_ | Choose the format you want the rule set in. Valid formats are zip and gzip. Defaults to zip. |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'type': 'string',
    'format': 'string'
}

HEADERS = {
    'Accept': 'string'
}

response = falcon.GetLatestIntelRuleFile(parameters=PARAMS, headers=HEADERS)
print(response)
```

**Uber class example**

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

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | The ids of rules to return. |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.GetIntelRuleEntities(ids=IDS)
print(response)
```

**Uber class example**

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

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |  |
| :---: | :--- | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | Set the starting row number to return actors IDs from. Defaults to 0. |  |
|  | **limit** | query | _integer_ | Set the number of actor IDs to return. The value must be between 1 and 5000. |  |
|  | **sort** | query | _string_ | Order fields in ascending or descending order.  Ex: created\_date | asc. |
|  | **filter** | query | _string_ | Filter your query by specifying FQL filter parameters. Filter parameters include:  actors, actors.id, actors.name, actors.slug, actors.url, created\_date, description, id, last\_modified\_date, motivations, motivations.id, motivations.slug, motivations.value, name, name.raw, short\_description, slug, sub\_type, sub\_type.id, sub\_type.name, sub\_type.slug, tags, tags.id, tags.slug, tags.value, target\_countries, target\_countries.id, target\_countries.slug, target\_countries.value, target\_industries, target\_industries.id, target\_industries.slug, target\_industries.value, type, type.id, type.name, type.slug, url. |  |
|  | **q** | query | _string_ | Perform a generic substring search across all fields. |  |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'offset': integer,
    'limit': integer,
    'sort': 'string',
    'filter': 'string',
    'q': 'string'
}

response = falcon.QueryIntelActorIds(parameters=PARAMS)
print(response)
```

**Uber class example**

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

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |  |
| :---: | :--- | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | Set the starting row number to return indicator IDs from. Defaults to 0. |  |
|  | **limit** | query | _integer_ | Set the number of indicator IDs to return. The number must be between 1 and 50000 |  |
|  | **sort** | query | _string_ | Order fields in ascending or descending order.  Ex: published\_date | asc. |
|  | **filter** | query | _string_ | Filter your query by specifying FQL filter parameters. Filter parameters include:  \_marker, actors, deleted, domain\_types, id, indicator, ip\_address\_types, kill\_chains, labels, labels.created\_on, labels.last\_valid\_on, labels.name, last\_updated, malicious\_confidence, malware\_families, published\_date, reports, targets, threat\_types, type, vulnerabilities. |  |
|  | **q** | query | _string_ | Perform a generic substring search across all fields. |  |
|  | **include\_deleted** | query | _boolean_ | If true, include both published and deleted indicators in the response. Defaults to false. |  |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

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
```

**Uber class example**

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

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |  |
| :---: | :--- | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | Set the starting row number to return report IDs from. Defaults to 0. |  |
|  | **limit** | query | _integer_ | Set the number of report IDs to return. The value must be between 1 and 5000. |  |
|  | **sort** | query | _string_ | Order fields in ascending or descending order.  Ex: created\_date | asc. |
|  | **filter** | query | _string_ | Filter your query by specifying FQL filter parameters. Filter parameters include:  actors, actors.id, actors.name, actors.slug, actors.url, created\_date, description, id, last\_modified\_date, motivations, motivations.id, motivations.slug, motivations.value, name, name.raw, short\_description, slug, sub\_type, sub\_type.id, sub\_type.name, sub\_type.slug, tags, tags.id, tags.slug, tags.value, target\_countries, target\_countries.id, target\_countries.slug, target\_countries.value, target\_industries, target\_industries.id, target\_industries.slug, target\_industries.value, type, type.id, type.name, type.slug, url. |  |
|  | **q** | query | _string_ | Perform a generic substring search across all fields. |  |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'offset': integer,
    'limit': integer,
    'sort': 'string',
    'filter': 'string',
    'q': 'string'
}

response = falcon.QueryIntelReportIds(parameters=PARAMS)
print(response)
```

**Uber class example**

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

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |  |
| :---: | :--- | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | Set the starting row number to return reports from. Defaults to 0. |  |
|  | **limit** | query | _integer_ | The number of rule IDs to return. Defaults to 10. |  |
|  | **sort** | query | _string_ | Order fields in ascending or descending order.  Ex: created\_date | asc. |
|  | **name** | query | array \(_string_\) | Search by rule title. |  |
| :white\_check\_mark: | **type** | query | _string_ | The rule news report type. Accepted values:  snort-suricata-master  snort-suricata-update  snort-suricata-changelog  yara-master  yara-update  yara-changelog  common-event-format  netwitness |  |
|  | **description** | query | array \(_string_\) | Substring match on description field. |  |
|  | **tags** | query | array \(_string_\) | Search for rule tags. |  |
|  | **min\_created\_date** | query | _integer_ | Filter results to those created on or after a certain date. |  |
|  | **max\_created\_date** | query | _string_ | Filter results to those created on or before a certain date. |  |
|  | **q** | query | _string_ | Perform a generic substring search across all fields. |  |

**Usage**

**Service class example**

```python
from falconpy import intel as FalconIntel

falcon = FalconIntel.Intel(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

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

response = falcon.QueryIntelRuleIds(parameters=PARAMS)
print(response)
```

**Uber class example**

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

