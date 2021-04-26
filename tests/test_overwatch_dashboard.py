# test_overwatch_dashboard.py
# This class tests the overwatch_dashboard service class
import os
import sys

# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.overwatch_dashboard import Overwatch_Dashboard as FalconOWD

auth = Authorization.TestAuthorization()
auth.getConfig()
falcon = FalconOWD(creds={"client_id": auth.config["falcon_client_id"],
                          "client_secret": auth.config["falcon_client_secret"]
                          })
AllowedResponses = [200, 403, 429]


class TestOverwatchDashboard:
    def serviceOWD_AggregatesDetectionsGlobalCounts(self):
        returned = False
        if falcon.AggregatesDetectionsGlobalCounts()["status_code"] in AllowedResponses:
            returned = True

        return returned

    def serviceOWD_AggregatesIncidentsGlobalCounts(self):
        returned = False
        if falcon.AggregatesIncidentsGlobalCounts()["status_code"] in AllowedResponses:
            returned = True

        return returned

    def serviceOWD_AggregatesOWEventsGlobalCounts(self):
        returned = False
        if falcon.AggregatesOWEventsGlobalCounts(bananas="yellow")["status_code"] in AllowedResponses:
            returned = True

        return returned

    def serviceOWD_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["AggregatesEvents", "body={}"],
            ["AggregatesEventsCollections", "body=[{}]"]
        ]
        for cmd in commandList:
            if eval("falcon.{}({})['status_code']".format(cmd[0], cmd[1])) != 500:
                errorChecks = False

        return errorChecks

    def test_AggregatesDetectionsGlobalCounts(self):
        assert self.serviceOWD_AggregatesDetectionsGlobalCounts() is True

    def test_AggregatesIncidentsGlobalCounts(self):
        assert self.serviceOWD_AggregatesIncidentsGlobalCounts() is True

    def test_AggregatesOWEventsGlobalCounts(self):
        assert self.serviceOWD_AggregatesOWEventsGlobalCounts() is True

    def test_Errors(self):
        assert self.serviceOWD_GenerateErrors() is True