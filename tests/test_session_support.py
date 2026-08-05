# test_session_support.py
# Tests optional requests.Session support for connection reuse.
#
# These tests are fully mocked (no live credentials, no network access to the
# real CrowdStrike API) and mirror the monkeypatch style already used in
# tests/test_uber_api_complete.py and tests/test_authentications.py.
import gc
import os
import sys
import concurrent.futures
from unittest.mock import MagicMock
import pytest
import requests
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# flake8: noqa=E402
from falconpy import OAuth2, APIHarness, APIHarnessV2, Hosts, APIError, Result
from falconpy._auth_object._interface_config import InterfaceConfiguration
from falconpy._util import perform_request
import falconpy._util._functions as _funcs


class _FakeResponse:
    """Minimal stand-in for requests.Response used by monkeypatch tests."""

    def __init__(self, status_code=200, body=None, headers=None, content=None):
        self.status_code = status_code
        self.headers = headers or {"Content-Type": "application/json"}
        self._body = body if body is not None else {"meta": {"trace_id": "abc"}, "resources": [], "errors": []}
        self.content = content or b'{"resources":[]}'

    def json(self):
        return self._body


def _login_response(token="fake_token_123", expires=1799, status=201):
    body = {"access_token": token, "expires_in": expires} if status == 201 else {"errors": [{"message": "Denied"}]}
    return _FakeResponse(status, body)


def _api_response(status=200, body=None):
    return _FakeResponse(status, body)


def _revoke_response(status=200):
    return _FakeResponse(status, {})


def _spy_session(responses):
    """Build a real requests.Session whose .request/.close are mocked for inspection."""
    session = requests.Session()
    session.request = MagicMock(side_effect=lambda *a, **kw: next(responses))
    session.close = MagicMock()
    return session, session.request


class TestSessionDefaultBehaviorUnchanged:
    """Prove that omitting session= leaves existing behavior untouched."""

    def test_no_session_uses_module_level_requests_request(self, monkeypatch):
        """Login without a session must still call the module-level requests.request."""
        responses = iter([_login_response()])
        mock_request = MagicMock(side_effect=lambda *a, **kw: next(responses))
        monkeypatch.setattr(_funcs.requests, "request", mock_request)
        session_class_mock = MagicMock(side_effect=AssertionError("Session should never be instantiated"))
        monkeypatch.setattr(_funcs.requests, "Session", session_class_mock)

        oauth = OAuth2(client_id="fake_id", client_secret="fake_secret")
        result = oauth.login()

        mock_request.assert_called_once()
        session_class_mock.assert_not_called()
        assert result["status_code"] == 201

    def test_no_session_hosts_service_class_unchanged(self, monkeypatch):
        """A Service Class without a session must still call the module-level requests.request."""
        responses = iter([_login_response(), _api_response()])
        mock_request = MagicMock(side_effect=lambda *a, **kw: next(responses))
        monkeypatch.setattr(_funcs.requests, "request", mock_request)

        hosts = Hosts(client_id="fake_id", client_secret="fake_secret")
        result = hosts.query_devices_by_filter(limit=1)

        assert mock_request.call_count == 2
        assert result["status_code"] == 200
        assert result["body"] == {"meta": {"trace_id": "abc"}, "resources": [], "errors": []}


