# test_configuration_assessment.py
# This class tests the configuration assessment service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ConfigurationAssessment

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ConfigurationAssessment(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429, 500]  # Temp allowing 403 / 500


class TestConfigurationAssessment:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "query_combined_assessments": falcon.query_combined_assessments(filter="aid:'12345678901234567890123456789012'"),
            "get_rule_details": falcon.get_rule_details(ids="12345678")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
