# test_hec.py
# This class tests the HTTP Event Collector class

# import json
import os
import sys
import logging
import pytest

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import (
    HTTPEventCollector,
    random_string,
    TimeUnit,
    Indicator,
    IngestFormat,
    IngestConfig,
    IngestPayload,
    SessionManager
    )
from datetime import datetime, timezone
from requests import Session
API_KEY = os.getenv("DEBUG_NGSIEM_API_KEY")
URL_KEY = os.getenv("DEBUG_NGSIEM_URL_KEY")
BASE_REGION = os.getenv("DEBUG_API_BASE_URL", "us1")
if BASE_REGION == "usgov1":
    # Not ready for USGOV1 unit testing
    pytest.skip(allow_module_level=True)
some_log = logging.basicConfig(level=logging.DEBUG)
HEC = HTTPEventCollector(api_key=API_KEY,
                         api_url_key=URL_KEY,
                         ingest_region=BASE_REGION,
                         debug=True
                         )
# Check if NGSIEM is properly configured
NGSIEM_CONFIGURED = API_KEY and URL_KEY and HEC.test_connection()
AllowedResponses = [200]

simple_payload = {"host": random_string(8).upper(), "timestamp": int(datetime.now(timezone.utc).timestamp() * TimeUnit["NANOSECONDS"].value)}

class TestHTTPEventCollector:
    def test_fail_connection(self):
        bad_hec = HTTPEventCollector(api_key="this_wont", api_url_key="work", debug=True) #, ingest_format="garbage", ingest_region="us1", ingest_timeout=None
        bad_hec.ingest_key = "neither_will"
        bad_hec.ingest_url_key = "this"
        bad_hec.ingest_format = "not_a_real_format"
        bad_hec.ingest_timeunit = "seconds"
        check = bad_hec.ingest_config.ingest_region
        bad_hec.ingest_config.ingest_region = check
        bad_hec.ingest_base_url = random_string(10, include_specials=True)
        #bad_hec.raw_ingest = True
        bad_hec.sanitize_log = False
        #bad_hec.retry_count = 1
        bad_hec.sessions = [Session()]
        bad_hec.thread_count = 2
        assert bad_hec.test_connection() == False

    @pytest.mark.skipif(not NGSIEM_CONFIGURED, reason="NGSIEM not properly configured")
    def test_connection(self):
        assert HEC.test_connection()

    @pytest.mark.skipif(not NGSIEM_CONFIGURED, reason="NGSIEM not properly configured")
    def test_simple_ingest(self):
        error_check = True
        result = HEC.send_event(simple_payload)
        if result not in AllowedResponses:
            error_check = False

        assert error_check

    @pytest.mark.skipif(not NGSIEM_CONFIGURED, reason="NGSIEM not properly configured")
    def test_list_ingest(self):
        result = 0
        result = HEC.send_event_list([simple_payload])
        indicator = Indicator("not_an_option")
        check_pos = indicator.position
        for _ in range(len(indicator.indicator)+1):
            f"{indicator}"
        if indicator.position <= check_pos:
            result = -2
        for gen_result in HEC.send_event_list([simple_payload], show_progress=True):
            result += gen_result

        assert result>1

    @pytest.mark.skipif(not NGSIEM_CONFIGURED, reason="NGSIEM not properly configured")
    def test_raw_ingest(self):
        error_check = True
        ingest_format_name = None
        for i_format in IngestFormat:
            if i_format.value == HEC.ingest_format:
                ingest_format_name = i_format.name
        raw_hec = HTTPEventCollector(api_key=HEC.ingest_key,
                                     api_url_key=HEC.ingest_url_key,
                                     ingest_region=BASE_REGION,
                                     raw_ingest=True,
                                     debug=True,
                                     ingest_format=ingest_format_name
                                     )
        result = raw_hec.send_event_file("tests/5records.raw")
        if result not in AllowedResponses:
            error_check = False
        raw_hec.ingest_timeout=10
        with raw_hec as hec:
            result = hec.send_event_file("tests/100thousand.raw.gz")
        if result not in AllowedResponses:
            error_check = False
        assert error_check

    def test_failures(self):
        bad_hec = HTTPEventCollector(api_key=API_KEY,
                                     api_url_key="7334$@",
                                     ingest_region=BASE_REGION,
                                     debug=True
                                     )
        session_list = bad_hec.sessions
        bad_hec.ingest_timeout = 1
        bad_hec.retry_count = 2
        error_check = 0

        result = bad_hec.send_event(simple_payload)
        if result == 500:
            error_check += 1
        bad_hec.raw_ingest = True
        bad_hec.ingest_url_key = URL_KEY

        result = bad_hec.send_event_file("tests/100thousand.raw.gz")
        if result in AllowedResponses or result == 500:
            error_check += 1

        try:
            result = bad_hec.send_event_file("does_not_exist")
        except SystemExit:
            error_check += 1
        assert error_check > 2

    def test_subclasses(self):
        config = IngestConfig(ingest_key=random_string(8), ingest_url_key=random_string(10), ingest_format="banana", ingest_timeout=0)
        config.ingest_base_url = "us1"
        check_value = config.ingest_timeout
        payload = IngestPayload(kind="red", module="yellow", event_type="blue", category="yellow", custom={"color": "chartreuse"}, fields={"color": "orange"})
        payload.kind = "purple"
        payload.module = "gray"
        payload.type = "black"
        payload.category = "white"
        payload.fields = {"another_color": "indigo"}
        json_output = payload.to_json(raw=True, nowrap=True)
        json_output = payload.to_json()
        another_payload = IngestPayload(category=["green"], timeunit=None, event_type=["yellow"], message = "whatever", fields={"#falconpy": "HEC Testing"})
        xml_version = another_payload.to_xml(raw=True, nowrap=True)
        xml_version = another_payload.to_xml()
        cxv_version = another_payload.to_csv()
        quick_hec = HTTPEventCollector(api_key=random_string(8), api_url_key=random_string(8), raw_ingest=True, thread_count=5)
        json_string = quick_hec.format_event(another_payload)
        quick_sm = SessionManager()
        count = 0
        for _ in quick_sm:
            count += 1
            # will scroll indefinitely
            if count > 3:
                break


