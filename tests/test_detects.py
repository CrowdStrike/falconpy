"""test_detects.py - This class tests the detects service class"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import Detects

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Detects(auth_object=config, validate_payloads=True)
AllowedResponses = [200, 400, 404, 429]


class TestDetects:
    """
    Detects Service Class test harness
    """

    def service_detects_get_detect_summaries(self):
        check = falcon.query_detects(parameters={"limit": 1})
        if check["status_code"] == 429:
            pytest.skip("Rate limit hit")
        if check["body"]["resources"]:
            id_list = check["body"]["resources"]
        else:
            id_list = "12345678"
        if falcon.get_detect_summaries(
                body={"ids": id_list}
                )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def service_detects_test_all(self):
        error_checks = True
        check = falcon.query_detects(limit=2)
        if check["status_code"] == 429:
            pytest.skip("Rate Limit hit")
        if check["body"]["resources"]:
            id_list = ",".join(check["body"]["resources"])
        else:
            pytest.skip("Detections API is deprecated")
        if not id_list:
            id_list = ["1234567890"]
        tests = {
            "query_detects": falcon.query_detects(),
            "get_detect_summaries": falcon.get_detect_summaries(body={"ids": ["12345678"]}),
            "get_aggregate_detects": falcon.get_aggregate_detects(body={"resource": {"bad": True}}),
            "update_detects_by_id_2": falcon.update_detects_by_ids(
                                        ids=id_list,
                                        show_in_ui=True, assigned_to_uuid="12345678", status="ignored",
                                        comment="FalconPy unit testing"
                                        ),
            "get_detect_summaries_2": falcon.get_detect_summaries(ids="12345678"),
            "get_detect_summaries_3": falcon.get_aggregate_detects(
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
                )
        }
        for key in tests:
            # print(tests[key])
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(f"{key}: {tests[key]}")
        return error_checks

    def service_detects_test_comment(self):
        # Unrelated to v1.3 updates
        # It appears the assigned_to_uuid value must be specified in order for this test to pass
        id_list = falcon.query_detects(limit=1).get("body").get("resources")
        if not id_list:
            return True  # False
        if falcon.update_detects_by_ids(ids=id_list, comment="FalconPy Unit Testing")["status_code"] in [200, 400]:
            return True
        else:
            return False

    def test_query_detects(self):
        assert bool(
            falcon.query_detects(parameters={"limit": 1})["status_code"] in AllowedResponses
            ) is True

    def test_comment_update(self):
        assert self.service_detects_test_comment() is True

    @pytest.mark.skipif(falcon.query_detects(parameters={"limit": 1})["status_code"] == 429,
                        reason="API rate limit reached"
                        )
    def test_get_detect_summaries(self):
        assert self.service_detects_get_detect_summaries() is True

    def test_all_functionality(self):
        assert self.service_detects_test_all() is True

    def test_validation_failure(self):
        assert bool(
            falcon.update_detects_by_ids(body={
                            "bananas": "Are yellow or green"
                            })["status_code"] in AllowedResponses
        ) is True

    def test_validation_datatype_failure(self):
        assert bool(
            falcon.update_detects_by_ids(body={
                            "ids": "This should be a list"
                            })["status_code"] in AllowedResponses
        ) is True

    def test_validation_invalid_param_failure(self):
        assert bool(
            falcon.get_detect_summaries(body={
                            "ids": ["123456789"],
                            "coffee": "Is delicious"
                            })["status_code"] in AllowedResponses
        ) is True

    def test_validation_disable(self):
        quiet_falcon = Detects(auth_object=config, validate_payloads=False)
        assert bool(
            quiet_falcon.get_detect_summaries(body={
                            "ids": ["123456789"],
                            "coffee": "Is delicious"
                            })["status_code"] in AllowedResponses
        ) is True
