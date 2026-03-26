"""test_network_scan_templates.py - Tests for NetworkScanTemplates service class."""
import os
import sys
import pytest
from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import NetworkScanTemplates

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = NetworkScanTemplates(auth_object=config)
AllowedResponses = [200, 201, 400, 403, 404, 429]


class TestNetworkScanTemplates:
    """NetworkScanTemplates Service Class test harness."""

    def run_all_tests(self):
        """Execute all tests and return results."""
        error_checks = True
        tests = {
            "GetTemplateConfigs": falcon.get_template_configs(),
            "GetTemplates": falcon.get_templates("string"),
            "CreateTemplates": falcon.create_templates(
                active_check_level="string",
                additional_tcp_ports=["string"],
                additional_udp_ports=["string"],
                auto_include_new_detections=True,
                detections=["string"],
                ignore_tcp_resets=True,
                name="string",
                ports_scan_level="string",
                scan_intensity="string",
                type="string"
            ),
            "UpdateTemplates": falcon.update_templates(
                active_check_level="string",
                additional_tcp_ports=["string"],
                additional_udp_ports=["string"],
                auto_include_new_detections=True,
                detections=["string"],
                id="string",
                ignore_tcp_resets=True,
                name="string",
                ports_scan_level="string",
                scan_intensity="string"
            ),
            "DeleteTemplates": falcon.delete_templates("string"),
            "QueryTemplates": falcon.query_templates(limit=1),
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
