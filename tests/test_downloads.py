# test_downloads.py
# This class tests the Downloads service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import Downloads

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Downloads(auth_object=config)
AllowedResponses = [200, 201, 207, 404, 429]

class TestDownloads:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "FetchFilesDownloadInfo": falcon.fetch_download_info(),
            "FetchFilesDownloadInfoV2": falcon.fetch_download_info_v2(),
            "DownloadFile": falcon.download(file_name="the_file_named_jeff.txt", file_version="1"),
            "EnumerateFile": falcon.enumerate()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
