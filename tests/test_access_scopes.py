# test_access_scopes.py
# This class tests the access_scopes service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import AccessScopes

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = AccessScopes(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestAccessScopes:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "ListAccessScopesExternal": falcon.list_access_scopes_external(ids="12345678"),
            "QueryAccessScopesExternal": falcon.query_access_scopes_external(filter="string", sort="string", offset=1,
                                                                             limit=1),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
