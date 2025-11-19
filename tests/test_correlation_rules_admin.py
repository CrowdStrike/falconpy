# test_cloud_security_rules_admin.py
# This class tests the CorrelationRulesAdmin service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CorrelationRulesAdmin

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CorrelationRulesAdmin(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestCloudSecurityAssets:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "entities_rules_ownership_put_v1": falcon.change_correlation_rule_owner(body={}),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
            # print(key)
            # print(tests[key])
        assert error_checks
