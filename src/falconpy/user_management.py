"""CrowdStrike Falcon User Management API interface class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

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
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import generic_payload_list
from ._service_class import ServiceClass
from ._endpoint._user_management import _user_management_endpoints as Endpoints


class UserManagement(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (OAuth2.token())
    """

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_roles(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get info about a role.

        Keyword arguments:
        ids -- List of role IDs to retrieve. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GetRoles
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetRoles",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def grant_user_role_ids(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """Assign one or more roles to a user.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "roleIds": [
                        "string"
                    ]
                }
        parameters -- full parameters payload, not required if other keywords are used.
        role_ids -- Role IDs you want to assign to the user id. (Can also use roleIds)
        user_uuid -- User ID to grant roles access to.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GrantUserRoleIds
        """
        if not body:
            if kwargs.get("role_ids", None):
                kwargs["roleIds"] = kwargs.get("role_ids", None)

            body = generic_payload_list(submitted_keywords=kwargs,
                                        payload_value="roleIds"
                                        )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GrantUserRoleIds",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def revoke_user_role_ids(self: object, parameters: dict = None, **kwargs) -> dict:
        """Revoke one or more roles from a user.

        Keyword arguments:
        ids -- List of role IDs. String or list of strings.
        parameters -- full parameters payload, not required if other keywords are used.
        user_uuid -- User ID to revoke roles for.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RevokeUserRoleIds
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RevokeUserRoleIds",
            keywords=kwargs,
            params=parameters
            )

    def get_available_role_ids(self: object) -> dict:
        """Show role IDs for all roles available in your customer account.

        For more information on each role, provide the role ID to get_roles.

        This method does not accept arguments or keywords.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GetAvailableRoleIds
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAvailableRoleIds"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_user_role_ids(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Show role IDs of roles assigned to a user.

        For more information on each role, provide the role ID to get_role.

        Keyword arguments:
        user_uuid -- User ID to retrieve roles for. String.
        parameters -- full parameters payload, not required if user_uuid is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be
                   'user_uuid'. All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/GetUserRoleIds
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetUserRoleIds",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "user_uuid")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def retrieve_user(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get info about a user.

        Keyword arguments:
        ids -- List of User IDs to retrieve. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveUser
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RetrieveUser",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_user(self: object, body: dict = None, **kwargs) -> dict:
        """Create a new user.

        After creating a user, assign one or more roles with grant_user_role_ids.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "firstName": "string",
                    "lastName": "string",
                    "password": "string",
                    "uid": "string"
                }
        first_name -- First name of the user. String. (can also use firstName)
        last_name -- Last name of the user. String. (can also use lastName)
        password -- Password. String.
                    As a best practice, we recommend ommitting password. If single sign-on is
                    enabled for your customer account, the password attribute is ignored. If
                    single sign-on is not enabled, we send a user activation request to their
                    email address when you create the user with no password. The user should use
                    the activation email to set their own password.
        uid -- The user's email address, which will be the assigned username. String. Required.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/CreateUser
        """
        if not body:
            body = {}
            body["uid"] = kwargs.get("uid", None)
            body["firstName"] = kwargs.get("firstName", None)
            body["firstName"] = kwargs.get("first_name", None)
            body["lastName"] = kwargs.get("lastName", None)
            body["lastName"] = kwargs.get("last_name", None)
            body["password"] = kwargs.get("password", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateUser",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_user(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Delete a user permanently.

        Keyword arguments:
        parameters -- full parameters payload, not required if user_uuid is provided as a keyword.
        user_uuid -- User ID to delete.

        Arguments: When not specified, the first argument to this method is assumed to be
                   'user_uuid'. All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/DeleteUser
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteUser",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "user_uuid")
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def update_user(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """Modify an existing user.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "firstName": "string",
                    "lastName": "string"
                }
        first_name -- First name to apply to the user. String. (Can also use firstName)
        last_name -- Last name to apply to the user. String. (Can also use lastName)
        parameters -- full parameters payload, not required if using other keywords.
        user_uuid -- User ID to modify.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/UpdateUser
        """
        if not body:
            body = {}
            body["firstName"] = kwargs.get("firstName", None)
            body["firstName"] = kwargs.get("first_name", None)
            body["lastName"] = kwargs.get("lastName", None)
            body["lastName"] = kwargs.get("last_name", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateUser",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    def retrieve_emails_by_cid(self: object) -> dict:
        """List the usernames (usually an email address) for all users in your customer account.

        This method does not accept arguments or keywords.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveEmailsByCID
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RetrieveEmailsByCID"
            )

    def retrieve_user_uuids_by_cid(self: object) -> dict:
        """List user IDs for all users in your customer account.

        For more information on each user, provide the user ID to retrieve_user.

        This method does not accept arguments or keywords.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveUserUUIDsByCID
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RetrieveUserUUIDsByCID"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def retrieve_user_uuid(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get a user's ID by providing a username (usually an email address).

        Keyword arguments:
        uid -- List of User IDs to retrieve. String or list of strings.
        parameters -- full parameters payload, not required if uid is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be
                   'uid'. All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/RetrieveUserUUID
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RetrieveUserUUID",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "uid")
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetRoles = get_roles
    GrantUserRoleIds = grant_user_role_ids
    RevokeUserRoleIds = revoke_user_role_ids
    GetAvailableRoleIds = get_available_role_ids
    GetUserRoleIds = get_user_role_ids
    RetrieveUser = retrieve_user
    CreateUser = create_user
    DeleteUser = delete_user
    UpdateUser = update_user
    RetrieveEmailsByCID = retrieve_emails_by_cid
    RetrieveUserUUIDsByCID = retrieve_user_uuids_by_cid
    RetrieveUserUUID = retrieve_user_uuid


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
User_Management = UserManagement  # pylint: disable=C0103
