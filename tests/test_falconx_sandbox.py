# test_falconx_sandbox.py
# This class tests the falconx_sandbox service class

import json
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import falconx_sandbox as FalconXSandbox

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconXSandbox.FalconX_Sandbox(access_token=auth.token)
AllowedResponses = [200, 429] #Adding rate-limiting as an allowed response for now

class TestFalconX:

    def serviceFalconX_QueryReports(self):
        if falcon.QueryReports(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False
    
    def serviceFalconX_QuerySubmissions(self):
        if falcon.QuerySubmissions(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False
            
    def serviceFalconX_GetSummaryReports(self):
        if falcon.GetSummaryReports(ids=falcon.QueryReports(parameters={"limit":1})["body"]["resources"])["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def test_QueryReports(self):
        assert self.serviceFalconX_QueryReports() == True
    
    def test_QuerySubmissions(self):
        assert self.serviceFalconX_QuerySubmissions() == True

    @pytest.mark.skipif(falcon.QueryReports(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    def test_GetSummaryReports(self):
        assert self.serviceFalconX_GetSummaryReports() == True

    def test_logout(self):
        assert auth.serviceRevoke() == True