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
            "ReplaceControlRules": falcon.ReplaceControlRules(ids="1234567", rule_ids=["rule1", "rule2"]),
            "GetComplianceControls": falcon.GetComplianceControls(ids="1234567"),
            "CreateComplianceControl": falcon.CreateComplianceControl(description="test description", framework_id="framework123", name="test control", section_name="section1"),
            "UpdateComplianceControl": falcon.UpdateComplianceControl(ids="1234567", description="updated description", name="updated control"),
            "DeleteComplianceControl": falcon.DeleteComplianceControl(ids="1234567"),
            "RenameSectionComplianceFramework": falcon.RenameSectionComplianceFramework(ids="1234567", sectionName="old_section", section_name="new_section"),
            "GetComplianceFrameworks": falcon.GetComplianceFrameworks(ids="1234567"),
            "CreateComplianceFramework": falcon.CreateComplianceFramework(active=True, description="framework description", name="test framework"),
            "UpdateComplianceFramework": falcon.UpdateComplianceFramework(ids="1234567", active=False, description="updated framework", name="updated name"),
            "DeleteComplianceFramework": falcon.DeleteComplianceFramework(ids="1234567"),
            "GetEvaluationResult": falcon.GetEvaluationResult(cloud_provider="aws", resource_type="ec2", ids="1234567", input={"key": "value"}, logic="test logic"),
            "GetRuleOverride": falcon.GetRuleOverride(ids="1234567"),
            "CreateRuleOverride": falcon.CreateRuleOverride(overrides={"comment": "test",
                                                                        "crn": "crn123",
                                                                        "expires_at": "2025-12-31T00:00:00Z",
                                                                        "override_type":"exception",
                                                                        "rule_id": "rule123",
                                                                        "reason": "testing"
                                                                        }),
            "UpdateRuleOverride": falcon.UpdateRuleOverride(overrides={"comment": "updated",
                                                                        "crn": "crn456",
                                                                        "expires_at": "2026-12-31T00:00:00Z",
                                                                        "override_type": "exception",
                                                                        "rule_id": "rule456",
                                                                        "reason": "update test"
                                                                        }),
            "DeleteRuleOverride": falcon.DeleteRuleOverride(ids="1234567"),
            "GetRule": falcon.GetRule(ids="1234567"),
            "CreateRuleMixin0": falcon.CreateRuleMixin0(alert_info="alert",
                                                        attack_types="attack",
                                                        controls=[{"Authority": "auth", "Code": "code"}],
                                                        description="rule description",
                                                        domain="domain1",
                                                        logic="rule logic",
                                                        name="test rule",
                                                        platform="aws",
                                                        provider="aws",
                                                        remediation_info="fix it",
                                                        remediation_url="http://example.com",
                                                        resource_type="ec2",
                                                        severity=3,
                                                        subdomain="subdomain1"
                                                        ),
            "CreateRuleMixin02": falcon.CreateRuleMixin0(alert_info="alert",
                                                         attack_types="attack",
                                                         Authority="auth",
                                                         Code="code",
                                                         description="rule description",
                                                         domain="domain1",
                                                         logic="rule logic",
                                                         name="test rule",
                                                         platform="aws",
                                                         provider="aws",
                                                         remediation_info="fix it",
                                                         remediation_url="http://example.com",
                                                         resource_type="ec2",
                                                         severity=3,
                                                         subdomain="subdomain1"
                                                         ),
            "UpdateRule": falcon.UpdateRule(alert_info="updated alert",
                                            attack_types=["attack1", "attack2"],
                                            category="category1",
                                            controls=[{"authority": "auth", "code": "code"}],
                                            description="updated rule",
                                            name="updated rule name",
                                            rule_logic_list={"logic": "logic",
                                                              "platform": "aws",
                                                              "remediation_info": "info",
                                                              "remediation_url": "http://example.com"
                                                              }, 
                                            severity=4,
                                            uuid="uuid123"
                                            ),
            "UpdateRule2": falcon.UpdateRule(alert_info="updated alert",
                                            attack_types=["attack1", "attack2"],
                                            category="category1",
                                            authority="auth",
                                            code="code",
                                            description="updated rule",
                                            name="updated rule name",
                                            rule_logic_list={"logic": "logic",
                                                              "platform": "aws",
                                                              "remediation_info": "info",
                                                              "remediation_url": "http://example.com"
                                                              }, 
                                            severity=4,
                                            uuid="uuid123"
                                            ),
            "DeleteRuleMixin0": falcon.DeleteRuleMixin0(ids="1234567"),
            "QueryComplianceControls": falcon.QueryComplianceControls(filter="whatever", limit=100, offset=0, sort="compliance_control_name|asc"),
            "QueryComplianceFrameworks": falcon.QueryComplianceFrameworks(filter="whatever", limit=100, offset=0, sort="compliance_framework_name|asc"),
            "QueryRule": falcon.QueryRule(filter="whatever", limit=100, offset=0, sort="rule_name|asc"),
            "GetRuleInputSchema": falcon.GetRuleInputSchema(domain="whatever", subdomain="whatever", resource_type="whatever"),
            "GetEnrichedAsset": falcon.GetEnrichedAsset(ids="1234567")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
