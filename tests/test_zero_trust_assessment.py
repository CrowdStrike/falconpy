"""
test_zero_trust_assessment.py - This class tests the zero_trust_assessment service class
"""
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.zero_trust_assessment import Zero_Trust_Assessment as FalconZTA

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = FalconZTA(access_token=token)
AllowedResponses = [200, 201, 404, 429]


class TestZeroTrustAssessment:
    # def zta_notfound(self):
    #     """
    #     Executes every statement in every method of the class, accepts all errors except 500
    #     """
    #     error_checks = True
    #     if falcon.getAssessmentV1(ids="12345678")["status_code"] not in AllowedResponses:
    #         error_checks = False

    #     return error_checks

    def test_notfound(self):
        """Pytest harness hook"""
        assert bool(falcon.getAssessmentV1(ids="12345678")["status_code"] in AllowedResponses) is True

    # This should be the last test executed, log out the token
    @staticmethod
    def test_logout():
        """Pytest harness hook"""
        assert bool(auth.clear_env_token()) is True
