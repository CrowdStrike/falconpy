"""This class tests the MessageCenter service class"""
import os
import sys
import pytest
# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import MessageCenter

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = MessageCenter(auth_object=config)
AllowedResponses = [200, 400, 403, 429, 405, 500]  # pre-1.2.16 - UpdateCase appears to be decomm'd


class TestMessageCenter:
    """Message Center Service Class test harness"""
    def message_center_full_series(self):
        """Test code paths within all methods."""
        error_checks = True
        FILENAME = "tests/testfile.png"
        PAYLOAD = open(FILENAME, 'rb').read()
        tests = {
            "aggregate_cases": falcon.aggregate_cases(body={}),
            "get_case_activity": falcon.get_case_activity(ids="12345678"),
            "add_case_activity": falcon.add_case_activity(content="This is the case body",
                                                          case_id="12345678",
                                                          activity_type="whatever",
                                                          user_uuid="bob@nowhere.com"
                                                          ),
            "download_case_attachment": falcon.download_case_attachment(ids="12345678"),
            "add_case_attachment": falcon.add_case_attachment(case_id="12345678",
                                                              file_data=PAYLOAD,
                                                              user_uuid="bob@nowhere.com",
                                                              ),
            "add_case_attachment2": falcon.add_case_attachment(case_id="12345678",
                                                               upfile=PAYLOAD,
                                                               user_uuid="bob@nowhere.com",
                                                               file_name="testfile.png"
                                                               ),
            "add_case_attachment3": falcon.add_case_attachment(case_id="12345678",
                                                               user_uuid="bob@nowhere.com",
                                                               file_name="testfile.png"
                                                               ),
            "create_case_v2": falcon.create_case_v2(content="Case content goes here",
                                              detections={
                                                  "id": "123456",
                                                  "url": "https://somewhere.com"
                                              },
                                              incidents={
                                                  "id": "12345",
                                                  "url": "https://somewhereelse.com"
                                              },
                                              title="This is the case title",
                                              case_type="Case type",
                                              user_uuid="larry@somewhere.com"
                                              ),
            "get_cases": falcon.get_cases(ids="12345678,9876543"),
            "query_activities": falcon.query_activities(limit=1),
            "query_cases": falcon.query_cases(limit=1)
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False

                # print(f"{key} processed with a {tests[key]} response")

        return error_checks

    @pytest.mark.skipif(auth.authorization.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_methods(self):
        """Pytest harness hook."""
        assert self.message_center_full_series() is True
