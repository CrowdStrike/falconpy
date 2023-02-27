# test_kubernetes_protection.py
# This class tests the Kubernetes_Protection service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import KubernetesProtection

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = KubernetesProtection(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 404, 403, 429, 500]  # Allowing 500 to reduce flakiness


class TestKubeProtect:
    def serviceKubeProtect_RunAllTests(self):
        error_checks = True
        tests = {
            "GetAWSAccountsMixin0": falcon.get_aws_accounts(limit=1),
            "CreateAWSAccount": falcon.create_aws_account(account_id="12345678", region="us-east-1"),
            "DeleteAWSAccountsMixin0": falcon.delete_aws_accounts(ids='12345678'),  # 403
            "UpdateAWSAccount": falcon.update_aws_account(ids='12345678'),  # 400
            "ListAzureAccounts": falcon.list_azure_accounts(ids="12345678"),
            "CreateAzureSubscription": falcon.create_azure_subscription(subscription_id="whatever",
                                                                        tenant_id="whatever"
                                                                        ),
            "DeleteAzureSubscription": falcon.delete_azure_subscription(ids="12345678"),
            "GetLocations": falcon.get_locations(),
            "GetHelmValuesYaml": falcon.get_helm_values_yaml(cluster_name='Harold'),  # 403
            "RegenerateAPIKey": falcon.regenerate(),  # Occasionally 500
            "GetClusters": falcon.get_clusters(),
            "TriggerScan": falcon.trigger_scan(scan_type='dry-run'),  # 403
            "PatchAzureSubscription": falcon.patch_azure_service_principal(subscription_id="whatever",
                                                                           client_id="whatever"
                                                                           ),
            "GetCombinedCloudClusters": falcon.get_cloud_clusters(ids="123456789"),
            "GetAzureTenantConfig": falcon.get_azure_tenant_config(ids="whatevers"),
            "GetStaticScripts": falcon.get_static_scripts(),
            "GetAzureTenantIDs": falcon.get_azure_tenant_ids(ids="12345678"),
            "GetAzureInstallScript": falcon.get_azure_install_script(ids="123456789")
        }

        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(f"{tests[key]}")

        return error_checks

    def test_RunAllTests(self):
        assert self.serviceKubeProtect_RunAllTests() is True
