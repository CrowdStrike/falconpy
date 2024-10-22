# test_quick_scam.py
# This class tests the QuickScan Pro service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import QuickScanPro

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = QuickScanPro(auth_object=config)
AllowedResponses = [200, 201, 207, 429]  # Adding rate-limiting as an allowed response for now


class TestQuickScanPro:

    def pro_service_scan_test_all(self):
        error_checks = True
        PAYLOAD = open("tests/testfile.png", 'rb').read()
        tests = {
            "upload_file": falcon.upload_file(file=PAYLOAD, scan=False),
            "upload_file_fail": falcon.upload_file(),
            "delete_file": falcon.delete_file("123456NOTAHASH"),
            "get_scan_result": falcon.get_scan_result("123456NOTAHASH"),
            "launch_scan": falcon.launch_scan(sha256="123456NOTAHASH"),
            "launch_scan_fail": falcon.launch_scan(),
            "delete_scan_result": falcon.delete_scan_result("123456NOTAHASH"),
            "query_scan_results": falcon.query_scan_results(filter="123456NOTAHASH", limit=1)
        }
        for key in tests:
            if tests[key]["status_code"] == 500:
                error_checks = False

        return error_checks

    def test_all_functionality(self):
        assert self.pro_service_scan_test_all() is True
