"""test_network_scan_scans.py - Tests for NetworkScanScans service class."""
import os
import sys
import pytest
from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import NetworkScanScans

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = NetworkScanScans(auth_object=config)
AllowedResponses = [200, 201, 400, 403, 404, 429]


class TestNetworkScanScans:
    """NetworkScanScans Service Class test harness."""

    def run_all_tests(self):
        """Execute all tests and return results."""
        error_checks = True
        tests = {
            "AggregateScansMixin0": falcon.aggregate_scans(
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
            "GetScans": falcon.get_scans("string"),
            "CreateScans": falcon.create_scans(
                block_windows={},
                credentialed=True,
                credentials={},
                description="string",
                fragile_device_detection=True,
                name="string",
                scheduling={},
                target_asset={},
                target_asset_filter={},
                target_external_ip={},
                target_ip={},
                target_type="string",
                template_id="string"
            ),
            "UpdateScans": falcon.update_scans(
                block_windows={},
                credentialed=True,
                credentials={},
                description="string",
                fragile_device_detection=True,
                id="string",
                name="string",
                scheduling={},
                target_asset={},
                target_asset_filter={},
                target_external_ip={},
                target_ip={},
                target_type="string",
                template_id="string"
            ),
            "DeleteScans": falcon.delete_scans("string"),
            "QueryScansMixin0": falcon.query_scans(limit=1),
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
