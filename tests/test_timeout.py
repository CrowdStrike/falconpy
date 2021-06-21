# test_timeout.py
# This class tests request timeouts
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.cloud_connect_aws import Cloud_Connect_AWS as FalconAWS

auth = Authorization.TestAuthorization()
auth.serviceAuth()

AllowedResponses = [200, 429, 500]  # Adding rate-limiting as an allowed response for now


class TestTimeouts:
    def timeout_test(self):
        falcon = FalconAWS(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        })
        success = False
        result = falcon.QueryAWSAccounts()
        if result['status_code'] in AllowedResponses:
            success = True

        return success

    def timeout_connect(self):
        falconConnectFail = FalconAWS(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }, timeout=(.01, 5)
        )
        success = False
        result = falconConnectFail.QueryAWSAccounts()
        if result['status_code'] in AllowedResponses:
            if "connect timeout" in result["body"]["errors"][0]["message"]:
                success = True

        return success

    def timeout_read(self):
        falconReadFail = FalconAWS(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }, timeout=(5, .01)
        )
        success = False
        result = falconReadFail.QueryAWSAccounts()
        if result['status_code'] in AllowedResponses:
            if "read timeout" in result["body"]["errors"][0]["message"]:
                success = True

        return success

    def timeout_standard(self):
        falconStandardFail = FalconAWS(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }, timeout=(.01)
        )
        success = False
        result = falconStandardFail.QueryAWSAccounts()
        if result['status_code'] in AllowedResponses:
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
