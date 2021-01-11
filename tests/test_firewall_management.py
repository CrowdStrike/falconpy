# test_firewall_management.py
# This class tests the firewall_management service class

import json
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import firewall_management as FalconFirewall

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconFirewall.Firewall_Management(access_token=auth.token)
AllowedResponses = [200, 429] #Adding rate-limiting as an allowed response for now

class TestFirewallManagement:

    def serviceFirewall_query_rules(self):
        if falcon.query_rules(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False


    def serviceFirewall_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        if falcon.aggregate_events(body={})["status_code"] != 500:
            errorChecks = False
        if falcon.aggregate_policy_rules(body={})["status_code"] != 500:
            errorChecks = False
        if falcon.aggregate_rule_groups(body={})["status_code"] != 500:
            errorChecks = False
        if falcon.aggregate_rules(body={})["status_code"] != 500:
            errorChecks = False
        if falcon.get_events(ids="12345678")["status_code"] != 500:
            errorChecks = False
        if falcon.get_firewall_fields(ids="12345678")["status_code"] != 500:
            errorChecks = False
        if falcon.get_platforms(ids="12345678")["status_code"] != 500:
            errorChecks = False
        if falcon.get_policy_containers(ids="12345678")["status_code"] != 500:
            errorChecks = False
        if falcon.update_policy_container(body={}, cs_username="BillTheCat")["status_code"] != 500:
            errorChecks = False
        if falcon.get_rule_groups(ids="12345678")["status_code"] != 500:
            errorChecks = False
        if falcon.create_rule_group(body={}, cs_username="HarryHenderson")["status_code"] != 500:
            errorChecks = False
        if falcon.delete_rule_groups(ids="12345678", cs_username="KyloRen")["status_code"] != 500:
            errorChecks = False
        if falcon.update_rule_group(body={}, cs_username="Calcifer")["status_code"] != 500:
            errorChecks = False
        if falcon.get_rules(ids="12345678")["status_code"] != 500:
            errorChecks = False
        if falcon.query_events()["status_code"] != 500:
            errorChecks = False
        if falcon.query_firewall_fields()["status_code"] != 500:
            errorChecks = False
        if falcon.query_platforms()["status_code"] != 500:
            errorChecks = False
        if falcon.query_policy_rules()["status_code"] != 500:
            errorChecks = False
        if falcon.query_rule_groups()["status_code"] != 500:
            errorChecks = False
        if falcon.query_rules()["status_code"] != 500:
            errorChecks = False
            
        return errorChecks

    # def test_query_rules(self):
    #     assert self.serviceFirewall_query_rules() == True

    def test_Logout(self):
        assert auth.serviceRevoke() == True

    def test_Errors(self):
        assert self.serviceFirewall_GenerateErrors() == True

#TODO: My current API key can't hit this API. Pending additional unit testing for now.