"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

host_groups - CrowdStrike Falcon Host Groups API interface class

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

from ._util import generate_error_result, force_default, args_to_params, handle_single_argument, process_service_request
from ._service_class import ServiceClass
from ._endpoint._host_group import _host_group_endpoints as Endpoints


class HostGroup(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_group_members(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Host Group in your environment by providing an FQL filter
        and paging details. Returns a set of host details which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/queryCombinedGroupMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedGroupMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_host_groups(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Host Groups in your environment by providing an FQL filter and
        paging details. Returns a set of Host Groups which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/queryCombinedHostGroups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedHostGroups",
            keywords=kwargs,
            params=parameters
            )

    def perform_group_action(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Perform the specified action on the Host Groups specified in the request.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/performGroupAction
        _allowed_actions = ['add-hosts', 'remove-hosts']
        operation_id = "performGroupAction"
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        action_name = parameter_payload.get("action_name", "Not Specified")
        if action_name.lower() in _allowed_actions:
            returned = process_service_request(
                            calling_object=self,
                            endpoints=Endpoints,
                            operation_id=operation_id,
                            body=body,
                            keywords=kwargs,
                            params=parameters
                            )
        else:
            returned = generate_error_result("Invalid value specified for action_name parameter.")

        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_host_groups(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a set of Host Groups by specifying their IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/getHostGroups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getHostGroups",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def create_host_groups(self: object, body: dict) -> dict:
        """
        Create Host Groups by specifying details about the group to create.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/createHostGroups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createHostGroups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_host_groups(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a set of Host Groups by specifying their IDs.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/deleteHostGroups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteHostGroups",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def update_host_groups(self: object, body: dict) -> dict:
        """
        Update Host Groups by specifying the ID of the group and details to update.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/updateHostGroups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateHostGroups",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_group_members(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Host Group in your environment by providing an FQL filter
        and paging details. Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/queryGroupMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryGroupMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_host_groups(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Host Groups in your environment by providing an FQL filter and
        paging details. Returns a set of Host Group IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/queryHostGroups
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryHostGroups",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    queryCombinedGroupMembers = query_combined_group_members
    queryCombinedHostGroups = query_combined_host_groups
    performGroupAction = perform_group_action
    getHostGroups = get_host_groups
    createHostGroups = create_host_groups
    deleteHostGroups = delete_host_groups
    updateHostGroups = update_host_groups
    queryGroupMembers = query_group_members
    queryHostGroups = query_host_groups


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Host_Group = HostGroup  # pylint: disable=C0103
