# Installation Tokens

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Installation Tokens service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-X%20No-red.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [audit\_events\_read](installation-tokens.md#audit_events_read) | Gets the details of one or more audit events by id. |
| [customer\_settings\_read](installation-tokens.md#customer_settings_read) | Check current installation token settings. |
| [tokens\_read](installation-tokens.md#tokens_read) | Gets the details of one or more tokens by id. |
| [tokens\_create](installation-tokens.md#tokens_create) | Creates a token. |
| [tokens\_delete](installation-tokens.md#tokens_delete) | Deletes a token immediately. To revoke a token, use PATCH /installation-tokens/entities/tokens/v1 instead. |
| [tokens\_update](installation-tokens.md#tokens_update) | Updates one or more tokens. Use this endpoint to edit labels, change expiration, revoke, or restore. |
| [audit\_events\_query](installation-tokens.md#audit_events_query) | Search for audit events by providing an FQL filter and paging details. |
| [tokens\_query](installation-tokens.md#tokens_query) | Search for tokens by providing an FQL filter and paging details. |

### audit\_events\_read

Gets the details of one or more audit events by id.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **ids** | query | array \(_string_\) | IDs of audit events to retrieve details for |

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

response = falcon.command('audit-events-read', ids=IDS)
print(response)
falcon.deauthenticate()
```

### customer\_settings\_read

Check current installation token settings.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

No parameters

**Usage**

**Uber class example**

```python
from falconpy import api_complete as FalconSDK

falcon = FalconSDK.APIHarness(creds={
      'client_id': falcon_client_id,
      'client_secret': falcon_client_secret
   }
)

response = falcon.command('customer-settings-read')
print(response)
falcon.deauthenticate()
```

### tokens\_read

Gets the details of one or more tokens by id.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **ids** | query | array \(_string_\) | IDs of tokens to retrieve details for |

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

response = falcon.command('tokens-read', ids=IDS)
print(response)
falcon.deauthenticate()
```

### tokens\_create

Creates a token.

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

response = falcon.command('tokens-create', body=BODY)
print(response)
falcon.deauthenticate()
```

### tokens\_delete

Deletes a token immediately. To revoke a token, use PATCH /installation-tokens/entities/tokens/v1 instead.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | The token ids to delete. |

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

response = falcon.command('tokens-delete', ids=IDS)
print(response)
falcon.deauthenticate()
```

### tokens\_update

Updates one or more tokens. Use this endpoint to edit labels, change expiration, revoke, or restore.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | The token ids to update. |
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

IDS = 'ID1,ID2,ID3'

response = falcon.command('tokens-update', body=BODY, ids=IDS)
print(response)
falcon.deauthenticate()
```

### audit\_events\_query

Search for audit events by providing an FQL filter and paging details.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | The offset to start retrieving records from. |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-1000\]. Defaults to 50. |
|  | **sort** | query | _string_ | The property to sort by \(e.g. timestamp.desc\). |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results \(e.g., `action:'token_create'`\). |

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
    'offset': integer,
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.command('audit-events-query', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### tokens\_query

Search for tokens by providing an FQL filter and paging details.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | The offset to start retrieving records from. |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-1000\]. Defaults to 50. |
|  | **sort** | query | _string_ | The property to sort by \(e.g. created\_timestamp.desc\). |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results \(e.g., `status:'valid'`\). |

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
    'offset': integer,
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.command('tokens-query', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

