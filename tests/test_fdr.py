# test_fdr.py
# This class tests the FDR service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import FDR

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FDR(auth_object=config)
AllowedResponses = [200, 201, 207, 403, 429, 500]

class TestFDR:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "get_event_combined": falcon.get_event_combined(),
            "get_event_entities": falcon.get_event_entities("12345678"),  # Weird 500 from here
            "get_fields_entities": falcon.get_field_entities(),
            "query_event_entities": falcon.query_event_entities(),
            "query_field_entities": falcon.query_field_entities()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
