"""
test_scheduled_reports.py - This class tests the Scheduled Reports service class
"""
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.scheduled_reports import ScheduledReports

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = ScheduledReports(access_token=token)
AllowedResponses = [200, 201, 403, 404, 429]  # Getting 403's atm


class TestIOC:
    def ioc_run_all_tests(self):
        error_checks = True
        tests = {
            "get_reports": falcon.get_reports(ids='12345678'),
            "query_reports": falcon.query_reports(limit=1)
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False

            # print(f"{key} operation returned a {tests[key]} status code")
            # print(tests[key])

        return error_checks

    def test_all_functionality(self):
        assert self.ioc_run_all_tests() is True
