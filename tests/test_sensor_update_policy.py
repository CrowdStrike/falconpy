# test_sensor_update_policy.py
# This class tests the sensor_update_policy service class

import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Classes to test - manually imported from sibling folder
from falconpy import SensorUpdatePolicies
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))


auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = SensorUpdatePolicies(auth_object=config)
AllowedResponses = [200, 400, 401, 404, 429]


class TestFalconSensorUpdate:
    def serviceSensorUpdate_querySensorUpdatePolicies(self):
        if falcon.querySensorUpdatePolicies(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_querySensorUpdatePolicyMembers(self):
        if falcon.querySensorUpdatePolicyMembers(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_querySensorUpdateKernelsDistinct(self):
        if falcon.query_kernels(distinct_field="flavor", limit=1)["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_queryCombinedSensorUpdateKernels(self):
        if falcon.query_combined_kernels(limit=1)["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_getSensorUpdatePolicies(self):
        try:
            id_lookup = falcon.querySensorUpdatePolicies(parameters={"limit": 1})
            if id_lookup["status_code"] == 429:
                pytest.skip("Rate limit hit")
            if id_lookup["body"]["resources"]:
                id_list = id_lookup["body"]["resources"][0]
            else:
                id_list = "1234567890"
            if falcon.getSensorUpdatePolicies(ids=id_list)["status_code"] in AllowedResponses:
                return True
            else:
                return False
        except KeyError:
            # Flaky
            pytest.skip("Workflow-related error, skipping")
            return True

    def serviceSensorUpdate_getSensorUpdatePoliciesV2(self):
        try:
            id_lookup = falcon.querySensorUpdatePolicies(parameters={"limit": 1})
            if id_lookup["status_code"] == 429:
                pytest.skip("Rate limit hit")
            if id_lookup["body"]["resources"]:
                id_list = id_lookup["body"]["resources"][0]
            else:
                id_list = "1234567890"
            if falcon.getSensorUpdatePoliciesV2(ids=id_list)["status_code"] in AllowedResponses:
                return True
            else:
                return False
        except KeyError:
            # Flaky
            pytest.skip("Workflow-related error, skipping")
            return True

    def serviceSensorUpdate_queryCombinedSensorUpdatePolicies(self):
        if falcon.queryCombinedSensorUpdatePolicies(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_queryCombinedSensorUpdatePoliciesV2(self):
        if falcon.queryCombinedSensorUpdatePoliciesV2(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_queryCombinedSensorUpdateBuilds(self):
        if falcon.queryCombinedSensorUpdateBuilds(limit=1)["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_queryCombinedSensorUpdatePolicyMembers(self):
        if falcon.queryCombinedSensorUpdatePolicyMembers(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceSensorUpdate_GenerateErrors(self):
        error_checks = True
        tests = {
            "uninstall_token": falcon.reveal_uninstall_token(device_id="MAINTENANCE"),
            "delete_policy": falcon.delete_policies(ids="12345678"),
            "update_policy": falcon.update_policies(description="whatever",
                                                    name="unit test",
                                                    id="12345678",
                                                    build="1309"
                                                    ),
            "update_policy_also": falcon.update_policies_v2(description="whatever",
                                                            name="unit test",
                                                            id="12345678",
                                                            build="1309",
                                                            uninstall_protection="DISABLED"
                                                            ),
            "set_precedence": falcon.set_policies_precedence(ids="12345678", platform_name="Windows"),
            "create_policy": falcon.create_policies(description="Unit test",
                                                    name="Unit test",
                                                    platform_name="Winders",
                                                    settings={"build": "1309"}
                                                    ),
            "create_policy_also": falcon.create_policies_v2(description="Unit test",
                                                            name="Unit test",
                                                            platform_name="Windowz",
                                                            build="1309",
                                                            uninstall_protection="DISABLED",
                                                            scheduler={"enabled": False},
                                                            show_early_adopter_builds=True,
                                                            variants=[{"build": "1309", "platform": "Windows"}]
                                                            ),
            "perform_action": falcon.perform_policies_action(action_name="disable",
                                                             ids="12345678",
                                                             action_parameters=[{
                                                                 "name": "group_id",
                                                                 "value": "123456789abcdef987654321"
                                                             }],
                                                             group_id="whatever"
                                                             )
        }

        for key in tests:
            # print(f"{key}\n{tests[key]}")
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(f"Failed on {key} with {tests[key]}")

        if falcon.perform_policies_action(action_name="dance",
                                          ids="12345678"
                                          )["status_code"] != 500:
            error_checks = False

        return error_checks

    def test_querySensorUpdatePolicies(self):
        assert self.serviceSensorUpdate_querySensorUpdatePolicies() is True

    def test_querySensorUpdatePolicyMembers(self):
        assert self.serviceSensorUpdate_querySensorUpdatePolicyMembers() is True

    def test_serviceSensorUpdate_querySensorUpdateKernelsDistinct(self):
        assert self.serviceSensorUpdate_querySensorUpdateKernelsDistinct() is True

    def test_serviceSensorUpdate_queryCombinedSensorUpdateKernels(self):
        assert self.serviceSensorUpdate_queryCombinedSensorUpdateKernels() is True

    def test_queryCombinedSensorUpdatePolicies(self):
        assert self.serviceSensorUpdate_queryCombinedSensorUpdatePolicies() is True

    def test_queryCombinedSensorUpdateBuilds(self):
        assert self.serviceSensorUpdate_queryCombinedSensorUpdateBuilds() is True

    def test_queryCombinedSensorUpdatePoliciesV2(self):
        assert self.serviceSensorUpdate_queryCombinedSensorUpdatePoliciesV2() is True

    def test_queryCombinedSensorUpdatePolicyMembers(self):
        assert self.serviceSensorUpdate_queryCombinedSensorUpdatePolicyMembers() is True

    # @pytest.mark.skipif(falcon.querySensorUpdatePolicies(parameters={"limit": 1})["status_code"] == 429,
    #                     reason="API rate limit reached")
    def test_getSensorUpdatePolicies(self):
        assert self.serviceSensorUpdate_getSensorUpdatePolicies() is True

    # @pytest.mark.skipif(falcon.querySensorUpdatePolicies(parameters={"limit": 1})["status_code"] == 429,
    #                     reason="API rate limit reached")
    def test_getSensorUpdatePoliciesV2(self):
        assert self.serviceSensorUpdate_getSensorUpdatePoliciesV2() is True

    def test_remaining_code_paths(self):
        assert self.serviceSensorUpdate_GenerateErrors() is True
