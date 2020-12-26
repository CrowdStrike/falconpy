# test_event_streams.py
# This class tests the event_streams service class

import json
import os
import sys
import datetime
import requests
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

#Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import event_streams as FalconStream

auth = Authorization.TestAuthorization()
auth.serviceAuth()
falcon = FalconStream.Event_Streams(access_token=auth.token)

class TestEventStreams:

    def serviceStream_listAvailableStreamsOAuth2(self):
        appId = "pytest-event_streams-unit-test"
        if falcon.listAvailableStreamsOAuth2(parameters={"appId":appId})["status_code"] == 200:
            return True
        else:
            return False

    def serviceStream_refreshActiveStreamSession(self):
        appId = "pytest-event_streams-unit-test"
        avail = falcon.listAvailableStreamsOAuth2(parameters={"appId":appId})
        t1 = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S +0000')
        headers = {'Authorization': 'Token %s' % (avail["body"]["resources"][0]["sessionToken"]["token"]), 'Date': t1, 'Connection': 'Keep-Alive'}
        stream = requests.get(avail["body"]["resources"][0]["dataFeedURL"], headers=headers, stream=True)
        with stream:
            if falcon.refreshActiveStreamSession(parameters={"appId": appId, "action_name":"refresh_active_stream_session"}, partition=0)["status_code"] == 200:
                return True
            else:
                return False

    def test_listAvailableStreamsOAuth2(self):
        assert self.serviceStream_listAvailableStreamsOAuth2() == True

    def test_refreshActiveStreamSession(self):
        assert self.serviceStream_refreshActiveStreamSession() == True

    def test_logout(self):
        assert auth.serviceRevoke() == True