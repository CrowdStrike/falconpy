# test_cloud_connect_aws.py
# This class tests the cloud_connect_aws service class

import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import cloud_connect_aws as FalconAWS

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconAWS.Cloud_Connect_AWS(access_token=auth.token)
AllowedResponses = [200, 201, 429] #Adding rate-limiting as an allowed response for now
accountPayload = {
        "resources": [
            {
                # "cloudtrail_bucket_owner_id": cloudtrail_bucket_owner_id,
                # "cloudtrail_bucket_region": cloudtrail_bucket_region,
                # "external_id": external_id,
                # "iam_role_arn": iam_role_arn,
                # "id": local_account,
                "rate_limit_reqs": 0,
                "rate_limit_time": 0
            }
        ]
    }
class TestCloudConnectAWS:
    def serviceCCAWS_GetAWSSettings(self):
        if falcon.GetAWSSettings()["status_code"] in AllowedResponses:
            return True
        else:
            return False      

    def serviceCCAWS_QueryAWSAccounts(self):
        if falcon.QueryAWSAccounts(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceCCAWS_GetAWSAccounts(self):
        if falcon.GetAWSAccounts(ids=falcon.QueryAWSAccounts(parameters={"limit":1})["body"]["resources"][0]["id"])["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceCCAWS_AccountUpdate(self):
        account = falcon.QueryAWSAccounts(parameters={"limit":1})["body"]["resources"][0]
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

    def serviceCCAWS_AccountDelete(self):
        if falcon.DeleteAWSAccounts(ids=accountPayload["resources"][0]["id"])["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceCCAWS_AccountRegister(self):
        if falcon.ProvisionAWSAccounts(body=accountPayload)["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceCCAWS_VerifyAWSAccountAccess(self):
        if falcon.VerifyAWSAccountAccess(ids=falcon.QueryAWSAccounts(parameters={"limit":1})["body"]["resources"][0]["id"])["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceCCAWS_QueryAWSAccountsForIDs(self):
        if falcon.QueryAWSAccountsForIDs(parameters={"limit":1})["status_code"] in AllowedResponses:
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
        if falcon.ProvisionAWSAccounts(body={})["status_code"] != 500:
            errorChecks = False
        if falcon.CreateOrUpdateAWSSettings(body={})["status_code"] != 500:
            errorChecks = False
        if falcon.VerifyAWSAccountAccess(ids="1234567890", body={})["status_code"] != 500:
            errorChecks = False

        return errorChecks

    def test_GetAWSSettings(self):
        assert self.serviceCCAWS_GetAWSSettings() == True

    def test_QueryAWSAccounts(self):
        assert self.serviceCCAWS_QueryAWSAccounts() == True
        
    @pytest.mark.skipif(falcon.QueryAWSAccounts(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    def test_GetAWSAccounts(self):
        assert self.serviceCCAWS_GetAWSAccounts() == True
    
    @pytest.mark.skipif(falcon.QueryAWSAccounts(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    def test_VerifyAWSAccountAccess(self):
        assert self.serviceCCAWS_VerifyAWSAccountAccess() == True
    
    @pytest.mark.skipif(falcon.QueryAWSAccounts(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    @pytest.mark.skipif(sys.version_info.minor < 9, reason="Frequency reduced due to potential race condition")
    def test_AccountUpdate(self):
        assert self.serviceCCAWS_AccountUpdate() == True
    
    @pytest.mark.skipif(falcon.QueryAWSAccounts(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    @pytest.mark.skipif(sys.version_info.minor < 9, reason="Frequency reduced due to potential race condition")
    def test_AccountDelete(self):
        assert self.serviceCCAWS_AccountDelete() == True

    def test_QueryAWSAccountsForIDs(self):
        assert self.serviceCCAWS_QueryAWSAccountsForIDs() == True
    
    @pytest.mark.skipif(falcon.QueryAWSAccounts(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    @pytest.mark.skipif(sys.version_info.minor < 9, reason="Frequency reduced due to potential race condition")
    def test_AccountRegister(self):
        assert self.serviceCCAWS_AccountRegister() == True

    def test_Logout(self):
        assert auth.serviceRevoke() == True

    def test_Errors(self):
        assert self.serviceCCAWS_GenerateErrors() == True
