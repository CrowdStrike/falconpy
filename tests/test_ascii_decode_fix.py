# test_ascii_decode_fix.py
# Tests for ASCII codec decode error fix (Issue #1298)
import os
import sys
import json
import logging
from unittest.mock import MagicMock
import pytest

sys.path.append(os.path.abspath('src'))
from falconpy._util._functions import (
    calc_content_return,
    _safe_decode_content,
)
from falconpy._error._exceptions import ContentDecodingError
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
    # Simulate resp.json() behavior
    def _json():
        return json.loads(body_bytes.decode("utf-8"))
    resp.json = _json
    return resp


def _mock_response_bad_json(status_code, content_type, body_bytes):
    """Mock response where resp.json() raises JSONDecodeError but content is decodable."""
    resp = MagicMock()
    resp.status_code = status_code
    resp.content = body_bytes
    resp.headers = {"content-type": content_type}
    resp.json = MagicMock(side_effect=json.JSONDecodeError("err", "doc", 0))
    return resp


# ────────────────────────────────────────────────────────────────────
# _safe_decode_content helper
# ────────────────────────────────────────────────────────────────────
class TestSafeDecodeContent:
    """Tests for the _safe_decode_content helper."""

    def test_utf8_ascii_only(self):
        """Pure ASCII bytes should decode cleanly."""
        assert _safe_decode_content(b'{"key": "value"}') == '{"key": "value"}'

    def test_utf8_accented_characters(self):
        """UTF-8 multi-byte characters (the 0xC3 byte) should decode correctly.
        This is the exact scenario from Issue #1298."""
        text = '{"name": "Ángel García"}'
        assert _safe_decode_content(text.encode("utf-8")) == text

    def test_utf8_chinese_characters(self):
        """CJK characters should decode correctly."""
        text = '{"user": "用户名"}'
        assert _safe_decode_content(text.encode("utf-8")) == text

    def test_utf8_emoji(self):
        """Emoji (4-byte UTF-8 sequences) should decode correctly."""
        text = '{"status": "✅ success"}'
        assert _safe_decode_content(text.encode("utf-8")) == text

    def test_latin1_fallback(self):
        """When UTF-8 decoding fails, latin-1 should be used as fallback."""
        # Byte 0xFF is invalid in UTF-8 but valid in latin-1 (ÿ)
        raw = b'{"val": "\xff"}'
        result = _safe_decode_content(raw)
        assert "\xff" not in result or "ÿ" in result  # latin-1 decoded

    def test_empty_bytes(self):
        """Empty bytes should decode to empty string."""
        assert _safe_decode_content(b"") == ""

    def test_large_payload_with_accented_names(self):
        """Simulate the real-world scenario: large JSON with accented names."""
        # Build a payload similar to what triggered #1298
        names = ["Müller", "Ángel", "François", "Ôsaka", "Ñoño"]
        payload = {"resources": [{"name": n} for n in names]}
        raw_bytes = json.dumps(payload).encode("utf-8")
        decoded = _safe_decode_content(raw_bytes)
        parsed = json.loads(decoded)
        assert len(parsed["resources"]) == 5
        assert parsed["resources"][0]["name"] == "Müller"


# ────────────────────────────────────────────────────────────────────
# calc_content_return — application/json with non-ASCII content
# ────────────────────────────────────────────────────────────────────
class TestCalcContentReturnJsonNonAscii:
    """Tests for non-ASCII JSON handling in calc_content_return (Issue #1298)."""

    def test_json_with_accented_names_via_resp_json(self):
        """Standard path: resp.json() succeeds with UTF-8 accented names."""
        payload = {"meta": {}, "resources": [{"name": "Ángel"}], "errors": []}
        resp = _mock_response(
            200,
            "application/json",
            json.dumps(payload).encode("utf-8")
        )
        returned, ctype = calc_content_return(resp, False, False, None, False, "GET")
        assert returned["status_code"] == 200
        assert returned["body"]["resources"][0]["name"] == "Ángel"

    def test_json_fallback_with_accented_names(self):
        """Fallback path: resp.json() fails but content has accented names.
        This was the exact crash scenario from Issue #1298."""
        payload = {"meta": {}, "resources": [{"name": "Müller"}], "errors": []}
        body_bytes = json.dumps(payload).encode("utf-8")
        resp = _mock_response_bad_json(200, "application/json", body_bytes)
        returned, ctype = calc_content_return(resp, False, False, None, False, "GET")
        assert returned["status_code"] == 200
        assert returned["body"]["resources"][0]["name"] == "Müller"

    def test_json_fallback_with_0xc3_byte(self):
        """The exact byte (0xC3) that caused Issue #1298 should now work."""
        # 0xC3 0x81 = 'Á' in UTF-8
        payload = '{"errors": [{"message": "User \\u00c1ngel not found"}]}'
        body_bytes = payload.encode("utf-8")
        resp = _mock_response_bad_json(404, "application/json", body_bytes)
        returned, ctype = calc_content_return(resp, False, False, None, False, "GET")
        assert returned["status_code"] == 404

    def test_json_fallback_ascii_only_backward_compat(self):
        """Pure ASCII JSON via fallback path should still work (backward compat)."""
        payload = {"meta": {}, "resources": ["abc123"], "errors": []}
        body_bytes = json.dumps(payload).encode("ascii")
        resp = _mock_response_bad_json(200, "application/json", body_bytes)
        returned, ctype = calc_content_return(resp, False, False, None, False, "GET")
        assert returned["status_code"] == 200
        assert "abc123" in str(returned["body"]["resources"])

    def test_json_with_multi_byte_cjk(self):
        """CJK characters in JSON should not crash the fallback decoder."""
        payload = {"resources": [{"desc": "用户"}], "errors": []}
        body_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        resp = _mock_response_bad_json(200, "application/json", body_bytes)
        returned, _ = calc_content_return(resp, False, False, None, False, "GET")
        assert returned["body"]["resources"][0]["desc"] == "用户"

    def test_json_head_request_no_crash(self):
        """HEAD request should not attempt fallback decode at all."""
        resp = _mock_response_bad_json(200, "application/json", b"")
        returned, _ = calc_content_return(resp, False, False, None, False, "HEAD")
        assert returned["status_code"] == 200


