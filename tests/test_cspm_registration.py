# test_cspm_registration.py
# This class tests the cspm_registration service class

import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import cspm_registration as FalconCSPM  # noqa: E402

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconCSPM.CSPM_Registration(access_token=auth.token)
AllowedResponses = [200, 201, 207, 429]  # Adding rate-limiting as an allowed response for now
textchars = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7f})
is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))  # noqa: E731


class TestCSPMRegistration:

    def serviceCSPM_GetCSPMAwsConsoleSetupURLs(self):
        if falcon.GetCSPMAwsConsoleSetupURLs()["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceCSPM_GetCSPMAwsAccountScriptsAttachment(self):
        if type(falcon.GetCSPMAwsAccountScriptsAttachment()) == bytes:
            return True
        else:
            return False

    def serviceCSPM_GetCSPMAzureUserScriptsAttachment(self):
        test_result = falcon.GetCSPMAzureUserScriptsAttachment()
        if type(test_result) == bytes:
            return True
        else:
            if test_result["body"]["errors"][0]["message"] == "No accounts found":
                return True
            else:
                return False

    def serviceStream_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["GetCSPMAwsAccount", "ids='12345678', org_ids='12345678'"],
            ["CreateCSPMAwsAccount", "body={}"],
            ["DeleteCSPMAwsAccount", "ids='12345678', org_ids='12345678'"],
            ["DeleteCSPMAwsAccount", "org_ids='12345678'"],
            ["GetCSPMAzureAccount", "ids='12345678'"],
            ["CreateCSPMAzureAccount", "body={}"],
            ["DeleteCSPMAzureAccount", "ids='12345678'"],
            ["UpdateCSPMAzureAccountClientID", ""],
            ["GetCSPMPolicy", "ids='12345678'"],
            ["GetCSPMPolicySettings", ""],
            ["UpdateCSPMPolicySettings", "body={}"],
            ["GetCSPMScanSchedule", ""],
            ["UpdateCSPMScanSchedule", "body={}"],
            ["PatchCSPMAwsAccount", "body={}"],
            ["UpdateCSPMAzureTenantDefaultSubscriptionID", "body={}"],
            ["GetIOAEvents", ""],
            ["GetIOAUsers", ""],
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_GetCSPMAwsConsoleSetupURLs(self):
        assert self.serviceCSPM_GetCSPMAwsConsoleSetupURLs() is True

    def test_GetCSPMAwsAccountScriptsAttachment(self):
        assert self.serviceCSPM_GetCSPMAwsAccountScriptsAttachment() is True

    def test_GetCSPMAzureUserScriptsAttachment(self):
        assert self.serviceCSPM_GetCSPMAzureUserScriptsAttachment() is True

    def test_Logout(self):
        assert auth.serviceRevoke() is True

    def test_Errors(self):
        assert self.serviceStream_GenerateErrors() is True
