"""
test_results.py -  This class tests Service Class functionality
"""
import os
import sys
import pytest
from json import loads
from time import time
import logging
from random import randrange
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import (
    Hosts,
    OAuth2,
    BaseServiceClass,
    FunctionalityNotImplemented,
    SSLDisabledWarning,
    APIError,
    SDKError,
    NoAuthenticationMechanism,
    Result,
    ExpandedResult,
    InvalidBaseURL,
    Workflows
    )

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
AllowedResponses = [200, 202, 401, 429]  # Adding rate-limiting as an allowed response for now
_OBJECT: OAuth2 = None
_CLEAN: Hosts = None
_HOSTS: Hosts = None
_DEBUG = os.getenv("FALCONPY_UNIT_TEST_DEBUG", None)
if _DEBUG:
    _DEBUG = True
_RATE_LIMITED: bool = False
rate_limited = pytest.mark.skipif(
    _RATE_LIMITED, reason="Rate limit met, skipping"
)
not_supported = pytest.mark.skipif(
    sys.version_info.minor <= 7, reason="Experimental functionality unavailable in this version of Python."
)
class SimpleServiceClass(BaseServiceClass):
    """I'm just here to test extensibility."""

    def init(self, access_token, proxy, timeout, renew_window, user_agent):
        super().__init__(access_token=access_token,
                         proxy=proxy,
                         timeout=timeout,
                         renew_window=renew_window,
                         user_agent=user_agent,
                         debug=_DEBUG
                         )

    def login(self):
        raise FunctionalityNotImplemented(message="I would say something funny here")

    def logout(self):
        raise FunctionalityNotImplemented(message="but unfortunately that's not yet implemented.")


class ExtremelyThinServiceClass(BaseServiceClass):
    """I'm just here to test extensibility."""

    def init(self, client_id, client_secret, proxy, timeout, renew_window, user_agent):
        super().__init__(client_id=client_id,
                         client_secret=client_secret,
                         proxy=proxy,
                         timeout=timeout,
                         renew_window=renew_window,
                         user_agent=user_agent,
                         debug=_DEBUG
                         )

    def login(self):
        raise FunctionalityNotImplemented(message="I would say something funny here")

    def logout(self):
        raise FunctionalityNotImplemented(message="but unfortunately that's not yet implemented.")


