# test_cloud_aws_registration.py
# This class tests the cloud_aws_registration service class

# import json
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import CloudAWSRegistration

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CloudAWSRegistration(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestCloudAWSRegistration:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "cloud_registration_aws_trigger_health_check": falcon.trigger_health_check(account_ids="whatever", organization_ids="whatever"),
            "cloud_registration_aws_get_accounts": falcon.get_accounts(ids="12345678"),
            "cloud_registration_aws_create_account": falcon.create_account(account_type="whatever", csp_events=False, products={"product": "whatever"}),
            "cloud_registration_aws_update_account": falcon.update_account(account_type="whatever", csp_events=True),
            "cloud_registration_aws_delete_account": falcon.delete_account(organization_ids="12345678"),
            "cloud_registration_aws_validate_accounts": falcon.validate_accounts(account_id="whatever", iam_role_arn="whatever"),
            "cloud_registration_aws_query_accounts": falcon.query_accounts(products="whatever", features="whatever"),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                if not (key == "cloud_registration_aws_delete_account" and tests[key]["status_code"] == 500):
                    error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
