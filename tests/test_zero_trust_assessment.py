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
from falconpy import ZeroTrustAssessment

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ZeroTrustAssessment(auth_object=config)
AllowedResponses = [200, 201, 401, 403, 404, 429]  # Allowing 403 for unscopeable query_combined_assessments


class TestZeroTrustAssessment:
    # def zta_notfound(self):
    #     """
    #     Executes every statement in every method of the class, accepts all errors except 500
    #     """
    #     error_checks = True
    #     if falcon.getAssessmentV1(ids="12345678")["status_code"] not in AllowedResponses:
    #         error_checks = False

    #     return error_checks

    def test_get_assessment(self):
        """Pytest harness hook"""
        assert bool(falcon.getAssessmentV1(ids="12345678")["status_code"] in AllowedResponses) is True

    def test_get_complance(self):
        """Pytest harness hook"""
        assert bool(falcon.get_compliance()["status_code"] in AllowedResponses) is True

    def test_get_assessments_by_score(self):
        """Pytest harness hook"""
        assert bool(falcon.get_assessments_by_score(filter="score:>1")["status_code"] in AllowedResponses) is True

    def test_query_combined_assessment(self):
        """Pytest harness hook"""
        assert bool(falcon.query_combined_assessments()["status_code"] in AllowedResponses) is True

    # This should be the last test executed, log out the token
    @staticmethod
    def test_logout():
        """Pytest harness hook"""
        assert bool(auth.clear_env_token()) is True
