# test_host_groups.py
# This class tests the firewall_policies service class

import json
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import host_group as FalconHostGroup

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = FalconHostGroup.Host_Group(access_token=token)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestHostGroup:

    def serviceHostGroup_queryHostGroups(self):
        if falcon.queryHostGroups(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceHostGroup_queryGroupMembers(self):
        if falcon.queryGroupMembers(
                parameters={"limit": 1, "id": falcon.queryHostGroups(parameters={"limit": 1})["body"]["resources"][0]}
                )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceHostGroup_getHostGroups(self):
        if falcon.getHostGroups(
                ids=falcon.queryHostGroups(parameters={"limit": 1})["body"]["resources"][0]
                )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceHostGroup_queryCombinedHostGroups(self):
        if falcon.queryCombinedHostGroups(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceHostGroup_queryCombinedGroupMembers(self):
        if falcon.queryCombinedGroupMembers(
            parameters={"limit": 1,
                        "id": falcon.queryCombinedHostGroups(parameters={"limit": 1})["body"]["resources"][0]["id"]
                        })["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceHostGroup_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["queryCombinedGroupMembers", ""],
            ["queryCombinedHostGroups", ""],
            ["performGroupAction", "action_name='add-hosts', body={}, parameters={}"],
            ["performGroupAction", "body={}, parameters={'action_name':'PooF'}"],
            ["performGroupAction", "body={}, parameters={}"],
            ["getHostGroups", "ids='12345678'"],
            ["createHostGroups", "body={}"],
            ["deleteHostGroups", "ids='12345678'"],
            ["updateHostGroups", "body={}"],
            ["queryGroupMembers", ""],
            ["queryHostGroups", ""]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_queryHostGroups(self):
        assert self.serviceHostGroup_queryHostGroups() is True

    @pytest.mark.skipif(falcon.queryHostGroups(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached")
    def test_queryGroupMembers(self):
        assert self.serviceHostGroup_queryGroupMembers() is True

    @pytest.mark.skipif(
        falcon.queryHostGroups(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached"
        )
    def test_getHostGroups(self):
        assert self.serviceHostGroup_getHostGroups() is True

    def test_queryCombinedHostGroups(self):
        assert self.serviceHostGroup_queryCombinedHostGroups() is True

    @pytest.mark.skipif(
        falcon.queryCombinedHostGroups(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached"
        )
    def test_queryCombinedGroupMembers(self):
        assert self.serviceHostGroup_queryCombinedGroupMembers() is True

    def test_Errors(self):
        assert self.serviceHostGroup_GenerateErrors() is True
