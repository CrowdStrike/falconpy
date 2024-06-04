"""
test_filevantage.py -  This class tests the FileVantage service class
"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import FileVantage

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FileVantage(auth_object=config)
AllowedResponses = [200, 202, 400, 404, 429]  # Adding rate-limiting as an allowed response for now


class TestFileVantage:
    """
    FileVantage Service Class test harness
    """
    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_query_changes(self):
        """Pytest harness hook"""
        assert bool(falcon.query_changes(limit=1)["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_query_changes_scroll(self):
        """Pytest harness hook"""
        assert bool(falcon.query_changes_scroll(limit=1)["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_get_changes(self):
        """Pytest harness hook"""
        # Also testing lazy loading of the ids parameter
        assert bool(
            falcon.get_changes("12345678")["status_code"] in AllowedResponses
        ) is True

    def service_filevantage_remaining_tests(self):

        error_checks = True
        tests = {
            "update_policy_host_groups": falcon.update_policy_host_groups(policy_id="12345678", ids="1", action="unassign"),
            "update_policy_precedence": falcon.update_policy_precedence(ids="12345678", type="Windows"),
            "update_policy_rule_groups": falcon.update_policy_rule_groups(ids="12345678", policy_id="9876543"),
            "get_policies": falcon.get_policies(ids="12345678"),
            "create_policy": falcon.create_policy(name="whatevers", enabled=False),
            "delete_policies": falcon.delete_policies("12345678"),
            "update_policies": falcon.update_policies(id="12345678", description="whatevs", name="whatevs"),
            "get_scheduled_exclusions": falcon.get_scheduled_exclusions(ids="12345678", policy_id="12345678"),
            "create_scheduled_exclusions": falcon.create_scheduled_exclusions(name="whatevers"),
            "delete_scheduled_exclusions": falcon.delete_scheduled_exclusions(ids="12345678", policy_id="12345678"),
            "update_scheduled_exclusions": falcon.update_scheduled_exclusions(),
            "update_rule_group_precedence": falcon.update_rule_group_precedence(ids="1,2,3,4", rule_group_id="12345678"),
            "get_rules": falcon.get_rules(ids="12345678", rule_group_id="12345678"),
            "create_rule": falcon.create_rule(watch_attributes_directory_changes=True, description="whatevers"),
            "delete_rule": falcon.delete_rules(ids="12345678", rule_group_id="12345678"),
            "update_rule": falcon.update_rule(),
            "get_rule_groups": falcon.get_rule_groups("12345678"),
            "create_rule_group": falcon.create_rule_group(name="Whatevers"),
            "delete_rule_groups": falcon.delete_rule_groups("12345678"),
            "update_rule_group" : falcon.update_rule_group(),
            "query_policies": falcon.query_policies(),
            "query_scheduled_exclusions": falcon.query_scheduled_exclusions(),
            "query_rule_groups": falcon.query_rule_groups(type="WindowsFiles"),
            "getActionsMixin0": falcon.get_actions(ids="123456"),
            "startActions": falcon.start_actions(change_ids="123456", comment="whatever", operation="whatever"),
            "getContents": falcon.get_contents(id="123456", compress=True),
            "signalChangesExternal": falcon.signal_changes("123456"),
            "queryActionsMixin0": falcon.query_actions()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                # print(f"{key}: {tests[key]}")
                error_checks = False

        return error_checks

    @pytest.mark.skipif(falcon.base_url.lower() == "https://api.laggar.gcw.crowdstrike.com", reason="Unit test not supported in GovCloud")
    def test_remaining_functionality(self):
        assert self.service_filevantage_remaining_tests() is True

    @pytest.mark.skipif(falcon.base_url.lower() == "https://api.laggar.gcw.crowdstrike.com", reason="Unit test not supported in GovCloud")
    def test_override_style(self):
        assert bool(falcon.override(method="PATCH", route="/filevantage/entities/policies-host-groups/v1",body={}, parameters={"policy_id":"12345678","action": "unassign","ids":["12345678"]})["status_code"] in AllowedResponses)