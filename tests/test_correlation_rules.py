# test_correlation_rules.py
# This class tests the correlation rules service class

# import json
import os
import sys
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CorrelationRules

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CorrelationRules(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 401, 404, 429]  # 400, 403, 404, 


class TestCorrelationRules:
    @pytest.mark.skipif(auth.authorization.base_url != "https://api.crowdstrike.com",
                        reason="Unit testing currently only available on US-1"
                        )
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "combined_rules_get_v1": falcon.get_rules_combined(filter="cid:'12345678901234567890123456789012'"),
            "entities_rules_get_v1": falcon.get_rules(ids="1234567890"),
            "entities_rules_post_v1": falcon.create_rule(trigger_on_create=False, name="whatever"),
            "entities_rules_delete_v1": falcon.delete_rules(ids="12345678"),
            "entities_rules_patch_v1": falcon.update_rule(id="12345678", name="whatever_else"),
            "queries_rules_get_v1": falcon.query_rules(filter="cid:'12345678901234567890123456789012'"),
            "aggregates_rule_versions_post_v1": falcon.aggregate_rule_versions(ids="12345678"),
            "combined_rules_get_v2": falcon.get_rules_combined_v2(limit=1),
            "entities_latest_rules_get_v1": falcon.get_latest_rule_versions(rule_ids="12345678"),
            "entities_rule_versions_export_post_v1": falcon.export_rule(sort="rule_id|desc", get_latest=False),
            "entities_rule_versions_import_post_v1": falcon.import_rule(rule={"description": "test_string",
                                                                              "name": "test_string",
                                                                              "search": {
                                                                                 "filter": "string",
                                                                                 "lookback": "string",
                                                                                 "outcome": "string",
                                                                                 "trigger_mode": "string"
                                                                               },
                                                                              }), 
            "entities_rule_versions_publish_patch_v1": falcon.publish_rule_version(id="12345678"),
            "entities_rule_versions_delete_v1": falcon.delete_rule_versions(ids="12345678"),
            "entities_rules_get_v2": falcon.get_rules_v2(ids="12345678"),
            "queries_rules_get_v2": falcon.query_rules_v2(limit=1),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                if key != "entities_rule_versions_import_post_v1" and not (key == "entities_rule_versions_publish_patch_v1" and tests[key]["status_code"] == 502):
                    error_checks = False
                    print(key)
                    print(tests[key])
        assert error_checks
