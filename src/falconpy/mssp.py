"""CrowdStrike Falcon Flight Control (MSSP) API interface class.

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
# pylint: disable=C0302,R0904  # Matching API operation counts
from typing import Dict, Union
from ._util import force_default, handle_single_argument, process_service_request
from ._payload import generic_payload_list, mssp_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._mssp import _mssp_endpoints as Endpoints


class FlightControl(ServiceClass):
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
    def get_children(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get link to child customer by child CID(s).

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getChildren

        Keyword arguments
        -----------------
        ids : str or list[str]
            CID of a child customer.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getChildren",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_children_v2(self: object, *args, body: dict = None, **kwargs) -> dict:
        """Get link to child customer by child CID(s).

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getChildrenV2

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when ids keyword is provided.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids : str or list[str]
            ID(s) of the indicator entities to retrieve.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = generic_payload_list(submitted_arguments=args,
                                        submitted_keywords=kwargs,
                                        payload_value="ids"
                                        )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getChildrenV2",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_cid_group_members_by_v1(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get CID Group members by CID Group IDs.

        ** DEPRECATED **

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getCIDGroupMembersBy

        Keyword arguments
        -----------------
        cid_group_ids : str or list[str]
            CID group IDs to search for.
        parameters : dict
            full parameters payload, not required if `cid_group_ids` is provided
            as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'cid_group_ids'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getCIDGroupMembersByV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "cid_group_ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_cid_group_members_by(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get CID Group members by CID Group IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getCIDGroupMembersByV2

        Keyword arguments
        -----------------
        ids : str or list[str]
            CID group IDs to search for. String or list of strings.
            The keyword `cid_group_ids` will also be accepted for this argument.
        parameters : dict
            full parameters payload, not required if `cid_group_ids` is provided
            as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("cid_group_ids", None) and not kwargs.get("ids", None):
            kwargs["ids"] = kwargs.get("cid_group_ids")

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getCIDGroupMembersBy",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def add_cid_group_members(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add new CID Group member.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/addCIDGroupMembers

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if sha256 is provided as a keyword.
                {
                    "resources": [
                        {
                            "cid_group_id": "string",
                            "cids": [
                                "string"
                            ]
                        }
                    ]
                }
        cid_group_id : str
            ID of the CID group to update.
        cids : str or list[str]
            CIDs to add to the group.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            item = generic_payload_list(submitted_keywords=kwargs, payload_value="cids")
            if kwargs.get("cid_group_id", None):
                item["cid_group_id"] = kwargs.get("cid_group_id", None)
            body["resources"] = [item]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="addCIDGroupMembers",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def delete_cid_group_members_v1(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete CID Group members entry.

        *DEPRECATED*
        Please use delete_cid_group_members.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteCIDGroupMembers

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if sha256 is provided as a keyword.
                {
                    "resources": [
                        {
                            "cid_group_id": "string",
                            "cids": [
                                "string"
                            ]
                        }
                    ]
                }
        cid_group_id : str
            ID of the CID group to update.
        cids : str or list[str]
            CIDs to remove from the group.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            item = generic_payload_list(submitted_keywords=kwargs, payload_value="cids")
            if kwargs.get("cid_group_id", None):
                item["cid_group_id"] = kwargs.get("cid_group_id", None)
            body["resources"] = [item]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteCIDGroupMembers",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def delete_cid_group_members(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete CID Group members entry.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteCIDGroupMembers

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if sha256 is provided as a keyword.
                {
                    "resources": [
                        {
                            "cid_group_id": "string",
                            "cids": [
                                "string"
                            ]
                        }
                    ]
                }
        cid_group_id : str
            ID of the CID group to update.
        cids : str or list[str]
            CIDs to remove from the group.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            item = generic_payload_list(submitted_keywords=kwargs, payload_value="cids")
            if kwargs.get("cid_group_id", None):
                item["cid_group_id"] = kwargs.get("cid_group_id", None)
            body["resources"] = [item]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteCIDGroupMembersV2",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_cid_group_by_id_v1(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get CID Group(s) by ID(s).

        ** DEPRECATED **

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getCIDGroupById

        Keyword arguments
        -----------------
        cid_group_ids : str or list[str]
            CID group IDs to search for.
        parameters : dict
            full parameters payload, not required if `cid_group_ids` is provided
            as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'cid_group_ids'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getCIDGroupByIdV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "cid_group_ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_cid_group_by_id(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get CID Group(s) by ID(s).

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getCIDGroupByIdV2

        Keyword arguments
        -----------------
        ids : str or list[str]
            CID group IDs to search for. String or list of strings.
            The keyword `cid_group_ids` will also be accepted for this argument.
        parameters : dict
            full parameters payload, not required if `cid_group_ids` is provided
            as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'cid_group_ids'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("cid_group_ids", None) and not kwargs.get("ids", None):
            kwargs["ids"] = kwargs.get("cid_group_ids")

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getCIDGroupById",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_cid_groups(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create new CID Group(s). Maximum 500 CID Group(s) allowed.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/createCIDGroups

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if sha256 is provided as a keyword.
                {
                    "resources": [
                        {
                            "cid": "string",
                            "cid_group_id": "string",
                            "description": "string",
                            "name": "string"
                        }
                    ]
                }
        cid : str
            CID to initially add to the group.
        cid_group_id : str
            CID Group ID.
        description : str
            Description for the CID group.
        name : str
            Name of the CID group.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = mssp_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createCIDGroups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_cid_groups(self: object,
                          *args,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete CID Group(s) by ID(s).

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteCIDGroups

        Keyword arguments
        -----------------
        cid_group_ids : str or list[str]
            CID group IDs to search for.
        parameters : dict
            full parameters payload, not required if `cid_group_ids` is provided
            as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'cid_group_ids'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteCIDGroups",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "cid_group_ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_cid_groups(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update existing CID Group(s).

        CID Group ID is expected for each CID Group definition provided in request body.

        CID Group member(s) remain unaffected.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/updateCIDGroups

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if sha256 is provided as a keyword.
                {
                    "resources": [
                        {
                            "cid": "string",
                            "cid_group_id": "string",
                            "description": "string",
                            "name": "string"
                        }
                    ]
                }
        cid : str
            CID to initially add to the group.
        cid_group_id : str
            CID Group ID.
        description : str
            Description for the CID group.
        name : str
            Name of the CID group.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = mssp_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateCIDGroups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_roles_by_id(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get MSSP Role assignment(s).

        MSSP Role assignment is of the format <user_group_id>:<cid_group_id>.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getRolesByID

        Keyword arguments
        -----------------
        ids : str or list[str]
            MSSP Role assignment is of the format <user_group_id>:<cid_group_id>.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getRolesByID",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def add_role(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Assign new MSSP Role(s) between User Group and CID Group.

        It does not revoke existing role(s) between User Group and CID Group.
        User Group ID and CID Group ID have to be specified in request.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/addRole

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if sha256 is provided as a keyword.
                {
                    "resources": [
                        {
                            "cid_group_id": "string",
                            "id": "string",
                            "role_ids": [
                                "string"
                            ],
                            "user_group_id": "string"
                        }
                    ]
                }
        cid_group_id : str
            CID Group ID.
        id : str
            Role Assignment ID.
        role_ids : str or list[str]
            Role IDs to be assigned.
        user_group_ids : str
            User Group ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = mssp_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="addRole",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def delete_roles(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete MSSP Role assignment(s) between User Group and CID Group.

        User Group ID and CID Group ID have to be specified in request.
        Only specified roles are removed if specified in request payload,
        else association between User Group and CID Group is dissolved completely
        (if there are no roles specified).

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deletedRoles

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if sha256 is provided as a keyword.
                {
                    "resources": [
                        {
                            "cid_group_id": "string",
                            "id": "string",
                            "role_ids": [
                                "string"
                            ],
                            "user_group_id": "string"
                        }
                    ]
                }
        cid_group_id : str
            CID Group ID.
        id : str
            Role Assignment ID.
        role_ids : str or list[str]
            Role IDs to be assigned.
        user_group_ids : str
            User Group ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = mssp_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deletedRoles",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_user_group_members_by_id_v1(self: object,
                                        *args,
                                        parameters: dict = None,
                                        **kwargs
                                        ) -> dict:
        """Get User Group members by User Group ID(s).

        ** DEPRECATED **

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getUserGroupMembersByID

        Keyword arguments
        -----------------
        user_group_ids : str or list[str]
            User group IDs to search for.
        parameters : dict
            full parameters payload, not required if `user_group_ids` is provided
            as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'user_group_ids'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getUserGroupMembersByIDV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "user_group_ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_user_group_members_by_id(self: object,
                                     *args,
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get User Group members by User Group ID(s).

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getUserGroupMembersByIDV2

        Keyword arguments
        -----------------
        ids : str or list[str]
            User group IDs to search for. String or list of strings.
            The keyword `user_group_ids` will also be accepted for this argument.
        parameters : dict
            full parameters payload, not required if `user_group_ids` is provided
            as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'user_group_ids'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("user_group_ids", None) and not kwargs.get("ids", None):
            kwargs["ids"] = kwargs.get("user_group_ids")

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getUserGroupMembersByID",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def add_user_group_members(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add new User Group member. Maximum 500 members allowed per User Group.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/addUserGroupMembers

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if sha256 is provided as a keyword.
                {
                    "resources": [
                        {
                            "user_group_id": "string",
                            "user_uuids": [
                                "string"
                            ]
                        }
                    ]
                }
        user_group_ids : str
            User Group ID.
        user_uuids : str or list[str]
            User UUIDs to assign to group.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = mssp_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="addUserGroupMembers",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def delete_user_group_members(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete User Group members entry.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteUserGroupMembers

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if sha256 is provided as a keyword.
                {
                    "resources": [
                        {
                            "user_group_id": "string",
                            "user_uuids": [
                                "string"
                            ]
                        }
                    ]
                }
        user_group_ids : str
            User Group ID.
        user_uuids : str or list[str]
            User UUIDs to remove from group.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = mssp_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteUserGroupMembers",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_user_groups_by_id_v1(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get User Groups by ID(s).

        ** DEPRECATED **

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getUserGroupsByID

        Keyword arguments
        -----------------
        user_group_ids : str or list[str]
            User group IDs to search for.
        parameters : dict
            full parameters payload, not required if `user_group_ids` is provided
            as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'user_group_ids'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getUserGroupsByIDV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "user_group_ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_user_groups_by_id(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get User Groups by ID(s).

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/getUserGroupsByIDV2

        Keyword arguments
        -----------------
        ids : str or list[str]
            User group IDs to search for. String or list of strings.
            The keyword `user_group_ids` will also be accepted for this argument.
        parameters : dict
            full parameters payload, not required if `user_group_ids` is provided
            as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'user_group_ids'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("user_group_ids", None) and not kwargs.get("ids", None):
            kwargs["ids"] = kwargs.get("user_group_ids")

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getUserGroupsByID",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_user_groups(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create new User Group(s). Maximum 500 User Group(s) allowed per customer.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/createUserGroup

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if sha256 is provided as a keyword.
                {
                    "resources": [
                        {
                            "cid": "string",
                            "description": "string",
                            "name": "string",
                            "user_group_id": "string"
                        }
                    ]
                }
        cid : str
            CID to initially add to the group.
        description : str
            Description for the CID group.
        name : str
            Name of the CID group.
        user_group_id : str
            User Group ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = mssp_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createUserGroups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_user_groups(self: object,
                           *args,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete User Group(s) by ID(s).

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/deleteUserGroups

        Keyword arguments
        -----------------
        user_group_ids : str or list[str]
            User group IDs to delete.
        parameters : dict
            full parameters payload, not required if `user_group_ids` is provided
            as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'user_group_ids'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteUserGroups",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "user_group_ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_user_groups(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update existing User Group(s).

        User Group ID is expected for each User Group definition provided in request body.

        User Group member(s) remain unaffected.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/updateUserGroups

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if sha256 is provided as a keyword.
                {
                    "resources": [
                        {
                            "cid": "string",
                            "description": "string",
                            "name": "string",
                            "user_group_id": "string"
                        }
                    ]
                }
        cid : str
            CID to initially add to the group.
        description : str
            Description for the CID group.
        name : str
            Name of the CID group.
        user_group_id : str
            User Group ID to update.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = mssp_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateUserGroups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_children(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query for customers linked as children.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryChildren

        Keyword arguments
        -----------------
        filter : str
            FQL formatted string used to limit results. String. Supported filter: cid
        limit : int
            The maximum number of records to return in this response. [Integer, 1-1000]
            Use with the offset parameter to manage pagination of results. Default: 10
        offset : int
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax. (Ex: `last_modified_timestamp|desc`)

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryChildren",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_cid_group_members(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query a CID Groups members by associated CID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryCIDGroupMembers

        Keyword arguments
        -----------------
        cid : str
            CID to lookup associated CID group ID
        limit : int
            The maximum number of records to return in this response. [Integer, 1-1000]
            Use with the offset parameter to manage pagination of results. Default: 10
        offset : int
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax. (Ex: `last_modified_timestamp|desc`)

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCIDGroupMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_cid_groups(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query a CID Groups.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryCIDGroups

        Keyword arguments
        -----------------
        name : str
            Name to lookup groups for
        limit : int
            The maximum number of records to return in this response. [Integer, 1-1000]
            Use with the offset parameter to manage pagination of results. Default: 10
        offset : int
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax. (Ex: `last_modified_timestamp|desc`)

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCIDGroups",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_roles(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query links between user groups and CID groups.

        At least one of CID Group ID or User Group ID should also be provided. Role ID is optional.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryRoles

        Keyword arguments
        -----------------
        user_group_id : str
            User group ID to fetch MSSP role for
        cid_group_id : str
            CID group ID to fetch MSSP role for
        role_id : str
            Role ID to fetch MSSP role for
        limit : int
            The maximum number of records to return in this response. [Integer, 1-1000]
            Use with the offset parameter to manage pagination of results. Default: 10
        offset : int
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax. (Ex: `last_modified_timestamp|desc`)

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryRoles",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_user_group_members(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query User Group member by User UUID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryRoles

        Keyword arguments
        -----------------
        user_uuid : str
            User UUID to lookup associated user group ID
        limit : int
            The maximum number of records to return in this response. [Integer, 1-1000]
            Use with the offset parameter to manage pagination of results. Default: 10
        offset : int
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax. (Ex: `last_modified_timestamp|desc`)

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryUserGroupMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_user_groups(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query User Groups.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/mssp/queryUserGroups

        Keyword arguments
        -----------------
        name : str
            Name to lookup groups for
        limit : int
            The maximum number of records to return in this response. [Integer, 1-1000]
            Use with the offset parameter to manage pagination of results. Default: 10
        offset : int
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax. (Ex: `last_modified_timestamp|desc`)

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
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
    getCIDGroupMembersByV1 = get_cid_group_members_by_v1
    getCIDGroupMembersByV2 = get_cid_group_members_by
    addCIDGroupMembers = add_cid_group_members
    deleteCIDGroupMembers = delete_cid_group_members
    deleteCIDGroupMembersV1 = delete_cid_group_members_v1
    deleteCIDGroupMembersV2 = delete_cid_group_members
    getCIDGroupById = get_cid_group_by_id
    getCIDGroupByIdV1 = get_cid_group_by_id_v1
    getCIDGroupByIdV2 = get_cid_group_by_id
    createCIDGroups = create_cid_groups
    deleteCIDGroups = delete_cid_groups
    updateCIDGroups = update_cid_groups
    getRolesByID = get_roles_by_id
    addRole = add_role
    deletedRoles = delete_roles
    deleteRoles = delete_roles  # Typo fix
    getUserGroupMembersByID = get_user_group_members_by_id
    getUserGroupMembersByIDV1 = get_user_group_members_by_id_v1
    getUserGroupMembersByIDV2 = get_user_group_members_by_id
    addUserGroupMembers = add_user_group_members
    deleteUserGroupMembers = delete_user_group_members
    getUserGroupsByID = get_user_groups_by_id
    getUserGroupsByIDV1 = get_user_groups_by_id_v1
    getUserGroupsByIDV2 = get_user_groups_by_id
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
