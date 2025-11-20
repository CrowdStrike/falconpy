"""
test_overwatch_dashboard.py - This class tests the overwatch_dashboard service class
"""
import os
import sys
# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import OverwatchDashboard

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = OverwatchDashboard(auth_object=config)
AllowedResponses = [200, 401, 403, 404, 429]


class TestOverwatchDashboard:
    """
    Overwatch Dashboard Service Class test harness
    """
    def overwatch_generate_errors(self):
        """
        Test code paths within methods by generating 500s, does not hit the API
        """
        falcon.base_url = "nowhere"
        error_checks = True
        tests = {
            "aggregates_events": falcon.AggregatesEvents(body={})["status_code"],
            "aggregates_events_collections": falcon.AggregatesEventsCollections(field="whatevers")["status_code"]
        }
        for key in tests:
            if tests[key] != 500:
                error_checks = False

            # print(f"{key} processed with a {tests[key]} response")

        return error_checks

    def test_aggregates_detections_global_counts(self):
        """
        Pytest harness hook
        """
        assert bool(falcon.AggregatesDetectionsGlobalCounts()["status_code"] in AllowedResponses) is True

    def test_aggregates_incidents_global_counts(self):
        """
        Pytest harness hook
        """
        assert bool(falcon.AggregatesIncidentsGlobalCounts()["status_code"] in AllowedResponses) is True

    def test_aggregates_events_global_counts(self):
        """
        Pytest harness hook
        """
        assert bool(falcon.AggregatesOWEventsGlobalCounts(bananas="yellow")["status_code"] in AllowedResponses) is True

    def test_errors(self):
        """
        Pytest harness hook
        """
        assert self.overwatch_generate_errors() is True

