# test_non_json_error_responses.py
# This class tests handling of error responses that do not contain JSON (Issue #1508)
import os
import sys
from unittest.mock import patch
import pytest
import requests
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy._util._functions import build_error_body_from_payload, calc_content_return
from falconpy._constant import MAX_ERROR_PAYLOAD_LENGTH
from falconpy._error import APIError
from falconpy import UserManagement, APIHarnessV2

# A gateway error page, the most common cause of a non-JSON error response.
_HTML_ERROR = b"<html><head><title>502 Bad Gateway</title></head><body>502</body></html>"
_TRACE_ID = "8f14e45f-ea8a-42f6-9e2b-1c3d4e5f6a7b"


def build_response(status_code: int, content_type, content: bytes) -> requests.Response:
    """Create a requests.Response without performing a live API call."""
    response = requests.Response()
    response.status_code = status_code
    response._content = content
    response.headers["X-Cs-Traceid"] = _TRACE_ID
    if content_type:
        response.headers["Content-Type"] = content_type

    return response


def content_return(response: requests.Response, pythonic: bool = False):
    """Call the response handler with the defaults used by a standard request."""
    return calc_content_return(resp=response,
                               contain=False,
                               auth=False,
                               log=None,
                               pythonic_mode=pythonic,
                               api_method="POST"
                               )


class TestNonJSONErrorResponses:
    """Confirm error responses that are not JSON return the documented structure."""

    @pytest.mark.parametrize("status_code,content_type,content", [
        (502, "text/html", _HTML_ERROR),                     # Gateway error page
        (503, None, b""),                                    # Empty body, no Content-Type
        (500, "application/octet-stream", b"\x00\x01\x02"),  # Unexpected content type
        (429, "text/html", b"<html>Too Many Requests</html>")  # Rate limit page
    ])
    def test_non_json_error_returns_standard_structure(self, status_code, content_type, content):
        """A non-JSON error response returns a dictionary instead of raising."""
        returned, _ = content_return(build_response(status_code, content_type, content))

        assert isinstance(returned, dict)
        # The status code reported by the API is retained, not replaced with a 500.
        assert returned["status_code"] == status_code
        # Headers are retained so the trace ID remains available for support requests.
        assert returned["headers"]["X-Cs-Traceid"] == _TRACE_ID
        assert isinstance(returned["body"], dict)
        assert returned["body"]["errors"][0]["code"] == status_code
        assert returned["body"]["errors"][0]["message"]
        assert returned["body"]["resources"] == []

    def test_error_message_contains_response_payload(self):
        """The payload returned by the API is surfaced within the error message."""
        returned, _ = content_return(build_response(502, "text/html", _HTML_ERROR))

        assert "502 Bad Gateway" in returned["body"]["errors"][0]["message"]

    def test_empty_payload_reports_no_content(self):
        """An error with no payload reports that no content was received."""
        returned, _ = content_return(build_response(503, None, b""))

        assert returned["body"]["errors"][0]["message"] == "No content was received for this request."

    def test_successful_binary_response_is_unchanged(self):
        """A successful binary response is still returned as raw bytes."""
        returned, _ = content_return(build_response(200, "application/octet-stream", b"\x50\x4b\x03\x04"))

        assert isinstance(returned, bytes)
        assert returned == b"\x50\x4b\x03\x04"

    def test_json_error_response_is_unchanged(self):
        """An error that does contain JSON is not modified."""
        body = b'{"meta": {"trace_id": "1"}, "errors": [{"code": 403, "message": "access denied"}], "resources": []}'
        returned, _ = content_return(build_response(403, "application/json", body))

        assert returned["body"]["errors"][0]["message"] == "access denied"
        assert returned["body"]["meta"]["trace_id"] == "1"

    def test_pythonic_mode_raises_with_payload(self):
        """Pythonic mode raises an APIError describing the failure."""
        with pytest.raises(APIError) as raised:
            content_return(build_response(502, "text/html", _HTML_ERROR), pythonic=True)

        assert raised.value.code == 502
        assert "502 Bad Gateway" in raised.value.message


class TestErrorBodyGeneration:
    """Confirm generated error bodies are well formed."""

    def test_oversized_payload_is_truncated(self):
        """A payload larger than the maximum length is truncated."""
        returned = build_error_body_from_payload(b"A" * (MAX_ERROR_PAYLOAD_LENGTH + 100), 502)
        message = returned["errors"][0]["message"]

        assert len(message) == MAX_ERROR_PAYLOAD_LENGTH + 3
        assert message.endswith("...")

    def test_undecodable_payload_does_not_raise(self):
        """A payload that is not valid UTF-8 is decoded without raising."""
        returned = build_error_body_from_payload(b"\xff\xfe binary payload", 500)

        assert "binary payload" in returned["errors"][0]["message"]

    def test_string_payload_is_accepted(self):
        """A payload that has already been decoded is handled."""
        returned = build_error_body_from_payload("  upstream connect error  ", 503)

        assert returned["errors"][0] == {"code": 503, "message": "upstream connect error"}


class TestNonJSONErrorResponsesByClass:
    """Confirm both class styles return the documented structure."""

    @staticmethod
    def gateway_error(*args, **kwargs) -> requests.Response:
        """Return a gateway error page in place of a live API response."""
        return build_response(502, "text/html", _HTML_ERROR)

    def test_service_class(self):
        """A Service Class returns the error structure instead of a generated 500."""
        with patch("requests.request", self.gateway_error):
            falcon = UserManagement(access_token="testing", base_url="https://api.crowdstrike.com")
            returned = falcon.grant_user_role_ids(role_ids=["role"], user_uuid="uuid")

        assert returned["status_code"] == 502
        assert returned["headers"]["X-Cs-Traceid"] == _TRACE_ID
        assert "502 Bad Gateway" in returned["body"]["errors"][0]["message"]

    def test_uber_class(self):
        """The Uber Class returns the error structure instead of a generated 500."""
        with patch("requests.request", self.gateway_error):
            falcon = APIHarnessV2(access_token="testing", base_url="https://api.crowdstrike.com")
            returned = falcon.command("GrantUserRoleIds", user_uuid="uuid", body={"roleIds": ["role"]})

        assert returned["status_code"] == 502
        assert returned["headers"]["X-Cs-Traceid"] == _TRACE_ID
        assert "502 Bad Gateway" in returned["body"]["errors"][0]["message"]
