"""
test_scheduled_reports.py - This class tests the Scheduled Reports service class
"""
import os
import sys
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ScheduledReports

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ScheduledReports(auth_object=config)
AllowedResponses = [200, 201, 400, 404, 429]


class TestScheduledReports:
    def run_all_tests(self):
        error_checks = True
        tests = {
            "get_reports": falcon.get_reports(ids='12345678'),
            "query_reports": falcon.query_reports(limit=1),
            "launch": falcon.launch(ids="12345678"),
            "launch_two": falcon.launch(ids="12345,67890"),
            "launch_three": falcon.launch(ids=["12345", "67890"])
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False

                # print(tests[key])

        return error_checks

    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_functionality(self):
        assert self.run_all_tests() is True