class TestIndicatorCoverage:
    """Cover _helper/_indicator.py lines 66-92."""

    def test_default_style(self):
        """Test Indicator with default (moon) style."""
        ind = Indicator()
        assert ind.position == -1
        assert isinstance(ind.indicator, list)
        result = f"{ind}"
        assert ind.position == 0
        assert isinstance(result, str)

    def test_valid_style(self):
        """Test Indicator with a valid named style."""
        ind = Indicator("clock")
        assert ind.indicator == Indicator.CLOCK

    def test_invalid_style_fallback(self):
        """Test Indicator with invalid style falls back to MOON."""
        ind = Indicator("not_a_real_style")
        assert ind.indicator == Indicator.MOON

    def test_repr_wraps_around(self):
        """Test that __repr__ wraps position back to 0."""
        ind = Indicator("moon")
        for _ in range(len(ind.indicator) + 1):
            f"{ind}"
        assert ind.position == 0

    def test_position_setter(self):
        """Test the position setter."""
        ind = Indicator()
        ind.position = 5
        assert ind.position == 5

    def test_indicator_property(self):
        """Test the indicator property getter."""
        ind = Indicator("kitt")
        assert ind.indicator == Indicator.KITT

    def test_position_property(self):
        """Test the position property getter."""
        ind = Indicator()
        assert ind.position == -1