class TestSessionUsedThroughoutLifecycle:
    """Prove a provided session is used for login, calls, renewal and logout."""

    def test_session_used_for_login_and_renewal_and_logout(self, monkeypatch):
        """The same session instance must service login, a renewal, and logout."""
        responses = iter([_login_response(), _login_response(token="renewed_token"), _revoke_response()])
        session, request_mock = _spy_session(responses)
        monkeypatch.setattr(_funcs.requests, "request", MagicMock(side_effect=AssertionError("must use session")))

        oauth = OAuth2(client_id="fake_id", client_secret="fake_secret", session=session)
        assert oauth.login()["status_code"] == 201
        assert oauth.token()["status_code"] == 201
        oauth.logout()

        assert request_mock.call_count == 3
        assert oauth.session is session
        session.close.assert_not_called()

    def test_close_never_called_including_after_object_teardown(self, monkeypatch):
        """FalconPy must never close a caller-provided session, even after teardown."""
        responses = iter([_login_response(), _revoke_response()])
        session, request_mock = _spy_session(responses)
        monkeypatch.setattr(_funcs.requests, "request", MagicMock(side_effect=AssertionError("must use session")))

        oauth = OAuth2(client_id="fake_id", client_secret="fake_secret", session=session)
        oauth.login()
        oauth.logout()
        del oauth
        gc.collect()

        session.close.assert_not_called()

    def test_apiharnessv2_session_identity_across_multiple_calls(self, monkeypatch):
        """APIHarnessV2 must reuse the same session for login and every command."""
        responses = iter([_login_response(), _api_response(), _api_response()])
        session, request_mock = _spy_session(responses)
        monkeypatch.setattr(_funcs.requests, "request", MagicMock(side_effect=AssertionError("must use session")))

        falcon = APIHarnessV2(client_id="fake_id", client_secret="fake_secret", session=session)
        falcon.command("QueryDevicesByFilter", parameters={"limit": 1})
        falcon.command("QueryDevicesByFilter", parameters={"limit": 1})

        assert falcon.session is session
        assert request_mock.call_count == 3

    def test_legacy_apiharness_session_param(self, monkeypatch):
        """The legacy standalone APIHarness must also thread the session through."""
        responses = iter([_login_response(), _api_response()])
        session, request_mock = _spy_session(responses)
        monkeypatch.setattr(_funcs.requests, "request", MagicMock(side_effect=AssertionError("must use session")))

        uber = APIHarness(client_id="fake_id", client_secret="fake_secret", session=session)
        uber.authenticate()
        result = uber.command(action="QueryDevicesByFilter", parameters={"limit": 1})

        assert isinstance(result, dict)
        assert uber.session is session
        assert request_mock.call_count == 2

    def test_hosts_service_class_session_param(self, monkeypatch):
        """A generated Service Class constructed directly from credentials must use the session."""
        responses = iter([_login_response(), _api_response()])
        session, request_mock = _spy_session(responses)
        monkeypatch.setattr(_funcs.requests, "request", MagicMock(side_effect=AssertionError("must use session")))

        hosts = Hosts(client_id="fake_id", client_secret="fake_secret", session=session)
        result = hosts.query_devices_by_filter(limit=1)

        assert result["status_code"] == 200
        assert hosts.auth_object.session is session
        assert request_mock.call_count == 2

    def test_service_class_override_route_uses_session(self, monkeypatch):
        """ServiceClass.override() (custom/override routes) must also use the session."""
        responses = iter([_login_response(), _api_response()])
        session, request_mock = _spy_session(responses)
        monkeypatch.setattr(_funcs.requests, "request", MagicMock(side_effect=AssertionError("must use session")))

        hosts = Hosts(client_id="fake_id", client_secret="fake_secret", session=session)
        result = hosts.override("GET", "/devices/queries/devices-scroll/v1", parameters={"limit": 1})

        assert result["status_code"] == 200
        assert request_mock.call_count == 2


class TestSharedAuthObjectSessionPropagation:
    """Prove a shared auth_object keeps carrying the same session for every consumer."""

    def test_shared_oauth2_session_used_by_service_class(self, monkeypatch):
        """A Service Class constructed via auth_object= must inherit that object's session."""
        responses = iter([_login_response(), _api_response()])
        session, request_mock = _spy_session(responses)
        monkeypatch.setattr(_funcs.requests, "request", MagicMock(side_effect=AssertionError("must use session")))

        auth = OAuth2(client_id="fake_id", client_secret="fake_secret", session=session)
        hosts = Hosts(auth_object=auth)
        result = hosts.query_devices_by_filter(limit=1)

        assert hosts.auth_object is auth
        assert hosts.auth_object.session is session
        assert result["status_code"] == 200

    def test_shared_auth_object_across_two_service_classes_same_session(self, monkeypatch):
        """Two Service Classes sharing one auth_object must share the same session and login once."""
        responses = iter([_login_response(), _api_response(), _api_response()])
        session, request_mock = _spy_session(responses)
        monkeypatch.setattr(_funcs.requests, "request", MagicMock(side_effect=AssertionError("must use session")))

        auth = OAuth2(client_id="fake_id", client_secret="fake_secret", session=session)
        hosts_a = Hosts(auth_object=auth)
        hosts_b = Hosts(auth_object=auth)
        hosts_a.query_devices_by_filter(limit=1)
        hosts_b.query_devices_by_filter(limit=1)

        # One login total (token reused), plus one API call per Service Class.
        assert request_mock.call_count == 3
        assert hosts_a.auth_object is hosts_b.auth_object is auth
        assert hosts_a.session is hosts_b.session is session


