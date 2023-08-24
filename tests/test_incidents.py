"""test_incidents.py

This class tests the incidents service class
"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import Incidents

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Incidents(auth_object=config)
AllowedResponses = [200, 400, 429]  # Adding rate-limiting as an allowed response for now


class TestIncidents:
    def serviceIncidents_CrowdScore(self):
        if falcon.CrowdScore(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIncidents_QueryBehaviors(self):
        if falcon.QueryBehaviors(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIncidents_QueryIncidents(self):
        if falcon.QueryIncidents(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIncidents_GetBehaviors(self):
        be_lookup = falcon.QueryBehaviors(parameters={"limit": 1})
        be_result="1234567890"
        if be_lookup["status_code"] != 429:
            if be_lookup["body"]["resources"]:
                be_result = be_lookup["body"]["resources"]
        if falcon.GetBehaviors(body={
                            "ids": be_result
                            })["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIncidents_GetIncidents(self):
        inc_lookup = falcon.QueryIncidents(parameters={"limit": 1})
        inc = "1234567890"
        if inc_lookup["status_code"] != 429:
            if inc_lookup["body"]["resources"]:
                inc = inc_lookup["body"]["resources"]
        if falcon.GetIncidents(body={
                            "ids": inc
                            })["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceIncidents_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        commandList = [
            ["CrowdScore", falcon.crowdscore()],
            ["GetBehaviors", falcon.get_behaviors()],
            ["PerformIncidentAction", falcon.perform_incident_action(action_parameters=[
                {"name": "whatever", "value": "something"}
                ],
                add_comment="Something",
                add_tag="Something",
                delete_tag="something",
                update_name="something",
                update_description="dark side",
                unassign=True,
                update_assigned_to_v2="UUID here",
                update_status="40"
                )],
            ["GetIncidents", falcon.get_incidents()],
            ["QueryBehaviors", falcon.query_behaviors()],
            ["QueryIncidents", falcon.query_incidents()]
        ]
        for cmd in commandList:
            if cmd[1]["status_code"] != 500:
                errorChecks = False

        return errorChecks

    def test_CrowdScore(self):
        assert self.serviceIncidents_CrowdScore() is True

    def test_QueryBehaviors(self):
        assert self.serviceIncidents_QueryBehaviors() is True

    def test_QueryIncidents(self):
        assert self.serviceIncidents_QueryIncidents() is True

    @pytest.mark.skipif(falcon.QueryIncidents(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached")
    def test_GetIncidents(self):
        assert self.serviceIncidents_GetIncidents() is True

    @pytest.mark.skipif(falcon.QueryBehaviors(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached")
    def test_GetBehaviors(self):
        assert self.serviceIncidents_GetBehaviors() is True

    def test_Errors(self):
        assert self.serviceIncidents_GenerateErrors() is True
