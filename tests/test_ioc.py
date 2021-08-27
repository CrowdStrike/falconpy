# test_ioc.py
# This class tests the IOC service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.ioc import IOC

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = IOC(access_token=token)
AllowedResponses = [200, 201, 404, 429]


class TestIOC:
    def ioc_run_all_tests(self):
        error_checks = True
        tests = {
            "indicator_combined": falcon.indicator_combined_v1(limit=1)["status_code"],
            "indicator_get": falcon.indicator_get_v1(ids='12345678')["status_code"],
            "indicator_create": falcon.indicator_create_v1(body={})["status_code"],
            "indicator_delete": falcon.indicator_delete_v1(ids='12345678')["status_code"],
            "indicator_update": falcon.indicator_update_v1(body={})["status_code"],
            "indicator_search": falcon.indicator_search_v1(parameters={'limit': 1})["status_code"],
        }
        for key in tests:
            if tests[key] not in AllowedResponses:
                error_checks = False

            # print(f"{key} operation returned a {tests[key]} status code")

        return error_checks

    def test_all_functionality(self):
        assert self.ioc_run_all_tests() is True

    # @staticmethod
    # def test_logout():
    #     """Pytest harness hook"""
    #     assert bool(falcon.auth_object.revoke(
    #         falcon.auth_object.token()["body"]["access_token"]
    #         )["status_code"] in AllowedResponses) is True
