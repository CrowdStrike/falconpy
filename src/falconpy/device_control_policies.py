"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

device_control_policies - CrowdStrike Falcon Device Control Policies API interface class

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
from ._util import generate_error_result, force_default, args_to_params, process_service_request, handle_single_argument
from ._service_class import ServiceClass
from ._endpoint._device_control_policies import _device_control_policies_endpoints as Endpoints


class DeviceControlPolicies(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Device Control Policy in your environment by providing an FQL filter
        and paging details. Returns a set of host details which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...   /device-control-policies/queryCombinedDeviceControlPolicyMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedDeviceControlPolicyMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Device Control Policies in your environment by providing an FQL filter and
        paging details. Returns a set of Device Control Policies which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /device-control-policies/queryCombinedDeviceControlPolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedDeviceControlPolicies",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def perform_action(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Device Control Policies in your environment by providing an FQL filter
        and paging details. Returns a set of Device Control Policies which match the filter criteria.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /device-control-policies/performDeviceControlPoliciesAction
        _allowed_actions = ['add-host-group', 'disable', 'enable', 'remove-host-group']
        operation_id = "performDeviceControlPoliciesAction"
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

    def set_precedence(self: object, body: dict) -> dict:
        """
        Sets the precedence of Device Control Policies based on the order of IDs specified in the request.
        The first ID specified will have the highest precedence and the last ID specified will have the lowest.
        You must specify all non-Default Policies for a platform when updating precedence.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /device-control-policies/performDeviceControlPoliciesAction
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="setDeviceControlPoliciesPrecedence",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a set of Device Control Policies by specifying their IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /device-control-policies/getDeviceControlPolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getDeviceControlPolicies",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def create_policies(self: object, body: dict) -> dict:
        """
        Create Device Control Policies by specifying details about the policy to create.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /device-control-policies/createDeviceControlPolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createDeviceControlPolicies",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a set of Device Control Policies by specifying their IDs.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          ...  /device-control-policies/createDeviceControlPolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteDeviceControlPolicies",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def update_policies(self: object, body: dict) -> dict:
        """
        Update Device Control Policies by specifying the ID of the policy and details to update.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         ...   /device-control-policies/updateDeviceControlPolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateDeviceControlPolicies",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Device Control Policy in your environment by providing an FQL filter
        and paging details. Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /device-control-policies/queryDeviceControlPolicyMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryDeviceControlPolicyMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Device Control Policies in your environment by providing an FQL filter and paging details.
        Returns a set of Device Control Policy IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /device-control-policies/queryDeviceControlPolicyMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryDeviceControlPolicies",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    queryCombinedDeviceControlPolicyMembers = query_combined_policy_members
    queryCombinedDeviceControlPolicies = query_combined_policies
    performDeviceControlPoliciesAction = perform_action
    setDeviceControlPoliciesPrecedence = set_precedence
    getDeviceControlPolicies = get_policies
    createDeviceControlPolicies = create_policies
    deleteDeviceControlPolicies = delete_policies
    updateDeviceControlPolicies = update_policies
    queryDeviceControlPolicyMembers = query_policy_members
    queryDeviceControlPolicies = query_policies


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Device_Control_Policies = DeviceControlPolicies  # pylint: disable=C0103
