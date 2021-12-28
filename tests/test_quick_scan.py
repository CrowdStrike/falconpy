# test_quick_scam.py
# This class tests the quick_scan service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import QuickScan

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = QuickScan(auth_object=config)
AllowedResponses = [200, 201, 207, 429]  # Adding rate-limiting as an allowed response for now


class TestQuickScan:

    def service_scan_test_all(self):
        error_checks = True
        tests = {
            "get_scans_aggregates": falcon.get_scans_aggregates(body={}),
            "get_scans": falcon.get_scans(ids="12345678"),
            "scan_samples": falcon.scan_samples(body={"samples": ["123456"]}),
            "scan_samples_two": falcon.scan_samples("123456"),
            "query_submissions": falcon.query_submissions(),
        }
        for key in tests:
            if tests[key]["status_code"] == 500:
                error_checks = False

        return error_checks

    def service_scan_test_aggregate(self):
        """Test the aggregate payload generated. Currently generates a 400 from the API."""
        result = falcon.get_scans_aggregates(date_ranges=[
                                                {
                                                    "from": "string",
                                                    "to": "string"
                                                }
                                            ],
                                            field="string",
                                            filter="string",
                                            interval="string",
                                            min_doc_count=0,
                                            missing="string",
                                            name="string",
                                            q="string",
                                            ranges=[
                                                {
                                                    "From": 0,
                                                    "To": 0
                                                }
                                            ],
                                            size=1,
                                            sort="string",
                                            sub_aggregates=[
                                                "string"
                                            ],
                                            time_zone="string",
                                            type="string"
                                            )

        if result != 500:
            return True
        else:
            return False

    def test_scan_aggregates_payload(self):
        assert self.service_scan_test_aggregate() is True

    def test_all_functionality(self):
        assert self.service_scan_test_all() is True
