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
            "queries_rules_get_v1": falcon.query_rules(filter="cid:'12345678901234567890123456789012'")
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
