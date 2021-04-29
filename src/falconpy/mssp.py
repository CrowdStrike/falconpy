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
import sys
from ._util import service_request, force_default, args_to_params
from ._service_class import ServiceClass
from ._endpoint._mssp import _mssp_endpoints as ENDPOINTS


class Flight_Control(ServiceClass):  # pylint: disable=C0103,R0904  # Matching API
    """The only requirement to instantiate an instance of this class
       is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def getChildren(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103  # Matching API
        """Get link to child customer by child CID(s)"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getChildren
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def getCIDGroupMembersBy(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103
        """Get CID Group members by CID Group IDs."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getCIDGroupMembersBy
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def addCIDGroupMembers(self: object, body: dict) -> dict:  # pylint: disable=C0103  #Matching API
        """Add new CID Group member."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/addCIDGroupMembers
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def deleteCIDGroupMembers(self: object, body: dict) -> dict:  # pylint: disable=C0103  #Matching API
        """ Delete a set of Prevention Policies by specifying their IDs. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteCIDGroupMembers
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def getCIDGroupById(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103  #Matching API
        """Get CID Group(s) by ID(s)."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getCIDGroupById
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def createCIDGroups(self: object, body: dict) -> dict:  # pylint: disable=C0103  #Matching API
        """Create new CID Group(s). Maximum 500 CID Group(s) allowed."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/createCIDGroups
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def deleteCIDGroups(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103  #Matching API
        """Delete CID Group(s) by ID(s)."""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteCIDGroups
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def updateCIDGroups(self: object, body: dict) -> dict:  # pylint: disable=C0103  #Matching API
        """Update existing CID Group(s). CID Group ID is expected for each CID
           Group definition provided in request body. CID Group member(s) remain unaffected.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/updateCIDGroups
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def getRolesByID(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103  #Matching API
        """Get MSSP Role assignment(s). MSSP Role assignment is of the format <user_group_id>:<cid_group_id>."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getRolesByID
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def addRole(self: object, body: dict) -> dict:  # pylint: disable=C0103  #Matching API
        """Assign new MSSP Role(s) between User Group and CID Group.
           It does not revoke existing role(s) between User Group and CID Group.
           User Group ID and CID Group ID have to be specified in request.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/addRole
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def deleteRoles(self: object, *args, **kwargs) -> dict:  # pylint: disable=C0103  #Matching API
        """Delete MSSP Role assignment(s) between User Group and CID Group.
           User Group ID and CID Group ID have to be specified in request.
           Only specified roles are removed if specified in request payload,
           else association between User Group and CID Group is dissolved completely (if no roles specified).

           Redirects to deletedRoles()
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deletedRoles
        returned = self.deletedRoles(*args, **kwargs)

        return returned

    def deletedRoles(self: object, body: dict) -> dict:  # pylint: disable=C0103  #Matching API
        """Delete MSSP Role assignment(s) between User Group and CID Group.
           User Group ID and CID Group ID have to be specified in request.
           Only specified roles are removed if specified in request payload,
           else association between User Group and CID Group is dissolved completely (if no roles specified).
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deletedRoles
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def getUserGroupMembersByID(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103
        """Get User Group members by User Group ID(s)."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getUserGroupMembersByID
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def addUserGroupMembers(self: object, body: dict) -> dict:  # pylint: disable=C0103  #Matching API
        """Add new User Group member. Maximum 500 members allowed per User Group."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/addUserGroupMembers
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def deleteUserGroupMembers(self: object, body: dict) -> dict:  # pylint: disable=C0103  #Matching API
        """Delete User Group members entry."""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteUserGroupMembers
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def getUserGroupsByID(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103  #Matching API
        """Get User Groups by ID(s)."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getUserGroupsByID
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def createUserGroup(self: object, body: dict) -> dict:  # pylint: disable=C0103  #Matching API
        """Create new User Group(s). Maximum 500 User Group(s) allowed per customer."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/createUserGroup
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def deleteUserGroups(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103  #Matching API
        """Delete User Group(s) by ID(s)."""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteUserGroups
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def updateUserGroups(self: object, body: dict) -> dict:  # pylint: disable=C0103  #Matching API
        """Update existing User Group(s). User Group ID is expected for each User Group
           definition provided in request body. User Group member(s) remain unaffected.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/updateUserGroups
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryChildren(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103  #Matching API
        """Query for customers linked as children"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryChildren
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryCIDGroupMembers(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103  #Matching API
        """Query a CID Groups members by associated CID."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryCIDGroupMembers
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryCIDGroups(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103  #Matching API
        """Query a CID Groups."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryCIDGroups
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryRoles(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103  #Matching API
        """Query MSSP Role assignment. At least one of CID Group ID or
           User Group ID should also be provided. Role ID is optional.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryRoles
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryUserGroupMembers(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103  #Matching API
        """Query User Group member by User UUID."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryRoles
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryUserGroups(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103  #Matching API
        """Query User Groups."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryUserGroups
        fname = sys._getframe().f_code.co_name  # pylint: disable=W0212  # Name lookup only
        target_url = f"{self.base_url}{[ep[2] for ep in ENDPOINTS if fname in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, ENDPOINTS, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned
