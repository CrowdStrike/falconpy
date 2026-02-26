# test_uber_api_complete.py
# This class tests the uber class

import json
import os
import sys
import pytest
import datetime
import hashlib
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# flake8: noqa=E402
# pylint: disable=C0103
# Classes to test - manually imported from our sibling folder
from falconpy import APIHarness, APIError
# Import perform_request from _util so we can test generating 405's directly
from falconpy._util import perform_request, force_default
from tests import test_authorization as Authorization


AllowedResponses = [200, 400, 401, 403, 404, 405, 415, 418, 429]
_DEBUG = os.getenv("FALCONPY_UNIT_TEST_DEBUG", None)
if _DEBUG:
    _DEBUG = True
if "DEBUG_API_ID" in os.environ and "DEBUG_API_SECRET" in os.environ:
    config = {}
    config["falcon_client_id"] = os.getenv("DEBUG_API_ID")
    config["falcon_client_secret"] = os.getenv("DEBUG_API_SECRET")
    if "DEBUG_API_BASE_URL" in os.environ:
        config["falcon_base_url"] = os.getenv("DEBUG_API_BASE_URL")
    else:
        config["falcon_base_url"] = "us1"
else:
    cur_path = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists('%s/test.config' % cur_path):
        with open('%s/test.config' % cur_path, 'r') as file_config:
            config = json.loads(file_config.read())
    else:
        sys.exit(1)

falcon = APIHarness(
    client_id=config["falcon_client_id"],
    client_secret=config["falcon_client_secret"],
    base_url=config["falcon_base_url"], debug=_DEBUG
    )


