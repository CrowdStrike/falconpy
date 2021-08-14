# test_response_policies.py
# This class tests the Response_Policies service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.response_policies import Response_Policies as FalconRTRPolicy

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = FalconRTRPolicy(access_token=token)
AllowedResponses = [200, 201, 400, 404, 429]


class TestRTRPolicy:
    def serviceRTRPolicy_RunAllTests(self):
        errorChecks = True
        commandList = [
            ["queryCombinedRTResponsePolicyMembers", "limit=1"],
            ["queryCombinedRTResponsePolicies", "limit=1,id=12345678"],
            ["performRTResponsePoliciesAction", "action_name='enable',body={'ids':['12345678']}"],
            ["setRTResponsePoliciesPrecedence", "body={'ids':['12345678','98765432'],'platform_name':'Windows'}"],
            ["getRTResponsePolicies", "ids='01234567890123456789012345678901'"],
            ["createRTResponsePolicies", "body={'resources': [{'settings': [{'id': '12345678'}]}]}"],  # Generates a 400
            ["deleteRTResponsePolicies", "ids='01234567890123456789012345678901'"],
            ["updateRTResponsePolicies", "body={}"],  # Generates a 400
            ["queryRTResponsePolicyMembers", "parameters={'limit':1,'ids':['12345678']}"],
            ["queryRTResponsePolicies", "limit=1"],
        ]
        for cmd in commandList:
            result = eval("falcon.{}({})".format(cmd[0], cmd[1]))
            if result['status_code'] not in AllowedResponses:
                errorChecks = False

        return errorChecks

    def test_RunAllTests(self):
        assert self.serviceRTRPolicy_RunAllTests() is True
