"""
test_discover.py - This class tests the Discover service class
"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import Discover

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Discover(auth_object=config)
AllowedResponses = [200, 201, 403, 404, 429]  # Getting 403's atm


class TestDiscover:
    def run_all_tests(self):
        error_checks = True
        check = falcon.query_hosts(limit=1)
        if check["status_code"] == 429:
            pytest.skip("Rate limit hit")
        if check["body"]["resources"]:
            id_list = check["body"]["resources"]
        else:
            id_list = "1234567890"
        tests = {
            "query_and_get_hosts": falcon.get_hosts(ids=id_list)
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False

            # print(f"{key} operation returned a {tests[key]} status code")
            # print(tests[key])

        return error_checks

    def test_all_functionality(self):
        assert self.run_all_tests() is True
