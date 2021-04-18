# Prevention Policies

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Prevention Policies service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [queryCombinedPreventionPolicyMembers](prevention-policies.md#querycombinedpreventionpolicymembers) | Search for members of a Prevention Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedPreventionPolicies](prevention-policies.md#querycombinedpreventionpolicies) | Search for Prevention Policies in your environment by providing an FQL filter and paging details. Returns a set of Prevention Policies which match the filter criteria |
| [performPreventionPoliciesAction](prevention-policies.md#performpreventionpoliciesaction) | Perform the specified action on the Prevention Policies specified in the request |
| [setPreventionPoliciesPrecedence](prevention-policies.md#setpreventionpoliciesprecedence) | Sets the precedence of Prevention Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence |
| [getPreventionPolicies](prevention-policies.md#getpreventionpolicies) | Retrieve a set of Prevention Policies by specifying their IDs |
| [createPreventionPolicies](prevention-policies.md#createpreventionpolicies) | Create Prevention Policies by specifying details about the policy to create |
| [deletePreventionPolicies](prevention-policies.md#deletepreventionpolicies) | Delete a set of Prevention Policies by specifying their IDs |
| [updatePreventionPolicies](prevention-policies.md#updatepreventionpolicies) | Update Prevention Policies by specifying the ID of the policy and details to update |
| [queryPreventionPolicyMembers](prevention-policies.md#querypreventionpolicymembers) | Search for members of a Prevention Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [queryPreventionPolicies](prevention-policies.md#querypreventionpolicies) | Search for Prevention Policies in your environment by providing an FQL filter and paging details. Returns a set of Prevention Policy IDs which match the filter criteria |

### queryCombinedPreventionPolicyMembers

Search for members of a Prevention Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **id** | query | _string_ | The ID of the Prevention Policy to search for members of |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by |

**Usage**

**Service class example**

```python
from falconpy import prevention_policies as FalconPP

falcon = FalconPP.Prevention_Policy(creds={
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

response = falcon.queryCombinedPreventionPolicyMembers(parameters=PARAMS)
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

response = falcon.command('queryCombinedPreventionPolicyMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryCombinedPreventionPolicies

Search for Prevention Policies in your environment by providing an FQL filter and paging details. Returns a set of Prevention Policies which match the filter criteria

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
from falconpy import prevention_policies as FalconPP

falcon = FalconPP.Prevention_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.queryCombinedPreventionPolicies(parameters=PARAMS)
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

response = falcon.command('queryCombinedPreventionPolicies', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### performPreventionPoliciesAction

Perform the specified action on the Prevention Policies specified in the request

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
from falconpy import prevention_policies as FalconPP

falcon = FalconPP.Prevention_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'action_name': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.performPreventionPoliciesAction(parameters=PARAMS, body=BODY)
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

response = falcon.command('performPreventionPoliciesAction', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```

### setPreventionPoliciesPrecedence

Sets the precedence of Prevention Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import prevention_policies as FalconPP

falcon = FalconPP.Prevention_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.setPreventionPoliciesPrecedence(body=BODY)
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

response = falcon.command('setPreventionPoliciesPrecedence', body=BODY)
print(response)
falcon.deauthenticate()
```

### getPreventionPolicies

Retrieve a set of Prevention Policies by specifying their IDs

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the Prevention Policies to return |

**Usage**

**Service class example**

```python
from falconpy import prevention_policies as FalconPP

falcon = FalconPP.Prevention_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.getPreventionPolicies(ids=IDS)
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

response = falcon.command('getPreventionPolicies', ids=IDS)
print(response)
falcon.deauthenticate()
```

### createPreventionPolicies

Create Prevention Policies by specifying details about the policy to create

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import prevention_policies as FalconPP

falcon = FalconPP.Prevention_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.createPreventionPolicies(body=BODY)
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

response = falcon.command('createPreventionPolicies', body=BODY)
print(response)
falcon.deauthenticate()
```

### deletePreventionPolicies

Delete a set of Prevention Policies by specifying their IDs

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the Prevention Policies to delete |

**Usage**

**Service class example**

```python
from falconpy import prevention_policies as FalconPP

falcon = FalconPP.Prevention_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.deletePreventionPolicies(ids=IDS)
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

response = falcon.command('deletePreventionPolicies', ids=IDS)
print(response)
falcon.deauthenticate()
```

### updatePreventionPolicies

Update Prevention Policies by specifying the ID of the policy and details to update

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import prevention_policies as FalconPP

falcon = FalconPP.Prevention_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.updatePreventionPolicies(body=BODY)
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

response = falcon.command('updatePreventionPolicies', body=BODY)
print(response)
falcon.deauthenticate()
```

### queryPreventionPolicyMembers

Search for members of a Prevention Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **id** | query | _string_ | The ID of the Prevention Policy to search for members of |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by |

**Usage**

**Service class example**

```python
from falconpy import prevention_policies as FalconPP

falcon = FalconPP.Prevention_Policy(creds={
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

response = falcon.queryPreventionPolicyMembers(parameters=PARAMS)
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

response = falcon.command('queryPreventionPolicyMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryPreventionPolicies

Search for Prevention Policies in your environment by providing an FQL filter and paging details. Returns a set of Prevention Policy IDs which match the filter criteria

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
from falconpy import prevention_policies as FalconPP

falcon = FalconPP.Prevention_Policy(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.queryPreventionPolicies(parameters=PARAMS)
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

response = falcon.command('queryPreventionPolicies', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

