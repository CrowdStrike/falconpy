# test_cspm_registration.py
# This class tests the cspm_registration service class

import json
import os
import sys
import datetime
import requests
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import cspm_registration as FalconCSPM

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconCSPM.CSPM_Registration(access_token=auth.token)
AllowedResponses = [200, 201, 207, 429] #Adding rate-limiting as an allowed response for now
textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))

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
        #print(falcon.GetCSPMAzureUserScriptsAttachment())
        if type(falcon.GetCSPMAzureUserScriptsAttachment()) == bytes:
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
#            ["GetCSPMAwsConsoleSetupURLs", ""],
#            ["GetCSPMAwsAccountScriptsAttachment", "body={}"],
            ["GetCSPMAzureAccount", "ids='12345678'"],
            ["CreateCSPMAzureAccount", "body={}"],
            ["DeleteCSPMAzureAccount", "ids='12345678'"],
            ["UpdateCSPMAzureAccountClientID", ""],
#            ["GetCSPMAzureUserScriptsAttachment", ""],
            ["GetCSPMPolicy", "ids='12345678'"],
            ["GetCSPMPolicySettings", ""],
            ["UpdateCSPMPolicySettings", "body={}"],
            ["GetCSPMScanSchedule", ""],
            ["UpdateCSPMScanSchedule", "body={}"]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_GetCSPMAwsConsoleSetupURLs(self):
        assert self.serviceCSPM_GetCSPMAwsConsoleSetupURLs() == True

    def test_GetCSPMAwsAccountScriptsAttachment(self):
        assert self.serviceCSPM_GetCSPMAwsAccountScriptsAttachment() == True

    def test_GetCSPMAzureUserScriptsAttachment(self):
        assert self.serviceCSPM_GetCSPMAzureUserScriptsAttachment() == True


    def test_Logout(self):
        assert auth.serviceRevoke() == True

    def test_Errors(self):
        assert self.serviceStream_GenerateErrors() == True