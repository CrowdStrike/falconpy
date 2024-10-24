# test_datascanner.py
# This class tests the DataScanner service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import DataScanner

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = DataScanner(auth_object=config)
AllowedResponses = [200, 201, 207, 404, 406, 429, 500]

class TestDataScanner:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "handle": falcon.handle(),
            "get_image_registry_credentials": falcon.get_image_registry_credentials(),
            "get_data_scanner_tasks": falcon.get_data_scanner_tasks(scanner_id="12345678"),
            "update_data_scanner_tasks": falcon.update_data_scanner_tasks(scanner_id="12345678", machine_id="BOB"),
            "get_data_scanner_tasks_fail": falcon.get_data_scanner_tasks(),
            "update_data_scanner_tasks_fail": falcon.update_data_scanner_tasks(scanner_id="12345678")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
