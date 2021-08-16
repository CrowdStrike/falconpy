"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

sensor_update_policy - CrowdStrike Falcon Sensor Policy Management API interface class

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
from ._util import generate_error_result, args_to_params, force_default, handle_single_argument, process_service_request
from ._service_class import ServiceClass
from ._endpoint._sensor_update_policies import _sensor_update_policies_endpoints as Endpoints


class SensorUpdatePolicy(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def reveal_uninstall_token(self: object, body: dict) -> dict:
        """
        Reveals an uninstall token for a specific device.
        To retrieve the bulk maintenance token pass the value 'MAINTENANCE' as the value for 'device_id'.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/revealUninstallToken
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="revealUninstallToken",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_builds(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve available builds for use with Sensor Update Policies.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/queryCombinedSensorUpdateBuilds
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedSensorUpdateBuilds",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "platform")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Sensor Update Policy in your environment by providing an FQL
        filter and paging details. Returns a set of host details which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/queryCombinedSensorUpdatePolicyMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedSensorUpdatePolicyMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Sensor Update Policies in your environment by providing an FQL filter and paging details.
        Returns a set of Sensor Update Policies which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/queryCombinedSensorUpdatePolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedSensorUpdatePolicies",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_policies_v2(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Sensor Update Policies with additional support for uninstall protection in your environment
        by providing an FQL filter and paging details.
        Returns a set of Sensor Update Policies which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/queryCombinedSensorUpdatePoliciesV2
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedSensorUpdatePoliciesV2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def perform_policies_action(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Perform the specified action on the Sensor Update Policies specified in the request.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /sensor-update-policies/performSensorUpdatePoliciesAction
        _allowed_actions = ['add-host-group', 'disable', 'enable', 'remove-host-group']
        operation_id = "performSensorUpdatePoliciesAction"
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

    def set_policies_precedence(self: object, body: dict) -> dict:
        """
        Sets the precedence of Sensor Update Policies based on the order of IDs specified in the request.
        The first ID specified will have the highest precedence and the last ID specified will have the lowest.
        You must specify all non-Default Policies for a platform when updating precedence.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /sensor-update-policies/setSensorUpdatePoliciesPrecedence
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="setSensorUpdatePoliciesPrecedence",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a set of Sensor Update Policies by specifying their IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/getSensorUpdatePolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getSensorUpdatePolicies",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def create_policies(self: object, body: dict) -> dict:
        """
        Create Sensor Update Policies by specifying details about the policy to create.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /sensor-update-policies/createSensorUpdatePolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createSensorUpdatePolicies",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Delete a set of Sensor Update Policies by specifying their IDs.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          ...  /sensor-update-policies/deleteSensorUpdatePolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteSensorUpdatePolicies",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def update_policies(self: object, body: dict) -> dict:
        """
        Update Sensor Update Policies by specifying the ID of the policy and details to update.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         ...   /sensor-update-policies/updateSensorUpdatePolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateSensorUpdatePolicies",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policies_v2(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve a set of Sensor Update Policies with additional
        support for uninstall protection by specifying their IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/getSensorUpdatePoliciesV2
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getSensorUpdatePoliciesV2",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def create_policies_v2(self: object, body: dict) -> dict:
        """
        Create Sensor Update Policies by specifying details about the
        policy to create with additional support for uninstall protection.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #        ...    /sensor-update-policies/createSensorUpdatePoliciesV2
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createSensorUpdatePoliciesV2",
            body=body
            )

    def update_policies_v2(self: object, body: dict) -> dict:
        """
        Update Sensor Update Policies by specifying the ID of the policy
        and details to update with additional support for uninstall protection.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         ...   /sensor-update-policies/updateSensorUpdatePoliciesV2
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateSensorUpdatePoliciesV2",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for members of a Sensor Update Policy in your environment by providing an FQL
        filter and paging details. Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/querySensorUpdatePolicyMembers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="querySensorUpdatePolicyMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policies(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for Sensor Update Policies in your environment by providing an FQL filter and
        paging details. Returns a set of Sensor Update Policy IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /sensor-update-policies/querySensorUpdatePolicies
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="querySensorUpdatePolicies",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    revealUninstallToken = reveal_uninstall_token
    queryCombinedSensorUpdateBuilds = query_combined_builds
    queryCombinedSensorUpdatePolicyMembers = query_combined_policy_members
    queryCombinedSensorUpdatePolicies = query_combined_policies
    queryCombinedSensorUpdatePoliciesV2 = query_combined_policies_v2
    performSensorUpdatePoliciesAction = perform_policies_action
    setSensorUpdatePoliciesPrecedence = set_policies_precedence
    getSensorUpdatePolicies = get_policies
    createSensorUpdatePolicies = create_policies
    deleteSensorUpdatePolicies = delete_policies
    updateSensorUpdatePolicies = update_policies
    getSensorUpdatePoliciesV2 = get_policies_v2
    createSensorUpdatePoliciesV2 = create_policies_v2
    updateSensorUpdatePoliciesV2 = update_policies_v2
    querySensorUpdatePolicyMembers = query_policy_members
    querySensorUpdatePolicies = query_policies


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Sensor_Update_Policy = SensorUpdatePolicy  # pylint: disable=C0103
