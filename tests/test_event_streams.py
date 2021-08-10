"""
test_event_streams.py - This class tests the event_streams service class
"""
# pylint: disable=E0401,C0413
import os
import sys
import datetime
import platform
import requests
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
# flake8: noqa=E402
from falconpy.event_streams import Event_Streams

auth = Authorization.TestAuthorization()
# Moving to credential authentication
auth.getConfig()
falcon = Event_Streams(creds={"client_id": auth.config["falcon_client_id"],
                              "client_secret": auth.config["falcon_client_secret"]})

AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now
APP_ID = "pytest-event_streams-unit-test"


class TestEventStreams:
    """Test harness for the Event Streams service class"""
    @staticmethod
    def stream_list():
        """list_available_streams"""
        return bool(falcon.listAvailableStreamsOAuth2(
                parameters={"appId": f"{APP_ID}"}
                )["status_code"] in AllowedResponses)

    @staticmethod
    def stream_refresh():
        """refresh_active_stream"""
        avail = falcon.listAvailableStreamsOAuth2(parameters={"appId": f"{APP_ID}"})
        current_time = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S +0000')
        headers = {
            'Authorization': 'Token %s' % (
                avail["body"]["resources"][0]["sessionToken"]["token"]
                ), 'Date': current_time, 'Connection': 'Keep-Alive'
            }
        stream = requests.get(avail["body"]["resources"][0]["dataFeedURL"], headers=headers, stream=True)
        with stream:
            result = falcon.refreshActiveStreamSession(appId=f"{APP_ID}",
                                                       action_name="refresh_active_stream_session",
                                                       partition="0"
                                                       )
            return bool(result["status_code"] in AllowedResponses)

    @staticmethod
    def stream_errors():
        """Generates errors to test remaining code paths"""
        falcon.base_url = "nowhere"
        error_checks = True
        if falcon.listAvailableStreamsOAuth2(parameters={})["status_code"] != 500:
            error_checks = False
        if falcon.refreshActiveStreamSession(parameters={}, partition=0)["status_code"] != 500:
            error_checks = False

        return error_checks

    @staticmethod
    def stream_logout():
        """Tests logout and discards the token"""
        return bool(falcon.auth_object.revoke(falcon.auth_object.token()["body"]["access_token"])["status_code"] == 200)

    def test_list(self):
        """Pylint test harness hook"""
        assert self.stream_list() is True

    @pytest.mark.skipif(sys.version_info.minor < 9, reason="Frequency reduced due to test flakiness")
    @pytest.mark.skipif(platform.system() != "Darwin", reason="Frequency reduced due to test flakiness")
    def test_refresh(self):
        """Pylint test harness hook"""
        assert self.stream_refresh() is True

    def test_logout(self):
        """Pylint test harness hook"""
        assert self.stream_logout() is True

    def test_errors(self):
        """Pylint test harness hook"""
        assert self.stream_errors() is True
