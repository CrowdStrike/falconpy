"""
test_falconx_sandbox.py - This class tests the falconx_sandbox service class
"""
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
token = auth.getConfigExtended()
falcon = FalconXSandbox(access_token=token)
AllowedResponses = [200, 201, 400, 403, 404, 429]  # Adding rate-limiting as an allowed response for now


class TestFalconXSandbox:
    """
    Test Harness for the Falcon X Sandbox Service Class
    """
    def falconx_generate_errors(self):
        """
        Executes every statement in every method of the class, accepts all errors except 500
        """
        error_checks = True
        tests = {
            "get_artifacts": falcon.GetArtifacts(parameters={})["status_code"],
            "get_summary_reports": falcon.GetSummaryReports(ids='12345678')["status_code"],
            "get_reports": falcon.GetReports(ids='12345678')["status_code"],
            "delete_report": falcon.DeleteReport(ids='12345678')["status_code"],
            "get_submissions": falcon.GetSubmissions(ids='12345678')["status_code"],
            "submit": falcon.Submit(body={})["status_code"],
            "query_reports": falcon.QueryReports()["status_code"],
            "query_submissions": falcon.QuerySubmissions()["status_code"],
            "get_sample": falcon.GetSampleV2(ids='12345678')["status_code"],
            "upload_sample": falcon.UploadSampleV2(body={}, parameters={}, file_data='')["status_code"],
            "delete_sample": falcon.DeleteSampleV2(ids='12345678')["status_code"],
            "query_sample": falcon.QuerySampleV1({'sha256s': ['12345678']})["status_code"]
        }
        for key in tests:
            if tests[key] not in AllowedResponses:
                error_checks = False

            # print(f"{key} operation returned a {tests[key]} status code")

        return error_checks

    def test_query_reports(self):
        """Pytest harness hook"""
        assert bool(falcon.QueryReports(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    def test_query_submissions(self):
        """Pytest harness hook"""
        assert bool(falcon.QuerySubmissions(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(falcon.QueryReports(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached")
    def test_get_summary_reports(self):
        """Pytest harness hook"""
        assert bool(falcon.GetSummaryReports(
                        ids=falcon.QueryReports(
                            parameters={"limit": 1}
                        )["body"]["resources"]
                    )["status_code"] in AllowedResponses) is True

    def test_errors(self):
        """Pytest harness hook"""
        assert self.falconx_generate_errors() is True

    # @staticmethod
    # def test_logout():
    #     """Pytest harness hook"""
    #     assert bool(falcon.auth_object.revoke(
    #         falcon.auth_object.token()["body"]["access_token"]
    #         )["status_code"] in AllowedResponses) is True
