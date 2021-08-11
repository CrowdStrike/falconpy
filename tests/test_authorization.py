# A valid CrowdStrike Falcon API key is required to run these tests.
# You can store these values in your environment (this is the preferred method).
# Example:
#    export DEBUG_API_ID=CLIENT_ID_GOES_HERE
#    export DEBUG_API_SECRET=CLIENT_SECRET_GOES_HERE
#
# You may also store these values locally in a configuration file.
# DO NOT SUBMIT A COMMIT OR A PR THAT INCLUDES YOUR CONFIGURATION FILE.
# API client ID & secret should be stored in tests/test.config in JSON format.
# {
#    "falcon_client_id": "CLIENT_ID_GOES_HERE",
#    "falcon_client_secret": "CLIENT_SECRET_GOES_HERE"
# }
import json
import os
import sys
import pytest
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from our sibling folder
# flake8: noqa=E402
from falconpy import api_complete as FalconSDK
from falconpy import oauth2 as FalconAuth
# Importing this to test disabling SSL Verification in a service class
from falconpy import hosts as FalconHosts


# The TestAuthorization class tests authentication and deauthentication
# for both the Uber and Service classes.
class TestAuthorization():
    def getConfig(self):
        # Grab our config parameters
        if "DEBUG_API_ID" in os.environ and "DEBUG_API_SECRET" in os.environ:
            self.config = {}
            self.config["falcon_client_id"] = os.getenv("DEBUG_API_ID")
            self.config["falcon_client_secret"] = os.getenv("DEBUG_API_SECRET")
            if "DEBUG_API_BASE_URL" in os.environ:
                self.config["falcon_base_url"] = os.getenv("DEBUG_API_BASE_URL")
            return True
        else:
            cur_path = os.path.dirname(os.path.abspath(__file__))
            if os.path.exists('%s/test.config' % cur_path):
                with open('%s/test.config' % cur_path, 'r') as file_config:
                    self.config = json.loads(file_config.read())
                return True
            else:
                return False

    def uberAuth(self):
        status = self.getConfig()
        if status:
            self.falcon = FalconSDK.APIHarness(creds={
                    "client_id": self.config["falcon_client_id"],
                    "client_secret": self.config["falcon_client_secret"]
                }
            )
            self.falcon.authenticate()
            if self.falcon.authenticated:
                return True
            else:
                return False
        else:
            return False

    def uberRevoke(self):
        return self.falcon.deauthenticate()

    def serviceAuth(self):
        status = self.getConfig()
        if status:
            self.authorization = FalconAuth.OAuth2(creds={
                'client_id': self.config["falcon_client_id"],
                'client_secret': self.config["falcon_client_secret"]
            })

            try:
                self.token = self.authorization.token()['body']['access_token']
            except KeyError:
                self.token = False

            if self.token:
                return True
            else:
                return False
        else:
            return False

    def serviceAuthNoSSL(self):
        status = self.getConfig()
        if status:
            self.authorization = FalconHosts.Hosts(creds={
                'client_id': self.config["falcon_client_id"],
                'client_secret': self.config["falcon_client_secret"]
            }, ssl_verify=False)

            if self.authorization.token:
                self.authorization.auth_object.revoke(self.authorization.token)
                return True
            else:
                return False
        else:
            return False

    def serviceMSSPAuth(self):
        status = self.getConfig()
        result = False
        if status:
            authorization = FalconAuth.OAuth2(creds={
                    'client_id': self.config["falcon_client_id"],
                    'client_secret': self.config["falcon_client_secret"],
                    'member_cid': '1234567890ABCDEFG'
                })
            try:
                req = authorization.token()
                if req["status_code"] in [201, 403]:  # Prolly an invalid MSSP cred, 403 is correct
                    result = True
            except KeyError:
                pass

        return result

    def failServiceAuth(self):
        self.authorization = FalconAuth.OAuth2(creds={
            'client_id': "BadClientID",
            'client_secret': "BadClientSecret"
        })
        self.authorization.base_url = "nowhere"
        try:
            self.token = self.authorization.token()['body']['access_token']
        except KeyError:
            self.token = False

        self.authorization.revoke(self.token)

        if self.token:
            return False
        else:
            return True

    def serviceRevoke(self):
        try:
            result = self.authorization.revoke(token=self.token)["status_code"]
            if result > 0:
                return True
            else:
                return False
        except KeyError:
            return False

    def credential_logout(self, api: object = None):
        if api:
            return bool(api.auth_object.revoke(api.auth_object.token()["body"]["access_token"])["status_code"] in [200, 201])
        else:
            return False

    def test_uberAuth(self):
        assert self.uberAuth() is True
        self.uberRevoke()

    def test_uberRevoke(self):
        self.uberAuth()
        assert self.uberRevoke() is True

    def test_serviceAuth(self):
        assert self.serviceAuth() is True
        self.serviceRevoke()

    # This test disables SSL and will generate a warning in pytest if we don't disable it
    @pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made.*")
    def test_serviceAuthNoSSL(self):
        assert self.serviceAuthNoSSL() is True

    def test_serviceMSSPAuth(self):
        assert self.serviceMSSPAuth() is True

    def test_serviceRevoke(self):
        self.serviceAuth()
        assert self.serviceRevoke() is True

    def test_failServiceAuth(self):
        assert self.failServiceAuth() is True
