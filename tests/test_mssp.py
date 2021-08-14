# test_mssp.py
# This class tests the mssp service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.mssp import Flight_Control  # noqa: E402  pylint: disable=E0401

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = Flight_Control(access_token=token)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestFlightControl:
    def serviceFlight_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["getChildren", "ids='12345678'"],
            ["getCIDGroupMembersBy", "cid_group_ids='12345678'"],
            ["addCIDGroupMembers", "body={}"],
            ["deleteCIDGroupMembers", "body={}"],
            ["getCIDGroupById", "cid_group_ids='12345678'"],
            ["createCIDGroups", "body={}"],
            ["deleteCIDGroups", "cid_group_ids='12345678'"],
            ["updateCIDGroups", "body={}"],
            ["getRolesByID", "ids='12345678'"],
            ["addRole", "body={}"],
            ["deleteRoles", "body={}"],
            ["getUserGroupMembersByID", "user_group_ids='12345678'"],
            ["getUserGroupsByID", "user_group_ids='12345678'"],
            ["addUserGroupMembers", "body={}"],
            ["deleteUserGroupMembers", "body={}"],
            ["createUserGroup", "body={}"],
            ["updateUserGroups", "body={}"],
            ["deleteUserGroups", "user_group_ids='12345678'"],
            ["queryChildren", ""],
            ["queryCIDGroupMembers", ""],
            ["queryCIDGroups", ""],
            ["queryRoles", ""],
            ["queryUserGroupMembers", ""],
            ["queryUserGroups", ""]

        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_Errors(self):
        assert self.serviceFlight_GenerateErrors() is True
