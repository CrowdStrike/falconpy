# test_response_policies.py
# This class tests the Response_Policies service class
import os
import sys
import random
import string
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ResponsePolicies

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ResponsePolicies(auth_object=config)
AllowedResponses = [200, 201, 400, 401, 404, 429]


class TestRTRPolicy:
    def service_rtr_policy_run_all(self):
        ran_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        error_checks = True
        tests = {
            "queryCombinedRTResponsePolicyMembers": falcon.query_combined_policy_members(limit=1),
            "queryCombinedRTResponsePolicies": falcon.query_combined_policies(limit=1, id="12345678"),
            "performRTResponsePoliciesAction": falcon.perform_policies_action(action_name='enable',
                                                                              body={'ids': ['12345678']}
                                                                              ),
            "perform_action_too": falcon.perform_policies_action(action_name="whatevers",
                                                                 action_parameters={"name": "filter", "value": ""},
                                                                 ids="12345678",
                                                                 group_id="whatever"
                                                                 ),
            "setRTResponsePoliciesPrecedence": falcon.set_policies_precedence(body={
                                                                                'ids': ['12345678', '98765432'],
                                                                                'platform_name': 'Windows'
                                                                                }),
            "set_precedence_as_well": falcon.set_policies_precedence(ids="12345678", platform_name="Windows"),
            "getRTResponsePolicies": falcon.get_policies(ids='01234567890123456789012345678901'),
            "createRTResponsePolicies": falcon.create_policies(body={
                                                                'resources': [{'settings': [{'id': '12345678'}]}]
                                                                }),
            "deleteRTResponsePolicies": falcon.delete_policies(ids='01234567890123456789012345678901'),
            "updateRTResponsePolicies": falcon.update_policies(body={}, clone_id="12345678"),
            "update_policy_too": falcon.update_policies(id="12345678",
                                                        name="whatevers",
                                                        settings=[{"id": "12345678", "value": {}}],
                                                        description="something"
                                                        ),
            "queryRTResponsePolicyMembers": falcon.query_policy_members(parameters={
                                                                            'limit': 1, 'ids': ['12345678']
                                                                            }),
            "queryRTResponsePolicies": falcon.query_policies(limit=1),
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

    def test_all_code_paths(self):
        assert self.service_rtr_policy_run_all() is True
