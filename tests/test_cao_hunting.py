# test_cao_hunting.py
# This class tests the cao_hunting service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CAOHunting

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CAOHunting(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 429]


class TestCAOHunting:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "AggregateIntelligenceQueries": falcon.aggregate_queries(),
            "GetArchiveExport": falcon.create_export_archive(),
            "GetIntelligenceQueries": falcon.get_queries(),
            "SearchIntelligenceQueries": falcon.search_queries()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