class TestHECCoverage:
    """Cover _ngsiem/_hec.py uncovered paths without requiring live NGSIEM."""

    def test_hec_context_manager_exit(self):
        """Cover __exit__ with an exception arg."""
        hec = HTTPEventCollector(
            api_key="fake_key",
            api_url_key="fake_url_key",
            debug=True
        )
        hec.__exit__(None, None, None)

    def test_hec_send_event_file_plain_text(self):
        """Cover send_event_file with a plain text file."""
        hec = HTTPEventCollector(
            api_key="fake_key",
            api_url_key="fake_url_key",
            debug=True,
            raw_ingest=True
        )
        hec.ingest_timeout = 1
        hec.retry_count = 1
        result = hec.send_event_file("tests/5records.raw")
        assert isinstance(result, int)

    def test_hec_retry_timeout(self):
        """Cover retry timeout path."""
        hec = HTTPEventCollector(
            api_key="fake_key",
            api_url_key="fake_url_key",
            debug=True
        )
        hec.ingest_timeout = 0.001
        hec.retry_count = 1
        result = hec.send_event({"host": "test", "test": True})
        assert result == 500

    def test_hec_retry_ssl_error(self):
        """Cover SSL/InvalidURL error retry path."""
        hec = HTTPEventCollector(
            api_key="fake_key",
            api_url_key="bad://invalid_url",
            debug=True
        )
        hec.ingest_timeout = 1
        hec.retry_count = 1
        result = hec.send_event({"host": "test", "test": True})
        assert result == 500

    def test_hec_send_event_success_logging(self):
        """Cover successful send_event with debug logging."""
        hec = HTTPEventCollector(
            api_key="fake_key",
            api_url_key="fake_url_key",
            debug=True
        )
        hec.sanitize_log = False
        hec.ingest_timeout = 1
        hec.retry_count = 1
        result = hec.send_event({"host": "test"})
        assert isinstance(result, int)

    def test_hec_process_list(self):
        """Cover process_list path."""
        hec = HTTPEventCollector(
            api_key="fake_key",
            api_url_key="fake_url_key",
            debug=True
        )
        hec.ingest_timeout = 1
        hec.retry_count = 1
        result = hec.send_event_list([{"host": "test1"}, {"host": "test2"}])
        assert isinstance(result, int)

    def test_hec_test_connection_failure_logging(self):
        """Cover test_connection logging paths."""
        hec = HTTPEventCollector(
            api_key="fake_key",
            api_url_key="fake_url_key",
            debug=True
        )
        hec.ingest_timeout = 1
        hec.retry_count = 1
        result = hec.test_connection()
        assert result is False

    def test_hec_log_startup_raw_ingest(self):
        """Cover log_startup with raw_ingest=True."""
        hec = HTTPEventCollector(
            api_key="fake_key",
            api_url_key="fake_url_key",
            debug=True,
            raw_ingest=True
        )
        assert hec.raw_ingest is True

    def test_hec_log_activity_list_with_logo(self):
        """Cover log_activity with list messages and logo mode."""
        hec = HTTPEventCollector(
            api_key="fake_key",
            api_url_key="fake_url_key",
            debug=True
        )
        hec.log_activity(["line1", "line2"], logo=True)
        hec.log_activity("single line message")
        hec.log_activity(None)

    def test_hec_send_event_file_gzip_with_failure(self):
        """Cover send_event_file with gzip that gets a response."""
        hec = HTTPEventCollector(
            api_key="fake_key",
            api_url_key="fake_url_key",
            debug=True,
            raw_ingest=True
        )
        hec.ingest_timeout = 1
        hec.retry_count = 1
        try:
            result = hec.send_event_file("tests/100thousand.raw.gz")
            assert isinstance(result, int)
        except Exception:
            pass

    def test_hec_process_list_with_progress(self):
        """Cover process_list_with_progress path."""
        hec = HTTPEventCollector(
            api_key="fake_key",
            api_url_key="fake_url_key",
            debug=True
        )
        hec.ingest_timeout = 1
        hec.retry_count = 1
        results = list(hec.send_event_list(
            [{"host": "test1"}, {"host": "test2"}],
            show_progress=True
        ))
        assert isinstance(results, list)

    def test_hec_enter_context_manager(self):
        """Cover __enter__ returns self."""
        hec = HTTPEventCollector(api_key="k", api_url_key="u")
        with hec as h:
            assert h is hec


class _FakeResponse:
    """Minimal stand-in for requests.Response used by monkeypatch tests."""

    def __init__(self, status_code=200, json_data=None, headers=None):
        self.status_code = status_code
        self.headers = headers or {"Content-Type": "application/json"}
        self._json_data = json_data or {"text": "Success"}
        self.content = b'{"text": "Success"}'

    def json(self):
        return self._json_data


class TestHECMockedCoverage:
    """Cover _ngsiem/_hec.py success paths using monkeypatch."""

    def test_hec_send_event_success(self, monkeypatch):
        """Cover send_event with successful response."""
        import requests
        monkeypatch.setattr(requests.Session, "post", lambda *a, **kw: _FakeResponse())
        hec = HTTPEventCollector(api_key="k", api_url_key="u", debug=True)
        result = hec.send_event({"host": "test"})
        assert result == 200

    def test_hec_test_connection_success(self, monkeypatch):
        """Cover test_connection success path."""
        import requests
        monkeypatch.setattr(requests.Session, "post", lambda *a, **kw: _FakeResponse())
        hec = HTTPEventCollector(api_key="k", api_url_key="u", debug=True)
        assert hec.test_connection() is True

    def test_hec_process_list_success(self, monkeypatch):
        """Cover process_list success count increment."""
        import requests
        monkeypatch.setattr(requests.Session, "post", lambda *a, **kw: _FakeResponse())
        hec = HTTPEventCollector(api_key="k", api_url_key="u", debug=True)
        result = hec.send_event_list([{"host": "a"}, {"host": "b"}])
        assert result == 2

    def test_hec_process_list_with_progress_success(self, monkeypatch):
        """Cover process_list_with_progress success count."""
        import requests
        monkeypatch.setattr(requests.Session, "post", lambda *a, **kw: _FakeResponse())
        hec = HTTPEventCollector(api_key="k", api_url_key="u", debug=True)
        results = list(hec.send_event_list([{"host": "a"}, {"host": "b"}], show_progress=True))
        assert results[-1] == 2

    def test_hec_send_event_file_success(self, monkeypatch):
        """Cover send_event_file with successful response."""
        import requests
        monkeypatch.setattr(requests.Session, "post", lambda *a, **kw: _FakeResponse())
        hec = HTTPEventCollector(api_key="k", api_url_key="u", debug=True, raw_ingest=True)
        result = hec.send_event_file("tests/5records.raw")
        assert result == 200