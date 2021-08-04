# test_real_time_response.py
# This class tests the real_time_response service class

import os
import pytest
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
# flake8: noqa: E402
from falconpy import real_time_response as FalconRTR
from falconpy import hosts as FalconHosts

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconRTR.Real_Time_Response(access_token=auth.token)
falcon_hosts = FalconHosts.Hosts(access_token=auth.token)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestRTR:

    def serviceRTR_ListAllSessions(self):
        if falcon.RTR_ListAllSessions(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    @pytest.mark.skipif(sys.version_info.minor < 9, reason="Frequency reduced due to potential race condition")
    def serviceRTR_SessionTester(self):
        returned = False
        # This will have to be periodically updated using this solution, but for now it provides the necessary code coverage.
        # Highly dependant upon my test CID / API keys
        aid_to_check = falcon_hosts.QueryDevicesByFilter(filter="hostname:'ip-172-31-30-80.us-west-1.compute.internal'")["body"]["resources"][0]
        if aid_to_check:
            session_id = falcon.RTR_InitSession(body={"device_id": aid_to_check})["body"]["resources"][0]["session_id"]
            if falcon.RTR_DeleteSession(session_id=session_id)["status_code"] == 204:
                returned = True
            else:
                returned = False

        return returned

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
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_RTR_ListAllSessions(self):
        assert self.serviceRTR_ListAllSessions() is True

    def test_RTR_SessionConnect(self):
        assert self.serviceRTR_SessionTester() is True

    def test_Logout(self):
        assert auth.serviceRevoke() is True

    def test_Errors(self):
        assert self.serviceRTR_GenerateErrors() is True