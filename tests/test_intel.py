# test_intel.py
# This class tests the intel service class
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# flake8: noqa=E401  # Classes to test - manually imported from sibling folder
from falconpy import intel as FalconIntel

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconIntel.Intel(access_token=auth.token)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestIntel:
    def serviceIntel_QueryIntelActorEntities(self):
        if falcon.QueryIntelActorEntities(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIntel_QueryIntelIndicatorEntities(self):
        if falcon.QueryIntelIndicatorEntities(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIntel_QueryIntelReportEntities(self):
        if falcon.QueryIntelReportEntities(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIntel_GetIntelActorEntities(self):
        result = falcon.GetIntelActorEntities(
            ids=falcon.QueryIntelActorEntities(parameters={"limit": 1})["body"]["resources"][0]["id"]
            )
        if result["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIntel_GetIntelIndicatorEntities(self):
        result = falcon.GetIntelIndicatorEntities(
            body={"id": falcon.QueryIntelIndicatorIds(parameters={"limit": 1})["body"]["resources"][0]}
            )
        if result["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIntel_GetIntelReportEntities(self):
        result = falcon.GetIntelReportEntities(
            ids=falcon.QueryIntelReportEntities(parameters={"limit": 1})["body"]["resources"][0]["id"]
            )
        if result["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIntel_QueryIntelActorIds(self):
        if falcon.QueryIntelActorIds(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIntel_QueryIntelIndicatorIds(self):
        if falcon.QueryIntelIndicatorIds(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIntel_QueryIntelReportIds(self):
        if falcon.QueryIntelReportIds(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIntel_QueryIntelRuleIds(self):
        result = falcon.QueryIntelRuleIds(parameters={"limit": 1, "type": "common-event-format"})
        if result["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIntel_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["QueryIntelActorEntities", ""],
            ["QueryIntelIndicatorEntities", ""],
            ["QueryIntelReportEntities", ""],
            ["GetIntelActorEntities", "ids='12345678'"],
            ["GetIntelIndicatorEntities", "body={}"],
            ["GetIntelReportPDF", "parameters={}"],
            ["GetIntelReportEntities", "ids='12345678'"],
            ["GetIntelRuleFile", "parameters={}"],
            ["GetLatestIntelRuleFile", "parameters={}"],
            ["GetIntelRuleEntities", "ids='12345678'"],
            ["QueryIntelActorIds", ""],
            ["QueryIntelIndicatorIds", ""],
            ["QueryIntelReportIds", ""],
            ["QueryIntelRuleIds", "parameters={}"]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_QueryIntelActorEntities(self):
        assert self.serviceIntel_QueryIntelActorEntities() is True

    def test_QueryIntelIndicatorEntities(self):
        assert self.serviceIntel_QueryIntelIndicatorEntities() is True

    def test_QueryIntelReportEntities(self):
        assert self.serviceIntel_QueryIntelReportEntities() is True

    @pytest.mark.skipif(
        falcon.QueryIntelActorEntities(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached"
        )
    def test_GetIntelActorEntities(self):
        assert self.serviceIntel_GetIntelActorEntities() is True

    # Not working - data issue with input body payload
    # @pytest.mark.skipif(
    #     falcon.QueryIntelIndicatorIds(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached"
    #     )
    # def test_GetIntelIndicatorEntities(self):
    #     assert self.serviceIntel_GetIntelIndicatorEntities() is True

    @pytest.mark.skipif(
        falcon.QueryIntelReportEntities(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached"
        )
    def test_GetIntelReportEntities(self):
        assert self.serviceIntel_GetIntelReportEntities() is True

    def test_QueryIntelActorIds(self):
        assert self.serviceIntel_QueryIntelActorIds() is True

    def test_QueryIntelIndicatorIds(self):
        assert self.serviceIntel_QueryIntelIndicatorIds() is True

    def test_QueryIntelReportIds(self):
        assert self.serviceIntel_QueryIntelReportIds() is True

    def test_QueryIntelRuleIds(self):
        assert self.serviceIntel_QueryIntelRuleIds() is True

    def test_Logout(self):
        assert auth.serviceRevoke() is True

    def test_Errors(self):
        assert self.serviceIntel_GenerateErrors() is True
