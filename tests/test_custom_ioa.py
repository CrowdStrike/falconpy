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
config = auth.getConfigObject()
falcon = FalconIOA(auth_object=config)
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
            "get_patterns": falcon.get_patterns(ids='12345678'),
            "get_platforms": falcon.get_platformsMixin0(ids='12345678'),
            "get_rule_groups": falcon.get_rule_groupsMixin0(ids='12345678'),
            "create_rule_group": falcon.create_rule_groupMixin0(body={}, cs_username='falconpy_unit_testing'),
            "delete_rule_group": falcon.delete_rule_groupMixin0(
                ids='12345678', cs_username='falconpy_unit_testing'
                ),
            "update_rule_group": falcon.update_rule_groupMixin0(body={}, cs_username='falconpy_unit_testing'),
            "get_rule_types": falcon.get_rule_types(ids='12345678'),
            "get_rules_get": falcon.get_rules_get(ids=['12345678', '23456789', '09876544']),
            "get_rules": falcon.get_rulesMixin0(ids='12345678'),
            "create_rule": falcon.create_rule(field_values={"something": "something-darkside"},
                                              cs_username='falconpy_unit_testing',
                                              rule_updates=[{"description": "New description"}]
                                              ),
            "create_rule_also": falcon.create_rule(field_values=[{"something": "something-darkside"}], rule_updates={"description": "New description"}),
            "delete_rules": falcon.delete_rules(ids='12345678', cs_username='falconpy_unit_testing'),
            "update_rules": falcon.update_rules(cs_username='falconpy_unit_testing',
                                                enabled=True,
                                                rulegroup_version=1,
                                                rule_updates={"something": "something-darkside"},
                                                disposition_id=1,
                                                ruletype_id="12345678"
                                                ),
            "update_rules_v2": falcon.update_rules_v2(enabled=True,
                                                      rulegroup_version=1,
                                                      rule_updates={"something": "something-darkside"},
                                                      disposition_id=1,
                                                      ruletype_id="12345678"
                                                      ),    
            "validate": falcon.validate(),
            "query_patterns": falcon.query_patterns(),
            "query_platforms": falcon.query_platformsMixin0(),
            "query_rule_groups_full": falcon.query_rule_groups_full(),
            "query_rule_groups": falcon.query_rule_groupsMixin0(),
            "query_rule_types": falcon.query_rule_types(),
            "query_rules": falcon.query_rulesMixin0()
        }
        for key in tests:
            if tests[key]["status_code"] != 500:
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
