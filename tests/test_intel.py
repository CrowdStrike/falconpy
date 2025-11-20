"""This class tests the intel service class"""
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# flake8: noqa=E401  # Classes to test - manually imported from sibling folder
from falconpy.intel import Intel
from falconpy import BaseURL
auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Intel(auth_object=config)
AllowedResponses = [200, 201, 400, 403, 404, 429]


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
            "get_latest_intel_rule_file": falcon.GetLatestIntelRuleFile(parameters={}, if_none_match="whatevs", if_modified_since="01/01/2020"),
            "get_intel_rule_entities": falcon.GetIntelRuleEntities(ids='12345678'),
            "query_intel_actor_ids": falcon.QueryIntelActorIds(),
            "query_intel_indicator_ids": falcon.QueryIntelIndicatorIds(limit=5),
            "query_intel_report_ids": falcon.QueryIntelReportIds(limit=1),
            "query_intel_rule_ids": falcon.QueryIntelRuleIds(parameters={"type": "common-event-format"}),
            "query_mitre_attacks": falcon.QueryMitreAttacks("fancy-bear"),
            "mitre_attacks": falcon.PostMitreAttacks(["fancy-bear", "slippy-spider"]),
            "get_mitre_report": falcon.GetMitreReport(actor_id="fancy-bear", format="CSV"),
            "GetMalwareMitreReport": falcon.get_malware_report(id="fancy-bear"),
            "query_malware_entities": falcon.query_malware_entities(limit=5),
            # "get_vulnerabilities": falcon.get_vulnerabilities(ids="12345678"),
            # "query_vulnerabilities": falcon.query_vulnerabilities()
        }

        if falcon.base_url.replace("https://", "") == BaseURL["US1"].value:
            # US-1 only for now.
            tests["get_vulnerabilities"] = falcon.get_vulnerabilities(ids="12345678")
            tests["query_vulnerabilities"] = falcon.query_vulnerabilities()
            tests["get_malware_entities"] = falcon.get_malware_entities("fancy-bear")
            tests["query_mitre_attacks_for_malware"] = falcon.query_mitre_attacks_for_malware(ids="fancy-bear")
            tests["query_malware"] = falcon.query_malware(limit=1)

        for key in tests:
            if isinstance(tests[key], dict):  # Allow for GetMitreReport's binary response
                if tests[key]["status_code"] not in AllowedResponses:
                    if key != "get_mitre_report":
                        error_checks = False
                    # print(key)
                    # print(tests[key]) 


            # print(f"{key} operation returned a {tests[key]} status code")

        return error_checks

    def test_all_code_paths(self):
        assert self.intel_test_all_code_paths() is True
