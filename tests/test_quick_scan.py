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
auth.serviceAuth()
falcon = FalconScan.Quick_Scan(access_token=auth.token)
AllowedResponses = [200, 201, 207, 429]  # Adding rate-limiting as an allowed response for now


class TestQuickScan:

    def serviceScan_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["GetScansAggregates", "body={}"],
            ["GetScans", "ids='12345678'"],
            ["ScanSamples", "body={}"],
            ["QuerySubmissionsMixin0", ""]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_Logout(self):
        assert auth.serviceRevoke() is True

    def test_Errors(self):
        assert self.serviceScan_GenerateErrors() is True
