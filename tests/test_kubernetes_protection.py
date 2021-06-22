# test_kubernetes_protection.py
# This class tests the Kubernetes_Protection service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.kubernetes_protection import Kubernetes_Protection as FalconKube

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconKube(access_token=auth.token)
AllowedResponses = [200, 207, 400, 403, 429]


class TestKubeProtect:
    def serviceKubeProtect_RunAllTests(self):
        errorChecks = True
        commandList = [
            ["GetAWSAccountsMixin0", "limit=1"],
            ["CreateAWSAccount", "body={}"],
            ["DeleteAWSAccountsMixin0", "ids='12345678'"],  # 403
            ["UpdateAWSAccount", "ids='12345678'"],  # 400
            ["GetLocations", ""],
            ["GetHelmValuesYaml", "cluster_name='Harold'"],  # 403
            ["RegenerateAPIKey", ""],
            ["GetClusters", ""],
            ["TriggerScan", "scan_type='dry-run'"],  # 403
        ]
        for cmd in commandList:
            result = eval("falcon.{}({})".format(cmd[0], cmd[1]))
            if result['status_code'] not in AllowedResponses:
                print(cmd[0])
                print(result)
                errorChecks = False

        return errorChecks

    def test_RunAllTests(self):
        assert self.serviceKubeProtect_RunAllTests() is True
