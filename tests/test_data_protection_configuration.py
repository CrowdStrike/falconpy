# test_data_protection_configuration.py
# This class tests the DataProtectionConfiguration service class

# import json
import os
import sys
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import DataProtectionConfiguration

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = DataProtectionConfiguration(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestDataProtectionConfiguration:
    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "entities_classification_get_v2": falcon.get_classification(ids="test-id"),
            "entities_classification_post_v2": falcon.create_classification(body={}),
            "entities_classification_patch_v2": falcon.update_classifications(body={}),
            "entities_classification_delete_v2": falcon.delete_classification(ids="test-id"),

            "entities_cloud_application_get": falcon.get_cloud_application(ids="test-id"),
            "entities_cloud_application_create": falcon.create_cloud_application(body={}),
            "entities_cloud_application_patch": falcon.update_cloud_application(id="test-id", body={}),
            "entities_cloud_application_delete": falcon.delete_cloud_application(ids="test-id"),

            "entities_content_pattern_get": falcon.get_content_pattern(ids="test-id"),
            "entities_content_pattern_create": falcon.create_content_pattern(body={}),
            "entities_content_pattern_patch": falcon.update_content_pattern(id="test-id", body={}),
            "entities_content_pattern_delete": falcon.delete_content_pattern(ids="test-id"),

            "entities_enterprise_account_get": falcon.get_enterprise_account(ids="test-id"),
            "entities_enterprise_account_create": falcon.create_enterprise_account(body={}),
            "entities_enterprise_account_patch": falcon.update_enterprise_account(body={}),
            "entities_enterprise_account_delete": falcon.delete_enterprise_account(ids="test-id"),

            "entities_file_type_get": falcon.get_file_type(ids="test-id"),

            "entities_sensitivity_label_get_v2": falcon.get_sensitivity_label(ids="test-id"),
            "entities_sensitivity_label_create_v2": falcon.create_sensitivity_label(body={}),
            "entities_sensitivity_label_delete_v2": falcon.delete_sensitivity_label(ids="test-id"),

            "entities_policy_get_v2": falcon.get_policies(ids="test-id"),
            "entities_policy_post_v2": falcon.create_policy(platform_name="win", body={}),
            "entities_policy_patch_v2": falcon.update_policies(platform_name="win", body={}),
            "entities_policy_delete_v2": falcon.delete_policies(ids="test-id", platform_name="win"),

            "entities_web_location_get_v2": falcon.get_web_location(ids="test-id"),
            "entities_web_location_create_v2": falcon.create_web_location(body={}),
            "entities_web_location_patch_v2": falcon.update_web_location(id="test-id", body={}),
            "entities_web_location_delete_v2": falcon.delete_web_location(ids="test-id"),

            "queries_classification_get_v2": falcon.query_classifications(),
            "queries_cloud_application_get_v2": falcon.query_cloud_applications(),
            "queries_content_pattern_get_v2": falcon.query_content_patterns(),
            "queries_enterprise_account_get_v2": falcon.query_enterprise_accounts(),
            "queries_file_type_get_v2": falcon.query_file_type(),
            "queries_sensitivity_label_get_v2": falcon.query_sensitivity_label(),
            "queries_policy_get_v2": falcon.query_policies(platform_name="win"),
            "queries_web_location_get_v2": falcon.query_web_locations(),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
