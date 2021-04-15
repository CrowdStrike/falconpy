# test_prevention_policy.py
# This class tests the prevention_policy service class

import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import prevention_policy as FalconPrevent

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconPrevent.Prevention_Policy(access_token=auth.token)
AllowedResponses = [200, 429] #Adding rate-limiting as an allowed response for now

class TestFalconPrevent:
    def servicePrevent_queryPreventionPolicies(self):
        if falcon.queryPreventionPolicies(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def servicePrevent_queryPreventionPolicyMembers(self):
        if falcon.queryPreventionPolicyMembers(parameters={"id": falcon.queryPreventionPolicies(parameters={"limit": 1})["body"]["resources"][0]})["status_code"] in AllowedResponses:
            return True
        else:
            return False
        return True

    def servicePrevent_getPreventionPolicies(self):
        if falcon.getPreventionPolicies(ids=falcon.queryPreventionPolicies(parameters={"limit": 1})["body"]["resources"][0])["status_code"] in AllowedResponses:
            return True
        else:
            return False
        return True

    def servicePrevent_queryCombinedPreventionPolicies(self):
        if falcon.queryCombinedPreventionPolicies(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def servicePrevent_queryCombinedPreventionPolicyMembers(self):
        if falcon.queryCombinedPreventionPolicyMembers(parameters={"id": falcon.queryCombinedPreventionPolicies(parameters={"limit": 1})["body"]["resources"][0]["id"]})["status_code"] in AllowedResponses:
            return True
        else:
            return False
        return True

    def servicePrevent_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["queryCombinedPreventionPolicyMembers", ""],
            ["queryCombinedPreventionPolicies", ""],
            ["performPreventionPoliciesAction", "body={}, action_name='enable', parameters={}"],
            ["performPreventionPoliciesAction", "body={}, parameters={'action_name':'PooF'}"],
            ["setPreventionPoliciesPrecedence", "body={}"],
            ["getPreventionPolicies", "ids='12345678'"],
            ["createPreventionPolicies", "body={}"],
            ["deletePreventionPolicies", "ids='12345678'"],
            ["updatePreventionPolicies", "body={}"],
            ["queryPreventionPolicyMembers", ""],
            ["queryPreventionPolicies", ""]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_queryPreventionPolicies(self):
        assert self.servicePrevent_queryPreventionPolicies() == True

    @pytest.mark.skipif(falcon.queryPreventionPolicies(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached")
    def test_queryPreventionPolicyMembers(self):
        assert self.servicePrevent_queryPreventionPolicyMembers() == True

    @pytest.mark.skipif(falcon.queryPreventionPolicies(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached")
    def test_getPreventionPolicies(self):
        assert self.servicePrevent_getPreventionPolicies() == True

    def test_queryCombinedPreventionPolicies(self):
        assert self.servicePrevent_queryCombinedPreventionPolicies() == True

    @pytest.mark.skipif(falcon.queryCombinedPreventionPolicies(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached")
    def test_queryCombinedPreventionPolicyMembers(self):
        assert self.servicePrevent_queryCombinedPreventionPolicyMembers() == True

    def test_Logout(self):
        assert auth.serviceRevoke() == True

    def test_Errors(self):
        assert self.servicePrevent_GenerateErrors() == True
