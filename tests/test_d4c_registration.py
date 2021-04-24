# test_d4c_registration.py
# This class tests the Discover for Cloud registration service class
import os
import sys

# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.d4c_registration import D4C_Registration as FalconD4C

auth = Authorization.TestAuthorization()
auth.getConfig()
falcon = FalconD4C(creds={"client_id": auth.config["falcon_client_id"],
                          "client_secret": auth.config["falcon_client_secret"]
                          })
AllowedResponses = [200, 429, 404]


class TestD4CRegistration:
    def serviceD4C_GetCSPMAzureUserScriptsAttachment(self):
        returned = False
        result = falcon.GetCSPMAzureUserScriptsAttachment()
        if isinstance(result, (bytes)):
            returned = True
        else:
            if "status_code" in result:
                if result["status_code"] in AllowedResponses:
                    returned = True

        return returned

    def serviceD4C_GetCSPMAzureUserScripts(self):
        returned = False
        result = falcon.GetCSPMAzureUserScripts()
        if isinstance(result, (bytes)):
            returned = True
        else:
            if "status_code" in result:
                if result["status_code"] in AllowedResponses:
                    returned = True

        return returned

    def serviceD4C_GetCSPMGCPUserScriptsAttachment(self):
        returned = False
        result = falcon.GetCSPMGCPUserScriptsAttachment()
        if isinstance(result, (bytes)):
            returned = True
        else:
            if "status_code" in result:
                if result["status_code"] in AllowedResponses:
                    returned = True

        return returned

    def serviceD4C_GetCSPMGCPUserScripts(self):
        returned = False
        result = falcon.GetCSPMGCPUserScripts()
        if isinstance(result, (bytes)):
            returned = True
        else:
            if "status_code" in result:
                if result["status_code"] in AllowedResponses:
                    returned = True

        return returned

    def serviceD4C_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["GetCSPMAzureAccount", "ids='12345678', scan_type='dry'"],
            ["UpdateCSPMAzureAccountClientID", "ids='12345678'"],
            ["GetCSPMCGPAccount", "ids='12345678', parameters={'scan_type': 'dry'}"],
            ["GetCSPMGCPAccount", "ids='12345678'"],  # Test the typo fix version
            ["CreateCSPMGCPAccount", "body={}"],
            ["CreateCSPMAzureAccount", "body={}"]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_GetCSPMAzureUserScriptsAttachment(self):
        assert self.serviceD4C_GetCSPMAzureUserScriptsAttachment() is True

    def test_GetCSPMAzureUserScripts(self):
        assert self.serviceD4C_GetCSPMAzureUserScripts() is True

    def test_GetCSPMGCPUserScriptsAttachment(self):
        assert self.serviceD4C_GetCSPMGCPUserScriptsAttachment() is True

    def test_GetCSPMGCPUserScripts(self):
        assert self.serviceD4C_GetCSPMGCPUserScripts() is True

    def test_Errors(self):
        assert self.serviceD4C_GenerateErrors() is True
