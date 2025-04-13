# test_faas_execution.py
# This class tests the faas_execution service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import FaaSExecution

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FaaSExecution(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 429]


class TestFaaSExecution:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "ReadRequestBody": falcon.read_request_body(id="whatever", sha256="whatever", fn="whatever", filename="whatever")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
