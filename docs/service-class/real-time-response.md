# Using the Real Time Response service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [RTR_AggregateSessions](#rtr-aggregatesessions) | Get aggregates on session data. |
| [BatchActiveResponderCmd](#batchactiverespondercmd) | Batch executes a RTR active-responder command across the hosts mapped to the given batch ID. |
| [BatchCmd](#batchcmd) | Batch executes a RTR read-only command across the hosts mapped to the given batch ID. |
| [BatchGetCmdStatus](#batchgetcmdstatus) | Retrieves the status of the specified batch get command.  Will return successful files when they are finished processing. |
| [BatchGetCmd](#batchgetcmd) | Batch executes `get` command across hosts to retrieve files. After this call is made `GET /real-time-response/combined/batch-get-command/v1` is used to query for the results. |
| [BatchInitSessions](#batchinitsessions) | Batch initialize a RTR session on multiple hosts.  Before any RTR commands can be used, an active session is needed on the host. |
| [BatchRefreshSessions](#batchrefreshsessions) | Batch refresh a RTR session on multiple hosts. RTR sessions will expire after 10 minutes unless refreshed. |
| [RTR_CheckActiveResponderCommandStatus](#rtr-checkactiverespondercommandstatus) | Get status of an executed active-responder command on a single host. |
| [RTR_ExecuteActiveResponderCommand](#rtr-executeactiverespondercommand) | Execute an active responder command on a single host. |
| [RTR_CheckCommandStatus](#rtr-checkcommandstatus) | Get status of an executed command on a single host. |
| [RTR_ExecuteCommand](#rtr-executecommand) | Execute a command on a single host. |
| [RTR_GetExtractedFileContents](#rtr-getextractedfilecontents) | Get RTR extracted file contents for specified session and sha256. |
| [RTR_ListFiles](#rtr-listfiles) | Get a list of files for the specified RTR session. |
| [RTR_DeleteFile](#rtr-deletefile) | Delete a RTR session file. |
| [RTR_ListQueuedSessions](#rtr-listqueuedsessions) | Get queued session metadata by session ID. |
| [RTR_DeleteQueuedSession](#rtr-deletequeuedsession) | Delete a queued session command |
| [RTR_PulseSession](#rtr-pulsesession) | Refresh a session timeout on a single host. |
| [RTR_ListSessions](#rtr-listsessions) | Get session metadata by session id. |
| [RTR_InitSession](#rtr-initsession) | Initialize a new session with the RTR cloud. |
| [RTR_DeleteSession](#rtr-deletesession) | Delete a session. |
| [RTR_ListAllSessions](#rtr-listallsessions) | Get a list of session_ids. |
### RTR_AggregateSessions
Get aggregates on session data.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Supported aggregations:  - `term` - `date_range`  Supported aggregation members:  **`date_ranges`** If peforming a date range query specify the **`from`** and **`to`** date ranges.  These can be in common date formats like `2019-07-18` or `now` **`field`** Term you want to aggregate on.  If doing a `date_range` query, this is the date field you want to apply the date ranges to **`filter`** Optional filter criteria in the form of an FQL query. For more information about FQL queries, see our [FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). **`name`** Name of the aggregation **`size`** Size limit to apply to the queries. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.RTR-AggregateSessions(body=BODY)
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

response = falcon.command('RTR-AggregateSessions', body=BODY)
print(response)
falcon.deauthenticate()
```
### BatchActiveResponderCmd
Batch executes a RTR active-responder command across the hosts mapped to the given batch ID.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __timeout__ | query | _integer_ | Timeout for how long to wait for the request in seconds, default timeout is 30 seconds. Maximum is 10 minutes. |
| | __timeout_duration__ | query | _string_ | Timeout duration for for how long to wait for the request in duration syntax. Example, `10s`. Valid units: `ns, us, ms, s, m, h`. Maximum is 10 minutes. |
| :white_check_mark: | __body__ | body | _string_ | Use this endpoint to run these [real time response commands](https://falcon.crowdstrike.com/support/documentation/11/getting-started-guide#rtr_commands): - `cat` - `cd` - `clear` - `cp` - `encrypt` - `env` - `eventlog` - `filehash` - `get` - `getsid` - `help` - `history` - `ipconfig` - `kill` - `ls` - `map` - `memdump` - `mkdir` - `mount` - `mv` - `netstat` - `ps` - `reg query` - `reg set` - `reg delete` - `reg load` - `reg unload` - `restart` - `rm` - `runscript` - `shutdown` - `unmap` - `update history` - `update install` - `update list` - `update query` - `xmemdump` - `zip`  **`base_command`** Active-Responder command type we are going to execute, for example: `get` or `cp`.  Refer to the RTR documentation for the full list of commands. **`batch_id`** Batch ID to execute the command on.  Received from `/real-time-response/combined/init-sessions/v1`. **`command_string`** Full command string for the command. For example  `get some_file.txt` **`optional_hosts`** List of a subset of hosts we want to run the command on.  If this list is supplied, only these hosts will receive the command. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'timeout': integer,
        'timeout_duration': 'string'
    }

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.BatchActiveResponderCmd(parameters=PARAMS, body=BODY)
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

response = falcon.command('BatchActiveResponderCmd', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```
### BatchCmd
Batch executes a RTR read-only command across the hosts mapped to the given batch ID.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __timeout__ | query | _integer_ | Timeout for how long to wait for the request in seconds, default timeout is 30 seconds. Maximum is 10 minutes. |
| | __timeout_duration__ | query | _string_ | Timeout duration for for how long to wait for the request in duration syntax. Example, `10s`. Valid units: `ns, us, ms, s, m, h`. Maximum is 10 minutes. |
| :white_check_mark: | __body__ | body | _string_ | Use this endpoint to run these [real time response commands](https://falcon.crowdstrike.com/support/documentation/11/getting-started-guide#rtr_commands): - `cat` - `cd` - `clear` - `env` - `eventlog` - `filehash` - `getsid` - `help` - `history` - `ipconfig` - `ls` - `mount` - `netstat` - `ps` - `reg query`  **`base_command`** read-only command type we are going to execute, for example: `ls` or `cd`.  Refer to the RTR documentation for the full list of commands. **`batch_id`** Batch ID to execute the command on.  Received from `/real-time-response/combined/init-sessions/v1`. **`command_string`** Full command string for the command. For example  `cd C:some_directory` **`optional_hosts`** List of a subset of hosts we want to run the command on.  If this list is supplied, only these hosts will receive the command. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'timeout': integer,
        'timeout_duration': 'string'
    }

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.BatchCmd(parameters=PARAMS, body=BODY)
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

response = falcon.command('BatchCmd', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```
### BatchGetCmdStatus
Retrieves the status of the specified batch get command.  Will return successful files when they are finished processing.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __timeout__ | query | _integer_ | Timeout for how long to wait for the request in seconds, default timeout is 30 seconds. Maximum is 10 minutes. |
| | __timeout_duration__ | query | _string_ | Timeout duration for for how long to wait for the request in duration syntax. Example, `10s`. Valid units: `ns, us, ms, s, m, h`. Maximum is 10 minutes. |
| :white_check_mark: | __batch_get_cmd_req_id__ | query | _string_ | Batch Get Command Request ID received from `/real-time-response/combined/get-command/v1` |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'timeout': integer,
        'timeout_duration': 'string',
        'batch_get_cmd_req_id': 'string'
    }

    response = falcon.BatchGetCmdStatus(parameters=PARAMS)
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
    'timeout_duration': 'string',
    'batch_get_cmd_req_id': 'string'
}

response = falcon.command('BatchGetCmdStatus', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### BatchGetCmd
Batch executes `get` command across hosts to retrieve files. After this call is made `GET /real-time-response/combined/batch-get-command/v1` is used to query for the results.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __timeout__ | query | _integer_ | Timeout for how long to wait for the request in seconds, default timeout is 30 seconds. Maximum is 10 minutes. |
| | __timeout_duration__ | query | _string_ | Timeout duration for for how long to wait for the request in duration syntax. Example, `10s`. Valid units: `ns, us, ms, s, m, h`. Maximum is 10 minutes. |
| :white_check_mark: | __body__ | body | _string_ | **`batch_id`** Batch ID to execute the command on.  Received from `/real-time-response/combined/init-sessions/v1`. **`file_path`** Full path to the file that is to be retrieved from each host in the batch. **`optional_hosts`** List of a subset of hosts we want to run the command on.  If this list is supplied, only these hosts will receive the command. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'timeout': integer,
        'timeout_duration': 'string'
    }

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.BatchGetCmd(parameters=PARAMS, body=BODY)
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

response = falcon.command('BatchGetCmd', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```
### BatchInitSessions
Batch initialize a RTR session on multiple hosts.  Before any RTR commands can be used, an active session is needed on the host.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __timeout__ | query | _integer_ | Timeout for how long to wait for the request in seconds, default timeout is 30 seconds. Maximum is 10 minutes. |
| | __timeout_duration__ | query | _string_ | Timeout duration for for how long to wait for the request in duration syntax. Example, `10s`. Valid units: `ns, us, ms, s, m, h`. Maximum is 10 minutes. |
| :white_check_mark: | __body__ | body | _string_ | **`host_ids`** List of host agent ID's to initialize a RTR session on **`existing_batch_id`** Optional batch ID. Use an existing batch ID if you want to initialize new hosts and add them to the existing batch |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'timeout': integer,
        'timeout_duration': 'string'
    }

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.BatchInitSessions(parameters=PARAMS, body=BODY)
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

response = falcon.command('BatchInitSessions', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```
### BatchRefreshSessions
Batch refresh a RTR session on multiple hosts. RTR sessions will expire after 10 minutes unless refreshed.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __timeout__ | query | _integer_ | Timeout for how long to wait for the request in seconds, default timeout is 30 seconds. Maximum is 10 minutes. |
| | __timeout_duration__ | query | _string_ | Timeout duration for for how long to wait for the request in duration syntax. Example, `10s`. Valid units: `ns, us, ms, s, m, h`. Maximum is 10 minutes. |
| :white_check_mark: | __body__ | body | _string_ | **`batch_id`** Batch ID to execute the command on.  Received from `/real-time-response/combined/init-sessions/v1`. **`hosts_to_remove`** Hosts to remove from the batch session.  Heartbeats will no longer happen on these hosts and the sessions will expire. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'timeout': integer,
        'timeout_duration': 'string'
    }

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.BatchRefreshSessions(parameters=PARAMS, body=BODY)
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

response = falcon.command('BatchRefreshSessions', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```
### RTR_CheckActiveResponderCommandStatus
Get status of an executed active-responder command on a single host.

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
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'cloud_request_id': 'string',
        'sequence_id': integer
    }

    response = falcon.RTR-CheckActiveResponderCommandStatus(parameters=PARAMS)
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

response = falcon.command('RTR-CheckActiveResponderCommandStatus', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### RTR_ExecuteActiveResponderCommand
Execute an active responder command on a single host.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Use this endpoint to run these [real time response commands](https://falcon.crowdstrike.com/support/documentation/11/getting-started-guide#rtr_commands): - `cat` - `cd` - `clear` - `cp` - `encrypt` - `env` - `eventlog` - `filehash` - `get` - `getsid` - `help` - `history` - `ipconfig` - `kill` - `ls` - `map` - `memdump` - `mkdir` - `mount` - `mv` - `netstat` - `ps` - `reg query` - `reg set` - `reg delete` - `reg load` - `reg unload` - `restart` - `rm` - `runscript` - `shutdown` - `unmap` - `update history` - `update install` - `update list` - `update query` - `xmemdump` - `zip`  Required values.  The rest of the fields are unused. **`base_command`** Active-Responder command type we are going to execute, for example: `get` or `cp`.  Refer to the RTR documentation for the full list of commands. **`command_string`** Full command string for the command. For example  `get some_file.txt` **`session_id`** RTR session ID to run the command on |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.RTR-ExecuteActiveResponderCommand(body=BODY)
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

response = falcon.command('RTR-ExecuteActiveResponderCommand', body=BODY)
print(response)
falcon.deauthenticate()
```
### RTR_CheckCommandStatus
Get status of an executed command on a single host.

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
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'cloud_request_id': 'string',
        'sequence_id': integer
    }

    response = falcon.RTR-CheckCommandStatus(parameters=PARAMS)
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

response = falcon.command('RTR-CheckCommandStatus', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### RTR_ExecuteCommand
Execute a command on a single host.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Use this endpoint to run these [real time response commands](https://falcon.crowdstrike.com/support/documentation/11/getting-started-guide#rtr_commands): - `cat` - `cd` - `clear` - `env` - `eventlog` - `filehash` - `getsid` - `help` - `history` - `ipconfig` - `ls` - `mount` - `netstat` - `ps` - `reg query`  Required values.  The rest of the fields are unused. **`base_command`** read-only command type we are going to execute, for example: `ls` or `cd`.  Refer to the RTR documentation for the full list of commands. **`command_string`** Full command string for the command. For example  `cd C:some_directory` **`session_id`** RTR session ID to run the command on |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.RTR-ExecuteCommand(body=BODY)
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

response = falcon.command('RTR-ExecuteCommand', body=BODY)
print(response)
falcon.deauthenticate()
```
### RTR_GetExtractedFileContents
Get RTR extracted file contents for specified session and sha256.

#### Content-Type
- Produces: _application/x-7z-compressed_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __session_id__ | query | _string_ | RTR Session id |
| :white_check_mark: | __sha256__ | query | _string_ | Extracted SHA256 (e.g. 'efa256a96af3b556cd3fc9d8b1cf587d72807d7805ced441e8149fc279db422b') |
| | __filename__ | query | _string_ | Filename to use for the archive name and the file within the archive. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'session_id': 'string',
        'sha256': 'string',
        'filename': 'string'
    }

    response = falcon.RTR-GetExtractedFileContents(parameters=PARAMS)
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
    'session_id': 'string',
    'sha256': 'string',
    'filename': 'string'
}

response = falcon.command('RTR-GetExtractedFileContents', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### RTR_ListFiles
Get a list of files for the specified RTR session.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __session_id__ | query | _string_ | RTR Session id |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'session_id': 'string'
    }

    response = falcon.RTR-ListFiles(parameters=PARAMS)
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
    'session_id': 'string'
}

response = falcon.command('RTR-ListFiles', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### RTR_DeleteFile
Delete a RTR session file.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | _string_ | RTR Session file id |
| :white_check_mark: | __session_id__ | query | _string_ | RTR Session id |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'session_id': 'string'
    }

    IDS = 'ID1,ID2,ID3'

    response = falcon.RTR-DeleteFile(parameters=PARAMS, ids=IDS)
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
    'session_id': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('RTR-DeleteFile', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### RTR_ListQueuedSessions
Get queued session metadata by session ID.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | **`ids`** List of RTR sessions to retrieve.  RTR will only return the sessions that were created by the calling user |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.RTR-ListQueuedSessions(body=BODY)
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

response = falcon.command('RTR-ListQueuedSessions', body=BODY)
print(response)
falcon.deauthenticate()
```
### RTR_DeleteQueuedSession
Delete a queued session command

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __session_id__ | query | _string_ | RTR Session id |
| :white_check_mark: | __cloud_request_id__ | query | _string_ | Cloud Request ID of the executed command to query |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'session_id': 'string',
        'cloud_request_id': 'string'
    }

    response = falcon.RTR-DeleteQueuedSession(parameters=PARAMS)
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
    'session_id': 'string',
    'cloud_request_id': 'string'
}

response = falcon.command('RTR-DeleteQueuedSession', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### RTR_PulseSession
Refresh a session timeout on a single host.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | **`device_id`** The host agent ID to refresh the RTR session on.  RTR will retrieve an existing session for the calling user on this host |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.RTR-PulseSession(body=BODY)
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

response = falcon.command('RTR-PulseSession', body=BODY)
print(response)
falcon.deauthenticate()
```
### RTR_ListSessions
Get session metadata by session id.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | **`ids`** List of RTR sessions to retrieve.  RTR will only return the sessions that were created by the calling user |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.RTR-ListSessions(body=BODY)
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

response = falcon.command('RTR-ListSessions', body=BODY)
print(response)
falcon.deauthenticate()
```
### RTR_InitSession
Initialize a new session with the RTR cloud.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | **`device_id`** The host agent ID to initialize the RTR session on.  RTR will retrieve an existing session for the calling user on this host |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.RTR-InitSession(body=BODY)
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

response = falcon.command('RTR-InitSession', body=BODY)
print(response)
falcon.deauthenticate()
```
### RTR_DeleteSession
Delete a session.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __session_id__ | query | _string_ | RTR Session id |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'session_id': 'string'
    }

    response = falcon.RTR-DeleteSession(parameters=PARAMS)
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
    'session_id': 'string'
}

response = falcon.command('RTR-DeleteSession', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### RTR_ListAllSessions
Get a list of session_ids.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __offset__ | query | _string_ | Starting index of overall result set from which to return ids. |
| | __limit__ | query | _integer_ | Number of ids to return. |
| | __sort__ | query | _string_ | Sort by spec. Ex: 'date_created|asc'. |
| | __filter__ | query | _string_ | Optional filter criteria in the form of an FQL query. For more information about FQL queries, see our [FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). “user_id” can accept a special value ‘@me’ which will restrict results to records with current user’s ID. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import real_time_response as FalconRTR

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconRTR.Real_Time_Response(access_token=token)

    PARAMS = {
        'offset': 'string',
        'limit': integer,
        'sort': 'string',
        'filter': 'string'
    }

    response = falcon.RTR-ListAllSessions(parameters=PARAMS)
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
    'limit': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.command('RTR-ListAllSessions', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
