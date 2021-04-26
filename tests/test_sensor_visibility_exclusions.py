# test_sensor_visibility_exclusions.py
# This class tests the sensor_visibility_exclusions service class
import os
import sys

# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.sensor_visibility_exclusions import Sensor_Visibility_Exclusions as FalconSVE

auth = Authorization.TestAuthorization()
auth.getConfig()
falcon = FalconSVE(creds={"client_id": auth.config["falcon_client_id"],
                          "client_secret": auth.config["falcon_client_secret"]
                          })
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestSVExclusions:
    def serviceSVE_ListExclusions(self):
        returned = False
        if falcon.querySensorVisibilityExclusionsV1(limit=1, offset=2, pizza="IsDelicious")["status_code"] in AllowedResponses:
            returned = True

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
