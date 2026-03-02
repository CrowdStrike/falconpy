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
from falconpy import FalconXSandbox

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FalconXSandbox(auth_object=config)
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
        filename = "tests/testfile.png"
        # FILENAME = f"tests/{filename}"
        # fmt = '%Y-%m-%d %H:%M:%S'
        with open(filename, 'rb') as testfile:
            PAYLOAD = testfile.read()
        #filename = None
        #PAYLOAD = None
        tests = {
            "get_artifacts": falcon.GetArtifacts(parameters={}),
            "get_summary_reports": falcon.GetSummaryReports(ids='12345678'),
            "get_reports": falcon.GetReports(ids='12345678'),
            "delete_report": falcon.DeleteReport(ids='12345678'),
            "get_submissions": falcon.GetSubmissions(ids='12345678'),
            "submit": falcon.Submit(document_password="banana",
                                    enable_tor=False,
                                    environment_id=300,
                                    send_email_notifications=False,
                                    user_tags="apples,bananas"
                                    ),
            "query_reports": falcon.QueryReports(),
            "query_submissions": falcon.QuerySubmissions(),
            "get_sample": falcon.GetSampleV2(ids='12345678'),
            "upload_sample": falcon.UploadSampleV2(file_name=filename, upfile=PAYLOAD, comment="testing", is_confidential=True),
            "upload_sample": falcon.UploadSampleV2(file_data=PAYLOAD),
            "upload_sample": falcon.UploadSampleV2(file_data=None, file_name="whatever.png"),
            "delete_sample": falcon.DeleteSampleV2(ids='12345678'),
            "query_sample": falcon.QuerySampleV1(sha256s='12345678'),
            "get_memory_dump": falcon.get_memory_dump("12345678"),
            "get_hex_dump": falcon.get_hex_dump("12345678"),
            "get_extracted_strings": falcon.get_dump_extracted_strings("12345678")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                # Temp allow 500s from the memory dump operations
                if key not in ["get_memory_dump", "get_hex_dump", "get_extracted_strings"]:
                    error_checks = False

                    # print(f"{key} operation returned {tests[key]}")

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
        id_lookup = falcon.query_reports(limit=1)
        id_list = "1234567890"
        if id_lookup["status_code"] not in [403, 404, 429]:
            if id_lookup["body"]["resources"]:
                id_list = id_lookup["body"]["resources"]

        assert bool(falcon.GetSummaryReports(
                        ids=id_list
                    )["status_code"] in AllowedResponses) is True

    def test_errors(self):
        """Pytest harness hook"""
        assert self.falconx_generate_errors() is True
