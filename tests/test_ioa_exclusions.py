# test_ioa_exclusions.py
# This class tests the ioa_exclusions service class
import os
import sys
import pytest
# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import IOAExclusions

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = IOAExclusions(auth_object=config)
AllowedResponses = [200, 400, 404, 429, 500]  # Adding rate-limiting as an allowed response for now


class TestIOAExclusions:
    def serviceIOAE_ListExclusions(self):
        returned = False
        if falcon.queryIOAExclusionsV1(limit=1, offset=2, pizza="IsDelicious")["status_code"] in AllowedResponses:
            returned = True
        else:
            pytest.skip("API communication issue")

        return returned

    def serviceIOAE_GenerateErrors(self):
        error_checks = True
        tests = {
            "get_ioa_exclusions": falcon.get_exclusions(ids="12345678"),
            "create_exclusion": falcon.create_exclusions(body={}),
            "create_exclusion_too": falcon.create_exclusions(comment="Unit Testing",
                                                             groups=["12345678"],
                                                             value="Charlie",
                                                             cl_regex="bob",
                                                             description="a",
                                                             detection_json="{}",
                                                             ifn_regex="c",
                                                             name="d",
                                                             pattern_id="e",
                                                             pattern_name="f"
                                                             ),
            "update_exclusion": falcon.update_exclusions(body={}),
            "update_exclusion_also": falcon.update_exclusions(comment="Unit Testing",
                                                              groups="12345678,98765432",
                                                              id="12345678",
                                                              value="Bananas",
                                                              cl_regex="bob",
                                                              description="a",
                                                              detection_json="{}",
                                                              ifn_regex="bobby",
                                                              name="d",
                                                              pattern_id="e",
                                                              pattern_name="f"
                                                              ),
            "delete_exclusion": falcon.delete_exclusions(ids="12345678"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                # print(f"{key} \n {tests[key]}")
                error_checks = False

        return error_checks

    def test_Find(self):
        assert self.serviceIOAE_ListExclusions() is True

    def test_Errors(self):
        assert self.serviceIOAE_GenerateErrors() is True
