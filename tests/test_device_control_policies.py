"""
test_device_control_poligies.py - This class tests the device_control_policies service class
"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# flake8: noqa=E401   # Classes to test - manually imported from sibling folder
from falconpy import DeviceControlPolicies

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = DeviceControlPolicies(auth_object=config)
AllowedResponses = [200, 429, 500]


class TestDeviceControlPolicy:
    """
    Test harness for the Device Control Policies Service Class
    """
    def serviceDeviceControlPolicies_GenerateErrors(self):
        """Generates a series of 500 errors to test remaining code paths"""
        falcon.base_url = "nowhere"
        error_checks = True
        tests = {
            "query_combined_device_control_policy_members": falcon.queryCombinedDeviceControlPolicyMembers(),
            "query_combined_device_control_policies": falcon.queryCombinedDeviceControlPolicies(),
            "perform_device_control_policies_action": falcon.performDeviceControlPoliciesAction(body={}, parameters={}, action_name='enable'),
            "perform_device_control_policies_action_two": falcon.performDeviceControlPoliciesAction(body={}, parameters={'action_name':'PooF'}),
            "perform_device_control_policies_action_three": falcon.perform_action(action_name="disable",
                                                                                  ids="12345678",
                                                                                  action_parameters=[{
                                                                                    "name": "group_id",
                                                                                    "value": "123456789abcdef987654321"
                                                                                    }],
                                                                                  group_id="12345678943413135245"
                                                                                  ),
            "set_device_control_policies_precedence": falcon.setDeviceControlPoliciesPrecedence(ids="12345678", platform_name="Windows"),
            "get_device_control_policies": falcon.getDeviceControlPolicies(ids='12345678'),
            "get_device_control_policies_v2": falcon.get_policies_v2(ids='12345678'),
            "create_device_control_policies": falcon.createDeviceControlPolicies(clone_id="12345678",
                                                                                 description="whatever",
                                                                                 name="UnitTesting",
                                                                                 platform_name="Linux",
                                                                                 settings={"classes": []}
                                                                                 ),
            "create_device_control_policies_v2": falcon.create_policies_v2(clone_id="12345678",
                                                                           description="whatever",
                                                                           name="UnitTesting",
                                                                           platform_name="Linux",
                                                                           settings={"classes": []}
                                                                           ),
            "delete_device_control_policies": falcon.deleteDeviceControlPolicies(ids='12345678'),
            "update_device_control_policies": falcon.updateDeviceControlPolicies(id="12345678",
                                                                                 description="More unit testing",
                                                                                 name="UnitTesting",
                                                                                 settings={"classes": []}
                                                                                 ),
            "update_device_control_policies_v2": falcon.update_policies_v2(id="12345678",
                                                                           description="More unit testing",
                                                                           name="UnitTesting",
                                                                           settings={"classes": []}
                                                                           ),
            "query_device_control_policy_members": falcon.queryDeviceControlPolicyMembers(),
            "query_device_control_policies": falcon.queryDeviceControlPolicies(),
            "get_default_device_control_policies": falcon.get_default_policies(),
            "update_default_device_control_policies": falcon.update_default_policies(blocked_custom_message="Test blocked notification",
                                                                                     blocked_notification={"custom_message": "Test blocked",
                                                                                                           "use_custom": True
                                                                                                           },
                                                                                     restricted_custom_message="Test restricted notification",
                                                                                     restricted_notification={"custom_message": "Test restricted",
                                                                                                              "use_custom": True
                                                                                                              }
                                                                                     ),
            "get_default_settings": falcon.get_default_settings(),
            "update_policy_classes": falcon.update_policy_classes(bluetooth_classes={}, usb_classes={}, id="12345678"),
            "update_default_settings": falcon.update_default_settings(bluetooth_custom_notifications={"blocked_notifications": {"custom_message": "bob"}},
                                                                      usb_exceptions={"delete_exception": ["bob"]}
                                                                      )
        }
        for key in tests:
            if tests[key]["status_code"] != 500:
                error_checks = False

           # print(f"{key} operation returned a {tests[key]} status code")

        return error_checks

    def test_queryDeviceControlPolicies(self):
        """
        Pytest harness hook
        """
        assert bool(falcon.queryDeviceControlPolicies(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    def test_queryDeviceControlPolicyMembers(self):
        """
        Pytest harness hook
        """
        policies = falcon.queryDeviceControlPolicies(limit=1)
        if policies["status_code"] in [429, 500]:
            pytest.skip("Rate limit hit")
        else:
            if "resources" in policies["body"]:
                if policies["body"]["resources"]:
                    result = falcon.queryDeviceControlPolicyMembers(id=policies["body"]["resources"][0])
                else:
                    pytest.skip("Rate limit hit")
            else:
                pytest.skip("Rate limit hit")
        assert bool(result["status_code"] in AllowedResponses) is True

    def test_getDeviceControlPolicies(self):
        """
        Pytest harness hook
        """
        policy = falcon.queryDeviceControlPolicies(parameters={"limit": 1})
        if policy["status_code"] in [429, 500]:  # Can't hit the API
            pytest.skip("Unable to communicate with the Device Control API")
        else:
            if "resources" in policy["body"]:
                if policy["body"]["resources"]:
                    assert bool(falcon.getDeviceControlPolicies(
                            ids=policy["body"]["resources"][0]
                            )["status_code"] in AllowedResponses) is True
                else:
                    pytest.skip("Unable to communicate with the Device Control API")
            else:
                pytest.skip("Unable to communicate with the Device Control API")

    def test_queryCombinedDeviceControlPolicies(self):
        """
        Pytest harness hook
        """
        assert bool(falcon.queryCombinedDeviceControlPolicies(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    def test_queryCombinedDeviceControlPolicyMembers(self):
        """
        Pytest harness hook
        """
        policies = falcon.queryCombinedDeviceControlPolicies(parameters={"limit": 1})
        if policies["status_code"] == [429, 500]:  # Can't hit the API
            pytest.skip("Unable to communicate with the Device Control API")
        else:
            if "resources" in policies["body"]:
                if policies["body"]["resources"]:
                    result = falcon.queryCombinedDeviceControlPolicyMembers(parameters={"id": policies["body"]["resources"][0]["id"]})
                    assert bool(result["status_code"] in AllowedResponses) is True
                else:
                    pytest.skip("Rate limit hit")
            else:
                pytest.skip("Rate limit hit")

    def test_errors(self):
        """
        Pytest harness hook
        """
        assert self.serviceDeviceControlPolicies_GenerateErrors() is True
