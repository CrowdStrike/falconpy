# test_quick_scam.py
# This class tests the quick_scan service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import quick_scan as FalconScan

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = FalconScan.Quick_Scan(access_token=token)
AllowedResponses = [200, 201, 207, 429]  # Adding rate-limiting as an allowed response for now


class TestQuickScan:

    def serviceScan_GenerateErrors(self):
        falcon.base_url = "nowhere"
        error_checks = True
        commandList = [
            ["GetScansAggregates", "body={}"],
            ["GetScans", "ids='12345678'"],
            ["ScanSamples", "body={}"],
            ["QuerySubmissionsMixin0", ""]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                error_checks = False

        return error_checks

    def test_Errors(self):
        assert self.serviceScan_GenerateErrors() is True
