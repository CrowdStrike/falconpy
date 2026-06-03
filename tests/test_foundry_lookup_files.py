# test_foundry_lookup_files.py
# This class tests the foundry_lookup_files service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import FoundryLookupFiles

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FoundryLookupFiles(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429, 500]


class TestFoundryLookupFiles:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "CreateFileV1": falcon.create_file_v1(),
            "UpdateFileV1": falcon.update_file_v1(),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
