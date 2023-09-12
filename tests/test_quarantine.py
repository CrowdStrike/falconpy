""" test_quarantine.py - This class tests the quarantine service class"""
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.quarantine import Quarantine

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Quarantine(auth_object=config)
AllowedResponses = [200, 201, 202, 203, 204, 400, 401, 404, 429]


class TestQuarantine:
    """Test harness for the Quarantine Service Class"""
    def quarantine_test_all_code_paths(self):
        """Test every code path, accepts all errors except 500"""
        error_checks = True
        tests = {
            "action_update_count": falcon.action_update_count(filter=""),
            "get_aggregate_files": falcon.get_aggregate_files(),
            "get_quarantine_files": falcon.get_quarantine_files(body={}),
            "update_quarantined_detects_by_id": falcon.update_quarantined_detects_by_id(body={},
                                                                                        action="release",
                                                                                        comment="Unit testing"
                                                                                        ),
            "update_quarantined_detects_by_query": falcon.update_quarantined_detects_by_query(body={}),
            "query_quarantine_files": falcon.query_quarantine_files(limit=10)
        }
        for key in tests:

            if tests[key]["status_code"] not in AllowedResponses and key != "get_aggregate_files":
                error_checks = False
                # print(f"Failed on {key} with {tests[key]}")
            # print(tests[key])
        return error_checks

    def test_all_paths(self):
        """Pytest harness hook"""
        assert self.quarantine_test_all_code_paths() is True
