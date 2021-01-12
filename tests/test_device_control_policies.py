# test_device_control_poligies.py
# This class tests the device_control_policies service class

import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import device_control_policies as FalconDeviceControlPolicy

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconDeviceControlPolicy.Device_Control_Policies(access_token=auth.token)
AllowedResponses = [200, 429] #Adding rate-limiting as an allowed response for now

class TestDeviceControlPolicy:

    def serviceDeviceControlPolicies_queryDeviceControlPolicies(self):
        if falcon.queryDeviceControlPolicies(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceDeviceControlPolicies_queryDeviceControlPolicyMembers(self):
        if falcon.queryDeviceControlPolicyMembers(parameters={"id": falcon.queryDeviceControlPolicies(parameters={"limit":1})["body"]["resources"][0]})["status_code"] in AllowedResponses:
            return True
        else:
            return False


    def serviceDeviceControlPolicies_getDeviceControlPolicies(self):
        if falcon.getDeviceControlPolicies(ids=falcon.queryDeviceControlPolicies(parameters={"limit":1})["body"]["resources"][0])["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceDeviceControlPolicies_queryCombinedDeviceControlPolicies(self):
        if falcon.queryCombinedDeviceControlPolicies(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceDeviceControlPolicies_queryCombinedDeviceControlPolicyMembers(self):
        if falcon.queryCombinedDeviceControlPolicyMembers(parameters={"id": falcon.queryCombinedDeviceControlPolicies(parameters={"limit":1})["body"]["resources"][0]["id"]})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceDeviceControlPolicies_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["queryCombinedDeviceControlPolicyMembers",""],
            ["queryCombinedDeviceControlPolicies",""],
            ["performDeviceControlPoliciesAction","body={}, parameters={}"],
            ["setDeviceControlPoliciesPrecedence", "body={}"],
            ["getDeviceControlPolicies","ids='12345678'"],
            ["createDeviceControlPolicies","body={}"],
            ["deleteDeviceControlPolicies","ids='12345678'"],
            ["updateDeviceControlPolicies","body={}"],
            ["queryDeviceControlPolicyMembers",""],
            ["queryDeviceControlPolicies",""]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0],cmd[1])) != 500:
                errorChecks = False
        
        return errorChecks

    def test_queryDeviceControlPolicies(self):
        assert self.serviceDeviceControlPolicies_queryDeviceControlPolicies() == True
    
    @pytest.mark.skipif(falcon.queryDeviceControlPolicies(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    def test_queryDeviceControlPolicyMembers(self):
        assert self.serviceDeviceControlPolicies_queryDeviceControlPolicyMembers() == True
    
    @pytest.mark.skipif(falcon.queryDeviceControlPolicies(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")    
    def test_getDeviceControlPolicies(self):
        assert self.serviceDeviceControlPolicies_getDeviceControlPolicies() == True

    def test_queryCombinedDeviceControlPolicies(self):
        assert self.serviceDeviceControlPolicies_queryCombinedDeviceControlPolicies() == True
    
    @pytest.mark.skipif(falcon.queryCombinedDeviceControlPolicies(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    def test_queryCombinedDeviceControlPolicyMembers(self):
        assert self.serviceDeviceControlPolicies_queryCombinedDeviceControlPolicyMembers() == True

    def test_Logout(self):
        assert auth.serviceRevoke() == True
    
    def test_Errors(self):
        assert self.serviceDeviceControlPolicies_GenerateErrors() == True
