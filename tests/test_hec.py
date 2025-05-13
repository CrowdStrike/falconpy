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

    def test_connection(self):
        assert HEC.test_connection()

    def test_simple_ingest(self):
        error_check = True
        result = HEC.send_event(simple_payload)
        if result not in AllowedResponses:
            error_check = False

        assert error_check

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
