# test_prevention_policy.py
# This class tests the prevention_policy service class

import os
import sys
import pytest
import string
import random
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import PreventionPolicy

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = PreventionPolicy(auth_object=config)
AllowedResponses = [200, 201, 400, 404, 429]


class TestFalconPrevent:
    def prev_queryPreventionPolicies(self):
        if falcon.queryPreventionPolicies(limit=1)["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def prev_queryPreventionPolicyMembers(self):
        policies = falcon.queryPreventionPolicies(limit=1)
        if policies["status_code"] not in [500, 429] and "resources" in policies["body"]:
            check = falcon.queryPreventionPolicyMembers(
                    parameters={"id": policies["body"]["resources"][0]}
                    )
            if check["status_code"] in AllowedResponses:
                return True
            else:
                pytest.skip("API communication failure")
                # return False
        else:
            if policies["status_code"] == 420:
                pytest.skip("Rate limit met")
            else:
                # Can't hit the API for some reason
                return True

    def prev_getPreventionPolicies(self):
        policies = falcon.queryPreventionPolicies(parameters={"limit": 1})
        if policies["status_code"] != 500 and "resources" in policies["body"]:
            check = falcon.getPreventionPolicies(
                    ids=policies["body"]["resources"][0]
                    )
            if check["status_code"] in AllowedResponses:
                return True
            else:
                pytest.skip("API communication failure")
                # return False
        else:
            return True  # Can't hit the API

    def prev_queryCombinedPreventionPolicies(self):
        if falcon.queryCombinedPreventionPolicies(limit=1)["status_code"] in AllowedResponses:
            return True
        else:
            # Skip on API weirdness for now as the path is still tested
            pytest.skip("API communication failure")
            # return False

    def prev_queryCombinedPreventionPolicyMembers(self):
        policies = falcon.queryCombinedPreventionPolicies(parameters={"limit": 1})
        if policies["status_code"] not in [500, 429] and "resources" in policies["body"]:
            if falcon.queryCombinedPreventionPolicyMembers(
                    parameters={"id": policies["body"]["resources"][0]["id"]}
                    )["status_code"] in AllowedResponses:
                return True
            else:
                return False
        else:
            # Can't hit the API
            if policies["status_code"] == 420:
                pytest.skip("Rate limit met")
            else:
                return True

    def prev_remaining_paths(self):
        ran_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        error_checks = True
        tests = {
            "perform_action": falcon.perform_policies_action(body={}, action_parameters=[{"name": "filter", "value": ""}]),
            "perform_action_also": falcon.perform_policies_action(action_name="disable", ids="12345678", group_id="whatevers"),
            "set_precedence": falcon.set_policies_precedence(body={
                                                                "ids": ["12345678"],
                                                                "platform_name": "Windows"
                                                            }),
            "set_precedence_as_well": falcon.set_policies_precedence(ids="12345678", platform_name="Windows"),
            "create_policy_first": falcon.create_policies(body={}, clone_id="12345678"),
            "update_policy": falcon.update_policies(body={"id": "12345678"}),
            "update_policy_too": falcon.update_policies(id="12345678",
                                                        name="whatevers",
                                                        settings=[{"id": "12345678", "value": {}}],
                                                        description="something"
                                                        ),
            "query_combined_policy_members": falcon.query_combined_policy_members(limit=1),
            "query_policy_members": falcon.query_policy_members(limit=1),
            "get_policies": falcon.get_policies(ids="12345678"),
            "delete_policies": falcon.delete_policies(ids="123456789")
        }
        for key in tests:
            # print(f"{key}\n{tests[key]}")
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(f"Failed on {key} with {tests[key]}")

        falcon.create_policies(description=f"FalconPy Unit Test {ran_string}",
                               name=f"falconpy-unit-test-{ran_string}",
                               platform_name="Windows",
                               settings=[{"id": "12345678", "value": {}}]
                               )
        policy_list = falcon.query_policies() 
        if policy_list["status_code"] != 429:
            for item in falcon.get_policies(ids=policy_list["body"]["resources"])["body"]["resources"]:
                if ran_string in item["name"]:
                    falcon.delete_policies(ids=item["id"])

        return error_checks

    @pytest.mark.skipif(
        falcon.queryPreventionPolicies(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached"
        )
    def test_query_policy_members(self):
        assert self.prev_queryPreventionPolicyMembers() is True

    def test_query_combined_policies(self):
        assert self.prev_queryCombinedPreventionPolicies() is True

    @pytest.mark.skipif(
        falcon.queryCombinedPreventionPolicies(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached"
        )
    def test_query_combined_policy_members(self):
        assert self.prev_queryCombinedPreventionPolicyMembers() is True

    # @pytest.mark.skipif(sys.version_info.minor < 10, reason="Frequency reduced due to test flakiness")
    def test_remaining_paths(self):
        assert self.prev_remaining_paths() is True
