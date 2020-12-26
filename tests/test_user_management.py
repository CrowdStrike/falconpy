# test_user_management.py
# This class tests the user_management service class

import json
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import user_management as FalconUsers

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconUsers.User_Management(access_token=auth.token)

class TestFalconUserManagement:
    def serviceUserManagement_RetrieveEmailsByCID(self):
        if falcon.RetrieveEmailsByCID()["status_code"] == 200:
            return True
        else:
            return False

    def serviceUserManagement_RetrieveUserUUIDsByCID(self):
        if falcon.RetrieveUserUUIDsByCID()["status_code"] == 200:
            return True
        else:
            return False

    def serviceUserManagement_RetrieveUserUUID(self):
        if falcon.RetrieveUserUUID(parameters={"uid": falcon.RetrieveEmailsByCID()["body"]["resources"][0]})["status_code"] == 200:
            return True
        else:
            return False

    def serviceUserManagement_RetrieveUser(self):
        if falcon.RetrieveUser(ids=falcon.RetrieveUserUUIDsByCID()["body"]["resources"][0])["status_code"] == 200:
            return True
        else:
            return False

    def serviceUserManagement_GetUserRoleIds(self):
        if falcon.GetUserRoleIds(parameters={"user_uuid":falcon.RetrieveUserUUIDsByCID()["body"]["resources"][0]})["status_code"] == 200:
            return True
        else:
            return False

    def serviceUserManagement_GetAvailableRoleIds(self):
        if falcon.GetAvailableRoleIds()["status_code"] == 200:
            return True
        else:
            return False

    def serviceUserManagement_GetRoles(self):
        if falcon.GetRoles(ids=falcon.GetAvailableRoleIds()["body"]["resources"][0])["status_code"] == 200:
            return True
        else:
            return False

    def test_RetrieveEmailsByCID(self):
        assert self.serviceUserManagement_RetrieveEmailsByCID() == True

    def test_RetrieveUserUUIDsByCID(self):
        assert self.serviceUserManagement_RetrieveUserUUIDsByCID() == True

    def test_RetrieveUserUUID(self):
        assert self.serviceUserManagement_RetrieveUserUUID() == True

    def test_RetrieveUser(self):
        assert self.serviceUserManagement_RetrieveUser() == True

    def test_GetUserRoleIds(self):
        assert self.serviceUserManagement_GetUserRoleIds() == True

    def test_GetAvailableRoleIds(self):
        print(falcon.GetAvailableRoleIds())
        assert self.serviceUserManagement_GetAvailableRoleIds() == True

    def test_GetRoles(self):
        assert self.serviceUserManagement_GetRoles() == True

    def test_logout(self):
        assert auth.serviceRevoke() == True