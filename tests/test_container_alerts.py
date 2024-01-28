# test_container_alerts.py
# This class tests the container alerts service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ContainerAlerts

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ContainerAlerts(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 404, 429]


class TestContainerAlerts:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "read_counts_by_severity": falcon.read_counts_by_severity(filter="cid:'12345678901234567890123456789012"),
            "read_counts": falcon.read_counts(filter="cid:'12345678901234567890123456789012"),
            "search_and_read": falcon.search_and_read(limit=1)
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
