"""
test_intel.py - This class tests the intel service class
"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# flake8: noqa=E401  # Classes to test - manually imported from sibling folder
from falconpy.intel import Intel

auth = Authorization.TestAuthorization()
auth.getConfig()
falcon = Intel(creds={"client_id": auth.config["falcon_client_id"],
                      "client_secret": auth.config["falcon_client_secret"]})
AllowedResponses = [200, 201, 400, 404, 429]


class TestIntel:
    """
    Intel Service Class test harness
    """
    def intel_test_all_code_paths(self):
        """
        Tests every statement within every method of the class, accepts all errors except 500
        """
        error_checks = True
        tests = {
            "query_intel_actor_entities": falcon.QueryIntelActorEntities(limit=1)["status_code"],
            "query_intel_indicator_entities": falcon.QueryIntelIndicatorEntities(parameters={"limit": 1})["status_code"],
            "query_intel_report_entities": falcon.QueryIntelReportEntities()["status_code"],
            "get_intel_actor_entities": falcon.GetIntelActorEntities(ids='12345678')["status_code"],
            "get_intel_indicator_entities": falcon.GetIntelIndicatorEntities(body={})["status_code"],
            "get_intel_report_pdf": falcon.GetIntelReportPDF(parameters={})["status_code"],
            "get_intel_report_entities": falcon.GetIntelReportEntities(ids='12345678')["status_code"],
            "get_intel_rule_file": falcon.GetIntelRuleFile(parameters={})["status_code"],
            "get_latest_intel_rule_file": falcon.GetLatestIntelRuleFile(parameters={})["status_code"],
            "get_intel_rule_entities": falcon.GetIntelRuleEntities(ids='12345678')["status_code"],
            "query_intel_actor_ids": falcon.QueryIntelActorIds()["status_code"],
            "query_intel_indicator_ids": falcon.QueryIntelIndicatorIds(limit=5)["status_code"],
            "query_intel_report_ids": falcon.QueryIntelReportIds(limit=1)["status_code"],
            "query_intel_rule_ids": falcon.QueryIntelRuleIds(parameters={"type": "common-event-format"})["status_code"]
        }
        for key in tests:
            if tests[key] not in AllowedResponses:
                error_checks = False

            # print(f"{key} operation returned a {tests[key]} status code")

        return error_checks

    def test_all_code_paths(self):
        assert self.intel_test_all_code_paths() is True

    @staticmethod
    def test_logout():
        """Pytest harness hook"""
        assert bool(falcon.auth_object.revoke(
            falcon.auth_object.token()["body"]["access_token"]
            )["status_code"] in AllowedResponses) is True
