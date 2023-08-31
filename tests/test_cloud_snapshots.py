"""
test_cloud_snapshots.py - This class tests the CloudSnapshots service class
"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CloudSnapshots, APIHarness

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CloudSnapshots(auth_object=config)

AllowedResponses = [200, 201, 204, 400, 404, 429]  # Allowing no content returned as code paths are confirmed


class TestCloudSnapshots:
    def run_tests(self):
        error_checks = True

        tests = {
            "RegisterAccount": falcon.register_account(aws_accounts=[{"account_number": "1"}]),
            "RegisterAccountToo": falcon.register_account(account_number="12345678"),
            "CreateInventory": falcon.create_inventory(job_metadata={"cloud_provider": "aws"}, result=[{"major_version": "1"}]),
            "CreateInventoryAlso": falcon.create_inventory(cloud_provider="aws", major_version="1", os_version="12"),
            "CreateInventoryAsWell": falcon.create_inventory(results={"applications":[]}),
            "CreateInventoryTheFourth": falcon.create_inventory(applications=[{"major_version": "42"}])
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(tests[key])
                # print(f"{key} operation returned a {tests[key]['status_code']} status code")

        return error_checks

    def test_get_credentials(self):
        """Pytest harness hook"""
        assert bool(falcon.get_credentials()["status_code"] in AllowedResponses) is True

    def test_remaining_code_paths(self):
        """Pytest harness hook"""
        assert self.run_tests() is True
