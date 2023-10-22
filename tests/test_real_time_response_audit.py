"""
test_real_time_response_audit.py - This class tests the RealTimeResponseAudit service class
"""
import os
import sys
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import RealTimeResponseAudit

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = RealTimeResponseAudit(auth_object=config)
AllowedResponses = [200, 201, 400, 404, 429]


class TestRealTimeResponseAudit:
    def run_all_tests(self):
        error_checks = True
        tests = {
            "RTRAuditSessions" : falcon.audit_sessions()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
            #     print(tests[key])

        return error_checks

    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_functionality(self):
        assert self.run_all_tests() is True
