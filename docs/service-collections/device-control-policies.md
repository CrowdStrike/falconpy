# Device Control Policies

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Device Control Policies service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [queryCombinedDeviceControlPolicyMembers](device-control-policies.md#querycombineddevicecontrolpolicymembers) | Search for members of a Device Control Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedDeviceControlPolicies](device-control-policies.md#querycombineddevicecontrolpolicies) | Search for Device Control Policies in your environment by providing an FQL filter and paging details. Returns a set of Device Control Policies which match the filter criteria |
| [performDeviceControlPoliciesAction](device-control-policies.md#performdevicecontrolpoliciesaction) | Perform the specified action on the Device Control Policies specified in the request |
| [setDeviceControlPoliciesPrecedence](device-control-policies.md#setdevicecontrolpoliciesprecedence) | Sets the precedence of Device Control Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence |
| [getDeviceControlPolicies](device-control-policies.md#getdevicecontrolpolicies) | Retrieve a set of Device Control Policies by specifying their IDs |
| [createDeviceControlPolicies](device-control-policies.md#createdevicecontrolpolicies) | Create Device Control Policies by specifying details about the policy to create |
| [deleteDeviceControlPolicies](device-control-policies.md#deletedevicecontrolpolicies) | Delete a set of Device Control Policies by specifying their IDs |
| [updateDeviceControlPolicies](device-control-policies.md#updatedevicecontrolpolicies) | Update Device Control Policies by specifying the ID of the policy and details to update |
| [queryDeviceControlPolicyMembers](device-control-policies.md#querydevicecontrolpolicymembers) | Search for members of a Device Control Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [queryDeviceControlPolicies](device-control-policies.md#querydevicecontrolpolicies) | Search for Device Control Policies in your environment by providing an FQL filter and paging details. Returns a set of Device Control Policy IDs which match the filter criteria |

### queryCombinedDeviceControlPolicyMembers

Search for members of a Device Control Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **id** | query | _string_ | The ID of the Device Control Policy to search for members of |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by |

**Usage**

**Service class example**

```python
from falconpy import device_control_policies as FalconDCP

falcon = FalconDCP.Device_Control_Policies(creds={
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

response = falcon.queryCombinedDeviceControlPolicyMembers(parameters=PARAMS)
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

response = falcon.command('queryCombinedDeviceControlPolicyMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryCombinedDeviceControlPolicies

Search for Device Control Policies in your environment by providing an FQL filter and paging details. Returns a set of Device Control Policies which match the filter criteria

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
from falconpy import device_control_policies as FalconDCP

falcon = FalconDCP.Device_Control_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.queryCombinedDeviceControlPolicies(parameters=PARAMS)
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

response = falcon.command('queryCombinedDeviceControlPolicies', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### performDeviceControlPoliciesAction

Perform the specified action on the Device Control Policies specified in the request

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
from falconpy import device_control_policies as FalconDCP

falcon = FalconDCP.Device_Control_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'action_name': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.performDeviceControlPoliciesAction(parameters=PARAMS, body=BODY)
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

response = falcon.command('performDeviceControlPoliciesAction', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```

### setDeviceControlPoliciesPrecedence

Sets the precedence of Device Control Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import device_control_policies as FalconDCP

falcon = FalconDCP.Device_Control_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.setDeviceControlPoliciesPrecedence(body=BODY)
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

response = falcon.command('setDeviceControlPoliciesPrecedence', body=BODY)
print(response)
falcon.deauthenticate()
```

### getDeviceControlPolicies

Retrieve a set of Device Control Policies by specifying their IDs

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the Device Control Policies to return |

**Usage**

**Service class example**

```python
from falconpy import device_control_policies as FalconDCP

falcon = FalconDCP.Device_Control_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.getDeviceControlPolicies(ids=IDS)
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

response = falcon.command('getDeviceControlPolicies', ids=IDS)
print(response)
falcon.deauthenticate()
```

### createDeviceControlPolicies

Create Device Control Policies by specifying details about the policy to create

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import device_control_policies as FalconDCP

falcon = FalconDCP.Device_Control_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.createDeviceControlPolicies(body=BODY)
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

response = falcon.command('createDeviceControlPolicies', body=BODY)
print(response)
falcon.deauthenticate()
```

### deleteDeviceControlPolicies

Delete a set of Device Control Policies by specifying their IDs

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the Device Control Policies to delete |

**Usage**

**Service class example**

```python
from falconpy import device_control_policies as FalconDCP

falcon = FalconDCP.Device_Control_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.deleteDeviceControlPolicies(ids=IDS)
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

response = falcon.command('deleteDeviceControlPolicies', ids=IDS)
print(response)
falcon.deauthenticate()
```

### updateDeviceControlPolicies

Update Device Control Policies by specifying the ID of the policy and details to update

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import device_control_policies as FalconDCP

falcon = FalconDCP.Device_Control_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.updateDeviceControlPolicies(body=BODY)
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

response = falcon.command('updateDeviceControlPolicies', body=BODY)
print(response)
falcon.deauthenticate()
```

### queryDeviceControlPolicyMembers

Search for members of a Device Control Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **id** | query | _string_ | The ID of the Device Control Policy to search for members of |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by |

**Usage**

**Service class example**

```python
from falconpy import device_control_policies as FalconDCP

falcon = FalconDCP.Device_Control_Policies(creds={
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

response = falcon.queryDeviceControlPolicyMembers(parameters=PARAMS)
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

response = falcon.command('queryDeviceControlPolicyMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryDeviceControlPolicies

Search for Device Control Policies in your environment by providing an FQL filter and paging details. Returns a set of Device Control Policy IDs which match the filter criteria

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
from falconpy import device_control_policies as FalconDCP

falcon = FalconDCP.Device_Control_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.queryDeviceControlPolicies(parameters=PARAMS)
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

response = falcon.command('queryDeviceControlPolicies', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

