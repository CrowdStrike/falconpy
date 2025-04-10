# test_container_image_compliance.py
# This class tests the ContainerImageCompliance service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Classes to test - manually imported from sibling folder
from falconpy import ContainerImageCompliance
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ContainerImageCompliance(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 404, 429, 500]


class TestContainerImageCompliance:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "aggregate_cluster_assessments": falcon.aggregate_cluster_assessments(),
            "aggregate_image_assessments": falcon.aggregate_image_assessments(),
            "aggregate_rules_assessments": falcon.aggregate_rules_assessments(filter="compliance_finding.severity: '4'"),
            "aggregate_failed_containers_by_rules": falcon.aggregate_failed_containers_by_rules(),
            "aggregate_failed_containers_count_by_severity": falcon.aggregate_failed_containers_count_by_severity(),
            "aggregate_failed_images_by_rules": falcon.aggregate_failed_images_by_rules(),
            "aggregate_failed_images_count_by_severity": falcon.aggregate_failed_images_count_by_severity(),
            "aggregate_failed_rules_by_clusters": falcon.aggregate_failed_rules_by_clusters(),
            "aggregate_failed_rules_by_image": falcon.aggregate_failed_rules_by_image(),
            "aggregate_failed_rules_count_by_severity": falcon.aggregate_failed_rules_count_by_severity(),
            "aggregate_rules_by_status": falcon.aggregate_rules_by_status()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
            #   print(key)
            #   print(tests[key])
        assert error_checks
