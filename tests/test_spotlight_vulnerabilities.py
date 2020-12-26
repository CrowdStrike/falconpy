# test_spotlight_vulnerabilities.py
# This class tests the spotlight_vulnerabilities service class

import json
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import spotlight_vulnerabilities as FalconSpotlight

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconSpotlight.Spotlight_Vulnerabilities(access_token=auth.token)
AllowedResponses = [200, 429] #Adding rate-limiting as an allowed response for now

class TestSpotlight:
    def serviceSpotlight_queryVulnerabilities(self):
        if falcon.queryVulnerabilities(parameters={"limit":1,"filter":"created_timestamp:>'2020-01-01T00:00:01Z'"})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSpotlight_getVulnerabilities(self):
        if falcon.getVulnerabilities(ids=falcon.queryVulnerabilities(parameters={"limit":1,"filter":"created_timestamp:>'2020-01-01T00:00:01Z'"})["body"]["resources"][0])["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def test_queryVulnerabilities(self):
        assert self.serviceSpotlight_queryVulnerabilities() == True

    def test_getVulnerabilities(self):
        assert self.serviceSpotlight_getVulnerabilities() == True

    def test_logout(self):
        assert auth.serviceRevoke() == True
