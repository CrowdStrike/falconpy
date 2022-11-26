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
from falconpy import APIHarness
from falconpy import OAuth2
# Importing this to test disabling SSL Verification in a service class
from falconpy import Hosts

shared_token = None
_DEBUG = os.getenv("FALCONPY_UNIT_TEST_DEBUG", None)
if _DEBUG:
    _DEBUG = True

# The TestAuthorization class tests authentication and deauthentication
# for both the Uber and Service classes.
class TestAuthorization():
    def getConfigObject(self):
        status = self.getConfig()
        if status:
            os.environ["FALCONPY_DEBUG_CLIENT_ID"] = self.config["falcon_client_id"]
            os.environ["FALCONPY_DEBUG_CLIENT_SECRET"] = self.config["falcon_client_secret"]
            self.authorization = OAuth2(creds={
                "client_id": self.config["falcon_client_id"],
                "client_secret": self.config["falcon_client_secret"]
            },
            base_url = self.config["falcon_base_url"], debug=_DEBUG)
        try:
            global shared_token
            if not shared_token:
                shared_token = self.authorization.token()['body']['access_token']
        except KeyError:
            shared_token = False
        
        return self.authorization

    def getConfigExtended(self):
        if "FALCONPY_DEBUG_TOKEN" in os.environ:
            self.token = os.getenv("FALCONPY_DEBUG_TOKEN")
            self.config = {}
            self.config["falcon_client_id"] = os.environ["FALCONPY_DEBUG_CLIENT_ID"]
            self.config["falcon_client_secret"] = os.environ["FALCONPY_DEBUG_CLIENT_SECRET"]
            if "DEBUG_API_BASE_URL" in os.environ:
                self.config["falcon_base_url"] = os.getenv("DEBUG_API_BASE_URL")
            else:
                self.config["falcon_base_url"] = "https://api.crowdstrike.com"
        else:
            status = self.getConfig()
            if status:
                os.environ["FALCONPY_DEBUG_CLIENT_ID"] = self.config["falcon_client_id"]
                os.environ["FALCONPY_DEBUG_CLIENT_SECRET"] = self.config["falcon_client_secret"]
                self.authorization = OAuth2(creds={
                    "client_id": self.config["falcon_client_id"],
                    "client_secret": self.config["falcon_client_secret"]
                },
                base_url = self.config["falcon_base_url"], debug=_DEBUG)
            try:
                self.token = self.authorization.token()['body']['access_token']
                os.environ["FALCONPY_DEBUG_TOKEN"] = self.token
            except KeyError:
                self.token = False
        
        return self.token

    def clear_env_token(self):
        if "FALCONPY_DEBUG_TOKEN" in os.environ:
            os.environ["FALCONPY_DEBUG_TOKEN"] = ""
            os.environ["FALCONPY_DEBUG_CLIENT_ID"] = ""
            os.environ["FALCONPY_DEBUG_CLIENT_SECRET"] = ""
        return True

    def getConfig(self):
        # Grab our config parameters
        if "DEBUG_API_ID" in os.environ and "DEBUG_API_SECRET" in os.environ:
            self.config = {}
            self.config["falcon_client_id"] = os.getenv("DEBUG_API_ID")
            self.config["falcon_client_secret"] = os.getenv("DEBUG_API_SECRET")
            if "DEBUG_API_BASE_URL" in os.environ:
                self.config["falcon_base_url"] = os.getenv("DEBUG_API_BASE_URL")
            else:
                self.config["falcon_base_url"] = "auto"
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
            self.falcon = APIHarness(creds={
                    "client_id": self.config["falcon_client_id"],
                    "client_secret": self.config["falcon_client_secret"],
                }, base_url=self.config["falcon_base_url"], renew_window=300, debug=_DEBUG
            )
            self.falcon.authenticate()
            if self.falcon.authenticated:
                return True
            else:
                if self.falcon.base_url == "https://api.laggar.gcw.crowdstrike.com":
                    pytest.skip("GovCloud rate limit hit")
                else:
                    return False
        else:
            return False

    def failUberMSSPAuth(self):
        status = self.getConfig()
        if status:
            self.falcon = APIHarness(client_id=self.config["falcon_client_id"],
                                     client_secret=self.config["falcon_client_secret"],
                                     member_cid="1234567890ABCDEFG", debug=_DEBUG
                                     )
            self.falcon.authenticate()
            if not self.falcon.authenticated:
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
            self.authorization = OAuth2(creds={
                'client_id': self.config["falcon_client_id"],
                'client_secret': self.config["falcon_client_secret"]
                },
                base_url=self.config["falcon_base_url"], debug=_DEBUG
            )

            try:
                check = self.authorization.token()
                if check["status_code"] == 429:
                    pytest.skip("Rate limit hit")
                self.token = check['body']['access_token']
                # Force a token authentication
                _ = Hosts(access_token=self.token)
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
            self.authorization = Hosts(creds={
                'client_id': self.config["falcon_client_id"],
                'client_secret': self.config["falcon_client_secret"]
            }, ssl_verify=False, base_url=self.config["falcon_base_url"], debug=_DEBUG)

            check = self.authorization.auth_object.token()
            if check["status_code"] == 429:
                pytest.skip("Rate limit hit")
            if check["body"]["access_token"]:
                self.authorization.auth_object.revoke(check["body"]["access_token"])
                return True
            else:
                return False
        else:
            return False

    def serviceMSSPAuth(self):
        status = self.getConfig()
        result = False
        if status:
            authorization = OAuth2(client_id=self.config["falcon_client_id"],
                                   client_secret=self.config["falcon_client_secret"],
                                   member_cid='1234567890ABCDEFG', debug=_DEBUG
                                   )
            try:
                req = authorization.token()
                if req["status_code"] in [201, 403]:  # Prolly an invalid MSSP cred, 403 is correct
                    result = True
            except KeyError:
                pass

        return result

    def failServiceAuth(self):
        self.authorization = Hosts(client_id="BadClientID",
                                   client_secret="BadClientSecret",
                                   member_cid="123456789ABCDEFG",
                                   base_url = "us3", debug=_DEBUG
                                   )
        # self.authorization.auth_object.base_url = "nowhere"
        try:
            self.token = self.authorization.auth_object.token()['body']['access_token']
        except KeyError:
            self.token = False

        self.authorization.auth_object.revoke(self.token)

        if self.token:
            return False
        else:
            return True

    def serviceRevoke(self):
        try:
            result = self.authorization.revoke(token=self.token, client_id=self.config["falcon_client_id"])["status_code"]
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

    def test_uberMSSPAuthFailure(self):
        assert self.failUberMSSPAuth() is True

    def test_serviceRevoke(self):
        self.serviceAuth()
        assert self.serviceRevoke() is True

    def test_failServiceAuth(self):
        assert self.failServiceAuth() is True

    @pytest.mark.skipif(os.getenv("DEBUG_API_BASE_URL", "us1").lower() in ["https://api.laggar.gcw.crowdstrike.com","usgov1"],
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_base_url_lookup(self):
        _ = self.getConfig()
        test_falcon = OAuth2(
            client_id=self.config["falcon_client_id"],
            client_secret=self.config["falcon_client_secret"],
            base_url="us1", debug=_DEBUG
        )
        assert bool(
            test_falcon.token()["status_code"] == 201
        )

    def test_fail_base_url_lookup(self):
        _ = self.getConfig()
        test_falcon = OAuth2(
            client_id=self.config["falcon_client_id"],
            client_secret=self.config["falcon_client_secret"],
            base_url="nowhere", debug=_DEBUG
        )
        assert bool(
            test_falcon.token()["status_code"] != 201
        )
