"""
test_detects.py - This class tests the detects service class
"""
import json
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import detects as FalconDetections

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = FalconDetections.Detects(access_token=token)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestDetects:
    """
    Detects Service Class test harness
    """

    def serviceDetects_GetDetectSummaries(self):
        if falcon.GetDetectSummaries(
                body={"ids": falcon.QueryDetects(parameters={"limit": 1})["body"]["resources"]}
                )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    # def serviceDetects_GetAggregateDetects(self):
    #     print(falcon.QueryDetects(parameters={"limit":1}))
    #     print(falcon.GetAggregateDetects(body=[{"ranges":"ranges'{}'".format(falcon.QueryDetects(parameters={"limit":1})["body"]["resources"][0])}]))
    #     if falcon.GetAggregateDetects(body={"id":falcon.QueryDetects(parameters={"limit":1})["body"]["resources"][0]})["status_code"] in AllowedResponses:
    #         return True
    #     else:
    #         return False

    def serviceDetects_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        if falcon.QueryDetects()["status_code"] not in [400, 500]:
            errorChecks = False
        if falcon.GetDetectSummaries(body={"ids": {"oops": False}})["status_code"] not in [400, 500]:
            errorChecks = False
        if falcon.GetAggregateDetects(body={"resource": {"bad": True}})["status_code"] not in [400, 500]:
            errorChecks = False
        if falcon.UpdateDetectsByIdsV2(body={"bananas": "Are yellow or green"})["status_code"] not in [400, 500]:
            errorChecks = False
        if falcon.GetDetectSummaries(body={"something": "something"})["status_code"] not in [400, 500]:
            errorChecks = False
        if falcon.GetDetectSummaries(body={"something": "something", "ids": "12345678"})["status_code"] not in [400, 500]:
            errorChecks = False

        # else:
        #     print(f"Correct fail {falcon.GetDetectSummaries(body={'something': 'something'})['status_code']}")
        #     print(falcon.GetDetectSummaries(body={"something": "something"}))
        return errorChecks

    def test_QueryDetects(self):
        assert bool(falcon.QueryDetects(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(falcon.QueryDetects(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached")
    def test_GetDetectSummaries(self):
        assert self.serviceDetects_GetDetectSummaries() is True

    # def test_GetAggregateDetects(self):
    #     assert self.serviceDetects_GetAggregateDetects() == True

    # @staticmethod
    # def test_logout():
    #     """
    #     Pytest harness hook
    #     """
    #     assert bool(falcon.auth_object.revoke(
    #         falcon.auth_object.token()["body"]["access_token"]
    #         )["status_code"] in AllowedResponses) is True

    def test_Errors(self):
        assert self.serviceDetects_GenerateErrors() is True
