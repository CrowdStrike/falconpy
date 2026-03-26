"""test_network_scan_scan_runs.py - Tests for NetworkScanScanRuns service class."""
import os
import sys
import pytest
from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import NetworkScanScanRuns

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = NetworkScanScanRuns(auth_object=config)
AllowedResponses = [200, 201, 400, 403, 404, 429]


class TestNetworkScanScanRuns:
    """NetworkScanScanRuns Service Class test harness."""

    def run_all_tests(self):
        """Execute all tests and return results."""
        error_checks = True
        tests = {
            "AggregateScanRuns": falcon.aggregate_scan_runs(
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
            "GetScanRuns": falcon.get_scan_runs(ids="string"),
            "CreateScanRuns": falcon.create_scan_runs(config={}, scan_id="string"),
            "UpdateScanRuns": falcon.update_scan_runs(action="stop", id="string"),
            "QueryScanRuns": falcon.query_scan_runs(
                offset=1,
                limit=1,
                sort="string",
                filter="string"
            ),
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
