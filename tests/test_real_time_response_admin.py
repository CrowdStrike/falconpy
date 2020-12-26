# test_real_time_response_admin.py
# This class tests the real_time_response_admin service class

import json
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import real_time_response_admin as FalconRTR

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconRTR.Real_Time_Response_Admin(access_token=auth.token)
AllowedResponses = [200, 429] #Adding rate-limiting as an allowed response for now

class TestRTR:

    def serviceRTR_ListPut_Files(self):
        if falcon.RTR_ListPut_Files(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceRTR_ListScripts(self):
        if falcon.RTR_ListScripts(parameters={"limit":1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def test_RTR_ListScripts(self):
        assert self.serviceRTR_ListScripts() == True

    def test_RTR_ListPut_Files(self):
        assert self.serviceRTR_ListPut_Files() == True

    def test_logout(self):
        assert auth.serviceRevoke() == True