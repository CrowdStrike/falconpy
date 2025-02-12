# test_drift_indicators.py
# This class tests the drift indicators service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import DriftIndicators

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = DriftIndicators(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestDriftIndicators:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "GetDriftIndicatorsValuesByDate": falcon.get_drift_indicators_by_date(filter="cid:'12345678901234567890123456789012'"),
            "ReadDriftIndicatorsCount": falcon.read_drift_indicator_counts(filter="cid:'12345678901234567890123456789012'"),
            "ReadDriftIndicatorEntities": falcon.read_drift_indicator_entities(ids="1234567890"),
            "SearchAndReadDriftIndicatorEntities": falcon.search_and_read_drift_indicators(filter="cid:'12345678901234567890123456789012'"),
            "SearchDriftIndicators": falcon.search_drift_indicators(filter="cid:'12345678901234567890123456789012'"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                if key != "ReadDriftIndicatorEntities":  # Allow 500 temporarily
                    error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
