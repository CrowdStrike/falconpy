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
from falconpy import device_control_policies as FalconDeviceControlPolicy

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = FalconDeviceControlPolicy.Device_Control_Policies(access_token=token)
AllowedResponses = [200, 429, 500]  # Adding 500


class TestDeviceControlPolicy:
    """
    Test harness for the Device Control Policies Service Class
    """
    def serviceDeviceControlPolicies_GenerateErrors(self):
        """
        Generates a series of 500 errors to test remaining code paths
        """
        falcon.base_url = "nowhere"
        error_checks = True
        tests = {
            "query_combined_device_control_policy_members": falcon.queryCombinedDeviceControlPolicyMembers()["status_code"],
            "query_combined_device_control_policies": falcon.queryCombinedDeviceControlPolicies()["status_code"],
            "perform_device_control_policies_action": falcon.performDeviceControlPoliciesAction(body={}, parameters={}, action_name='enable')["status_code"],
            "perform_device_control_policies_action_two": falcon.performDeviceControlPoliciesAction(body={}, parameters={'action_name':'PooF'})["status_code"],
            "perform_device_control_policies_action_three": falcon.performDeviceControlPoliciesAction(body={}, parameters={})["status_code"],
            "set_device_control_policies_precedence": falcon.setDeviceControlPoliciesPrecedence(body={})["status_code"],
            "get_device_control_policies": falcon.getDeviceControlPolicies(ids='12345678')["status_code"],
            "create_device_control_policies": falcon.createDeviceControlPolicies(body={})["status_code"],
            "delete_device_control_policies": falcon.deleteDeviceControlPolicies(ids='12345678')["status_code"],
            "update_device_control_policies": falcon.updateDeviceControlPolicies(body={})["status_code"],
            "query_device_control_policy_members": falcon.queryDeviceControlPolicyMembers()["status_code"],
            "query_device_control_policies": falcon.queryDeviceControlPolicies()["status_code"]
        }
        for key in tests:
            if tests[key] != 500:
                error_checks = False

            # print(f"{key} operation returned a {tests[key]} status code")

        return error_checks

    def test_queryDeviceControlPolicies(self):
        """
        Pytest harness hook
        """
        assert bool(falcon.queryDeviceControlPolicies(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(
        falcon.queryDeviceControlPolicies(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached"
        )
    def test_queryDeviceControlPolicyMembers(self):
        """
        Pytest harness hook
        """
        policies = falcon.queryDeviceControlPolicies(limit=1)
        result = falcon.queryDeviceControlPolicyMembers(
                id=policies["body"]["resources"][0]
                )
        assert bool(result["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(
        falcon.queryDeviceControlPolicies(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached"
        )
    def test_getDeviceControlPolicies(self):
        """
        Pytest harness hook
        """
        policy = falcon.queryDeviceControlPolicies(parameters={"limit": 1})
        if policy["status_code"] == 500:  # Can't hit the API
            pytest.skip("Unable to communicate with the Device Control API")
        else:
            assert bool(falcon.getDeviceControlPolicies(
                    ids=policy["body"]["resources"][0]
                    )["status_code"] in AllowedResponses) is True

    def test_queryCombinedDeviceControlPolicies(self):
        """
        Pytest harness hook
        """
        assert bool(falcon.queryCombinedDeviceControlPolicies(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(
        falcon.queryCombinedDeviceControlPolicies(
            parameters={"limit": 1}
            )["status_code"] == 429, reason="API rate limit reached"
        )
    def test_queryCombinedDeviceControlPolicyMembers(self):
        """
        Pytest harness hook
        """
        policies = falcon.queryCombinedDeviceControlPolicies(parameters={"limit": 1})
        if policies["status_code"] == 500:  # Can't hit the API
            pytest.skip("Unable to communicate with the Device Control API")
        else:
            result = falcon.queryCombinedDeviceControlPolicyMembers(parameters={"id": policies["body"]["resources"][0]["id"]})
            assert bool(result["status_code"] in AllowedResponses) is True

    def test_errors(self):
        """
        Pytest harness hook
        """
        assert self.serviceDeviceControlPolicies_GenerateErrors() is True

    # @staticmethod
    # def test_logout():
    #     """
    #     Pytest harness hook
    #     """
    #     assert bool(falcon.auth_object.revoke(
    #         falcon.auth_object.token()["body"]["access_token"]
    #         )["status_code"] in AllowedResponses) is True
