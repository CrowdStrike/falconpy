"""test_network_scan_networks.py - Tests for NetworkScanNetworks service class."""
import os
import sys
import pytest
from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import NetworkScanNetworks

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = NetworkScanNetworks(auth_object=config)
AllowedResponses = [200, 201, 400, 403, 404, 429]


class TestNetworkScanNetworks:
    """NetworkScanNetworks Service Class test harness."""

    def run_all_tests(self):
        """Execute all tests and return results."""
        error_checks = True
        tests = {
            "AggregateNetworks": falcon.aggregate_networks(
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
            "GetNetworks": falcon.get_networks("string"),
            "CreateNetworks": falcon.create_networks(
                name="string",
                scanner_aids=["string"],
                scanner_assignment_type="string",
                subnet="string",
                zone_id="string"
            ),
            "UpdateNetworks": falcon.update_networks(
                id="string",
                name="string",
                ownership="string",
                scanner_aids=["string"],
                scanner_assignment_type="string",
                zone_id="string"
            ),
            "DeleteNetworks": falcon.delete_networks("string"),
            "QueryNetworks": falcon.query_networks(limit=1),
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
