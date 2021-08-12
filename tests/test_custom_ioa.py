"""
test_custom_ioa.py - This class tests the custom_ioa service class
"""
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.custom_ioa import Custom_IOA as FalconIOA

auth = Authorization.TestAuthorization()
auth.getConfig()
falcon = FalconIOA(creds={"client_id": auth.config["falcon_client_id"],
                          "client_secret": auth.config["falcon_client_secret"]})
AllowedResponses = [200, 201, 207, 429]  # Adding rate-limiting as an allowed response for now


class TestCustomIOA:
    """Custom IOA Service Class test harness"""
    @staticmethod
    def ioa_generate_errors():
        """Generates errors for every operation and tests every code path"""
        falcon.base_url = "nowhere"
        error_checks = True
        # Intentionally crossing both code patterns for a while with this - jshcodes @ 08.10.21
        tests = {
            "get_patterns": falcon.get_patterns(ids='12345678')["status_code"],
            "get_platforms": falcon.get_platformsMixin0(ids='12345678')["status_code"],
            "get_rule_groups": falcon.get_rule_groupsMixin0(ids='12345678')["status_code"],
            "create_rule_group": falcon.create_rule_groupMixin0(body={}, cs_username='falconpy_unit_testing')["status_code"],
            "delete_rule_group": falcon.delete_rule_groupMixin0(
                ids='12345678', cs_username='falconpy_unit_testing'
                )["status_code"],
            "update_rule_group": falcon.update_rule_groupMixin0(body={}, cs_username='falconpy_unit_testing')["status_code"],
            "get_rule_types": falcon.get_rule_types(ids='12345678')["status_code"],
            "get_rules_get": falcon.get_rules_get(ids=['12345678', '23456789', '09876544'])["status_code"],
            "get_rules": falcon.get_rulesMixin0(ids='12345678')["status_code"],
            "create_rule": falcon.create_rule(body={}, cs_username='falconpy_unit_testing')["status_code"],
            "delete_rules": falcon.delete_rules(ids='12345678', cs_username='falconpy_unit_testing')["status_code"],
            "update_rules": falcon.update_rules(body={}, cs_username='falconpy_unit_testing')["status_code"],
            "validate": falcon.validate(body={})["status_code"],
            "query_patterns": falcon.query_patterns()["status_code"],
            "query_platforms": falcon.query_platformsMixin0()["status_code"],
            "query_rule_groups_full": falcon.query_rule_groups_full()["status_code"],
            "query_rule_groups": falcon.query_rule_groupsMixin0()["status_code"],
            "query_rule_types": falcon.query_rule_types()["status_code"],
            "query_rules": falcon.query_rulesMixin0()["status_code"]
        }
        for key in tests:
            if tests[key] != 500:
                error_checks = False

        return error_checks

    def test_query_patterns(self):
        """Pytest harness hook"""
        assert bool(falcon.query_patterns()["status_code"] in AllowedResponses) is True

    def test_query_platforms(self):
        """Pytest harness hook"""
        assert bool(falcon.query_platformsMixin0()["status_code"] in AllowedResponses) is True

    def test_query_rule_groups_full(self):
        """Pytest harness hook"""
        assert bool(falcon.query_rule_groups_full()["status_code"] in AllowedResponses) is True

    def test_query_rule_groups(self):
        """Pytest harness hook"""
        assert bool(falcon.query_rule_groupsMixin0()["status_code"] in AllowedResponses) is True

    def test_query_rule_types(self):
        """Pytest harness hook"""
        assert bool(falcon.query_rule_types()["status_code"] in AllowedResponses) is True

    def test_query_rules(self):
        """Pytest harness hook"""
        assert bool(falcon.query_rulesMixin0()["status_code"] in AllowedResponses) is True

    def test_errors(self):
        """Pytest harness hook"""
        assert self.ioa_generate_errors() is True

    @staticmethod
    def test_logout():
        """Pytest harness hook"""
        assert bool(falcon.auth_object.revoke(
            falcon.auth_object.token()["body"]["access_token"]
            )["status_code"] in AllowedResponses) is True
