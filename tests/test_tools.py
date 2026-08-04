# test_tools.py
# This class tests the tools service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import Tools

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Tools(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestTools:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "EntitiesToolsV1": falcon.entities_tools_v1(ids="12345678"),
            "QueriesToolsV1": falcon.queries_tools_v1(offset=1, limit=1, sort="string", filter="string"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
