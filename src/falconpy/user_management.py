"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

user_management - CrowdStrike Falcon User Management API interface class

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
# pylint: disable=C0103  # Aligning method names to API operation IDs
from ._util import force_default, process_service_request
from ._service_class import ServiceClass
from ._endpoint._user_management import _user_management_endpoints as Endpoints


class User_Management(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetRoles(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get info about a role.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GetRoles
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetRoles",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GrantUserRoleIds(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Assign one or more roles to a user.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GrantUserRoleIds
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GrantUserRoleIds",
            method="POST",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def RevokeUserRoleIds(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Revoke one or more roles from a user.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RevokeUserRoleIds
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RevokeUserRoleIds",
            method="DELETE",
            keywords=kwargs,
            params=parameters
            )

    def GetAvailableRoleIds(self: object) -> dict:
        """
        Show role IDs for all roles available in your customer account.
        For more information on each role, provide the role ID to `/customer/entities/roles/v1`.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GetAvailableRoleIds
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAvailableRoleIds"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetUserRoleIds(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Show role IDs of roles assigned to a user. For more information on each role,
        provide the role ID to `/customer/entities/roles/v1`.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GetUserRoleIds
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetUserRoleIds",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def RetrieveUser(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get info about a user.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveUser
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RetrieveUser",
            keywords=kwargs,
            params=parameters
            )

    def CreateUser(self: object, body: dict) -> dict:
        """
        Create a new user. After creating a user,
        assign one or more roles with POST /user-roles/entities/user-roles/v1.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/CreateUser
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateUser",
            method="POST",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def DeleteUser(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a user permanently.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/DeleteUser
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteUser",
            method="DELETE",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def UpdateUser(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Modify an existing user.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/UpdateUser
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateUser",
            method="PATCH",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    def RetrieveEmailsByCID(self: object) -> dict:
        """
        List the usernames (usually an email address) for all users in your customer account.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveEmailsByCID
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RetrieveEmailsByCID"
            )

    def RetrieveUserUUIDsByCID(self: object) -> dict:
        """
        List user IDs for all users in your customer account.
        For more information on each user, provide the user ID to `/users/entities/user/v1`.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveUserUUIDsByCID
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RetrieveUserUUIDsByCID"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def RetrieveUserUUID(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get a user's ID by providing a username (usually an email address).
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveUserUUID
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RetrieveUserUUID",
            keywords=kwargs,
            params=parameters
            )
