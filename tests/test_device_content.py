# test_device_content.py
# This class tests the device_content service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import DeviceContent

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = DeviceContent(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestDeviceContent:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "entities_states_v1": falcon.get_states(ids="12345678"),
            "queries_states_v1": falcon.query_states(limit=1)
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
