"""
test_discover.py - This class tests the Discover service class
"""
import os
import sys
import platform
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
        hosts_id_list = "1234567890"
        if check["status_code"] == 429:
            pytest.skip("Rate limit hit")
        if check["status_code"] == 200:
            if check["body"]["resources"]:
                hosts_id_list = check["body"]["resources"]
        check = falcon.query_accounts(limit=1)
        accounts_id_list = "1234567890"
        if check["status_code"] == 429:
            pytest.skip("Rate limit hit")
        if check["status_code"] == 200:
            if check["body"]["resources"]:
                accounts_id_list = check["body"]["resources"]
        check = falcon.query_applications(limit=1)
        applications_id_list = "1234567890"
        if check["status_code"] == 429:
            pytest.skip("Rate limit hit")
        if check["status_code"] == 200:
            if check["body"]["resources"]:
                applications_id_list = check["body"]["resources"]
        check = falcon.query_logins(limit=1)
        logins_id_list = "1234567890"
        if check["status_code"] == 429:
            pytest.skip("Rate limit hit")
        if check["status_code"] == 200:
            if check["body"]["resources"]:
                logins_id_list = check["body"]["resources"]
        check = falcon.query_iot_hosts(limit=1)
        check = falcon.query_iot_hosts_v2(limit=1)
        assets_id_list = "1234567890"
        if check["status_code"] == 429:
            pytest.skip("Rate limit hit")
        if check["status_code"] == 200:
            if check["body"]["resources"]:
                assets_id_list = check["body"]["resources"]
        tests = {
            "query_and_get_accounts": falcon.get_accounts(ids=accounts_id_list),
            "query_and_get_hosts": falcon.get_hosts(ids=hosts_id_list),
            "query_and_get_logins": falcon.get_logins(ids=logins_id_list),
            "query_and_get_applications": falcon.get_applications(ids=applications_id_list),
            "query_iot_hosts": falcon.get_iot_hosts(ids=assets_id_list),
            "combined_applications": falcon.query_combined_applications(limit=1),
            "combined_hosts": falcon.query_combined_hosts(limit=1)

        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False

            # print(f"{key} operation returned a {tests[key]} status code")
            # print(tests[key])

        return error_checks

    @pytest.mark.skipif(platform.system() != "Darwin", reason="Frequency reduced due to potential race condition")
    def test_all_functionality(self):
        assert self.run_all_tests() is True
