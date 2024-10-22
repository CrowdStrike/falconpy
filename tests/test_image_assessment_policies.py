# test_image_assessment_policies.py
# This class tests the image assessment policies service class

# import json
import os
import sys
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import ImageAssessmentPolicies

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ImageAssessmentPolicies(auth_object=config)
AllowedResponses = [200, 201, 204, 207, 400, 403, 502]  # Allowing 502 from CreatePolicyGroups for now


class TestImageAssessmentPolicies:
    @pytest.mark.skipif(config.base_url == "https://api.us-2.crowdstrike.com",
                        reason="Unit testing unavailable on US-2"
                        )
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "ReadPolicies": falcon.read_policies(),
            "CreatePolicies": falcon.create_policies(description="whatever"),
            "UpdatePolicies": falcon.update_policies(name="whatever", is_enabled=False, rules=[], policy_data={}),
            "UpdatePolicies": falcon.update_policies(name="whatever", is_enabled=False, rules={}, policy_data={}),
            "ReadPolicyExclusions": falcon.read_policy_exclusions(),
            "UpdatePolicyExclusions": falcon.update_policy_exclusions(description="whatever", conditions=[]),
            "ReadPolicyGroups": falcon.read_policy_groups(),
            "CreatePolicyGroups": falcon.create_policy_groups(name="whatever", policy_id="1234567"),
            "UpdatePolicyGroups": falcon.update_policy_groups(id="12345678", description="something", policy_group_data={}),
            "UpdatePolicyGroups": falcon.update_policy_groups(id="12345678", description="something", conditions={"whatever": "something"}),
            "DeletePolicyGroup": falcon.delete_policy_group(id="1234567"),
            "UpdatePolicyPrecedence": falcon.update_policy_precedence(precedence="123457,8765542"),
        }
        if tests["CreatePolicies"]["status_code"] == 200:
            tests["DeletePolicy"] = falcon.delete_policy(tests["CreatePolicies"]["body"]["resources"][0]["policy_id"])
        else:
            tests["DeletePolicy"] = falcon.delete_policy("12345678")
        for key in tests:

            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
