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

class TestFirewallManagement:

    def serviceFirewall_query_rules(self):
        if falcon.query_rules(parameters={"limit":1})["status_code"] == 200:
            return True
        else:
            return False

    # def test_query_rules(self):
    #     assert self.serviceFirewall_query_rules() == True

    def test_logout(self):
        assert auth.serviceRevoke() == True

#TODO: My current API key can't hit this API. Pending additional unit testing for now.