# test_real_time_response.py
# This class tests the real_time_response service class

import json
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import real_time_response as FalconRTR

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconRTR.Real_Time_Response(access_token=auth.token)

class TestRTR:

    def serviceRTR_ListAllSessions(self):
        if falcon.RTR_ListAllSessions(parameters={"limit":1})["status_code"] == 200:
            return True
        else:
            return False

    def test_RTR_ListAllSessions(self):
        assert self.serviceRTR_ListAllSessions() == True

    def test_logout(self):
        assert auth.serviceRevoke() == True