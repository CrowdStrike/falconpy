"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

mssp (Flight Control) - CrowdStrike Falcon Event Stream API interface class

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
# pylint: disable=R0904  # Matching API operation counts
from ._util import force_default, handle_single_argument, process_service_request
from ._service_class import ServiceClass
from ._endpoint._mssp import _mssp_endpoints as Endpoints


class FlightControl(ServiceClass):
    """The only requirement to instantiate an instance of this class
       is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_children(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get link to child customer by child CID(s)
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getChildren
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getChildren",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_cid_group_members_by(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get CID Group members by CID Group IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getCIDGroupMembersBy
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getCIDGroupMembersBy",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "cid_group_ids")
            )

    def add_cid_group_members(self: object, body: dict) -> dict:
        """
        Add new CID Group member.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/addCIDGroupMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="addCIDGroupMembers",
            body=body
            )

    def delete_cid_group_members(self: object, body: dict) -> dict:
        """
        Delete CID Group members entry.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteCIDGroupMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteCIDGroupMembers",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_cid_group_by_id(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get CID Group(s) by ID(s).
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getCIDGroupById
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getCIDGroupById",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "cid_group_ids")
            )

    def create_cid_groups(self: object, body: dict) -> dict:
        """
        Create new CID Group(s). Maximum 500 CID Group(s) allowed.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/createCIDGroups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createCIDGroups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_cid_groups(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Delete CID Group(s) by ID(s).
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteCIDGroups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteCIDGroups",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "cid_group_ids")
            )

    def update_cid_groups(self: object, body: dict) -> dict:
        """
        Update existing CID Group(s). CID Group ID is expected for each CID
        Group definition provided in request body. CID Group member(s) remain unaffected.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/updateCIDGroups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateCIDGroups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_roles_by_id(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get MSSP Role assignment(s). MSSP Role assignment is of the format <user_group_id>:<cid_group_id>.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getRolesByID
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getRolesByID",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def add_role(self: object, body: dict) -> dict:
        """
        Assign new MSSP Role(s) between User Group and CID Group.
        It does not revoke existing role(s) between User Group and CID Group.
        User Group ID and CID Group ID have to be specified in request.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/addRole
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="addRole",
            body=body
            )

    def delete_roles(self: object, body: dict) -> dict:
        """
        Delete MSSP Role assignment(s) between User Group and CID Group.
        User Group ID and CID Group ID have to be specified in request.
        Only specified roles are removed if specified in request payload,
        else association between User Group and CID Group is dissolved completely (if no roles specified).
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deletedRoles
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deletedRoles",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_user_group_members_by_id(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get User Group members by User Group ID(s).
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getUserGroupMembersByID
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getUserGroupMembersByID",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "user_group_ids")
            )

    def add_user_group_members(self: object, body: dict) -> dict:
        """
        Add new User Group member. Maximum 500 members allowed per User Group.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/addUserGroupMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="addUserGroupMembers",
            body=body
            )

    def delete_user_group_members(self: object, body: dict) -> dict:
        """
        Delete User Group members entry.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteUserGroupMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteUserGroupMembers",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_user_groups_by_id(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get User Groups by ID(s).
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getUserGroupsByID
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getUserGroupsByID",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "user_group_ids")
            )

    def create_user_groups(self: object, body: dict) -> dict:
        """
        Create new User Group(s). Maximum 500 User Group(s) allowed per customer.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/createUserGroup
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createUserGroups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_user_groups(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Delete User Group(s) by ID(s).
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteUserGroups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteUserGroups",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "user_group_ids")
            )

    def update_user_groups(self: object, body: dict) -> dict:
        """
        Update existing User Group(s). User Group ID is expected for each User Group
        definition provided in request body. User Group member(s) remain unaffected.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/updateUserGroups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateUserGroups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_children(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Query for customers linked as children
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryChildren
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryChildren",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_cid_group_members(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Query a CID Groups members by associated CID.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryCIDGroupMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCIDGroupMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_cid_groups(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Query a CID Groups.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryCIDGroups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCIDGroups",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_roles(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Query MSSP Role assignment. At least one of CID Group ID or
        User Group ID should also be provided. Role ID is optional.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryRoles
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryRoles",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_user_group_members(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Query User Group member by User UUID.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryRoles
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryUserGroupMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_user_groups(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Query User Groups.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryUserGroups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryUserGroups",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    getChildren = get_children
    getCIDGroupMembersBy = get_cid_group_members_by
    addCIDGroupMembers = add_cid_group_members
    deleteCIDGroupMembers = delete_cid_group_members
    getCIDGroupById = get_cid_group_by_id
    createCIDGroups = create_cid_groups
    deleteCIDGroups = delete_cid_groups
    updateCIDGroups = update_cid_groups
    getRolesByID = get_roles_by_id
    addRole = add_role
    deletedRoles = delete_roles
    deleteRoles = delete_roles  # Typo fix
    getUserGroupMembersByID = get_user_group_members_by_id
    addUserGroupMembers = add_user_group_members
    deleteUserGroupMembers = delete_user_group_members
    getUserGroupsByID = get_user_groups_by_id
    createUserGroup = create_user_groups    # Typo fix
    createUserGroups = create_user_groups
    deleteUserGroups = delete_user_groups
    updateUserGroups = update_user_groups
    queryChildren = query_children
    queryCIDGroupMembers = query_cid_group_members
    queryCIDGroups = query_cid_groups
    queryRoles = query_roles
    queryUserGroupMembers = query_user_group_members
    queryUserGroups = query_user_groups


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Flight_Control = FlightControl  # pylint: disable=C0103
