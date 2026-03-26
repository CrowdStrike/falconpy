"""test_network_scan_scanners.py - Tests for NetworkScanScanners service class."""
import os
import sys
import pytest
from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import NetworkScanScanners

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = NetworkScanScanners(auth_object=config)
AllowedResponses = [200, 201, 400, 403, 404, 429]


class TestNetworkScanScanners:
    """NetworkScanScanners Service Class test harness."""

    def run_all_tests(self):
        """Execute all tests and return results."""
        error_checks = True
        tests = {
            "AggregateScanners": falcon.aggregate_scanners(
                date_ranges=[{}],
                exclude="string",
                field="string",
                filter="string",
                from_=1,
                include="string",
                interval="string",
                missing="string",
                min_doc_count=1,
                name="string",
                q="string",
                ranges=[{}],
                size=1,
                sort="string",
                sub_aggregates=[{}],
                time_zone="string",
                type="string"
            ),
            "GetScanners": falcon.get_scanners("string"),
            "UpdateScanners": falcon.update_scanners(
                action="string",
                aids=["string"]
            ),
            "QueryScanners": falcon.query_scanners(limit=1),
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
