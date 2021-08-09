# test_event_streams.py
# This class tests the event_streams service class
import os
import sys
import datetime
import requests
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy.event_streams import Event_Streams

auth = Authorization.TestAuthorization()
# Moving to credential authentication
auth.getConfig()
falcon = Event_Streams(creds={"client_id": auth.config["falcon_client_id"],
                              "client_secret": auth.config["falcon_client_secret"]})

AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now
appId = "pytest-event_streams-unit-test"


class TestEventStreams:

    def serviceStream_listAvailableStreamsOAuth2(self):
        if falcon.listAvailableStreamsOAuth2(
                parameters={"appId": f"{appId}"}
                )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def serviceStream_refreshActiveStreamSession(self):
        avail = falcon.listAvailableStreamsOAuth2(parameters={"appId": f"{appId}"})
        t1 = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S +0000')
        headers = {
            'Authorization': 'Token %s' % (
                avail["body"]["resources"][0]["sessionToken"]["token"]
                ), 'Date': t1, 'Connection': 'Keep-Alive'
            }
        stream = requests.get(avail["body"]["resources"][0]["dataFeedURL"], headers=headers, stream=True)
        with stream:
            result = falcon.refreshActiveStreamSession(appId=f"{appId}",
                                                       action_name="refresh_active_stream_session",
                                                       partition="0"
                                                       )
            if result["status_code"] in AllowedResponses:
                return True
            else:
                return False

    def serviceStream_GenerateErrors(self):
        falcon.base_url = "nowhere"
        errorChecks = True
        if falcon.listAvailableStreamsOAuth2(parameters={})["status_code"] != 500:
            errorChecks = False
        if falcon.refreshActiveStreamSession(parameters={}, partition=0)["status_code"] != 500:
            errorChecks = False

        return errorChecks

    def serviceStream_Logout(self):
        if falcon.auth_object.revoke(falcon.auth_object.token()["body"]["access_token"])["status_code"] == 200:
            return True
        else:
            return False

    def test_list(self):
        assert self.serviceStream_listAvailableStreamsOAuth2() is True

    @pytest.mark.skipif(sys.version_info.minor < 9, reason="Frequency reduced due to test flakiness")
    def test_refresh(self):
        assert self.serviceStream_refreshActiveStreamSession() is True

    def test_logout(self):
        assert self.serviceStream_Logout() is True

    def test_errors(self):
        assert self.serviceStream_GenerateErrors() is True
