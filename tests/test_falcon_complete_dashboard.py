# test_falcon_complete_dashboard.py
# This class tests the falcon_complete_dashboard service class
import os
import sys

# Authentication via test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CompleteDashboard

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CompleteDashboard(auth_object=config)
AllowedResponses = [200, 403, 429]


class TestFalconCompleteDashboard:
    def ServiceFCD_QueryAlertIdsByFilter(self, ver: int = 1):
        returned = False
        if ver == 1:
            if falcon.QueryAlertIdsByFilterV1()["status_code"] in AllowedResponses:
                returned = True
        else:
            if falcon.QueryAlertIdsByFilterV2()["status_code"] in AllowedResponses:
                returned = True

        return returned

    def ServiceFCD_QueryAllowListFilter(self):
        returned = False
        if falcon.QueryAllowListFilter()["status_code"] in AllowedResponses:
            returned = True

        return returned

    def ServiceFCD_QueryBlockListFilter(self):
        returned = False
        if falcon.QueryBlockListFilter()["status_code"] in AllowedResponses:
            returned = True

        return returned

    def ServiceFCD_QueryDetectionIdsByFilter(self):
        returned = False
        if falcon.QueryDetectionIdsByFilter(bananas="yellow")["status_code"] in AllowedResponses:
            returned = True

        return returned

    def ServiceFCD_GetDeviceCountCollectionQueriesByFilter(self):
        returned = False
        if falcon.GetDeviceCountCollectionQueriesByFilter(parameters={"limit": 1})["status_code"] in AllowedResponses:
            returned = True

        return returned

    def ServiceFCD_QueryEscalationsFilter(self):
        returned = False
        if falcon.QueryEscalationsFilter(limit=1,offset=2)["status_code"] in AllowedResponses:
            returned = True

        return returned

    def ServiceFCD_QueryIncidentIdsByFilter(self):
        returned = False
        if falcon.QueryIncidentIdsByFilter(bananas="yellow")["status_code"] in AllowedResponses:
            returned = True

        return returned

    def ServiceFCD_QueryRemediationsFilter(self):
        returned = False
        if falcon.QueryRemediationsFilter(bananas="yellow")["status_code"] in AllowedResponses:
            returned = True

        return returned

    def ServiceFCD_GenerateErrors(self):
        falcon.base_url = "nowhere"
        error_checks = True
        tests = {
            "AggregateAlerts": falcon.aggregate_alerts(),
            "AggregateAllowList": falcon.aggregate_allow_list(),
            "AggregateBlockList": falcon.aggregate_block_list(),
            "AggregateDetections": falcon.aggregate_detections(),
            "AggregateDeviceCountCollection": falcon.aggregate_device_count_collection(),
            "AggregateEscalations": falcon.aggregate_escalations(),
            "AggregateFCIncidents": falcon.aggregate_fc_incidents(),
            "AggregateRemediations": falcon.aggregate_remediations(),
            "AggregatePreventionPolicy": falcon.aggregate_prevention_policy(),
            "AggregateSensorUpdatePolicy": falcon.aggregate_sensor_update_policy(),
            "AggregateSupportIssues": falcon.aggregate_support_issues(),
            "AggregateTotalDeviceCounts": falcon.aggregate_total_device_counts()

        }
        for key in tests:
            if tests[key]["status_code"] != 500:
                error_checks = False

        return error_checks

    def test_QueryAlertIdsByFilter(self):
        assert self.ServiceFCD_QueryAlertIdsByFilter() is True

    def test_QueryAlertIdsByFilterV2(self):
        assert self.ServiceFCD_QueryAlertIdsByFilter(2) is True

    def test_QueryAllowListFilter(self):
        assert self.ServiceFCD_QueryAllowListFilter() is True

    def test_QueryBlockListFilter(self):
        assert self.ServiceFCD_QueryBlockListFilter() is True

    def test_QueryDetectionIdsByFilter(self):
        assert self.ServiceFCD_QueryDetectionIdsByFilter() is True

    def test_GetDeviceCountCollectionQueriesByFilter(self):
        assert self.ServiceFCD_GetDeviceCountCollectionQueriesByFilter() is True

    def test_QueryEscalationsFilter(self):
        assert self.ServiceFCD_QueryEscalationsFilter() is True

    def test_QueryIncidentIdsByFilter(self):
        assert self.ServiceFCD_QueryIncidentIdsByFilter() is True

    def test_QueryRemediationsFilter(self):
        assert self.ServiceFCD_QueryRemediationsFilter() is True

    def test_Errors(self):
        assert self.ServiceFCD_GenerateErrors() is True
