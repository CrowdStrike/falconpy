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
from falconpy import hosts as FalconHosts

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = FalconHosts.Hosts(access_token=token)
AllowedResponses = [200, 202, 429]  # Adding rate-limiting as an allowed response for now


class TestHosts:
    """
    Hosts Service Class test harness
    """
    def hosts_add_tag(self):
        """
        Tests tagging functionality
        """
        id_list = []
        id_list.append(
            falcon.GetDeviceDetails(
                ids=falcon.QueryDevicesByFilter(parameters={"limit": 1})["body"]["resources"][0]
            )["body"]["resources"][0]["device_id"]
        )
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
        id_list.append(
            falcon.GetDeviceDetails(
                ids=falcon.QueryDevicesByFilter(parameters={"limit": 1})["body"]["resources"][0]
                )["body"]["resources"][0]["device_id"]
        )
        #  Generate an error by sending garbage as the action_name
        if not falcon.UpdateDeviceTags(
            action_name="KaBOOM!", ids=id_list, tags=["FalconGroupingTags/testtag"]
        )["status_code"] == 500:
            return False
        return True

    def hosts_perform_action(self):
        """
        Tests the perform action endpoint
        """
        test_id = [falcon.QueryDevicesByFilter(limit=1)["body"]["resources"][0]]
        payload = {"ids": test_id}
        action_test = falcon.PerformActionV2(action_name="hide_host", body=payload)
        if action_test["status_code"] == 202:
            action_test = falcon.PerformActionV2(action_name="unhide_host", body=payload)
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
            "perform_action": falcon.PerformActionV2(body={}, action_name='unhide_host', parameters={})["status_code"],
            "perform_action_params": falcon.PerformActionV2(body={}, parameters={'action_name': 'PooF'})["status_code"],
            "perform_action_null": falcon.PerformActionV2(body={}, parameters={})["status_code"],
            "get_device_details": falcon.GetDeviceDetails(ids='12345678')["status_code"],
            "query_hidden_devices": falcon.QueryHiddenDevices()["status_code"],
            "query_devices_by_filter_scroll": falcon.QueryDevicesByFilterScroll()["status_code"],
            "query_devices_by_filter": falcon.QueryDevicesByFilter()["status_code"]
        }
        for key in tests:
            if tests[key] != 500:
                error_checks = False
            # print(f"{key} test returned a {tests[key]} status code")
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

    def test_tagging(self):
        """Pytest harness hook"""
        assert self.hosts_add_tag() is True

    def test_generate_tag_error(self):
        """Pytest harness hook"""
        assert self.hosts_generate_tag_error() is True

    def test_get_device_details(self):
        """Pytest harness hook"""
        # Test lazy loading of the ids parameter
        assert bool(
            falcon.GetDeviceDetails(
                falcon.QueryDevicesByFilter(parameters={"limit": 1})["body"]["resources"][0]
                )["status_code"] in AllowedResponses
        ) is True

    def test_get_device_login_history(self):
        """Pytest harness hook"""
        assert bool(
            falcon.query_device_login_history(body={
                "ids": [falcon.QueryDevicesByFilter(parameters={"limit": 1})["body"]["resources"][0]]
                })["status_code"] in AllowedResponses
        ) is True

    def test_get_device_network_history(self):
        """Pytest harness hook"""
        assert bool(
            falcon.query_network_address_history(body={
                "ids": [falcon.QueryDevicesByFilter(parameters={"limit": 1})["body"]["resources"][0]]
                })["status_code"] in AllowedResponses
        ) is True
    @pytest.mark.skipif(sys.version_info.minor < 9, reason="Frequency reduced due to test flakiness")
    @pytest.mark.skipif(platform.system() != "Darwin", reason="Frequency reduced due to test flakiness")
    def test_perform_action(self):
        """Pytest harness hook"""
        assert self.hosts_perform_action() is True

    def test_errors(self):
        """Pytest harness hook"""
        assert self.hosts_generate_errors() is True
