# test_hosts.py
# This class tests the hosts service class

import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import hosts as FalconHosts

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconHosts.Hosts(access_token=auth.token)
AllowedResponses = [200, 202, 429]  # Adding rate-limiting as an allowed response for now


class TestHosts:

    def serviceHosts_QueryHiddenDevices(self):
        if falcon.QueryHiddenDevices(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceHosts_QueryDevicesByFilterScroll(self):
        if falcon.QueryDevicesByFilterScroll(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceHosts_QueryDevicesByFilter(self):
        if falcon.QueryDevicesByFilter(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    # Commenting out until the updated hosts service class is available
    # @pytest.mark.skipif(falcon.QueryDevicesByFilter(parameters={"limit":1})["status_code"] == 429, reason="API rate limit reached")
    # def serviceHosts_GetDeviceDetails(self):
    #     if falcon.GetDeviceDetails(ids=falcon.QueryDevicesByFilter(parameters={"limit":1})["body"]["resources"][0])["status_code"] in AllowedResponses:
    #         return True
    #     else:
    #         return False

    def serviceHosts_addTag(self):
        id_list = []
        id_list.append(
            falcon.GetDeviceDetails(ids=falcon.QueryDevicesByFilter(parameters={"limit":1})["body"]["resources"][0])["body"]["resources"][0]["device_id"]
        )
        # test basic, id is a list, single valid tag w/o manipulation
        if not falcon.UpdateDeviceTags(action_name="add", ids=id_list, tags=["FalconGroupingTags/testtag"])["status_code"] in AllowedResponses:
            return False
        if not falcon.UpdateDeviceTags(action_name="remove", ids=id_list, tags=["FalconGroupingTags/testtag"])["status_code"] in AllowedResponses:
            return False
        # id is a list, multiple tags needing manipulation
        if not falcon.UpdateDeviceTags(action_name="add", ids=id_list, tags=["testtag", "tagtest", "anothertag"])["status_code"] in AllowedResponses:
            return False
        if not falcon.UpdateDeviceTags(action_name="remove", ids=id_list, tags=["testtag", "tagtest", "anothertag"])["status_code"] in AllowedResponses:
            return False
        # id is a list, mutliple tags some need manipulation
        if not falcon.UpdateDeviceTags(action_name="add", ids=id_list, tags=["FalconGroupingTags/testtag", "manipulate", "FalconGroupingTags/anothertag"])["status_code"] in AllowedResponses:
            return False
        if not falcon.UpdateDeviceTags(action_name="remove", ids=id_list, tags=["FalconGroupingTags/testtag", "manipulate", "FalconGroupingTags/anothertag"])["status_code"] in AllowedResponses:
            return False
        # id is single string, single valid tag w/o manipulation
        if not falcon.UpdateDeviceTags(action_name="add", ids=id_list[0], tags=["FalconGroupingTags/testtag"])["status_code"] in AllowedResponses:
            return False
        if not falcon.UpdateDeviceTags(action_name="remove", ids=id_list[0], tags=["FalconGroupingTags/testtag"])["status_code"] in AllowedResponses:
            return False
        # Force the unit test down line 84
        if not falcon.UpdateDeviceTags(action_name="add", ids=id_list, tags="FalconGroupingTags/testtag")["status_code"] in AllowedResponses:
            return False

        return True

    def serviceHosts_GenerateTagError(self):
        id_list = []
        id_list.append(
            falcon.GetDeviceDetails(ids=falcon.QueryDevicesByFilter(parameters={"limit":1})["body"]["resources"][0])["body"]["resources"][0]["device_id"]
        )
        #  Generate an error by sending garbage as the action_name
        if not falcon.UpdateDeviceTags(action_name="KaBOOM!", ids=id_list, tags=["FalconGroupingTags/testtag"])["status_code"] == 500:
            return False
        return True

    def serviceHosts_PerformActionV2(self):
        id_list = []
        id_list.append(
            falcon.GetDeviceDetails(ids=falcon.QueryDevicesByFilter(parameters={"limit":1})["body"]["resources"][0])["body"]["resources"][0]["device_id"]
        )
        if falcon.PerformActionV2(
                parameters={
                    "action_name": "unhide_host"
                },
                body={
                    "ids": id_list
                }
                )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceHosts_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["PerformActionV2","body={}, action_name='unhide_host', parameters={}"],
            ["PerformActionV2","body={}, parameters={'action_name':'PooF'}"],
            ["GetDeviceDetails", "ids='12345678'"],
            ["QueryHiddenDevices", ""],
            ["QueryDevicesByFilterScroll", ""],
            ["QueryDevicesByFilter", ""]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_QueryHiddenDevices(self):
        assert self.serviceHosts_QueryHiddenDevices() == True

    def test_QueryDevicesByFilterScroll(self):
        assert self.serviceHosts_QueryDevicesByFilterScroll() == True

    def test_QueryDevicesByFilter(self):
        assert self.serviceHosts_QueryDevicesByFilter() == True
    
    def test_tagging(self):
        assert self.serviceHosts_addTag() == True

    def test_GenerateTagError(self):
        assert self.serviceHosts_GenerateTagError() == True
    # def test_GetDeviceDetails(self):
    #     assert self.serviceHosts_GetDeviceDetails() == True

    # Not working... need to pull a valid AID
    # def test_PerformActionV2(self):
    #     assert self.serviceHosts_PerformActionV2() == True

    def test_Logout(self):
        assert auth.serviceRevoke() == True

    def test_Errors(self):
        assert self.serviceHosts_GenerateErrors() == True
