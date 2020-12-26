# test_iocs.py
# This class tests the iocs service class

import json
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import iocs as FalconIOCs

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconIOCs.Iocs(access_token=auth.token)
AllowedResponses = [200, 429] #Adding rate-limiting as an allowed response for now

class TestIOCs:
    def serviceIOCs_QueryIOCs(self):
        if falcon.QueryIOCs()["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIOCs_GetIOC(self):
        
        if falcon.GetIOC(parameters={"type":"ipv4", "value":falcon.QueryIOCs(parameters={"types":"ipv4"})["body"]["resources"][0]})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def test_QueryIOCs(self):
        assert self.serviceIOCs_QueryIOCs() == True

    # Current test environment doesn't have any custom IOCs configured atm
    # def test_GetIOC(self):
    #     assert self.serviceIOCs_GetIOC() == True


    def test_logout(self):
        assert auth.serviceRevoke() == True