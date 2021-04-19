# Firewall Management

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Firewall Management service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [aggregate\_events](firewall-management.md#aggregate_events) | Aggregate events for customer |
| [aggregate\_policy\_rules](firewall-management.md#aggregate_policy_rules) | Aggregate rules within a policy for customer |
| [aggregate\_rule\_groups](firewall-management.md#aggregate_rule_groups) | Aggregate rule groups for customer |
| [aggregate\_rules](firewall-management.md#aggregate_rules) | Aggregate rules for customer |
| [get\_events](firewall-management.md#get_events) | Get events entities by ID and optionally version |
| [get\_firewall\_fields](firewall-management.md#get_firewall_fields) | Get the firewall field specifications by ID |
| [get\_platforms](firewall-management.md#get_platforms) | Get platforms by ID, e.g., windows or mac or droid |
| [get\_policy\_containers](firewall-management.md#get_policy_containers) | Get policy container entities by policy ID |
| [update\_policy\_container](firewall-management.md#update_policy_container) | Update an identified policy container |
| [get\_rule\_groups](firewall-management.md#get_rule_groups) | Get rule group entities by ID. These groups do not contain their rule entites, just the rule IDs in precedence order. |
| [create\_rule\_group](firewall-management.md#create_rule_group) | Create new rule group on a platform for a customer with a name and description, and return the ID |
| [delete\_rule\_groups](firewall-management.md#delete_rule_groups) | Delete rule group entities by ID |
| [update\_rule\_group](firewall-management.md#update_rule_group) | Update name, description, or enabled status of a rule group, or create, edit, delete, or reorder rules |
| [get\_rules](firewall-management.md#get_rules) | Get rule entities by ID \(64-bit unsigned int as decimal string\) or Family ID \(32-character hexadecimal string\) |
| [query\_events](firewall-management.md#query_events) | Find all event IDs matching the query with filter |
| [query\_firewall\_fields](firewall-management.md#query_firewall_fields) | Get the firewall field specification IDs for the provided platform |
| [query\_platforms](firewall-management.md#query_platforms) | Get the list of platform names |
| [query\_policy\_rules](firewall-management.md#query_policy_rules) | Find all firewall rule IDs matching the query with filter, and return them in precedence order |
| [query\_rule\_groups](firewall-management.md#query_rule_groups) | Find all rule group IDs matching the query with filter |
| [query\_rules](firewall-management.md#query_rules) | Find all rule IDs matching the query with filter |

### aggregate\_events

Aggregate events for customer

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ | Query criteria and settings |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.aggregate_events(body=BODY)
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

response = falcon.command('aggregate-events', body=BODY)
print(response)
falcon.deauthenticate()
```

### aggregate\_policy\_rules

Aggregate rules within a policy for customer

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ | Query criteria and settings |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.aggregate_policy_rules(body=BODY)
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

response = falcon.command('aggregate-policy-rules', body=BODY)
print(response)
falcon.deauthenticate()
```

### aggregate\_rule\_groups

Aggregate rule groups for customer

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ | Query criteria and settings |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.aggregate_rule_groups(body=BODY)
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

response = falcon.command('aggregate-rule-groups', body=BODY)
print(response)
falcon.deauthenticate()
```

### aggregate\_rules

Aggregate rules for customer

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ | Query criteria and settings |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.aggregate_rules(body=BODY)
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

response = falcon.command('aggregate-rules', body=BODY)
print(response)
falcon.deauthenticate()
```

### get\_events

Get events entities by ID and optionally version

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The events to retrieve, identified by ID |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.get_events(ids=IDS)
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

response = falcon.command('get-events', ids=IDS)
print(response)
falcon.deauthenticate()
```

### get\_firewall\_fields

Get the firewall field specifications by ID

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the rule types to retrieve |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.get_firewall_fields(ids=IDS)
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

response = falcon.command('get-firewall-fields', ids=IDS)
print(response)
falcon.deauthenticate()
```

### get\_platforms

Get platforms by ID, e.g., windows or mac or droid

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the platforms to retrieve |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.get_platforms(ids=IDS)
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

response = falcon.command('get-platforms', ids=IDS)
print(response)
falcon.deauthenticate()
```

### get\_policy\_containers

Get policy container entities by policy ID

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The policy container\(s\) to retrieve, identified by policy ID |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.get_policy_containers(ids=IDS)
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

response = falcon.command('get-policy-containers', ids=IDS)
print(response)
falcon.deauthenticate()
```

### update\_policy\_container

Update an identified policy container

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **X-CS-USERNAME** | header | _string_ | The user id |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

HEADERS = {
    'X-CS-USERNAME': 'string'
}

response = falcon.update_policy_container(body=BODY, headers=HEADERS)
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

HEADERS = {
    'X-CS-USERNAME': 'string'
}

response = falcon.command('update-policy-container', body=BODY, headers=HEADERS)
print(response)
falcon.deauthenticate()
```

### get\_rule\_groups

Get rule group entities by ID. These groups do not contain their rule entites, just the rule IDs in precedence order.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the rule groups to retrieve |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.get_rule_groups(ids=IDS)
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

response = falcon.command('get-rule-groups', ids=IDS)
print(response)
falcon.deauthenticate()
```

### create\_rule\_group

Create new rule group on a platform for a customer with a name and description, and return the ID

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **X-CS-USERNAME** | header | _string_ | The user id |
|  | **clone\_id** | query | _string_ | A rule group ID from which to copy rules. If this is provided then the 'rules' property of the body is ignored. |
|  | **library** | query | _string_ | If this flag is set to true then the rules will be cloned from the clone\_id from the CrowdStrike Firewall Rule Groups Library. |
|  | **comment** | query | _string_ | Audit log comment for this action |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'clone_id': 'string',
    'library': 'string',
    'comment': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

HEADERS = {
    'X-CS-USERNAME': 'string'
}

response = falcon.create_rule_group(parameters=PARAMS, body=BODY, headers=HEADERS)
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
    'clone_id': 'string',
    'library': 'string',
    'comment': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

HEADERS = {
    'X-CS-USERNAME': 'string'
}

response = falcon.command('create-rule-group', parameters=PARAMS, body=BODY, headers=HEADERS)
print(response)
falcon.deauthenticate()
```

### delete\_rule\_groups

Delete rule group entities by ID

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **X-CS-USERNAME** | header | _string_ | The user id |
| ✅ | **ids** | query | array \(_string_\) | The IDs of the rule groups to be deleted |
|  | **comment** | query | _string_ | Audit log comment for this action |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'comment': 'string'
}

HEADERS = {
    'X-CS-USERNAME': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.delete_rule_groups(parameters=PARAMS, headers=HEADERS, ids=IDS)
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
    'comment': 'string'
}

HEADERS = {
    'X-CS-USERNAME': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('delete-rule-groups', parameters=PARAMS, headers=HEADERS, ids=IDS)
print(response)
falcon.deauthenticate()
```

### update\_rule\_group

Update name, description, or enabled status of a rule group, or create, edit, delete, or reorder rules

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **X-CS-USERNAME** | header | _string_ | The user id |
|  | **comment** | query | _string_ | Audit log comment for this action |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'comment': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

HEADERS = {
    'X-CS-USERNAME': 'string'
}

response = falcon.update_rule_group(parameters=PARAMS, body=BODY, headers=HEADERS)
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
    'comment': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

HEADERS = {
    'X-CS-USERNAME': 'string'
}

response = falcon.command('update-rule-group', parameters=PARAMS, body=BODY, headers=HEADERS)
print(response)
falcon.deauthenticate()
```

### get\_rules

Get rule entities by ID \(64-bit unsigned int as decimal string\) or Family ID \(32-character hexadecimal string\)

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | The rules to retrieve, identified by ID |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.get_rules(ids=IDS)
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

response = falcon.command('get-rules', ids=IDS)
print(response)
falcon.deauthenticate()
```

### query\_events

Find all event IDs matching the query with filter

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **sort** | query | _string_ | Possible order by fields: |
|  | **filter** | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: enabled, platform, name, description, etc TODO. Filter range criteria: created\_on, modified\_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
|  | **q** | query | _string_ | Match query criteria, which includes all the filter string fields, plus TODO |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |
|  | **after** | query | _string_ | A pagination token used with the `limit` parameter to manage pagination of results. On your first request, don't provide an `after` token. On subsequent requests, provide the `after` token from the previous response to continue from that place in the results. |
|  | **limit** | query | _integer_ | Number of ids to return. |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'sort': 'string',
    'filter': 'string',
    'q': 'string',
    'offset': 'string',
    'after': 'string',
    'limit': integer
}

response = falcon.query_events(parameters=PARAMS)
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
    'sort': 'string',
    'filter': 'string',
    'q': 'string',
    'offset': 'string',
    'after': 'string',
    'limit': integer
}

response = falcon.command('query-events', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### query\_firewall\_fields

Get the firewall field specification IDs for the provided platform

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **platform\_id** | query | _string_ | Get fields configuration for this platform |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |
|  | **limit** | query | _integer_ | Number of ids to return. |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'platform_id': 'string',
    'offset': 'string',
    'limit': integer
}

response = falcon.query_firewall_fields(parameters=PARAMS)
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
    'platform_id': 'string',
    'offset': 'string',
    'limit': integer
}

response = falcon.command('query-firewall-fields', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### query\_platforms

Get the list of platform names

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |
|  | **limit** | query | _integer_ | Number of ids to return. |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'offset': 'string',
    'limit': integer
}

response = falcon.query_platforms(parameters=PARAMS)
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
    'limit': integer
}

response = falcon.command('query-platforms', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### query\_policy\_rules

Find all firewall rule IDs matching the query with filter, and return them in precedence order

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **id** | query | _string_ | The ID of the policy container within which to query |
|  | **sort** | query | _string_ | Possible order by fields: |
|  | **filter** | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: enabled, platform, name, description, etc TODO. Filter range criteria: created\_on, modified\_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
|  | **q** | query | _string_ | Match query criteria, which includes all the filter string fields, plus TODO |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |
|  | **limit** | query | _integer_ | Number of ids to return. |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'id': 'string',
    'sort': 'string',
    'filter': 'string',
    'q': 'string',
    'offset': 'string',
    'limit': integer
}

response = falcon.query_policy_rules(parameters=PARAMS)
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
    'sort': 'string',
    'filter': 'string',
    'q': 'string',
    'offset': 'string',
    'limit': integer
}

response = falcon.command('query-policy-rules', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### query\_rule\_groups

Find all rule group IDs matching the query with filter

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **sort** | query | _string_ | Possible order by fields: |
|  | **filter** | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: enabled, platform, name, description, etc TODO. Filter range criteria: created\_on, modified\_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
|  | **q** | query | _string_ | Match query criteria, which includes all the filter string fields, plus TODO |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |
|  | **after** | query | _string_ | A pagination token used with the `limit` parameter to manage pagination of results. On your first request, don't provide an `after` token. On subsequent requests, provide the `after` token from the previous response to continue from that place in the results. |
|  | **limit** | query | _integer_ | Number of ids to return. |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'sort': 'string',
    'filter': 'string',
    'q': 'string',
    'offset': 'string',
    'after': 'string',
    'limit': integer
}

response = falcon.query_rule_groups(parameters=PARAMS)
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
    'sort': 'string',
    'filter': 'string',
    'q': 'string',
    'offset': 'string',
    'after': 'string',
    'limit': integer
}

response = falcon.command('query-rule-groups', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### query\_rules

Find all rule IDs matching the query with filter

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **sort** | query | _string_ | Possible order by fields: |
|  | **filter** | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: enabled, platform, name, description, etc TODO. Filter range criteria: created\_on, modified\_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
|  | **q** | query | _string_ | Match query criteria, which includes all the filter string fields, plus TODO |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |
|  | **after** | query | _string_ | A pagination token used with the `limit` parameter to manage pagination of results. On your first request, don't provide an `after` token. On subsequent requests, provide the `after` token from the previous response to continue from that place in the results. |
|  | **limit** | query | _integer_ | Number of ids to return. |

**Usage**

**Service class example**

```python
from falconpy import firewall_management as FalconFM

falcon = FalconFM.Firewall_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'sort': 'string',
    'filter': 'string',
    'q': 'string',
    'offset': 'string',
    'after': 'string',
    'limit': integer
}

response = falcon.query_rules(parameters=PARAMS)
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
    'sort': 'string',
    'filter': 'string',
    'q': 'string',
    'offset': 'string',
    'after': 'string',
    'limit': integer
}

response = falcon.command('query-rules', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

