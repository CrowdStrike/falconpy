# IOA Exclusions

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the IOA Exclusions service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-X%20No-red.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [getIOAExclusionsV1](ioa-exclusions.md#getioaexclusionsv1) | Get a set of IOA Exclusions by specifying their IDs |
| [createIOAExclusionsV1](ioa-exclusions.md#createioaexclusionsv1) | Create the IOA exclusions |
| [deleteIOAExclusionsV1](ioa-exclusions.md#deleteioaexclusionsv1) | Delete the IOA exclusions by id |
| [updateIOAExclusionsV1](ioa-exclusions.md#updateioaexclusionsv1) | Update the IOA exclusions |
| [queryIOAExclusionsV1](ioa-exclusions.md#queryioaexclusionsv1) | Search for IOA exclusions. |

### getIOAExclusionsV1

Get a set of IOA Exclusions by specifying their IDs

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The ids of the exclusions to retrieve |

**Usage**

**Uber class example**

```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

IDS = 'ID1,ID2,ID3'

response = falcon.command('getIOAExclusionsV1', ids=IDS)
print(response)
falcon.deauthenticate()
```

### createIOAExclusionsV1

Create the IOA exclusions

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

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

response = falcon.command('createIOAExclusionsV1', body=BODY)
print(response)
falcon.deauthenticate()
```

### deleteIOAExclusionsV1

Delete the IOA exclusions by id

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The ids of the exclusions to delete |
|  | **comment** | query | _string_ | Explains why this exclusions was deleted |

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
    'comment': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('deleteIOAExclusionsV1', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```

### updateIOAExclusionsV1

Update the IOA exclusions

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

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

response = falcon.command('updateIOAExclusionsV1', body=BODY)
print(response)
falcon.deauthenticate()
```

### queryIOAExclusionsV1

Search for IOA exclusions.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results. |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-500\] |
|  | **sort** | query | _string_ | The sort expression that should be used to sort the results. |

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
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('queryIOAExclusionsV1', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

