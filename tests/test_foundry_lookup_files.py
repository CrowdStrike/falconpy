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
AllowedResponses = [200, 201, 207, 400, 401, 403, 404, 429, 500]


class TestFoundryLookupFiles:
    def test_all_code_paths(self):
        error_checks = True
        payload = open("tests/testfile.png", "rb").read()
        tests = {
            "CreateFileV1": falcon.create_file_v1(file=payload,
                                                  file_name="testfile.csv",
                                                  name="unittestfile",
                                                  description="FalconPy unit test",
                                                  repo="unittest"
                                                  ),
            "CreateFileV1_fail": falcon.create_file_v1(),
            "UpdateFileV1": falcon.update_file_v1(id="123456NOTAREALID",
                                                  description="FalconPy unit test",
                                                  file=payload,
                                                  file_name="testfile.csv"
                                                  ),
            "UpdateFileV1_no_file": falcon.update_file_v1(id="123456NOTAREALID",
                                                          description="FalconPy unit test"
                                                          ),
            "CreateFileV1_params_dict": falcon.create_file_v1(file_name="testfile.csv",
                                                              parameters={"file": payload,
                                                                          "name": "unittestfile",
                                                                          "repo": "unittest"}
                                                              ),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
