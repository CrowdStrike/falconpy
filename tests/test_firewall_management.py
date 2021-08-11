""" test_firewall_management.py - This class tests the firewall_management service class"""
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.firewall_management import Firewall_Management as FalconFirewall

auth = Authorization.TestAuthorization()
auth.getConfig()
falcon = FalconFirewall(creds={"client_id": auth.config["falcon_client_id"],
                               "client_secret": auth.config["falcon_client_secret"]
                               })
AllowedResponses = [200, 201, 400, 404, 429]


class TestFirewallManagement:
    """Test harness for the Firewall Management Service Class"""
    @staticmethod
    def firewall_test_all_code_paths():
        """Test every code path, accepts all errors except 500"""
        error_checks = True
        tests = {
            "aggregate_events": falcon.aggregate_events(body={})["status_code"],
            "aggregate_policy_rules": falcon.aggregate_policy_rules(body={})["status_code"],
            "aggregate_rule_groups": falcon.aggregate_rule_groups(body={})["status_code"],
            "aggregate_rules": falcon.aggregate_rules(body={})["status_code"],
            "get_events": falcon.get_events(ids="12345678")["status_code"],
            "get_firewall_fields": falcon.get_firewall_fields(ids="12345678")["status_code"],
            "get_platforms": falcon.get_platforms(ids="12345678")["status_code"],
            "get_policy_containers": falcon.get_policy_containers(ids="12345678")["status_code"],
            "update_policy_container": falcon.update_policy_container(body={}, cs_username="BillTheCat")["status_code"],
            "get_rule_groups": falcon.get_rule_groups(ids="12345678")["status_code"],
            "create_rule_group": falcon.create_rule_group(body={}, cs_username="HarryHenderson")["status_code"],
            "delete_rule_groups": falcon.delete_rule_groups(ids="12345678", cs_username="KyloRen")["status_code"],
            "update_rule_group": falcon.update_rule_group(body={}, cs_username="Calcifer")["status_code"],
            "get_rules": falcon.get_rules(ids="12345678")["status_code"],
            "query_events": falcon.query_events()["status_code"],
            "query_firewall_fields": falcon.query_firewall_fields()["status_code"],
            "query_platforms": falcon.query_platforms()["status_code"],
            "query_policy_rules": falcon.query_policy_rules()["status_code"],
            "query_rule_groups": falcon.query_rule_groups()["status_code"],
            "query_rules": falcon.query_rules()["status_code"]

        }
        for key in tests:
            if tests[key] not in AllowedResponses:
                error_checks = False
                # print(f"Failed on {key} with {tests[key]}")

        return error_checks

    @staticmethod
    def test_query_rules():
        """Pytest harness hook"""
        assert bool(falcon.query_rules(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    def test_all_paths(self):
        """Pytest harness hook"""
        assert self.firewall_test_all_code_paths() is True

    @staticmethod
    def test_logout():
        """Pytest harness hook"""
        assert bool(falcon.auth_object.revoke(
            falcon.auth_object.token()["body"]["access_token"]
            )["status_code"] in [200, 201]) is True
