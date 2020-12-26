# test_detects.py
# This class tests the detects service class

import json
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import detects as FalconDetections

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconDetections.Detects(access_token=auth.token)
AllowedResponses = [200, 429] #Adding rate-limiting as an allowed response for now

class TestDetects:

    def serviceDetects_QueryDetects(self):
        if falcon.QueryDetects(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    @pytest.mark.skipif(falcon.QueryDetects(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    def serviceDetects_GetDetectSummaries(self):
        if falcon.GetDetectSummaries(body={"ids":falcon.QueryDetects(parameters={"limit":1})["body"]["resources"]})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    # def serviceDetects_GetAggregateDetects(self):
    #     auth, falcon = self.authenticate()
    #     if falcon.GetAggregateDetects(body={"ids":falcon.QueryDetects(parameters={"limit":1})["body"]["resources"]})["status_code"] in AllowedResponses:
    #         auth.serviceRevoke()
    #         return True
    #     else:
    #         auth.serviceRevoke()
    #         return False

    def test_QueryDetects(self):
        assert self.serviceDetects_QueryDetects() == True

    def test_GetDetectSummaries(self):
        assert self.serviceDetects_GetDetectSummaries() == True

    # def test_GetAggregateDetects(self):
    #     assert self.serviceDetects_GetAggregateDetects() == True

    def test_logout(self):
        assert auth.serviceRevoke() == True