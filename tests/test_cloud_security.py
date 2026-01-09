# test_cloud_security.py
# This class tests the CloudSecurity service class

# import json
import os
import sys
import pytest

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization

# Classes to test - manually imported from sibling folder
from falconpy import CloudSecurity
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = CloudSecurity(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 404, 429, 500]


class TestCloudPolicies:
    @pytest.mark.skipif(config.base_url == "https://api.laggar.gcw.crowdstrike.com",
                        reason="Unit testing unavailable on US-GOV-1"
                        )
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "combined_cloud_risks": falcon.combined_cloud_risks(filter="severity:'high'", sort="account_id|asc", limit=100, offset=0),
            "ListCloudGroupsExternal": falcon.list_cloud_groups(filter="name:'test'", sort="created_at|desc", offset=0, limit=50),
            "ListCloudGroupsByIDExternal": falcon.list_cloud_groups_by_id(ids="1234567"),
            "CreateCloudGroupExternal": falcon.create_cloud_group(business_impact="high", business_unit="engineering", description="test group", environment="dev", name="test-group", owners=["user1", "user2"], selectors={"cloud_resources": [{"account_ids": ["123"], "cloud_provider": "aws", "filters": {"region": ["us-east-1"], "tags": ["prod"]}}], "images": [{"filters": {"repository": ["repo"], "tag": ["latest"]}, "registry": "registry1"}]}),
            "UpdateCloudGroupExternal": falcon.update_cloud_group(business_impact="medium", business_unit="operations", description="updated group", environment="prod", name="updated-group", owners=["user3", "user4"], selectors={"cloud_resources": [{"account_ids": ["456"], "cloud_provider": "azure", "filters": {"region": ["east-us"], "tags": ["test"]}}], "images": [{"filters": {"repository": ["repo2"], "tag": ["v1.0"]}, "registry": "registry2"}]}),
            "DeleteCloudGroupsExternal": falcon.delete_cloud_groups(ids="1234567"),
            "ListCloudGroupIDsExternal": falcon.list_group_ids(filter="environment:'prod'", sort="name|asc", offset=0, limit=100)
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks
