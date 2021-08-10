# test_real_time_response_admin.py
# This class tests the real_time_response_admin service class

import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.real_time_response_admin import Real_Time_Response_Admin as FalconRTR

auth = Authorization.TestAuthorization()
auth.getConfig()
falcon = FalconRTR(creds={"client_id": auth.config["falcon_client_id"],
                          "client_secret": auth.config["falcon_client_secret"]})
AllowedResponses = [200, 201, 429]  # Adding rate-limiting as an allowed response for now


class TestRTR:

    def serviceRTR_ListPut_Files(self):
        if falcon.RTR_ListPut_Files(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceRTR_ListScripts(self):
        if falcon.RTR_ListScripts(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceRTR_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["BatchAdminCmd", "body={}"],
            ["RTR_CheckAdminCommandStatus", "parameters={}"],
            ["RTR_ExecuteAdminCommand", "body={}"],
            ["RTR_GetPut_Files", "ids='12345678'"],
            ["RTR_CreatePut_Files", "data={}, files=[]"],
            ["RTR_DeletePut_Files", "ids='12345678'"],
            ["RTR_GetScripts", "ids='12345678'"],
            ["RTR_CreateScripts", "data={}, files=[]"],
            ["RTR_DeleteScripts", "ids='12345678'"],
            ["RTR_UpdateScripts", "data={}, files=[]"],
            ["RTR_ListPut_Files", ""],
            ["RTR_ListScripts", ""]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def rtr_logout(self):
        if falcon.auth_object.revoke(falcon.auth_object.token()["body"]["access_token"])["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def test_RTR_ListScripts(self):
        assert self.serviceRTR_ListScripts() is True

    def test_RTR_ListPut_Files(self):
        assert self.serviceRTR_ListPut_Files() is True

    def test_Logout(self):
        assert self.rtr_logout() is True

    def test_Errors(self):
        assert self.serviceRTR_GenerateErrors() is True
