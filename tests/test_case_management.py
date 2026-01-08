# test_case_management.py
# This class tests the CaseManagement service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CaseManagement

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CaseManagement(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 404, 429]


class TestCaseManagement:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "aggregates_file_details_post_v1": falcon.aggregates_file_details_post_v1(ids="1234567890", filter="whatever"),
            "combined_file_details_get_v1": falcon.query_file_details(filter="whatever", limit=10, offset=0),
            "entities_file_details_get_v1": falcon.get_file_details(ids="1234567890"),
            "entities_file_details_patch_v1": falcon.update_file_details(id="12345678", description="whatever"),
            "entities_files_bulk_download_post_v1": falcon.bulk_download_files(ids="1234567"),
            "entities_files_download_get_v1": falcon.download_existing_files(id="1234567890"),
            "entities_files_upload_post_v1": falcon.upload_file(file="nonexistent_file.txt", description="test", case_id="123"),
            "entities_files_upload_post_v1_no_file": falcon.upload_file(description="test", case_id="123"),
            "entities_files_delete_v1": falcon.delete_file_details(ids="1234567890"),
            "queries_file_details_get_v1": falcon.query_file_detail_ids(filter="whatever", limit=10, offset=0),
            "aggregates_notification_groups_post_v1": falcon.get_notification_groups_aggregation(**{"date_ranges": {},
                                                                                                    "from": 0,
                                                                                                    "field": "whatever",
                                                                                                    "filter": "whatever",
                                                                                                    "name": "whatever",
                                                                                                    "size": 0,
                                                                                                    "sort": "whatever",
                                                                                                    "type": "terms"}),
            "aggregates_notification_groups_post_v2": falcon.get_notification_groups_aggregation_v2(**{"date_ranges": {},
                                                                                                       "from": 0,
                                                                                                       "field": "whatever",
                                                                                                       "filter": "whatever",
                                                                                                       "name": "whatever",
                                                                                                       "size": 0,
                                                                                                       "sort": "whatever",
                                                                                                       "type": "terms"}),
            "aggregates_slas_post_v1": falcon.get_sla_aggregations(**{"date_ranges": {},
                                                                      "from": 0,
                                                                      "field": "whatever",
                                                                      "filter": "whatever",
                                                                      "name": "whatever",
                                                                      "size": 0,
                                                                      "sort": "whatever",
                                                                      "type": "terms"}),
            "aggregates_templates_post_v1": falcon.get_template_aggregations(**{"date_ranges": {},
                                                                                "from": 0,
                                                                                "field": "whatever",
                                                                                "filter": "whatever",
                                                                                "name": "whatever",
                                                                                "size": 0,
                                                                                "sort": "whatever",
                                                                                "type": "terms"}),
            "entities_fields_get_v1": falcon.get_fields(ids=["1234567890"]),
            "entities_notification_groups_get_v1": falcon.get_notification_groups(ids=["1234567890"]),
            "entities_notification_groups_get_v2": falcon.get_notification_groups_v2(ids=["1234567890"]),
            "entities_notification_groups_post_v1": falcon.create_notification_group(name="whatever", description="whatever", channels={"config_id": "123", "type": "email"}),
            "entities_notification_groups_patch_v1": falcon.update_notification_group(id="1234567", name="whatever", description="whatever", channels=[{"config_id": "123", "type": "email"}]),
            "entities_notification_groups_delete_v1": falcon.delete_notification_group(ids=["1234567890"]),
            "entities_notification_groups_post_v2": falcon.create_notification_group_v2(name="whatever", description="whatever", channels={"config_id": "123", "type": "email", "params": {}}),
            "entities_notification_groups_patch_v2": falcon.update_notification_group_v2(id="1234567", name="whatever", description="whatever", channels=[{"config_id": "123", "type": "email", "params": {}}]),
            "entities_notification_groups_delete_v2": falcon.delete_notification_group_v2(ids=["1234567890"]),
            "entities_slas_get_v1": falcon.get_slas(ids="1234567890"),
            "entities_slas_post_v1": falcon.create_sla(description="whatever", name="whatever", goals={"duration_seconds": 0, "type": "whatever"}),
            "entities_slas_patch_v1": falcon.update_sla(description="whatever", name="whatever", goals={"duration_seconds": 0, "type": "whatever", "escalation_policy": {"steps": [{"escalate_after_seconds": 0, "notification_group_id": "1234567"}]}}),
            "entities_slas_delete_v1": falcon.delete_sla(ids="1234567890"),
            "entities_template_snapshots_get_v1": falcon.get_template_snapshots(template_ids="1234567890", ids="1234567890", versions=0),
            "entities_templates_export_get_v1": falcon.export_templates(ids="1234567890", filter="whatever", **{"format": "json"}),
            "entities_files_upload_post_v1_success": falcon.upload_file(file="README.md", description="whatever", case_id="124567"),
            "entities_templates_import_post_v1": falcon.import_template(file="README.md", dry_run=True),
            "entities_templates_import_post_v1_no_file": falcon.import_template(dry_run=True),
            "entities_templates_import_post_v1_bad_file": falcon.import_template(file="nonexistent_template.txt", dry_run=True),
            "entities_templates_get_v1": falcon.get_templates(ids="1234567890"),
            "entities_templates_post_v1": falcon.create_template(description="whatever", name="whatever", sla_id="1234567890", fields={"name": "whatever", "data_type": "whatever"}),
            "entities_templates_patch_v1": falcon.update_template(id="1234567", name="whatever", sla_id="1234567890", description="whatever", fields={"name": "whatever", "data_type": "whatever", "id": "1234567", "input_type": "whatever", "multivalued": True, "default_value": "1234567", "options": [{"id": "1234567", "value": "whatever"}], "required": True}),
            "entities_templates_delete_v1": falcon.delete_templates(ids="1234567890"),
            "queries_fields_get_v1": falcon.query_fields(filter="whatever", limit=10, offset=0),
            "queries_notification_groups_get_v1": falcon.query_notification_groups(filter="whatever", sort="name", limit=10, offset=0),
            "queries_notification_groups_get_v2": falcon.query_notification_groups_v2(filter="whatever", sort="name", limit=10, offset=0),
            "queries_slas_get_v1": falcon.query_slas(filter="whatever", sort="name", limit=10, offset=0),
            "queries_template_snapshots_get_v1": falcon.query_template_snapshots(filter="whatever", limit=10, offset=0),
            "queries_templates_get_v1": falcon.query_templates(filter="whatever", sort="name", limit=10, offset=0),
            "entities_alert_evidence_post_v1": falcon.add_case_alert_evidence(id="1234567", alerts={"id": "1234567"}),
            "entities_case_tags_post_v1": falcon.add_case_tags(id="1234567", tags=["whatever"]),
            "entities_case_tags_delete_v1": falcon.delete_case_tags(id="1234567890", tag="todo"),
            "entities_cases_put_v2": falcon.create_case(name="whatever", description="whatever", assigned_to_user_uuid="whatever", evidence={}, severity=0, status="whatever", tags=["whatever"], template={"id": "1234567"}),
            "entities_cases_post_v2": falcon.get_cases(ids="ids"),
            "entities_cases_patch_v2": falcon.update_case_fields(id="1234567", expected_consistency_version=0, expected_version=0, fields={}),
            "entities_event_evidence_post_v1": falcon.add_case_event_evidence(id="12345678", events=[{"id": "123"}]),
            "queries_cases_get_v1": falcon.query_case_ids(limit=10, offset=0, sort="name", filter="whatever", q="search")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
