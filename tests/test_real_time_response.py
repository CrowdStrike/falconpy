# test_real_time_response.py
# This class tests the real_time_response service class

import json
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import real_time_response as FalconRTR

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconRTR.Real_Time_Response(access_token=auth.token)
AllowedResponses = [200, 429] #Adding rate-limiting as an allowed response for now

class TestRTR:

    def serviceRTR_ListAllSessions(self):
        if falcon.RTR_ListAllSessions(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceRTR_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["RTR_AggregateSessions","body={}"],
            ["BatchActiveResponderCmd","body={}"],
            ["BatchCmd","body={}"],
            ["BatchGetCmdStatus","parameters={}"],
            ["BatchGetCmd","body={}"],
            ["BatchInitSessions","body={}"],
            ["BatchRefreshSessions","body={}"],
            ["RTR_CheckActiveResponderCommandStatus","parameters={}"],
            ["RTR_ExecuteActiveResponderCommand","body={}"],
            ["RTR_CheckCommandStatus","parameters={}"],
            ["RTR_ExecuteCommand","body={}"],
            ["RTR_GetExtractedFileContents","parameters={}"],
            ["RTR_ListFiles","parameters={}"],
            ["RTR_DeleteFile","ids='12345678', parameters={}"],
            ["RTR_ListQueuedSessions","body={}"],
            ["RTR_DeleteQueuedSession","parameters={}"],
            ["RTR_PulseSession","body={}"],
            ["RTR_ListSessions","body={}"],
            ["RTR_InitSession","body={}"],
            ["RTR_DeleteSession","parameters={}"],
            ["RTR_ListAllSessions",""]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0],cmd[1])) != 500:
                errorChecks = False
        
        return errorChecks

    def test_RTR_ListAllSessions(self):
        assert self.serviceRTR_ListAllSessions() == True

    def test_Logout(self):
        assert auth.serviceRevoke() == True

    def test_Errors(self):
        assert self.serviceRTR_GenerateErrors() == True