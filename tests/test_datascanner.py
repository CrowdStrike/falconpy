# test_certificate_based_exclusions.py
# This class tests the CertificateBasedExclusions service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Classes to test - manually imported from sibling folder
from falconpy import DataScanner
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = DataScanner(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 404, 429, 500]


class TestDataScanner:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "get_image_registry_credentials": falcon.get_image_registry_credentials(),
            "get_data_scanner_tasks": falcon.get_data_scanner_tasks(),
            "update_data_scanner_tasks": falcon.update_data_scanner_tasks()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
