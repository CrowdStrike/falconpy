"""
test_admission_control_policies.py - This class tests the AdmissionControlPolicies service class
"""
import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))

from falconpy import AdmissionControlPolicies

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = AdmissionControlPolicies(auth_object=config)
AllowedResponses = [200, 201, 400, 403, 404, 429]


class TestAdmissionControlPolicies:
    def run_all_tests(self):
        error_checks = True
        tests = {
            "GetPolicies": falcon.get_policies(ids="12345678"),
            "GetPoliciesMultiple": falcon.get_policies(ids=["12345678", "87654321"]),
            "CreatePolicy": falcon.create_policy(
                description="Test policy description",
                name="Test Policy"
            ),
            "UpdatePolicy": falcon.update_policy(
                ids="12345678",
                description="Updated description",
                is_enabled=True,
                name="Updated Policy"
            ),
            "DeletePolicies": falcon.delete_policies(ids="12345678"),
            "DeletePoliciesMultiple": falcon.delete_policies(ids=["12345678", "87654321"]),
            "AddHostGroups": falcon.add_host_groups(
                host_groups=["group1", "group2"],
                id="12345678"
            ),
            "AddHostGroupsSingle": falcon.add_host_groups(
                host_groups="group1",
                id="12345678"
            ),
            "RemoveHostGroups": falcon.remove_host_groups(
                policy_id="12345678",
                host_group_ids=["group1", "group2"]
            ),
            "RemoveHostGroupsSingle": falcon.remove_host_groups(
                policy_id="12345678",
                host_group_ids="group1"
            ),
            "UpdatePolicyPrecedence": falcon.update_policy_precedence(
                id="12345678",
                precedence=10
            ),
            "AddCustomRules": falcon.add_custom_rules(
                id="12345678",
                rule_groups=[
                    {
                        "id": "rulegroup1",
                        "custom_rules": [
                            {
                                "id": "customrule1",
                                "action": "DENY"
                            }
                        ]
                    }
                ]
            ),
            "DeleteCustomRules": falcon.delete_custom_rules(
                policy_id="12345678",
                custom_rule_ids=["customrule1", "customrule2"]
            ),
            "DeleteCustomRulesSingle": falcon.delete_custom_rules(
                policy_id="12345678",
                custom_rule_ids="customrule1"
            ),
            "SetRuleGroupPrecedence": falcon.set_rule_group_precedence(
                id="12345678",
                rule_groups=[
                    {"id": "rulegroup1"},
                    {"id": "rulegroup2"}
                ]
            ),
            "ReplaceRuleGroupSelectors": falcon.replace_rule_group_selectors(
                id="12345678",
                rule_groups=[
                    {
                        "id": "rulegroup1",
                        "labels": [
                            {
                                "key": "environment",
                                "operator": "In",
                                "value": "production"
                            }
                        ],
                        "namespaces": [
                            {"value": "default"}
                        ]
                    }
                ]
            ),
            "CreateRuleGroups": falcon.create_rule_groups(
                id="12345678",
                rule_groups=[
                    {
                        "description": "Test rule group",
                        "name": "Test Rule Group"
                    }
                ]
            ),
            "UpdateRuleGroups": falcon.update_rule_groups(
                id="12345678",
                rule_groups=[
                    {
                        "id": "rulegroup1",
                        "description": "Updated rule group",
                        "name": "Updated Rule Group",
                        "custom_rules": [
                            {
                                "id": "customrule1",
                                "action": "ALLOW"
                            }
                        ],
                        "default_rules": [
                            {
                                "code": "DR001",
                                "action": "DENY"
                            }
                        ],
                        "deny_on_error": {
                            "deny": True
                        },
                        "image_assessment": {
                            "enabled": True,
                            "unassessed_handling": "DENY"
                        }
                    }
                ]
            ),
            "DeleteRuleGroups": falcon.delete_rule_groups(
                policy_id="12345678",
                rule_group_ids=["rulegroup1", "rulegroup2"]
            ),
            "DeleteRuleGroupsSingle": falcon.delete_rule_groups(
                policy_id="12345678",
                rule_group_ids="rulegroup1"
            ),
            "QueryPolicies": falcon.query_policies(
                filter="name:'Test*'",
                limit=100,
                offset=0,
                sort="precedence"
            ),
            "QueryPoliciesMinimal": falcon.query_policies(),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False

        return error_checks

    def test_all_functionality(self):
        assert self.run_all_tests() is True
