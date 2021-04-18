# Cloud Connect AWS

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Cloud Connect AWS service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [QueryAWSAccounts](cloud-connect-aws.md#queryawsaccounts) | Search for provisioned AWS Accounts by providing an FQL filter and paging details. Returns a set of AWS accounts which match the filter criteria |
| [GetAWSSettings](cloud-connect-aws.md#getawssettings) | Retrieve a set of Global Settings which are applicable to all provisioned AWS accounts |
| [GetAWSAccounts](cloud-connect-aws.md#getawsaccounts) | Retrieve a set of AWS Accounts by specifying their IDs |
| [ProvisionAWSAccounts](cloud-connect-aws.md#provisionawsaccounts) | Provision AWS Accounts by specifying details about the accounts to provision |
| [DeleteAWSAccounts](cloud-connect-aws.md#deleteawsaccounts) | Delete a set of AWS Accounts by specifying their IDs |
| [UpdateAWSAccounts](cloud-connect-aws.md#updateawsaccounts) | Update AWS Accounts by specifying the ID of the account and details to update |
| [CreateOrUpdateAWSSettings](cloud-connect-aws.md#createorupdateawssettings) | Create or update Global Settings which are applicable to all provisioned AWS accounts |
| [VerifyAWSAccountAccess](cloud-connect-aws.md#verifyawsaccountaccess) | Performs an Access Verification check on the specified AWS Account IDs |
| [QueryAWSAccountsForIDs](cloud-connect-aws.md#queryawsaccountsforids) | Search for provisioned AWS Accounts by providing an FQL filter and paging details. Returns a set of AWS account IDs which match the filter criteria |

### QueryAWSAccounts

Search for provisioned AWS Accounts by providing an FQL filter and paging details. Returns a set of AWS accounts which match the filter criteria

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-500\]. Defaults to 100. |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **sort** | query | _string_ | The property to sort by \(e.g. alias.desc or state.asc\) |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |

**Usage**

**Service class example**

```python
from falconpy import cloud_connect_aws as FalconAWS

falcon = FalconAWS.Cloud_Connect_AWS(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'limit': integer,
    'offset': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.QueryAWSAccounts(parameters=PARAMS)
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
    'limit': integer,
    'offset': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.command('QueryAWSAccounts', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

### GetAWSSettings

Retrieve a set of Global Settings which are applicable to all provisioned AWS accounts

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

No parameters

**Usage**

**Service class example**

```python
from falconpy import cloud_connect_aws as FalconAWS

falcon = FalconAWS.Cloud_Connect_AWS(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

response = falcon.GetAWSSettings()
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

response = falcon.command('GetAWSSettings')
print(response)
falcon.deauthenticate()
```

### GetAWSAccounts

Retrieve a set of AWS Accounts by specifying their IDs

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | IDs of accounts to retrieve details |

**Usage**

**Service class example**

```python
from falconpy import cloud_connect_aws as FalconAWS

falcon = FalconAWS.Cloud_Connect_AWS(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.GetAWSAccounts(ids=IDS)
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

response = falcon.command('GetAWSAccounts', ids=IDS)
print(response)
falcon.deauthenticate()
```

### ProvisionAWSAccounts

Provision AWS Accounts by specifying details about the accounts to provision

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **mode** | query | _string_ | Mode for provisioning. Allowed values are `manual` or `cloudformation`. Defaults to manual if not defined. |
| :white\_check\_mark: | **body** | body | _string_ |  |

**Usage**

**Service class example**

```python
from falconpy import cloud_connect_aws as FalconAWS

falcon = FalconAWS.Cloud_Connect_AWS(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'mode': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.ProvisionAWSAccounts(parameters=PARAMS, body=BODY)
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
    'mode': 'string'
}

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.command('ProvisionAWSAccounts', parameters=PARAMS, body=BODY)
print(response)
falcon.deauthenticate()
```

### DeleteAWSAccounts

Delete a set of AWS Accounts by specifying their IDs

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | IDs of accounts to remove |

**Usage**

**Service class example**

```python
from falconpy import cloud_connect_aws as FalconAWS

falcon = FalconAWS.Cloud_Connect_AWS(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.DeleteAWSAccounts(ids=IDS)
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

response = falcon.command('DeleteAWSAccounts', ids=IDS)
print(response)
falcon.deauthenticate()
```

### UpdateAWSAccounts

Update AWS Accounts by specifying the ID of the account and details to update

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
from falconpy import cloud_connect_aws as FalconAWS

falcon = FalconAWS.Cloud_Connect_AWS(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.UpdateAWSAccounts(body=BODY)
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

response = falcon.command('UpdateAWSAccounts', body=BODY)
print(response)
falcon.deauthenticate()
```

### CreateOrUpdateAWSSettings

Create or update Global Settings which are applicable to all provisioned AWS accounts

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
from falconpy import cloud_connect_aws as FalconAWS

falcon = FalconAWS.Cloud_Connect_AWS(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

BODY = {
    'Body Payload': 'See body description above'
}

response = falcon.CreateOrUpdateAWSSettings(body=BODY)
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

response = falcon.command('CreateOrUpdateAWSSettings', body=BODY)
print(response)
falcon.deauthenticate()
```

### VerifyAWSAccountAccess

Performs an Access Verification check on the specified AWS Account IDs

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| :white\_check\_mark: | **ids** | query | array \(_string_\) | IDs of accounts to verify access on |

**Usage**

**Service class example**

```python
from falconpy import cloud_connect_aws as FalconAWS

falcon = FalconAWS.Cloud_Connect_AWS(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.VerifyAWSAccountAccess(ids=IDS)
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

response = falcon.command('VerifyAWSAccountAccess', ids=IDS)
print(response)
falcon.deauthenticate()
```

### QueryAWSAccountsForIDs

Search for provisioned AWS Accounts by providing an FQL filter and paging details. Returns a set of AWS account IDs which match the filter criteria

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
|  | **limit** | query | _integer_ | The maximum records to return. \[1-500\]. Defaults to 100. |
|  | **offset** | query | _integer_ | The offset to start retrieving records from |
|  | **sort** | query | _string_ | The property to sort by \(e.g. alias.desc or state.asc\) |
|  | **filter** | query | _string_ | The filter expression that should be used to limit the results |

**Usage**

**Service class example**

```python
from falconpy import cloud_connect_aws as FalconAWS

falcon = FalconAWS.Cloud_Connect_AWS(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

PARAMS = {
    'limit': integer,
    'offset': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.QueryAWSAccountsForIDs(parameters=PARAMS)
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
    'limit': integer,
    'offset': integer,
    'sort': 'string',
    'filter': 'string'
}

response = falcon.command('QueryAWSAccountsForIDs', parameters=PARAMS)
print(response)
falcon.deauthenticate()
```

