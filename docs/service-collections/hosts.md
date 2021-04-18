# Hosts

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Hosts service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [PerformActionV2](hosts.md#performactionv2) | Take various actions on the hosts in your environment. Contain or lift containment on a host. Delete or restore a host. |
| [UpdateDeviceTags](hosts.md#updatedevicetags) | Append or remove one or more Falcon Grouping Tags on one or more hosts. |
| [GetDeviceDetails](hosts.md#getdevicedetails) | Get details on one or more hosts by providing agent IDs \(AID\). You can get a host's agent IDs \(AIDs\) from the /devices/queries/devices/v1 endpoint, the Falcon console or the Streaming API |
| [QueryHiddenDevices](hosts.md#queryhiddendevices) | Retrieve hidden hosts that match the provided filter criteria. |
| [QueryDevicesByFilterScroll](hosts.md#querydevicesbyfilterscroll) | Search for hosts in your environment by platform, hostname, IP, and other criteria with continuous pagination capability \(based on offset pointer which expires after 2 minutes with no maximum limit\) |
| [QueryDevicesByFilter](hosts.md#querydevicesbyfilter) | Search for hosts in your environment by platform, hostname, IP, and other criteria. |

### PerformActionV2

Take various actions on the hosts in your environment. Contain or lift containment on a host. Delete or restore a host.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **action\_name** | query | _string_ | Specify one of these actions:  - `contain` - This action contains the host, which stops any network communications to locations other than the CrowdStrike cloud and IPs specified in your [containment policy](https://falcon.crowdstrike.com/support/documentation/11/getting-started-guide#containmentpolicy) - `lift_containment`: This action lifts containment on the host, which returns its network communications to normal - `hide_host`: This action will delete a host. After the host is deleted, no new detections for that host will be reported via UI or APIs - `unhide_host`: This action will restore a host. Detection reporting will resume after the host is restored |
| :white\_check\_mark: | **body** | body | _string_ | The host agent ID \(AID\) of the host you want to contain. Get an agent ID from a detection, the Falcon console, or the Streaming API.  Provide the ID in JSON format with the key `ids` and the value in square brackets, such as:   `"ids": ["123456789"]` |

**Usage**

**Service class example**

```python
from falconpy import hosts as FalconHosts

falcon = FalconHosts.Hosts(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'action_name': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.PerformActionV2(parameters=PARAMS, body=BODY)
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
    'action_name': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.command('PerformActionV2', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```

### UpdateDeviceTags

Append or remove one or more Falcon Grouping Tags on one or more hosts.

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
from falconpy import hosts as FalconHosts

falcon = FalconHosts.Hosts(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.UpdateDeviceTags(body=BODY)
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

response = falcon.command('UpdateDeviceTags', body=BODY)
print(response)
falcon.deauthenticate()
```

### GetDeviceDetails

Get details on one or more hosts by providing agent IDs \(AID\). You can get a host's agent IDs \(AIDs\) from the /devices/queries/devices/v1 endpoint, the Falcon console or the Streaming API

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | The host agentIDs used to get details on |

**Usage**

**Service class example**

```python
from falconpy import hosts as FalconHosts

falcon = FalconHosts.Hosts(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.GetDeviceDetails(ids=IDS)
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

response = falcon.command('GetDeviceDetails', ids=IDS)
print(response)
falcon.deauthenticate()
```

### QueryHiddenDevices

Retrieve hidden hosts that match the provided filter criteria.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by \(e.g. status.desc or hostname.asc\) |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |

**Usage**

**Service class example**

```python
from falconpy import hosts as FalconHosts

falcon = FalconHosts.Hosts(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'offset': integer,
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.QueryHiddenDevices(parameters=PARAMS)
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
    'filter': 'string'
}

response = falcon.command('QueryHiddenDevices', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### QueryDevicesByFilterScroll

Search for hosts in your environment by platform, hostname, IP, and other criteria with continuous pagination capability \(based on offset pointer which expires after 2 minutes with no maximum limit\)

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **offset** | query | _string_ | The offset to page from, for the next result set |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by \(e.g. status.desc or hostname.asc\) |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |

**Usage**

**Service class example**

```python
from falconpy import hosts as FalconHosts

falcon = FalconHosts.Hosts(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'offset': 'string',
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.QueryDevicesByFilterScroll(parameters=PARAMS)
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
    'offset': 'string',
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.command('QueryDevicesByFilterScroll', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### QueryDevicesByFilter

Search for hosts in your environment by platform, hostname, IP, and other criteria.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by \(e.g. status.desc or hostname.asc\) |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |

**Usage**

**Service class example**

```python
from falconpy import hosts as FalconHosts

falcon = FalconHosts.Hosts(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'offset': integer,
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.QueryDevicesByFilter(parameters=PARAMS)
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
    'filter': 'string'
}

response = falcon.command('QueryDevicesByFilter', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