def _capture_call(monkeypatch, use_session, **perform_kwargs):
    """Invoke perform_request either with a session or via the module-level requests.request."""
    fake_resp = _api_response(status=perform_kwargs.pop("_status", 200), body=perform_kwargs.pop("_body", None))
    mock_callable = MagicMock(return_value=fake_resp)
    if use_session:
        session = requests.Session()
        session.request = mock_callable
        perform_kwargs["session"] = session
    else:
        monkeypatch.setattr(_funcs.requests, "request", mock_callable)
    result = perform_request(**perform_kwargs)
    return mock_callable.call_args, result


def _base_kwargs():
    return dict(endpoint="https://api.crowdstrike.com/test", method="GET",
                params={"limit": 1}, headers={"X-Test": "1"}, proxy={"https": "http://x:1"},
                timeout=30, verify=False)


class TestRequestArgumentParity:
    """Prove request arguments and response handling are identical with/without a session."""

    def test_params_body_headers_proxy_timeout_verify_are_identical(self, monkeypatch):
        """The outgoing call and returned result must match whether or not a session is used."""
        call_no_session, result_no_session = _capture_call(monkeypatch, False, **_base_kwargs())
        call_with_session, result_with_session = _capture_call(monkeypatch, True, **_base_kwargs())

        assert call_no_session.args == call_with_session.args
        assert call_no_session.kwargs == call_with_session.kwargs
        assert result_no_session == result_with_session

    def test_response_parsing_identical_for_success_and_error_bodies(self, monkeypatch):
        """Both success and error response bodies must parse identically with/without a session."""
        for status, body in [(200, {"resources": ["a"], "errors": []}),
                             (403, {"resources": [], "errors": [{"message": "Access denied"}]})]:
            kwargs = _base_kwargs()
            kwargs["_status"] = status
            kwargs["_body"] = body
            _, result_no_session = _capture_call(monkeypatch, False, **dict(kwargs))
            _, result_with_session = _capture_call(monkeypatch, True, **dict(kwargs))
            assert result_no_session == result_with_session

    def test_stream_true_passthrough_identical(self, monkeypatch):
        """The stream=True early-return branch must behave the same with/without a session."""
        kwargs = _base_kwargs()
        kwargs["stream"] = True
        _, result_no_session = _capture_call(monkeypatch, False, **dict(kwargs))
        _, result_with_session = _capture_call(monkeypatch, True, **dict(kwargs))
        assert isinstance(result_no_session, _FakeResponse)
        assert isinstance(result_with_session, _FakeResponse)
        assert result_no_session.status_code == result_with_session.status_code

    def test_files_upload_kwarg_identical(self, monkeypatch):
        """The files= multipart upload kwarg must be forwarded identically with/without a session."""
        kwargs = _base_kwargs()
        kwargs["method"] = "POST"
        kwargs["files"] = [("file", ("test.txt", b"data", "text/plain"))]
        call_no_session, _ = _capture_call(monkeypatch, False, **dict(kwargs))
        call_with_session, _ = _capture_call(monkeypatch, True, **dict(kwargs))
        assert call_no_session.kwargs["files"] == call_with_session.kwargs["files"]


