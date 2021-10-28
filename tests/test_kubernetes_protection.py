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
token = auth.getConfigExtended()
falcon = KubernetesProtection(access_token=token)
AllowedResponses = [200, 207, 400, 403, 429, 500]  # Allowing 500 to reduce flakiness


class TestKubeProtect:
    def serviceKubeProtect_RunAllTests(self):
        error_checks = True
        tests = {
            "GetAWSAccountsMixin0": falcon.get_aws_accounts(limit=1),
            "CreateAWSAccount": falcon.create_aws_account(account_id="12345678", region="us-east-1"),
            "DeleteAWSAccountsMixin0": falcon.delete_aws_accounts(ids='12345678'),  # 403
            "UpdateAWSAccount": falcon.update_aws_account(ids='12345678'),  # 400
            "GetLocations": falcon.get_locations(),
            "GetHelmValuesYaml": falcon.get_helm_values_yaml(cluster_name='Harold'),  # 403
            "RegenerateAPIKey": falcon.regenerate(),  # Occasionally 500
            "GetClusters": falcon.get_clusters(),
            "TriggerScan": falcon.trigger_scan(scan_type='dry-run'),  # 403
        }

        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False

        return error_checks

    def test_RunAllTests(self):
        assert self.serviceKubeProtect_RunAllTests() is True
