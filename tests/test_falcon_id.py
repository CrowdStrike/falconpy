# test_falcon_id.py
# This class tests the falcon_id service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import FalconId

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FalconId(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestFalconId:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "GetThirdPartyPasskeyRegistry": falcon.get_third_party_passkey_registry(ids="12345678"),
            "DeleteThirdPartyPasskeyRegistry": falcon.delete_third_party_passkey_registry(ids="12345678"),
            "UpdateThirdPartyPasskeyRegistry": falcon.update_third_party_passkey_registry(enabled="string", id="string"),
            "QueryThirdPartyPasskeyRegistry": falcon.query_third_party_passkey_registry(filter="string", offset=1, limit=1,
                                                                                        sort="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
