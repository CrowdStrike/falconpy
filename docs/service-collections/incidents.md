# Incidents

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Incidents service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [CrowdScore](incidents.md#crowdscore) | Query environment wide CrowdScore and return the entity data |
| [GetBehaviors](incidents.md#getbehaviors) | Get details on behaviors by providing behavior IDs |
| [PerformIncidentAction](incidents.md#performincidentaction) | Perform a set of actions on one or more incidents, such as adding tags or comments or updating the incident name or description |
| [GetIncidents](incidents.md#getincidents) | Get details on incidents by providing incident IDs |
| [QueryBehaviors](incidents.md#querybehaviors) | Search for behaviors by providing an FQL filter, sorting, and paging details |
| [QueryIncidents](incidents.md#queryincidents) | Search for incidents by providing an FQL filter, sorting, and paging details |

### CrowdScore

Query environment wide CrowdScore and return the entity data

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **filter** | query | _string_ | Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-2500\] |
|  | **sort** | query | _string_ | The property to sort on, followed by a dot \(.\), followed by the sort direction, either "asc" or "desc". |

**Usage**

**Service class example**

```python
from falconpy import incidents as FalconIncidents

falcon = FalconIncidents.Incidents(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'filter': 'string',
    'offset': 'string',
    'limit': integer,
    'sort': 'string'
}

response = falcon.CrowdScore(parameters=PARAMS)
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
    'filter': 'string',
    'offset': 'string',
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('CrowdScore', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### GetBehaviors

Get details on behaviors by providing behavior IDs

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import incidents as FalconIncidents

falcon = FalconIncidents.Incidents(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.GetBehaviors(body=BODY)
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

response = falcon.command('GetBehaviors', body=BODY)
print(response)
falcon.deauthenticate()
```

### PerformIncidentAction

Perform a set of actions on one or more incidents, such as adding tags or comments or updating the incident name or description

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import incidents as FalconIncidents

falcon = FalconIncidents.Incidents(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.PerformIncidentAction(body=BODY)
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

response = falcon.command('PerformIncidentAction', body=BODY)
print(response)
falcon.deauthenticate()
```

### GetIncidents

Get details on incidents by providing incident IDs

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import incidents as FalconIncidents

falcon = FalconIncidents.Incidents(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.GetIncidents(body=BODY)
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

response = falcon.command('GetIncidents', body=BODY)
print(response)
falcon.deauthenticate()
```

### QueryBehaviors

Search for behaviors by providing an FQL filter, sorting, and paging details

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **filter** | query | _string_ | Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-500\] |
|  | **sort** | query | _string_ | The property to sort on, followed by a dot \(.\), followed by the sort direction, either "asc" or "desc". |

**Usage**

**Service class example**

```python
from falconpy import incidents as FalconIncidents

falcon = FalconIncidents.Incidents(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'filter': 'string',
    'offset': 'string',
    'limit': integer,
    'sort': 'string'
}

response = falcon.QueryBehaviors(parameters=PARAMS)
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
    'filter': 'string',
    'offset': 'string',
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('QueryBehaviors', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### QueryIncidents

Search for incidents by providing an FQL filter, sorting, and paging details

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **sort** | query | _string_ | The property to sort on, followed by a dot \(.\), followed by the sort direction, either "asc" or "desc". |
|  | **filter** | query | _string_ | Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-500\] |

**Usage**

**Service class example**

```python
from falconpy import incidents as FalconIncidents

falcon = FalconIncidents.Incidents(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'sort': 'string',
    'filter': 'string',
    'offset': 'string',
    'limit': integer
}

response = falcon.QueryIncidents(parameters=PARAMS)
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
    'sort': 'string',
    'filter': 'string',
    'offset': 'string',
    'limit': integer
}

response = falcon.command('QueryIncidents', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

