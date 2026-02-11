# test_response_handling.py
# Tests for non-JSON and text response handling (Issue #1154)
import os
import sys
import logging
from unittest.mock import MagicMock
import pytest
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
from falconpy._util._functions import (
    calc_content_return,
    _build_text_error_body,
    log_api_activity,
)
from falconpy._error._warnings import NoContentWarning
from falconpy._result._result import BaseResult, Result


def _mock_response(status_code, content_type, body_bytes, headers=None):
    """Build a mock requests.Response with the given content type and body."""
    resp = MagicMock()
    resp.status_code = status_code
    resp.content = body_bytes
    hdrs = {"content-type": content_type}
    if headers:
        hdrs.update(headers)
    resp.headers = hdrs
    return resp


# ────────────────────────────────────────────────────────────────────
# _build_text_error_body helper
# ────────────────────────────────────────────────────────────────────
class TestBuildTextErrorBody:
    """Unit tests for the _build_text_error_body helper."""

    def test_basic_message(self):
        result = _build_text_error_body("Something went wrong", 403)
        assert result == {
            "errors": [{"code": 403, "message": "Something went wrong"}],
            "resources": []
        }

    def test_strips_whitespace(self):
        result = _build_text_error_body("  padded message  \n", 500)
        assert result["errors"][0]["message"] == "padded message"

    def test_empty_string(self):
        result = _build_text_error_body("", 204)
        assert result["errors"][0]["message"] == ""
        assert result["errors"][0]["code"] == 204
        assert result["resources"] == []


# ────────────────────────────────────────────────────────────────────
# calc_content_return — text/plain
# ────────────────────────────────────────────────────────────────────
class TestCalcContentReturnTextPlain:
    """Tests for text/plain response handling in calc_content_return."""

    def test_text_plain_non_json_403(self):
        """Issue #1154: text/plain 403 should surface the actual error text."""
        resp = _mock_response(
            403,
            "text/plain",
            b"Remote response feature is not enabled"
        )
        returned, ctype = calc_content_return(resp, False, False, None, False, "POST")
        assert returned["status_code"] == 403
        errors = returned["body"]["errors"]
        assert len(errors) == 1
        assert errors[0]["message"] == "Remote response feature is not enabled"
        assert errors[0]["code"] == 403

    def test_text_plain_valid_json_backward_compat(self):
        """text/plain with a valid JSON body should still be parsed as JSON."""
        import json
        json_payload = {"meta": {"query_time": 0.01}, "resources": ["abc"], "errors": []}
        resp = _mock_response(
            200,
            "text/plain; charset=utf-8",
            json.dumps(json_payload).encode("utf-8")
        )
        returned, ctype = calc_content_return(resp, False, False, None, False, "GET")
        assert returned["status_code"] == 200
        # The JSON body should have been parsed, not wrapped in an error
        assert returned["body"].get("resources") is not None

    def test_text_plain_empty_body(self):
        """An empty text/plain body should produce an empty error message."""
        resp = _mock_response(200, "text/plain", b"")
        returned, _ = calc_content_return(resp, False, False, None, False, "GET")
        assert returned["status_code"] == 200
        errors = returned["body"]["errors"]
        assert len(errors) == 1
        assert errors[0]["message"] == ""

    def test_text_plain_unicode_body(self):
        """Non-ASCII text/plain content should be decoded correctly."""
        msg = "Zugriff verweigert: Überprüfen Sie Ihre Anmeldedaten"
        resp = _mock_response(403, "text/plain", msg.encode("utf-8"))
        returned, _ = calc_content_return(resp, False, False, None, False, "GET")
        assert returned["body"]["errors"][0]["message"] == msg

    def test_text_plain_multiline_body(self):
        """Multi-line text should be preserved (stripped of outer whitespace)."""
        msg = "Error occurred.\nPlease contact support.\nRef: ABC-123"
        resp = _mock_response(500, "text/plain", msg.encode("utf-8"))
        returned, _ = calc_content_return(resp, False, False, None, False, "GET")
        assert "Please contact support." in returned["body"]["errors"][0]["message"]

    def test_text_plain_head_request(self):
        """HEAD request with text/plain content type should still be handled."""
        resp = _mock_response(200, "text/plain", b"")
        returned, _ = calc_content_return(resp, False, False, None, False, "HEAD")
        assert returned["status_code"] == 200

    def test_text_plain_error_pythonic_mode(self):
        """Pythonic mode should raise APIError with the actual text message."""
        from falconpy._error import APIError
        resp = _mock_response(
            403,
            "text/plain",
            b"Remote response feature is not enabled"
        )
        with pytest.raises(APIError) as exc_info:
            calc_content_return(resp, False, False, None, True, "POST")
        assert "Remote response feature is not enabled" in str(exc_info.value)

    def test_text_plain_200_non_json(self):
        """A 200 response with non-JSON text/plain should still return cleanly."""
        resp = _mock_response(200, "text/plain", b"OK")
        returned, _ = calc_content_return(resp, False, False, None, False, "GET")
        assert returned["status_code"] == 200
        assert returned["body"]["errors"][0]["message"] == "OK"

    def test_text_plain_with_charset_suffix(self):
        """Content-Type 'text/plain; charset=iso-8859-1' should match text/plain."""
        resp = _mock_response(403, "text/plain; charset=iso-8859-1", b"Forbidden")
        returned, ctype = calc_content_return(resp, False, False, None, False, "GET")
        assert returned["body"]["errors"][0]["message"] == "Forbidden"


