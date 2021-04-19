# IOCs

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the IOCs service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [DevicesCount](iocs.md#devicescount) | Number of hosts in your customer account that have observed a given custom IOC |
| [GetIOC](iocs.md#getioc) | Get an IOC by providing a type and value |
| [CreateIOC](iocs.md#createioc) | Create a new IOC |
| [DeleteIOC](iocs.md#deleteioc) | Delete an IOC by providing a type and value |
| [UpdateIOC](iocs.md#updateioc) | Update an IOC by providing a type and value |
| [DevicesRanOn](iocs.md#devicesranon) | Find hosts that have observed a given custom IOC. For details about those hosts, use GET /devices/entities/devices/v1 |
| [QueryIOCs](iocs.md#queryiocs) | Search the custom IOCs in your customer account |
| [ProcessesRanOn](iocs.md#processesranon) | Search for processes associated with a custom IOC |
| [entities\_processes](iocs.md#entities_processes) | For the provided ProcessID retrieve the process details |

### DevicesCount

Number of hosts in your customer account that have observed a given custom IOC

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **type** | query | _string_ | The type of the indicator. Valid types include:  sha256: A hex-encoded sha256 hash string. Length - min: 64, max: 64.  md5: A hex-encoded md5 hash string. Length - min 32, max: 32.  domain: A domain name. Length - min: 1, max: 200.  ipv4: An IPv4 address. Must be a valid IP address.  ipv6: An IPv6 address. Must be a valid IP address. |
| ✅ | **value** | query | _string_ | The string representation of the indicator |

**Usage**

**Service class example**

```python
from falconpy import iocs as FalconIOCs

falcon = FalconIOCs.Iocs(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'type': 'string',
    'value': 'string'
}

response = falcon.DevicesCount(parameters=PARAMS)
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
    'value': 'string'
}

response = falcon.command('DevicesCount', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### GetIOC

Get an IOC by providing a type and value

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **type** | query | _string_ | The type of the indicator. Valid types include:  sha256: A hex-encoded sha256 hash string. Length - min: 64, max: 64.  md5: A hex-encoded md5 hash string. Length - min 32, max: 32.  domain: A domain name. Length - min: 1, max: 200.  ipv4: An IPv4 address. Must be a valid IP address.  ipv6: An IPv6 address. Must be a valid IP address. |
| ✅ | **value** | query | _string_ | The string representation of the indicator |

**Usage**

**Service class example**

```python
from falconpy import iocs as FalconIOCs

falcon = FalconIOCs.Iocs(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'type': 'string',
    'value': 'string'
}

response = falcon.GetIOC(parameters=PARAMS)
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
    'value': 'string'
}

response = falcon.command('GetIOC', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### CreateIOC

Create a new IOC

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ | Create a new IOC by providing a JSON object that includes these key/value pairs:  **type** \(required\): The type of the indicator. Valid values:  - sha256: A hex-encoded sha256 hash string. Length - min: 64, max: 64.  - md5: A hex-encoded md5 hash string. Length - min 32, max: 32.  - domain: A domain name. Length - min: 1, max: 200.  - ipv4: An IPv4 address. Must be a valid IP address.  - ipv6: An IPv6 address. Must be a valid IP address.  **value** \(required\): The string representation of the indicator.  **policy** \(required\): Action to take when a host observes the custom IOC. Values:  - detect: Enable detections for this custom IOC  - none: Disable detections for this custom IOC  **share\_level** \(optional\): Visibility of this custom IOC. All custom IOCs are visible only within your customer account, so only one value is valid:  - red  **expiration\_days** \(optional\): Number of days this custom IOC is active. Only applies for the types `domain`, `ipv4`, and `ipv6`.  **source** \(optional\): The source where this indicator originated. This can be used for tracking where this indicator was defined. Limit 200 characters.  **description** \(optional\): Descriptive label for this custom IOC |

**Usage**

**Service class example**

```python
from falconpy import iocs as FalconIOCs

falcon = FalconIOCs.Iocs(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.CreateIOC(body=BODY)
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

response = falcon.command('CreateIOC', body=BODY)
print(response)
falcon.deauthenticate()
```

### DeleteIOC

Delete an IOC by providing a type and value

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **type** | query | _string_ | The type of the indicator. Valid types include:  sha256: A hex-encoded sha256 hash string. Length - min: 64, max: 64.  md5: A hex-encoded md5 hash string. Length - min 32, max: 32.  domain: A domain name. Length - min: 1, max: 200.  ipv4: An IPv4 address. Must be a valid IP address.  ipv6: An IPv6 address. Must be a valid IP address. |
| ✅ | **value** | query | _string_ | The string representation of the indicator |

**Usage**

**Service class example**

```python
from falconpy import iocs as FalconIOCs

falcon = FalconIOCs.Iocs(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'type': 'string',
    'value': 'string'
}

response = falcon.DeleteIOC(parameters=PARAMS)
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
    'value': 'string'
}

response = falcon.command('DeleteIOC', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### UpdateIOC

Update an IOC by providing a type and value

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |
| ✅ | **type** | query | _string_ | The type of the indicator. Valid types include:  sha256: A hex-encoded sha256 hash string. Length - min: 64, max: 64.  md5: A hex-encoded md5 hash string. Length - min 32, max: 32.  domain: A domain name. Length - min: 1, max: 200.  ipv4: An IPv4 address. Must be a valid IP address.  ipv6: An IPv6 address. Must be a valid IP address. |
| ✅ | **value** | query | _string_ | The string representation of the indicator |

**Usage**

**Service class example**

```python
from falconpy import iocs as FalconIOCs

falcon = FalconIOCs.Iocs(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'type': 'string',
    'value': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.UpdateIOC(parameters=PARAMS, body=BODY)
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
    'value': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.command('UpdateIOC', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```

### DevicesRanOn

Find hosts that have observed a given custom IOC. For details about those hosts, use GET /devices/entities/devices/v1

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **type** | query | _string_ | The type of the indicator. Valid types include:  sha256: A hex-encoded sha256 hash string. Length - min: 64, max: 64.  md5: A hex-encoded md5 hash string. Length - min 32, max: 32.  domain: A domain name. Length - min: 1, max: 200.  ipv4: An IPv4 address. Must be a valid IP address.  ipv6: An IPv6 address. Must be a valid IP address. |
| ✅ | **value** | query | _string_ | The string representation of the indicator |
|  | **limit** | query | _string_ | The first process to return, where 0 is the latest offset. Use with the offset parameter to manage pagination of results. |
|  | **offset** | query | _string_ | The first process to return, where 0 is the latest offset. Use with the limit parameter to manage pagination of results. |

**Usage**

**Service class example**

```python
from falconpy import iocs as FalconIOCs

falcon = FalconIOCs.Iocs(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'type': 'string',
    'value': 'string',
    'limit': 'string',
    'offset': 'string'
}

response = falcon.DevicesRanOn(parameters=PARAMS)
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
    'value': 'string',
    'limit': 'string',
    'offset': 'string'
}

response = falcon.command('DevicesRanOn', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### QueryIOCs

Search the custom IOCs in your customer account

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **types** | query | _string_ | The type of the indicator. Valid types include:  sha256: A hex-encoded sha256 hash string. Length - min: 64, max: 64.  md5: A hex-encoded md5 hash string. Length - min 32, max: 32.  domain: A domain name. Length - min: 1, max: 200.  ipv4: An IPv4 address. Must be a valid IP address.  ipv6: An IPv6 address. Must be a valid IP address. |
|  | **values** | query | _string_ | The string representation of the indicator |
|  | **from.expiration\_timestamp** | query | _string_ | Find custom IOCs created after this time \(RFC-3339 timestamp\) |
|  | **to.expiration\_timestamp** | query | _string_ | Find custom IOCs created before this time \(RFC-3339 timestamp\) |
|  | **policies** | query | _string_ | ndetect: Find custom IOCs that produce notificationsnnnone: Find custom IOCs the particular indicator has been detected on a host. This is equivalent to turning the indicator off. |
|  | **sources** | query | _string_ | The source where this indicator originated. This can be used for tracking where this indicator was defined. Limit 200 characters. |
|  | **share\_levels** | query | _string_ | The level at which the indicator will be shared. Currently only red share level \(not shared\) is supported, indicating that the IOC isn't shared with other FH customers. |
|  | **created\_by** | query | _string_ | created\_by |
|  | **deleted\_by** | query | _string_ | The user or API client who deleted the custom IOC |
|  | **include\_deleted** | query | _string_ | true: Include deleted IOCs  false: Don't include deleted IOCs \(default\) |

**Usage**

**Service class example**

```python
from falconpy import iocs as FalconIOCs

falcon = FalconIOCs.Iocs(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'types': 'string',
    'values': 'string',
    'from.expiration_timestamp': 'string',
    'to.expiration_timestamp': 'string',
    'policies': 'string',
    'sources': 'string',
    'share_levels': 'string',
    'created_by': 'string',
    'deleted_by': 'string',
    'include_deleted': 'string'
}

response = falcon.QueryIOCs(parameters=PARAMS)
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
    'types': 'string',
    'values': 'string',
    'from.expiration_timestamp': 'string',
    'to.expiration_timestamp': 'string',
    'policies': 'string',
    'sources': 'string',
    'share_levels': 'string',
    'created_by': 'string',
    'deleted_by': 'string',
    'include_deleted': 'string'
}

response = falcon.command('QueryIOCs', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### ProcessesRanOn

Search for processes associated with a custom IOC

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **type** | query | _string_ | The type of the indicator. Valid types include:  sha256: A hex-encoded sha256 hash string. Length - min: 64, max: 64.  md5: A hex-encoded md5 hash string. Length - min 32, max: 32.  domain: A domain name. Length - min: 1, max: 200.  ipv4: An IPv4 address. Must be a valid IP address.  ipv6: An IPv6 address. Must be a valid IP address. |
| ✅ | **value** | query | _string_ | The string representation of the indicator |
| ✅ | **device\_id** | query | _string_ | Specify a host's ID to return only processes from that host. Get a host's ID from GET /devices/queries/devices/v1, the Falcon console, or the Streaming API. |
|  | **limit** | query | _string_ | The first process to return, where 0 is the latest offset. Use with the offset parameter to manage pagination of results. |
|  | **offset** | query | _string_ | The first process to return, where 0 is the latest offset. Use with the limit parameter to manage pagination of results. |

**Usage**

**Service class example**

```python
from falconpy import iocs as FalconIOCs

falcon = FalconIOCs.Iocs(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'type': 'string',
    'value': 'string',
    'device_id': 'string',
    'limit': 'string',
    'offset': 'string'
}

response = falcon.ProcessesRanOn(parameters=PARAMS)
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
    'value': 'string',
    'device_id': 'string',
    'limit': 'string',
    'offset': 'string'
}

response = falcon.command('ProcessesRanOn', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### entities\_processes

For the provided ProcessID retrieve the process details

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | ProcessID for the running process you want to lookup |

**Usage**

**Service class example**

```python
from falconpy import iocs as FalconIOCs

falcon = FalconIOCs.Iocs(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.entities_processes(ids=IDS)
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

response = falcon.command('entities.processes', ids=IDS)
print(response)
falcon.deauthenticate()
```

