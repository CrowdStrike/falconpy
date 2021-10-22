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
from falconpy import cloud_connect_aws as FalconAWS
from falconpy import oauth2 as FalconAuth
from falconpy._util import service_request

auth = Authorization.TestAuthorization()

token = auth.getConfigExtended()
falcon = FalconAWS.Cloud_Connect_AWS(access_token=token)
AllowedResponses = [200, 201, 429]  # Adding rate-limiting as an allowed response for now
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


class TestCloudConnectAWS:
    def serviceCCAWS_AuthWithCreds(self):
        falconWithCreds = FalconAWS.Cloud_Connect_AWS(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        })

        return falconWithCreds.authenticated()

    def serviceCCAWS_AuthWithObject(self):
        falconWithObject = FalconAWS.Cloud_Connect_AWS(auth_object=FalconAuth.OAuth2(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }))

        return falconWithObject.authenticated()

    def serviceCCAWS_RefreshToken(self):
        falconWithObject = FalconAWS.Cloud_Connect_AWS(auth_object=FalconAuth.OAuth2(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }))

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
        falconWithObject = FalconAWS.Cloud_Connect_AWS(auth_object=FalconAuth.OAuth2(creds={
            'client_id': auth.config["falcon_client_id"],
            'client_secret': auth.config["falcon_client_secret"]
        }))
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
        liste = []
        for thing in falcon.QueryAWSAccounts(parameters={"limit": 2})["body"]["resources"]:
            liste.append(thing["id"])
        if falcon.GetAWSAccounts(ids=liste)["status_code"] in AllowedResponses:
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

    def test_GetAWSSettings(self):
        assert bool(falcon.GetAWSSettings()["status_code"] in AllowedResponses) is True

    def test_QueryAWSAccounts(self):
        assert bool(falcon.QueryAWSAccounts(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(falcon.QueryAWSAccounts(
        parameters={"limit": 1}
        )["status_code"] == 429, reason="API rate limit reached")
    def test_GetAWSAccounts(self):
        assert bool(falcon.GetAWSAccounts(ids=falcon.QueryAWSAccounts(
                    parameters={"limit": 1}
                    )["body"]["resources"][0]["id"])["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(falcon.QueryAWSAccounts(
        parameters={"limit": 1}
        )["status_code"] == 429, reason="API rate limit reached")
    def test_GetAWSAccountsUsingList(self):
        assert self.serviceCCAWS_GetAWSAccountsUsingList() is True

    def test_QueryAWSAccountsForIDs(self):
        assert bool(falcon.QueryAWSAccountsForIDs(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    def test_AuthWithCreds(self):
        assert self.serviceCCAWS_AuthWithCreds() is True

    def test_AuthWithObject(self):
        assert self.serviceCCAWS_AuthWithObject() is True

    def test_RefreshToken(self):
        assert self.serviceCCAWS_RefreshToken() is True

    def test_InvalidPayloads(self):
        assert self.serviceCCAWS_InvalidPayloads() is True

    def test_ForceAttributeError(self):
        assert self.serviceCCAWS_ForceAttributeError() is True

    def test_argument_vs_keyword(self):
        assert bool(
            falcon.VerifyAWSAccountAccess(falcon.QueryAWSAccountsForIDs(limit=1)["body"]["resources"][0])
            ) is True

    def test_Errors(self):
        assert self.serviceCCAWS_GenerateErrors() is True

    # @staticmethod
    # def test_logout():
    #     """
    #     Pytest harness hook
    #     """
    #     assert bool(falcon.auth_object.revoke(
    #         falcon.auth_object.token()["body"]["access_token"]
    #         )["status_code"] in AllowedResponses) is True
