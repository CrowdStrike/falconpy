# test_zero_trust_assessment.py
# This class tests the zero_trust_assessment service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.zero_trust_assessment import Zero_Trust_Assessment as FalconZTA

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconZTA(access_token=auth.token)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestZeroTrustAssessment:
    def serviceZTA_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["getAssessmentV1", "ids='12345678'"]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_Logout(self):
        assert auth.serviceRevoke() is True

    def test_Errors(self):
        assert self.serviceZTA_GenerateErrors() is True
