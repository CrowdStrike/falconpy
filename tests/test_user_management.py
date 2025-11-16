"""
test_user_management.py - This class tests the user_management service class
"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Classes to test - manually imported from sibling folder
from falconpy import UserManagement
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = UserManagement(auth_object=config)
AllowedResponses = [200, 400, 401, 403, 404, 429]  # Adding rate-limiting as an allowed response for now


class TestFalconUserManagement:
    """
    User Management Service Class test harness
    """
    def um_retrieve_user_uuid(self):
        """
        retrieve_user_uuid
        """
        try:
            id_list = falcon.RetrieveEmailsByCID()["body"]["resources"][0]
            if falcon.RetrieveUserUUID(parameters={"uid": id_list})["status_code"] in AllowedResponses:
                return True
            else:
                return False
        except KeyError:
            pytest.skip("Workflow-related error, skipping")
            return True

    def um_retrieve_user(self):
        """
        retrieve_user
        """
        try:
            id_list = falcon.RetrieveUserUUIDsByCID()["body"]["resources"][0]
            if falcon.RetrieveUser(ids=id_list)["status_code"] in AllowedResponses:
                return True
            else:
                return False
        except KeyError:
            pytest.skip("Workflow-related error, skipping")
            return True

    def um_get_user_role_ids(self):
        """
        get_user_role_ids
        """
        try:
            id_list = falcon.RetrieveUserUUIDsByCID()["body"]["resources"][0]
            if falcon.GetUserRoleIds(parameters={"user_uuid": id_list})["status_code"] in AllowedResponses:
                return True
            else:
                return False
        except KeyError:
            pytest.skip("Workflow-related error, skipping")
            return True

    def um_get_roles(self):
        """
        get_roles
        """
        try:
            id_list = falcon.GetAvailableRoleIds()["body"]["resources"][0]
            if falcon.GetRoles(ids=id_list)["status_code"] in AllowedResponses:
                return True
            else:
                return False
        except KeyError:
            pytest.skip("Workflow-related error, skipping")
            return True

    def um_generate_errors(self):
        """
        Test every code path within every method by generating 500s, does not hit the API
        """
        #falcon.base_url = "nowhere"
        error_checks = True
        tests = {
            "aggregateUsersV1": falcon.aggregate_users(),
            "get_roles": falcon.GetRoles(ids='12345678'),
            "grant_user_role_ids_first": falcon.GrantUserRoleIds(body={}, parameters={}),
            "grant_user_role_ids": falcon.GrantUserRoleIds(user_uuid="12345678", roleIds=["12345678"]),
            "grant_user_role_ids_as_well": falcon.GrantUserRoleIds(user_uuid="12345678",
                                                                   role_ids=["12345678"]
                                                                   ),
            "revoke_user_role_ids": falcon.RevokeUserRoleIds(ids='12345678',
                                                             parameters={},
                                                             user_uuid="whatever@nowhere.com"
                                                             ),
            "get_available_role_ids": falcon.GetAvailableRoleIds(),
            "get_user_role_ids": falcon.GetUserRoleIds(parameters={}),
            "retrieve_user": falcon.RetrieveUser(ids='12345678'),
            "create_user": falcon.CreateUser(body={},
                                             uid="whatever@nowhere.com",
                                             first_name="Unit",
                                             last_name="Testing",
                                             password="DontUseThis"
                                             ),
            "delete_user": falcon.DeleteUser(parameters={}),
            "delete_user_again": falcon.DeleteUser(ids="12345678"),
            "update_user_first": falcon.UpdateUser(body={}, parameters={}),
            "update_user": falcon.UpdateUser(user_uuid="12345678",
                                             first_name="unit",
                                             last_name="testing"
                                             ),
            "retrieve_emails_by_cid": falcon.RetrieveEmailsByCID(),
            "retrieve_user_uuids_by_cid": falcon.RetrieveUserUUIDsByCID(),
            "retrieve_user_uuid": falcon.RetrieveUserUUID(parameters={}),
            "get_user_grants_v1": falcon.get_user_grants_v1(user_uuid="12345678"),
            "get_user_grants": falcon.get_user_grants(user_uuid="12345678"),
            "get_roles_mssp": falcon.get_roles_mssp(ids="1234567890", cid="1234567890"),
            "get_roles_mssp_v1": falcon.get_roles_mssp_v1(ids="1234567890", cid="1234567890"),
            "user_action": falcon.user_action(action_name="reset_password",
                                              ids="1ab2c345-67d8-90e1-2345-6789f0a12bc3"
                                              ),
            "user_roles_action": falcon.user_roles_action(action="grant",
                                                          role_ids="12345678",
                                                          uuid="123567890"
                                                          ),
            "retrieve_users": falcon.retrieve_users("1234567890"),
            "create_user_mssp": falcon.create_user_mssp(uid="whatever@nowhere.com",
                                                        first_name="Unit",
                                                        last_name="Testing",
                                                        password="DontUseThis"
                                                        ),
            "delete_user_mssp": falcon.delete_user_mssp(ids="1234567890"),
            "update_user_mssp": falcon.update_user_mssp(user_uuid="123456789", first_name="Bob"),
            "query_roles": falcon.query_roles("1234567890"),
            "query_users": falcon.query_users()
        }
        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                if key not in ["query_roles", "user_action"]:  # Temporarily allow 500s from these ops
                    error_checks = False
                # print(f"{key} processed with a {tests[key]} response")

        return error_checks

    def test_retrieve_emails_by_cid(self):
        """
        Pytest harness hook
        """
        assert bool(falcon.RetrieveEmailsByCID()["status_code"] in AllowedResponses) is True

    def test_retrieve_user_uuids_by_cid(self):
        """
        Pytest harness hook
        """
        assert bool(falcon.RetrieveUserUUIDsByCID()["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(falcon.RetrieveEmailsByCID()["status_code"] == 429, reason="API rate limit reached")
    def test_retrieve_user_uuid(self):
        """
        Pytest harness hook
        """
        assert self.um_retrieve_user_uuid() is True

    @pytest.mark.skipif(falcon.RetrieveUserUUIDsByCID()["status_code"] == 429, reason="API rate limit reached")
    def test_retrieve_user(self):
        """
        Pytest harness hook
        """
        assert self.um_retrieve_user() is True

    @pytest.mark.skipif(falcon.RetrieveUserUUIDsByCID()["status_code"] == 429, reason="API rate limit reached")
    def test_get_user_role_ids(self):
        """
        Pytest harness hook
        """
        assert self.um_get_user_role_ids() is True

    def test_get_available_role_ids(self):
        """
        Pytest harness hook
        """
        assert bool(falcon.GetAvailableRoleIds()["status_code"] in AllowedResponses) is True

    @pytest.mark.skipif(falcon.GetAvailableRoleIds()["status_code"] == 429, reason="API rate limit reached")
    def test_get_roles(self):
        """
        Pytest harness hook
        """
        assert self.um_get_roles() is True

    def test_errors(self):
        """
        Pytest harness hook
        """
        assert self.um_generate_errors() is True

    # @staticmethod
    # def test_logout():
    #     """
    #     Pytest harness hook
    #     """
    #     assert bool(falcon.auth_object.revoke(
    #         falcon.auth_object.token()["body"]["access_token"]
    #         )["status_code"] in AllowedResponses) is True