class TestServiceClass:
    """Service Class test harness."""

    @rate_limited
    @not_supported
    def test_log_setup(self):
        global _OBJECT
        # Create an auth object with debug enabled
        _OBJECT = OAuth2(creds=config.creds, debug=True)
        if _OBJECT.token_status == 429:
            global _RATE_LIMITED  # Don't think this will actually get hit
            _RATE_LIMITED = True
        # Force it off in a regular Service Class
        debug_off = Hosts(auth=_OBJECT, debug=False)
        # Force it back on with another Service Class (and disable sanitization)
        debug_back_on = Hosts(auth=debug_off.auth_object, debug=True, debug_record_count=42, sanitize_log=False)
        # Change the debug record count while we're here
        debug_back_on.debug_record_count = 1
        debug_off.sanitize_log = True
        debug_back_on.sanitize_log = True
        assert bool(debug_back_on.debug
                    and debug_back_on.debug_record_count == 1
                    and not debug_off.debug
                    and debug_back_on.log  # Confirm the property
                    and _OBJECT.sanitize_log
                    and debug_back_on.sanitize_log
                    )

    @rate_limited
    @not_supported
    def test_property_debug_record_count(self):
        global _CLEAN
        _CLEAN = Hosts(creds=config.creds, user_agent="clean/1.0", timeout=120, proxy={}, base_url=config.base_url)
        if _CLEAN.token_status == 429:
            global _RATE_LIMITED
            _RATE_LIMITED = True

        assert bool(_CLEAN.debug_record_count)

    @rate_limited
    @not_supported
    def test_service_class_context_manager(self):
        _success = False
        with _CLEAN as sdk:
            if sdk.query_devices()["status_code"] == 200:
                _success = True
        assert _success

    @rate_limited
    @not_supported
    def test_service_class_context_manager_with_pythonic_error(self):
        _success = False
        new_sdk = Workflows(creds=config.creds, base_url=config.base_url, pythonic=True, debug=True)
        try:
            with new_sdk as sdk:
                result = sdk.import_definition(data_file="InvalidDataFile")
                raise SDKError(code=500, message="Unit testing")
        except SDKError:
            _success = True
        assert _success

    @rate_limited
    @not_supported
    def test_property_refreshable(self):
        assert bool(_CLEAN.refreshable)

    @rate_limited
    @not_supported
    def test_property_token_fail_reason(self):
        _CLEAN.login()
        assert bool(not _CLEAN.token_fail_reason or "Region autodiscovery failure" in _CLEAN.token_fail_reason)

    @rate_limited
    @not_supported
    def test_property_token_status(self):
        assert bool(_CLEAN.token_status)

    @rate_limited
    @not_supported
    def test_property_headers(self):
        assert bool(_CLEAN.headers)

    @rate_limited
    @not_supported
    def test_property_user_agent(self):
        assert bool(_CLEAN.user_agent)

    @rate_limited
    @not_supported
    def test_property_user_agent_setter(self):
        _CLEAN.user_agent = "XYZZY"
        assert bool(_CLEAN.user_agent == "XYZZY")

    @rate_limited
    @not_supported
    def test_property_renew_window(self):
        assert bool(_CLEAN.renew_window)

    @rate_limited
    @not_supported
    def test_property_renew_window_setter(self):
        _CLEAN.renew_window = 1137
        assert bool(_CLEAN.renew_window == 1137)

    @rate_limited
    @not_supported
    def test_property_timeout(self):
        assert bool(_CLEAN.timeout)

    @rate_limited
    @not_supported
    def test_property_timeout_setter(self):
        _CLEAN.timeout = (42,378)
        assert bool(_CLEAN.timeout[0] == 42 and _CLEAN.timeout[1] == 378)

    @rate_limited
    @not_supported
    def test_property_proxy(self):
        assert bool(not _CLEAN.proxy)

    @rate_limited
    @not_supported
    def test_property_proxy_setter(self):
        _CLEAN.proxy = {"https": "https://we-stop-breaches:8000"}
        _returned = bool(_CLEAN.proxy["https"] == "https://we-stop-breaches:8000")
        assert bool(_returned)

    @rate_limited
    @not_supported
    def test_disable_ssl_verify_dynamic(self):
        _CLEAN.ssl_verify = False
        assert bool(not _CLEAN.ssl_verify)


    @rate_limited
    @not_supported
    def test_property_base_service_class_proxy(self):
        _OBJECT.login()
        _SIMPLE: SimpleServiceClass = SimpleServiceClass(
            access_token=_OBJECT.token_value,
            proxy={"CrowdStrike": "WE STOP BREACHES"},
            timeout=(42,99),
            renew_window=777,
            user_agent="crowdstrike-falconpy-base-testing/1.2.3",
            debug_record_count=43,
            debug=_DEBUG
            )
        _success = False
        try:
            _SIMPLE.user_agent = "this-is-different/3.0"
            _SIMPLE.proxy = {"CrowdStrike" : "STILL STOPPING BREACHES"}
            _SIMPLE.renew_window = 1234
            _SIMPLE.debug_record_count = 42
            _SIMPLE.timeout = (100, 101)

        except FunctionalityNotImplemented:
            # Should crash because we're inheriting the base
            # he doesn't implement a setter for proxy or user_agent
            _success = True

        assert bool(_success)
        #assert _success
            
    @rate_limited
    @not_supported
    def test_auth_object_direct_change(self):
        _right_error = False
        _DIRECT: ExtremelyThinServiceClass = ExtremelyThinServiceClass(
            client_id=os.getenv("DEBUG_API_ID"),
            client_secret=os.getenv("DEBUG_API_SECRET"),
            proxy={"CrowdStrike": "WE STOP BREACHES WITH PYTHON"},
            timeout=1137,
            renew_window=333,
            user_agent="crowdstrike-testing/5.4.2",
            debug=_DEBUG
            )
        try:
            _DIRECT.proxy = {"CrowdStrike": "WE STOP BREACHES"}
        except FunctionalityNotImplemented:
            _right_error = True
        assert bool(_DIRECT.headers
                    and _DIRECT.timeout
                    and _DIRECT.renew_window
                    and _DIRECT.user_agent
                    and "WITH PYTHON" in _DIRECT.proxy["CrowdStrike"]
                    and _right_error
                     )

    @rate_limited
    @not_supported
    def test_auth_object_pythonic_failure(self):
        # Disable any environment keys that could trigger environment authentication
        save_id = os.getenv("FALCON_CLIENT_ID")
        save_key = os.getenv("FALCON_CLIENT_SECRET")
        if save_id or save_key:
            os.environ["FALCON_CLIENT_ID"] = ""
            os.environ["FALCON_CLIENT_SECRET"] = ""

        with pytest.warns(NoAuthenticationMechanism):
            _will_fail = OAuth2(debug=_DEBUG, pythonic=True)
            _will_fail.proxy = {"CrowdStrike": "WE STOP BREACHES"}
            _will_fail.timeout = (18, 42)
            _will_fail.user_agent = "crowdstrike-testing/1.2.3"
            _will_fail.debug_record_count = 142
            _will_fail.sanitize_log = True
            _will_fail.token_time = time()
            _will_fail.token_fail_reason = "Just Because"
            _will_fail.token_value = "no cash value"
            _will_fail.pythonic = True

        if save_id or save_key:
            os.environ["FALCON_CLIENT_ID"] = save_id
            os.environ["FALCON_CLIENT_SECRET"] = save_key


        assert (_will_fail.config
                and _will_fail.proxy["CrowdStrike"] == "WE STOP BREACHES"
                and _will_fail.timeout[1] == 42
                and "crowdstrike" in _will_fail.user_agent
                and _will_fail.debug_record_count == 142
                and _will_fail.sanitize_log
                )

    @rate_limited
    @not_supported
    def test_auth_object_invalid_config(self):
        _success = False
        _thing = OAuth2(creds=config.creds, debug=_DEBUG)
        try:
            _thing.config = {"This really should": "not work"}
        except ValueError:
            if _thing.log:
                _thing.log.error("Invalid value specified for Interface Configuration")
            _success = True

        assert _success

    @rate_limited
    @not_supported
    def test_log_facility_shutdown(self):
        _thing = OAuth2(creds=config.creds, debug=True)
        _thing.login()
        _active = _thing.log_facility.active
        if (_thing.authenticated() and not _thing.token_expired()) or _active:  # Duplicative, testing methods
            #if _thing.log_facility.active:
            _thing.log_facility.deactivate_log()

        assert not _thing.log

    @rate_limited
    @not_supported
    def test_truly_ridiculous_base_url(self):
        _exploding_banana: logging.Logger = logging.getLogger(__name__)
        try:
            _ = OAuth2(creds=config.creds, debug=_DEBUG, base_url=_exploding_banana)
        except InvalidBaseURL as bad_base:
            _OBJECT.log.error(bad_base.message)
            _success = True

        assert _success

    @rate_limited
    @not_supported
    def test_legacy_result_expansion(self):
        global _HOSTS
        _HOSTS = Hosts(creds=config.creds, debug=_DEBUG)
        _result = _HOSTS.query_devices(limit=1)
        _expanded_result = ExpandedResult()(status_code=_result["status_code"],
                                            headers=_result["headers"],
                                            content={"body": _result["body"]}
                                            )

        assert bool(_expanded_result[0] in AllowedResponses and _expanded_result[1])

    @rate_limited
    @not_supported
    def test_raw_result_repr(self):
        _raw_face = {"access_token": {"CrowdStrike": "WE STOP BREACHES"}}
        _raw_result = Result(status_code=200, headers={"Random": "HeaderThing"}, body=_raw_face)
        # Force it thru the repr method
        assert loads(str(_raw_result).replace("'", '"'))["body"]["access_token"]["CrowdStrike"] == "WE STOP BREACHES"

    @rate_limited
    @not_supported
    def test_list_response_component_get_property(self):
        with pytest.warns(SSLDisabledWarning):
            _no_ssl = Hosts(creds=config.creds, pythonic=True, debug=_DEBUG, ssl_verify=False)
            # if _no_ssl.base_url == "https://api.laggar.gcw.crowdstrike.com":
            #     pytest.skip("SSL required for GovCloud testing.")
            try:
                _thing: Result = _no_ssl.query_devices(limit=3)
            except APIError:
                pytest.skip("SSL required for GovCloud testing.")
            # Check log sanitization code path
            _HOSTS.sanitize_log = False
            _HOSTS.query_devices(limit=1)
            _HOSTS.sanitize_log = True
            # Revoke the dirty token
            _HOSTS.logout()

        position = randrange(0, len(_thing.resources), 1)
        assert bool(_thing.resources.get_property(position) == _thing.resources[position])


    @rate_limited
    @not_supported
    def test_list_response_component_get_property_fail(self):
        position = 5
        _success = False
        if config.base_url != "https://api.laggar.gcw.crowdstrike.com":
            with pytest.warns(SSLDisabledWarning):
                _no_ssl = Hosts(creds=config.creds, pythonic=True, debug=_DEBUG, ssl_verify=False)
                if _no_ssl.token_status == 403:
                    pytest.skip("SSL required for GovCloud testing.")
                try:
                    if _no_ssl.token_valid and not _no_ssl.token_stale:  # Duplicative, just testing the properties
                        _thing: Result = _no_ssl.query_devices(limit=3)
                except APIError:
                    pytest.skip("SSL required for GovCloud testing.")
        else:
            pytest.skip("This test is unsupported in this region.")

        try:
            _success = bool(_thing.resources.get_property(position))
        except IndexError:
            _success = True

        assert(_success)
