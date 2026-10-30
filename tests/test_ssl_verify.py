# test_ssl_verify.py
# Tests ssl_verify handling, including support for a CA_BUNDLE path.
#
# ssl_verify accepts a boolean, or the path to a CA_BUNDLE file or directory of
# trusted certificates (str or os.PathLike), mirroring the requests verify argument.
#
# These tests are fully mocked (no live credentials, no network access to the
# real CrowdStrike API) and follow the monkeypatch style used in
# tests/test_session_support.py.
import os
import sys
import pathlib
from unittest.mock import MagicMock
import pytest
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# flake8: noqa=E402
from falconpy import OAuth2, APIHarnessV2, Hosts
from falconpy._auth_object._interface_config import InterfaceConfiguration
import falconpy._util._functions as _funcs

# Never opened: requests.request is mocked in every test that performs a request.
CA_PATH = os.path.join("path", "to", "ca-bundle.pem")

# (value provided by the caller, value FalconPy must hand to requests)
NORMALIZATION_CASES = [
    pytest.param(True, True, id="true"),
    pytest.param(False, False, id="false"),
    pytest.param(CA_PATH, CA_PATH, id="str-path"),
    pytest.param(pathlib.Path(CA_PATH), CA_PATH, id="pathlike"),
    # requests treats "" as falsy and would silently disable verification.
    pytest.param("", True, id="empty-string-stays-secure"),
    pytest.param("   ", True, id="whitespace-stays-secure"),
    pytest.param(None, True, id="none"),
    pytest.param(0, True, id="int-zero-stays-secure"),
    pytest.param({}, True, id="unsupported-type"),
]


class _FakeResponse:
    """Minimal stand-in for requests.Response used by monkeypatch tests."""

    def __init__(self, status_code=200, body=None, headers=None):
        self.status_code = status_code
        self.headers = headers or {"Content-Type": "application/json"}
        self._body = body if body is not None else {"meta": {}, "resources": [], "errors": []}
        self.content = b'{"resources":[]}'

    def json(self):
        return self._body


def _login_response():
    return _FakeResponse(201, {"access_token": "fake_token_123", "expires_in": 1799})


def _mock_requests(monkeypatch, *responses):
    """Replace the module-level requests.request with a mock returning responses in order."""
    queue = iter(responses)
    mock_request = MagicMock(side_effect=lambda *a, **kw: next(queue))
    monkeypatch.setattr(_funcs.requests, "request", mock_request)
    return mock_request


def _assert_same_value(actual, expected):
    """Compare value and type so True is not confused with 1, or False with 0."""
    assert actual == expected
    assert type(actual) is type(expected)


class TestSSLVerifyNormalization:
    """The constructor and the setter must store the same value for the same input."""

    @pytest.mark.parametrize("provided, expected", NORMALIZATION_CASES)
    def test_constructor_normalization(self, provided, expected):
        _assert_same_value(InterfaceConfiguration(ssl_verify=provided).ssl_verify, expected)

    @pytest.mark.parametrize("provided, expected", NORMALIZATION_CASES)
    def test_setter_normalization(self, provided, expected):
        config = InterfaceConfiguration()
        config.ssl_verify = provided
        _assert_same_value(config.ssl_verify, expected)


class TestSSLVerifyReachesRequests:
    """A CA_BUNDLE path given to a constructor must arrive at requests unchanged."""

    @pytest.mark.parametrize("interface_class", [APIHarnessV2, OAuth2])
    def test_login_uses_constructor_ca_path(self, monkeypatch, interface_class):
        mock_request = _mock_requests(monkeypatch, _login_response())
        falcon = interface_class(client_id="fake_id", client_secret="fake_secret", ssl_verify=CA_PATH)
        falcon.login()

        assert falcon.ssl_verify == CA_PATH
        assert mock_request.call_args.kwargs["verify"] == CA_PATH
        assert falcon.token_status == 201

    def test_service_class_constructor_login_uses_ca_path(self, monkeypatch):
        # Service Classes log in during construction, so the path must be honored there.
        mock_request = _mock_requests(monkeypatch, _login_response())
        hosts = Hosts(client_id="fake_id", client_secret="fake_secret", ssl_verify=CA_PATH)

        assert hosts.ssl_verify == CA_PATH
        assert mock_request.call_count == 1
        assert mock_request.call_args.kwargs["verify"] == CA_PATH

    def test_uber_command_uses_constructor_ca_path(self, monkeypatch):
        mock_request = _mock_requests(monkeypatch, _FakeResponse())
        falcon = APIHarnessV2(access_token="fake_token_123", ssl_verify=CA_PATH)
        falcon.command("QueryDevicesByFilterScroll")

        assert mock_request.call_args.kwargs["verify"] == CA_PATH

    def test_service_class_method_uses_constructor_ca_path(self, monkeypatch):
        mock_request = _mock_requests(monkeypatch, _FakeResponse())
        hosts = Hosts(access_token="fake_token_123", ssl_verify=CA_PATH)
        hosts.query_devices_by_filter_scroll()

        assert mock_request.call_args.kwargs["verify"] == CA_PATH

    def test_pathlike_reaches_requests_as_str(self, monkeypatch):
        mock_request = _mock_requests(monkeypatch, _login_response())
        OAuth2(client_id="fake_id", client_secret="fake_secret", ssl_verify=pathlib.Path(CA_PATH)).login()

        _assert_same_value(mock_request.call_args.kwargs["verify"], CA_PATH)

    @pytest.mark.parametrize("empty_value", ["", "   "])
    def test_empty_ca_path_never_disables_verification(self, monkeypatch, empty_value):
        # Guards against an unset "CA bundle" config value turning TLS verification off.
        mock_request = _mock_requests(monkeypatch, _login_response(), _login_response())
        falcon = OAuth2(client_id="fake_id", client_secret="fake_secret", ssl_verify=empty_value)
        falcon.login()
        falcon.ssl_verify = empty_value
        falcon.login()

        assert [c.kwargs["verify"] for c in mock_request.call_args_list] == [True, True]
