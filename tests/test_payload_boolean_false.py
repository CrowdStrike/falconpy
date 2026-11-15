# test_payload_boolean_false.py
# Tests that boolean keywords passed as False are kept in request payloads [Issue 1530].
#
# These tests are fully mocked (no live credentials, no network access to the
# real CrowdStrike API) and follow the monkeypatch style used in
# tests/test_ssl_verify.py.
import os
import sys
from unittest.mock import MagicMock
import pytest
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# flake8: noqa=E402
from falconpy import FirewallManagement, IdentityProtection, SensorUpdatePolicy
from falconpy._payload import (
    network_locations_create_payload,
    idp_policy_payload,
    sensor_policy_payload
    )
import falconpy._util._functions as _funcs


class _FakeResponse:
    """Minimal stand-in for requests.Response."""

    status_code = 200
    headers = {"Content-Type": "application/json"}
    content = b'{"resources":[]}'

    def json(self):
        return {"meta": {}, "resources": [], "errors": []}


def _mock_requests(monkeypatch):
    """Replace requests.request so nothing is sent, and return the mock."""
    mock_request = MagicMock(return_value=_FakeResponse())
    monkeypatch.setattr(_funcs.requests, "request", mock_request)
    return mock_request


def _sent_body(mock_request):
    return mock_request.call_args.kwargs["json"]


class TestNetworkLocationsPayload:

    @pytest.mark.parametrize("value", [True, False])
    def test_enabled_is_kept(self, value):
        payload = network_locations_create_payload({"name": "HQ", "enabled": value})
        assert payload == {"name": "HQ", "enabled": value}

    def test_enabled_omitted_when_not_passed(self):
        assert "enabled" not in network_locations_create_payload({"name": "HQ"})

    def test_enabled_omitted_when_none(self):
        assert "enabled" not in network_locations_create_payload({"name": "HQ", "enabled": None})

    def test_falsy_non_boolean_keys_still_omitted(self):
        payload = network_locations_create_payload({"name": "", "description": None, "enabled": False})
        assert payload == {"enabled": False}

    @pytest.mark.parametrize("method", [
        "create_network_locations", "upsert_network_locations", "update_network_locations"
    ])
    def test_service_methods_send_false(self, monkeypatch, method):
        mock_request = _mock_requests(monkeypatch)
        falcon = FirewallManagement(access_token="not-a-real-token")
        getattr(falcon, method)(id="loc-1", name="HQ", enabled=False)
        assert _sent_body(mock_request)["enabled"] is False


class TestIdentityProtectionPolicyPayload:

    @pytest.mark.parametrize("value", [True, False])
    def test_enabled_and_simulation_mode_kept(self, value):
        payload = idp_policy_payload({"name": "r", "enabled": value, "simulation_mode": value})
        assert payload == {"name": "r", "enabled": value, "simulationMode": value}

    def test_camel_case_simulation_mode_false_kept(self):
        payload = idp_policy_payload({"simulationMode": False})
        assert payload == {"simulationMode": False}

    def test_booleans_omitted_when_not_passed(self):
        assert idp_policy_payload({"name": "r"}) == {"name": "r"}

    def test_booleans_omitted_when_none(self):
        payload = idp_policy_payload({"name": "r", "enabled": None, "simulation_mode": None})
        assert payload == {"name": "r"}

    def test_create_policy_rule_sends_false(self, monkeypatch):
        mock_request = _mock_requests(monkeypatch)
        falcon = IdentityProtection(access_token="not-a-real-token")
        falcon.create_policy_rule(name="r", action="ALLOW", trigger="access",
                                  enabled=False, simulation_mode=False)
        body = _sent_body(mock_request)
        assert body["enabled"] is False
        assert body["simulationMode"] is False


class TestSensorUpdatePolicyPayload:

    @pytest.mark.parametrize("value", [True, False])
    def test_show_early_adopter_builds_kept(self, value):
        payload = sensor_policy_payload({"id": "pol-1", "show_early_adopter_builds": value})
        assert payload == {"resources": [{"id": "pol-1", "settings": {"show_early_adopter_builds": value}}]}

    def test_no_settings_when_not_passed(self):
        assert sensor_policy_payload({"id": "pol-1"}) == {"resources": [{"id": "pol-1"}]}

    def test_no_settings_when_none(self):
        payload = sensor_policy_payload({"id": "pol-1", "show_early_adopter_builds": None})
        assert payload == {"resources": [{"id": "pol-1"}]}

    @pytest.mark.parametrize("method", [
        "create_policies_v2", "update_policies_v2", "create_policies", "update_policies"
    ])
    def test_service_methods_send_false(self, monkeypatch, method):
        mock_request = _mock_requests(monkeypatch)
        falcon = SensorUpdatePolicy(access_token="not-a-real-token")
        getattr(falcon, method)(id="pol-1", show_early_adopter_builds=False)
        settings = _sent_body(mock_request)["resources"][0]["settings"]
        assert settings["show_early_adopter_builds"] is False
