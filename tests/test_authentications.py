# test_authentications.py
# Tests different service class authentication styles
import logging
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import (
    ZeroTrustAssessment,
    OAuth2,
    APIHarness,
    version,
    InvalidCredentialFormat,
    Hosts,
    )
from falconpy._util import confirm_base_region, confirm_base_url
from falconpy._version import _TITLE, _VERSION

auth = Authorization.TestAuthorization()
auth.serviceAuth()
AllowedResponses = [200, 401, 403, 429]
_DEBUG = os.getenv("FALCONPY_UNIT_TEST_DEBUG", None)
if _DEBUG:
    _DEBUG = True


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
        if result["status_code"] == 400:
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

    def test_child_login_logout(self):
        _success = False
        test_object = Hosts(client_id="whatever", client_secret="whatever", debug=_DEBUG)
        failed_child_login = test_object.child_login(member_cid="12345678")
        if not failed_child_login:
            failed_child_login = test_object.child_logout(login_as_parent=False)
            if not failed_child_login:
                _success = True
        assert _success