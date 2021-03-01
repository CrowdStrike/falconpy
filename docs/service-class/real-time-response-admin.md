# Using the Real Time Response Admin service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [BatchAdminCmd](#batchadmincmd) | Batch executes a RTR administrator command across the hosts mapped to the given batch ID. |
| [RTR_CheckAdminCommandStatus](#rtr-checkadmincommandstatus) | Get status of an executed RTR administrator command on a single host. |
| [RTR_ExecuteAdminCommand](#rtr-executeadmincommand) | Execute a RTR administrator command on a single host. |
| [RTR_GetPut_Files](#rtr-getput-files) | Get put-files based on the ID's given. These are used for the RTR `put` command. |
| [RTR_CreatePut_Files](#rtr-createput-files) | Upload a new put-file to use for the RTR `put` command. |
| [RTR_DeletePut_Files](#rtr-deleteput-files) | Delete a put-file based on the ID given.  Can only delete one file at a time. |
| [RTR_GetScripts](#rtr-getscripts) | Get custom-scripts based on the ID's given. These are used for the RTR `runscript` command. |
| [RTR_CreateScripts](#rtr-createscripts) | Upload a new custom-script to use for the RTR `runscript` command. |
| [RTR_DeleteScripts](#rtr-deletescripts) | Delete a custom-script based on the ID given.  Can only delete one script at a time. |
| [RTR_UpdateScripts](#rtr-updatescripts) | Upload a new scripts to replace an existing one. |
| [RTR_ListPut_Files](#rtr-listput-files) | Get a list of put-file ID's that are available to the user for the `put` command. |
| [RTR_ListScripts](#rtr-listscripts) | Get a list of custom-script ID's that are available to the user for the `runscript` command. |
### BatchAdminCmd
Batch executes a RTR administrator command across the hosts mapped to the given batch ID.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __timeout__ | query | _integer_ | Timeout for how long to wait for the request in seconds, default timeout is 30 seconds. Maximum is 10 minutes. |
| | __timeout_duration__ | query | _string_ | Timeout duration for for how long to wait for the request in duration syntax. Example, `10s`. Valid units: `ns, us, ms, s, m, h`. Maximum is 10 minutes. |
| :white_check_mark: | __body__ | body | _string_ | Use this endpoint to run these [real time response commands](https://falcon.crowdstrike.com/support/documentation/11/getting-started-guide#rtr_commands): - `cat` - `cd` - `clear` - `cp` - `encrypt` - `env` - `eventlog` - `filehash` - `get` - `getsid` - `help` - `history` - `ipconfig` - `kill` - `ls` - `map` - `memdump` - `mkdir` - `mount` - `mv` - `netstat` - `ps` - `put` - `reg query` - `reg set` - `reg delete` - `reg load` - `reg unload` - `restart` - `rm` - `run` - `runscript` - `shutdown` - `unmap` - `update history` - `update install` - `update list` - `update query` - `xmemdump` - `zip`  **`base_command`** Active-Responder command type we are going to execute, for example: `get` or `cp`.  Refer to the RTR documentation for the full list of commands. **`batch_id`** Batch ID to execute the command on.  Received from `/real-time-response/combined/init-sessions/v1`. **`command_string`** Full command string for the command. For example  `get some_file.txt` **`optional_hosts`** List of a subset of hosts we want to run the command on.  If this list is supplied, only these hosts will receive the command. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response_admin as FalconRTRAdmin

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTRAdmin.Real_Time_Response_Admin(access_token=token)

    PARAMS = {
        'timeout': integer,
        'timeout_duration': 'string'
    }

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.BatchAdminCmd(parameters=PARAMS, body=BODY)
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
### RTR_CheckAdminCommandStatus
Get status of an executed RTR administrator command on a single host.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __cloud_request_id__ | query | _string_ | Cloud Request ID of the executed command to query |
| :white_check_mark: | __sequence_id__ | query | _integer_ | Sequence ID that we want to retrieve. Command responses are chunked across sequences |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response_admin as FalconRTRAdmin

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTRAdmin.Real_Time_Response_Admin(access_token=token)

    PARAMS = {
        'cloud_request_id': 'string',
        'sequence_id': integer
    }

    response = falcon.RTR-CheckAdminCommandStatus(parameters=PARAMS)
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
    'cloud_request_id': 'string',
    'sequence_id': integer
}

response = falcon.command('RTR-CheckAdminCommandStatus', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### RTR_ExecuteAdminCommand
Execute a RTR administrator command on a single host.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Use this endpoint to run these [real time response commands](https://falcon.crowdstrike.com/support/documentation/11/getting-started-guide#rtr_commands): - `cat` - `cd` - `clear` - `cp` - `encrypt` - `env` - `eventlog` - `filehash` - `get` - `getsid` - `help` - `history` - `ipconfig` - `kill` - `ls` - `map` - `memdump` - `mkdir` - `mount` - `mv` - `netstat` - `ps` - `put` - `reg query` - `reg set` - `reg delete` - `reg load` - `reg unload` - `restart` - `rm` - `run` - `runscript` - `shutdown` - `unmap` - `update history` - `update install` - `update list` - `update query` - `xmemdump` - `zip`  Required values.  The rest of the fields are unused. **`base_command`** Active-Responder command type we are going to execute, for example: `get` or `cp`.  Refer to the RTR documentation for the full list of commands. **`command_string`** Full command string for the command. For example  `get some_file.txt` **`session_id`** RTR session ID to run the command on |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response_admin as FalconRTRAdmin

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTRAdmin.Real_Time_Response_Admin(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.RTR-ExecuteAdminCommand(body=BODY)
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

response = falcon.command('RTR-ExecuteAdminCommand', body=BODY)
print(response)
falcon.deauthenticate()
```
### RTR_GetPut_Files
Get put-files based on the ID's given. These are used for the RTR `put` command.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | File IDs |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response_admin as FalconRTRAdmin

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTRAdmin.Real_Time_Response_Admin(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.RTR-GetPut-Files(ids=IDS)
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

response = falcon.command('RTR-GetPut-Files', ids=IDS)
print(response)
falcon.deauthenticate()
```
### RTR_CreatePut_Files
Upload a new put-file to use for the RTR `put` command.

#### Content-Type
- Consumes: _multipart/form-data_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __file__ | formData | _file_ | put-file to upload |
| :white_check_mark: | __description__ | formData | _string_ | File description |
| | __name__ | formData | _string_ | File name (if different than actual file name) |
| | __comments_for_audit_log__ | formData | _string_ | The audit log comment |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response_admin as FalconRTRAdmin

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTRAdmin.Real_Time_Response_Admin(access_token=token)

    PAYLOAD = {
        'description': 'string',
        'name': 'string',
        'comments_for_audit_log': 'string'
    }

    response = falcon.RTR-CreatePut-Files(data=PAYLOAD, files=[('file', ('testfile.jpg', open('testfile.jpg','rb').read(), 'image/jpg'))])
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

PAYLOAD = {
    'description': 'string',
    'name': 'string',
    'comments_for_audit_log': 'string'
}

response = falcon.command('RTR-CreatePut-Files', data=PAYLOAD, files=[('file', ('testfile.jpg', open('testfile.jpg','rb').read(), 'image/jpg'))])
print(response)
falcon.deauthenticate()
```
### RTR_DeletePut_Files
Delete a put-file based on the ID given.  Can only delete one file at a time.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | _string_ | File id |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response_admin as FalconRTRAdmin

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTRAdmin.Real_Time_Response_Admin(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.RTR-DeletePut-Files(ids=IDS)
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

response = falcon.command('RTR-DeletePut-Files', ids=IDS)
print(response)
falcon.deauthenticate()
```
### RTR_GetScripts
Get custom-scripts based on the ID's given. These are used for the RTR `runscript` command.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | File IDs |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response_admin as FalconRTRAdmin

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTRAdmin.Real_Time_Response_Admin(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.RTR-GetScripts(ids=IDS)
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

response = falcon.command('RTR-GetScripts', ids=IDS)
print(response)
falcon.deauthenticate()
```
### RTR_CreateScripts
Upload a new custom-script to use for the RTR `runscript` command.

#### Content-Type
- Consumes: _multipart/form-data_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __file__ | formData | _file_ | custom-script file to upload.  These should be powershell scripts. |
| :white_check_mark: | __description__ | formData | _string_ | File description |
| | __name__ | formData | _string_ | File name (if different than actual file name) |
| | __comments_for_audit_log__ | formData | _string_ | The audit log comment |
| :white_check_mark: | __permission_type__ | formData | _string_ | Permission for the custom-script. Valid permission values:   - `private`, usable by only the user who uploaded it   - `group`, usable by all RTR Admins   - `public`, usable by all active-responders and RTR admins |
| | __content__ | formData | _string_ | The script text that you want to use to upload |
| | __platform__ | formData | array (_string_) | Platforms for the file. Currently supports: windows, mac, linux, . If no platform is provided, it will default to 'windows' |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response_admin as FalconRTRAdmin

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTRAdmin.Real_Time_Response_Admin(access_token=token)

    PAYLOAD = {
        'description': 'string',
        'name': 'string',
        'comments_for_audit_log': 'string',
        'permission_type': 'string',
        'content': 'string',
        'platform':     [
           'string',
           'string'
    ]
    }

    response = falcon.RTR-CreateScripts(data=PAYLOAD, files=[('file', ('testfile.jpg', open('testfile.jpg','rb').read(), 'image/jpg'))])
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
### RTR_DeleteScripts
Delete a custom-script based on the ID given.  Can only delete one script at a time.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | _string_ | File id |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response_admin as FalconRTRAdmin

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTRAdmin.Real_Time_Response_Admin(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.RTR-DeleteScripts(ids=IDS)
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

response = falcon.command('RTR-DeleteScripts', ids=IDS)
print(response)
falcon.deauthenticate()
```
### RTR_UpdateScripts
Upload a new scripts to replace an existing one.

#### Content-Type
- Consumes: _multipart/form-data_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __id__ | formData | _string_ | ID to update |
| | __file__ | formData | _file_ | custom-script file to upload.  These should be powershell scripts. |
| | __description__ | formData | _string_ | File description |
| | __name__ | formData | _string_ | File name (if different than actual file name) |
| | __comments_for_audit_log__ | formData | _string_ | The audit log comment |
| | __permission_type__ | formData | _string_ | Permission for the custom-script. Valid permission values:   - `private`, usable by only the user who uploaded it   - `group`, usable by all RTR Admins   - `public`, usable by all active-responders and RTR admins |
| | __content__ | formData | _string_ | The script text that you want to use to upload |
| | __platform__ | formData | array (_string_) | Platforms for the file. Currently supports: windows, mac,  |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response_admin as FalconRTRAdmin

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTRAdmin.Real_Time_Response_Admin(access_token=token)

    PAYLOAD = {
        'id': 'string',
        'description': 'string',
        'name': 'string',
        'comments_for_audit_log': 'string',
        'permission_type': 'string',
        'content': 'string',
        'platform':     [
           'string',
           'string'
    ]
    }

    response = falcon.RTR-UpdateScripts(data=PAYLOAD, files=[('file', ('testfile.jpg', open('testfile.jpg','rb').read(), 'image/jpg'))])
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
### RTR_ListPut_Files
Get a list of put-file ID's that are available to the user for the `put` command.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __filter__ | query | _string_ | Optional filter criteria in the form of an FQL query. For more information about FQL queries, see our [FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return ids. |
| | __limit__ | query | _integer_ | Number of ids to return. |
| | __sort__ | query | _string_ | Sort by spec. Ex: 'created_at|asc'. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response_admin as FalconRTRAdmin

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTRAdmin.Real_Time_Response_Admin(access_token=token)

    PARAMS = {
        'filter': 'string',
        'offset': 'string',
        'limit': integer,
        'sort': 'string'
    }

    response = falcon.RTR-ListPut-Files(parameters=PARAMS)
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
    'filter': 'string',
    'offset': 'string',
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('RTR-ListPut-Files', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### RTR_ListScripts
Get a list of custom-script ID's that are available to the user for the `runscript` command.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __filter__ | query | _string_ | Optional filter criteria in the form of an FQL query. For more information about FQL queries, see our [FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return ids. |
| | __limit__ | query | _integer_ | Number of ids to return. |
| | __sort__ | query | _string_ | Sort by spec. Ex: 'created_at|asc'. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response_admin as FalconRTRAdmin

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTRAdmin.Real_Time_Response_Admin(access_token=token)

    PARAMS = {
        'filter': 'string',
        'offset': 'string',
        'limit': integer,
        'sort': 'string'
    }

    response = falcon.RTR-ListScripts(parameters=PARAMS)
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
    'filter': 'string',
    'offset': 'string',
    'limit': integer,
    'sort': 'string'
}

response = falcon.command('RTR-ListScripts', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
