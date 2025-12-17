"""
test_d4c_registration.py - This class tests the Discover for Cloud registration service class
"""
import os
import sys
import pytest
# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import D4CRegistration

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = D4CRegistration(auth_object=config)
AllowedResponses = [200, 429, 400, 404, 403]


class TestD4CRegistration:
    """
    Test harness for the D4C Registration Service Class
    """
    def d4c_get_azure_user_scripts_attachment(self):
        """
        get_azure_user_scripts_attachment
        """
        returned = False
        result = falcon.GetCSPMAzureUserScriptsAttachment(tenant_id="12345678")
        if isinstance(result, bytes):
            returned = True
        else:
            if "status_code" in result:
                if result["status_code"] in AllowedResponses:
                    returned = True

        return returned

    def d4c_get_azure_user_scripts(self):
        """
        get_azure_user_scripts
        """
        returned = False
        result = falcon.GetCSPMAzureUserScripts()
        if isinstance(result, (bytes)):
            returned = True
        else:
            if "status_code" in result:
                if result["status_code"] in AllowedResponses:
                    returned = True

        return returned

    def d4c_get_gcp_user_scripts_attachment(self):
        """
        get_gcp_user_scripts_attachment
        """
        returned = False
        result = falcon.GetCSPMGCPUserScriptsAttachment()
        if isinstance(result, (bytes)):
            returned = True
        else:
            if "status_code" in result:
                if result["status_code"] in AllowedResponses:
                    returned = True

        return returned

    def d4c_get_gcp_user_scripts(self):
        """
        get_gcp_user_scripts
        """
        returned = False
        result = falcon.GetCSPMGCPUserScripts()
        if isinstance(result, (bytes)):
            returned = True
        else:
            if "status_code" in result:
                if result["status_code"] in AllowedResponses:
                    returned = True

        return returned

    def d4c_generate_errors(self):
        """
        Test every code path within every method by generating 500s, does not hit the API
        """
        falcon.base_url = "nowhere"
        error_checks = True
        tests = {
            "get_azure_account": falcon.GetCSPMAzureAccount(ids='12345678', scan_type='dry'),
            "update_azure_account_client_id": falcon.UpdateCSPMAzureAccountClientID(ids='12345678', tenant_id="12345678"),
            "get_cgp_account": falcon.GetCSPMCGPAccount(ids='12345678', parameters={'scan_type': 'dry'}),
            "get_gcp_acocunt": falcon.GetCSPMGCPAccount(ids='12345678'),  # Test the typo fix version
            "create_gcp_account": falcon.CreateCSPMGCPAccount(body={}, parent_id="12345678"),
            "create_azure_account": falcon.CreateCSPMAzureAccount(body={}, subscription_id="12345678", tenant_id="12345678", years_valid=3, default_subscription=False),
            "azure_download_certificate": falcon.DiscoverCloudAzureDownloadCertificate("12345678"),  # Also testing arg handling
            "GetD4CAwsAccount": falcon.get_aws_account("123456789", scan_type="dry"),
            "CreateD4CAwsAccount": falcon.create_aws_account(account_id="123456789",
                                                             account_type="single",
                                                             cloudtrail_region="us-east-2",
                                                             is_master=False,
                                                             organization_id="12345678"
                                                             ),
            "DeleteD4CAwsAccount": falcon.delete_aws_account("ID_DOES_NOT_EXIST"),
            "GetD4CAwsConsoleSetupURLs": falcon.get_aws_console_setup("us-east-2"),
            "GetD4CAwsAccountScriptsAttachment": falcon.get_aws_account_scripts(ids="12345678",
                                                                                behavior_assessment_enabled=False,
                                                                                sensor_management_enabled=False,
                                                                                vulnerability_scanning_enabled=False
                                                                                ),
            "GetHorizonD4CScripts": falcon.get_aws_horizon_scripts(organization_id="123456789"),
            "GetDiscoverCloudAzureTenantIDs": falcon.get_azure_tenant_ids(),
            "DeleteD4CGCPAccount": falcon.delete_gcp_account("1234567"),
            "ConnectD4CGCPAccount": falcon.connect_gcp_account(client_id="123456", parent_id="123456"),
            "GetD4CGCPServiceAccoutnExt": falcon.get_gcp_service_account(id="12345678"),
            "GetD4CGCPUserScriptsAttachmentV2": falcon.get_gcp_user_scripts_attachment_v2(ids="12345678"),
            "UpdateD4CGCPServiceAccountsExt": falcon.update_gcp_service_account(service_account_id=2),
        }
        for key in tests:
            if tests[key]["status_code"] != 500:
                error_checks = False

            # print(f"{key} processed with a {tests[key]} response")

        return error_checks

    @pytest.mark.skipif(config.base_url == "https://api.eu-1.crowdstrike.com",
                        reason="Unit testing unavailable on EU-1"
                        )
    def test_GetCSPMAzureUserScriptsAttachment(self):
        """
        Pytest harness hook
        """
        assert self.d4c_get_azure_user_scripts_attachment() is True

    def test_GetCSPMAzureUserScripts(self):
        """
        Pytest harness hook
        """
        assert self.d4c_get_azure_user_scripts() is True

    def test_GetCSPMGCPUserScriptsAttachment(self):
        """
        Pytest harness hook
        """
        assert self.d4c_get_gcp_user_scripts_attachment() is True

    def test_GetCSPMGCPUserScripts(self):
        """
        Pytest harness hook
        """
        assert self.d4c_get_gcp_user_scripts() is True

    def test_Errors(self):
        """
        Pytest harness hook
        """
        assert self.d4c_generate_errors() is True

    # @staticmethod
    # def test_logout():
    #     """
    #     Pytest harness hook
    #     """
    #     assert bool(falcon.auth_object.revoke(
    #         falcon.auth_object.token()["body"]["access_token"]
    #         )["status_code"] in AllowedResponses) is True
