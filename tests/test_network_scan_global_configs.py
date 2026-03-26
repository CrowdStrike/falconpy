"""test_network_scan_global_configs.py - Tests for NetworkScanGlobalConfigs service class."""
import os
import sys
import pytest
from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import NetworkScanGlobalConfigs

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = NetworkScanGlobalConfigs(auth_object=config)
AllowedResponses = [200, 201, 400, 403, 404, 429]


class TestNetworkScanGlobalConfigs:
    """NetworkScanGlobalConfigs Service Class test harness."""

    def run_all_tests(self):
        """Execute all tests and return results."""
        error_checks = True
        tests = {
            "GetGlobalConfigs": falcon.get_global_configs(),
            "UpdateGlobalConfigs": falcon.update_global_configs(
                auto_confirm_ownership={},
                max_concurrent_tasks=1,
                network_scanning_enabled=True,
                scan_exclusion={},
                scanners=[{}],
                scanners_exclusion=[{}]
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
