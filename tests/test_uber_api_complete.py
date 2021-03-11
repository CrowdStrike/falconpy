# test_uber_api_complete.py
# This class tests the uber class

import json
import os
import sys
import pytest
import datetime
import hashlib
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from our sibling folder
from falconpy import api_complete as FalconSDK

AllowedResponses = [200, 400, 415, 429, 500]

if "DEBUG_API_ID" in os.environ and "DEBUG_API_SECRET" in os.environ:
    config = {}
    config["falcon_client_id"] = os.getenv("DEBUG_API_ID")
    config["falcon_client_secret"] = os.getenv("DEBUG_API_SECRET")
else:
    cur_path = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists('%s/test.config' % cur_path):
        with open('%s/test.config' % cur_path, 'r') as file_config:
            config = json.loads(file_config.read())
    else:
        sys.exit(1)

falcon = FalconSDK.APIHarness(
    creds={
        "client_id": config["falcon_client_id"],
        "client_secret": config["falcon_client_secret"]
    }
)
falcon.authenticate()
if not falcon.authenticated:
    sys.exit(1)


class TestUber:
    def uberCCAWS_GetAWSSettings(self):
        if falcon.command("GetAWSSettings")["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_QueryAWSAccounts(self):
        if falcon.command("QueryAWSAccounts", parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_GetAWSAccounts(self):
        if falcon.command("GetAWSAccounts", ids=falcon.command("QueryAWSAccounts",
                          parameters={"limit": 1})["body"]["resources"][0]["id"])["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_VerifyAWSAccountAccess(self):
        if falcon.command("VerifyAWSAccountAccess", ids=falcon.command("QueryAWSAccounts",
                          parameters={"limit": 1})["body"]["resources"][0]["id"])["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_QueryAWSAccountsForIDs(self):
        if falcon.command("QueryAWSAccountsForIDs", parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_TestUploadDownload(self):
        FILENAME = "tests/testfile.png"
        fmt = '%Y-%m-%d %H:%M:%S'
        stddate = datetime.datetime.now().strftime(fmt)
        sdtdate = datetime.datetime.strptime(stddate, fmt)
        sdtdate = sdtdate.timetuple()
        jdate = sdtdate.tm_yday
        jdate = "{}{}".format(stddate.replace("-", "").replace(":", "").replace(" ", ""), jdate)
        SOURCE = "%s_source.png" % jdate
        TARGET = "tests/%s_target.png" % jdate
        PAYLOAD = open(FILENAME, 'rb').read()
        response = falcon.command('UploadSampleV3', file_name=SOURCE, data=PAYLOAD, content_type="application/octet-stream")
        sha = response["body"]["resources"][0]["sha256"]
        response = falcon.command("GetSampleV3", parameters={}, ids=sha)
        open(TARGET, 'wb').write(response)
        buf = 65536
        hash1 = hashlib.sha256()
        with open(FILENAME, 'rb') as f:
            while True:
                data = f.read(buf)
                if not data:
                    break
                hash1.update(data)
        hash1 = hash1.hexdigest()
        hash2 = hashlib.sha256()
        with open(TARGET, 'rb') as f:
            while True:
                data = f.read(buf)
                if not data:
                    break
                hash2.update(data)
        hash2 = hash2.hexdigest()
        if os.path.exists(TARGET):
            os.remove(TARGET)
        if hash1 == hash2:
            return True
        else:
            return False

    def uberCCAWS_GenerateError(self):
        if falcon.command("QueryAWSAccounts", partition=0)["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_GenerateInvalidPayload(self):
        if falcon.command("refreshActiveStreamSession", partition=9,
                          parameters={"action_name": "refresh_active_stream_session"})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_OverrideAndHeader(self):
        if falcon.command(action="", override="GET,/cloud-connect-aws/combined/accounts/v1",
                          headers={"Nothing": "Special"})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_TestMSSP(self):
        falcon.creds["member_cid"] = "1234567890ABCDEFG"
        if not falcon.authenticate():
            falcon.creds.pop("member_cid")
            return True
        else:
            falcon.creds.pop("member_cid")
            return False

    def uberCCAWS_BadMethod(self):
        if falcon.command(action="", override="BANANA,/cloud-connect-aws/combined/accounts/v1",
                          headers={"Nothing": "Special"})["status_code"] == 405:
            return True
        else:
            return False

    def uberCCAWS_BadCommand(self):
        if falcon.command(action="IWantTheImpossible", parameters={"limit": 1})["status_code"] == 418:
            return True
        else:
            return False

    def uberCCAWS_GenerateServerError(self):
        if falcon.command("GetAWSAccounts", ids="123", data=['Kerash!'])["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCHosts_GenerateActionNameError(self):
        if falcon.command("PerformActionV2", parameters={}, body={}, action_name="Squish")["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_GenerateTokenError(self):
        hold_token = falcon.token
        falcon.token = "I am a bad token!"
        if not falcon.deauthenticate():
            falcon.token = hold_token
            return True
        else:
            falcon.token = hold_token
            return False

    def uberCCAWS_BadAuthentication(self):
        falcon = FalconSDK.APIHarness(
            creds={
                "client_id": "BadClientID",
                "client_secret": "BadClientSecret"
            }
        )
        if falcon.command("QueryAWSAccounts", parameters={"limit": 1})["status_code"] == 401:
            return True
        else:
            return False

    def uberCCAWS_DisableSSLVerify(self):
        falcon = FalconSDK.APIHarness(
            creds={
                "client_id": config["falcon_client_id"],
                "client_secret": config["falcon_client_secret"]
            }, ssl_verify=False
        )
        if falcon.command("QueryAWSAccounts", parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def test_GetAWSSettings(self):
        assert self.uberCCAWS_GetAWSSettings() == True

    def test_QueryAWSAccounts(self):
        assert self.uberCCAWS_QueryAWSAccounts() == True

    @pytest.mark.skipif(falcon.command("QueryAWSAccounts",
                        parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached")
    def test_GetAWSAccounts(self):
        assert self.uberCCAWS_GetAWSAccounts() == True

    @pytest.mark.skipif(falcon.command("QueryAWSAccounts",
                        parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached")
    def test_VerifyAWSAccountAccess(self):
        assert self.uberCCAWS_VerifyAWSAccountAccess() == True

    def test_QueryAWSAccountsForIDs(self):
        assert self.uberCCAWS_QueryAWSAccountsForIDs() == True

    def test_UploadDownload(self):
        assert self.uberCCAWS_TestUploadDownload() == True

    def test_GenerateError(self):
        assert self.uberCCAWS_GenerateError() == True

    def test_GenerateInvalidPayload(self):
        assert self.uberCCAWS_GenerateInvalidPayload() == True

    def test_BadCommand(self):
        assert self.uberCCAWS_BadCommand() == True

    def test_OverrideAndHeader(self):
        # Also check token auto-renewal
        falcon.token_expiration = 0
        assert self.uberCCAWS_OverrideAndHeader() == True

    def test_GenerateActionNameError(self):
        assert self.uberCCHosts_GenerateActionNameError() == True

    def test_BadMethod(self):
        assert self.uberCCAWS_BadMethod() == True

    def test_GenerateServerError(self):
        assert self.uberCCAWS_GenerateServerError() == True

    def test_TestMSSP(self):
        assert self.uberCCAWS_TestMSSP() == True

    # def test_logout(self):
    #     assert falcon.deauthenticate() == True

    def test_GenerateTokenError(self):
        assert self.uberCCAWS_GenerateTokenError() == True

    def test_BadAuthentication(self):
        assert self.uberCCAWS_BadAuthentication() == True

    @pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made.*")
    def test_DisableSSLVerify(self):
        assert self.uberCCAWS_DisableSSLVerify() == True
