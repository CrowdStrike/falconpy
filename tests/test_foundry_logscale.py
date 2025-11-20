"""
test_foundry_logscale.py - This class tests the FoundryLogScale service class
"""
import os
import sys
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import FoundryLogScale

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FoundryLogScale(auth_object=config)
AllowedResponses = [200, 201, 400, 401, 403, 404, 429, 406, 500, 501, 502, 503]


class TestFoundryLogScale:
    def run_all_tests(self):
        error_checks = True
        tests = {
            "ListReposV1" : falcon.list_repos(),
            "ListViewV1" : falcon.list_views(),
            "IngestDataV1" : falcon.ingest_data(data_file="testfile.png", tag="file_tag"),
            "IngestDataV1also" : falcon.ingest_data(file="testfile.png", tag="file_tag"),
            "CreateSavedSearchesDynamicExecuteV1" : falcon.execute_dynamic(end="10", start="1"),
            "GetSavedSearchesExecuteV1" : falcon.get_search_results(job_id="12345"),
            "CreateSavedSearchesExecuteV1" : falcon.execute(search_parameters={"something": "somethingElse"}, end="10", start="1"),
            "CreateSavedSearchesIngestV1" : falcon.populate(app_id="pommegranate"),
            "GetSavedSearchesJobResultsDownloadV1" : falcon.download_results(job_id="12345", result_format="json"),
            "IngestDataAsyncV1": falcon.ingest_data_async(data_file="testfile.png", tag="file_tag"),
            "IngestDataAsyncV1variant": falcon.ingest_data_async(file="testfile.png", tag="file_tag"),
            "CreateFileV1": falcon.create_file(file="tests/testfile.json", repo="whatever"),
            "UpdateFileV1": falcon.update_file(file="tests/testfile.json", description="whatever")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(f"\n{key}\n")
                # print(tests[key])

        return error_checks

    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_functionality(self):
        assert self.run_all_tests() is True
