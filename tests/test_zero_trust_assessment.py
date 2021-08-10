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
auth.getConfig()
falcon = FalconZTA(creds={"client_id": auth.config["falcon_client_id"],
                          "client_secret": auth.config["falcon_client_secret"]})
AllowedResponses = [200, 201, 429]


class TestZeroTrustAssessment:
    def zta_notfound(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        if falcon.getAssessmentV1(ids="12345678")["status_code"] != 500:
            errorChecks = False

        return errorChecks

    def zta_logout(self):
        if falcon.auth_object.revoke(falcon.auth_object.token()["body"]["access_token"])["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def test_logout(self):
        assert self.zta_logout() is True

    def test_notfound(self):
        assert self.zta_notfound() is True
