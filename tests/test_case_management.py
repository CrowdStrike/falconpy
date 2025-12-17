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
            "aggregates_file_details_post_v1": falcon.aggregates_file_details_post_v1(),
            "combined_file_details_get_v1": falcon.query_file_details(),
            "entities_file_details_get_v1": falcon.get_file_details(ids="1234567890"),
            #"entities_file_details_patch_v1": falcon.update_file_details(body={}),
            "entities_files_bulk_download_post_v1": falcon.bulk_download_files(body={}),
            "entities_files_download_get_v1": falcon.download_existing_files(id="1234567890"),
            #"entities_files_upload_post_v1": falcon.CHECKTHIS_upload_file(),
            "entities_files_delete_v1": falcon.delete_file_details(ids="1234567890"),
            "queries_file_details_get_v1": falcon.query_file_detail_ids(),
            "aggregates_notification_groups_post_v1": falcon.get_notification_groups(body={}),
            "aggregates_notification_groups_post_v2": falcon.get_notification_groups_v2(body={}),
            "aggregates_slas_post_v1": falcon.get_sla_aggregations(body={}),
            "aggregates_templates_post_v1": falcon.get_template_aggregations(body={}),
            "entities_fields_get_v1": falcon.get_fields(ids=["1234567890"]),
            "entities_notification_groups_get_v1": falcon.get_notification_groups(ids=["1234567890"]),
            "entities_notification_groups_post_v1": falcon.create_notification_group(body={}),
            "entities_notification_groups_patch_v1": falcon.update_notification_group(body={}),
            "entities_notification_groups_delete_v1": falcon.delete_notification_group(ids=["1234567890"]),
            "entities_notification_groups_post_v2": falcon.create_notification_group_v2(body={}),
            "entities_notification_groups_patch_v2": falcon.update_notification_group_v2(body={}),
            "entities_notification_groups_delete_v2": falcon.delete_notification_group_v2(ids=["1234567890"]),
            "entities_slas_get_v1": falcon.get_slas(ids="1234567890"),
            "entities_slas_post_v1": falcon.create_sla(body={}),
            "entities_slas_patch_v1": falcon.update_sla(body={}),
            "entities_slas_delete_v1": falcon.delete_sla(ids="1234567890"),
            "entities_template_snapshots_get_v1": falcon.get_template_snapshots(template_ids="1234567890"),
            "entities_templates_export_get_v1": falcon.export_templates(ids="1234567890"),
            "entities_templates_import_post_v1": falcon.import_template(file="README.md"),
            "entities_templates_get_v1": falcon.get_templates(ids="1234567890"),
            "entities_templates_post_v1": falcon.create_template(body={}),
            "entities_templates_patch_v1": falcon.update_template(body={}),
            "entities_templates_delete_v1": falcon.delete_templates(ids="1234567890"),
            "queries_fields_get_v1": falcon.query_fields(),
            "queries_notification_groups_get_v1": falcon.query_notification_groups(),
            "queries_notification_groups_get_v2": falcon.query_notification_groups_v2(),
            "queries_slas_get_v1": falcon.query_slas(),
            "queries_template_snapshots_get_v1": falcon.query_template_snapshots(),
            "queries_templates_get_v1": falcon.query_templates(),
            "entities_alert_evidence_post_v1": falcon.add_case_alert_evidence(body={}),
            "entities_case_tags_post_v1": falcon.add_case_tags(body={}),
            "entities_case_tags_delete_v1": falcon.delete_case_tags(id="1234567890", tag="todo"),
            "entities_cases_put_v2": falcon.create_case(body={}),
            "entities_cases_post_v2": falcon.get_cases(ids="1234567890"),
            "entities_cases_patch_v2": falcon.update_case_fields(body={}),
            "entities_event_evidence_post_v1": falcon.add_case_event_evidence(body={}),
            "queries_cases_get_v1": falcon.query_case_ids()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks