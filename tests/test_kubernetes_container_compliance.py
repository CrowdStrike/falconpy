# test_kubernetes_container_compliance.py
# This class tests the kubernetes_container_compliance service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import KubernetesContainerCompliance

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = KubernetesContainerCompliance(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestKubernetesContainerCompliance:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "AggregateAssessmentsGroupedByClustersV2": falcon.aggregate_assessments_by_cluster(),
            "AggregateComplianceByAssetType": falcon.aggregate_compliance_by_asset_type(),
            "AggregateComplianceByClusterType": falcon.aggregate_compliance_by_cluster_type(),
            "AggregateComplianceByFramework": falcon.aggregate_compliance_by_framework(),
            "AggregateFailedRulesByClustersV3": falcon.aggregate_failed_rules_by_clusters(),
            "AggregateFailedRulesByClustersV3": falcon.aggregate_failed_rules_by_clusters(),
            "AggregateAssessmentsGroupedByRulesV2": falcon.aggregate_assessments_by_rules(),
            "AggregateTopFailedImages": falcon.aggregate_top_failed_images(),
            "CombinedImagesFindings": falcon.image_findings(),
            "CombinedNodesFindings": falcon.node_findings(),
            "getRulesMetadataByID": falcon.get_rules_metadata(ids="whatever")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
