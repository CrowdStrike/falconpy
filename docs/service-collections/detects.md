# Detects

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Detects service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [GetAggregateDetects](detects.md#getaggregatedetects) | Get detect aggregates as specified via json in request body. |
| [UpdateDetectsByIdsV2](detects.md#updatedetectsbyidsv2) | Modify the state, assignee, and visibility of detections |
| [GetDetectSummaries](detects.md#getdetectsummaries) | View information about detections |
| [QueryDetects](detects.md#querydetects) | Search for detection IDs that match a given query |

### GetAggregateDetects

Get detect aggregates as specified via json in request body.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ | Query criteria and settings |

**Usage**

**Service class example**

```python
from falconpy import detects as FalconDetects

falcon = FalconDetects.Detects(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.GetAggregateDetects(body=BODY)
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

response = falcon.command('GetAggregateDetects', body=BODY)
print(response)
falcon.deauthenticate()
```

### UpdateDetectsByIdsV2

Modify the state, assignee, and visibility of detections

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ | This endpoint modifies attributes \(state and assignee\) of detections.   This endpoint accepts a query formatted as a JSON array of key-value pairs. You can update one or more attributes one or more detections with a single request.  **`assigned_to_uuid` values**  A user ID, such as `1234567891234567891`  **`ids` values**  One or more detection IDs, which you can find with the `/detects/queries/detects/v1` endpoint, the Falcon console, or the Streaming API.  **`show_in_ui` values**  - `true`: This detection is displayed in Falcon - `false`: This detection is not displayed in Falcon. Most commonly used together with the `status` key's `false_positive` value.  **`status` values**  - `new` - `in_progress` - `true_positive` - `false_positive` - `ignored`  **`comment` values** Optional comment to add to the detection. Comments are displayed with the detection in Falcon and usually used to provide context or notes for other Falcon users. A detection can have multiple comments over time. |

**Usage**

**Service class example**

```python
from falconpy import detects as FalconDetects

falcon = FalconDetects.Detects(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.UpdateDetectsByIdsV2(body=BODY)
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

response = falcon.command('UpdateDetectsByIdsV2', body=BODY)
print(response)
falcon.deauthenticate()
```

### GetDetectSummaries

View information about detections

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ | View key attributes of detections, including the associated host, [disposition](https://falcon.crowdstrike.com/support/documentation/2/query-api-reference#patterndispositionvalue), objective/tactic/technique, adversary, and more. Specify one or more detection IDs \(max 1000 per request\). Find detection IDs with the `/detects/queries/detects/v1` endpoint, the Falcon console, or the Streaming API. |

**Usage**

**Service class example**

```python
from falconpy import detects as FalconDetects

falcon = FalconDetects.Detects(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.GetDetectSummaries(body=BODY)
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

response = falcon.command('GetDetectSummaries', body=BODY)
print(response)
falcon.deauthenticate()
```

### QueryDetects

Search for detection IDs that match a given query

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **offset** | query | _integer_ | The first detection to return, where `0` is the latest detection. Use with the `limit` parameter to manage pagination of results. |
|  | **limit** | query | _integer_ | The maximum number of detections to return in this response \(default: 9999; max: 9999\). Use with the `offset` parameter to manage pagination of results. |
|  | **sort** | query | _string_ | Sort detections using these options:  - `first_behavior`: Timestamp of the first behavior associated with this detection - `last_behavior`: Timestamp of the last behavior associated with this detection - `max_severity`: Highest severity of the behaviors associated with this detection - `max_confidence`: Highest confidence of the behaviors associated with this detection - `adversary_id`: ID of the adversary associated with this detection, if any - `devices.hostname`: Hostname of the host where this detection was detected  Sort either `asc` \(ascending\) or `desc` \(descending\). For example: \`last\_behavior \| asc\` |
|  | **filter** | query | _string_ | Filter detections using a query in Falcon Query Language \(FQL\) An asterisk wildcard `*` includes all results.   Common filter options include:  - `status` - `device.device_id` - `max_severity`  The full list of valid filter options is extensive. Review it in our [documentation inside the Falcon console](https://falcon.crowdstrike.com/support/documentation/2/query-api-reference#detections_fql). |
|  | **q** | query | _string_ | Search all detection metadata for the provided string |

**Usage**

**Service class example**

```python
from falconpy import detects as FalconDetects

falcon = FalconDetects.Detects(creds={
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

response = falcon.QueryDetects(parameters=PARAMS)
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

response = falcon.command('QueryDetects', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

