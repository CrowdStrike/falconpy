# Overwatch Dashboard

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Overwatch Dashboard service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-X%20No-red.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [AggregatesDetectionsGlobalCounts](overwatch-dashboard.md#aggregatesdetectionsglobalcounts) | Get the total number of detections pushed across all customers |
| [AggregatesEventsCollections](overwatch-dashboard.md#aggregateseventscollections) | Get OverWatch detection event collection info by providing an aggregate query |
| [AggregatesEvents](overwatch-dashboard.md#aggregatesevents) | Get aggregate OverWatch detection event info by providing an aggregate query |
| [AggregatesIncidentsGlobalCounts](overwatch-dashboard.md#aggregatesincidentsglobalcounts) | Get the total number of incidents pushed across all customers |
| [AggregatesOWEventsGlobalCounts](overwatch-dashboard.md#aggregatesoweventsglobalcounts) | Get the total number of OverWatch events across all customers |

### AggregatesDetectionsGlobalCounts

Get the total number of detections pushed across all customers

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **filter** | query | _string_ | An FQL filter string |

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
    'filter': 'string'
}

response = falcon.command('AggregatesDetectionsGlobalCounts', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### AggregatesEventsCollections

Get OverWatch detection event collection info by providing an aggregate query

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

response = falcon.command('AggregatesEventsCollections', body=BODY)
print(response)
falcon.deauthenticate()
```

### AggregatesEvents

Get aggregate OverWatch detection event info by providing an aggregate query

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

response = falcon.command('AggregatesEvents', body=BODY)
print(response)
falcon.deauthenticate()
```

### AggregatesIncidentsGlobalCounts

Get the total number of incidents pushed across all customers

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **filter** | query | _string_ | An FQL filter string |

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
    'filter': 'string'
}

response = falcon.command('AggregatesIncidentsGlobalCounts', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### AggregatesOWEventsGlobalCounts

Get the total number of OverWatch events across all customers

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **filter** | query | _string_ | An FQL filter string |

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
    'filter': 'string'
}

response = falcon.command('AggregatesOWEventsGlobalCounts', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

