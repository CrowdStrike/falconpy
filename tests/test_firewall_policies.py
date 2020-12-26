# test_firewall_policies.py
# This class tests the firewall_policies service class

import json
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import firewall_policies as FalconFirewallPolicy

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconFirewallPolicy.Firewall_Policies(access_token=auth.token)
AllowedResponses = [200, 429] #Adding rate-limiting as an allowed response for now

class TestFirewallPolicy:

    def serviceFirewall_queryFirewallPolicies(self):
        if falcon.queryFirewallPolicies(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    # def test_queryFirewallPolicies(self):
    #     assert self.serviceFirewall_queryFirewallPolicies() == True

    def test_logout(self):
        assert auth.serviceRevoke() == True
#TODO: My current API key can't hit this API. Pending additional unit testing for now.