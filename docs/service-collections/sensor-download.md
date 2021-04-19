# Sensor Download

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Sensor Download service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [GetCombinedSensorInstallersByQuery](sensor-download.md#getcombinedsensorinstallersbyquery) | Get sensor installer details by provided query |
| [DownloadSensorInstallerById](sensor-download.md#downloadsensorinstallerbyid) | Download sensor installer by SHA256 ID |
| [GetSensorInstallersEntities](sensor-download.md#getsensorinstallersentities) | Get sensor installer details by provided SHA256 IDs |
| [GetSensorInstallersCCIDByQuery](sensor-download.md#getsensorinstallersccidbyquery) | Get CCID to use with sensor installers |
| [GetSensorInstallersByQuery](sensor-download.md#getsensorinstallersbyquery) | Get sensor installer IDs by provided query |

### GetCombinedSensorInstallersByQuery

Get sensor installer details by provided query

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |  |  |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | The first item to return, where 0 is the latest item. Use with the limit parameter to manage pagination of results. |  |  |
|  | **limit** | query | _integer_ | The number of items to return in this response \(default: 100, max: 500\). Use with the offset parameter to manage pagination of results. |  |  |
|  | **sort** | query | _string_ | Sort items using their properties. Common sort options include:  version | asc&lt;/li&gt;release\_date | desc&lt;/li&gt;&lt;/ul&gt; |
|  | **filter** | query | _string_ | Filter items using a query in Falcon Query Language \(FQL\). An asterisk wildcard \* includes all results.  Common filter options include:  |  |  |

**Usage**

**Service class example**

```python
from falconpy import sensor_download as FalconSensor

falcon = FalconSensor.Sensor_Download(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'offset': integer,
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.GetCombinedSensorInstallersByQuery(parameters=PARAMS)
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

response = falcon.command('GetCombinedSensorInstallersByQuery', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### DownloadSensorInstallerById

Download sensor installer by SHA256 ID

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **id** | query | _string_ | SHA256 of the installer to download |

**Usage**

**Service class example**

```python
from falconpy import sensor_download as FalconSensor

falcon = FalconSensor.Sensor_Download(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'id': 'string'
}

response = falcon.DownloadSensorInstallerById(parameters=PARAMS)
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

response = falcon.command('DownloadSensorInstallerById', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### GetSensorInstallersEntities

Get sensor installer details by provided SHA256 IDs

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the installers |

**Usage**

**Service class example**

```python
from falconpy import sensor_download as FalconSensor

falcon = FalconSensor.Sensor_Download(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.GetSensorInstallersEntities(ids=IDS)
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

response = falcon.command('GetSensorInstallersEntities', ids=IDS)
print(response)
falcon.deauthenticate()
```

### GetSensorInstallersCCIDByQuery

Get CCID to use with sensor installers

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

No parameters

**Usage**

**Service class example**

```python
from falconpy import sensor_download as FalconSensor

falcon = FalconSensor.Sensor_Download(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

response = falcon.GetSensorInstallersCCIDByQuery()
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

response = falcon.command('GetSensorInstallersCCIDByQuery')
print(response)
falcon.deauthenticate()
```

### GetSensorInstallersByQuery

Get sensor installer IDs by provided query

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |  |  |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | The first item to return, where 0 is the latest item. Use with the limit parameter to manage pagination of results. |  |  |
|  | **limit** | query | _integer_ | The number of items to return in this response \(default: 100, max: 500\). Use with the offset parameter to manage pagination of results. |  |  |
|  | **sort** | query | _string_ | Sort items using their properties. Common sort options include:  version | asc&lt;/li&gt;release\_date | desc&lt;/li&gt;&lt;/ul&gt; |
|  | **filter** | query | _string_ | Filter items using a query in Falcon Query Language \(FQL\). An asterisk wildcard \* includes all results.  Common filter options include:  |  |  |

**Usage**

**Service class example**

```python
from falconpy import sensor_download as FalconSensor

falcon = FalconSensor.Sensor_Download(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'offset': integer,
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.GetSensorInstallersByQuery(parameters=PARAMS)
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

response = falcon.command('GetSensorInstallersByQuery', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

