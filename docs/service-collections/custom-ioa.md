# Custom IOA

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Custom IOA service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [get\_patterns](custom-ioa.md#get_patterns) | Get pattern severities by ID. |
| [get\_platformsMixin0](custom-ioa.md#get_platformsmixin0) | Get platforms by ID. |
| [get\_rule\_groupsMixin0](custom-ioa.md#get_rule_groupsmixin0) | Get rule groups by ID. |
| [create\_rule\_groupMixin0](custom-ioa.md#create_rule_groupmixin0) | Create a rule group for a platform with a name and an optional description. Returns the rule group. |
| [delete\_rule\_groupsMixin0](custom-ioa.md#delete_rule_groupsmixin0) | Delete rule groups by ID. |
| [update\_rule\_groupMixin0](custom-ioa.md#update_rule_groupmixin0) | Update a rule group. The following properties can be modified: name, description, enabled. |
| [get\_rule\_types](custom-ioa.md#get_rule_types) | Get rule types by ID. |
| [get\_rules\_get](custom-ioa.md#get_rules_get) | Get rules by ID and optionally version in the following format: `ID[:version]`. |
| [get\_rulesMixin0](custom-ioa.md#get_rulesmixin0) | Get rules by ID and optionally version in the following format: `ID[:version]`. The max number of IDs is constrained by URL size. |
| [create\_rule](custom-ioa.md#create_rule) | Create a rule within a rule group. Returns the rule. |
| [delete\_rules](custom-ioa.md#delete_rules) | Delete rules from a rule group by ID. |
| [update\_rules](custom-ioa.md#update_rules) | Update rules within a rule group. Return the updated rules. |
| [validate](custom-ioa.md#validate) | Validates field values and checks for matches if a test string is provided. |
| [query\_patterns](custom-ioa.md#query_patterns) | Get all pattern severity IDs. |
| [query\_platformsMixin0](custom-ioa.md#query_platformsmixin0) | Get all platform IDs. |
| [query\_rule\_groups\_full](custom-ioa.md#query_rule_groups_full) | Find all rule groups matching the query with optional filter. |
| [query\_rule\_groupsMixin0](custom-ioa.md#query_rule_groupsmixin0) | Finds all rule group IDs matching the query with optional filter. |
| [query\_rule\_types](custom-ioa.md#query_rule_types) | Get all rule type IDs. |
| [query\_rulesMixin0](custom-ioa.md#query_rulesmixin0) | Finds all rule IDs matching the query with optional filter. |

### get\_patterns

Get pattern severities by ID.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | The IDs of the entities |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.get_patterns(ids=IDS)
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

response = falcon.command('get-patterns', ids=IDS)
print(response)
falcon.deauthenticate()
```

### get\_platformsMixin0

Get platforms by ID.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | The IDs of the entities |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.get_platformsMixin0(ids=IDS)
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

response = falcon.command('get-platformsMixin0', ids=IDS)
print(response)
falcon.deauthenticate()
```

### get\_rule\_groupsMixin0

Get rule groups by ID.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | The IDs of the entities |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.get_rule_groupsMixin0(ids=IDS)
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

response = falcon.command('get-rule-groupsMixin0', ids=IDS)
print(response)
falcon.deauthenticate()
```

### create\_rule\_groupMixin0

Create a rule group for a platform with a name and an optional description. Returns the rule group.

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
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.create_rule_groupMixin0(body=BODY)
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

response = falcon.command('create-rule-groupMixin0', body=BODY)
print(response)
falcon.deauthenticate()
```

### delete\_rule\_groupsMixin0

Delete rule groups by ID.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **comment** | query | _string_ | Explains why the entity is being deleted |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | The IDs of the entities |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'comment': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.delete_rule_groupsMixin0(parameters=PARAMS, ids=IDS)
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

IDS = 'ID1,ID2,ID3'

response = falcon.command('delete-rule-groupsMixin0', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```

### update\_rule\_groupMixin0

Update a rule group. The following properties can be modified: name, description, enabled.

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
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.update_rule_groupMixin0(body=BODY)
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

response = falcon.command('update-rule-groupMixin0', body=BODY)
print(response)
falcon.deauthenticate()
```

### get\_rule\_types

Get rule types by ID.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | The IDs of the entities |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.get_rule_types(ids=IDS)
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

response = falcon.command('get-rule-types', ids=IDS)
print(response)
falcon.deauthenticate()
```

### get\_rules\_get

Get rules by ID and optionally version in the following format: `ID[:version]`.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ | The "ids" field contains a list of the rules to retrieve. |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.get_rules_get(body=BODY)
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

response = falcon.command('get-rules-get', body=BODY)
print(response)
falcon.deauthenticate()
```

### get\_rulesMixin0

Get rules by ID and optionally version in the following format: `ID[:version]`. The max number of IDs is constrained by URL size.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | The IDs of the entities |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.get_rulesMixin0(ids=IDS)
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

response = falcon.command('get-rulesMixin0', ids=IDS)
print(response)
falcon.deauthenticate()
```

### create\_rule

Create a rule within a rule group. Returns the rule.

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
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.create_rule(body=BODY)
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

response = falcon.command('create-rule', body=BODY)
print(response)
falcon.deauthenticate()
```

### delete\_rules

Delete rules from a rule group by ID.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **rule\_group\_id** | query | _string_ | The parent rule group |
|  | **comment** | query | _string_ | Explains why the entity is being deleted |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | The IDs of the entities |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'rule_group_id': 'string',
    'comment': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.delete_rules(parameters=PARAMS, ids=IDS)
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
    'rule_group_id': 'string',
    'comment': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('delete-rules', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```

### update\_rules

Update rules within a rule group. Return the updated rules.

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
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.update_rules(body=BODY)
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

response = falcon.command('update-rules', body=BODY)
print(response)
falcon.deauthenticate()
```

### validate

Validates field values and checks for matches if a test string is provided.

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
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.validate(body=BODY)
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

response = falcon.command('validate', body=BODY)
print(response)
falcon.deauthenticate()
```

### query\_patterns

Get all pattern severity IDs.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return IDs |
|  | **limit** | query | _integer_ | Number of IDs to return |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'offset': 'string',
    'limit': integer
}

response = falcon.query_patterns(parameters=PARAMS)
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

response = falcon.command('query-patterns', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### query\_platformsMixin0

Get all platform IDs.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return IDs |
|  | **limit** | query | _integer_ | Number of IDs to return |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'offset': 'string',
    'limit': integer
}

response = falcon.query_platformsMixin0(parameters=PARAMS)
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

response = falcon.command('query-platformsMixin0', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### query\_rule\_groups\_full

Find all rule groups matching the query with optional filter.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **sort** | query | _string_ | Possible order by fields: {created\_by, created\_on, modified\_by, modified\_on, enabled, name, description} |
|  | **filter** | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: \[enabled platform name description rules.action\_label rules.name rules.description rules.pattern\_severity rules.ruletype\_name rules.enabled\]. Filter range criteria: created\_on, modified\_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
|  | **q** | query | _string_ | Match query criteria, which includes all the filter string fields |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return IDs |
|  | **limit** | query | _integer_ | Number of IDs to return |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'sort': 'string',
    'filter': 'string',
    'q': 'string',
    'offset': 'string',
    'limit': integer
}

response = falcon.query_rule_groups_full(parameters=PARAMS)
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
    'limit': integer
}

response = falcon.command('query-rule-groups-full', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### query\_rule\_groupsMixin0

Finds all rule group IDs matching the query with optional filter.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **sort** | query | _string_ | Possible order by fields: {created\_by, created\_on, modified\_by, modified\_on, enabled, name, description} |
|  | **filter** | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: \[enabled platform name description rules.action\_label rules.name rules.description rules.pattern\_severity rules.ruletype\_name rules.enabled\]. Filter range criteria: created\_on, modified\_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
|  | **q** | query | _string_ | Match query criteria, which includes all the filter string fields |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return IDs |
|  | **limit** | query | _integer_ | Number of IDs to return |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'sort': 'string',
    'filter': 'string',
    'q': 'string',
    'offset': 'string',
    'limit': integer
}

response = falcon.query_rule_groupsMixin0(parameters=PARAMS)
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
    'limit': integer
}

response = falcon.command('query-rule-groupsMixin0', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### query\_rule\_types

Get all rule type IDs.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return IDs |
|  | **limit** | query | _integer_ | Number of IDs to return |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'offset': 'string',
    'limit': integer
}

response = falcon.query_rule_types(parameters=PARAMS)
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

response = falcon.command('query-rule-types', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### query\_rulesMixin0

Finds all rule IDs matching the query with optional filter.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **sort** | query | _string_ | Possible order by fields: {rules.ruletype\_name, rules.enabled, rules.created\_by, rules.current\_version.name, rules.current\_version.modified\_by, rules.created\_on, rules.current\_version.description, rules.current\_version.pattern\_severity, rules.current\_version.action\_label, rules.current\_version.modified\_on} |
|  | **filter** | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: \[enabled platform name description rules.action\_label rules.name rules.description rules.pattern\_severity rules.ruletype\_name rules.enabled\]. Filter range criteria: created\_on, modified\_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
|  | **q** | query | _string_ | Match query criteria, which includes all the filter string fields |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return IDs |
|  | **limit** | query | _integer_ | Number of IDs to return |

**Usage**

**Service class example**

```python
from falconpy import custom_ioa as FalconIOA

falcon = FalconIOA.Custom_IOA(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'sort': 'string',
    'filter': 'string',
    'q': 'string',
    'offset': 'string',
    'limit': integer
}

response = falcon.query_rulesMixin0(parameters=PARAMS)
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
    'limit': integer
}

response = falcon.command('query-rulesMixin0', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

