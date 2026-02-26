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
AllowedResponses = [200, 400, 403, 404, 429]  # Adding rate-limiting and auth errors as allowed responses


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

    def serviceMLE_V2Exclusions(self):
        error_checks = True
        tests = {
            "aggregate_exclusions": falcon.aggregate_exclusions(
                field="value",
                filter="created_by:'test'",
                size=10
            ),
            "get_all_exclusions": falcon.get_all_exclusions(),
            "perform_actions": falcon.perform_actions(
                action_name="validate_filepath",
                action_parameters=[{"name": "test", "value": "test"}],
                available=True,
                description="test",
                group="test",
                label="test",
                name="test"
            ),
            "get_reports": falcon.get_reports(
                report_format="csv",
                search={"filter": "value:'test'", "sort": "value.asc"}
            ),
            "get_exclusions_by_id": falcon.get_exclusions_by_id(ids="12345678"),
            "create_exclusions_v2": falcon.create_exclusions_v2(
                exclusions=[{
                    "comment": "Unit Testing",
                    "excluded_from": ["blocking"],
                    "grandparent_value": "test",
                    "groups": ["12345678"],
                    "parent_value": "test",
                    "value": "test"
                }]
            ),
            "update_exclusions_v2": falcon.update_exclusions_v2(
                comment="Unit Testing",
                excluded_from=["blocking"],
                grandparent_value="test",
                groups=["12345678"],
                id="12345678",
                parent_value="test",
                value="test"
            ),
            "delete_exclusions_v2": falcon.delete_exclusions_v2(
                ids="12345678",
                comment="Unit Testing"
            ),
            "search_exclusions_v2": falcon.search_exclusions_v2(
                filter="value:'test'",
                offset=0,
                limit=10,
                sort="value.asc"
            ),
            "get_ml_exclusion_sets": falcon.get_ml_exclusion_sets(ids="12345678"),
            "create_ml_exclusions_v2": falcon.create_ml_exclusions_v2(
                comment="Unit Testing",
                excluded_from=["blocking"],
                groups=["12345678"],
                value="test"
            ),
            "update_ml_exclusions": falcon.update_ml_exclusions(
                comment="Unit Testing",
                groups=["12345678"],
                id="12345678",
                is_descendant_process=True,
                value="test"
            ),
            "update_ml_exclusions_2": falcon.update_ml_exclusions(
                comment="Unit Testing",
                groups="12345678,987654321",
                id="12345678",
                is_descendant_process=True,
                value="test"
            ),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                print(f"{key} failed with status {tests[key]['status_code']}")
                print(tests[key])

        return error_checks

    def test_Find(self):
        assert self.serviceMLE_ListExclusions() is True

    def test_Errors(self):
        assert self.serviceMLE_GenerateErrors() is True

    def test_V2Exclusions(self):
        assert self.serviceMLE_V2Exclusions() is True
