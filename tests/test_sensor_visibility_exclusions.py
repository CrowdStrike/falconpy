# test_sensor_visibility_exclusions.py
# This class tests the sensor_visibility_exclusions service class
import os
import sys
import pytest
# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.sensor_visibility_exclusions import Sensor_Visibility_Exclusions as FalconSVE

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = FalconSVE(access_token=token)
AllowedResponses = [200, 429]


class TestSVExclusions:
    def serviceSVE_ListExclusions(self):
        returned = False
        exclusions = falcon.querySensorVisibilityExclusionsV1(limit=1, offset=2, pizza="IsDelicious")
        if exclusions["status_code"] in AllowedResponses:
            returned = True
        elif exclusions["status_code"] == 500:
            pytest.skip("API communication failure")
        return returned

    def serviceSVE_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["getSensorVisibilityExclusionsV1", "ids='12345678'"],
            ["createSVExclusionsV1", "body={}"],
            ["updateSensorVisibilityExclusionsV1", "body={}"],
            ["deleteSensorVisibilityExclusionsV1", "ids='12345678'"]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_Find(self):
        assert self.serviceSVE_ListExclusions() is True

    def test_Errors(self):
        assert self.serviceSVE_GenerateErrors() is True
