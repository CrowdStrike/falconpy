# Using the Falconx Sandbox service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [GetArtifacts](#getartifacts) | Download IOC packs, PCAP files, and other analysis artifacts. |
| [GetSummaryReports](#getsummaryreports) | Get a short summary version of a sandbox report. |
| [GetReports](#getreports) | Get a full sandbox report. |
| [DeleteReport](#deletereport) | Delete report based on the report ID. Operation can be checked for success by polling for the report ID on the report-summaries endpoint. |
| [GetSubmissions](#getsubmissions) | Check the status of a sandbox analysis. Time required for analysis varies but is usually less than 15 minutes. |
| [Submit](#submit) | Submit an uploaded file or a URL for sandbox analysis. Time required for analysis varies but is usually less than 15 minutes. |
| [QueryReports](#queryreports) | Find sandbox reports by providing an FQL filter and paging details. Returns a set of report IDs that match your criteria. |
| [QuerySubmissions](#querysubmissions) | Find submission IDs for uploaded files by providing an FQL filter and paging details. Returns a set of submission IDs that match your criteria. |
| [GetSampleV2](#getsamplev2) | Retrieves the file associated with the given ID (SHA256) |
| [UploadSampleV2](#uploadsamplev2) | Upload a file for sandbox analysis. After uploading, use `/falconx/entities/submissions/v1` to start analyzing the file. |
| [DeleteSampleV2](#deletesamplev2) | Removes a sample, including file, meta and submissions from the collection |
| [QuerySampleV1](#querysamplev1) | Retrieves a list with sha256 of samples that exist and customer has rights to access them, maximum number of accepted items is 200 |
### GetArtifacts
Download IOC packs, PCAP files, and other analysis artifacts.

#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __id__ | query | _string_ | ID of an artifact, such as an IOC pack, PCAP file, or actor image. Find an artifact ID in a report or summary. |
| | __name__ | query | _string_ | The name given to your downloaded file. |
| | __Accept-Encoding__ | header | _string_ | Format used to compress your downloaded file. Currently, you must provide the value `gzip`, the only valid format. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import falconx_sandbox as FalconX

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconX.FalconX_Sandbox(access_token=token)

    PARAMS = {
        'id': 'string',
        'name': 'string'
    }

    HEADERS = {
        'Accept-Encoding': 'string'
    }

    response = falcon.GetArtifacts(parameters=PARAMS, headers=HEADERS)
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
    'name': 'string'
}

HEADERS = {
    'Accept-Encoding': 'string'
}

response = falcon.command('GetArtifacts', parameters=PARAMS, headers=HEADERS)
print(response)
falcon.deauthenticate()
```
### GetSummaryReports
Get a short summary version of a sandbox report.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | ID of a summary. Find a summary ID from the response when submitting a malware sample or search with `/falconx/queries/reports/v1`. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import falconx_sandbox as FalconX

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconX.FalconX_Sandbox(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.GetSummaryReports(ids=IDS)
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

response = falcon.command('GetSummaryReports', ids=IDS)
print(response)
falcon.deauthenticate()
```
### GetReports
Get a full sandbox report.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | ID of a report. Find a report ID from the response when submitting a malware sample or search with `/falconx/queries/reports/v1`. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import falconx_sandbox as FalconX

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconX.FalconX_Sandbox(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.GetReports(ids=IDS)
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

response = falcon.command('GetReports', ids=IDS)
print(response)
falcon.deauthenticate()
```
### DeleteReport
Delete report based on the report ID. Operation can be checked for success by polling for the report ID on the report-summaries endpoint.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | _string_ | ID of a report. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import falconx_sandbox as FalconX

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconX.FalconX_Sandbox(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.DeleteReport(ids=IDS)
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

response = falcon.command('DeleteReport', ids=IDS)
print(response)
falcon.deauthenticate()
```
### GetSubmissions
Check the status of a sandbox analysis. Time required for analysis varies but is usually less than 15 minutes.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __ids__ | query | array (_string_) | ID of a submitted malware sample. Find a submission ID from the response when submitting a malware sample or search with `/falconx/queries/submissions/v1`. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import falconx_sandbox as FalconX

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconX.FalconX_Sandbox(access_token=token)

    IDS = 'ID1,ID2,ID3'

    response = falcon.GetSubmissions(ids=IDS)
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

response = falcon.command('GetSubmissions', ids=IDS)
print(response)
falcon.deauthenticate()
```
### Submit
Submit an uploaded file or a URL for sandbox analysis. Time required for analysis varies but is usually less than 15 minutes.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| :white_check_mark: | __body__ | body | _string_ | Submit either a URL or a sample SHA256 for sandbox analysis. The sample file must have been previously uploaded through `/samples/entities/samples/v2`. You must specify a JSON object that includes the `falconx.SubmissionParametersV1` key/value pairs shown below.  **`environment_id`**: Specifies the sandbox environment used for analysis. Values:  - `300`: Linux Ubuntu 16.04, 64-bit - `200`: Android (static analysis) - `160`: Windows 10, 64-bit - `110`: Windows 7, 64-bit - `100`: Windows 7, 32-bit  **`sha256`** ID of the sample, which is a SHA256 hash value. Find a sample ID from the response when uploading a malware sample or search with `/falconx/queries/submissions/v1`.The `url` parameter must be unset if `sha256` is used.  **`url`** A web page or file URL. It can be HTTP(S) or FTP. The `sha256` parameter must be unset if `url` is used.  **`action_script`** (optional): Runtime script for sandbox analysis. Values:  - `default` - `default_maxantievasion` - `default_randomfiles` - `default_randomtheme` - `default_openie`  **`command_line`** (optional): Command line script passed to the submitted file at runtime. Max length: 2048 characters  **`document_password`** (optional): Auto-filled for Adobe or Office files that prompt for a password. Max length: 32 characters  **`enable_tor`** (optional): If `true`, sandbox analysis routes network traffic via TOR. Default: `false`.  **`submit_name`** (optional): Name of the malware sample that's used for file type detection and analysis  **`system_date`** (optional): Set a custom date in the format `yyyy-MM-dd` for the sandbox environment  **`system_time`** (optional): Set a custom time in the format `HH:mm` for the sandbox environment. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import falconx_sandbox as FalconX

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconX.FalconX_Sandbox(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    response = falcon.Submit(body=BODY)
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

response = falcon.command('Submit', body=BODY)
print(response)
falcon.deauthenticate()
```
### QueryReports
Find sandbox reports by providing an FQL filter and paging details. Returns a set of report IDs that match your criteria.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __filter__ | query | _string_ | Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
| | __offset__ | query | _string_ | The offset to start retrieving reports from. |
| | __limit__ | query | _integer_ | Maximum number of report IDs to return. Max: 5000. |
| | __sort__ | query | _string_ | Sort order: `asc` or `desc`. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import falconx_sandbox as FalconX

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconX.FalconX_Sandbox(access_token=token)

    PARAMS = {
        'filter': 'string',
        'offset': 'string',
        'limit': integer,
        'sort': 'string'
    }

    response = falcon.QueryReports(parameters=PARAMS)
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

response = falcon.command('QueryReports', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### QuerySubmissions
Find submission IDs for uploaded files by providing an FQL filter and paging details. Returns a set of submission IDs that match your criteria.

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __filter__ | query | _string_ | Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide). |
| | __offset__ | query | _string_ | The offset to start retrieving submissions from. |
| | __limit__ | query | _integer_ | Maximum number of submission IDs to return. Max: 5000. |
| | __sort__ | query | _string_ | Sort order: `asc` or `desc`. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import falconx_sandbox as FalconX

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconX.FalconX_Sandbox(access_token=token)

    PARAMS = {
        'filter': 'string',
        'offset': 'string',
        'limit': integer,
        'sort': 'string'
    }

    response = falcon.QuerySubmissions(parameters=PARAMS)
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

response = falcon.command('QuerySubmissions', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```
### GetSampleV2
Retrieves the file associated with the given ID (SHA256)

#### Content-Type
- Produces: _application/octet-stream_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __X-CS-USERUUID__ | header | _string_ | User UUID |
| :white_check_mark: | __ids__ | query | _string_ | The file SHA256. |
| | __password_protected__ | query | _string_ | Flag whether the sample should be zipped and password protected with pass='infected' |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import falconx_sandbox as FalconX

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconX.FalconX_Sandbox(access_token=token)

    PARAMS = {
        'password_protected': 'string'
    }

    HEADERS = {
        'X-CS-USERUUID': 'string'
    }

    IDS = 'ID1,ID2,ID3'

    response = falcon.GetSampleV2(parameters=PARAMS, headers=HEADERS, ids=IDS)
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
    'password_protected': 'string'
}

HEADERS = {
    'X-CS-USERUUID': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('GetSampleV2', parameters=PARAMS, headers=HEADERS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### UploadSampleV2
Upload a file for sandbox analysis. After uploading, use `/falconx/entities/submissions/v1` to start analyzing the file.

#### Content-Type
- Consumes: _application/octet-stream_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __X-CS-USERUUID__ | header | _string_ | User UUID |
| :white_check_mark: | __body__ | body | _string_ | Content of the uploaded sample in binary format. For example, use `--data-binary @$FILE_PATH` when using cURL. Max file size: 100 MB.  Accepted file formats:  - Portable executables: `.exe`, `.scr`, `.pif`, `.dll`, `.com`, `.cpl`, etc. - Office documents: `.doc`, `.docx`, `.ppt`, `.pps`, `.pptx`, `.ppsx`, `.xls`, `.xlsx`, `.rtf`, `.pub` - PDF - APK - Executable JAR - Windows script component: `.sct` - Windows shortcut: `.lnk` - Windows help: `.chm` - HTML application: `.hta` - Windows script file: `.wsf` - Javascript: `.js` - Visual Basic: `.vbs`,  `.vbe` - Shockwave Flash: `.swf` - Perl: `.pl` - Powershell: `.ps1`, `.psd1`, `.psm1` - Scalable vector graphics: `.svg` - Python: `.py` - Linux ELF executables - Email files: MIME RFC 822 `.eml`, Outlook `.msg`. |
| :white_check_mark: | __upfile__ | formData | _file_ | The binary file. |
| :white_check_mark: | __file_name__ | query | _string_ | Name of the file. |
| | __comment__ | query | _string_ | A descriptive comment to identify the file for other users. |
| | __is_confidential__ | query | _boolean_ | Defines visibility of this file in Falcon MalQuery, either via the API or the Falcon console.  - `true`: File is only shown to users within your customer account - `false`: File can be seen by other CrowdStrike customers   Default: `true`. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import falconx_sandbox as FalconX

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconX.FalconX_Sandbox(access_token=token)

    PARAMS = {
        'file_name': 'string',
        'comment': 'string',
        'is_confidential': boolean
    }

    BODY = {
        'Body Payload': 'See body description above'
    }

    FILENAME = 'testfile.jpg'
    PAYLOAD = open(FILENAME, 'rb').read()

    HEADERS = {
        'X-CS-USERUUID': 'string'
    }

    response = falcon.UploadSampleV2(parameters=PARAMS, body=BODY, data=PAYLOAD, file_name=FILENAME, content_type='application/octet-stream', headers=HEADERS)
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
    'file_name': 'string',
    'comment': 'string',
    'is_confidential': boolean
}

BODY = {
    'Body Payload': 'See body description above'
}

FILENAME = 'testfile.jpg'
PAYLOAD = open(FILENAME, 'rb').read()

HEADERS = {
    'X-CS-USERUUID': 'string'
}

response = falcon.command('UploadSampleV2', parameters=PARAMS, body=BODY, data=PAYLOAD, file_name=FILENAME, content_type='application/octet-stream', headers=HEADERS)
print(response)
falcon.deauthenticate()
```
### DeleteSampleV2
Removes a sample, including file, meta and submissions from the collection

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __X-CS-USERUUID__ | header | _string_ | User UUID |
| :white_check_mark: | __ids__ | query | _string_ | The file SHA256. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import falconx_sandbox as FalconX

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconX.FalconX_Sandbox(access_token=token)

    HEADERS = {
        'X-CS-USERUUID': 'string'
    }

    IDS = 'ID1,ID2,ID3'

    response = falcon.DeleteSampleV2(headers=HEADERS, ids=IDS)
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

HEADERS = {
    'X-CS-USERUUID': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('DeleteSampleV2', headers=HEADERS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### QuerySampleV1
Retrieves a list with sha256 of samples that exist and customer has rights to access them, maximum number of accepted items is 200

#### Content-Type
- Consumes: _application/json_
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __X-CS-USERUUID__ | header | _string_ | User UUID |
| :white_check_mark: | __body__ | body | _string_ | Pass a list of sha256s to check if the exist. It will be returned the list of existing hashes. |
#### Usage
##### Service class example
```python
from falconpy import oauth2 as FalconAuth
from falconpy import falconx_sandbox as FalconX

authorization = FalconAuth.OAuth2(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

try:
     token = authorization.token()['body']['access_token']
except:
     token = False

if token:
    falcon = FalconX.FalconX_Sandbox(access_token=token)

    BODY = {
        'Body Payload': 'See body description above'
    }

    HEADERS = {
        'X-CS-USERUUID': 'string'
    }

    response = falcon.QuerySampleV1(body=BODY, headers=HEADERS)
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
    'X-CS-USERUUID': 'string'
}

response = falcon.command('QuerySampleV1', body=BODY, headers=HEADERS)
print(response)
falcon.deauthenticate()
```
