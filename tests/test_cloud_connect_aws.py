# test_cloud_connect_aws.py
# This class tests the cloud_connect_aws service class

import json
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import cloud_connect_aws as FalconAWS

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconAWS.Cloud_Connect_AWS(access_token=auth.token)

class TestCloudConnectAWS:
    def serviceCCAWS_GetAWSSettings(self):
        if falcon.GetAWSSettings()["status_code"] == 200:
            return True
        else:
            return False      

    def serviceCCAWS_QueryAWSAccounts(self):
        if falcon.QueryAWSAccounts()["status_code"] == 200:
            return True
        else:
            return False

    def serviceCCAWS_GetAWSAccounts(self):
        if falcon.GetAWSAccounts(ids=falcon.QueryAWSAccounts(parameters={"limit":1})["body"]["resources"][0]["id"])["status_code"] == 200:
            return True
        else:
            return False
        
    def serviceCCAWS_VerifyAWSAccountAccess(self):
        if falcon.VerifyAWSAccountAccess(ids=falcon.QueryAWSAccounts(parameters={"limit":1})["body"]["resources"][0]["id"])["status_code"] == 200:
            return True
        else:
            return False

    def serviceCCAWS_QueryAWSAccountsForIDs(self):
        if falcon.QueryAWSAccountsForIDs(parameters={"limit":1})["status_code"] == 200:
            return True
        else:
            return False

    def test_GetAWSSettings(self):
        assert self.serviceCCAWS_GetAWSSettings() == True

    def test_QueryAWSAccounts(self):
        assert self.serviceCCAWS_QueryAWSAccounts() == True

    def test_GetAWSAccounts(self):
        assert self.serviceCCAWS_GetAWSAccounts() == True

    def test_VerifyAWSAccountAccess(self):
        assert self.serviceCCAWS_VerifyAWSAccountAccess() == True
        
    def test_QueryAWSAccountsForIDs(self):
        assert self.serviceCCAWS_QueryAWSAccountsForIDs() == True

    def test_logout(self):
        assert auth.serviceRevoke() == True