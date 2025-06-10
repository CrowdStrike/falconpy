"""
test_hosts.py -  This class tests the hosts service class
"""
import platform
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import Hosts

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Hosts(auth_object=config)
AllowedResponses = [200, 202, 400, 401, 403, 404, 429, 501]  # Allow 501 from usgov1


class TestHosts:
    """
    Hosts Service Class test harness
    """
    def hosts_add_tag(self):
        """
        Tests tagging functionality
        """
        id_list = "1234567890"
        id_lookup = falcon.QueryDevicesByFilter(parameters={"limit": 1})
        if id_lookup["status_code"] != 429:
            if id_lookup["body"]["resources"]:
                id_list = id_lookup["body"]["resources"]
        # id_list.append(
        #     falcon.GetDeviceDetails(
        #         ids=found_id
        #     )["body"]["resources"][0]["device_id"]
        # )
        # test basic, id is a list, single valid tag w/o manipulation
        if not falcon.UpdateDeviceTags(
            action_name="add", ids=id_list, tags=["FalconGroupingTags/testtag"]
        )["status_code"] in AllowedResponses:
            return False
        if not falcon.UpdateDeviceTags(
            action_name="remove", ids=id_list, tags=["FalconGroupingTags/testtag"]
        )["status_code"] in AllowedResponses:
            return False
        # id is a list, multiple tags needing manipulation
        if not falcon.UpdateDeviceTags(
            action_name="add", ids=id_list, tags=["testtag", "tagtest", "anothertag"]
        )["status_code"] in AllowedResponses:
            return False
        if not falcon.UpdateDeviceTags(
            action_name="remove", ids=id_list, tags=["testtag", "tagtest", "anothertag"]
        )["status_code"] in AllowedResponses:
            return False
        # id is a list, mutliple tags some need manipulation
        if not falcon.UpdateDeviceTags(
            action_name="add",
            ids=id_list,
            tags=["FalconGroupingTags/testtag", "manipulate", "FalconGroupingTags/anothertag"]
        )["status_code"] in AllowedResponses:
            return False
        if not falcon.UpdateDeviceTags(
            action_name="remove",
            ids=id_list,
            tags=["FalconGroupingTags/testtag", "manipulate", "FalconGroupingTags/anothertag"]
        )["status_code"] in AllowedResponses:
            return False
        # id is single string, single valid tag w/o manipulation
        if not falcon.UpdateDeviceTags(
            action_name="add", ids=id_list[0], tags=["FalconGroupingTags/testtag"]
        )["status_code"] in AllowedResponses:
            return False
        if not falcon.UpdateDeviceTags(
            action_name="remove", ids=id_list[0], tags=["FalconGroupingTags/testtag"]
        )["status_code"] in AllowedResponses:
            return False
        # Force the unit test down line 84
        if not falcon.UpdateDeviceTags(
            action_name="add", ids=id_list, tags="FalconGroupingTags/testtag"
        )["status_code"] in AllowedResponses:
            return False

        return True

    def hosts_generate_tag_error(self):
        """
        Tests tag error handling
        """
        id_list = []
        id_lookup = falcon.QueryDevicesByFilter(parameters={"limit": 1})
        found_id = "1234567890"
        if id_lookup["status_code"] != 429:
            if id_lookup["body"]["resources"]:
                found_id = id_lookup["body"]["resources"]

        # id_list.append(
        #     falcon.GetDeviceDetails(
        #         ids=found_id
        #     )["body"]["resources"][0]["device_id"]
        # )
        #  Generate an error by sending garbage as the action_name
        if not falcon.UpdateDeviceTags(
            action_name="KaBOOM!", ids=found_id, tags=["FalconGroupingTags/testtag"]
        )["status_code"] == 500:
            return False
        return True

    def hosts_perform_action(self):
        """
        Tests the perform action endpoint
        """

        id_lookup = falcon.QueryDevicesByFilter(limit=1)
        if id_lookup["status_code"] != 429:
            test_id = id_lookup["body"]["resources"][0]
        else:
            pytest.skip("Rate limit met")
        payload = {"ids": [test_id]}
        action_test = falcon.PerformActionV2(action_name="hide_host", body=payload)
        if action_test["status_code"] == 202:
            action_test = falcon.PerformActionV2(action_name="unhide_host", ids=test_id)
            if action_test["status_code"] == 202:
                return True
            else:
                return False
        else:
            pytest.skip("Perform action test failure, skipping")
            return False

    def hosts_generate_errors(self):
        """
        Generates a series of 500 errors to test remaining code paths
        """
        falcon.base_url = "nowhere"
        error_checks = True
        tests = {
            "perform_action": falcon.PerformActionV2(ids="12345,67890", action_name='unhide_host', parameters={})["status_code"],
            "perform_action_params": falcon.PerformActionV2(body={}, parameters={'action_name': 'PooF'})["status_code"],
            "perform_action_null": falcon.PerformActionV2(body={}, parameters={})["status_code"],
            "get_device_details": falcon.GetDeviceDetails(ids='12345678')["status_code"],
            "get_device_detailsv1": falcon.GetDeviceDetailsV1(ids='12345678')["status_code"],
            "get_device_detailsv2": falcon.GetDeviceDetailsV2(ids='12345678')["status_code"],
            "query_hidden_devices": falcon.QueryHiddenDevices()["status_code"],
            "query_devices_by_filter_scroll": falcon.QueryDevicesByFilterScroll()["status_code"],
            "query_devices_by_filter": falcon.QueryDevicesByFilter()["status_code"],
            "get_online_state": falcon.get_online_state("12345678")["status_code"],
            "entities_perform_action": falcon.perform_group_action(action_name="add_group_member",
                                                                   action_parameters={"name": "Whatever", "value": "Thing"},
                                                                   ids="ID1,ID2,ID3",
                                                                   name="bob",
                                                                   value="larry"
                                                                   )["status_code"],
            "entities_perform_action_also": falcon.perform_group_action(action_name="add_bob",
                                                                   action_parameters={"name": "Whatever", "value": "Thing"},
                                                                   ids="ID1,ID2,ID3",
                                                                   name="bob",
                                                                   value="larry"
                                                                   )["status_code"],
            "CombinedDevicesByFilter": falcon.query_devices_by_filter_combined(limit=1)["status_code"],
            "CombinedHiddenDevicesByFilter": falcon.query_hidden_devices_combined(limit=1)["status_code"]
        }
        for key in tests:
            if tests[key] not in [400, 500]:
                error_checks = False
                # print(f"{key} test returned a {tests[key]} status code")
                # print(key)
                # print(tests[key]) 
        return error_checks

    def test_query_hidden_devices(self):
        """Pytest harness hook"""
        assert bool(falcon.QueryHiddenDevices(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    def test_query_devices_by_filter_scroll(self):
        """Pytest harness hook"""
        assert bool(falcon.QueryDevicesByFilterScroll(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    def test_query_devices_by_filter(self):
        """Pytest harness hook"""
        assert bool(falcon.QueryDevicesByFilter(parameters={"limit": 1})["status_code"] in AllowedResponses) is True

    def test_expanded_host_result(self):
        """Tests for result expansion in a non-binary payload."""
        assert bool(falcon.query_devices_by_filter(limit=1, expand_result=True)[0] in AllowedResponses) is True

    def test_tagging(self):
        """Pytest harness hook"""
        assert self.hosts_add_tag() is True

    def test_generate_tag_error(self):
        """Pytest harness hook"""
        assert self.hosts_generate_tag_error() is True

    def test_get_device_details(self):
        """Pytest harness hook"""
        id_lookup = falcon.QueryDevicesByFilter(parameters={"limit": 1})
        found_id = "1234567890"
        if id_lookup["status_code"] != 429:
            if id_lookup["body"]["resources"]:
                found_id = id_lookup["body"]["resources"][0]
        # Test lazy loading of the ids parameter
        assert bool(
            falcon.GetDeviceDetails(found_id)["status_code"] in AllowedResponses
        ) is True

    def test_get_device_login_history(self):
        """Pytest harness hook"""
        id_lookup = falcon.QueryDevicesByFilter(parameters={"limit": 1})
        id_list = "1234567890"
        if id_lookup["status_code"] != 429:
            if id_lookup["body"]["resources"]:
                id_list = id_lookup["body"]["resources"][0]

        assert bool(
            falcon.query_device_login_history({
                "ids": [id_list]
                })["status_code"] in AllowedResponses
        ) is True

    def test_get_device_login_history_two(self):
        """Pytest harness hook"""
        id_lookup = falcon.QueryDevicesByFilter(parameters={"limit": 1})
        id_list = "1234567890"
        if id_lookup["status_code"] != 429:
            if id_lookup["body"]["resources"]:
                id_list = id_lookup["body"]["resources"][0]
        assert bool(
            falcon.query_device_login_history_v2(
                ids=id_list
                )["status_code"] in AllowedResponses
        ) is True

    def test_get_device_login_history_three(self):
        """Pytest harness hook"""
        id_lookup = falcon.QueryDevicesByFilter(parameters={"limit": 1})
        id_list = "1234567890"
        if id_lookup["status_code"] != 429:
            if id_lookup["body"]["resources"]:
                id_list = id_lookup["body"]["resources"][0]
        assert bool(
            falcon.query_device_login_history(id_list)["status_code"] in AllowedResponses
        ) is True

    def test_get_device_network_history(self):
        """Pytest harness hook"""
        id_lookup = falcon.QueryDevicesByFilter(parameters={"limit": 1})
        id_list = "1234567890"
        if id_lookup["status_code"] != 429:
            if id_lookup["body"]["resources"]:
                id_list = id_lookup["body"]["resources"][0]
        assert bool(
            falcon.query_network_address_history(body={
                "ids": [id_list]
                })["status_code"] in AllowedResponses
        ) is True

    def test_get_device_network_history_two(self):
        """Pytest harness hook"""
        id_lookup = falcon.QueryDevicesByFilter(parameters={"limit": 1})
        id_list = "1234567890"
        if id_lookup["status_code"] != 429:
            if id_lookup["body"]["resources"]:
                id_list = id_lookup["body"]["resources"][0]
        result = bool(falcon.query_network_address_history(
                    ids=id_list
                    )["status_code"] in AllowedResponses)
        if "api.laggar.gcw.crowdstrike.com" in falcon.base_url:
            result = True
        assert bool(result) is True

    @pytest.mark.skipif(sys.version_info.minor < 10 and platform.system() != "Darwin",
                        reason="Frequency reduced due to test flakiness"
                        )
    def test_perform_action(self):
        """Pytest harness hook"""
        assert self.hosts_perform_action() is True

    def test_missing_keyword(self):
        """Pytest harness hook."""
        assert bool(
            falcon.query_devices_by_filter("Arguments not accepted")["status_code"] == 500
        ) is True

    def test_errors(self):
        """Pytest harness hook"""
        assert self.hosts_generate_errors() is True
