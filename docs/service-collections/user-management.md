# User Management

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the User Management service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [GetRoles](user-management.md#getroles) | Get info about a role |
| [GrantUserRoleIds](user-management.md#grantuserroleids) | Assign one or more roles to a user |
| [RevokeUserRoleIds](user-management.md#revokeuserroleids) | Revoke one or more roles from a user |
| [GetAvailableRoleIds](user-management.md#getavailableroleids) | Show role IDs for all roles available in your customer account. For more information on each role, provide the role ID to `/customer/entities/roles/v1`. |
| [GetUserRoleIds](user-management.md#getuserroleids) | Show role IDs of roles assigned to a user. For more information on each role, provide the role ID to `/customer/entities/roles/v1`. |
| [RetrieveUser](user-management.md#retrieveuser) | Get info about a user |
| [CreateUser](user-management.md#createuser) | Create a new user. After creating a user, assign one or more roles with POST /user-roles/entities/user-roles/v1 |
| [DeleteUser](user-management.md#deleteuser) | Delete a user permanently |
| [UpdateUser](user-management.md#updateuser) | Modify an existing user's first or last name |
| [RetrieveEmailsByCID](user-management.md#retrieveemailsbycid) | List the usernames \(usually an email address\) for all users in your customer account |
| [RetrieveUserUUIDsByCID](user-management.md#retrieveuseruuidsbycid) | List user IDs for all users in your customer account. For more information on each user, provide the user ID to `/users/entities/user/v1`. |
| [RetrieveUserUUID](user-management.md#retrieveuseruuid) | Get a user's ID by providing a username \(usually an email address\) |

### GetRoles

Get info about a role

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | ID of a role. Find a role ID from `/customer/queries/roles/v1` or `/users/queries/roles/v1`. |

**Usage**

**Service class example**

```python
from falconpy import user_management as FalconUsers

falcon = FalconUsers.User_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.GetRoles(ids=IDS)
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

response = falcon.command('GetRoles', ids=IDS)
print(response)
falcon.deauthenticate()
```

### GrantUserRoleIds

Assign one or more roles to a user

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **user\_uuid** | query | _string_ | ID of a user. Find a user's ID from `/users/entities/user/v1`. |
| ✅ | **body** | body | _string_ | Role ID\(s\) of the role you want to assign |

**Usage**

**Service class example**

```python
from falconpy import user_management as FalconUsers

falcon = FalconUsers.User_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'user_uuid': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.GrantUserRoleIds(parameters=PARAMS, body=BODY)
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
    'user_uuid': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.command('GrantUserRoleIds', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```

### RevokeUserRoleIds

Revoke one or more roles from a user

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **user\_uuid** | query | _string_ | ID of a user. Find a user's ID from `/users/entities/user/v1`. |
| ✅ | **ids** | query | array \(_string_\) | One or more role IDs to revoke. Find a role's ID from `/users/queries/roles/v1`. |

**Usage**

**Service class example**

```python
from falconpy import user_management as FalconUsers

falcon = FalconUsers.User_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'user_uuid': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.RevokeUserRoleIds(parameters=PARAMS, ids=IDS)
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
    'user_uuid': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('RevokeUserRoleIds', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```

### GetAvailableRoleIds

Show role IDs for all roles available in your customer account. For more information on each role, provide the role ID to `/customer/entities/roles/v1`.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

No parameters

**Usage**

**Service class example**

```python
from falconpy import user_management as FalconUsers

falcon = FalconUsers.User_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

response = falcon.GetAvailableRoleIds()
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

response = falcon.command('GetAvailableRoleIds')
print(response)
falcon.deauthenticate()
```

### GetUserRoleIds

Show role IDs of roles assigned to a user. For more information on each role, provide the role ID to `/customer/entities/roles/v1`.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **user\_uuid** | query | _string_ | ID of a user. Find a user's ID from `/users/entities/user/v1`. |

**Usage**

**Service class example**

```python
from falconpy import user_management as FalconUsers

falcon = FalconUsers.User_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'user_uuid': 'string'
}

response = falcon.GetUserRoleIds(parameters=PARAMS)
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
    'user_uuid': 'string'
}

response = falcon.command('GetUserRoleIds', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### RetrieveUser

Get info about a user

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | ID of a user. Find a user's ID from `/users/entities/user/v1`. |

**Usage**

**Service class example**

```python
from falconpy import user_management as FalconUsers

falcon = FalconUsers.User_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.RetrieveUser(ids=IDS)
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

response = falcon.command('RetrieveUser', ids=IDS)
print(response)
falcon.deauthenticate()
```

### CreateUser

Create a new user. After creating a user, assign one or more roles with POST /user-roles/entities/user-roles/v1

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ | Attributes for this user. `uid` \(required\) is the user's email address, which is their username in Falcon.  Optional attributes:    As a best practice, we recommend omitting `password`. If single sign-on is enabled for your customer account, the `password` attribute is ignored. If single sign-on is not enabled, we send a user activation request to their email address when you create the user with no `password`. The user should use the activation email to set their own password. |

**Usage**

**Service class example**

```python
from falconpy import user_management as FalconUsers

falcon = FalconUsers.User_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.CreateUser(body=BODY)
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

response = falcon.command('CreateUser', body=BODY)
print(response)
falcon.deauthenticate()
```

### DeleteUser

Delete a user permanently

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **user\_uuid** | query | _string_ | ID of a user. Find a user's ID from `/users/entities/user/v1`. |

**Usage**

**Service class example**

```python
from falconpy import user_management as FalconUsers

falcon = FalconUsers.User_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'user_uuid': 'string'
}

response = falcon.DeleteUser(parameters=PARAMS)
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
    'user_uuid': 'string'
}

response = falcon.command('DeleteUser', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### UpdateUser

Modify an existing user's first or last name

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **user\_uuid** | query | _string_ | ID of a user. Find a user's ID from `/users/entities/user/v1`. |
| ✅ | **body** | body | _string_ | Attributes for this user. All attributes \(shown below\) are optional. |

**Usage**

**Service class example**

```python
from falconpy import user_management as FalconUsers

falcon = FalconUsers.User_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'user_uuid': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.UpdateUser(parameters=PARAMS, body=BODY)
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
    'user_uuid': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.command('UpdateUser', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```

### RetrieveEmailsByCID

List the usernames \(usually an email address\) for all users in your customer account

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

No parameters

**Usage**

**Service class example**

```python
from falconpy import user_management as FalconUsers

falcon = FalconUsers.User_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

response = falcon.RetrieveEmailsByCID()
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

response = falcon.command('RetrieveEmailsByCID')
print(response)
falcon.deauthenticate()
```

### RetrieveUserUUIDsByCID

List user IDs for all users in your customer account. For more information on each user, provide the user ID to `/users/entities/user/v1`.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

No parameters

**Usage**

**Service class example**

```python
from falconpy import user_management as FalconUsers

falcon = FalconUsers.User_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

response = falcon.RetrieveUserUUIDsByCID()
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

response = falcon.command('RetrieveUserUUIDsByCID')
print(response)
falcon.deauthenticate()
```

### RetrieveUserUUID

Get a user's ID by providing a username \(usually an email address\)

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **uid** | query | array \(_string_\) | A username. This is usually the user's email address, but may vary based on your configuration. |

**Usage**

**Service class example**

```python
from falconpy import user_management as FalconUsers

falcon = FalconUsers.User_Management(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'uid': [
       'string',
       'string'
    ]
}

response = falcon.RetrieveUserUUID(parameters=PARAMS)
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
    'uid': [
       'string',
       'string'
    ]
}

response = falcon.command('RetrieveUserUUID', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

