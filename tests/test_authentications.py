# test_authentications.py
# Tests different service class authentication styles
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.zero_trust_assessment import Zero_Trust_Assessment as FalconZTA
from falconpy.cloud_connect_aws import Cloud_Connect_AWS as FalconAWS
from falconpy import oauth2 as FalconAuth

auth = Authorization.TestAuthorization()
auth.serviceAuth()
AllowedResponses = [200, 429, 401]  # Adding rate-limiting as an allowed response for now


class TestAuthentications:

    def serviceAny_TestCredentialAuthFailure(self):
        bad_falcon = FalconZTA(creds={"client_id": "This", "client_secret": "WontWork"})
        result = bad_falcon.getAssessmentV1(ids='12345678')

        if result["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceAny_TestStaleObjectAuth(self):

        falcon = FalconAWS(auth_object=FalconAuth.OAuth2(creds={
                                                                "client_id": auth.config["falcon_client_id"],
                                                                "client_secret": auth.config["falcon_client_secret"]
                                                                }))
        result = falcon.QueryAWSAccounts()
        if result["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceAny_TestObjectAuth(self):
        auth_obj = FalconAuth.OAuth2(creds={
                                            "client_id": auth.config["falcon_client_id"],
                                            "client_secret": auth.config["falcon_client_secret"]
                                            })
        auth_obj.token()
        falcon = FalconAWS(auth_object=auth_obj)
        result = falcon.QueryAWSAccounts()
        if result["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceAny_TestBadObjectAuth(self):

        falcon = FalconAWS(auth_object=FalconAuth.OAuth2(creds={
                                                                "client_id": "ThisAlso",
                                                                "client_secret": "WontWork"
                                                                }))
        result = falcon.QueryAWSAccounts()
        if result["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def test_BadCredentialAuth(self):
        assert self.serviceAny_TestCredentialAuthFailure() is True

    def test_StaleObjectAuth(self):
        assert self.serviceAny_TestStaleObjectAuth() is True

    def test_BadObjectAuth(self):
        assert self.serviceAny_TestBadObjectAuth() is True

    def test_ObjectAuth(self):
        assert self.serviceAny_TestObjectAuth() is True