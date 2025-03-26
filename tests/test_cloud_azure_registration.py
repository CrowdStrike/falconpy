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
AllowedResponses = [200, 201, 207, 400, 403, 429]


class TestCloudAzureRegistration:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "cloud_registration_azure_download_script": falcon.download_script(tenant_id="12345678")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