# ────────────────────────────────────────────────────────────────────
# calc_content_return — text/html
# ────────────────────────────────────────────────────────────────────
class TestCalcContentReturnTextHTML:
    """Tests for text/html response handling."""

    def test_text_html_proxy_error(self):
        """Proxy/WAF HTML error pages should be surfaced in the standard format."""
        html = "<html><body><h1>403 Forbidden</h1></body></html>"
        resp = _mock_response(403, "text/html", html.encode("utf-8"))
        returned, ctype = calc_content_return(resp, False, False, None, False, "GET")
        assert returned["status_code"] == 403
        assert "403 Forbidden" in returned["body"]["errors"][0]["message"]
        assert ctype.startswith("text/html")

    def test_text_html_empty(self):
        """Empty HTML response should produce an empty error message."""
        resp = _mock_response(502, "text/html; charset=utf-8", b"")
        returned, _ = calc_content_return(resp, False, False, None, False, "GET")
        assert returned["body"]["errors"][0]["message"] == ""

    def test_text_html_with_invalid_utf8(self):
        """Malformed UTF-8 in HTML responses should be handled via replacement."""
        body = b"<html>Invalid byte: \xff\xfe</html>"
        resp = _mock_response(500, "text/html", body)
        returned, _ = calc_content_return(resp, False, False, None, False, "GET")
        # Should not raise, the replacement characters will be in the message
        assert returned["status_code"] == 500
        assert "html" in returned["body"]["errors"][0]["message"].lower()

    def test_text_html_pythonic_mode(self):
        """Pythonic mode with text/html error should raise APIError."""
        from falconpy._error import APIError
        html = "<html><body>Gateway Timeout</body></html>"
        resp = _mock_response(504, "text/html", html.encode("utf-8"))
        with pytest.raises(APIError):
            calc_content_return(resp, False, False, None, True, "GET")


# ────────────────────────────────────────────────────────────────────
# log_api_activity — text content types
# ────────────────────────────────────────────────────────────────────
class TestLogApiActivity:
    """Tests for log_api_activity with text content types."""

    def test_log_text_html(self):
        """text/html responses should be logged as text, not as binary."""
        logger = MagicMock(spec=logging.Logger)
        api = MagicMock()
        api.log_util = logger
        api.sanitize_log = False
        api.max_debug = 10

        content = {"status_code": 403, "body": {"errors": [{"message": "err"}]}}
        log_api_activity(content, "text/html", api)

        calls = [str(c) for c in logger.debug.call_args_list]
        result_calls = [c for c in calls if "RESULT" in c]
        assert len(result_calls) > 0
        for rc in result_calls:
            assert "binary" not in rc.lower()

    def test_log_text_plain(self):
        """text/plain responses should be logged as text."""
        logger = MagicMock(spec=logging.Logger)
        api = MagicMock()
        api.log_util = logger
        api.sanitize_log = False
        api.max_debug = 10

        content = {"status_code": 200, "body": {}}
        log_api_activity(content, "text/plain", api)

        calls = [str(c) for c in logger.debug.call_args_list]
        result_calls = [c for c in calls if "RESULT" in c]
        assert len(result_calls) > 0
        for rc in result_calls:
            assert "binary" not in rc.lower()


