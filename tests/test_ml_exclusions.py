# test_ml_exclusions.py
# This class tests the ml_exclusions service class
import os
import sys
import pytest
# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import MLExclusions

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = MLExclusions(auth_object=config)
AllowedResponses = [200, 400, 404, 429]  # Adding rate-limiting as an allowed response for now


class TestMLExclusions:
    def serviceMLE_ListExclusions(self):
        returned = False
        result = falcon.queryMLExclusionsV1(limit=1, offset=2, pizza="IsDelicious")
        if result["status_code"] in AllowedResponses:
            returned = True
        else:
            pytest.skip("Unable to communicate with the API")

        return returned

    def serviceMLE_GenerateErrors(self):
        error_checks = True
        tests = {
            "get_ml_exclusions": falcon.get_exclusions(ids="12345678"),
            "create_exclusion": falcon.create_exclusions(body={}),
            "create_exclusion_too": falcon.create_exclusions(comment="Unit Testing",
                                                             groups=["12345678"],
                                                             value="Charlie",
                                                             excluded_from=["blocking"]
                                                             ),
            "update_exclusion": falcon.update_exclusions(body={"id": "12345678"}),
            "update_exclusion_also": falcon.update_exclusions(comment="Unit Testing",
                                                              groups="12345,67890",
                                                              id="12345678",
                                                              value="Bananas",
                                                              excluded_from="banana,apples"
                                                              ),
            "delete_exclusion": falcon.delete_exclusions(ids="12345678"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                # print(f"{key} \n {tests[key]}")
                error_checks = False

        return error_checks

    def test_Find(self):
        assert self.serviceMLE_ListExclusions() is True

    def test_Errors(self):
        assert self.serviceMLE_GenerateErrors() is True
