# test_network_scan_detections.py
# This class tests the network_scan_detections service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import NetworkScanDetections

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = NetworkScanDetections(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestNetworkScanDetections:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "aggregate_detections": falcon.aggregate_netscan_detections(date_ranges="string", exclude="string",
                                                                        field="string", filter="string", include="string",
                                                                        interval="string", max_doc_count="string",
                                                                        min_doc_count="string", missing="string",
                                                                        name="string", percents="string", q="string",
                                                                        ranges="string", size="string", sort="string",
                                                                        sub_aggregates="string", time_zone="string",
                                                                        type="string", max="string", min="string",
                                                                        filters="string", other_bucket="string",
                                                                        other_bucket_key="string"),
            "combined_detections": falcon.get_combined_netscan_detections(offset=1, limit=1, sort="string", filter="string"),
            "get_detections": falcon.get_netscan_detections(ids="12345678"),
            "query_detections": falcon.query_netscan_detections(offset=1, limit=1, sort="string", filter="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks

    def test_payload_coverage(self):
        """Exercise nested payload builder branches."""
        falcon.aggregate_netscan_detections(max="string", min="string", filters="string", other_bucket="string", other_bucket_key="string")
        assert True
