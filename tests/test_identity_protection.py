# test_identity_protection.py
# This class tests the identity_protection service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.identity_protection import Identity_Protection as FalconIDP

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconIDP(access_token=auth.token)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestIdentityProtection:
    def serviceIDP_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["GraphQL", "body={}"]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) not in [400, 403, 500]:
                errorChecks = False

        return errorChecks

    def test_Logout(self):
        assert auth.serviceRevoke() is True

    def test_Errors(self):
        assert self.serviceIDP_GenerateErrors() is True
