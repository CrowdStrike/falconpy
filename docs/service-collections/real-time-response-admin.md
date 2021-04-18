# Real Time Response Admin

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Real Time Response Admin service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [BatchAdminCmd](real-time-response-admin.md#batchadmincmd) | Batch executes a RTR administrator command across the hosts mapped to the given batch ID. |
| [RTR\_CheckAdminCommandStatus](real-time-response-admin.md#rtr_checkadmincommandstatus) | Get status of an executed RTR administrator command on a single host. |
| [RTR\_ExecuteAdminCommand](real-time-response-admin.md#rtr_executeadmincommand) | Execute a RTR administrator command on a single host. |
| [RTR\_GetPut\_Files](real-time-response-admin.md#rtr_getput_files) | Get put-files based on the ID's given. These are used for the RTR `put` command. |
| [RTR\_CreatePut\_Files](real-time-response-admin.md#rtr_createput_files) | Upload a new put-file to use for the RTR `put` command. |
| [RTR\_DeletePut\_Files](real-time-response-admin.md#rtr_deleteput_files) | Delete a put-file based on the ID given.  Can only delete one file at a time. |
| [RTR\_GetScripts](real-time-response-admin.md#rtr_getscripts) | Get custom-scripts based on the ID's given. These are used for the RTR `runscript` command. |
| [RTR\_CreateScripts](real-time-response-admin.md#rtr_createscripts) | Upload a new custom-script to use for the RTR `runscript` command. |
| [RTR\_DeleteScripts](real-time-response-admin.md#rtr_deletescripts) | Delete a custom-script based on the ID given.  Can only delete one script at a time. |
| [RTR\_UpdateScripts](real-time-response-admin.md#rtr_updatescripts) | Upload a new scripts to replace an existing one. |
| [RTR\_ListPut\_Files](real-time-response-admin.md#rtr_listput_files) | Get a list of put-file ID's that are available to the user for the `put` command. |
| [RTR\_ListScripts](real-time-response-admin.md#rtr_listscripts) | Get a list of custom-script ID's that are available to the user for the `runscript` command. |

### BatchAdminCmd

Batch executes a RTR administrator command across the hosts mapped to the given batch ID.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **timeout** | query | _integer_ | Timeout for how long to wait for the request in seconds, default timeout is 30 seconds. Maximum is 10 minutes. |
|  | **timeout\_duration** | query | _string_ | Timeout duration for for how long to wait for the request in duration syntax. Example, `10s`. Valid units: `ns, us, ms, s, m, h`. Maximum is 10 minutes. |
| :white\_check\_mark: | **body** | body | _string_ | Use this endpoint to run these [real time response commands](https://falcon.crowdstrike.com/support/documentation/11/getting-started-guide#rtr_commands): - `cat` - `cd` - `clear` - `cp` - `encrypt` - `env` - `eventlog` - `filehash` - `get` - `getsid` - `help` - `history` - `ipconfig` - `kill` - `ls` - `map` - `memdump` - `mkdir` - `mount` - `mv` - `netstat` - `ps` - `put` - `reg query` - `reg set` - `reg delete` - `reg load` - `reg unload` - `restart` - `rm` - `run` - `runscript` - `shutdown` - `unmap` - `update history` - `update install` - `update list` - `update query` - `xmemdump` - `zip`  **`base_command`** Active-Responder command type we are going to execute, for example: `get` or `cp`.  Refer to the RTR documentation for the full list of commands. **`batch_id`** Batch ID to execute the command on.  Received from `/real-time-response/combined/init-sessions/v1`. **`command_string`** Full command string for the command. For example  `get some_file.txt` **`optional_hosts`** List of a subset of hosts we want to run the command on.  If this list is supplied, only these hosts will receive the command. |

**Usage**

**Service class example**

```python
from falconpy import real_time_response_admin as FalconRTRAdmin

falcon = FalconRTRAdmin.Real_Time_Response_Admin(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'timeout': integer,
    'timeout_duration': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.BatchAdminCmd(parameters=PARAMS, body=BODY)
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
    'timeout': integer,
    'timeout_duration': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.command('BatchAdminCmd', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```

### RTR\_CheckAdminCommandStatus

Get status of an executed RTR administrator command on a single host.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **cloud\_request\_id** | query | _string_ | Cloud Request ID of the executed command to query |
| :white\_check\_mark: | **sequence\_id** | query | _integer_ | Sequence ID that we want to retrieve. Command responses are chunked across sequences |

**Usage**

**Service class example**

```python
from falconpy import real_time_response_admin as FalconRTRAdmin

falcon = FalconRTRAdmin.Real_Time_Response_Admin(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'cloud_request_id': 'string',
    'sequence_id': integer
}

response = falcon.RTR_CheckAdminCommandStatus(parameters=PARAMS)
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
    'cloud_request_id': 'string',
    'sequence_id': integer
}

response = falcon.command('RTR-CheckAdminCommandStatus', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### RTR\_ExecuteAdminCommand

Execute a RTR administrator command on a single host.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ | Use this endpoint to run these [real time response commands](https://falcon.crowdstrike.com/support/documentation/11/getting-started-guide#rtr_commands): - `cat` - `cd` - `clear` - `cp` - `encrypt` - `env` - `eventlog` - `filehash` - `get` - `getsid` - `help` - `history` - `ipconfig` - `kill` - `ls` - `map` - `memdump` - `mkdir` - `mount` - `mv` - `netstat` - `ps` - `put` - `reg query` - `reg set` - `reg delete` - `reg load` - `reg unload` - `restart` - `rm` - `run` - `runscript` - `shutdown` - `unmap` - `update history` - `update install` - `update list` - `update query` - `xmemdump` - `zip`  Required values.  The rest of the fields are unused. **`base_command`** Active-Responder command type we are going to execute, for example: `get` or `cp`.  Refer to the RTR documentation for the full list of commands. **`command_string`** Full command string for the command. For example  `get some_file.txt` **`session_id`** RTR session ID to run the command on |

**Usage**

**Service class example**

```python
from falconpy import real_time_response_admin as FalconRTRAdmin

falcon = FalconRTRAdmin.Real_Time_Response_Admin(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.RTR_ExecuteAdminCommand(body=BODY)
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

response = falcon.command('RTR-ExecuteAdminCommand', body=BODY)
print(response)
falcon.deauthenticate()
```

### RTR\_GetPut\_Files

Get put-files based on the ID's given. These are used for the RTR `put` command.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | File IDs |

**Usage**

**Service class example**

```python
from falconpy import real_time_response_admin as FalconRTRAdmin

falcon = FalconRTRAdmin.Real_Time_Response_Admin(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.RTR_GetPut_Files(ids=IDS)
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

response = falcon.command('RTR-GetPut-Files', ids=IDS)
print(response)
falcon.deauthenticate()
```

### RTR\_CreatePut\_Files

Upload a new put-file to use for the RTR `put` command.

**Content-Type**

* Consumes: _multipart/form-data_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **file** | formData | _file_ | put-file to upload |
| :white\_check\_mark: | **description** | formData | _string_ | File description |
|  | **name** | formData | _string_ | File name \(if different than actual file name\) |
|  | **comments\_for\_audit\_log** | formData | _string_ | The audit log comment |

**Usage**

**Service class example**

```python
from falconpy import real_time_response_admin as FalconRTRAdmin

falcon = FalconRTRAdmin.Real_Time_Response_Admin(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PAYLOAD = {
    'description': 'string',
    'name': 'string',
    'comments_for_audit_log': 'string'
}

response = falcon.RTR_CreatePut_Files(data=PAYLOAD, files=[('file', ('testfile.jpg', open('testfile.jpg','rb').read(), 'image/jpg'))])
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

PAYLOAD = {
    'description': 'string',
    'name': 'string',
    'comments_for_audit_log': 'string'
}

response = falcon.command('RTR-CreatePut-Files', data=PAYLOAD, files=[('file', ('testfile.jpg', open('testfile.jpg','rb').read(), 'image/jpg'))])
print(response)
falcon.deauthenticate()
```

### RTR\_DeletePut\_Files

Delete a put-file based on the ID given. Can only delete one file at a time.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | _string_ | File id |

**Usage**

**Service class example**

```python
from falconpy import real_time_response_admin as FalconRTRAdmin

falcon = FalconRTRAdmin.Real_Time_Response_Admin(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.RTR_DeletePut_Files(ids=IDS)
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

response = falcon.command('RTR-DeletePut-Files', ids=IDS)
print(response)
falcon.deauthenticate()
```

### RTR\_GetScripts

Get custom-scripts based on the ID's given. These are used for the RTR `runscript` command.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | File IDs |

**Usage**

**Service class example**

```python
from falconpy import real_time_response_admin as FalconRTRAdmin

falcon = FalconRTRAdmin.Real_Time_Response_Admin(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.RTR_GetScripts(ids=IDS)
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

response = falcon.command('RTR-GetScripts', ids=IDS)
print(response)
falcon.deauthenticate()
```

### RTR\_CreateScripts

Upload a new custom-script to use for the RTR `runscript` command.

**Content-Type**

* Consumes: _multipart/form-data_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **file** | formData | _file_ | custom-script file to upload.  These should be powershell scripts. |
| :white\_check\_mark: | **description** | formData | _string_ | File description |
|  | **name** | formData | _string_ | File name \(if different than actual file name\) |
|  | **comments\_for\_audit\_log** | formData | _string_ | The audit log comment |
| :white\_check\_mark: | **permission\_type** | formData | _string_ | Permission for the custom-script. Valid permission values:   - `private`, usable by only the user who uploaded it   - `group`, usable by all RTR Admins   - `public`, usable by all active-responders and RTR admins |
|  | **content** | formData | _string_ | The script text that you want to use to upload |
|  | **platform** | formData | array \(_string_\) | Platforms for the file. Currently supports: windows, mac, linux, . If no platform is provided, it will default to 'windows' |

**Usage**

**Service class example**

```python
from falconpy import real_time_response_admin as FalconRTRAdmin

falcon = FalconRTRAdmin.Real_Time_Response_Admin(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PAYLOAD = {
    'description': 'string',
    'name': 'string',
    'comments_for_audit_log': 'string',
    'permission_type': 'string',
    'content': 'string',
    'platform': [
       'string',
       'string'
    ]
}

response = falcon.RTR_CreateScripts(data=PAYLOAD, files=[('file', ('testfile.jpg', open('testfile.jpg','rb').read(), 'image/jpg'))])
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

PAYLOAD = {
    'description': 'string',
    'name': 'string',
    'comments_for_audit_log': 'string',
    'permission_type': 'string',
    'content': 'string',
    'platform': [
       'string',
       'string'
    ]
}

response = falcon.command('RTR-CreateScripts', data=PAYLOAD, files=[('file', ('testfile.jpg', open('testfile.jpg','rb').read(), 'image/jpg'))])
print(response)
falcon.deauthenticate()
```

### RTR\_DeleteScripts

Delete a custom-script based on the ID given. Can only delete one script at a time.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | _string_ | File id |

**Usage**

**Service class example**

```python
from falconpy import real_time_response_admin as FalconRTRAdmin

falcon = FalconRTRAdmin.Real_Time_Response_Admin(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.RTR_DeleteScripts(ids=IDS)
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

response = falcon.command('RTR-DeleteScripts', ids=IDS)
print(response)
falcon.deauthenticate()
```

### RTR\_UpdateScripts

Upload a new scripts to replace an existing one.

**Content-Type**

* Consumes: _multipart/form-data_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **id** | formData | _string_ | ID to update |
|  | **file** | formData | _file_ | custom-script file to upload.  These should be powershell scripts. |
|  | **description** | formData | _string_ | File description |
|  | **name** | formData | _string_ | File name \(if different than actual file name\) |
|  | **comments\_for\_audit\_log** | formData | _string_ | The audit log comment |
|  | **permission\_type** | formData | _string_ | Permission for the custom-script. Valid permission values:   - `private`, usable by only the user who uploaded it   - `group`, usable by all RTR Admins   - `public`, usable by all active-responders and RTR admins |
|  | **content** | formData | _string_ | The script text that you want to use to upload |
|  | **platform** | formData | array \(_string_\) | Platforms for the file. Currently supports: windows, mac, |

**Usage**

**Service class example**

```python
from falconpy import real_time_response_admin as FalconRTRAdmin

falcon = FalconRTRAdmin.Real_Time_Response_Admin(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PAYLOAD = {
    'id': 'string',
    'description': 'string',
    'name': 'string',
    'comments_for_audit_log': 'string',
    'permission_type': 'string',
    'content': 'string',
    'platform': [
       'string',
       'string'
    ]
}

response = falcon.RTR_UpdateScripts(data=PAYLOAD, files=[('file', ('testfile.jpg', open('testfile.jpg','rb').read(), 'image/jpg'))])
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

PAYLOAD = {
    'id': 'string',
    'description': 'string',
    'name': 'string',
    'comments_for_audit_log': 'string',
    'permission_type': 'string',
    'content': 'string',
    'platform': [
       'string',
       'string'
    ]
}

response = falcon.command('RTR-UpdateScripts', data=PAYLOAD, files=[('file', ('testfile.jpg', open('testfile.jpg','rb').read(), 'image/jpg'))])
print(response)
falcon.deauthenticate()
```

### RTR\_ListPut\_Files

Get a list of put-file ID's that are available to the user for the `put` command.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |  |
| :---: | :--- | :--- | :--- | :--- | :--- |
|  | **filter** | query | _string_ | Optional filter criteria in the form of an FQL query. For more information about FQL queries, see our [FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |  |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |  |
|  | **limit** | query | _integer_ | Number of ids to return. |  |
|  | **sort** | query | _string_ | Sort by spec. Ex: 'created\_at | asc'. |

**Usage**

**Service class example**

```python
from falconpy import real_time_response_admin as FalconRTRAdmin

falcon = FalconRTRAdmin.Real_Time_Response_Admin(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'filter': 'string',
    'offset': 'string',
    'limit': integer,
    'sort': 'string'
}

response = falcon.RTR_ListPut_Files(parameters=PARAMS)
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
    'offset': 'string',
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('RTR-ListPut-Files', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### RTR\_ListScripts

Get a list of custom-script ID's that are available to the user for the `runscript` command.

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |  |
| :---: | :--- | :--- | :--- | :--- | :--- |
|  | **filter** | query | _string_ | Optional filter criteria in the form of an FQL query. For more information about FQL queries, see our [FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |  |
|  | **offset** | query | _string_ | Starting index of overall result set from which to return ids. |  |
|  | **limit** | query | _integer_ | Number of ids to return. |  |
|  | **sort** | query | _string_ | Sort by spec. Ex: 'created\_at | asc'. |

**Usage**

**Service class example**

```python
from falconpy import real_time_response_admin as FalconRTRAdmin

falcon = FalconRTRAdmin.Real_Time_Response_Admin(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'filter': 'string',
    'offset': 'string',
    'limit': integer,
    'sort': 'string'
}

response = falcon.RTR_ListScripts(parameters=PARAMS)
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
    'offset': 'string',
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('RTR-ListScripts', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

