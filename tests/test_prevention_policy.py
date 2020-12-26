# test_prevention_policy.py
# This class tests the prevention_policy service class

import json
import os
import sys
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import prevention_policy as FalconPrevent

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconPrevent.Prevention_Policy(access_token=auth.token)

class TestFalconPrevent:
    def servicePrevent_queryPreventionPolicies(self):
        if falcon.queryPreventionPolicies(parameters={"limit":1})["status_code"] == 200:
            return True
        else:
            return False

    def servicePrevent_queryPreventionPolicyMembers(self):
        if falcon.queryPreventionPolicyMembers(parameters={"id":falcon.queryPreventionPolicies(parameters={"limit":1})["body"]["resources"][0]})["status_code"] == 200:
            return True
        else:
            return False
        return True

    def servicePrevent_getPreventionPolicies(self):
        if falcon.getPreventionPolicies(ids=falcon.queryPreventionPolicies(parameters={"limit":1})["body"]["resources"][0])["status_code"] == 200:
            return True
        else:
            return False
        return True

    def servicePrevent_queryCombinedPreventionPolicies(self):
        if falcon.queryCombinedPreventionPolicies(parameters={"limit":1})["status_code"] == 200:
            return True
        else:
            return False

    def servicePrevent_queryCombinedPreventionPolicyMembers(self):
        if falcon.queryCombinedPreventionPolicyMembers(parameters={"id":falcon.queryCombinedPreventionPolicies(parameters={"limit":1})["body"]["resources"][0]["id"]})["status_code"] == 200:
            return True
        else:
            return False
        return True

    def test_queryPreventionPolicies(self):
        assert self.servicePrevent_queryPreventionPolicies() == True

    def test_queryPreventionPolicyMembers(self):
        assert self.servicePrevent_queryPreventionPolicyMembers() == True

    def test_getPreventionPolicies(self):
        assert self.servicePrevent_getPreventionPolicies() == True

    def test_queryCombinedPreventionPolicies(self):
        assert self.servicePrevent_queryCombinedPreventionPolicies() == True

    def test_queryCombinedPreventionPolicyMembers(self):
        assert self.servicePrevent_queryCombinedPreventionPolicyMembers() == True

    def test_logout(self):
        assert auth.serviceRevoke() == True