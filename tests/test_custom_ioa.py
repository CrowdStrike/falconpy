# test_custom_ioa.py
# This class tests the custom_ioa service class

# import json
import os
import sys
# import datetime
# import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import custom_ioa as FalconIOA

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconIOA.Custom_IOA(access_token=auth.token)
AllowedResponses = [200, 201, 207, 429]  # Adding rate-limiting as an allowed response for now


class TestCustomIOA:

    def serviceIOA_QueryPatterns(self):
        return falcon.query_patterns()["status_code"] in AllowedResponses

    def serviceIOA_QueryPlatformsMixin0(self):
        return falcon.query_platformsMixin0()["status_code"] in AllowedResponses

    def serviceIOA_QueryRuleGroupsFull(self):
        return falcon.query_rule_groups_full()["status_code"] in AllowedResponses

    def serviceIOA_QueryRuleGroupsMixin0(self):
        return falcon.query_rule_groupsMixin0()["status_code"] in AllowedResponses

    def serviceIOA_QueryRuleTypes(self):
        return falcon.query_rule_types()["status_code"] in AllowedResponses

    def serviceIOA_QueryRulesMixin0(self):
        return falcon.query_rulesMixin0()["status_code"] in AllowedResponses

    def serviceIOA_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["get_patterns", "ids='12345678'"],
            ["get_platformsMixin0", "ids='12345678'"],
            ["get_rule_groupsMixin0", "ids='12345678'"],
            ["create_rule_groupMixin0", "body={}, cs_username='unit_testing'"],
            ["delete_rule_groupMixin0", "ids='12345678', cs_username='unit_testing'"],
            ["update_rule_groupMixin0", "body={}, cs_username='unit_testing'"],
            ["get_rule_types", "ids='12345678'"],
            ["get_rules_get", "ids='12345678'"],
            ["get_rulesMixin0", "ids='12345678'"],
            ["create_rule", "body={}, cs_username='unit_testing'"],
            ["delete_rules", "ids='12345678', parameters={}, cs_username='unit_testing'"],
            ["update_rules", "body={}, cs_username='unit_testing'"],
            ["validate", "body={}"],
            ["query_patterns", ""],
            ["query_platformsMixin0", ""],
            ["query_rule_groups_full", ""],
            ["query_rule_groupsMixin0", ""],
            ["query_rule_types", ""],
            ["query_rulesMixin0", ""]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_QueryPatterns(self):
        assert self.serviceIOA_QueryPatterns() is True

    def test_QueryPlatformsMixin0(self):
        assert self.serviceIOA_QueryPlatformsMixin0() is True

    def test_QueryRuleGroupsFull(self):
        assert self.serviceIOA_QueryRuleGroupsFull() is True

    def test_QueryRuleGroupsMixin0(self):
        assert self.serviceIOA_QueryRuleGroupsMixin0() is True

    def test_QueryRuleTypes(self):
        assert self.serviceIOA_QueryRuleTypes() is True

    def test_QueryRulesMixin0(self):
        assert self.serviceIOA_QueryRulesMixin0() is True

    def test_Logout(self):
        assert auth.serviceRevoke() is True

    def test_Errors(self):
        assert self.serviceIOA_GenerateErrors() is True
