# test_ml_exclusions.py
# This class tests the ml_exclusions service class
import os
import sys

# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.ml_exclusions import ML_Exclusions as FalconMLE

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = FalconMLE(access_token=token)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestMLExclusions:
    def serviceMLE_ListExclusions(self):
        returned = False
        result = falcon.queryMLExclusionsV1(limit=1, offset=2, pizza="IsDelicious")
        if result["status_code"] in AllowedResponses:
            returned = True

        return returned

    def serviceMLE_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["getMLExclusionsV1", "ids='12345678'"],
            ["createMLExclusionsV1", "body={}"],
            ["updateMLExclusionsV1", "body={}"],
            ["deleteMLExclusionsV1", "ids='12345678'"]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_Find(self):
        assert self.serviceMLE_ListExclusions() is True

    def test_Errors(self):
        assert self.serviceMLE_GenerateErrors() is True
