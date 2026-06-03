"""CrowdStrike Falcon ProfileGroups API interface class.

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
from typing import Dict, Union
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import create_group_v1_mixin0_payload, get_group_users_v1_payload, get_groups_v1_mixin0_payload, get_user_groups_v1_payload, group_actions_v1_mixin0_payload, group_users_actions_v1_mixin0_payload, update_group_v1_mixin0_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._profile_groups import _profile_groups_endpoints as Endpoints


class ProfileGroups(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (oauth2.py)
    """

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def group_actions_v1_mixin0(self: object,
                                body: dict = None,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Perform actions on profile groups (add/remove roles, user groups, FGA objects).

        Keyword arguments:
        action_name -- Action to perform Available values: add_roles, remove_roles, add_user_groups, remove_user_groups,
                       add_fga_objects, remove_fga_objects. String.
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "action_parameters": [
                        {
                            "name": "string",
                            "value": "string"
                        }
                    ],
                    "filter": "string",
                    "ids": [
                        "string"
                    ]
                }
        action_parameters -- The action_parameters value. List.
        filter -- The filter value. String.
        ids -- The ids value. List.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/profile-groups/GroupActionsV1Mixin0
        """
        if not body:
            body = group_actions_v1_mixin0_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GroupActionsV1Mixin0",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def group_users_actions_v1_mixin0(self: object,
                                      body: dict = None,
                                      parameters: dict = None,
                                      **kwargs
                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add or remove users from profile groups.

        Keyword arguments:
        action_name -- Action to perform Available values: add_users, remove_users. String.
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "action_parameters": [
                        {
                            "name": "string",
                            "value": "string"
                        }
                    ],
                    "filter": "string",
                    "ids": [
                        "string"
                    ]
                }
        action_parameters -- The action_parameters value. List.
        filter -- The filter value. String.
        ids -- The ids value. List.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/profile-groups/GroupUsersActionsV1Mixin0
        """
        if not body:
            body = group_users_actions_v1_mixin0_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GroupUsersActionsV1Mixin0",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_group_users_v1(self: object,
                           body: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a list of groups with users that belong to them.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids -- Profile Group IDs to get users for List.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/profile-groups/GetGroupUsersV1
        """
        if not body:
            body = get_group_users_v1_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetGroupUsersV1",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_groups_v1_mixin0(self: object,
                             body: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get profile groups by IDs with full details.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids -- Profile Group IDs to retrieve List.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/profile-groups/GetGroupsV1Mixin0
        """
        if not body:
            body = get_groups_v1_mixin0_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetGroupsV1Mixin0",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_group_v1_mixin0(self: object,
                               body: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new profile group.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "cid": "string",
                    "description": "string",
                    "name": "string"
                }
        cid -- CID for the new profile group in a Flight Control environment String.
        description -- Optional description for the group String.
        name -- Name for the new profile group String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/profile-groups/CreateGroupV1Mixin0
        """
        if not body:
            body = create_group_v1_mixin0_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateGroupV1Mixin0",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_groups_v1(self: object,
                         *args,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete profile groups by IDs.

        Keyword arguments:
        ids -- Group IDs to delete String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/profile-groups/DeleteGroupsV1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteGroupsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_group_v1_mixin0(self: object,
                               body: dict = None,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update profile group metadata (name, description).

        Keyword arguments:
        id -- ID of the group to update String.
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "description": "string",
                    "name": "string"
                }
        description -- New description for the group String.
        name -- New name for the group String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/profile-groups/UpdateGroupV1Mixin0
        """
        if not body:
            body = update_group_v1_mixin0_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateGroupV1Mixin0",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_user_groups_v1(self: object,
                           body: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a list of users with the groups that they belong to.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids -- User UUIDs to get groups for List.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/profile-groups/GetUserGroupsV1
        """
        if not body:
            body = get_user_groups_v1_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetUserGroupsV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_groups_v1_mixin0(self: object,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query profile group IDs with FQL filtering, pagination, and sorting.

        Keyword arguments:
        filter -- FQL filter expression to filter groups by name or cid String.
        sort -- Sort by field|direction (name, updated_at, member_count) String.
        offset -- Number of groups to skip Integer.
        limit -- Maximum groups to return [1-500] Integer.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/profile-groups/QueryGroupsV1Mixin0
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryGroupsV1Mixin0",
            keywords=kwargs,
            params=parameters
            )
    GroupActionsV1Mixin0 = group_actions_v1_mixin0
    GroupUsersActionsV1Mixin0 = group_users_actions_v1_mixin0
    GetGroupUsersV1 = get_group_users_v1
    GetGroupsV1Mixin0 = get_groups_v1_mixin0
    CreateGroupV1Mixin0 = create_group_v1_mixin0
    DeleteGroupsV1 = delete_groups_v1
    UpdateGroupV1Mixin0 = update_group_v1_mixin0
    GetUserGroupsV1 = get_user_groups_v1
    QueryGroupsV1Mixin0 = query_groups_v1_mixin0
