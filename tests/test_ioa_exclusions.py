# test_ioa_exclusions.py
# This class tests the ioa_exclusions service class
import os
import sys

# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.ioa_exclusions import IOA_Exclusions as FalconIOAE

auth = Authorization.TestAuthorization()
auth.getConfig()
falcon = FalconIOAE(creds={"client_id": auth.config["falcon_client_id"],
                           "client_secret": auth.config["falcon_client_secret"]
                           })
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestIOAExclusions:
    def serviceIOAE_ListExclusions(self):
        returned = False
        if falcon.queryIOAExclusionsV1(limit=1, offset=2, pizza="IsDelicious")["status_code"] in AllowedResponses:
            returned = True

        return returned

    def serviceIOAE_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["getIOAExclusionsV1", "ids='12345678'"],
            ["createIOAExclusionsV1", "body={}"],
            ["updateIOAExclusionsV1", "body={}"],
            ["deleteIOAExclusionsV1", "ids='12345678'"]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_Find(self):
        assert self.serviceIOAE_ListExclusions() is True

    def test_Errors(self):
        assert self.serviceIOAE_GenerateErrors() is True
