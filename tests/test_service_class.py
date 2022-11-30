"""
test_results.py -  This class tests Service Class functionality
"""
import os
import sys
from time import time

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
    FalconInterface,
    ServiceClass
    )

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
AllowedResponses = [200, 202, 429]  # Adding rate-limiting as an allowed response for now
_OBJECT: OAuth2 = None
_CLEAN: Hosts = None
_DEBUG = os.getenv("FALCONPY_UNIT_TEST_DEBUG", None)
if _DEBUG:
    _DEBUG = True


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

    def test_log_setup(self):
        global _OBJECT
        # Create an auth object with debug enabled
        _OBJECT = OAuth2(creds=config.creds, debug=True)
        # Force it off in a regular Service Class
        debug_off = Hosts(auth=_OBJECT, debug=False)
        # Force it back on with another Service Class (and disable sanitization)
        debug_back_on = Hosts(auth=debug_off.auth_object, debug=True, debug_record_count=42, sanitize=False)
        # Change the debug record count while we're here
        debug_back_on.debug_record_count = 1
        assert bool(debug_back_on.debug
                    and debug_back_on.debug_record_count == 1
                    and not debug_off.debug
                    and debug_back_on.log  # Confirm the property
                    and _OBJECT.sanitize_log
                    )

    def test_property_debug_record_count(self):
        global _CLEAN
        _CLEAN = Hosts(creds=config.creds, user_agent="clean/1.0", timeout=120, proxy={})
        assert bool(_CLEAN.debug_record_count)

    def test_property_refreshable(self):
        assert bool(_CLEAN.refreshable)
    
    def test_property_token_fail_reason(self):
        assert bool(not _CLEAN.token_fail_reason)

    def test_property_token_status(self):
        assert bool(_CLEAN.token_status)
    
    def test_property_headers(self):
        assert bool(_CLEAN.headers)
    
    def test_property_user_agent(self):
        assert bool(_CLEAN.user_agent)

    def test_property_user_agent_setter(self):
        _CLEAN.user_agent = "XYZZY"
        assert bool(_CLEAN.user_agent == "XYZZY")

    def test_property_renew_window(self):
        assert bool(_CLEAN.renew_window)

    def test_property_renew_window_setter(self):
        _CLEAN.renew_window = 1137
        assert bool(_CLEAN.renew_window == 1137)

    def test_property_timeout(self):
        assert bool(_CLEAN.timeout)

    def test_property_timeout_setter(self):
        _CLEAN.timeout = (42,378)
        assert bool(_CLEAN.timeout[0] == 42 and _CLEAN.timeout[1] == 378)

    def test_property_proxy(self):
        assert bool(not _CLEAN.proxy)

    def test_property_proxy_setter(self):
        _CLEAN.proxy = {"https": "https://we-stop-breaches:8000"}
        _returned = bool(_CLEAN.proxy["https"] == "https://we-stop-breaches:8000")
        assert bool(_returned)

    def test_disable_ssl_verify_dynamic(self):
        _CLEAN.ssl_verify = False
        assert bool(not _CLEAN.ssl_verify)

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
            

    def test_auth_object_direct_change(self):
        _DIRECT: ExtremelyThinServiceClass = ExtremelyThinServiceClass(
            client_id=os.getenv("DEBUG_API_ID"),
            client_secret=os.getenv("DEBUG_API_SECRET"),
            proxy={"CrowdStrike": "WE STOP BREACHES WITH PYTHON"},
            timeout=1137,
            renew_window=333,
            user_agent="crowdstrike-testing/5.4.2",
            debug=_DEBUG
            )

        assert bool(_DIRECT.headers
                    and _DIRECT.timeout
                    and _DIRECT.renew_window
                    and _DIRECT.user_agent
                    and "WITH PYTHON" in _DIRECT.proxy["CrowdStrike"]
                     )

    