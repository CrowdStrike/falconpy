# test_content_update_policies.py
# This class tests the content_update_policies service class

# import json
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ContentUpdatePolicies

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ContentUpdatePolicies(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestContentUpdatePolicies:
    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "queryCombinedContentUpdatePolicyMembers": falcon.query_policy_members_combined(limit=1),
            "queryCombinedContentUpdatePolicies": falcon.query_policies_combined(limit=1),
            "performContentUpdatePoliciesAction": falcon.perform_action(ids="12345678", action_parameters={"name": "whatever", "value": "whatever"}),
            "setContentUpdatePoliciesPrecedence": falcon.set_precedence(ids="1,2"),
            "getContentUpdatePolicies": falcon.get_policies(ids="12345678"),
            "createContentUpdatePolicies": falcon.create_policies(description="whatever", name="whatever"),
            "updateContentUpdatePolicies": falcon.update_policies(description="whatever", name="whatever", id="12345678"),
            "deleteContentUpdatePolicies": falcon.delete_policies(ids="12345678"),
            "queryContentUpdatePolicyMembers": falcon.query_policy_members(limit=1),
            "queryPinnableContentVersions": falcon.query_pinnable_content_versions(category="system_critical"),
            "queryContentUpdatePolicies": falcon.query_policies(limit=1),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
