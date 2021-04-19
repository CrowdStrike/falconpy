# Firewall Policies

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Firewall Policies service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [queryCombinedFirewallPolicyMembers](firewall-policies.md#querycombinedfirewallpolicymembers) | Search for members of a Firewall Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria |
| [queryCombinedFirewallPolicies](firewall-policies.md#querycombinedfirewallpolicies) | Search for Firewall Policies in your environment by providing an FQL filter and paging details. Returns a set of Firewall Policies which match the filter criteria |
| [performFirewallPoliciesAction](firewall-policies.md#performfirewallpoliciesaction) | Perform the specified action on the Firewall Policies specified in the request |
| [setFirewallPoliciesPrecedence](firewall-policies.md#setfirewallpoliciesprecedence) | Sets the precedence of Firewall Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence |
| [getFirewallPolicies](firewall-policies.md#getfirewallpolicies) | Retrieve a set of Firewall Policies by specifying their IDs |
| [createFirewallPolicies](firewall-policies.md#createfirewallpolicies) | Create Firewall Policies by specifying details about the policy to create |
| [deleteFirewallPolicies](firewall-policies.md#deletefirewallpolicies) | Delete a set of Firewall Policies by specifying their IDs |
| [updateFirewallPolicies](firewall-policies.md#updatefirewallpolicies) | Update Firewall Policies by specifying the ID of the policy and details to update |
| [queryFirewallPolicyMembers](firewall-policies.md#queryfirewallpolicymembers) | Search for members of a Firewall Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria |
| [queryFirewallPolicies](firewall-policies.md#queryfirewallpolicies) | Search for Firewall Policies in your environment by providing an FQL filter and paging details. Returns a set of Firewall Policy IDs which match the filter criteria |

### queryCombinedFirewallPolicyMembers

Search for members of a Firewall Policy in your environment by providing an FQL filter and paging details. Returns a set of host details which match the filter criteria

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **id** | query | _string_ | The ID of the Firewall Policy to search for members of |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by |

**Usage**

**Service class example**

```python
from falconpy import firewall_policies as FalconFP

falcon = FalconFP.Firewall_Policies(creds={
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

response = falcon.queryCombinedFirewallPolicyMembers(parameters=PARAMS)
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

response = falcon.command('queryCombinedFirewallPolicyMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryCombinedFirewallPolicies

Search for Firewall Policies in your environment by providing an FQL filter and paging details. Returns a set of Firewall Policies which match the filter criteria

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
from falconpy import firewall_policies as FalconFP

falcon = FalconFP.Firewall_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.queryCombinedFirewallPolicies(parameters=PARAMS)
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

response = falcon.command('queryCombinedFirewallPolicies', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### performFirewallPoliciesAction

Perform the specified action on the Firewall Policies specified in the request

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
from falconpy import firewall_policies as FalconFP

falcon = FalconFP.Firewall_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'action_name': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.performFirewallPoliciesAction(parameters=PARAMS, body=BODY)
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

response = falcon.command('performFirewallPoliciesAction', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```

### setFirewallPoliciesPrecedence

Sets the precedence of Firewall Policies based on the order of IDs specified in the request. The first ID specified will have the highest precedence and the last ID specified will have the lowest. You must specify all non-Default Policies for a platform when updating precedence

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import firewall_policies as FalconFP

falcon = FalconFP.Firewall_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.setFirewallPoliciesPrecedence(body=BODY)
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

response = falcon.command('setFirewallPoliciesPrecedence', body=BODY)
print(response)
falcon.deauthenticate()
```

### getFirewallPolicies

Retrieve a set of Firewall Policies by specifying their IDs

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the Firewall Policies to return |

**Usage**

**Service class example**

```python
from falconpy import firewall_policies as FalconFP

falcon = FalconFP.Firewall_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.getFirewallPolicies(ids=IDS)
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

response = falcon.command('getFirewallPolicies', ids=IDS)
print(response)
falcon.deauthenticate()
```

### createFirewallPolicies

Create Firewall Policies by specifying details about the policy to create

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |
|  | **clone\_id** | query | _string_ | The policy ID to be cloned from |

**Usage**

**Service class example**

```python
from falconpy import firewall_policies as FalconFP

falcon = FalconFP.Firewall_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'clone_id': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.createFirewallPolicies(parameters=PARAMS, body=BODY)
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
    'clone_id': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.command('createFirewallPolicies', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```

### deleteFirewallPolicies

Delete a set of Firewall Policies by specifying their IDs

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the Firewall Policies to delete |

**Usage**

**Service class example**

```python
from falconpy import firewall_policies as FalconFP

falcon = FalconFP.Firewall_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.deleteFirewallPolicies(ids=IDS)
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

response = falcon.command('deleteFirewallPolicies', ids=IDS)
print(response)
falcon.deauthenticate()
```

### updateFirewallPolicies

Update Firewall Policies by specifying the ID of the policy and details to update

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import firewall_policies as FalconFP

falcon = FalconFP.Firewall_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.updateFirewallPolicies(body=BODY)
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

response = falcon.command('updateFirewallPolicies', body=BODY)
print(response)
falcon.deauthenticate()
```

### queryFirewallPolicyMembers

Search for members of a Firewall Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **id** | query | _string_ | The ID of the Firewall Policy to search for members of |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-5000\] |
|  | **sort** | query | _string_ | The property to sort by |

**Usage**

**Service class example**

```python
from falconpy import firewall_policies as FalconFP

falcon = FalconFP.Firewall_Policies(creds={
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

response = falcon.queryFirewallPolicyMembers(parameters=PARAMS)
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

response = falcon.command('queryFirewallPolicyMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryFirewallPolicies

Search for Firewall Policies in your environment by providing an FQL filter and paging details. Returns a set of Firewall Policy IDs which match the filter criteria

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
from falconpy import firewall_policies as FalconFP

falcon = FalconFP.Firewall_Policies(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'filter': 'string',
    'offset': integer,
    'limit': integer,
    'sort': 'string'
}

response = falcon.queryFirewallPolicies(parameters=PARAMS)
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

response = falcon.command('queryFirewallPolicies', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

