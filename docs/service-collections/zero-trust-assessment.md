# Zero Trust Assessment

![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png) [![Twitter URL](https://img.shields.io/twitter/url?label=Follow%20%40CrowdStrike&style=social&url=https%3A%2F%2Ftwitter.com%2FCrowdStrike)](https://twitter.com/CrowdStrike)

## Using the Zero Trust Assessment service collection

![Uber class support](https://img.shields.io/badge/Uber%20class%20support-%E2%9C%93%20Yes-green.svg) ![Uber class support](https://img.shields.io/badge/Service%20class%20support-%E2%9C%93%20Yes-green.svg)

### Table of Contents

| API Function | Description |
| :--- | :--- |
| [getAssessmentV1](zero-trust-assessment.md#getassessmentv1) | Get Zero Trust Assessment data for one or more hosts by providing agent IDs \(AID\) and a customer ID \(CID\). |

### getAssessmentV1

Get Zero Trust Assessment data for one or more hosts by providing agent IDs \(AID\) and a customer ID \(CID\).

**Content-Type**

* Consumes: _application/json_
* Produces: _application/json_

**Parameters**

| Required | Name | Type | Datatype | Description |
| :---: | :--- | :--- | :--- | :--- |
| ✅ | **ids** | query | array \(_string_\) | One or more agent IDs, which you can find in the data.zta file, or the Falcon console. |

**Usage**

**Service class example**

```python
from falconpy import zero_trust_assessment as FalconZTA

falcon = FalconZTA.Zero_Trust_Assessment(creds={
     'client_id': falcon_client_id,
     'client_secret': falcon_client_secret
})

IDS = 'ID1,ID2,ID3'

response = falcon.getAssessmentV1(ids=IDS)
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

response = falcon.command('getAssessmentV1', ids=IDS)
print(response)
falcon.deauthenticate()
```

