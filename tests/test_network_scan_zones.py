"""test_network_scan_zones.py - Tests for NetworkScanZones service class."""
import os
import sys
import pytest
from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import NetworkScanZones

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = NetworkScanZones(auth_object=config)
AllowedResponses = [200, 201, 400, 403, 404, 429]


class TestNetworkScanZones:
    """NetworkScanZones Service Class test harness."""

    def run_all_tests(self):
        """Execute all tests and return results."""
        error_checks = True
        tests = {
            "AggregateZones": falcon.aggregate_zones(
                date_ranges=[{}],
                exclude="string",
                field="string",
                filter="string",
                interval="string",
                max_doc_count=1,
                min_doc_count=1,
                missing="string",
                name="string",
                q="string",
                ranges=[{}],
                size=1,
                sort="string",
                sub_aggregates=[{}],
                time_zone="string",
                type="string"
            ),
            "CombinedZones": falcon.combined_zones(
                offset=1,
                limit=1,
                sort="string",
                filter="string"
            ),
            "GetZones": falcon.get_zones("string"),
            "CreateZones": falcon.create_zones(
                name="string",
                scanners=["string"]
            ),
            "UpdateZones": falcon.update_zones(
                id="string",
                name="string",
                scanners_to_add=["string"],
                scanners_to_remove=["string"]
            ),
            "DeleteZones": falcon.delete_zones("string"),
            "QueryZones": falcon.query_zones(limit=1),
        }

        for test_name, test_result in tests.items():
            if test_result["status_code"] == 429:
                pytest.skip("Rate limit hit")
            if test_result["status_code"] not in AllowedResponses:
                error_checks = False
                print(f"{test_name} failed: {test_result}")

        return error_checks

    def test_all(self):
        """Pytest harness hook."""
        assert self.run_all_tests() is True
