# test_cloud_security_assets.py
# This class tests the cloud_security_assets service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CloudSecurityAssets

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CloudSecurityAssets(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestCloudSecurityAssets:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "cloud_security_assets_combined_application_findings": falcon.combined_application_findings(crn="12345678", type="whatever"),
            "cloud_security_assets_combined_compliance_by_account": falcon.get_combined_compliance_by_account(limit=1),
            "cloud_security_assets_entities_get": falcon.get_assets("12345678"),
            "cloud_security_assets_queries": falcon.query_assets(filter="zone:'bob'"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                if key != "cloud_security_assets_combined_application_findings":
                    error_checks = False
                    # print(key)
                    # print(tests[key])
        assert error_checks