class TestUber:
    def uberCCAWS_GetAWSSettings(self):
        if falcon.command("GetAWSSettings")["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_QueryAWSAccounts(self):
        if falcon.command("QueryAWSAccounts", parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_GetAWSAccounts(self):
        try:
            id_lookup = falcon.command("QueryAWSAccounts", parameters={"limit": 1})
            if id_lookup["body"]["resources"]:
                id_list = id_lookup["body"]["resources"][0]["id"]
            else:
                id_list = "123456789012"
            if falcon.command("GetAWSAccounts", ids=id_list)["status_code"] in AllowedResponses:
                return True
            else:
                return False
        except KeyError:
            pytest.skip("Workflow-related error, skipping")
            return True

    def uberCCAWS_VerifyAWSAccountAccess(self):
        try:
            id_list = falcon.command("QueryAWSAccounts", parameters={"limit": 1})["body"]["resources"][0]["id"]
            if falcon.command("VerifyAWSAccountAccess", ids=id_list)["status_code"] in AllowedResponses:
                return True
            else:
                return False
        except KeyError:
            pytest.skip("Workflow-related error, skipping")
            return True

    # Intentionally specifying this incorrectly to test the failure code path
    @force_default(defaults=["params"], default_types=[""])
    def uberCCAWS_QueryAWSAccountsForIDs(self, params: dict = None):
        if falcon.command("QueryAWSAccountsForIDs", parameters=params)["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_TestUploadDownload(self):
        FILENAME = "tests/testfile.png"
        fmt = '%Y-%m-%d %H:%M:%S'
        stddate = datetime.datetime.now().strftime(fmt)
        sdtdate = datetime.datetime.strptime(stddate, fmt)
        sdtdate = sdtdate.timetuple()
        jdate = sdtdate.tm_yday
        jdate = "{}{}".format(stddate.replace("-", "").replace(":", "").replace(" ", ""), jdate)
        SOURCE = "%s_source.png" % jdate
        TARGET = "tests/%s_target.png" % jdate
        PAYLOAD = open(FILENAME, 'rb').read()
        response = falcon.command('UploadSampleV3', file_name=SOURCE, data=PAYLOAD, content_type="application/octet-stream")
        try:
            if response["status_code"] == 429:
                pytest.skip("Rate limit hit")
            if response["body"]["resources"]:
                sha = response["body"]["resources"][0]["sha256"]
            else:
                pytest.skip("Rate limit hit")
            response = falcon.command("GetSampleV3", ids=sha)
            try:
                open(TARGET, 'wb').write(response)
            except TypeError:
                return True
            buf = 65536
            hash1 = hashlib.sha256()
            with open(FILENAME, 'rb') as f:
                while True:
                    data = f.read(buf)
                    if not data:
                        break
                    hash1.update(data)
            hash1 = hash1.hexdigest()
            hash2 = hashlib.sha256()
            with open(TARGET, 'rb') as f:
                while True:
                    data = f.read(buf)
                    if not data:
                        break
                    hash2.update(data)
            hash2 = hash2.hexdigest()
            if os.path.exists(TARGET):
                os.remove(TARGET)
            _ = falcon.command("DeleteSampleV3", ids=sha)
            if hash1 == hash2:
                return True
            else:
                return False
        except KeyError:
            # Flaky
            pytest.skip("Workflow-related error, skipping")
            return True

    def uberCCAWS_GenerateError(self):
        if falcon.command("QueryDetects", partition=0)["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_GenerateInvalidPayload(self):
        if falcon.command("refreshActiveStreamSession", partition=9,
                          parameters={"action_name": "refresh_active_stream_session"})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_OverrideAndHeader(self):
        if falcon.command(override="GET,/detects/queries/detects/v1",
                          headers={"Nothing": "Special"})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberContainer_TestBodyIDsPayload(self):
        successful = False
        if falcon.authenticated and not falcon.token_expired():
            if falcon.command("GetDeviceDetails", ids="12345678")["status_code"] in AllowedResponses:
                successful = True

        return successful

    def uberCCAWS_TestMSSP(self):
        if falcon.command("QueryDetects", limit=1)["status_code"] == 429:
            pytest.skip("Rate limit hit")
        falcon.creds["member_cid"] = "1234567890ABCDEFG"
        if not falcon.authenticate():
            returned = True
        else:
            returned = False
        falcon.creds.pop("member_cid")

        return returned

    def uberCCAWS_BadMethod(self):
        if falcon.command(action="", override="BANANA,/detects/queries/detects/v1",
                          headers={"Nothing": "Special"})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_BadCommand(self):
        if falcon.command(action="IWantTheImpossible", parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_GenerateServerError(self):
        if falcon.command("GetDetectSummaries", ids="123", data=['Kerash!'])["status_code"] == 500:
            return True
        else:
            return False

    @force_default(defaults=["params"])  # Intentionally specifying this incorrectly to test the failure code path
    def uberCCHosts_GenerateActionNameError(self, params: dict = None):
        if falcon.command("PerformActionV2",
                          parameters=params,
                          body={},
                          action_name="Squish"
                          )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_GenerateInvalidOperationIDError(self):
        if perform_request(method="FETCH", endpoint="/somewhere/interesting", debug=_DEBUG, log_util=falcon.log)["status_code"] in AllowedResponses:
            return True
        else:
            return False

    # Token revocation is returning a 200 regardless of the token we send.
    # Changed to client ID on 08.02.21 - jshcodes@CrowdStrike
    def uberCCAWS_GenerateTokenError(self):
        #hold_token = falcon.token
        #falcon.token = "I am a bad token!"
        hold_id = falcon.creds["client_id"]
        falcon.creds["client_id"] = "Gonna Crash"
        if not falcon.deauthenticate():
            returned = True
        else:
            returned = False
        falcon.creds["client_id"] = hold_id

        return returned

    def uberCCAWS_BadAuthentication(self):
        falcon = APIHarness(debug=_DEBUG)
        if falcon.command("QueryDetects", parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uberCCAWS_DisableSSLVerify(self):
        falcon = APIHarness(
            creds={
                "client_id": config["falcon_client_id"],
                "client_secret": config["falcon_client_secret"]
            }, ssl_verify=False, base_url=config["falcon_base_url"], debug=_DEBUG
        )
        if falcon.command("QueryDetects", parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uber_test_invalid_reserved_word_payload(self):
        params = {
            filter:"hostname:'falconpy-unit-testing'"
        }
        if falcon.command("QueryDevicesByFilter", parameters=params)["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def uber_test_distinct_field(self):
        if falcon.command("querySensorUpdateKernelsDistinct", distinct_field="flavor")["status_code"] in AllowedResponses:
            return True
        else:
            return False

    # def test_GetAWSSettings(self):
    #     assert self.uberCCAWS_GetAWSSettings() is True

    def test_reserved_words(self):
        assert self.uber_test_invalid_reserved_word_payload() is True

    def test_distinct_field(self):
        assert self.uber_test_distinct_field() is True

    # def test_QueryAWSAccounts(self):
    #     assert self.uberCCAWS_QueryAWSAccounts() is True

    # @pytest.mark.skipif(falcon.command("QueryAWSAccounts",
    #                     parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached")
    # def test_GetAWSAccounts(self):
    #     assert self.uberCCAWS_GetAWSAccounts() is True

    # def test_QueryAWSAccountsForIDs(self):
    #     assert self.uberCCAWS_QueryAWSAccountsForIDs() is True

    @pytest.mark.skipif("laggar" in falcon.base_url, reason="US-GOV-1 testing disabled")
    def test_UploadDownload(self):
        assert self.uberCCAWS_TestUploadDownload() is True

    def test_GenerateError(self):
        assert self.uberCCAWS_GenerateError() is True

    def test_GenerateInvalidPayload(self):
        assert self.uberCCAWS_GenerateInvalidPayload() is True

    def test_BadCommand(self):
        assert self.uberCCAWS_BadCommand() is True

    def test_OverrideAndHeader(self):
        # Also check token auto-renewal
        falcon.token_expiration = 0
        assert self.uberCCAWS_OverrideAndHeader() is True

    def test_PreferredDefaultLookup(self):
        assert bool(
            falcon.command("report_executions_download_get", ids="1234567890")["status_code"] in AllowedResponses
        ) is True

    def test_ContainerBodyIDPayload(self):
        assert self.uberContainer_TestBodyIDsPayload() is True

    def test_GenerateActionNameError(self):
        assert self.uberCCHosts_GenerateActionNameError(params=None) is True

    def test_GenerateInvalidOperationIDError(self):
        assert self.uberCCAWS_GenerateInvalidOperationIDError() is True

    def test_BadMethod(self):
        assert self.uberCCAWS_BadMethod() is True

    def test_GenerateServerError(self):
        assert self.uberCCAWS_GenerateServerError() is True

    def test_TestMSSP(self):
        assert self.uberCCAWS_TestMSSP() is True

    def test_GenerateTokenError(self):
        assert self.uberCCAWS_GenerateTokenError() is True

    def test_BadAuthentication(self):
        assert self.uberCCAWS_BadAuthentication() is True

    @pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made.*")
    def test_DisableSSLVerify(self):
        assert self.uberCCAWS_DisableSSLVerify() is True

    def test_crossover_properties(self):
        _success = True
        try:
            _ = falcon.token_value
            debug_setting = falcon.debug
            pythonic_setting = falcon.pythonic
            falcon.pythonic = False
            debug_rec_count = falcon.debug_record_count
            falcon.debug_record_count = 101
            sanitize = falcon.sanitize_log
            falcon.sanitize_log = True
        except:
            _success = False
        assert _success

    # def test_uber_deprecated_methods(self):
    #     assert bool(falcon.valid_cred_format()
    #                 and falcon.headers()
    #                 and falcon.token
    #                 )

    # def test_uber_deprecated_attributes(self):
    #     _success = False
    #     falcon.token_renew_window = 180
    #     if falcon.token_renew_window == 180:
    #         _success = True
    #     assert _success

    # def test_uber_properties(self):
    #     # Force a new object so we can flip the debug flag
    #     temp_falcon = APIHarness(access_token=falcon.token_value,
    #                              base_url=config["falcon_base_url"],
    #                              debug=True
    #                              )

    #     assert bool(temp_falcon.debug)

    # def test_uber_revoke_failure(self):
    #     assert bool(falcon.command("oauth2RevokeToken")["status_code"] == 400)

    # def test_uber_revoke_success(self):
    #     assert(bool(
    #         falcon.command("oauth2RevokeToken", token_value=falcon.token_value)["status_code"]==200
    #         ))

    # def test_pythonic_failure(self):
    #     _success = False
    #     new_falcon = APIHarness(access_token=falcon.token_value,
    #                         base_url=config["falcon_base_url"],
    #                         debug=_DEBUG,
    #                         pythonic=True
    #                         )
    #     try:
    #         new_falcon.command("GetDeviceDetails", ids="12345678")
    #     except APIError:
    #         _success = True
    #     assert _success


_auth = Authorization.TestAuthorization()
_auth.getConfig()


class TestLegacyUberCoverage:
    """Cover api_complete/_legacy.py debug properties and command logging."""

    def test_legacy_uber_debug_properties(self):
        """Test the debug-mode properties on the legacy APIHarness."""
        uber = APIHarness(
            client_id="fake_id",
            client_secret="fake_secret",
            debug=True,
            debug_record_count=50,
            sanitize_log=True
        )
        assert uber.debug is True
        assert uber.log is not None
        assert uber.debug_record_count == 50
        uber.debug_record_count = 25
        assert uber.debug_record_count == 25
        assert uber.sanitize_log is True
        uber.sanitize_log = False
        assert uber.sanitize_log is False

    def test_legacy_uber_no_debug_properties(self):
        """Test debug properties with no debug mode."""
        uber = APIHarness(
            client_id="fake_id",
            client_secret="fake_secret",
            debug=False
        )
        assert uber.debug is False
        assert uber.log is None
        assert uber.debug_record_count == 100
        assert uber.sanitize_log is True

    def test_legacy_uber_command_logging(self):
        """Legacy command logging of operation when authenticated with debug."""
        uber = APIHarness(
            client_id="fake_id",
            client_secret="fake_secret",
            debug=True
        )
        uber.authenticated = True
        uber.token = "fake_token"
        result = uber.command(action="queryDevicesByFilter", parameters={"limit": 1})
        assert isinstance(result, dict)


class TestLegacyUberStreamDebugCoverage:
    """Cover _util/_functions.py stream with debug logging (legacy)."""

    def test_legacy_uber_stream_with_debug(self):
        """Streaming request via legacy uber with debug."""
        uber = APIHarness(
            client_id=_auth.config["falcon_client_id"],
            client_secret=_auth.config["falcon_client_secret"],
            base_url=_auth.config["falcon_base_url"],
            debug=True
        )
        uber.authenticate()
        if uber.authenticated:
            result = uber.command(
                action="queryDevicesByFilter",
                parameters={"limit": 1}
            )
            assert isinstance(result, dict)


class _FakeResponse:
    """Minimal stand-in for requests.Response used by monkeypatch tests."""

    def __init__(self, status_code=200, body=None, headers=None, content=None):
        self.status_code = status_code
        self.headers = headers or {"Content-Type": "application/json"}
        self._body = body or {"meta": {"trace_id": "abc"}, "resources": [], "errors": []}
        self.content = content or b'{"resources":[]}'

    def json(self):
        return self._body


class TestLegacyPerformRequestMockedCoverage:
    """Cover legacy uber debug logging with monkeypatch."""

    def test_legacy_uber_debug_operation_logging(self, monkeypatch):
        """Cover legacy APIHarness debug logging on normal operation."""
        import falconpy._util._functions as _funcs
        responses = iter([
            _FakeResponse(201, {"access_token": "fake_token_123", "expires_in": 1799}),
            _FakeResponse(200, {"meta": {"trace_id": "abc"}, "resources": [], "errors": []}),
        ])
        monkeypatch.setattr(_funcs.requests, "request", lambda *a, **kw: next(responses))
        uber = APIHarness(
            client_id="fake_id",
            client_secret="fake_secret",
            debug=True
        )
        uber.authenticate()
        result = uber.command(action="QueryDevicesByFilter", parameters={"limit": 1})
        assert isinstance(result, dict)