"""
test_api_request.py -  This class tests the APIRequest class
"""
import os
import sys
import logging
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
from falconpy import (
    LogFacility,
    APIRequest,
    APIError,
    RequestValidator,
    FalconInterface,
    InterfaceConfiguration
    )
from falconpy._result._base_dictionary import UnsupportedPythonVersion

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()

_OBJECT: APIRequest = None
_RATE_LIMITED: bool = False
not_supported = pytest.mark.skipif(
    sys.version_info.minor <= 7, reason="Experimental functionality unavailable in this version of Python."
)
experimental = pytest.mark.xfail
some_log = logging.basicConfig(level=logging.DEBUG)


class TestAPIRequest:
    """
    APIRequest Class test harness
    """

    @not_supported
    def test_falcon_interface_config_change(self):
        interface = FalconInterface(client_id="whatever", client_secret="whatever")
        interface_config = InterfaceConfiguration(base_url="https://someplace.shiny.com", proxy={"https": "https://my.proxy.com:8080"}, timeout=42, user_agent="agent-bob/1.2.3", ssl_verify=False)
        interface.config = interface_config
        assert bool(interface.base_url == "https://someplace.shiny.com")

    @not_supported
    def test_api_request_generic_object(self):
        global _OBJECT, _RATE_LIMITED
        log_facility = LogFacility()
        initializer = {
            "log_util": some_log,
            "debug_record_count": 150,
            "sanitize": True,
            "body_validator": {"Something": str},
            "body_required": ["Something"]
        }
        try:
            _ = APIRequest(endpoint="/somewhere/sunny/with/a/beach") # Throw away to test a generic
            _OBJECT = APIRequest(endpoint="/somewhere/out/there", initializer=initializer)
        except APIError as api_error:
            if api_error.code == 429:
                _RATE_LIMITED = True
                pytest.skip("Rate limited")
        assert bool(isinstance(_OBJECT, APIRequest))

    @not_supported
    def test_api_request_properties(self):
        global _OBJECT, _RATE_LIMITED
        valid = {"Nothing": str}
        valid_required = ["Nothing"]
        new_validator = RequestValidator(validator=valid, required=valid_required)
        _success = True
        try:
            _OBJECT.meta.debug_headers = {"TheseHeaders":"Are not real"}
            _OBJECT.meta.endpoint = "/somewhere/else/out/there"
            _OBJECT.meta.method = "POST"
            _OBJECT.payloads.body = {"some_key": "some_value"}
            _OBJECT.payloads.data = {"some_data_key": "some_data_value"}
            _OBJECT.payloads.params = {"some_param_key": "some_param_value"}
            _OBJECT.payloads.files = [("somefile.ext", ("MyFile", "FILEDATAGOESHERE", "application/octet-stream"))]
            _OBJECT.connection.proxy = {"https": "https://some.proxy.com:8088"}
            _OBJECT.connection.timeout = (30, 90)
            _OBJECT.connection.user_agent = "not-a-real-agent/1.2.3"
            _OBJECT.behavior.authenticating = False
            _OBJECT.behavior.container = True
            _OBJECT.behavior.expand_result = True
            _OBJECT.behavior.perform = True
            _OBJECT.request_log.debug_record_count = 200
            _OBJECT.request_log.sanitize_log = False
            _OBJECT.behavior.stream = True
            if _OBJECT.behavior.body_required[0] != "Something":
                _success = False
            if _OBJECT.behavior.body_validator["Something"] != str:
                _success = False
            _OBJECT.behavior.validator = new_validator
            if _OBJECT.behavior.body_required[0] != "Nothing":
                _success = False
            if _OBJECT.behavior.body_validator["Nothing"] != str:
                _success = False
            new_validator.required = ["Somewhere"]
            new_validator.validator = {"Somewhere": dict}
            _OBJECT.behavior.validator = new_validator
            if _OBJECT.behavior.body_required[0] != "Somewhere":
                _success = False
            if _OBJECT.behavior.body_validator["Somewhere"] != dict:
                _success = False
            if _OBJECT.meta.debug_headers["TheseHeaders"] != "Are not real":
                _success = False
            if _OBJECT.meta.endpoint != "/somewhere/else/out/there":
                _success = False
            if _OBJECT.meta.method != "POST":
                _success = False
            if _OBJECT.payloads.body["some_key"] != "some_value":
                _success = False
            if _OBJECT.payloads.data["some_data_key"] != "some_data_value":
                _success = False
            if _OBJECT.payloads.params["some_param_key"] != "some_param_value":
                _success = False
            if _OBJECT.payloads.files[0][1][0] != "MyFile":
                _success = False
            if _OBJECT.connection.proxy["https"] != "https://some.proxy.com:8088":
                _success = False
            if _OBJECT.connection.timeout[1] != 90:
                _success = False
            if _OBJECT.connection.user_agent != "not-a-real-agent/1.2.3":
                _success = False
            if _OBJECT.behavior.authenticating:
                _success = False
            if not _OBJECT.behavior.container:
                _success = False
            if not _OBJECT.behavior.expand_result:
                _success = False
            if not _OBJECT.behavior.perform:
                _success = False
            if _OBJECT.request_log.debug_record_count != 200:
                _success = False
            if _OBJECT.request_log.sanitize_log:
                _success = False
            if not _OBJECT.behavior.stream:
                _success = False
        except APIError as api_error:
            if api_error.code == 429:
                _RATE_LIMITED = True
                pytest.skip("Rate limited")
        assert _success
