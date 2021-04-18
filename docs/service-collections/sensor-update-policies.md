# Sensor Update Policies

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Sensor Update Policies service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [revealUninstallToken](sensor-update-policies.md#revealuninstalltoken) | Reveals an uninstall token for a specific device. To retrieve the bulk maintenance token pass the value 'MAINTENANCE' as the value for 'device\_id' |
| [queryCombinedSensorUpdateBuilds](sensor-update-policies.md#querycombinedsensorupdatebuilds) | Retrieve available builds for use with Sensor Update Policies |
| [queryCombinedSensorUpdatePolicyMembers](sensor-update-policies.md#querycombinedsensorupdatepolicymembers) | Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedSensorUpdatePolicies](sensor-update-policies.md#querycombinedsensorupdatepolicies) | Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria |
| [queryCombinedSensorUpdatePoliciesV2](sensor-update-policies.md#querycombinedsensorupdatepoliciesv2) | Search for Sensor Update Policies with additional support for uninstall protection in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria |
| [performSensorUpdatePoliciesAction](sensor-update-policies.md#performsensorupdatepoliciesaction) | Perform the specified action on the Sensor Update Policies specified in the request |
| [setSensorUpdatePoliciesPrecedence](sensor-update-policies.md#setsensorupdatepoliciesprecedence) | Sets the precedence of Sensor Update Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence |
| [getSensorUpdatePolicies](sensor-update-policies.md#getsensorupdatepolicies) | Retrieve a set of Sensor Update Policies by specifying their IDs |
| [createSensorUpdatePolicies](sensor-update-policies.md#createsensorupdatepolicies) | Create Sensor Update Policies by specifying details about the policy to create |
| [deleteSensorUpdatePolicies](sensor-update-policies.md#deletesensorupdatepolicies) | Delete a set of Sensor Update Policies by specifying their IDs |
| [updateSensorUpdatePolicies](sensor-update-policies.md#updatesensorupdatepolicies) | Update Sensor Update Policies by specifying the ID of the policy and details to update |
| [getSensorUpdatePoliciesV2](sensor-update-policies.md#getsensorupdatepoliciesv2) | Retrieve a set of Sensor Update Policies with additional support for uninstall protection by specifying their IDs |
| [createSensorUpdatePoliciesV2](sensor-update-policies.md#createsensorupdatepoliciesv2) | Create Sensor Update Policies by specifying details about the policy to create with additional support for uninstall protection |
| [updateSensorUpdatePoliciesV2](sensor-update-policies.md#updatesensorupdatepoliciesv2) | Update Sensor Update Policies by specifying the ID of the policy and details to update with additional support for uninstall protection |
| [querySensorUpdatePolicyMembers](sensor-update-policies.md#querysensorupdatepolicymembers) | Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [querySensorUpdatePolicies](sensor-update-policies.md#querysensorupdatepolicies) | Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policy IDs which match the filter criteria |

### revealUninstallToken

Reveals an uninstall token for a specific device. To retrieve the bulk maintenance token pass the value 'MAINTENANCE' as the value for 'device\_id'

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.revealUninstallToken(body=BODY)
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

response = falcon.command('revealUninstallToken', body=BODY)
print(response)
falcon.deauthenticate()
```

### queryCombinedSensorUpdateBuilds

Retrieve available builds for use with Sensor Update Policies

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **platform** | query | _string_ | The platform to return builds for |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'platform': 'string'
}

response = falcon.queryCombinedSensorUpdateBuilds(parameters=PARAMS)
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
    'platform': 'string'
}

response = falcon.command('queryCombinedSensorUpdateBuilds', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryCombinedSensorUpdatePolicyMembers

Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **id** | query | _string_ | The ID of the Sensor Update Policy to search for members of |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'id': 'string',
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.queryCombinedSensorUpdatePolicyMembers(parameters=PARAMS)
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
    'id': 'string',
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('queryCombinedSensorUpdatePolicyMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryCombinedSensorUpdatePolicies

Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.queryCombinedSensorUpdatePolicies(parameters=PARAMS)
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
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('queryCombinedSensorUpdatePolicies', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryCombinedSensorUpdatePoliciesV2

Search for Sensor Update Policies with additional support for uninstall protection in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policies which match the filter criteria

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.queryCombinedSensorUpdatePoliciesV2(parameters=PARAMS)
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
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('queryCombinedSensorUpdatePoliciesV2', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### performSensorUpdatePoliciesAction

Perform the specified action on the Sensor Update Policies specified in the request

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **action\_name** | query | _string_ | The action to perform |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'action_name': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.performSensorUpdatePoliciesAction(parameters=PARAMS, body=BODY)
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

response = falcon.command('performSensorUpdatePoliciesAction', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```

### setSensorUpdatePoliciesPrecedence

Sets the precedence of Sensor Update Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.setSensorUpdatePoliciesPrecedence(body=BODY)
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

response = falcon.command('setSensorUpdatePoliciesPrecedence', body=BODY)
print(response)
falcon.deauthenticate()
```

### getSensorUpdatePolicies

Retrieve a set of Sensor Update Policies by specifying their IDs

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the Sensor Update Policies to return |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.getSensorUpdatePolicies(ids=IDS)
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

response = falcon.command('getSensorUpdatePolicies', ids=IDS)
print(response)
falcon.deauthenticate()
```

### createSensorUpdatePolicies

Create Sensor Update Policies by specifying details about the policy to create

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.createSensorUpdatePolicies(body=BODY)
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

response = falcon.command('createSensorUpdatePolicies', body=BODY)
print(response)
falcon.deauthenticate()
```

### deleteSensorUpdatePolicies

Delete a set of Sensor Update Policies by specifying their IDs

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the Sensor Update Policies to delete |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.deleteSensorUpdatePolicies(ids=IDS)
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

response = falcon.command('deleteSensorUpdatePolicies', ids=IDS)
print(response)
falcon.deauthenticate()
```

### updateSensorUpdatePolicies

Update Sensor Update Policies by specifying the ID of the policy and details to update

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.updateSensorUpdatePolicies(body=BODY)
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

response = falcon.command('updateSensorUpdatePolicies', body=BODY)
print(response)
falcon.deauthenticate()
```

### getSensorUpdatePoliciesV2

Retrieve a set of Sensor Update Policies with additional support for uninstall protection by specifying their IDs

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the Sensor Update Policies to return |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.getSensorUpdatePoliciesV2(ids=IDS)
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

response = falcon.command('getSensorUpdatePoliciesV2', ids=IDS)
print(response)
falcon.deauthenticate()
```

### createSensorUpdatePoliciesV2

Create Sensor Update Policies by specifying details about the policy to create with additional support for uninstall protection

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.createSensorUpdatePoliciesV2(body=BODY)
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

response = falcon.command('createSensorUpdatePoliciesV2', body=BODY)
print(response)
falcon.deauthenticate()
```

### updateSensorUpdatePoliciesV2

Update Sensor Update Policies by specifying the ID of the policy and details to update with additional support for uninstall protection

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.updateSensorUpdatePoliciesV2(body=BODY)
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

response = falcon.command('updateSensorUpdatePoliciesV2', body=BODY)
print(response)
falcon.deauthenticate()
```

### querySensorUpdatePolicyMembers

Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **id** | query | _string_ | The ID of the Sensor Update Policy to search for members of |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'id': 'string',
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.querySensorUpdatePolicyMembers(parameters=PARAMS)
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
    'id': 'string',
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('querySensorUpdatePolicyMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### querySensorUpdatePolicies

Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policy IDs which match the filter criteria

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by |

**Usage**

**Service class example**

```python
from falconpy import sensor_update_policies as FalconSUP

falcon = FalconSUP.Sensor_Update_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.querySensorUpdatePolicies(parameters=PARAMS)
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
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('querySensorUpdatePolicies', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

