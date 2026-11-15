# test_query_string_keywords.py
# Tests that documented query string keywords reach the request URL [Issue 1529].
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
from falconpy import (
    AgentInvocation,
    Agents,
    CustomStorage,
    FalconXSandbox,
    FirewallManagement,
    Hosts,
    NGSIEM,
    RealTimeResponse
    )
import falconpy._util._functions as _funcs


class _FakeResponse:
    """Minimal stand-in for requests.Response."""

    status_code = 200
    headers = {"Content-Type": "application/json"}
    content = b'{"resources":[]}'

    def json(self):
        return {"meta": {}, "resources": [], "errors": []}


TOKEN = "not-a-real-token"

# (service class, method, keywords passed, query string expected, body keys expected)
CASES = [
    pytest.param(RealTimeResponse, "init_session",
                 {"device_id": "abc", "timeout": 120, "timeout_duration": "2m"},
                 {"timeout": 120, "timeout_duration": "2m"}, {"device_id": "abc"},
                 id="init_session"),
    pytest.param(Hosts, "query_device_login_history_v2",
                 {"ids": "abc", "limit": 50, "from": "now-7d", "to": "now-1d"},
                 {"limit": 50, "from": "now-7d", "to": "now-1d"}, {"ids": ["abc"]},
                 id="query_device_login_history_v2"),
    pytest.param(NGSIEM, "update_data_connection",
                 {"ids": "conn-1", "name": "renamed"},
                 {"ids": "conn-1"}, {"name": "renamed"},
                 id="update_data_connection"),
    pytest.param(FirewallManagement, "update_network_locations_metadata",
                 {"cid": "cid-1", "comment": "why"},
                 {"comment": "why"}, {"cid": "cid-1"},
                 id="update_network_locations_metadata"),
    pytest.param(FirewallManagement, "update_network_locations_precedence",
                 {"cid": "cid-1", "location_precedence": ["loc-1"], "comment": "why"},
                 {"comment": "why"}, {"cid": "cid-1"},
                 id="update_network_locations_precedence"),
    pytest.param(FirewallManagement, "upsert_network_locations",
                 {"id": "loc-1", "name": "HQ", "comment": "why"},
                 {"comment": "why"}, {"id": "loc-1", "name": "HQ"},
                 id="upsert_network_locations"),
    pytest.param(FalconXSandbox, "submit",
                 {"sha256": "a" * 64, "environment_id": 160, "aid": "aid-1"},
                 {"aid": "aid-1"}, {},
                 id="submit"),
    pytest.param(Agents, "create_or_update_agent",
                 {"id": "agent-1", "wait_for_ready": False},
                 {"wait_for_ready": False}, {"id": "agent-1"},
                 id="create_or_update_agent"),
    pytest.param(AgentInvocation, "update_agent_invocation",
                 {"id": "inv-1", "status": "cancelled", "project_id": "proj-1"},
                 {"project_id": "proj-1"}, {"id": "inv-1", "status": "cancelled"},
                 id="update_agent_invocation"),
]


def _as_sent(params):
    """perform_request sends booleans in the query string as lowercase strings."""
    return {k: str(v).lower() if isinstance(v, bool) else v for k, v in params.items()}


def _mock_requests(monkeypatch):
    """Replace requests.request so nothing is sent, and return the mock."""
    mock_request = MagicMock(return_value=_FakeResponse())
    monkeypatch.setattr(_funcs.requests, "request", mock_request)
    return mock_request


class TestQueryStringKeywords:

    @pytest.mark.parametrize("service, method, keywords, expected_params, expected_body", CASES)
    def test_keywords_reach_query_string(self, monkeypatch, service, method, keywords,
                                         expected_params, expected_body):
        mock_request = _mock_requests(monkeypatch)
        result = getattr(service(access_token=TOKEN), method)(**keywords)
        assert result["status_code"] == 200
        sent = mock_request.call_args.kwargs
        assert sent["params"] == _as_sent(expected_params)
        for key, value in expected_body.items():
            assert sent["json"][key] == value

    @pytest.mark.parametrize("service, method, keywords, expected_params, expected_body", CASES)
    def test_parameters_dictionary_is_honored(self, monkeypatch, service, method, keywords,
                                              expected_params, expected_body):
        mock_request = _mock_requests(monkeypatch)
        body_keywords = {k: v for k, v in keywords.items() if k not in expected_params}
        getattr(service(access_token=TOKEN), method)(parameters=dict(expected_params), **body_keywords)
        assert mock_request.call_args.kwargs["params"] == _as_sent(expected_params)

    def test_upload_version_dry_run(self, monkeypatch):
        mock_request = _mock_requests(monkeypatch)
        result = CustomStorage(access_token=TOKEN).upload_version(collection_name="c",
                                                                  collection_version="v1",
                                                                  object_key="k",
                                                                  body=b"data",
                                                                  dry_run=True
                                                                  )
        assert result["status_code"] == 200
        method, url = mock_request.call_args.args
        sent = mock_request.call_args.kwargs
        assert method == "PUT"
        assert url.endswith("/customobjects/v1/collections/c/v1/objects/k")
        assert sent["params"] == {"dry_run": "true"}
        assert sent["json"] == b"data"

    def test_upload_version_parameters_dictionary(self, monkeypatch):
        mock_request = _mock_requests(monkeypatch)
        CustomStorage(access_token=TOKEN).upload_version(collection_name="c",
                                                         collection_version="v1",
                                                         object_key="k",
                                                         body=b"data",
                                                         parameters={"dry_run": True}
                                                         )
        assert mock_request.call_args.kwargs["params"] == {"dry_run": "true"}

    def test_no_query_string_when_not_passed(self, monkeypatch):
        mock_request = _mock_requests(monkeypatch)
        RealTimeResponse(access_token=TOKEN).init_session(device_id="abc")
        assert not mock_request.call_args.kwargs["params"]
