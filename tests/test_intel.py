"""This class tests the intel service class"""
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
token = auth.getConfigExtended()
falcon = Intel(access_token=token)
AllowedResponses = [200, 201, 400, 404, 429]


class TestIntel:
    """Intel Service Class test harness"""
    def intel_test_all_code_paths(self):
        """Tests every statement within every method of the class, accepts all errors except 500"""
        error_checks = True
        tests = {
            "query_intel_actor_entities": falcon.QueryIntelActorEntities(limit=1),
            "query_intel_indicator_entities": falcon.QueryIntelIndicatorEntities(parameters={"limit": 1}),
            "query_intel_report_entities": falcon.QueryIntelReportEntities(),
            "get_intel_actor_entities": falcon.GetIntelActorEntities(ids='12345678'),
            "get_intel_indicator_entities": falcon.GetIntelIndicatorEntities(body={"ids":["1234567"]}),
            "get_intel_indicator_entities_also": falcon.GetIntelIndicatorEntities("1234567"),
            "get_intel_report_pdf": falcon.GetIntelReportPDF(parameters={}),
            "get_intel_report_entities": falcon.GetIntelReportEntities(ids='12345678'),
            "get_intel_rule_file": falcon.GetIntelRuleFile(parameters={}),
            "get_latest_intel_rule_file": falcon.GetLatestIntelRuleFile(parameters={}),
            "get_intel_rule_entities": falcon.GetIntelRuleEntities(ids='12345678'),
            "query_intel_actor_ids": falcon.QueryIntelActorIds(),
            "query_intel_indicator_ids": falcon.QueryIntelIndicatorIds(limit=5),
            "query_intel_report_ids": falcon.QueryIntelReportIds(limit=1),
            "query_intel_rule_ids": falcon.QueryIntelRuleIds(parameters={"type": "common-event-format"})
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                # print(tests[key])    
                error_checks = False

            # print(f"{key} operation returned a {tests[key]} status code")

        return error_checks

    def test_all_code_paths(self):
        assert self.intel_test_all_code_paths() is True
