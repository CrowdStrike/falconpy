# test_sensor_update_policy.py
# This class tests the sensor_update_policy service class

import json
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import sensor_update_policy as FalconSensorUpdate

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconSensorUpdate.Sensor_Update_Policy(access_token=auth.token)
AllowedResponses = [200, 429] #Adding rate-limiting as an allowed response for now

class TestFalconSensorUpdate:
    def serviceSensorUpdate_querySensorUpdatePolicies(self):
        if falcon.querySensorUpdatePolicies(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_querySensorUpdatePolicyMembers(self):
        if falcon.querySensorUpdatePolicyMembers(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_getSensorUpdatePolicies(self):
        if falcon.getSensorUpdatePolicies(ids=falcon.querySensorUpdatePolicies(parameters={"limit":1})["body"]["resources"][0])["status_code"] in AllowedResponses:
            return True
        else:
            return False
    
    def serviceSensorUpdate_getSensorUpdatePoliciesV2(self):
        if falcon.getSensorUpdatePoliciesV2(ids=falcon.querySensorUpdatePolicies(parameters={"limit":1})["body"]["resources"][0])["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_queryCombinedSensorUpdatePolicies(self):
        if falcon.queryCombinedSensorUpdatePolicies(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_queryCombinedSensorUpdatePolicyMembers(self):
        if falcon.queryCombinedSensorUpdatePolicyMembers(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def test_querySensorUpdatePolicies(self):
        assert self.serviceSensorUpdate_querySensorUpdatePolicies() == True

    def test_querySensorUpdatePolicyMembers(self):
        assert self.serviceSensorUpdate_querySensorUpdatePolicyMembers() == True

    def test_queryCombinedSensorUpdatePolicies(self):
        assert self.serviceSensorUpdate_queryCombinedSensorUpdatePolicies() == True

    def test_queryCombinedSensorUpdatePolicyMembers(self):
        assert self.serviceSensorUpdate_queryCombinedSensorUpdatePolicyMembers() == True
    
    @pytest.mark.skipif(falcon.querySensorUpdatePolicies(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    def test_getSensorUpdatePolicies(self):
        assert self.serviceSensorUpdate_getSensorUpdatePolicies() == True
    
    @pytest.mark.skipif(falcon.querySensorUpdatePolicies(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    def test_getSensorUpdatePoliciesV2(self):
        assert self.serviceSensorUpdate_getSensorUpdatePoliciesV2() == True

    def test_logout(self):
        assert auth.serviceRevoke() == True