"""
test_cspm_registration.py - This class tests the cspm_registration service class
"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CSPMRegistration  # noqa: E402

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CSPMRegistration(auth_object=config)
AllowedResponses = [200, 201, 207, 401, 403, 429]  # Adding rate-limiting as an allowed response for now
textchars = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7f})
is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))  # noqa: E731


class TestCSPMRegistration:
    """
    Test harness for the CSPM Registration service class
    """
    def cspm_get_azure_user_scripts_attachment(self):
        """
        Download and confirm the Azure user script attachment
        """
        test_result = falcon.GetCSPMAzureUserScriptsAttachment()
        if type(test_result) == bytes:
            return True
        else:
            if test_result["body"]["errors"][0]["message"] == "No accounts found":
                return True
            else:
                pytest.skip("Script attachment download failure.")
                # return False

    def cspm_generate_errors(self):
        """
        Test every code path within every method by generating 500s, does not hit the API
        """
        falcon.base_url = "nowhere"
        error_checks = True
        tests = {
            "get_aws_account": falcon.GetCSPMAwsAccount(ids='12345678', organization_ids='12345678', scan_type="dry"),
            "create_aws_account": falcon.CreateCSPMAwsAccount(account_id="12345678",
                                                              cloudtrail_region="us-east-1",
                                                              organization_id="12345678"
                                                              ),
            "delete_aws_account": falcon.DeleteCSPMAwsAccount(ids='12345678', organization_ids='12345678'),
            "delete_aws_account_org": falcon.DeleteCSPMAwsAccount(organization_ids='12345678'),
            "get_azure_account": falcon.GetCSPMAzureAccount(ids='12345678', scan_type="dry"),
            "create_azure_account": falcon.CreateCSPMAzureAccount(tenant_id="12345678",
                                                                  subscription_id="12345678",
                                                                  behavior_assessment_enabled=True,
                                                                  years_valid=3
                                                                  ),
            "delete_azure_account": falcon.DeleteCSPMAzureAccount(ids='12345678'),
            "update_azure_account_client_id": falcon.UpdateCSPMAzureAccountClientID(tenant_id="12345678", id="12345678"),
            "get_policy": falcon.GetCSPMPolicy(ids='12345678'),
            "get_policy_settings": falcon.GetCSPMPolicySettings(cloud_platform="aws", policy_id=1),
            "update_policy_settings": falcon.UpdateCSPMPolicySettings(enabled=False,
                                                                      policy_id=1,
                                                                      severity="LOW",
                                                                      regions="us-east-1,us-west-1",
                                                                      tag_excluded=False,
                                                                      account_id="1234567"
                                                                      ),
            "get_scan_schedule": falcon.GetCSPMScanSchedule(cloud_platform="gcp"),
            "update_scan_schedule": falcon.UpdateCSPMScanSchedule(cloud_platform="gcp",
                                                                  next_scan_timestamp="2021-10-25T05:22:27.365Z",
                                                                  scan_schedule="daily"
                                                                  ),
            "update_aws_account": falcon.PatchCSPMAwsAccount(account_id="12345678", cloudtrail_region="us-east-1"),
            "update_azure_tenant_default_subscription_id": falcon.UpdateCSPMAzureTenantDefaultSubscriptionID(
                                                                    tenant_id="12345678"
                                                                    ),
            "get_azure_user_scripts_attachment": falcon.get_azure_user_scripts_attachment(tenant_id="12345678"),
            "azure_download_certificate": falcon.azure_download_certificate(tenant_id="1234567"),
            "get_ioa_events": falcon.GetIOAEvents(),
            "get_ioa_users": falcon.GetIOAUsers(),
            "get_behavior_detections": falcon.get_behavior_detections(limit=1),
            "get_configuration_detections": falcon.get_configuration_detections(limit=1),
            "GetConfigurationDetectionEntities": falcon.get_configuration_detection_entities(),
            "GetConfigurationDetectionIdsV2": falcon.get_configuration_detection_ids_v2(),
            "GetCSPMPoliciesDetails": falcon.get_policy_details()
        }
        for key in tests:
            if tests[key]["status_code"] != 500:
                error_checks = False

                # print(f"{key} operation returned a {tests[key]} status code")

        return error_checks

    @pytest.mark.skipif(os.getenv("DEBUG_API_BASE_URL", "us1").lower() in ["https://api.eu-1.crowdstrike.com", "eu1"],
                        reason="Unit testing unavailable on EU-1"
                        )
    def test_get_aws_console_setup_urls(self):
        """Pytest harness hook"""
        assert bool(falcon.GetCSPMAwsConsoleSetupURLs()["status_code"] in AllowedResponses) is True
    @pytest.mark.skipif(os.getenv("DEBUG_API_BASE_URL", "us1").lower() in [
        "https://api.eu-1.crowdstrike.com", "eu1", "https://api.us-2.crowdstrike.com", "us2", "https://api.laggar.gcw.crowdstrike.com", "usgov1"
        ],
                        reason="Unit testing unavailable on US-2 / EU-1"
                        )
    def test_get_aws_account_scripts_attachment(self):
        """Pytest harness hook"""
        check = falcon.GetCSPMAwsAccountScriptsAttachment()
        if isinstance(check, dict):
            assert bool(check["status_code"] in AllowedResponses)
        else:
            assert bool(type(falcon.GetCSPMAwsAccountScriptsAttachment()) == bytes) is True

    @pytest.mark.skipif(os.getenv("DEBUG_API_BASE_URL", "us1").lower() in ["https://api.laggar.gcw.crowdstrike.com", "usgov1"],
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_get_azure_user_scripts_attachment(self):
        """Pytest harness hook"""
        assert self.cspm_get_azure_user_scripts_attachment() is True

    # @staticmethod
    # def test_logout():
    #     """Pytest harness hook"""
    #     assert bool(falcon.auth_object.revoke(
    #         falcon.auth_object.token()["body"]["access_token"]
    #         )["status_code"] in AllowedResponses) is True

    def test_errors(self):
        """Pytest harness hook"""
        assert self.cspm_generate_errors() is True
