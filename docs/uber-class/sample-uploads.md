# Using the Sample Uploads service collection
![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-X%20No-red.svg)
## Table of Contents
| API Function | Description |
| :--- | :--- |
| [GetSampleV3](#getsamplev3) | Retrieves the file associated with the given ID (SHA256) |
| [UploadSampleV3](#uploadsamplev3) | Upload a file for further cloud analysis. After uploading, call the specific analysis API endpoint. |
| [DeleteSampleV3](#deletesamplev3) | Removes a sample, including file, meta and submissions from the collection |
### GetSampleV3
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

response = falcon.command('GetSampleV3', parameters=PARAMS, headers=HEADERS, ids=IDS)
print(response)
falcon.deauthenticate()
```
### UploadSampleV3
Upload a file for further cloud analysis. After uploading, call the specific analysis API endpoint.

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

response = falcon.command('UploadSampleV3', parameters=PARAMS, body=BODY, data=PAYLOAD, file_name=FILENAME, content_type='application/octet-stream', headers=HEADERS)
print(response)
falcon.deauthenticate()
```
### DeleteSampleV3
Removes a sample, including file, meta and submissions from the collection

#### Content-Type
- Produces: _application/json_
#### Parameters
| Required | Name  | Type  | Datatype | Description |
| :---: | :---- | :---- | :-------- | :---------- |
| | __X-CS-USERUUID__ | header | _string_ | User UUID |
| :white_check_mark: | __ids__ | query | _string_ | The file SHA256. |
#### Usage
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

response = falcon.command('DeleteSampleV3', headers=HEADERS, ids=IDS)
print(response)
falcon.deauthenticate()
```
