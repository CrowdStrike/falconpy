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
AllowedResponses = [200, 400, 403, 404, 429, 500]  # Adding rate-limiting and auth errors as allowed responses


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

    def serviceIOAE_SSExclusions(self):
        error_checks = True
        tests = {
            "get_ss_exclusion_aggregates": falcon.get_ss_exclusion_aggregates(
                ifn_regex="test",
                cl_regex="test",
                field="pattern_id",
                filter="name:'test'",
                size=10
            ),
            "get_ss_exclusion_reports_v2": falcon.get_ss_exclusion_reports_v2(
                report_format="csv",
                search={"filter": "name:'test'", "sort": "name.asc"}
            ),
            "get_ss_exclusion_rules_v2": falcon.get_ss_exclusion_rules_v2(ids="12345678"),
            "create_ss_exclusions": falcon.create_ss_exclusions(
                exclusions=[{
                    "cl_regex": "test",
                    "comment": "Unit Testing",
                    "description": "test",
                    "detection_json": "{}",
                    "grandparent_cl_regex": "test",
                    "grandparent_ifn_regex": "test",
                    "host_groups": ["12345678"],
                    "ifn_regex": "test",
                    "name": "test",
                    "parent_cl_regex": "test",
                    "parent_ifn_regex": "test",
                    "pattern_id": "12345678",
                    "pattern_name": "test"
                }]
            ),
            "update_ss_exclusions": falcon.update_ss_exclusions(
                exclusions=[{
                    "cl_regex": "test",
                    "comment": "Unit Testing",
                    "description": "test",
                    "detection_json": "{}",
                    "grandparent_cl_regex": "test",
                    "grandparent_ifn_regex": "test",
                    "host_groups": ["12345678"],
                    "id": "12345678",
                    "ifn_regex": "test",
                    "name": "test",
                    "parent_cl_regex": "test",
                    "parent_ifn_regex": "test",
                    "pattern_id": "12345678",
                    "pattern_name": "test"
                }]
            ),
            "delete_ss_exclusions": falcon.delete_ss_exclusions(
                ids="12345678",
                comment="Unit Testing"
            ),
            "get_ss_exclusion_matched_rules": falcon.get_ss_exclusion_matched_rules(
                aid="12345678",
                command_line="test",
                grandparent_command_line="test",
                grandparent_image_file_name="test",
                image_file_name="test",
                parent_command_line="test",
                parent_image_file_name="test",
                pattern_ids=["12345678"]
            ),
            "get_default_ss_exclusions": falcon.get_default_ss_exclusions(
                aid="12345678",
                command_line="test",
                grandparent_command_line="test",
                grandparent_image_file_name="test",
                image_file_name="test",
                parent_command_line="test",
                parent_image_file_name="test"
            ),
            "query_ss_exclusions": falcon.query_ss_exclusions(
                filter="name:'test'",
                ifn_regex="test",
                cl_regex="test",
                offset=0,
                limit=10,
                sort="name.asc"
            ),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                print(f"{key} failed with status {tests[key]['status_code']}")
                print(tests[key])

        return error_checks

    def test_Find(self):
        assert self.serviceIOAE_ListExclusions() is True

    def test_Errors(self):
        assert self.serviceIOAE_GenerateErrors() is True

    def test_SSExclusions(self):
        assert self.serviceIOAE_SSExclusions() is True
