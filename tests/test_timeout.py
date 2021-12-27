# test_timeout.py
# This class tests request timeouts
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CloudConnectAWS
from falconpy import OAuth2

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
# auth.serviceAuth()

AllowedResponses = [200, 429, 500]  # Adding rate-limiting as an allowed response for now


class TestTimeouts:
    def timeout_test(self):
        falcon = CloudConnectAWS(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        })
        success = False
        result = falcon.QueryAWSAccounts()
        if result['status_code'] in AllowedResponses:
            success = True

        return success

    def timeout_connect(self):
        falconConnectFail = CloudConnectAWS(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }, timeout=(.001, 5)
        )
        success = False
        result = falconConnectFail.QueryAWSAccounts()
        if result['status_code'] in AllowedResponses:
            if "connect timeout" in result["body"]["errors"][0]["message"]:
                success = True

        return success

    def timeout_read(self):
        falconReadFail = CloudConnectAWS(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }, timeout=(5, .001)
        )
        success = False
        result = falconReadFail.QueryAWSAccounts()
        if result['status_code'] in AllowedResponses:
            if "read timeout" in result["body"]["errors"][0]["message"]:
                success = True

        return success

    def timeout_standard(self):
        falconStandardFail = CloudConnectAWS(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }, timeout=.001
        )
        success = False
        result = falconStandardFail.QueryAWSAccounts()
        if result['status_code'] in AllowedResponses:
            if "connect timeout" in result["body"]["errors"][0]["message"]:
                success = True

        return success

    def timeout_legacy_auth(self):
        falconLegacyFail = OAuth2(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }, timeout=.001)
        success = False
        result = falconLegacyFail.token()
        if result["status_code"] in AllowedResponses:
            if "connect timeout" in result["body"]["errors"][0]["message"]:
                success = True

        return success

    def test_NoTimeout(self):
        assert self.timeout_test() is True

    def test_StandardTimeout(self):
        assert self.timeout_standard() is True

    def test_ConnectTimeout(self):
        assert self.timeout_connect() is True

    def test_ReadTimeout(self):
        assert self.timeout_read() is True

    def test_LegacyTimeout(self):
        assert self.timeout_legacy_auth() is True
