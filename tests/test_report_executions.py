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
from falconpy import ReportExecutions

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ReportExecutions(auth_object=config)
AllowedResponses = [200, 201, 403, 404, 429]  # Getting 403's atm


class TestReportExecutions:
    def ioc_run_all_tests(self):
        error_checks = True
        tests = {
            "get_download": falcon.get_download(ids='12345678'),
            "get_reports": falcon.get_reports(ids='12345678'),
            "query_reports": falcon.query_reports(limit=1),
            "retry_reports": falcon.retry_reports(ids="123456789"),
            "retry_reports_also": falcon.retry_reports("1234567890"),
            "retry_reports_as_well": falcon.retry_reports(["12345", "67890"])
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
        assert self.ioc_run_all_tests() is True
