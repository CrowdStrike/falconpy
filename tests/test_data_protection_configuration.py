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
        
        # Define classification properties
        classification_props = {
            "content_patterns": ["pattern1"],
            "evidence_duplication_enabled": True,
            "file_types": ["pdf", "docx"],
            "protection_mode": "monitor",
            "sensitivity_labels": ["label1"],
            "web_sources": ["source1"]
        }
        
        # Define policy properties
        policy_props = {
            "allow_notifications": "default",
            "block_all_data_access": False,
            "classifications": ["class1"],
            "enable_content_inspection": True,
            "enable_network_inspection": True,
            "inspection_depth": "balanced",
            "min_confidence_level": "low"
        }
        
        tests = {
            "entities_classification_get_v2": falcon.get_classification(ids="test-id"),
            "entities_classification_post_v2": falcon.create_classification(name="test-classification", classification_properties=classification_props),
            "entities_classification_patch_v2": falcon.update_classifications(name="updated-classification", classification_properties=classification_props),
            "entities_classification_delete_v2": falcon.delete_classification(ids="test-id"),

            "entities_cloud_application_get": falcon.get_cloud_application(ids="test-id"),
            "entities_cloud_application_create": falcon.create_cloud_application(description="test app",
                                                                                 name="test-cloud-app",
                                                                                 urls={"fqdn": "example.com", "path": "/api"}
                                                                                 ),
            "entities_cloud_application_patch": falcon.update_cloud_application(id="test-id",
                                                                                description="updated app",
                                                                                name="updated-cloud-app",
                                                                                urls={"fqdn": "example2.com", "path": "/api/v2"}
                                                                                ),
            "entities_cloud_application_delete": falcon.delete_cloud_application(ids="test-id"),

            "entities_content_pattern_get": falcon.get_content_pattern(ids="test-id"),
            "entities_content_pattern_create": falcon.create_content_pattern(category="pii",
                                                                             description="test pattern",
                                                                             example="123-45-6789",
                                                                             min_match_threshold=1,
                                                                             name="test-pattern",
                                                                             regexes=["\\d{3}-\\d{2}-\\d{4}"],
                                                                             region="us-east-1"
                                                                             ),
            "entities_content_pattern_patch": falcon.update_content_pattern(id="test-id",
                                                                            category="phi",
                                                                            description="updated pattern",
                                                                            example="987-65-4321",
                                                                            min_match_threshold=2,
                                                                            name="updated-pattern",
                                                                            regexes=["\\d{3}-\\d{2}-\\d{4}"],
                                                                            region="us-west-2"
                                                                            ),
            "entities_content_pattern_delete": falcon.delete_content_pattern(ids="test-id"),

            "entities_enterprise_account_get": falcon.get_enterprise_account(ids="test-id"),
            "entities_enterprise_account_create": falcon.create_enterprise_account(application_group_id="group123",
                                                                                   domains=["example.com"],
                                                                                   name="test-enterprise",
                                                                                   plugin_config_id="config123"
                                                                                   ),
            "entities_enterprise_account_patch": falcon.update_enterprise_account(application_group_id="group456",
                                                                                  domains=["example2.com"],
                                                                                  name="updated-enterprise",
                                                                                  plugin_config_id="config456"
                                                                                  ),
            "entities_enterprise_account_delete": falcon.delete_enterprise_account(ids="test-id"),

            "entities_file_type_get": falcon.get_file_type(ids="test-id"),

            "entities_sensitivity_label_get_v2": falcon.get_sensitivity_label(ids="test-id"),
            "entities_sensitivity_label_create_v2": falcon.create_sensitivity_label(co_authoring=True,
                                                                                    display_name="Confidential",
                                                                                    external_id="ext123",
                                                                                    label_provider="provider1",
                                                                                    name="test-label",
                                                                                    plugins_configuration_id="plugin123",
                                                                                    synced=True
                                                                                    ),
            "entities_sensitivity_label_delete_v2": falcon.delete_sensitivity_label(ids="test-id"),

            "entities_policy_get_v2": falcon.get_policies(ids="test-id"),
            "entities_policy_post_v2": falcon.create_policy(resources=[]),
            "entities_policy_post_v2": falcon.create_policy(platform_name="win", description="test policy", name="test-policy", policy_properties=policy_props, precedence=1),
            "entities_policy_patch_v2": falcon.update_policies(platform_name="win", description="updated policy", name="updated-policy", policy_properties=policy_props, precedence=2),
            "entities_policy_delete_v2": falcon.delete_policies(ids="test-id", platform_name="win"),

            "entities_web_location_get_v2": falcon.get_web_location(ids="test-id"),
            "entities_web_location_create_v2": falcon.create_web_location(application_id="app123",
                                                                          deleted=False,
                                                                          enterprise_account_id="ent123",
                                                                          location_type="cloud",
                                                                          name="test-location",
                                                                          provider_location_id="prov123",
                                                                          provider_location_name="provider-loc",
                                                                          type="custom"
                                                                          ),
            "entities_web_location_patch_v2": falcon.update_web_location(id="test-id",
                                                                         application_id="app456",
                                                                         deleted=False,
                                                                         enterprise_account_id="ent456",
                                                                         location_type="on-prem",
                                                                         ame="updated-location",
                                                                         provider_location_id="prov456",
                                                                         provider_location_name="updated-provider-loc",
                                                                         type="predefined"
                                                                         ),
            "entities_web_location_delete_v2": falcon.delete_web_location(ids="test-id"),

            "queries_classification_get_v2": falcon.query_classifications(filter="name:'test'", offset=0, limit=50, sort="name|asc"),
            "queries_cloud_application_get_v2": falcon.query_cloud_applications(filter="name:'test'", sort="name|asc", limit=50, offset=0),
            "queries_content_pattern_get_v2": falcon.query_content_patterns(filter="category:'pii'", sort="name|asc", limit=50, offset=0),
            "queries_enterprise_account_get_v2": falcon.query_enterprise_accounts(filter="name:'test'", sort="name|asc", limit=50, offset=0),
            "queries_file_type_get_v2": falcon.query_file_type(filter="name:'pdf'", sort="name|asc", limit=50, offset=0),
            "queries_sensitivity_label_get_v2": falcon.query_sensitivity_label(filter="name:'test'", sort="name|asc", limit=50, offset=0),
            "queries_policy_get_v2": falcon.query_policies(platform_name="win", filter="name:'test'", offset=0, limit=50, sort="name|asc"),
            "queries_web_location_get_v2": falcon.query_web_locations(filter="name:'test'", type="custom", limit=50, offset=0),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
