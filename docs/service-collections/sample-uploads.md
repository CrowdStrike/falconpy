# Sample Uploads

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Sample Uploads service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [GetSampleV3](sample-uploads.md#getsamplev3) | Retrieves the file associated with the given ID \(SHA256\) |
| [UploadSampleV3](sample-uploads.md#uploadsamplev3) | Upload a file for further cloud analysis. After uploading, call the specific analysis API endpoint. |
| [DeleteSampleV3](sample-uploads.md#deletesamplev3) | Removes a sample, including file, meta and submissions from the collection |

### GetSampleV3

Retrieves the file associated with the given ID \(SHA256\)

**Content-Type**

* Produces: _application/octet-stream_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **X-CS-USERUUID** | header | _string_ | User UUID |
| :white\_check\_mark: | **ids** | query | _string_ | The file SHA256. |
|  | **password\_protected** | query | _string_ | Flag whether the sample should be zipped and password protected with pass='infected' |

**Usage**

**Service class example**

```python
from falconpy import sample_uploads as FalconSamples

falcon = FalconSamples.Sample_Uploads(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'password_protected': 'string'
}

HEADERS = {
    'X-CS-USERUUID': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.GetSampleV3(parameters=PARAMS, headers=HEADERS, ids=IDS)
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

**Content-Type**

* Consumes: _application/octet-stream_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **X-CS-USERUUID** | header | _string_ | User UUID |
| :white\_check\_mark: | **body** | body | _string_ | Content of the uploaded sample in binary format. For example, use `--data-binary @$FILE_PATH` when using cURL. Max file size: 100 MB.  Accepted file formats:  - Portable executables: `.exe`, `.scr`, `.pif`, `.dll`, `.com`, `.cpl`, etc. - Office documents: `.doc`, `.docx`, `.ppt`, `.pps`, `.pptx`, `.ppsx`, `.xls`, `.xlsx`, `.rtf`, `.pub` - PDF - APK - Executable JAR - Windows script component: `.sct` - Windows shortcut: `.lnk` - Windows help: `.chm` - HTML application: `.hta` - Windows script file: `.wsf` - Javascript: `.js` - Visual Basic: `.vbs`,  `.vbe` - Shockwave Flash: `.swf` - Perl: `.pl` - Powershell: `.ps1`, `.psd1`, `.psm1` - Scalable vector graphics: `.svg` - Python: `.py` - Linux ELF executables - Email files: MIME RFC 822 `.eml`, Outlook `.msg`. |
| :white\_check\_mark: | **upfile** | formData | _file_ | The binary file. |
| :white\_check\_mark: | **file\_name** | query | _string_ | Name of the file. |
|  | **comment** | query | _string_ | A descriptive comment to identify the file for other users. |
|  | **is\_confidential** | query | _boolean_ | Defines visibility of this file in Falcon MalQuery, either via the API or the Falcon console.  - `true`: File is only shown to users within your customer account - `false`: File can be seen by other CrowdStrike customers   Default: `true`. |

**Usage**

**Service class example**

```python
from falconpy import sample_uploads as FalconSamples

falcon = FalconSamples.Sample_Uploads(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

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

response = falcon.UploadSampleV3(parameters=PARAMS, body=BODY, data=PAYLOAD, file_name=FILENAME, content_type='application/octet-stream', headers=HEADERS)
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

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **X-CS-USERUUID** | header | _string_ | User UUID |
| :white\_check\_mark: | **ids** | query | _string_ | The file SHA256. |

**Usage**

**Service class example**

```python
from falconpy import sample_uploads as FalconSamples

falcon = FalconSamples.Sample_Uploads(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

HEADERS = {
    'X-CS-USERUUID': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.DeleteSampleV3(headers=HEADERS, ids=IDS)
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

HEADERS = {
    'X-CS-USERUUID': 'string'
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('DeleteSampleV3', headers=HEADERS, ids=IDS)
print(response)
falcon.deauthenticate()
```