# ────────────────────────────────────────────────────────────────────
# NoContentWarning — enhanced with response_body / content_type
# ────────────────────────────────────────────────────────────────────
class TestNoContentWarningEnhanced:
    """Tests for the enhanced NoContentWarning with response_body."""

    def test_default_message_unchanged(self):
        """Without response_body, the default message should be preserved."""
        w = NoContentWarning()
        assert w.message == "No content was received for this request."
        assert w.response_body is None
        assert w.content_type is None

    def test_response_body_overrides_message(self):
        """When response_body is provided, it becomes the warning message."""
        w = NoContentWarning(
            code=403,
            response_body="Remote response feature is not enabled",
            content_type="text/plain"
        )
        assert w.message == "Remote response feature is not enabled"
        assert w.code == 403
        assert w.response_body == "Remote response feature is not enabled"
        assert w.content_type == "text/plain"

    def test_response_body_strips_whitespace(self):
        """Leading/trailing whitespace in response_body should be stripped."""
        w = NoContentWarning(
            response_body="  some error  \n",
            content_type="text/plain"
        )
        assert w.message == "some error"

    def test_explicit_message_takes_priority(self):
        """An explicit message should not be overridden by response_body."""
        w = NoContentWarning(
            message="Custom message",
            response_body="Raw body text"
        )
        assert w.message == "Custom message"
        assert w.response_body == "Raw body text"

    def test_result_property(self):
        """The .result property should still work with enhanced warning."""
        w = NoContentWarning(
            code=403,
            response_body="Forbidden",
            content_type="text/plain"
        )
        result = w.result
        assert result["status_code"] == 403
        assert "Forbidden" in str(result["body"])


# ────────────────────────────────────────────────────────────────────
# BaseResult._is_text_error_body
# ────────────────────────────────────────────────────────────────────
class TestIsTextErrorBody:
    """Tests for BaseResult._is_text_error_body static method."""

    def test_detects_text_error_body(self):
        """A dict with only 'errors' and 'resources' is a text error body."""
        body = {"errors": [{"code": 403, "message": "Forbidden"}], "resources": []}
        assert BaseResult._is_text_error_body(body) is True

    def test_rejects_standard_api_body(self):
        """A body with 'meta' is a standard API response, not a text error."""
        body = {"meta": {}, "errors": [], "resources": []}
        assert BaseResult._is_text_error_body(body) is False

    def test_rejects_auth_body(self):
        """A body with 'access_token' is an auth response."""
        body = {"access_token": "tok", "errors": [], "resources": []}
        assert BaseResult._is_text_error_body(body) is False

    def test_rejects_non_dict(self):
        """Non-dict inputs should return False."""
        assert BaseResult._is_text_error_body("string") is False
        assert BaseResult._is_text_error_body([]) is False
        assert BaseResult._is_text_error_body(None) is False

    def test_rejects_dict_with_extra_keys(self):
        """A dict with extra keys beyond errors/resources is not a text error body."""
        body = {"errors": [], "resources": [], "extra": "value"}
        assert BaseResult._is_text_error_body(body) is False


# ────────────────────────────────────────────────────────────────────
# Result._parse_body text error body path
# ────────────────────────────────────────────────────────────────────
class TestResultParseBodyTextError:
    """Tests for the text error body path in Result._parse_body."""

    def test_text_error_body_populates_errors(self):
        """A text error body should populate the Errors attribute."""
        body = _build_text_error_body("Server error occurred", 500)
        result = Result(500, {"content-type": "text/plain"}, body)
        assert len(result.errors) == 1
        assert result.errors[0]["message"] == "Server error occurred"

    def test_text_error_body_empty_resources(self):
        """A text error body should have empty resources."""
        body = _build_text_error_body("Forbidden", 403)
        result = Result(403, {"content-type": "text/plain"}, body)
        assert len(result.resources) == 0

    def test_text_error_body_full_return_format(self):
        """full_return from a text error body should have standard structure."""
        body = _build_text_error_body("Not Allowed", 403)
        result = Result(403, {"content-type": "text/plain"}, body)
        fr = result.full_return
        assert fr["status_code"] == 403
        assert "errors" in fr["body"]
        assert fr["body"]["errors"][0]["message"] == "Not Allowed"
        assert fr["body"]["resources"] == []
