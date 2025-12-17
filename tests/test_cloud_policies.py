# test_cloud_policies.py
# This class tests the CloudPolicies service class

# import json
import os
import sys
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Classes to test - manually imported from sibling folder
from falconpy import CloudPolicies
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CloudPolicies(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 401, 404, 429, 500]


class TestCloudPolicies:
    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_code_paths(self):
        error_checks = True

        tests = {
            "ReplaceControlRules": falcon.ReplaceControlRules(body={}),
            "GetComplianceControls": falcon.GetComplianceControls(ids="1234567"),
            "CreateComplianceControl": falcon.CreateComplianceControl(body={}),
            "UpdateComplianceControl": falcon.UpdateComplianceControl(body={}),
            "DeleteComplianceControl": falcon.DeleteComplianceControl(ids="1234567"),
            "RenameSectionComplianceFramework": falcon.RenameSectionComplianceFramework(ids="1234567"),
            "GetComplianceFrameworks": falcon.GetComplianceFrameworks(ids="1234567"),
            "CreateComplianceFramework": falcon.CreateComplianceFramework(body={}),
            "UpdateComplianceFramework": falcon.UpdateComplianceFramework(body={}),
            "DeleteComplianceFramework": falcon.DeleteComplianceFramework(ids="1234567"),
            "GetEvaluationResult": falcon.GetEvaluationResult(body={}),
            "GetRuleOverride": falcon.GetRuleOverride(ids="1234567"),
            "CreateRuleOverride": falcon.CreateRuleOverride(body={}),
            "UpdateRuleOverride": falcon.UpdateRuleOverride(body={}),
            "DeleteRuleOverride": falcon.DeleteRuleOverride(ids="1234567"),
            "GetRule": falcon.GetRule(ids="1234567"),
            "CreateRuleMixin0": falcon.CreateRuleMixin0(body={}),
            "UpdateRule": falcon.UpdateRule(body={}),
            "DeleteRuleMixin0": falcon.DeleteRuleMixin0(ids="1234567"),
            "QueryComplianceControls": falcon.QueryComplianceControls(),
            "QueryComplianceFrameworks": falcon.QueryComplianceFrameworks(),
            "QueryRule": falcon.QueryRule(),
            "GetRuleInputSchema": falcon.GetRuleInputSchema(domain="whatever", subdomain="whatever", resource_type="whatever"),
            "GetEnrichedAsset": falcon.GetEnrichedAsset(ids="1234567")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
