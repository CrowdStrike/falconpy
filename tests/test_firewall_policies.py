# test_firewall_policies.py 
# This class tests the firewall_policies service class
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# flake8: noqa=R0402  # Classes to test - manually imported from sibling folder
from falconpy import FirewallPolicies

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FirewallPolicies(auth_object=config)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestFirewallPolicy:

    def serviceFirewall_queryFirewallPolicies(self):
        if falcon.queryFirewallPolicies(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceFirewall_GenerateErrors(self):
        falcon.base_url = "nowhere"
        error_checks = True
        tests = {
            "query_combined_device_control_policy_members": falcon.queryCombinedFirewallPolicyMembers(),
            "query_combined_device_control_policies": falcon.queryCombinedFirewallPolicies(),
            "perform_device_control_policies_action": falcon.performFirewallPoliciesAction(body={}, parameters={}, action_name='enable'),
            "perform_device_control_policies_action_two": falcon.performFirewallPoliciesAction(body={}, parameters={'action_name':'PooF'}),
            "perform_device_control_policies_action_three": falcon.perform_action(action_name="disable",
                                                                                  ids="12345678",
                                                                                  action_parameters=[{
                                                                                    "name": "group_id",
                                                                                    "value": "123456789abcdef987654321"
                                                                                    }],
                                                                                  group_id="group_id_can_go_here_too"
                                                                                  ),
            "set_device_control_policies_precedence": falcon.setFirewallPoliciesPrecedence(ids="12345678", platform_name="Windows"),
            "get_device_control_policies": falcon.getFirewallPolicies(ids='12345678'),
            "create_device_control_policies": falcon.createFirewallPolicies(clone_id="12345678",
                                                                                 description="whatever",
                                                                                 name="UnitTesting",
                                                                                 platform_name="Linux",
                                                                                 settings={"classes": []}
                                                                                 ),
            "delete_device_control_policies": falcon.deleteFirewallPolicies(ids='12345678'),
            "update_device_control_policies": falcon.updateFirewallPolicies(id="12345678",
                                                                                 description="More unit testing",
                                                                                 name="UnitTesting",
                                                                                 settings={"classes": []}
                                                                                 ),
            "query_device_control_policy_members": falcon.queryFirewallPolicyMembers(),
            "query_device_control_policies": falcon.queryFirewallPolicies()
        }
        for key in tests:
            if tests[key]["status_code"] != 500:
                error_checks = False

            # print(f"{key} operation returned a {tests[key]} status code")

        return error_checks

    def test_Errors(self):
        assert self.serviceFirewall_GenerateErrors() is True
