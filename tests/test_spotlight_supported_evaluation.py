# test_spotlight_supported_evaluation.py
# This class tests the SpotlightSupportedEvaluation service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import SpotlightSupportedEvaluation

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = SpotlightSupportedEvaluation(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestSpotlightSupportedEvaluation:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "combinedSupportedEvaluationExt": falcon.get_supported_evaluations(filter="risk_provider:'S'"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
