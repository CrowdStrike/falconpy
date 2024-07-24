# test_container_detections.py
# This class tests the container detections service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ContainerDetections

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ContainerDetections(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestContainerDetections:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "ReadDetectionsCountBySeverity": falcon.read_detection_counts_by_severity("cid:'1234567890'"),
            "ReadDetectionsCountByType": falcon.read_detections_count_by_type(filter="cid:'1234567890'"),
            "ReadDetectionsCount": falcon.read_detections_count(filter="cid:'1234567890'"),
            "ReadCombinedDetections": falcon.read_combined_detections(filter="cid:'1234567890'", limit=1),
            "GetRuntimeDetectionsCombinedV2": falcon.search_runtime_detections(limit=1, filter="cid:'1234567'"),
            "ReadDetections": falcon.read_detections(limit=1, filter="cid:'1234567890'"),
            "SearchDetections": falcon.search_detections(filter="cid:'1234567890'", limit=1)
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