class TestPythonicModeWithSession:
    """Prove both pythonic and non-pythonic response modes still work with a session."""

    def test_pythonic_true_with_session_success(self, monkeypatch):
        """A successful call with a session and pythonic=True must return a Result."""
        responses = iter([_login_response(), _api_response(status=200)])
        session, _ = _spy_session(responses)
        monkeypatch.setattr(_funcs.requests, "request", MagicMock(side_effect=AssertionError("must use session")))

        hosts = Hosts(client_id="fake_id", client_secret="fake_secret", session=session, pythonic=True)
        result = hosts.query_devices_by_filter(limit=1)

        assert isinstance(result, Result)

    def test_pythonic_true_with_session_raises_apierror_on_failure(self, monkeypatch):
        """A failing call with a session and pythonic=True must raise APIError."""
        responses = iter([
            _login_response(),
            _api_response(status=403, body={"resources": [], "errors": [{"message": "Access denied"}]})
        ])
        session, _ = _spy_session(responses)
        monkeypatch.setattr(_funcs.requests, "request", MagicMock(side_effect=AssertionError("must use session")))

        hosts = Hosts(client_id="fake_id", client_secret="fake_secret", session=session, pythonic=True)
        with pytest.raises(APIError):
            hosts.query_devices_by_filter(limit=1)

    def test_pythonic_false_with_session_returns_plain_dict(self, monkeypatch):
        """Default (non-pythonic) mode with a session must still return a plain dict."""
        responses = iter([_login_response(), _api_response(status=200)])
        session, _ = _spy_session(responses)
        monkeypatch.setattr(_funcs.requests, "request", MagicMock(side_effect=AssertionError("must use session")))

        hosts = Hosts(client_id="fake_id", client_secret="fake_secret", session=session)
        result = hosts.query_devices_by_filter(limit=1)

        assert isinstance(result, dict) and not isinstance(result, Result)
        assert set(["status_code", "headers", "body"]).issubset(result.keys())


class TestSessionConcurrencySmoke:
    """Smoke test only: FalconPy itself must not crash under shared concurrent use.

    This does NOT prove raw socket-level thread-safety of requests.Session, which is a
    property of requests/urllib3, not something FalconPy can guarantee.
    """

    def test_shared_session_survives_concurrent_calls(self, monkeypatch):
        """A session shared across threads via one auth_object must not raise or corrupt state."""
        session = requests.Session()
        session.request = MagicMock(side_effect=lambda *a, **kw: _login_response() if "/oauth2/token" in a[1]
                                     else _api_response())
        monkeypatch.setattr(_funcs.requests, "request", MagicMock(side_effect=AssertionError("must use session")))

        auth = OAuth2(client_id="fake_id", client_secret="fake_secret", session=session)
        auth.login()
        session.request.reset_mock()

        hosts = Hosts(auth_object=auth)
        num_calls = 10
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
            futures = [pool.submit(hosts.query_devices_by_filter, limit=1) for _ in range(num_calls)]
            results = [f.result() for f in futures]

        assert all(r["status_code"] == 200 for r in results)
        assert session.request.call_count == num_calls


class TestSessionPropertyMutators:
    """Cover the session property setters on the auth object and its configuration."""

    def test_interface_configuration_session_setter(self):
        """InterfaceConfiguration.session must store the assigned session."""
        config = InterfaceConfiguration(base_url="https://api.crowdstrike.com")
        assert config.session is None
        session = requests.Session()
        config.session = session
        assert config.session is session

    def test_falcon_interface_session_setter_propagates_to_config(self):
        """Assigning to FalconInterface.session must reach the underlying configuration."""
        session = requests.Session()
        auth = OAuth2(client_id="fake_id", client_secret="fake_secret")
        assert auth.session is None

        auth.session = session
        assert auth.session is session
        assert auth.config.session is session

    def test_falcon_interface_session_can_be_cleared(self):
        """Clearing the session must restore the default (no session) behavior."""
        auth = OAuth2(client_id="fake_id", client_secret="fake_secret", session=requests.Session())
        assert auth.session is not None
        auth.session = None
        assert auth.session is None
        assert auth.config.session is None
