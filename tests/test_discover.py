"""
test_discover.py - This class tests the Discover service class
"""
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import Discover

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = Discover(access_token=token)
AllowedResponses = [200, 201, 403, 404, 429]  # Getting 403's atm


class TestDiscover:
    def run_all_tests(self):
        error_checks = True
        tests = {
            "query_and_get_hosts": falcon.get_hosts(ids=falcon.query_hosts(limit=1)["body"]["resources"])
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False

            # print(f"{key} operation returned a {tests[key]} status code")
            # print(tests[key])

        return error_checks

    def test_all_functionality(self):
        assert self.run_all_tests() is True
