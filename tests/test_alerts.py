# test_alerts.py
# This class tests the Alerts service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import Alerts

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Alerts(auth_object=config)
AllowedResponses = [200, 201, 400, 404, 429]


class TestAlerts:
    def alerts_run_all_tests(self):
        error_checks = True
        tests = {
            "aggregate_alerts": falcon.get_aggregate_alerts(
                date_ranges=[
                    {
                        "from": "string",
                        "to": "string"
                    }
                ],
                field="string",
                filter="string",
                interval="string",
                min_doc_count=0,
                missing="string",
                name="string",
                q="string",
                ranges=[
                    {
                        "From": 0,
                        "To": 0
                    }
                ],
                size=0,
                sort="string",
                sub_aggregates=[
                    "string"
                ],
                time_zone="string",
                type="string"
            ),
            "aggregate_alerts_v2": falcon.get_aggregate_alerts_v2(
                date_ranges=[
                    {
                        "from": "string",
                        "to": "string"
                    }
                ],
                field="string",
                filter="string",
                interval="string",
                min_doc_count=0,
                missing="string",
                name="string",
                q="string",
                ranges=[
                    {
                        "From": 0,
                        "To": 0
                    }
                ],
                size=0,
                sort="string",
                sub_aggregates=[
                    "string"
                ],
                time_zone="string",
                type="string"
            ),
            "update_alerts_v1": falcon.update_alerts_v2(ids="12345678",
                                                     show_in_ui=False,
                                                     action_parameters=[{
                                                         "show_in_ui": False
                                                         }]
                                                     ),
            "update_alerts_v2": falcon.update_alerts_v3(ids="12345678",
                                                     show_in_ui=False,
                                                     action_parameters=[{
                                                            "show_in_ui": False
                                                         }]
                                                     ),  
            "get_alerts_v1": falcon.get_alerts_v1(ids="12345678"),
            "get_alerts_v2": falcon.get_alerts_v2(ids="12345678"),
            "query_alerts_v1": falcon.query_alerts_v1(),
            "query_alerts_v2": falcon.query_alerts_v2()

        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(tests[key])
                # print(f"{key} operation returned a {tests[key]['status_code']} status code")

        return error_checks

    def test_all_functionality(self):
        assert self.alerts_run_all_tests() is True
