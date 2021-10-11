# test_installation_tokens.py
# This class tests the installation_tokens service class
import os
import sys
import string
import random
import pytest
# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import InstallationTokens

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = InstallationTokens(access_token=token)
AllowedResponses = [200, 201, 400, 404, 429]


class TestInstallationTokens:
    def svc_tokens_get_customer_settings(self):
        returned = False
        if falcon.customer_settings_read()["status_code"] in AllowedResponses:
            returned = True

        return returned

    def svc_tokens_query_audit_events(self):
        returned = False
        if falcon.audit_events_query(limit=1, offset=2)["status_code"] in AllowedResponses:
            returned = True

        return returned

    def svc_tokens_query_tokens(self):
        returned = False
        if falcon.tokens_query(bananas="yellow", limit=1, parameters={"offset": 2})["status_code"] in AllowedResponses:
            returned = True

        return returned

    def svc_tokens_test_code_paths(self):
        error_checks = True
        ran_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        tests = {
            "audit_events_read": falcon.audit_events_read(ids="12345678"),
            "tokens_read": falcon.tokens_read(ids="12345678"),
            "tokens_create_first": falcon.tokens_create(body={}),
            "tokens_create": falcon.tokens_create(type="customer_managed",
                                                  expires_timestamp="2022-12-01T00:00:00Z",
                                                  label=f"Unit testing {ran_string}"
                                                  ),
            "tokens_update_first": falcon.tokens_update(body={}, ids="12345678")
        }
        for key in tests:
            # print(f"{key} \n {tests[key]}")
            _ = f"{key} \n {tests[key]}"
            if tests[key]["status_code"] not in AllowedResponses:
                # print(f"{key} \n {tests[key]}")
                error_checks = False

        # Test update / delete after a slight delay
        try:
            id_list = falcon.tokens_query(filter=f"label:'Unit testing {ran_string}'")
            if id_list["status_code"] != 429:
                falcon.tokens_update(ids=id_list["body"]["resources"],
                                     expires_timestamp="2022-12-31T00:00:00Z",
                                     label=f"Unit testing {ran_string}",
                                     revoked=True
                                     )
                falcon.tokens_delete(ids=id_list["body"]["resources"])
            else:
                pytest.skip("Rate limit hit, skipping")

        except KeyError:
            error_checks = False

        return error_checks

    def test_get_customer_settings(self):
        assert self.svc_tokens_get_customer_settings() is True

    def test_query_audit_events(self):
        assert self.svc_tokens_query_audit_events() is True

    def test_query_tokens(self):
        assert self.svc_tokens_query_tokens() is True

    @pytest.mark.skipif(sys.version_info.minor < 9, reason="Frequency reduced due to token API rate limit configuration")
    def test_remaining_code_paths(self):
        assert self.svc_tokens_test_code_paths() is True
