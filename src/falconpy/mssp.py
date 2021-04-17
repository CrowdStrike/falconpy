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
from ._util import service_request, parse_id_list
from ._service_class import ServiceClass


class Flight_Control(ServiceClass):
    """The only requirement to instantiate an instance of this class
       is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def getChildren(self: object, ids) -> dict:
        """Get link to child customer by child CID(s)"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getChildren
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'​/mssp​/entities​/children​/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def getCIDGroupMembersBy(self: object, cid_group_ids) -> dict:
        """Get CID Group members by CID Group IDs."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getCIDGroupMembersBy
        ID_LIST = str(parse_id_list(cid_group_ids)).replace(",", "&cid_group_ids=")
        FULL_URL = self.base_url+'​/mssp/entities/cid-group-members/v1?cid_group_ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def addCIDGroupMembers(self: object, body: dict) -> dict:
        """Add new CID Group member."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/addCIDGroupMembers
        FULL_URL = self.base_url+'/mssp/entities/cid-group-members/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def deleteCIDGroupMembers(self: object, body: dict) -> dict:
        """ Delete a set of Prevention Policies by specifying their IDs. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteCIDGroupMembers
        FULL_URL = self.base_url+'/mssp/entities/cid-group-members/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def getCIDGroupById(self: object, cid_group_ids) -> dict:
        """Get CID Group(s) by ID(s)."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getCIDGroupById
        ID_LIST = str(parse_id_list(cid_group_ids)).replace(",", "&cid_group_ids=")
        FULL_URL = self.base_url+'​/mssp/entities/cid-groups/v1?cid_group_ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def createCIDGroups(self: object, body: dict) -> dict:
        """Create new CID Group(s). Maximum 500 CID Group(s) allowed."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/createCIDGroups
        FULL_URL = self.base_url+'/mssp/entities/cid-groups/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def deleteCIDGroups(self: object, cid_group_ids) -> dict:
        """Delete CID Group(s) by ID(s)."""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteCIDGroups
        ID_LIST = str(parse_id_list(cid_group_ids)).replace(",", "&cid_group_ids=")
        FULL_URL = self.base_url+'/mssp/entities/cid-groups/v1?cid_group_ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def updateCIDGroups(self: object, body: dict) -> dict:
        """Update existing CID Group(s). CID Group ID is expected for each CID
           Group definition provided in request body. CID Group member(s) remain unaffected.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/updateCIDGroups
        FULL_URL = self.base_url+'/mssp/entities/cid-groups/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def getRolesByID(self: object, ids) -> dict:
        """Get MSSP Role assignment(s). MSSP Role assignment is of the format <user_group_id>:<cid_group_id>."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getRolesByID
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'​/mssp/entities/mssp-roles/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def addRole(self: object, body: dict) -> dict:
        """Assign new MSSP Role(s) between User Group and CID Group.
           It does not revoke existing role(s) between User Group and CID Group.
           User Group ID and CID Group ID have to be specified in request.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/addRole
        FULL_URL = self.base_url+'/mssp/entities/mssp-roles/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def deleteRoles(self: object, body: dict) -> dict:
        """Delete MSSP Role assignment(s) between User Group and CID Group.
           User Group ID and CID Group ID have to be specified in request.
           Only specified roles are removed if specified in request payload,
           else association between User Group and CID Group is dissolved completely (if no roles specified).
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteRoles
        FULL_URL = self.base_url+'/mssp/entities/mssp-roles/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def getUserGroupMembersByID(self: object, user_group_ids) -> dict:
        """Get User Group members by User Group ID(s)."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getUserGroupMembersByID
        ID_LIST = str(parse_id_list(user_group_ids)).replace(",", "&user_group_ids=")
        FULL_URL = self.base_url+'​/mssp/entities/user-group-members/v1?user_group_ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def addUserGroupMembers(self: object, body: dict) -> dict:
        """Add new User Group member. Maximum 500 members allowed per User Group."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/addUserGroupMembers
        FULL_URL = self.base_url+'/mssp/entities/user-group-members/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def deleteUserGroupMembers(self: object, body: dict) -> dict:
        """Delete User Group members entry."""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteUserGroupMembers
        FULL_URL = self.base_url+'/mssp/entities/user-group-members/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def getUserGroupsByID(self: object, user_group_ids) -> dict:
        """Get User Groups by ID(s)."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getUserGroupsByID
        ID_LIST = str(parse_id_list(user_group_ids)).replace(",", "&user_group_ids=")
        FULL_URL = self.base_url+'/mssp/entities/user-groups/v1?user_group_ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def createUserGroup(self: object, body: dict) -> dict:
        """Create new User Group(s). Maximum 500 User Group(s) allowed per customer."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/createUserGroup
        FULL_URL = self.base_url+'/mssp/entities/user-groups/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def deleteUserGroups(self: object, user_group_ids) -> dict:
        """Delete User Group(s) by ID(s)."""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteUserGroups
        ID_LIST = str(parse_id_list(user_group_ids)).replace(",", "&user_group_ids=")
        FULL_URL = self.base_url+'/mssp/entities/user-groups/v1?user_group_ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def updateUserGroups(self: object, body: dict) -> dict:
        """Update existing User Group(s). User Group ID is expected for each User Group
           definition provided in request body. User Group member(s) remain unaffected.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/updateUserGroups
        FULL_URL = self.base_url+'/mssp/entities/user-groups/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def queryChildren(self: object, parameters: dict = None) -> dict:
        """Query for customers linked as children"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryChildren
        FULL_URL = self.base_url+'/mssp/queries/children/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def queryCIDGroupMembers(self: object, parameters: dict = None) -> dict:
        """Query a CID Groups members by associated CID."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryCIDGroupMembers
        FULL_URL = self.base_url+'/mssp/queries/cid-group-members/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def queryCIDGroups(self: object, parameters: dict = None) -> dict:
        """Query a CID Groups."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryCIDGroups
        FULL_URL = self.base_url+'/mssp/queries/cid-groups/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def queryRoles(self: object, parameters: dict = None) -> dict:
        """Query MSSP Role assignment. At least one of CID Group ID or
           User Group ID should also be provided. Role ID is optional.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryRoles
        FULL_URL = self.base_url+'​/mssp​/queries​/mssp-roles​/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def queryUserGroupMembers(self: object, parameters: dict = None) -> dict:
        """Query User Group member by User UUID."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryRoles
        FULL_URL = self.base_url+'​/mssp/queries/user-group-members/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def queryUserGroups(self: object, parameters: dict = None) -> dict:
        """Query User Groups."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryUserGroups
        FULL_URL = self.base_url+'​​/mssp​/queries​/user-groups​/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned
