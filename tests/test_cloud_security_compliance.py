# test_cloud_security_compliance.py
# This class tests the cloud_security_compliance service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CloudSecurityCompliance

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CloudSecurityCompliance(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestCloudSecurityCompliance:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "cloud_compliance_framework_posture_summaries": falcon.framework_posture_summaries("1ab2c345-67d8-90e1-2345-6789f0a12bc3"),
            "cloud_compliance_rule_posture_summaries": falcon.rule_posture_summaries(ids="1ab2c345-67d8-90e1-2345-6789f0a12bc3"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