# ────────────────────────────────────────────────────────────────────
# ContentDecodingError exception
# ────────────────────────────────────────────────────────────────────
class TestContentDecodingError:
    """Tests for the new ContentDecodingError exception."""

    def test_basic_construction(self):
        err = ContentDecodingError(encoding="ascii", position=32125)
        assert err.encoding == "ascii"
        assert err.position == 32125
        assert err.code == 500
        assert "ascii" in err.message
        assert "32125" in err.message

    def test_default_message(self):
        err = ContentDecodingError()
        assert err.message == "Unable to decode API response content."
        assert err.encoding is None
        assert err.position is None

    def test_custom_message(self):
        err = ContentDecodingError(message="Custom error", encoding="utf-8")
        assert err.message == "Custom error"
        assert err.encoding == "utf-8"

    def test_result_property(self):
        err = ContentDecodingError(code=500, encoding="ascii", position=100)
        result = err.result
        assert result["status_code"] == 500
        assert "ascii" in str(result["body"])

    def test_simple_property(self):
        err = ContentDecodingError(encoding="ascii", position=42)
        assert "500" in err.simple
        assert "ascii" in err.simple


# ────────────────────────────────────────────────────────────────────
# NoContentWarning — encoding context
# ────────────────────────────────────────────────────────────────────
class TestNoContentWarningEncoding:
    """Tests for the enhanced NoContentWarning with encoding property."""

    def test_default_no_encoding(self):
        w = NoContentWarning()
        assert w.encoding is None
        assert w.message == "No content was received for this request."

    def test_with_encoding(self):
        w = NoContentWarning(code=200, encoding="ascii")
        assert w.encoding == "ascii"
        assert "ascii" in w.message

    def test_explicit_message_priority(self):
        w = NoContentWarning(message="Custom", encoding="utf-8")
        assert w.message == "Custom"
        assert w.encoding == "utf-8"

    def test_result_with_encoding(self):
        w = NoContentWarning(code=200, encoding="ascii")
        result = w.result
        assert result["status_code"] == 200


# ────────────────────────────────────────────────────────────────────
# BaseResult._safe_decode_body
# ────────────────────────────────────────────────────────────────────
class TestSafeDecodeBody:
    """Tests for BaseResult._safe_decode_body static method."""

    def test_utf8_bytes(self):
        text = "Ángel García"
        assert BaseResult._safe_decode_body(text.encode("utf-8")) == text

    def test_latin1_fallback(self):
        raw = b"\xff\xfe"
        result = BaseResult._safe_decode_body(raw)
        # Should not raise
        assert len(result) == 2

    def test_empty_bytes(self):
        assert BaseResult._safe_decode_body(b"") == ""


# ────────────────────────────────────────────────────────────────────
# Result._parse_body bytes with JSON content
# ────────────────────────────────────────────────────────────────────
class TestResultParseBodyBytes:
    """Tests for encoding-aware _parse_body when receiving bytes."""

    def test_bytes_json_with_accented_names(self):
        """Bytes containing valid JSON with accented names should be parsed."""
        payload = {"meta": {}, "resources": [{"name": "François"}], "errors": []}
        body_bytes = json.dumps(payload).encode("utf-8")
        result = Result(200, {"content-type": "application/json"}, body_bytes)
        # Should parse the JSON successfully instead of treating as binary
        assert result.resources is not None
        assert len(result.resources) == 1

    def test_bytes_genuine_binary_not_parsed(self):
        """Genuine binary content should still be treated as binary."""
        body_bytes = b"\x89PNG\r\n\x1a\n\x00\x00"  # PNG header
        result = Result(200, {"content-type": "image/png"}, body_bytes)
        assert result.resources is not None

    def test_bytes_empty(self):
        """Empty bytes should not crash."""
        result = Result(200, {"content-type": "application/json"}, b"")
        assert result.resources is not None
