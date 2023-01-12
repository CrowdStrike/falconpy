"""
test_tailored_intelligence.py - This class tests the TailoredIntelligence service class
"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import TailoredIntelligence

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = TailoredIntelligence(auth_object=config)

AllowedResponses = [200, 201, 404, 429]


class TestTailoredIntelligence:
    def run_tests(self):
        error_checks = True

        tests = {
            "GetEventsBody": falcon.get_event_body("12345678"),
            "GetEventsEntities": falcon.get_event_entities("123456789"),
            "GetEventsEntities": falcon.get_event_entities(ids="123456789"),
            "QueryEvents": falcon.query_events(),
            "GetRulesEntities": falcon.get_rule_entities("123456789"),
            "GetRulesEntities": falcon.get_rule_entities(ids="123456789"),
            "QueryRules": falcon.query_rules()
        }
        for key in tests:
            if not isinstance(tests[key], bytes):  # GetEventsBody returns a binary object
                if tests[key]["status_code"] not in AllowedResponses:
                    error_checks = False
                    # print(tests[key])
                    # print(f"{key} operation returned a {tests[key]['status_code']} status code")

        return error_checks

    @pytest.mark.skipif(falcon.base_url.lower() != "https://api.crowdstrike.com",
                        reason="US-1 unit testing only"
                        )
    def test_all_code_paths(self):
        """Pytest harness hook"""
        assert self.run_tests() is True
