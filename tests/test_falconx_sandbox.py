# test_falconx_sandbox.py
# This class tests the falconx_sandbox service class

import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.falconx_sandbox import FalconXSandbox

auth = Authorization.TestAuthorization()
auth.getConfig()
falcon = FalconXSandbox(creds={"client_id": auth.config["falcon_client_id"],
                               "client_secret": auth.config["falcon_client_secret"]})
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestFalconX:

    def serviceFalconX_QueryReports(self):
        if falcon.QueryReports(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceFalconX_QuerySubmissions(self):
        if falcon.QuerySubmissions(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceFalconX_GetSummaryReports(self):
        if falcon.GetSummaryReports(
                    ids=falcon.QueryReports(
                        parameters={"limit": 1}
                    )["body"]["resources"]
                )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceFalconX_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["GetArtifacts", "parameters={}"],
            ["GetSummaryReports", "ids='12345678'"],
            ["GetReports", "ids='12345678'"],
            ["DeleteReport", "ids='12345678'"],
            ["GetSubmissions", "ids='12345678'"],
            ["Submit", "body={}"],
            ["QueryReports", ""],
            ["QuerySubmissions", ""],
            ["GetSampleV2", "ids='12345678'"],
            ["UploadSampleV2", "body={}, parameters={}, file_data=''"],
            ["DeleteSampleV2", "ids='12345678'"],
            ["QuerySampleV1", "{'sha256s': ['12345678']}"]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def falconx_logout(self):
        if falcon.auth_object.revoke(falcon.auth_object.token()["body"]["access_token"])["status_code"] == 200:
            return True
        else:
            return False

    def test_QueryReports(self):
        assert self.serviceFalconX_QueryReports() is True

    def test_QuerySubmissions(self):
        assert self.serviceFalconX_QuerySubmissions() is True

    @pytest.mark.skipif(falcon.QueryReports(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached")
    def test_GetSummaryReports(self):
        assert self.serviceFalconX_GetSummaryReports() is True

    def test_Logout(self):
        assert self.falconx_logout() is True

    def test_Errors(self):
        assert self.serviceFalconX_GenerateErrors() is True
