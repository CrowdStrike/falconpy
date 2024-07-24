# test_cloud_connect_aws.py
# This class tests the cloud_connect_aws service class
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CloudConnectAWS
from falconpy import oauth2 as FalconAuth
from falconpy._util import service_request

pytest.skip(allow_module_level=True)

auth = Authorization.TestAuthorization()

config = auth.getConfigObject()
falcon = CloudConnectAWS(auth_object=config)
AllowedResponses = [200, 201, 404, 429]  # Adding rate-limiting as an allowed response for now
accountPayload = {
        "resources": [
            {
                "rate_limit_reqs": 0,
                "rate_limit_time": 0
            }
        ]
    }
falconWithCreds = None
falconWithObject = None
_DEBUG = os.getenv("FALCONPY_UNIT_TEST_DEBUG", None)
if _DEBUG:
    _DEBUG = True

usone_only = pytest.mark.skipif(falcon.base_url.lower() != "https://api.crowdstrike.com",
                        reason="US-1 unit testing only",
                        )

class TestCloudConnectAWS:
    def serviceCCAWS_AuthWithCreds(self):
        falconWithCreds = CloudConnectAWS(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }, base_url=auth.config["falcon_base_url"], debug=_DEBUG)
        check = falconWithCreds.auth_object.token()
        if check["status_code"] == 429:
            pytest.skip("Rate limit hit")
        return falconWithCreds.authenticated()

    def serviceCCAWS_AuthWithObject(self):
        falconWithObject = CloudConnectAWS(auth_object=FalconAuth.OAuth2(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }, base_url=auth.config["falcon_base_url"], debug=_DEBUG))
        check = falconWithObject.auth_object.token()
        if check["status_code"] == 429:
            pytest.skip("Rate limit hit")
        return falconWithObject.authenticated()

    def serviceCCAWS_RefreshToken(self):
        falconWithObject = CloudConnectAWS(auth_object=FalconAuth.OAuth2(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }, base_url=auth.config["falcon_base_url"], debug=_DEBUG))
        check = falconWithObject.auth_object.token()
        if check["status_code"] == 429:
            pytest.skip("Rate limit hit")

        if not falconWithObject.token_expired():
            falconWithObject.auth_object.token_expiration = 0  # Forcibly expire the current token
            if falconWithObject.QueryAWSAccounts(parameters={"limit": 1})["status_code"] in AllowedResponses:
                return True
            else:
                return False
        else:
            return False

    def serviceCCAWS_InvalidPayloads(self):
        result = True
        falconWithObject = CloudConnectAWS(auth_object=FalconAuth.OAuth2(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }, base_url=auth.config["falcon_base_url"], debug=_DEBUG))
        check = falconWithObject.auth_object.token()
        if check["status_code"] == 429:
            pytest.skip("Rate limit hit")
        
        if not falconWithObject.QueryAWSAccounts(parameters={"limite": 1})["status_code"] in AllowedResponses:
            result = False

        if not falconWithObject.QueryAWSAccounts(parameters={"limit": "1"})["status_code"] in AllowedResponses:
            result = False

        if falconWithObject.UpdateAWSAccounts(body={"resource": "I'm gonna go Boom!"})["status_code"] != 400:
            result = False

        if falconWithObject.UpdateAWSAccounts(body={"resources": {"id": "I'm gonna go Boom!"}})["status_code"] != 400:
            result = False

        return result

    def serviceCCAWS_GetAWSAccountsUsingList(self):
        testing = falcon.QueryAWSAccounts(parameters={"limit": 2})
        if testing["body"]["resources"]:
            for registration in testing["body"]["resources"]:
                test_ids = registration["id"]
        else:
            test_ids = ["123456789012", "210987654321"]

        if falcon.GetAWSAccounts(ids=test_ids)["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceCCAWS_AccountUpdate(self):
        account = falcon.QueryAWSAccounts(parameters={"limit": 1})["body"]["resources"][0]
        accountPayload["resources"][0]["cloudtrail_bucket_owner_id"] = account["cloudtrail_bucket_owner_id"]
        accountPayload["resources"][0]["cloudtrail_bucket_region"] = account["cloudtrail_bucket_region"]
        orig_external_id = account["external_id"]
        accountPayload["resources"][0]["external_id"] = "UnitTesting"
        accountPayload["resources"][0]["iam_role_arn"] = account["iam_role_arn"]
        accountPayload["resources"][0]["id"] = account["id"]
        if falcon.UpdateAWSAccounts(body=accountPayload)["status_code"] in AllowedResponses:
            accountPayload["resources"][0]["external_id"] = orig_external_id
            return True
        else:
            accountPayload["resources"][0]["external_id"] = orig_external_id
            return False

    def serviceCCAWS_ForceAttributeError(self):
        FULL_URL = falcon.base_url+'/cloud-connect-aws/combined/accounts/v1'
        if service_request(caller=self,
                           method="GET",
                           endpoint=FULL_URL,
                           headers=falcon.headers,
                           verify=falcon.ssl_verify
                           )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceCCAWS_GenerateErrors(self):
        # Garf the base_url so we force 500s for each method to cover all remaining code paths
        falcon.base_url = "nowhere"
        errorChecks = True
        if falcon.QueryAWSAccounts()["status_code"] != 500:
            errorChecks = False
        if falcon.QueryAWSAccountsForIDs()["status_code"] != 500:
            errorChecks = False
        if falcon.GetAWSSettings()["status_code"] != 500:
            errorChecks = False
        if falcon.GetAWSAccounts(ids="1234567890")["status_code"] != 500:
            errorChecks = False
        if falcon.UpdateAWSAccounts(body={})["status_code"] != 500:
            errorChecks = False
        if falcon.DeleteAWSAccounts(ids="1234567890")["status_code"] != 500:
            errorChecks = False
        if falcon.ProvisionAWSAccounts(
                cloudtrail_bucket_owner_id="string",
                cloudtrail_bucket_region="string",
                external_id="string",
                iam_role_arn="string",
                id="string",
                rate_limit_reqs=0,
                rate_limit_time=0,
                static_external_id="string"
                )["status_code"] != 500:
            errorChecks = False
        if falcon.CreateOrUpdateAWSSettings(body={})["status_code"] != 500:
            errorChecks = False
        if falcon.VerifyAWSAccountAccess(ids="1234567890")["status_code"] != 500:
            errorChecks = False

        return errorChecks

    @usone_only
    def test_GetAWSSettings(self):
        assert bool(falcon.GetAWSSettings()["status_code"] in AllowedResponses) is True

    @usone_only
    def test_QueryAWSAccounts(self):
        assert bool(falcon.QueryAWSAccounts(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    @usone_only
    @pytest.mark.skipif(falcon.QueryAWSAccounts(
        parameters={"limit": 1}
        )["status_code"] == 429, reason="API rate limit reached")
    def test_GetAWSAccounts(self):
        testing = falcon.QueryAWSAccounts(parameters={"limit": 1})
        if testing["body"]["resources"]:
            test_id = testing["body"]["resources"][0]["id"]
        else:
            test_id = "123456789012"
        assert bool(falcon.GetAWSAccounts(ids=test_id)["status_code"] in AllowedResponses) is True

    @usone_only
    @pytest.mark.skipif(falcon.QueryAWSAccounts(
        parameters={"limit": 1}
        )["status_code"] == 429, reason="API rate limit reached")
    def test_GetAWSAccountsUsingList(self):
        assert self.serviceCCAWS_GetAWSAccountsUsingList() is True

    @usone_only
    def test_QueryAWSAccountsForIDs(self):
        assert bool(falcon.QueryAWSAccountsForIDs(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    @usone_only
    def test_AuthWithCreds(self):
        assert self.serviceCCAWS_AuthWithCreds() is True

    @usone_only
    def test_AuthWithObject(self):
        assert self.serviceCCAWS_AuthWithObject() is True

    @usone_only
    def test_RefreshToken(self):
        assert self.serviceCCAWS_RefreshToken() is True

    @usone_only
    def test_InvalidPayloads(self):
        assert self.serviceCCAWS_InvalidPayloads() is True

    @usone_only
    def test_ForceAttributeError(self):
        assert self.serviceCCAWS_ForceAttributeError() is True

    @usone_only
    def test_argument_vs_keyword(self):
        assert bool(falcon.get_aws_accounts("123456789012")["status_code"] in AllowedResponses) is True

    @usone_only
    def test_Errors(self):
        assert self.serviceCCAWS_GenerateErrors() is True
