# test_profile_groups.py
# This class tests the profile_groups service class

import os
import sys

from tests import test_authorization as Authorization

sys.path.append(os.path.abspath('src'))
from falconpy import ProfileGroups

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = ProfileGroups(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 403, 404, 429]


class TestProfileGroups:
    def test_all_code_paths(self):
        error_checks = True
        tests = {
            "GroupActionsV1Mixin0": falcon.group_actions_v1_mixin0(action_name="string", action_parameters="string",
                                                                   filter="string", ids="string"),
            "GroupUsersActionsV1Mixin0": falcon.group_users_actions_v1_mixin0(action_name="string",
                                                                              action_parameters="string", filter="string",
                                                                              ids="string"),
            "GetGroupUsersV1": falcon.get_group_users_v1(ids="string"),
            "GetGroupsV1Mixin0": falcon.get_groups_v1_mixin0(ids="string"),
            "CreateGroupV1Mixin0": falcon.create_group_v1_mixin0(cid="string", description="string", name="string"),
            "DeleteGroupsV1": falcon.delete_groups_v1(ids="12345678"),
            "UpdateGroupV1Mixin0": falcon.update_group_v1_mixin0(id="string", description="string", name="string"),
            "GetUserGroupsV1": falcon.get_user_groups_v1(ids="string"),
            "QueryGroupsV1Mixin0": falcon.query_groups_v1_mixin0(filter="string", sort="string", offset=1, limit=1),
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
        assert error_checks
