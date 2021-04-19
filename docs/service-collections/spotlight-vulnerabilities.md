# Spotlight Vulnerabilities

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Spotlight Vulnerabilities service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [getVulnerabilities](spotlight-vulnerabilities.md#getvulnerabilities) | Get details on vulnerabilities by providing one or more IDs |
| [queryVulnerabilities](spotlight-vulnerabilities.md#queryvulnerabilities) | Search for Vulnerabilities in your environment by providing an FQL filter and paging details. Returns a set of Vulnerability IDs which match the filter criteria |

### getVulnerabilities

Get details on vulnerabilities by providing one or more IDs

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | One or more vulnerability IDs \(max: 400\). Find vulnerability IDs with GET /spotlight/queries/vulnerabilities/v1 |

**Usage**

**Service class example**

```python
from falconpy import spotlight_vulnerabilities as FalconSV

falcon = FalconSV.Sensor_Vulnerabilities(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.getVulnerabilities(ids=IDS)
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

response = falcon.command('getVulnerabilities', ids=IDS)
print(response)
falcon.deauthenticate()
```

### queryVulnerabilities

Search for Vulnerabilities in your environment by providing an FQL filter and paging details. Returns a set of Vulnerability IDs which match the filter criteria

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |  |  |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
|  | **after** | query | _string_ | A pagination token used with the `limit` parameter to manage pagination of results. On your first request, don't provide an `after` token. On subsequent requests, provide the `after` token from the previous response to continue from that place in the results. |  |  |
|  | **limit** | query | _integer_ | The number of items to return in this response \(default: 100, max: 400\). Use with the after parameter to manage pagination of results. |  |  |
|  | **sort** | query | _string_ | Sort vulnerabilities by their properties. Common sort options include:  created\_timestamp | desc&lt;/li&gt;closed\_timestamp | asc&lt;/li&gt;&lt;/ul&gt; |
| ✅ | **filter** | query | _string_ | Filter items using a query in Falcon Query Language \(FQL\). Wildcards \* are unsupported.   Common filter options include:   |  |  |

**Usage**

**Service class example**

```python
from falconpy import spotlight_vulnerabilities as FalconSV

falcon = FalconSV.Sensor_Vulnerabilities(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'after': 'string',
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.queryVulnerabilities(parameters=PARAMS)
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
    'after': 'string',
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.command('queryVulnerabilities', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

