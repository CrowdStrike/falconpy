# test_cloud_google_cloud_registration.py
# This class tests the cloud_google_cloud_registration service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CloudGoogleCloudRegistration

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CloudGoogleCloudRegistration(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestCloudGoogleCloudRegistration:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "cloud_registration_gcp_trigger_health_check": falcon.trigger_health_check(ids="12345678"),
            "cloud_registration_gcp_get_registration": falcon.get_registration(ids="12345678"),
            "cloud_registration_gcp_put_registration": falcon.update_registration(body={}),
            "cloud_registration_gcp_create_registration": falcon.create_registration(body={}),
            "cloud_registration_gcp_update_registration": falcon.cloud_registration_gcp_update_registration(ids="12345678", body={}),
            "cloud_registration_gcp_delete_registration": falcon.delete_registration(ids="12345678")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                if not (key == "cloud_registration_gcp_trigger_health_check" and tests[key]["status_code"] == 500):
                    error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
