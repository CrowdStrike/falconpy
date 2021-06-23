# test_recon.py
# This class tests the Falcon X Recon service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.recon import Recon as FalconRecon

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconRecon(access_token=auth.token)
AllowedResponses = [200, 201, 403, 404, 429]


class TestRecon:
    def serviceRecon_RunAllTests(self):
        errorChecks = True
        commandList = [
            ["AggregateNotificationsV1", "body={}"],  # 403
            ["PreviewRuleV1", "body={}"],
            ["GetActionsV1", "ids='12345678'"],
            ["CreateActionsV1", "body={}"],
            ["DeleteActionV1", "parameters={'ids':'12345678'}"],  # 403
            ["UpdateActionV1", "body={}"],
            ["GetNotificationsDetailedTranslatedV1", "ids='12345678'"],
            ["GetNotificationsDetailedV1", "ids='12345678'"],
            ["GetNotificationsTranslatedV1", "ids='12345678'"],
            ["GetNotificationsV1", "ids='12345678'"],
            ["DeleteNotificationsV1", "ids='12345678'"],
            ["UpdateNotificationsV1", "body={}"],
            ["GetRulesV1", "ids='12345678'"],
            ["CreateRulesV1", "body={}"],  # 403
            ["DeleteRulesV1", "ids='12345678'"],
            ["UpdateRulesV1", "body={}"],
            ["QueryActionsV1", "limit=1"],
            ["QueryNotificationsV1", "parameters={'limit':1}"],
            ["QueryRulesV1", "limit=1"],
        ]
        for cmd in commandList:
            result = eval("falcon.{}({})".format(cmd[0], cmd[1]))
            if result['status_code'] not in AllowedResponses:
                errorChecks = False

        return errorChecks

    def test_RunAllTests(self):
        assert self.serviceRecon_RunAllTests() is True
