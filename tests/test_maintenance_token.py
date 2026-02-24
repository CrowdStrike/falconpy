# test_maintenance_token.py
# This class tests the MaintenanceToken service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import MaintenanceToken

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = MaintenanceToken(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestMaintenanceToken:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "incrementUninstallToken": falcon.increment_uninstall_token(audit_message="test increment"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
