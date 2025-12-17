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
            "combined_cloud_risks": falcon.combined_cloud_risks(),
            "ListCloudGroupsExternal": falcon.list_cloud_groups(),
            "ListCloudGroupsByIDExternal": falcon.list_cloud_groups_by_id(),
            "CreateCloudGroupExternal": falcon.create_cloud_group(body={}),
            "UpdateCloudGroupExternal": falcon.update_cloud_group(group={}),
            "DeleteCloudGroupsExternal": falcon.delete_cloud_groups(ids="1234567"),
            "ListCloudGroupIDsExternal": falcon.list_group_ids()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(key)
                # print(tests[key])
        assert error_checks