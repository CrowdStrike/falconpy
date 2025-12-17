# test_cloud_azure_registration.py
# This class tests the cloud_azure_registration service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CloudAzureRegistration

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CloudAzureRegistration(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]

AZURE_PAYLOAD = {
  "resource": {
    "account_type": "string",
    "additional_features": [
      {
        "feature": "string",
        "product": "string",
        "subscription_ids": [
          "string"
        ]
      }
    ],
    "additional_properties": {},
    "api_client_key_id": "string",
    "api_client_key_type": "string",
    "cs_infra_region": "string",
    "cs_infra_subscription_id": "string",
    "deployment_method": "string",
    "deployment_stack_host_id": "string",
    "deployment_stack_name": "string",
    "dspm_regions": "string,string",
    "environment": "string",
    "event_hub_settings": [
      {
        "cid": "string",
        "consumer_group": "string",
        "event_hub_id": "string",
        "purpose": "string",
        "tenant_id": "string"
      }
    ],
    "management_group_ids": [
      "string"
    ],
    "microsoft_graph_permission_ids": [
      "string"
    ],
    "microsoft_graph_permission_ids_readonly": True,
    "products": [
      {
        "features": [
          "string"
        ],
        "product": "string"
      }
    ],
    "resource_name_prefix": "string",
    "resource_name_suffix": "string",
    "status": "string",
    "subscription_ids": [
      "string"
    ],
    "tags": {
      "additionalProp1": "string",
      "additionalProp2": "string",
      "additionalProp3": "string"
    },
    "template_version": "string",
    "tenant_id": "string"
  }
}

class TestCloudAzureRegistration:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "cloud_registration_azure_delete_legacy_subscription": falcon.delete_legacy_subscription(body={}),
            "cloud_registration_azure_trigger_health_check": falcon.health_check(tenant_id="12345678"),
            "cloud_registration_azure_get_registration": falcon.get_registration(tenant_id="12345678"),
            "cloud_registration_azure_create_registration": falcon.create_registration(**AZURE_PAYLOAD["resource"]),
            "cloud_registration_azure_update_registration": falcon.update_registration(**AZURE_PAYLOAD["resource"]),
            "cloud_registration_azure_delete_registration": falcon.delete_registration(tenant_ids="12345678"),
            "download_azure_script": falcon.deployment_script(tenant_id="12345678"),
            "cloud_registration_azure_download_script": falcon.download_script(tenant_id="12345678"),
            "cloud_registration_azure_validate_registration": falcon.validate_registration(tenant_id="12345678", stack_name="12345678")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
