# test_firewall_policies.py
# This class tests the firewall_policies service class

import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import firewall_policies as FalconFirewallPolicy

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconFirewallPolicy.Firewall_Policies(access_token=auth.token)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestFirewallPolicy:

    def serviceFirewall_queryFirewallPolicies(self):
        if falcon.queryFirewallPolicies(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    # def test_queryFirewallPolicies(self):
    #     assert self.serviceFirewall_queryFirewallPolicies() == True

    def serviceFirewall_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["queryCombinedFirewallPolicyMembers", ""],
            ["queryCombinedFirewallPolicies", ""],
            ["performFirewallPoliciesAction", "action_name='enable', body={}, parameters={}"],
            ["performFirewallPoliciesAction", "action_name='make-it-go-boom', body={}, parameters={}"],
            ["setFirewallPoliciesPrecedence", "body={}"],
            ["getFirewallPolicies", "ids='12345678'"],
            ["createFirewallPolicies", "body={}"],
            ["deleteFirewallPolicies", "ids='12345678'"],
            ["updateFirewallPolicies", "body={}"],
            ["queryFirewallPolicyMembers", ""],
            ["queryFirewallPolicies", ""]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_Logout(self):
        assert auth.serviceRevoke() == True

    def test_Errors(self):
        assert self.serviceFirewall_GenerateErrors() == True
