# test_sensor_update_policy.py
# This class tests the sensor_update_policy service class

import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Classes to test - manually imported from sibling folder
from falconpy import sensor_update_policy as FalconSensorUpdate
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))


auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconSensorUpdate.Sensor_Update_Policy(access_token=auth.token)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestFalconSensorUpdate:
    def serviceSensorUpdate_querySensorUpdatePolicies(self):
        if falcon.querySensorUpdatePolicies(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_querySensorUpdatePolicyMembers(self):
        if falcon.querySensorUpdatePolicyMembers(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_getSensorUpdatePolicies(self):
        try:
            id_list = falcon.querySensorUpdatePolicies(parameters={"limit": 1})["body"]["resources"][0]
            if falcon.getSensorUpdatePolicies(ids=id_list)["status_code"] in AllowedResponses:
                return True
            else:
                return False
        except KeyError:
            # Flaky
            pytest.skip("Workflow-related error, skipping")
            return True

    def serviceSensorUpdate_getSensorUpdatePoliciesV2(self):
        try:
            id_list = falcon.querySensorUpdatePolicies(parameters={"limit": 1})["body"]["resources"][0]
            if falcon.getSensorUpdatePoliciesV2(ids=id_list)["status_code"] in AllowedResponses:
                return True
            else:
                return False
        except KeyError:
            # Flaky
            pytest.skip("Workflow-related error, skipping")
            return True

    def serviceSensorUpdate_queryCombinedSensorUpdatePolicies(self):
        if falcon.queryCombinedSensorUpdatePolicies(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_queryCombinedSensorUpdatePolicyMembers(self):
        if falcon.queryCombinedSensorUpdatePolicyMembers(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["querySensorUpdatePolicies", ""],
            ["querySensorUpdatePolicyMembers", ""],
            ["getSensorUpdatePolicies", "ids='12345678'"],
            ["getSensorUpdatePoliciesV2", "ids='12345678'"],
            ["queryCombinedSensorUpdatePolicies", ""],
            ["queryCombinedSensorUpdatePolicyMembers", ""],
            ["revealUninstallToken", "body={}"],
            ["queryCombinedSensorUpdateBuilds", ""],
            ["createSensorUpdatePolicies", "body={}"],
            ["createSensorUpdatePoliciesV2", "body={}"],
            ["deleteSensorUpdatePolicies", "ids=['12345678','98765432','01234567']"],
            ["updateSensorUpdatePolicies", "body={}"],
            ["updateSensorUpdatePoliciesV2", "body={}"],
            ["performSensorUpdatePoliciesAction", "body={}, action_name='enable'"],
            ["performSensorUpdatePoliciesAction", "body={}"],
            ["setSensorUpdatePoliciesPrecedence", "body={}"],
            ["queryCombinedSensorUpdatePoliciesV2", ""]
        ]

        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_querySensorUpdatePolicies(self):
        assert self.serviceSensorUpdate_querySensorUpdatePolicies() is True

    def test_querySensorUpdatePolicyMembers(self):
        assert self.serviceSensorUpdate_querySensorUpdatePolicyMembers() is True

    def test_queryCombinedSensorUpdatePolicies(self):
        assert self.serviceSensorUpdate_queryCombinedSensorUpdatePolicies() is True

    def test_queryCombinedSensorUpdatePolicyMembers(self):
        assert self.serviceSensorUpdate_queryCombinedSensorUpdatePolicyMembers() is True

    @pytest.mark.skipif(falcon.querySensorUpdatePolicies(parameters={"limit": 1})["status_code"] == 429,
                        reason="API rate limit reached")
    def test_getSensorUpdatePolicies(self):
        assert self.serviceSensorUpdate_getSensorUpdatePolicies() is True

    @pytest.mark.skipif(falcon.querySensorUpdatePolicies(parameters={"limit": 1})["status_code"] == 429,
                        reason="API rate limit reached")
    def test_getSensorUpdatePoliciesV2(self):
        assert self.serviceSensorUpdate_getSensorUpdatePoliciesV2() is True

    def test_Logout(self):
        assert auth.serviceRevoke() is True

    def test_Errors(self):
        assert self.serviceSensorUpdate_GenerateErrors() is True
