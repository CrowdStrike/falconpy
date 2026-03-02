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
            "CombinedDetections": falcon.search_detections(),
            "RegisterAccount": falcon.register_account(aws_accounts=[{"account_number": "1"}]),
            "RegisterAccountToo": falcon.register_account(account_number="12345678"),
            "ReadDeploymentsCombined": falcon.search_scan_jobs(),
            "ReadDeploymentEntities": falcon.get_scan_jobs(ids="ABCDEF12-1234-ABCD-5678-ABCDEF123456"),
            "GetScanReport": falcon.get_scan_reports(ids="12345678"),
            "CreateDeploymentEntity": falcon.launch_scan_job(account_id="12345", asset_identifier="123456", cloud_provider="aws", region="us-east-2")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(tests[key])
                # print(f"{key} operation returned a {tests[key]['status_code']} status code")

        return error_checks

    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_get_credentials(self):
        """Pytest harness hook"""
        assert bool(falcon.get_credentials()["status_code"] in [*AllowedResponses, 500]) is True

    def test_get_credentials_iac(self):
        """Pytest harness hook"""
        assert bool(falcon.get_iac_credentials()["status_code"] in [*AllowedResponses, 500]) is True

    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_remaining_code_paths(self):
        """Pytest harness hook"""
        assert self.run_tests() is True
