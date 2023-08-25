# test_mssp.py
# This class tests the mssp service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import FlightControl  # noqa: E402  pylint: disable=E0401

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = FlightControl(auth_object=config)
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


class TestFlightControl:
    def serviceFlight_GenerateErrors(self):
        falcon.base_url = "nowhere"
        error_checks = True
        tests = {
            "getChildren": falcon.get_children(ids='12345678'),
            "getChildrenV2": falcon.get_children_v2(ids='12345678'),
            "getCIDGroupMembersByV1": falcon.get_cid_group_members_by_v1(cid_group_ids='12345678'),
            "getCIDGroupMembersByV2": falcon.get_cid_group_members_by(cid_group_ids='12345678'),
            "addCIDGroupMembers": falcon.add_cid_group_members(cid_group_id="12345678"),
            "deleteCIDGroupMembersV1": falcon.delete_cid_group_members_v1(cid_group_id="12345678"),
            "deleteCIDGroupMembersV2": falcon.delete_cid_group_members(cid_group_id="12345678"),
            "getCIDGroupByIdV1": falcon.get_cid_group_by_id_v1(cid_group_ids='12345678'),
            "getCIDGroupByIdV2": falcon.get_cid_group_by_id(cid_group_ids='12345678'),
            "createCIDGroups": falcon.create_cid_groups(body={}),
            "deleteCIDGroups": falcon.delete_cid_groups(cid_group_ids='12345678'),
            "updateCIDGroups": falcon.update_cid_groups(body={}),
            "getRolesByID": falcon.get_roles_by_id(ids='12345678'),
            "addRole": falcon.add_role(body={}),
            "deleteRoles": falcon.delete_roles(body={}),
            "getUserGroupMembersByIDV1": falcon.get_user_group_members_by_id_v1(user_group_ids='12345678'),
            "getUserGroupMembersByIDV2": falcon.get_user_group_members_by_id(user_group_ids='12345678'),
            "getUserGroupsByIDV1": falcon.get_user_groups_by_id_v1(user_group_ids='12345678'),
            "getUserGroupsByIDV2": falcon.get_user_groups_by_id(user_group_ids='12345678'),
            "addUserGroupMembers": falcon.add_user_group_members(body={}),
            "deleteUserGroupMembers": falcon.delete_user_group_members(body={}),
            "createUserGroups": falcon.create_user_groups(body={}),
            "updateUserGroups": falcon.update_user_groups(user_group_id="12345678",
                                                          name="UnitTesting",
                                                          role_ids="12345,67890"),
            "deleteUserGroups": falcon.delete_user_groups(user_group_ids='12345678'),
            "queryChildren": falcon.query_children(),
            "queryCIDGroupMembers": falcon.query_cid_group_members(),
            "queryCIDGroups": falcon.query_cid_groups(),
            "queryRoles": falcon.query_roles(),
            "queryUserGroupMembers": falcon.query_user_group_members(),
            "queryUserGroups": falcon.query_user_groups()

        }
        for key in tests:
            if tests[key]["status_code"] != 500:
                error_checks = False

        return error_checks

    def test_Errors(self):
        assert self.serviceFlight_GenerateErrors() is True
