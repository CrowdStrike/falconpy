# MSSP

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the MSSP \(Flight Control\) service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [getChildren](mssp.md#getchildren) | Get link to child customer by child CID\(s\) |
| [getCIDGroupMembersBy](mssp.md#getcidgroupmembersby) | Get CID Group members by CID Group IDs. |
| [addCIDGroupMembers](mssp.md#addcidgroupmembers) | Add new CID Group member. |
| [deleteCIDGroupMembers](mssp.md#deletecidgroupmembers) | Delete CID Group members entry. |
| [getCIDGroupById](mssp.md#getcidgroupbyid) | Get CID Group\(s\) by ID\(s\). |
| [createCIDGroups](mssp.md#createcidgroups) | Create new CID Group\(s\). Maximum 500 CID Group\(s\) allowed. |
| [deleteCIDGroups](mssp.md#deletecidgroups) | Delete CID Group\(s\) by ID\(s\). |
| [updateCIDGroups](mssp.md#updatecidgroups) | Update existing CID Group\(s\). CID Group ID is expected for each CID Group definition provided in request body. CID Group member\(s\) remain unaffected. |
| [getRolesByID](mssp.md#getrolesbyid) | Get MSSP Role assignment\(s\). MSSP Role assignment is of the format :. |
| [addRole](mssp.md#addrole) | Assign new MSSP Role\(s\) between User Group and CID Group. It does not revoke existing role\(s\) between User Group and CID Group. User Group ID and CID Group ID have to be specified in request. |
| [deletedRoles](mssp.md#deletedroles) | Delete MSSP Role assignment\(s\) between User Group and CID Group. User Group ID and CID Group ID have to be specified in request. Only specified roles are removed if specified in request payload, else association between User Group and CID Group is dissolved completely \(if no roles specified\). |
| [getUserGroupMembersByID](mssp.md#getusergroupmembersbyid) | Get User Group members by User Group ID\(s\). |
| [addUserGroupMembers](mssp.md#addusergroupmembers) | Add new User Group member. Maximum 500 members allowed per User Group. |
| [deleteUserGroupMembers](mssp.md#deleteusergroupmembers) | Delete User Group members entry. |
| [getUserGroupsByID](mssp.md#getusergroupsbyid) | Get User Group by ID\(s\). |
| [createUserGroups](mssp.md#createusergroups) | Create new User Group\(s\). Maximum 500 User Group\(s\) allowed per customer. |
| [deleteUserGroups](mssp.md#deleteusergroups) | Delete User Group\(s\) by ID\(s\). |
| [updateUserGroups](mssp.md#updateusergroups) | Update existing User Group\(s\). User Group ID is expected for each User Group definition provided in request body. User Group member\(s\) remain unaffected. |
| [queryChildren](mssp.md#querychildren) | Query for customers linked as children |
| [queryCIDGroupMembers](mssp.md#querycidgroupmembers) | Query a CID Groups members by associated CID. |
| [queryCIDGroups](mssp.md#querycidgroups) | Query CID Groups. |
| [queryRoles](mssp.md#queryroles) | Query MSSP Role assignment. At least one of CID Group ID or User Group ID should also be provided. Role ID is optional. |
| [queryUserGroupMembers](mssp.md#queryusergroupmembers) | Query User Group member by User UUID. |
| [queryUserGroups](mssp.md#queryusergroups) | Query User Groups. |

### getChildren

Get link to child customer by child CID\(s\)

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | CID of a child customer |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.getChildren(ids=IDS)
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

response = falcon.command('getChildren', ids=IDS)
print(response)
falcon.deauthenticate()
```

### getCIDGroupMembersBy

Get CID Group members by CID Group IDs.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **cid\_group\_ids** | query | array \(_string_\) | CID Group IDs to be searched on |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

CID_GROUP_IDS = 'ID1,ID2,ID3'

response = falcon.getCIDGroupMembersBy(cid_group_ids=CID_GROUP_IDS)
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
    'cid_group_ids': [
       'string',
       'string'
    ]
}

response = falcon.command('getCIDGroupMembersBy', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### addCIDGroupMembers

Add new CID Group member.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.addCIDGroupMembers(body=BODY)
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

response = falcon.command('addCIDGroupMembers', body=BODY)
print(response)
falcon.deauthenticate()
```

### deleteCIDGroupMembers

Delete CID Group members entry.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.deleteCIDGroupMembers(body=BODY)
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

response = falcon.command('deleteCIDGroupMembers', body=BODY)
print(response)
falcon.deauthenticate()
```

### getCIDGroupById

Get CID Group\(s\) by ID\(s\).

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **cid\_group\_ids** | query | array \(_string_\) | CID Group IDs to be searched on |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

CID_GROUP_IDS = 'ID1,ID2,ID3'

response = falcon.getCIDGroupById(cid_group_ids=CID_GROUP_IDS)
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
    'cid_group_ids': [
       'string',
       'string'
    ]
}

response = falcon.command('getCIDGroupById', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### createCIDGroups

Create new CID Group\(s\). Maximum 500 CID Group\(s\) allowed.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.createCIDGroups(body=BODY)
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

response = falcon.command('createCIDGroups', body=BODY)
print(response)
falcon.deauthenticate()
```

### deleteCIDGroups

Delete CID Group\(s\) by ID\(s\).

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **cid\_group\_ids** | query | array \(_string_\) | CID group ids to be deleted |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

CID_GROUP_IDS = 'ID1,ID2,ID3'

response = falcon.deleteCIDGroups(cid_group_ids=CID_GROUP_IDS)
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
    'cid_group_ids': [
       'string',
       'string'
    ]
}

response = falcon.command('deleteCIDGroups', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### updateCIDGroups

Update existing CID Group\(s\). CID Group ID is expected for each CID Group definition provided in request body. CID Group member\(s\) remain unaffected.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.updateCIDGroups(body=BODY)
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

response = falcon.command('updateCIDGroups', body=BODY)
print(response)
falcon.deauthenticate()
```

### getRolesByID

Get MSSP Role assignment\(s\). MSSP Role assignment is of the format :.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | MSSP Role assignment is of the format : |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.getRolesByID(ids=IDS)
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

response = falcon.command('getRolesByID', ids=IDS)
print(response)
falcon.deauthenticate()
```

### addRole

Assign new MSSP Role\(s\) between User Group and CID Group. It does not revoke existing role\(s\) between User Group and CID Group. User Group ID and CID Group ID have to be specified in request.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.addRole(body=BODY)
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

response = falcon.command('addRole', body=BODY)
print(response)
falcon.deauthenticate()
```

### deletedRoles

Delete MSSP Role assignment\(s\) between User Group and CID Group. User Group ID and CID Group ID have to be specified in request. Only specified roles are removed if specified in request payload, else association between User Group and CID Group is dissolved completely \(if no roles specified\).

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.deletedRoles(body=BODY)
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

response = falcon.command('deletedRoles', body=BODY)
print(response)
falcon.deauthenticate()
```

### getUserGroupMembersByID

Get User Group members by User Group ID\(s\).

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **user\_group\_ids** | query | _string_ | User Group IDs to search for |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

USER_GROUP_IDS = 'ID1,ID2,ID3'

response = falcon.getUserGroupMembersByID(user_group_ids=USER_GROUP_IDS)
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
    'user_group_ids': 'string'
}

response = falcon.command('getUserGroupMembersByID', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### addUserGroupMembers

Add new User Group member. Maximum 500 members allowed per User Group.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.addUserGroupMembers(body=BODY)
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

response = falcon.command('addUserGroupMembers', body=BODY)
print(response)
falcon.deauthenticate()
```

### deleteUserGroupMembers

Delete User Group members entry.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.deleteUserGroupMembers(body=BODY)
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

response = falcon.command('deleteUserGroupMembers', body=BODY)
print(response)
falcon.deauthenticate()
```

### getUserGroupsByID

Get User Group by ID\(s\).

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **user\_group\_ids** | query | array \(_string_\) | User Group IDs to search for |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

USER_GROUP_IDS = 'ID1,ID2,ID3'

response = falcon.getUserGroupsByID(user_group_ids=USER_GROUP_IDS)
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
    'user_group_ids': [
       'string',
       'string'
    ]
}

response = falcon.command('getUserGroupsByID', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### createUserGroups

Create new User Group\(s\). Maximum 500 User Group\(s\) allowed per customer.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.createUserGroups(body=BODY)
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

response = falcon.command('createUserGroups', body=BODY)
print(response)
falcon.deauthenticate()
```

### deleteUserGroups

Delete User Group\(s\) by ID\(s\).

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **user\_group\_ids** | query | array \(_string_\) | User Group IDs |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

USER_GROUP_IDS = 'ID1,ID2,ID3'

response = falcon.deleteUserGroups(user_group_ids=USER_GROUP_IDS)
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
    'user_group_ids': [
       'string',
       'string'
    ]
}

response = falcon.command('deleteUserGroups', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### updateUserGroups

Update existing User Group\(s\). User Group ID is expected for each User Group definition provided in request body. User Group member\(s\) remain unaffected.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.updateUserGroups(body=BODY)
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

response = falcon.command('updateUserGroups', body=BODY)
print(response)
falcon.deauthenticate()
```

### queryChildren

Query for customers linked as children

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **sort** | query | _string_ | The sort expression used to sort the results |
|  | **offset** | query | _integer_ | Starting index of overall result set from which to return ids |
|  | **limit** | query | _integer_ | Number of ids to return |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'sort': 'string',
    'offset': integer,
    'limit': integer
}

response = falcon.queryChildren(parameters=PARAMS)
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
    'offset': integer,
    'limit': integer
}

response = falcon.command('queryChildren', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryCIDGroupMembers

Query a CID Groups members by associated CID.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **cid** | query | _string_ | CID to lookup associated CID group ID |
|  | **sort** | query | _string_ | The sort expression used to sort the results |
|  | **offset** | query | _integer_ | Starting index of overall result set from which to return id |
|  | **limit** | query | _integer_ | Number of ids to return |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'cid': 'string',
    'sort': 'string',
    'offset': integer,
    'limit': integer
}

response = falcon.queryCIDGroupMembers(parameters=PARAMS)
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
    'cid': 'string',
    'sort': 'string',
    'offset': integer,
    'limit': integer
}

response = falcon.command('queryCIDGroupMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryCIDGroups

Query CID Groups.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **name** | query | _string_ | Name to lookup groups for |
|  | **sort** | query | _string_ | The sort expression used to sort the results |
|  | **offset** | query | _integer_ | Starting index of overall result set from which to return ids |
|  | **limit** | query | _integer_ | Number of ids to return |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'name': 'string',
    'sort': 'string',
    'offset': integer,
    'limit': integer
}

response = falcon.queryCIDGroups(parameters=PARAMS)
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
    'name': 'string',
    'sort': 'string',
    'offset': integer,
    'limit': integer
}

response = falcon.command('queryCIDGroups', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryRoles

Query MSSP Role assignment. At least one of CID Group ID or User Group ID should also be provided. Role ID is optional.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **user\_group\_id** | query | _string_ | User Group ID to fetch MSSP role for |
|  | **cid\_group\_id** | query | _string_ | CID Group ID to fetch MSSP role for |
|  | **role\_id** | query | _string_ | Role ID to fetch MSSP role for |
|  | **sort** | query | _string_ | The sort expression used to sort the results |
|  | **offset** | query | _integer_ | Starting index of overall result set from which to return ids |
|  | **limit** | query | _integer_ | Number of ids to return |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'user_group_id': 'string',
    'cid_group_id': 'string',
    'role_id': 'string',
    'sort': 'string',
    'offset': integer,
    'limit': integer
}

response = falcon.queryRoles(parameters=PARAMS)
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
    'user_group_id': 'string',
    'cid_group_id': 'string',
    'role_id': 'string',
    'sort': 'string',
    'offset': integer,
    'limit': integer
}

response = falcon.command('queryRoles', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryUserGroupMembers

Query User Group member by User UUID.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **user\_uuid** | query | _string_ | User UUID to lookup associated user group ID |
|  | **sort** | query | _string_ | The sort expression used to sort the results |
|  | **offset** | query | _integer_ | Starting index of overall result set from which to return ids |
|  | **limit** | query | _integer_ | Number of ids to return |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'user_uuid': 'string',
    'sort': 'string',
    'offset': integer,
    'limit': integer
}

response = falcon.queryUserGroupMembers(parameters=PARAMS)
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
    'user_uuid': 'string',
    'sort': 'string',
    'offset': integer,
    'limit': integer
}

response = falcon.command('queryUserGroupMembers', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### queryUserGroups

Query User Groups.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **name** | query | _string_ | Name to lookup groups for |
|  | **sort** | query | _string_ | The sort expression used to sort the results |
|  | **offset** | query | _integer_ | Starting index of overall result set from which to return ids |
|  | **limit** | query | _integer_ | Number of ids to return |

**Usage**

**Service class example**

```python
from falconpy import mssp as FalconMSSP

falcon = FalconMSSP.Flight_Control(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'name': 'string',
    'sort': 'string',
    'offset': integer,
    'limit': integer
}

response = falcon.queryUserGroups(parameters=PARAMS)
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
    'name': 'string',
    'sort': 'string',
    'offset': integer,
    'limit': integer
}

response = falcon.command('queryUserGroups', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

