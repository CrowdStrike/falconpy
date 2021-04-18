# Falcon Complete Dashboard

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Falcon Complete Dashboard service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-X%20No-red.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [AggregateAllowList](falcon-complete-dashboard.md#aggregateallowlist) | Retrieve aggregate allowlist ticket values based on the matched filter |
| [AggregateBlockList](falcon-complete-dashboard.md#aggregateblocklist) | Retrieve aggregate blocklist ticket values based on the matched filter |
| [AggregateDetections](falcon-complete-dashboard.md#aggregatedetections) | Retrieve aggregate detection values based on the matched filter |
| [AggregateDeviceCountCollection](falcon-complete-dashboard.md#aggregatedevicecountcollection) | Retrieve aggregate host/devices count based on the matched filter |
| [AggregateEscalations](falcon-complete-dashboard.md#aggregateescalations) | Retrieve aggregate escalation ticket values based on the matched filter |
| [AggregateFCIncidents](falcon-complete-dashboard.md#aggregatefcincidents) | Retrieve aggregate incident values based on the matched filter |
| [AggregateRemediations](falcon-complete-dashboard.md#aggregateremediations) | Retrieve aggregate remediation ticket values based on the matched filter |
| [QueryAllowListFilter](falcon-complete-dashboard.md#queryallowlistfilter) | Retrieve allowlist tickets that match the provided filter criteria with scrolling enabled |
| [QueryBlockListFilter](falcon-complete-dashboard.md#queryblocklistfilter) | Retrieve block listtickets that match the provided filter criteria with scrolling enabled |
| [QueryDetectionIdsByFilter](falcon-complete-dashboard.md#querydetectionidsbyfilter) | Retrieve DetectionsIds that match the provided FQL filter, criteria with scrolling enabled |
| [GetDeviceCountCollectionQueriesByFilter](falcon-complete-dashboard.md#getdevicecountcollectionqueriesbyfilter) | Retrieve device count collection Ids that match the provided FQL filter, criteria with scrolling enabled |
| [QueryEscalationsFilter](falcon-complete-dashboard.md#queryescalationsfilter) | Retrieve escalation tickets that match the provided filter criteria with scrolling enabled |
| [QueryIncidentIdsByFilter](falcon-complete-dashboard.md#queryincidentidsbyfilter) | Retrieve incidents that match the provided filter criteria with scrolling enabled |
| [QueryRemediationsFilter](falcon-complete-dashboard.md#queryremediationsfilter) | Retrieve remediation tickets that match the provided filter criteria with scrolling enabled |

### AggregateAllowList

Retrieve aggregate allowlist ticket values based on the matched filter

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ |  |

**Usage**

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

response = falcon.command('AggregateAllowList', body=BODY)
print(response)
falcon.deauthenticate()
```

### AggregateBlockList

Retrieve aggregate blocklist ticket values based on the matched filter

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ |  |

**Usage**

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

response = falcon.command('AggregateBlockList', body=BODY)
print(response)
falcon.deauthenticate()
```

### AggregateDetections

Retrieve aggregate detection values based on the matched filter

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ |  |

**Usage**

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

response = falcon.command('AggregateDetections', body=BODY)
print(response)
falcon.deauthenticate()
```

### AggregateDeviceCountCollection

Retrieve aggregate host/devices count based on the matched filter

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ |  |

**Usage**

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

response = falcon.command('AggregateDeviceCountCollection', body=BODY)
print(response)
falcon.deauthenticate()
```

### AggregateEscalations

Retrieve aggregate escalation ticket values based on the matched filter

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ |  |

**Usage**

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

response = falcon.command('AggregateEscalations', body=BODY)
print(response)
falcon.deauthenticate()
```

### AggregateFCIncidents

Retrieve aggregate incident values based on the matched filter

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ |  |

**Usage**

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

response = falcon.command('AggregateFCIncidents', body=BODY)
print(response)
falcon.deauthenticate()
```

### AggregateRemediations

Retrieve aggregate remediation ticket values based on the matched filter

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ |  |

**Usage**

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

response = falcon.command('AggregateRemediations', body=BODY)
print(response)
falcon.deauthenticate()
```

### QueryAllowListFilter

Retrieve allowlist tickets that match the provided filter criteria with scrolling enabled

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-500\] |
|  | **sort** | query | _string_ | The property to sort on, followed by a dot \(.\), followed by the sort direction, either "asc" or "desc". |
|  | **filter** | query | _string_ | Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |

**Usage**

**Uber class example**

```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

PARAMS = {
    'limit': integer,
    'sort': 'string',
    'filter': 'string',
    'offset': 'string'
}

response = falcon.command('QueryAllowListFilter', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### QueryBlockListFilter

Retrieve block listtickets that match the provided filter criteria with scrolling enabled

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-500\] |
|  | **sort** | query | _string_ | The property to sort on, followed by a dot \(.\), followed by the sort direction, either "asc" or "desc". |
|  | **filter** | query | _string_ | Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |

**Usage**

**Uber class example**

```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

PARAMS = {
    'limit': integer,
    'sort': 'string',
    'filter': 'string',
    'offset': 'string'
}

response = falcon.command('QueryBlockListFilter', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### QueryDetectionIdsByFilter

Retrieve DetectionsIds that match the provided FQL filter, criteria with scrolling enabled

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-500\] |
|  | **sort** | query | _string_ | The property to sort on, followed by a dot \(.\), followed by the sort direction, either "asc" or "desc". |
|  | **filter** | query | _string_ | Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |

**Usage**

**Uber class example**

```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

PARAMS = {
    'limit': integer,
    'sort': 'string',
    'filter': 'string',
    'offset': 'string'
}

response = falcon.command('QueryDetectionIdsByFilter', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### GetDeviceCountCollectionQueriesByFilter

Retrieve device count collection Ids that match the provided FQL filter, criteria with scrolling enabled

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-500\] |
|  | **sort** | query | _string_ | The property to sort on, followed by a dot \(.\), followed by the sort direction, either "asc" or "desc". |
|  | **filter** | query | _string_ | Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |

**Usage**

**Uber class example**

```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

PARAMS = {
    'limit': integer,
    'sort': 'string',
    'filter': 'string',
    'offset': 'string'
}

response = falcon.command('GetDeviceCountCollectionQueriesByFilter', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### QueryEscalationsFilter

Retrieve escalation tickets that match the provided filter criteria with scrolling enabled

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-500\] |
|  | **sort** | query | _string_ | The property to sort on, followed by a dot \(.\), followed by the sort direction, either "asc" or "desc". |
|  | **filter** | query | _string_ | Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |

**Usage**

**Uber class example**

```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

PARAMS = {
    'limit': integer,
    'sort': 'string',
    'filter': 'string',
    'offset': 'string'
}

response = falcon.command('QueryEscalationsFilter', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### QueryIncidentIdsByFilter

Retrieve incidents that match the provided filter criteria with scrolling enabled

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-500\] |
|  | **sort** | query | _string_ | The property to sort on, followed by a dot \(.\), followed by the sort direction, either "asc" or "desc". |
|  | **filter** | query | _string_ | Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |

**Usage**

**Uber class example**

```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

PARAMS = {
    'limit': integer,
    'sort': 'string',
    'filter': 'string',
    'offset': 'string'
}

response = falcon.command('QueryIncidentIdsByFilter', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### QueryRemediationsFilter

Retrieve remediation tickets that match the provided filter criteria with scrolling enabled

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-500\] |
|  | **sort** | query | _string_ | The property to sort on, followed by a dot \(.\), followed by the sort direction, either "asc" or "desc". |
|  | **filter** | query | _string_ | Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |

**Usage**

**Uber class example**

```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

PARAMS = {
    'limit': integer,
    'sort': 'string',
    'filter': 'string',
    'offset': 'string'
}

response = falcon.command('QueryRemediationsFilter', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

