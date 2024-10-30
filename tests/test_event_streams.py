"""
test_event_streams.py - This class tests the event_streams service class
"""
# pylint: disable=E0401,C0413
import os
import sys
import datetime
from datetime import datetime, timezone
import platform
import requests
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
# flake8: noqa=E402
from falconpy import EventStreams

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = EventStreams(auth_object=config)

AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now
APP_ID = "pytest-event_streams-unit-test"


class TestEventStreams:
    """Test harness for the Event Streams service class"""
    @staticmethod
    def stream_list():
        """list_available_streams"""
        return bool(falcon.listAvailableStreamsOAuth2(
                    app_id=APP_ID
                    )["status_code"] in AllowedResponses)

    @staticmethod
    def stream_refresh():
        """refresh_active_stream"""
        avail = falcon.listAvailableStreamsOAuth2(parameters={"appId": f"{APP_ID}"})
        current_time = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S +0000')
        if avail["body"]["resources"]:
            headers = {
                'Authorization': 'Token %s' % (
                    avail["body"]["resources"][0]["sessionToken"]["token"]
                    ), 'Date': current_time, 'Connection': 'Keep-Alive'
                }
            stream = requests.get(avail["body"]["resources"][0]["dataFeedURL"], headers=headers, stream=True)
            with stream:
                result = falcon.refreshActiveStreamSession(app_id=f"{APP_ID}",
                                                        action_name="refresh_active_stream_session",
                                                        partition=0
                                                        )
                return bool(result["status_code"] in AllowedResponses)
        else:
            pytest.skip("Rate limited")

    @staticmethod
    def stream_refresh_default_action():
        """refresh_active_stream"""
        avail = falcon.listAvailableStreamsOAuth2(parameters={"appId": f"{APP_ID}"})
        current_time = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S +0000')
        if avail["body"]["resources"]:
            headers = {
                'Authorization': 'Token %s' % (
                    avail["body"]["resources"][0]["sessionToken"]["token"]
                    ), 'Date': current_time, 'Connection': 'Keep-Alive'
                }

            stream = requests.get(avail["body"]["resources"][0]["dataFeedURL"], headers=headers, stream=True)
            with stream:
                result = falcon.refreshActiveStreamSession(appId=f"{APP_ID}",
                                                        partition="0"
                                                        )
                return bool(result["status_code"] in AllowedResponses)
        else:
            pytest.skip("Rate limited")

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

    def test_list(self):
        """Pylint test harness hook"""
        assert self.stream_list() is True

    # @pytest.mark.skipif(sys.version_info.minor < 10, reason="Frequency reduced due to test flakiness")
    @pytest.mark.skipif(platform.system() != "Darwin", reason="Frequency reduced due to test flakiness")
    def test_refresh(self):
        """Pytest harness hook"""
        assert self.stream_refresh() is True

    # @pytest.mark.skipif(sys.version_info.minor < 10, reason="Frequency reduced due to test flakiness")
    @pytest.mark.skipif(platform.system() != "Darwin", reason="Frequency reduced due to test flakiness")
    def test_default_refresh(self):
        """Pytest harness hook"""
        assert self.stream_refresh_default_action() is True


    def test_errors(self):
        """Pytest harness hook"""
        assert self.stream_errors() is True

    # @staticmethod
    # def test_logout():
    #     """Pytest harness hook"""
    #     assert bool(falcon.auth_object.revoke(
    #         falcon.auth_object.token()["body"]["access_token"]
    #         )["status_code"] in AllowedResponses) is True
