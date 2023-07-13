# test_recon.py
# This class tests the Falcon X Recon service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import Recon

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = Recon(auth_object=config)

AllowedResponses = [200, 201, 400, 403, 404, 429, 500]


class TestRecon:
    def service_recon_run_all_tests(self):

        error_checks = True
        tests = {
            "aggregate_notifications": falcon.aggregate_notifications(body={}),
            "aggregate_notifications_exposed": falcon.aggregate_notifications_exposed_data_records(body={}),
            "preview_rule": falcon.preview_rule(body={}),
            "preview_rule_jr": falcon.preview_rule(filter="something", topic="somethingElse"),
            "get_actions": falcon.get_actions(ids='12345678'),
            "create_actions": falcon.create_actions(body={}, recipients="12345,67890", trigger_matchless=False),
            "create_actions_alternatively": falcon.create_actions(frequency="whenevers",
                                                                  recipients=["123456"],
                                                                  type="TheGoodKind"
                                                                  ),
            "create_actions_just_cuz": falcon.create_actions(actions=[
                                            {
                                                "frequency": "sometimes",
                                                "recipients": ["1234567", "8901234"],
                                                "type": "theOtherKind"
                                            }
                                        ]),
            "delete_action": falcon.delete_action(ids="1234567"),
            "update_notifications": falcon.update_notifications(body={"id": "1234567"}),
            "update_notifications_also": falcon.update_notifications(id="1234567",
                                                                     assigned_to_uuid="1234567",
                                                                     status="new"
                                                                     ),
            "update_action": falcon.update_action(body={"id": "1234567",
                                                        "frequency": "whatever",
                                                        "recipients": ["definitely bob"],
                                                        "status": "OhSoVeryUrgent"
                                                        }),
            "update_action_as_well": falcon.update_action(id="1234567",
                                                          frequency="often",
                                                          status="new",
                                                          recipients="123456,654321",
                                                          trigger_matchless=False
                                                          ),
            "get_notifications_detailed_translated": falcon.get_notifications_detailed_translated(ids="1234567"),
            "get_notfications_detailed": falcon.get_notifications_detailed(ids="1234567"),
            "get_notifications_translated": falcon.get_notifications_translated(ids="1234567"),
            "get_notifications_exposed": falcon.get_notifications_exposed_data_records(ids="12345678"),
            "get_notifications": falcon.get_notifications(ids="12345678"),
            "get_export_job_file": falcon.get_export_job_file_contents(ids="12345678"),
            "get_export_job": falcon.get_export_jobs(ids="123456789"),
            "delete_export_job": falcon.delete_export_jobs(ids="12345678"),
            "create_export_job": falcon.create_export_jobs(
                entity="string",
                export_type="string",
                filter="string",
                human_readable=True,
                sort="string"
            ),
            "delete_notifications": falcon.delete_notifications(ids="1234567"),
            "get_rules": falcon.get_rules(ids="12345678"),
            "create_rules": falcon.create_rules(body={}),
            "delete_rules": falcon.delete_rules(ids="12345678"),
            "update_rules": falcon.update_rules(body={}),
            "update_rules_too": falcon.update_rules(filter="whatever",
                                                    id="1234567",
                                                    permissions="public",
                                                    priority="high",
                                                    name="FunGoBat"
                                                    ),
            "update_rules_three": falcon.update_rules(rules=[{
                                                    "filter": "whatever",
                                                    "id": "1234567",
                                                    "permissions": "public",
                                                    "priority": "high",
                                                    "name": "FunGoBat"
                                                    }]),
            "update_rules_four": falcon.update_rules(rules={"filter":"whatevs"},
                                                     filter="sumpthin",
                                                     id="1754251",
                                                     permissions="private",
                                                     priority="moderate",
                                                     name="MelloYellow",
                                                     topic="whatevers",
                                                     breach_monitoring_enabled=False
                                                     ),
            "query_actions": falcon.query_actions(),
            "query_notifications_exposed": falcon.query_notifications_exposed_data_records(),
            "query_notifications": falcon.query_notifications(),
            "query_rules": falcon.query_rules()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                # print(f"{key}: {tests[key]}")
                error_checks = False

        return error_checks

    def test_all_functionality(self):
        assert self.service_recon_run_all_tests() is True
