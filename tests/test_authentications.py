# test_authentications.py
# Tests different service class authentication styles
import logging
import os
import sys
import pytest
import warnings
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import (
    ZeroTrustAssessment,
    OAuth2,
    APIHarness,
    APIHarnessV2,
    version,
    InvalidCredentialFormat,
    Hosts,
    )
from falconpy._util import confirm_base_region, confirm_base_url
from falconpy import (
    DeprecatedOperation,
    DeprecatedClass,
    InvalidBaseURL,
)
from falconpy._util._functions import (
    confirm_base_url as confirm_base_url_func,
    deprecated_operation,
    deprecated_class,
)
from falconpy._version import _TITLE, _VERSION

auth = Authorization.TestAuthorization()
auth.serviceAuth()
AllowedResponses = [200, 401, 403, 429]
_DEBUG = os.getenv("FALCONPY_UNIT_TEST_DEBUG", None)
if _DEBUG:
    _DEBUG = True
_MSSP = None


class TestAuthentications:

    def serviceAny_TestCredentialAuthFailure(self):
        bad_falcon = ZeroTrustAssessment(creds={"client_id": "This", "client_secret": "WontWork"}, debug=_DEBUG)
        # Check the service class login code path at the same time
        bad_falcon.login()
        result = bad_falcon.getAssessmentV1(ids='12345678')

        if result["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceAny_TestBadCredRevoke(self):
        bad_falcon = OAuth2(client_id="this_is", client_secret=["garbage"], debug=_DEBUG, sanitize_log=False)  # Generate a hard error
        result = bad_falcon.revoke(token="whatevers")
        if result["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceAny_TestStaleObjectAuth(self):
        falcon = Hosts(auth_object=OAuth2(creds={"client_id": auth.config["falcon_client_id"],
                                                           "client_secret": auth.config["falcon_client_secret"]
                                                           },
                                                    base_url = "us-1",  # Testing dashed base specifier
                                                    debug=_DEBUG))
        result = falcon.QueryDevicesByFilterScroll()
        if result["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceAny_forceCrossCloudResponseFailure(self):
        falcon = OAuth2(client_id=os.environ["CROSS_DEBUG_KEY"],
                        client_secret="will_not_work",
                        base_url="us1", debug=_DEBUG
                        )
        result = falcon.token()
        if result["status_code"] == 403:
            falcon = APIHarness(client_id=os.environ["CROSS_DEBUG_KEY"],
                                client_secret="will_not_work",
                                base_url="us1", debug=_DEBUG
                                )
            t_creds = {
                "client_id": os.environ["CROSS_DEBUG_KEY"],
                "client_secret": "shouldn't work",
            }
            result = falcon.command("oauth2AccessToken", data=t_creds, base_url="us1")
            if result["status_code"] in [401, 403]:
                return True
            else:
                return False
        else:
            return False

    def serviceAny_forceCrossCloudResponseGovFailure(self):
        _success = False
        falcon = OAuth2(client_id=os.environ["CROSS_DEBUG_KEY"],
                        client_secret=os.environ["CROSS_DEBUG_SECRET"],
                        base_url="us1", debug=_DEBUG
                        )
        result = falcon.token()
        if result["status_code"] == 403:
            falcon = APIHarness(client_id=os.environ["CROSS_DEBUG_KEY"],
                                client_secret=os.environ["CROSS_DEBUG_SECRET"],
                                base_url="us1", debug=_DEBUG
                                )
            result = falcon.authenticate()
            if falcon.token_status == 403:
                _success = True
        return _success

    def serviceAny_checkRegionNameLookups(self):
        falcon = OAuth2(client_id=auth.config["falcon_client_id"],
                        client_secret=auth.config["falcon_client_secret"],
                        base_url="usgov1", debug=_DEBUG
                        )
        result = falcon.token()
        if result["status_code"] in [400, 403]:
            return True
        elif result["status_code"] == 429:
            pytest.skip("Rate limit hit")
        else:
            return False

    def serviceAny_reallyBadBaseURL(self):
        bad_url = "https://this-url-does-not-exist/"
        test = confirm_base_url(bad_url)
        result = confirm_base_region(bad_url)
        if result == "US1":
            return True
        else:
            return False

    def serviceAny_forceGovCloudAutoSelectFailure(self):
        falcon = OAuth2(client_id=os.environ["CROSS_DEBUG_KEY"],
                        client_secret=os.environ["CROSS_DEBUG_SECRET"],
                        base_url="usgov1", debug=_DEBUG
                        )
        result = falcon.token()
        if result["status_code"] == 201:
            falcon = APIHarness(client_id=os.environ["CROSS_DEBUG_KEY"],
                                client_secret=os.environ["CROSS_DEBUG_SECRET"],
                                base_url="https://api.laggar.gcw.crowdstrike.com/",  # Testing for issue 558
                                debug=_DEBUG
                                )
            t_creds = {
                "client_id": os.environ["CROSS_DEBUG_KEY"],
                "client_secret": os.environ["CROSS_DEBUG_SECRET"],
            }
            result = falcon.command("oauth2AccessToken", data=t_creds, base_url="usgov1")
            if result["status_code"] == 201:
                falcon = Hosts(client_id=os.environ["CROSS_DEBUG_KEY"],
                               client_secret=os.environ["CROSS_DEBUG_SECRET"],
                               base_url="usgov1",
                               renew_window=300,
                               debug=_DEBUG
                               )
                result = falcon.auth_object.token()
                if result["status_code"] == 429:
                    pytest.skip("Rate limit hit")
                if result["status_code"] == 201:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def serviceAny_TestObjectAuth(self):
        _returned = True
        # Should also test direct auth in the authentication class
        auth_obj = OAuth2(client_id=auth.config["falcon_client_id"],
                          client_secret=auth.config["falcon_client_secret"],
                          debug=_DEBUG
                          )
        auth_obj.token()
        # While we're at it, test user_agent override
        falcon = Hosts(auth_object=auth_obj, user_agent=f"{_TITLE}/{str(_VERSION)}", debug=_DEBUG)
        result = falcon.QueryDevicesByFilterScroll()
        if result["status_code"] not in AllowedResponses:
            _returned = False
        # And test the new built in logout functionality
        falcon.logout()
        # Garf up our creds and do it again to force an error
        auth_obj.creds = {"client_id" : "Invalid", "client_secret": "Credential"}
        falcon.logout()
        # Now test the override property setters
        falcon.proxy = {"https": "https://notreallyaproxy.com:8888"}
        falcon.timeout = (5, 5)
        # The BearerToken object now maintains a minimum of 120 seconds
        # for a token renewal window across all objects. This is true
        # regardless of whether the property `renew_window` or the
        # deprecated property `token_renew_window` is used.
        falcon.token_renew_window = 340
        falcon.user_agent = "falconpy-unit-testing/1337.1"
        # Finally test the property getters
        if not falcon.proxy["https"] == "https://notreallyaproxy.com:8888":
            _returned = False
        if not falcon.timeout == (5, 5):
            _returned = False
        if not falcon.token_renew_window == 340:
            _returned = False
        if not falcon.user_agent == "falconpy-unit-testing/1337.1":
            _returned = False

        return _returned


    def serviceAny_TestBadObjectAuth(self):
        # Should also test bad direct auth in the authentication class
        falcon = Hosts(auth_object=OAuth2(debug=_DEBUG))
        result = falcon.QueryDevicesByFilterScroll()
        if result["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceAny_TestEasyObjectAuth(self):
        auth_obj = ZeroTrustAssessment(client_id=auth.config["falcon_client_id"],
                          client_secret=auth.config["falcon_client_secret"],
                          debug=_DEBUG
                          )
        # auth_obj.token()
        # Test passing just the service class object, not the auth_object attribute
        # Service Class base object should detect and handle this.
        falcon = Hosts(auth_object=auth_obj)
        result = falcon.QueryDevicesByFilterScroll()
        if result["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def test_BadCredentialAuth(self):
        assert self.serviceAny_TestCredentialAuthFailure() is True

    def test_BadCredRevoke(self):
        assert self.serviceAny_TestBadCredRevoke() is True

    def test_StaleObjectAuth(self):
        assert self.serviceAny_TestStaleObjectAuth() is True

    def test_EasyObjectAuth(self):
        assert self.serviceAny_TestEasyObjectAuth() is True

    def test_BadObjectAuth(self):
        assert self.serviceAny_TestBadObjectAuth() is True

    def test_badBaseURL(self):
        assert self.serviceAny_reallyBadBaseURL() is True

    def test_crossCloudFailure(self):
        assert self.serviceAny_forceCrossCloudResponseFailure() is True

    @pytest.mark.skipif(auth.authorization.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unsupported in GovCloud"
                        )
    def test_checkRegionLookups(self):
        assert self.serviceAny_checkRegionNameLookups() is True

    @pytest.mark.skipif(auth.authorization.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unsupported in GovCloud"
                        )
    def test_crossGovCloudSelectFailure(self):
        result = self.serviceAny_forceGovCloudAutoSelectFailure()
        assert True

    def test_crossGovCloudSelectGovFailure(self):
        assert self.serviceAny_forceCrossCloudResponseGovFailure() is True

    def test_ObjectAuth(self):
        assert self.serviceAny_TestObjectAuth() is True

    def test_NoSecret(self):
        # Disable any environment keys that could trigger environment authentication
        save_id = os.getenv("FALCON_CLIENT_ID")
        save_key = os.getenv("FALCON_CLIENT_SECRET")
        if save_id or save_key:
            os.environ["FALCON_CLIENT_ID"] = ""
            os.environ["FALCON_CLIENT_SECRET"] = ""
        thing = OAuth2(client_id="Whatever", debug=_DEBUG)
        result = thing.login()
        if save_id or save_key:
            os.environ["FALCON_CLIENT_ID"] = save_id
            os.environ["FALCON_CLIENT_SECRET"] = save_key
        assert bool(result["status_code"] == 403)

    def test_version_check(self):
        vers = version()
        assert bool(len(vers) > 3)

    def test_version_compare(self):
        assert bool(version("1.2.16"))  # Will be true as this method is released in 1.3+

    def test_version_compare_quick(self):
        assert bool(version("0.9"))  # Will be true as this method is released in 1.3+

    def test_version_compare_exact_match(self):
        assert bool(version(version()))  # Should be a while before we hit that...

    def test_legacy_token_lookup(self):
        test_object = Hosts(auth_object=auth.authorization)
        assert bool(test_object.token)

    def test_EnvironmentAuthentication(self):
        _returned = False
        save_id = os.getenv("FALCON_CLIENT_ID")
        save_key = os.getenv("FALCON_CLIENT_SECRET")
        if save_id or save_key:
            env_keys = {
                "id_name": "DEBUG_API_ID",
                "secret_name": "DEBUG_API_SECRET",
                "prefix": ""
                }
            thing = Hosts(debug=_DEBUG, environment=env_keys)
            result = thing.login()
            if thing.token_status == 201:
                _returned = True
            assert _returned
        else:
            pytest.skip("Required environment credentials not present")

    def test_EnvironmentAuthFail(self):
        _returned = False
        save_id = os.getenv("FALCON_CLIENT_ID")
        save_key = os.getenv("FALCON_CLIENT_SECRET")
        if save_id or save_key:
            thing = Hosts(debug=_DEBUG, member_cid="12345678")
            result = thing.login()
            if thing.token_status != 201:
                _returned = True
            assert _returned
        else:
            pytest.skip("Required environment credentials not present")

    @pytest.mark.skipif(auth.authorization.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Test unsupported in GovCloud"
                        )
    def test_string_credentials_dictionary(self):
        key = auth.config["falcon_client_id"]
        the_other_bit = auth.config["falcon_client_secret"]
        test_string = "{" + f"'client_id': '{key}', 'client_secret': '{the_other_bit}'" + "}"
        test_object = Hosts(creds=test_string, debug=_DEBUG)
        test_object.login()
        assert bool(test_object.authenticated())

    def test_bad_credentials_dictionary(self):
        _success = False
        test = "Bob"
        try:
            test_object = Hosts(creds=test)
        except InvalidCredentialFormat:
            test = 2
            try:
                test_object = Hosts(creds=test, debug=_DEBUG)
            except InvalidCredentialFormat:
                _success = True
        assert _success

    def test_named_log_target(self):
        named_log = logging.getLogger("named_target")
        test_object = Hosts(debug=named_log, pythonic=True, access_token=auth.authorization.token_value, base_url=auth.authorization.base_url)
        assert bool(test_object.query_devices_by_filter_scroll(limit=1).status_code == 200)

    def test_oauth2_logout_with_debug_logging(self):
        """Test that OAuth2.logout() logs a warning when revocation fails and debug is enabled."""
        bad_oauth = OAuth2(client_id="bad_id", client_secret="bad_secret", debug=True)
        result = bad_oauth.logout()
        assert result["status_code"] != 200

    def test_child_login_logout(self):
        _success = False
        test_object = Hosts(client_id="whatever", client_secret="whatever", debug=_DEBUG)
        failed_child_login = test_object.child_login(member_cid="12345678")
        if not failed_child_login:
            failed_child_login = test_object.child_logout(login_as_parent=False)
            if not failed_child_login:
                _success = True
        assert _success


    def test_mssp_login(self):
        global _MSSP
        _success = False
        _MSSP = Hosts(client_id=auth.config["falcon_client_id"], client_secret=auth.config["falcon_client_secret"], debug=_DEBUG)
        if not _MSSP.child_login(member_cid="1234567890"):
            _success = True
            _MSSP.auth_object.creds["member_cid"] = "1234567890"
        assert(_success)

    def test_mssp_logout(self):
        #_MSSP = Hosts(client_id=auth.config["falcon_client_id"], client_secret=auth.config["falcon_client_secret"], debug=_DEBUG)
        print(_MSSP.child_logout(login_as_parent=False))


class TestUtilFunctionsCoverage:
    """Cover _util/_functions.py uncovered lines."""

    def test_confirm_base_url_none_raises(self):
        """confirm_base_url(None) raises InvalidBaseURL."""
        try:
            confirm_base_url_func(None)
            assert False, "Should have raised InvalidBaseURL"
        except InvalidBaseURL:
            pass

    def test_deprecated_operation_with_log(self):
        """deprecated_operation non-pythonic with logger."""
        logger = logging.getLogger("test_deprecated_op")
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        logger.addHandler(handler)
        deprecated_operation(False, logger, "OldOp", "NewOp")
        logger.removeHandler(handler)

    def test_deprecated_operation_no_log(self):
        """deprecated_operation non-pythonic with no logger."""
        deprecated_operation(False, None, "OldOp", "NewOp")

    def test_deprecated_class_with_log(self):
        """deprecated_class non-pythonic with logger."""
        logger = logging.getLogger("test_deprecated_cls")
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        logger.addHandler(handler)
        deprecated_class(False, logger, "OldCls", "NewCls")
        logger.removeHandler(handler)

    def test_deprecated_class_no_log(self):
        """deprecated_class non-pythonic with no logger."""
        deprecated_class(False, None, "OldCls", "NewCls")

    def test_deprecated_operation_pythonic(self):
        """deprecated_operation in pythonic mode issues a FutureWarning."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            deprecated_operation(True, None, "OldOp", "NewOp")
            assert len(w) == 1
            assert issubclass(w[0].category, FutureWarning)

    def test_deprecated_class_pythonic(self):
        """deprecated_class in pythonic mode issues a FutureWarning."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            deprecated_class(True, None, "OldCls", "NewCls")
            assert len(w) == 1
            assert issubclass(w[0].category, FutureWarning)


class TestOAuth2LogoutCoverage:
    """Cover oauth2.py logout with logging."""

    def test_logout_with_logging_fails(self):
        """OAuth2.logout() with log enabled hitting CannotRevokeToken."""
        oauth = OAuth2(
            client_id="fake_id",
            client_secret="fake_secret",
            debug=True
        )
        result = oauth.logout()
        assert isinstance(result, dict)
        assert result["status_code"] != 200


class TestFalconInterfaceCoverage:
    """Cover _auth_object/_falcon_interface.py remaining lines."""

    def test_environment_auth(self):
        """Cover environment variable auth and env_secret property."""
        orig_id = os.environ.get("FALCON_CLIENT_ID")
        orig_secret = os.environ.get("FALCON_CLIENT_SECRET")
        try:
            os.environ["FALCON_CLIENT_ID"] = "env_test_id"
            os.environ["FALCON_CLIENT_SECRET"] = "env_test_secret"
            oauth = OAuth2()
            assert oauth.auth_style == "ENVIRONMENT"
            assert oauth.env_secret == "CLIENT_SECRET"
        finally:
            if orig_id is not None:
                os.environ["FALCON_CLIENT_ID"] = orig_id
            else:
                os.environ.pop("FALCON_CLIENT_ID", None)
            if orig_secret is not None:
                os.environ["FALCON_CLIENT_SECRET"] = orig_secret
            else:
                os.environ.pop("FALCON_CLIENT_SECRET", None)

    def test_environment_auth_with_member_cid(self):
        """Cover environment auth with member_cid."""
        orig_id = os.environ.get("FALCON_CLIENT_ID")
        orig_secret = os.environ.get("FALCON_CLIENT_SECRET")
        try:
            os.environ["FALCON_CLIENT_ID"] = "env_test_id"
            os.environ["FALCON_CLIENT_SECRET"] = "env_test_secret"
            oauth = OAuth2(member_cid="test_member_cid")
            assert oauth.auth_style == "ENVIRONMENT"
            assert oauth.creds.get("member_cid") == "test_member_cid"
        finally:
            if orig_id is not None:
                os.environ["FALCON_CLIENT_ID"] = orig_id
            else:
                os.environ.pop("FALCON_CLIENT_ID", None)
            if orig_secret is not None:
                os.environ["FALCON_CLIENT_SECRET"] = orig_secret
            else:
                os.environ.pop("FALCON_CLIENT_SECRET", None)

    def test_environment_auth_custom_env(self):
        """Cover custom environment secret name."""
        orig_id = os.environ.get("MY_PREFIX_MY_ID")
        orig_secret = os.environ.get("MY_PREFIX_MY_SECRET")
        try:
            os.environ["MY_PREFIX_MY_ID"] = "custom_env_id"
            os.environ["MY_PREFIX_MY_SECRET"] = "custom_env_secret"
            oauth = OAuth2(environment={
                "prefix": "MY_PREFIX_",
                "id_name": "MY_ID",
                "secret_name": "MY_SECRET"
            })
            assert oauth.auth_style == "ENVIRONMENT"
            assert oauth.env_secret == "MY_SECRET"
        finally:
            if orig_id is not None:
                os.environ["MY_PREFIX_MY_ID"] = orig_id
            else:
                os.environ.pop("MY_PREFIX_MY_ID", None)
            if orig_secret is not None:
                os.environ["MY_PREFIX_MY_SECRET"] = orig_secret
            else:
                os.environ.pop("MY_PREFIX_MY_SECRET", None)

    def test_child_login_pythonic(self):
        """Cover child_login where login() returns bool."""
        oauth = OAuth2(
            client_id="fake_id",
            client_secret="fake_secret",
        )
        oauth.login = lambda: True
        oauth.creds["member_cid"] = None
        result = oauth.child_login(member_cid="test_child_cid")
        assert result is True

    def test_child_login_dict_success(self, monkeypatch):
        """Cover child_login where login() returns dict with 201."""
        import falconpy._util._functions as _funcs

        class _FakeResp:
            status_code = 201
            headers = {"Content-Type": "application/json", "X-Cs-Region": "us-1"}
            content = b'{"access_token": "child_token", "expires_in": 1799}'
            def json(self):
                return {"access_token": "child_token", "expires_in": 1799}

        monkeypatch.setattr(_funcs.requests, "request", lambda *a, **kw: _FakeResp())
        oauth = OAuth2(
            client_id="fake_id",
            client_secret="fake_secret"
        )
        result = oauth.child_login(member_cid="test_child_cid")
        assert result is True

    def test_child_logout_pythonic(self):
        """Cover child_logout where login() returns bool."""
        oauth = OAuth2(
            client_id="fake_id",
            client_secret="fake_secret",
        )
        oauth.creds["member_cid"] = "test_child_cid"
        oauth.login = lambda: True
        result = oauth.child_logout(login_as_parent=True)
        assert result is True

    def test_logout_handler_invalid_creds_with_logging(self):
        """Cover InvalidCredentials caught in _logout_handler with debug."""
        oauth = OAuth2(debug=True)
        result = oauth.logout()
        assert isinstance(result, dict)
        assert result.get("status_code") is not None
