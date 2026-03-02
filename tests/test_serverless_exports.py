# test_serverless_exports.py
# This class tests the ServerlessExports service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ServerlessExports

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ServerlessExports(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestServerlessExports:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "QueryExportJobsMixin0": falcon.query_export_jobs(),
            "LaunchExportJobMixin0": falcon.launch_export_job(resource="function.detections", format="csv"),
            "ReadExportJobsMixin0": falcon.read_export_jobs(ids="12345"),
            "DownloadExportFileMixin0": falcon.download_export_file(id="12345"),
            "GetCombinedVulnerabilitiesSARIF": falcon.get_vulnerabilities(limit=1),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
