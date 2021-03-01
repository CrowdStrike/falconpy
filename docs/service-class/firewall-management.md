# Using the Firewall Management service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [aggregate_events](#aggregate-events) | Aggregate events for customer |
| [aggregate_policy_rules](#aggregate-policy-rules) | Aggregate rules within a policy for customer |
| [aggregate_rule_groups](#aggregate-rule-groups) | Aggregate rule groups for customer |
| [aggregate_rules](#aggregate-rules) | Aggregate rules for customer |
| [get_events](#get-events) | Get events entities by ID and optionally version |
| [get_firewall_fields](#get-firewall-fields) | Get the firewall field specifications by ID |
| [get_platforms](#get-platforms) | Get platforms by ID, e.g., windows or mac or droid |
| [get_policy_containers](#get-policy-containers) | Get policy container entities by policy ID |
| [update_policy_container](#update-policy-container) | Update an identified policy container |
| [get_rule_groups](#get-rule-groups) | Get rule group entities by ID. These groups do not contain their rule entites, just the rule IDs in precedence order. |
| [create_rule_group](#create-rule-group) | Create new rule group on a platform for a customer with a name and description, and return the ID |
| [delete_rule_groups](#delete-rule-groups) | Delete rule group entities by ID |
| [update_rule_group](#update-rule-group) | Update name, description, or enabled status of a rule group, or create, edit, delete, or reorder rules |
| [get_rules](#get-rules) | Get rule entities by ID (64-bit unsigned int as decimal string) or Family ID (32-character hexadecimal string) |
| [query_events](#query-events) | Find all event IDs matching the query with filter |
| [query_firewall_fields](#query-firewall-fields) | Get the firewall field specification IDs for the provided platform |
| [query_platforms](#query-platforms) | Get the list of platform names |
| [query_policy_rules](#query-policy-rules) | Find all firewall rule IDs matching the query with filter, and return them in precedence order |
| [query_rule_groups](#query-rule-groups) | Find all rule group IDs matching the query with filter |
| [query_rules](#query-rules) | Find all rule IDs matching the query with filter |
### aggregate_events
Aggregate events for customer

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Query criteria and settings |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.aggregate-events(body=BODY)
    print(response)

    authorization.revoke(token=token)
```
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

response = falcon.command('aggregate-events', body=BODY)
print(response)
falcon.deauthenticate()
```
### aggregate_policy_rules
Aggregate rules within a policy for customer

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Query criteria and settings |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.aggregate-policy-rules(body=BODY)
    print(response)

    authorization.revoke(token=token)
```
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

response = falcon.command('aggregate-policy-rules', body=BODY)
print(response)
falcon.deauthenticate()
```
### aggregate_rule_groups
Aggregate rule groups for customer

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Query criteria and settings |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.aggregate-rule-groups(body=BODY)
    print(response)

    authorization.revoke(token=token)
```
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

response = falcon.command('aggregate-rule-groups', body=BODY)
print(response)
falcon.deauthenticate()
```
### aggregate_rules
Aggregate rules for customer

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Query criteria and settings |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.aggregate-rules(body=BODY)
    print(response)

    authorization.revoke(token=token)
```
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

response = falcon.command('aggregate-rules', body=BODY)
print(response)
falcon.deauthenticate()
```
### get_events
Get events entities by ID and optionally version

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The events to retrieve, identified by ID |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.get-events(ids=IDS)
    print(response)

    authorization.revoke(token=token)
```
##### Uber class example
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
### get_firewall_fields
Get the firewall field specifications by ID

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the rule types to retrieve |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.get-firewall-fields(ids=IDS)
    print(response)

    authorization.revoke(token=token)
```
##### Uber class example
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
### get_platforms
Get platforms by ID, e.g., windows or mac or droid

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the platforms to retrieve |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.get-platforms(ids=IDS)
    print(response)

    authorization.revoke(token=token)
```
##### Uber class example
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
### get_policy_containers
Get policy container entities by policy ID

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The policy container(s) to retrieve, identified by policy ID |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.get-policy-containers(ids=IDS)
    print(response)

    authorization.revoke(token=token)
```
##### Uber class example
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
### update_policy_container
Update an identified policy container

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __X-CS-USERNAME__ | header | _string_ | The user id |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    HEADERS = {
        'X-CS-USERNAME': 'string'
    }

    response = falcon.update-policy-container(body=BODY, headers=HEADERS)
    print(response)

    authorization.revoke(token=token)
```
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

response = falcon.command('update-policy-container', body=BODY, headers=HEADERS)
print(response)
falcon.deauthenticate()
```
### get_rule_groups
Get rule group entities by ID. These groups do not contain their rule entites, just the rule IDs in precedence order.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the rule groups to retrieve |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.get-rule-groups(ids=IDS)
    print(response)

    authorization.revoke(token=token)
```
##### Uber class example
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
### create_rule_group
Create new rule group on a platform for a customer with a name and description, and return the ID

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __X-CS-USERNAME__ | header | _string_ | The user id |
| | __clone_id__ | query | _string_ | A rule group ID from which to copy rules. If this is provided then the 'rules' property of the body is ignored. |
| | __library__ | query | _string_ | If this flag is set to true then the rules will be cloned from the clone_id from the CrowdStrike Firewal Rule Groups Library. |
| | __comment__ | query | _string_ | Audit log comment for this action |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

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

    response = falcon.create-rule-group(parameters=PARAMS, body=BODY, headers=HEADERS)
    print(response)

    authorization.revoke(token=token)
```
##### Uber class example
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
### delete_rule_groups
Delete rule group entities by ID

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __X-CS-USERNAME__ | header | _string_ | The user id |
| :white_check_mark: | __ids__ | query | array (_string_) | The IDs of the rule groups to be deleted |
| | __comment__ | query | _string_ | Audit log comment for this action |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    PARAMS = {
        'comment': 'string'
    }

    HEADERS = {
        'X-CS-USERNAME': 'string'
    }

    IDS = 'ID1,ID2,ID3'

    response = falcon.delete-rule-groups(parameters=PARAMS, headers=HEADERS, ids=IDS)
    print(response)

    authorization.revoke(token=token)
```
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

response = falcon.command('delete-rule-groups', parameters=PARAMS, headers=HEADERS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### update_rule_group
Update name, description, or enabled status of a rule group, or create, edit, delete, or reorder rules

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __X-CS-USERNAME__ | header | _string_ | The user id |
| | __comment__ | query | _string_ | Audit log comment for this action |
| :white_check_mark: | __body__ | body | _string_ 
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    PARAMS = {
        'comment': 'string'
    }

    BODY = {
        'Body Payload': 'See body description above'
    }

    HEADERS = {
        'X-CS-USERNAME': 'string'
    }

    response = falcon.update-rule-group(parameters=PARAMS, body=BODY, headers=HEADERS)
    print(response)

    authorization.revoke(token=token)
```
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
### get_rules
Get rule entities by ID (64-bit unsigned int as decimal string) or Family ID (32-character hexadecimal string)

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | The rules to retrieve, identified by ID |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.get-rules(ids=IDS)
    print(response)

    authorization.revoke(token=token)
```
##### Uber class example
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
### query_events
Find all event IDs matching the query with filter

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __sort__ | query | _string_ | Possible order by fields:  |
| | __filter__ | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: enabled, platform, name, description, etc TODO. Filter range criteria: created_on, modified_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
| | __q__ | query | _string_ | Match query criteria, which includes all the filter string fields, plus TODO |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return ids. |
| | __after__ | query | _string_ | A pagination token used with the `limit` parameter to manage pagination of results. On your first request, don't provide an `after` token. On subsequent requests, provide the `after` token from the previous response to continue from that place in the results. |
| | __limit__ | query | _integer_ | Number of ids to return. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    PARAMS = {
        'sort': 'string',
        'filter': 'string',
        'q': 'string',
        'offset': 'string',
        'after': 'string',
        'limit': integer
    }

    response = falcon.query-events(parameters=PARAMS)
    print(response)

    authorization.revoke(token=token)
```
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
    'after': 'string',
    'limit': integer
}

response = falcon.command('query-events', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### query_firewall_fields
Get the firewall field specification IDs for the provided platform

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __platform_id__ | query | _string_ | Get fields configuration for this platform |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return ids. |
| | __limit__ | query | _integer_ | Number of ids to return. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    PARAMS = {
        'platform_id': 'string',
        'offset': 'string',
        'limit': integer
    }

    response = falcon.query-firewall-fields(parameters=PARAMS)
    print(response)

    authorization.revoke(token=token)
```
##### Uber class example
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
### query_platforms
Get the list of platform names

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return ids. |
| | __limit__ | query | _integer_ | Number of ids to return. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    PARAMS = {
        'offset': 'string',
        'limit': integer
    }

    response = falcon.query-platforms(parameters=PARAMS)
    print(response)

    authorization.revoke(token=token)
```
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

response = falcon.command('query-platforms', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### query_policy_rules
Find all firewall rule IDs matching the query with filter, and return them in precedence order

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __id__ | query | _string_ | The ID of the policy container within which to query |
| | __sort__ | query | _string_ | Possible order by fields:  |
| | __filter__ | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: enabled, platform, name, description, etc TODO. Filter range criteria: created_on, modified_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
| | __q__ | query | _string_ | Match query criteria, which includes all the filter string fields, plus TODO |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return ids. |
| | __limit__ | query | _integer_ | Number of ids to return. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    PARAMS = {
        'id': 'string',
        'sort': 'string',
        'filter': 'string',
        'q': 'string',
        'offset': 'string',
        'limit': integer
    }

    response = falcon.query-policy-rules(parameters=PARAMS)
    print(response)

    authorization.revoke(token=token)
```
##### Uber class example
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
### query_rule_groups
Find all rule group IDs matching the query with filter

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __sort__ | query | _string_ | Possible order by fields:  |
| | __filter__ | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: enabled, platform, name, description, etc TODO. Filter range criteria: created_on, modified_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
| | __q__ | query | _string_ | Match query criteria, which includes all the filter string fields, plus TODO |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return ids. |
| | __after__ | query | _string_ | A pagination token used with the `limit` parameter to manage pagination of results. On your first request, don't provide an `after` token. On subsequent requests, provide the `after` token from the previous response to continue from that place in the results. |
| | __limit__ | query | _integer_ | Number of ids to return. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    PARAMS = {
        'sort': 'string',
        'filter': 'string',
        'q': 'string',
        'offset': 'string',
        'after': 'string',
        'limit': integer
    }

    response = falcon.query-rule-groups(parameters=PARAMS)
    print(response)

    authorization.revoke(token=token)
```
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
    'after': 'string',
    'limit': integer
}

response = falcon.command('query-rule-groups', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### query_rules
Find all rule IDs matching the query with filter

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __sort__ | query | _string_ | Possible order by fields:  |
| | __filter__ | query | _string_ | FQL query specifying the filter parameters. Filter term criteria: enabled, platform, name, description, etc TODO. Filter range criteria: created_on, modified_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'. |
| | __q__ | query | _string_ | Match query criteria, which includes all the filter string fields, plus TODO |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return ids. |
| | __after__ | query | _string_ | A pagination token used with the `limit` parameter to manage pagination of results. On your first request, don't provide an `after` token. On subsequent requests, provide the `after` token from the previous response to continue from that place in the results. |
| | __limit__ | query | _integer_ | Number of ids to return. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import firewall_management as FalconFM

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconFM.Firewall_Management(access_token=token)

    PARAMS = {
        'sort': 'string',
        'filter': 'string',
        'q': 'string',
        'offset': 'string',
        'after': 'string',
        'limit': integer
    }

    response = falcon.query-rules(parameters=PARAMS)
    print(response)

    authorization.revoke(token=token)
```
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
    'after': 'string',
    'limit': integer
}

response = falcon.command('query-rules', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
