# CSPM Registration

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the CSPM Registration service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [GetCSPMAwsAccount](cspm-registration.md#getcspmawsaccount) | Returns information about the current status of an AWS account. |
| [CreateCSPMAwsAccount](cspm-registration.md#createcspmawsaccount) | Creates a new account in our system for a customer and generates a script for them to run in their AWS cloud environment to grant us access. |
| [DeleteCSPMAwsAccount](cspm-registration.md#deletecspmawsaccount) | Deletes an existing AWS account or organization in our system. |
| [GetCSPMAwsConsoleSetupURLs](cspm-registration.md#getcspmawsconsolesetupurls) | Return a URL for customer to visit in their cloud environment to grant us access to their AWS environment. |
| [GetCSPMAwsAccountScriptsAttachment](cspm-registration.md#getcspmawsaccountscriptsattachment) | Return a script for customer to run in their cloud environment to grant us access to their AWS environment as a downloadable attachment. |
| [GetCSPMAzureAccount](cspm-registration.md#getcspmazureaccount) | Return information about Azure account registration |
| [CreateCSPMAzureAccount](cspm-registration.md#createcspmazureaccount) | Creates a new account in our system for a customer and generates a script for them to run in their cloud environment to grant us access. |
| [DeleteCSPMAzureAccount](cspm-registration.md#deletecspmazureaccount) | Deletes an Azure subscription from the system. |
| [UpdateCSPMAzureAccountClientID](cspm-registration.md#updatecspmazureaccountclientid) | Update an Azure service account in our system by with the user-created client\_id created with the public key we've provided |
| [GetCSPMAzureUserScriptsAttachment](cspm-registration.md#getcspmazureuserscriptsattachment) | Return a script for customer to run in their cloud environment to grant us access to their Azure environment as a downloadable attachment |
| [GetCSPMPolicy](cspm-registration.md#getcspmpolicy) | Given a policy ID, returns detailed policy information. |
| [GetCSPMPolicySettings](cspm-registration.md#getcspmpolicysettings) | Returns information about current policy settings. |
| [UpdateCSPMPolicySettings](cspm-registration.md#updatecspmpolicysettings) | Updates a policy setting - can be used to override policy severity or to disable a policy entirely. |
| [GetCSPMScanSchedule](cspm-registration.md#getcspmscanschedule) | Returns scan schedule configuration for one or more cloud platforms. |
| [UpdateCSPMScanSchedule](cspm-registration.md#updatecspmscanschedule) | Updates scan schedule configuration for one or more cloud platforms. |

### GetCSPMAwsAccount

Returns information about the current status of an AWS account.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **scan-type** | query | _string_ | Type of scan, dry or full, to perform on selected accounts |
|  | **ids** | query | array \(_string_\) | AWS account IDs |
|  | **organization-ids** | query | array \(_string_\) | AWS organization IDs |
|  | **status** | query | _string_ | Account status to filter results by. |
|  | **limit** | query | _integer_ | The maximum records to return. Defaults to 100. |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'scan-type': 'string',
    'organization-ids': [
       'string',
       'string'
    ],
    'status': 'string',
    'limit': integer,
    'offset': integer
}

IDS = 'ID1,ID2,ID3'

response = falcon.GetCSPMAwsAccount(parameters=PARAMS, ids=IDS)
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
    'scan-type': 'string',
    'organization-ids': [
       'string',
       'string'
    ],
    'status': 'string',
    'limit': integer,
    'offset': integer
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('GetCSPMAwsAccount', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```

### CreateCSPMAwsAccount

Creates a new account in our system for a customer and generates a script for them to run in their AWS cloud environment to grant us access.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.CreateCSPMAwsAccount(body=BODY)
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

response = falcon.command('CreateCSPMAwsAccount', body=BODY)
print(response)
falcon.deauthenticate()
```

### DeleteCSPMAwsAccount

Deletes an existing AWS account or organization in our system.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **ids** | query | array \(_string_\) | AWS account IDs to remove |
|  | **organization-ids** | query | array \(_string_\) | AWS organization IDs to remove |

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'organization-ids': [
       'string',
       'string'
    ]
}

IDS = 'ID1,ID2,ID3'

response = falcon.DeleteCSPMAwsAccount(parameters=PARAMS, ids=IDS)
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
    'organization-ids': [
       'string',
       'string'
    ]
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('DeleteCSPMAwsAccount', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```

### GetCSPMAwsConsoleSetupURLs

Return a URL for customer to visit in their cloud environment to grant us access to their AWS environment.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

No parameters

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

response = falcon.GetCSPMAwsConsoleSetupURLs()
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

response = falcon.command('GetCSPMAwsConsoleSetupURLs')
print(response)
falcon.deauthenticate()
```

### GetCSPMAwsAccountScriptsAttachment

Return a script for customer to run in their cloud environment to grant us access to their AWS environment as a downloadable attachment.

**Content-Type**

* Produces: _application/json_

**Parameters**

No parameters

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

response = falcon.GetCSPMAwsAccountScriptsAttachment()
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

response = falcon.command('GetCSPMAwsAccountScriptsAttachment')
print(response)
falcon.deauthenticate()
```

### GetCSPMAzureAccount

Return information about Azure account registration

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **ids** | query | array \(_string_\) | SubscriptionIDs of accounts to select for this status operation. If this is empty then all accounts are returned. |
|  | **scan-type** | query | _string_ | Type of scan, dry or full, to perform on selected accounts |
|  | **status** | query | _string_ | Account status to filter results by. |
|  | **limit** | query | _integer_ | The maximum records to return. Defaults to 100. |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'scan-type': 'string',
    'status': 'string',
    'limit': integer,
    'offset': integer
}

IDS = 'ID1,ID2,ID3'

response = falcon.GetCSPMAzureAccount(parameters=PARAMS, ids=IDS)
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
    'scan-type': 'string',
    'status': 'string',
    'limit': integer,
    'offset': integer
}

IDS = 'ID1,ID2,ID3'

response = falcon.command('GetCSPMAzureAccount', parameters=PARAMS, ids=IDS)
print(response)
falcon.deauthenticate()
```

### CreateCSPMAzureAccount

Creates a new account in our system for a customer and generates a script for them to run in their cloud environment to grant us access.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.CreateCSPMAzureAccount(body=BODY)
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

response = falcon.command('CreateCSPMAzureAccount', body=BODY)
print(response)
falcon.deauthenticate()
```

### DeleteCSPMAzureAccount

Deletes an Azure subscription from the system.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | Azure subscription IDs to remove |

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.DeleteCSPMAzureAccount(ids=IDS)
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

response = falcon.command('DeleteCSPMAzureAccount', ids=IDS)
print(response)
falcon.deauthenticate()
```

### UpdateCSPMAzureAccountClientID

Update an Azure service account in our system by with the user-created client\_id created with the public key we've provided

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **id** | query | _string_ | ClientID to use for the Service Principal associated with the customer's Azure account |
|  | **tenant-id** | query | _string_ | Tenant ID to update client ID for. Required if multiple tenants are registered. |
| :white\_check\_mark: | **body** | body | _string_ | This is a placeholder only. Please ignore this field. |

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'id': 'string',
    'tenant-id': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.UpdateCSPMAzureAccountClientID(parameters=PARAMS, body=BODY)
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
    'id': 'string',
    'tenant-id': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.command('UpdateCSPMAzureAccountClientID', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```

### GetCSPMAzureUserScriptsAttachment

Return a script for customer to run in their cloud environment to grant us access to their Azure environment as a downloadable attachment

**Content-Type**

* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **tenant-id** | query | _string_ | Tenant ID to generate script for. Defaults to most recently registered tenant. |

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'tenant-id': 'string'
}

response = falcon.GetCSPMAzureUserScriptsAttachment(parameters=PARAMS)
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
    'tenant-id': 'string'
}

response = falcon.command('GetCSPMAzureUserScriptsAttachment', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### GetCSPMPolicy

Given a policy ID, returns detailed policy information.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | _string_ | Policy ID |

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.GetCSPMPolicy(ids=IDS)
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

response = falcon.command('GetCSPMPolicy', ids=IDS)
print(response)
falcon.deauthenticate()
```

### GetCSPMPolicySettings

Returns information about current policy settings.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **service** | query | _string_ | Service type to filter policy settings by. |
|  | **policy-id** | query | _string_ | Policy ID |

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'service': 'string',
    'policy-id': 'string'
}

response = falcon.GetCSPMPolicySettings(parameters=PARAMS)
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
    'service': 'string',
    'policy-id': 'string'
}

response = falcon.command('GetCSPMPolicySettings', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### UpdateCSPMPolicySettings

Updates a policy setting - can be used to override policy severity or to disable a policy entirely.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.UpdateCSPMPolicySettings(body=BODY)
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

response = falcon.command('UpdateCSPMPolicySettings', body=BODY)
print(response)
falcon.deauthenticate()
```

### GetCSPMScanSchedule

Returns scan schedule configuration for one or more cloud platforms.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **cloud-platform** | query | array \(_string_\) | Cloud Platform |

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'cloud-platform': [
       'string',
       'string'
    ]
}

response = falcon.GetCSPMScanSchedule(parameters=PARAMS)
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
    'cloud-platform': [
       'string',
       'string'
    ]
}

response = falcon.command('GetCSPMScanSchedule', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### UpdateCSPMScanSchedule

Updates scan schedule configuration for one or more cloud platforms.

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import cspm_registration as FalconCSPM

falcon = FalconCSPM.CSPM_Registration(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.UpdateCSPMScanSchedule(body=BODY)
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

response = falcon.command('UpdateCSPMScanSchedule', body=BODY)
print(response)
falcon.deauthenticate()
```

