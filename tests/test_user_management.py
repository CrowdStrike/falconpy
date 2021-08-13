"""
test_user_management.py - This class tests the user_management service class
"""
import os
import sys
import pytest
# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Classes to test - manually imported from sibling folder
from falconpy import user_management as FalconUsers
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))

auth = Authorization.TestAuthorization()
auth.getConfig()
falcon = FalconUsers.User_Management(creds={"client_id": auth.config["falcon_client_id"],
                                            "client_secret": auth.config["falcon_client_secret"]
                                            })
AllowedResponses = [200, 429]  # Adding rate-limiting as an allowed response for now


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
        falcon.base_url = "nowhere"
        error_checks = True
        tests = {
            "get_roles": falcon.GetRoles(ids='12345678')["status_code"],
            "grant_user_role_ids": falcon.GrantUserRoleIds(body={}, parameters={})["status_code"],
            "revoke_user_role_ids": falcon.RevokeUserRoleIds(ids='12345678', parameters={})["status_code"],
            "get_available_role_ids": falcon.GetAvailableRoleIds()["status_code"],
            "get_user_role_ids": falcon.GetUserRoleIds(parameters={})["status_code"],
            "retrieve_user": falcon.RetrieveUser(ids='12345678')["status_code"],
            "create_user": falcon.CreateUser(body={})["status_code"],
            "delete_user": falcon.DeleteUser(parameters={})["status_code"],
            "update_user": falcon.UpdateUser(body={}, parameters={})["status_code"],
            "retrieve_emails_by_cid": falcon.RetrieveEmailsByCID()["status_code"],
            "retrieve_user_uuids_by_cid": falcon.RetrieveUserUUIDsByCID()["status_code"],
            "retrieve_user_uuid": falcon.RetrieveUserUUID(parameters={})["status_code"]
        }
        for key in tests:
            if tests[key] != 500:
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

    @staticmethod
    def test_logout():
        """
        Pytest harness hook
        """
        assert bool(falcon.auth_object.revoke(
            falcon.auth_object.token()["body"]["access_token"]
            )["status_code"] in AllowedResponses) is True
