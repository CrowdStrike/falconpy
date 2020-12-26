# test_incidents.py
# This class tests the incidents service class

import json
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import incidents as FalconIncidents

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconIncidents.Incidents(access_token=auth.token)
AllowedResponses = [200, 429] #Adding rate-limiting as an allowed response for now

class TestIncidents:

    def serviceIncidents_CrowdScore(self):
        if falcon.CrowdScore(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIncidents_QueryBehaviors(self):
        if falcon.QueryBehaviors(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIncidents_QueryIncidents(self):
        if falcon.QueryIncidents(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    @pytest.mark.skipif(falcon.QueryBehaviors(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    def serviceIncidents_GetBehaviors(self):
        if falcon.GetBehaviors(body={"ids":falcon.QueryBehaviors(parameters={"limit":1})["body"]["resources"]})["status_code"] in AllowedResponses:
            return True
        else:
            return False
    @pytest.mark.skipif(falcon.QueryIncidents(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    def serviceIncidents_GetIncidents(self):
        if falcon.GetIncidents(body={"ids":falcon.QueryIncidents(parameters={"limit":1})["body"]["resources"]})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def test_CrowdScore(self):
        assert self.serviceIncidents_CrowdScore() == True

    def test_QueryBehaviors(self):
        assert self.serviceIncidents_QueryBehaviors() == True

    def test_QueryIncidents(self):
        assert self.serviceIncidents_QueryIncidents() == True

    def test_GetIncidents(self):
        assert self.serviceIncidents_GetIncidents() == True

    def test_GetBehaviors(self):
        assert self.serviceIncidents_GetBehaviors() == True

    def test_logout(self):
        assert auth.serviceRevoke() == True