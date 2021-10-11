"""test_host_groups.py
This class tests the firewall_policies service class
"""

import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import HostGroup

auth = Authorization.TestAuthorization()
token = auth.getConfigExtended()
falcon = HostGroup(access_token=token)
AllowedResponses = [200, 400, 404, 429]  # Adding rate-limiting as an allowed response for now


class TestHostGroup:

    def svc_hg_query_host_groups(self):
        if falcon.query_host_groups(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def svc_hg_query_group_members(self):
        if falcon.query_group_members(
                parameters={"limit": 1, "id": falcon.query_host_groups(parameters={"limit": 1})["body"]["resources"][0]}
                )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def svc_hg_get_host_groups(self):
        if falcon.get_host_groups(
                ids=falcon.query_host_groups(parameters={"limit": 1})["body"]["resources"][0]
                )["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def svc_hg_query_combined_host_groups(self):
        if falcon.query_combined_host_groups(parameters={"limit": 1})["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def svc_hg_query_combined_group_members(self):
        if falcon.query_combined_group_members(
            parameters={"limit": 1,
                        "id": falcon.query_combined_host_groups(parameters={"limit": 1})["body"]["resources"][0]["id"]
                        })["status_code"] in AllowedResponses:
            return True
        else:
            return False

    def svc_hg_test_all_functionality(self):
        error_checks = True
        tests = {
            "perform_group_action": falcon.perform_group_action(ids="12345678",
                                                                action_name="add-hosts",
                                                                action_parameters=[{
                                                                    "name": "filter",
                                                                    "value": "platform_name:'Windows'"
                                                                }]
                                                                ),
            "create_host_groups": falcon.create_host_groups(body={}, group_type="Dunno"),
            "create_host_groups_also": falcon.create_host_groups(assignment_rule="WhateverBro",
                                                                 description="FalconPy Unit Testing",
                                                                 name="UnitTestWhatevers"
                                                                 ),
            "delete_host_groups": falcon.delete_host_groups(ids="12345678"),
            "update_host_groups_first": falcon.update_host_groups(body={}),
            "update_host_groups": falcon.update_host_groups(assignment_rule="WhateverBro",
                                                            description="FalconPy Unit Testing",
                                                            name="UnitTestWhatevers",
                                                            id="12345678"
                                                            ),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                # print(f"{key} \n {tests[key]}")
                error_checks = False

        return error_checks

    def test_query_host_groups(self):
        assert self.svc_hg_query_host_groups() is True

    @pytest.mark.skipif(falcon.query_host_groups(
        parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached"
        )
    def test_query_group_members(self):
        assert self.svc_hg_query_group_members() is True

    @pytest.mark.skipif(
        falcon.query_host_groups(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached"
        )
    def test_get_host_groups(self):
        assert self.svc_hg_get_host_groups() is True

    def test_query_combined_host_groups(self):
        assert self.svc_hg_query_combined_host_groups() is True

    @pytest.mark.skipif(
        falcon.query_combined_host_groups(parameters={"limit": 1})["status_code"] == 429, reason="API rate limit reached"
        )
    def test_query_combined_group_members(self):
        assert self.svc_hg_query_combined_group_members() is True

    def test_post_functionality(self):
        assert self.svc_hg_test_all_functionality() is True

    def test_invalid_action_error(self):
        assert bool(
            int(
                falcon.perform_group_action(body={}, action_name="boogie")["status_code"]
            ) == 500
        )
