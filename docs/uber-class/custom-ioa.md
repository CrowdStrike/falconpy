# Using the Custom IOA service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-X%20No-red.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [get_patterns](#get-patterns) | Get pattern severities by ID. |
| [get_platformsMixin0](#get-platformsmixin0) | Get platforms by ID. |
| [get_rule_groupsMixin0](#get-rule-groupsmixin0) | Get rule groups by ID. |
| [create_rule_groupMixin0](#create-rule-groupmixin0) | Create a rule group for a platform with a name and an optional description. Returns the rule group. |
| [delete_rule_groupsMixin0](#delete-rule-groupsmixin0) | Delete rule groups by ID. |
| [update_rule_groupMixin0](#update-rule-groupmixin0) | Update a rule group. The following properties can be modified: name, description, enabled. |
| [get_rule_types](#get-rule-types) | Get rule types by ID. |
| [get_rules_get](#get-rules-get) | Get rules by ID and optionally version in the following format: `ID[:version]`. |
| [get_rulesMixin0](#get-rulesmixin0) | Get rules by ID and optionally version in the following format: `ID[:version]`. The max number of IDs is constrained by URL size. |
| [create_rule](#create-rule) | Create a rule within a rule group. Returns the rule. |
| [delete_rules](#delete-rules) | Delete rules from a rule group by ID. |
| [update_rules](#update-rules) | Update rules within a rule group. Return the updated rules. |
| [validate](#validate) | Validates field values and checks for matches if a test string is provided. |
| [query_patterns](#query-patterns) | Get all pattern severity IDs. |
| [query_platformsMixin0](#query-platformsmixin0) | Get all platform IDs. |
| [query_rule_groups_full](#query-rule-groups-full) | Find all rule groups matching the query with optional filter. |
| [query_rule_groupsMixin0](#query-rule-groupsmixin0) | Finds all rule group IDs matching the query with optional filter. |
| [query_rule_types](#query-rule-types) | Get all rule type IDs. |
| [query_rulesMixin0](#query-rulesmixin0) | Finds all rule IDs matching the query with optional filter. |
### get_patterns
Get pattern severities by ID.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the entities |
#### Usage
##### Uber class example
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
### get_platformsMixin0
Get platforms by ID.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the entities |
#### Usage
##### Uber class example
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
### get_rule_groupsMixin0
Get rule groups by ID.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the entities |
#### Usage
##### Uber class example
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
### create_rule_groupMixin0
Create a rule group for a platform with a name and an optional description. Returns the rule group.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __X-CS-USERNAME__ | header | _string_ | The user ID |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
##### Uber class example
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

response = falcon.command('create-rule-groupMixin0', body=BODY, headers=HEADERS)
print(response)
falcon.deauthenticate()
```
### delete_rule_groupsMixin0
Delete rule groups by ID.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __X-CS-USERNAME__ | header | _string_ | The user ID |
| | __comment__ | query | _string_ | Explains why the entity is being deleted |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the entities |
#### Usage
##### Uber class example
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

response = falcon.command('delete-rule-groupsMixin0', parameters=PARAMS, headers=HEADERS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### update_rule_groupMixin0
Update a rule group. The following properties can be modified: name, description, enabled.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __X-CS-USERNAME__ | header | _string_ | The user ID |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
##### Uber class example
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

response = falcon.command('update-rule-groupMixin0', body=BODY, headers=HEADERS)
print(response)
falcon.deauthenticate()
```
### get_rule_types
Get rule types by ID.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the entities |
#### Usage
##### Uber class example
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
### get_rules_get
Get rules by ID and optionally version in the following format: `ID[:version]`.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | The "ids" field contains a list of the rules to retrieve. |
#### Usage
##### Uber class example
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
### get_rulesMixin0
Get rules by ID and optionally version in the following format: `ID[:version]`. The max number of IDs is constrained by URL size.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the entities |
#### Usage
##### Uber class example
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
### create_rule
Create a rule within a rule group. Returns the rule.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __X-CS-USERNAME__ | header | _string_ | The user ID |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
##### Uber class example
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

response = falcon.command('create-rule', body=BODY, headers=HEADERS)
print(response)
falcon.deauthenticate()
```
### delete_rules
Delete rules from a rule group by ID.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __X-CS-USERNAME__ | header | _string_ | The user ID |
| :white_check_mark: | __rule_group_id__ | query | _string_ | The parent rule group |
| | __comment__ | query | _string_ | Explains why the entity is being deleted |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the entities |
#### Usage
##### Uber class example
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

HEADERS = {
    'X-CS-USERNAME': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('delete-rules', parameters=PARAMS, headers=HEADERS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### update_rules
Update rules within a rule group. Return the updated rules.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __X-CS-USERNAME__ | header | _string_ | The user ID |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
##### Uber class example
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

response = falcon.command('update-rules', body=BODY, headers=HEADERS)
print(response)
falcon.deauthenticate()
```
### validate
Validates field values and checks for matches if a test string is provided.

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
##### Uber class example
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
### query_patterns
Get all pattern severity IDs.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return IDs |
| | __limit__ | query | _integer_ | Number of IDs to return |
#### Usage
##### Uber class example
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
### query_platformsMixin0
Get all platform IDs.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return IDs |
| | __limit__ | query | _integer_ | Number of IDs to return |
#### Usage
##### Uber class example
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
### query_rule_groups_full
Find all rule groups matching the query with optional filter.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __sort__ | query | _string_ | Possible order by fields: {created_by, created_on, modified_by, modified_on, enabled, name, description} |
| | __filter__ | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: [enabled platform name description rules.action_label rules.name rules.description rules.pattern_severity rules.ruletype_name rules.enabled]. Filter range criteria: created_on, modified_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
| | __q__ | query | _string_ | Match query criteria, which includes all the filter string fields |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return IDs |
| | __limit__ | query | _integer_ | Number of IDs to return |
#### Usage
##### Uber class example
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
### query_rule_groupsMixin0
Finds all rule group IDs matching the query with optional filter.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __sort__ | query | _string_ | Possible order by fields: {created_by, created_on, modified_by, modified_on, enabled, name, description} |
| | __filter__ | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: [enabled platform name description rules.action_label rules.name rules.description rules.pattern_severity rules.ruletype_name rules.enabled]. Filter range criteria: created_on, modified_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
| | __q__ | query | _string_ | Match query criteria, which includes all the filter string fields |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return IDs |
| | __limit__ | query | _integer_ | Number of IDs to return |
#### Usage
##### Uber class example
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
### query_rule_types
Get all rule type IDs.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return IDs |
| | __limit__ | query | _integer_ | Number of IDs to return |
#### Usage
##### Uber class example
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
### query_rulesMixin0
Finds all rule IDs matching the query with optional filter.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __sort__ | query | _string_ | Possible order by fields: {rules.ruletype_name, rules.enabled, rules.created_by, rules.current_version.name, rules.current_version.modified_by, rules.created_on, rules.current_version.description, rules.current_version.pattern_severity, rules.current_version.action_label, rules.current_version.modified_on} |
| | __filter__ | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: [enabled platform name description rules.action_label rules.name rules.description rules.pattern_severity rules.ruletype_name rules.enabled]. Filter range criteria: created_on, modified_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
| | __q__ | query | _string_ | Match query criteria, which includes all the filter string fields |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return IDs |
| | __limit__ | query | _integer_ | Number of IDs to return |
#### Usage
##### Uber class example
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
