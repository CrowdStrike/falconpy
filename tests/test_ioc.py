# test_ioc.py
# This class tests the IOC service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.ioc import IOC as FalconIOC

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconIOC(access_token=auth.token)
AllowedResponses = [200, 201, 404, 429]


class TestIOC:
    def serviceIOC_RunAllTests(self):
        errorChecks = True
        commandList = [
            ["indicator_combined_v1", "limit=1"],
            ["indicator_get_v1", "ids='12345678'"],
            ["indicator_create_v1", "body={}"],
            ["indicator_delete_v1", "ids='12345678'"],
            ["indicator_update_v1", "body={}"],
            ["indicator_search_v1", "parameters={'limit':1}"],
        ]
        for cmd in commandList:
            result = eval("falcon.{}({})".format(cmd[0], cmd[1]))
            if result['status_code'] not in AllowedResponses:
                errorChecks = False

        return errorChecks

    def test_RunAllTests(self):
        assert self.serviceIOC_RunAllTests() is True
