"""CrowdStrike Falcon Device Control Policies API interface class.

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
from ._util import generate_error_result, force_default, args_to_params
from ._util import process_service_request, handle_single_argument
from ._payload import generic_payload_list, device_policy_payload
from ._service_class import ServiceClass
from ._endpoint._device_control_policies import _device_control_policies_endpoints as Endpoints


class DeviceControlPolicies(ServiceClass):
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
    def query_combined_policy_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Search for a Device Control Policy members and return full detail.

        Search for members of a Device Control Policy in your environment by
        providing an FQL filter and paging details. Returns a set of host details
        which match the filter criteria.

        Keyword arguments:
        id -- The ID of the Device Control Policy to search for members of
        filter -- The filter expression that should be used to limit the results. FQL syntax.
        limit -- The maximum number of records to return in this response. [Integer, 1-5000]
                 Use with the offset parameter to manage pagination of results.
        offset -- The offset to start retrieving records from. Integer.
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.
        sort -- The property to sort by. FQL syntax.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
                    /device-control-policies/queryCombinedDeviceControlPolicyMembers
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedDeviceControlPolicyMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_combined_policies(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Search for a Device Control Policies and return full detail.

        Search for Device Control Policies in your environment by providing an FQL filter and
        paging details. Returns a set of Device Control Policies which match the filter criteria.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
        limit -- The maximum number of records to return in this response. [Integer, 1-5000]
                 Use with the offset parameter to manage pagination of results.
        offset -- The offset to start retrieving records from. Integer.
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.
        sort -- The property to sort by. FQL syntax.
                created_by                      modified_timestamp
                created_timestamp               name
                enabled                         platform_name
                modified_by                     precedence

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
                    /device-control-policies/queryCombinedDeviceControlPolicies
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryCombinedDeviceControlPolicies",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def perform_action(self: object, body: dict = None, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Perform a Device Control Policy action.

        Keyword arguments:
        action_name -- action to perform: 'add-host-group', 'disable', 'enable',
                       or 'remove-host-group'.
        action_parameters -- Action specific parameter options. List of dictionaries.
                             {
                                 "name": "string",
                                 "value": "string"
                             }
        body -- full body payload, not required if keywords are used.
                {
                    "action_parameters": [
                        {
                            "name": "group_id",
                            "value": "string"
                        }
                    ],
                    "ids": [
                        "string"
                    ]
                }
        group_id -- Host Group ID to apply the policy to. String.
                    Overridden if action_parameters is specified.
        ids -- Device Control policy ID(s) to perform actions against. String or list of strings.
        parameters - full parameters payload, not required if action_name is provided as a keyword.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
                    /device-control-policies/performDeviceControlPoliciesAction
        """
        _allowed_actions = ['add-host-group', 'disable', 'enable', 'remove-host-group']
        operation_id = "performDeviceControlPoliciesAction"
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        action_name = parameter_payload.get("action_name", "Not Specified")
        if action_name.lower() in _allowed_actions:
            if not body:
                body = generic_payload_list(submitted_keywords=kwargs, payload_value="ids")
                if kwargs.get("group_id", None):
                    body["action_parameters"] = [{
                        "name": "group_id",
                        "value": kwargs.get("group_id", None)
                    }]
                # Passing an action_parameters list will override the group_id keyword
                if kwargs.get("action_parameters", None):
                    body["action_parameters"] = kwargs.get("action_parameters", None)

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

    @force_default(defaults=["body"], default_types=["dict"])
    def set_precedence(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Set Device Control Policy precedence.

        Sets the precedence of Device Control Policies based on the order of IDs specified in
        the request. The first ID specified will have the highest precedence and the last ID
        specified will have the lowest. You must specify all non-Default Policies for a platform
        when updating precedence.

        Keyword arguments:
        body -- full body payload, not required if keywords are used.
                {
                    "ids": [
                        "string"
                    ],
                    "platform_name": "Windows"
                }
        ids -- Device Control policy ID(s) to perform actions against. String or list of strings.
        platform_name -- OS platform name.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
                    /device-control-policies/performDeviceControlPoliciesAction
        """
        if not body:
            body = generic_payload_list(submitted_keywords=kwargs, payload_value="ids")
            if kwargs.get("platform_name", None):
                body["platform_name"] = kwargs.get("platform_name", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="setDeviceControlPoliciesPrecedence",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policies(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Retrieve a set of Device Control Policies by specifying their IDs.

        Keyword arguments:
        ids -- List of Device Control Policy IDs to retrieve. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
                    /device-control-policies/getDeviceControlPolicies
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getDeviceControlPolicies",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_policies(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Create Device Control Policies by specifying details about the policy to create.

        Keyword arguments:
        body -- full body payload, not required if keywords are used.
                {
                "resources": [
                    {
                        "clone_id": "string",
                        "description": "string",
                        "name": "string",
                        "platform_name": "Windows",
                        "settings": {
                            "classes": [
                            {
                                "action": "FULL_ACCESS",
                                "exceptions": [
                                {
                                    "action": "string",
                                    "class": "string",
                                    "combined_id": "string",
                                    "id": "string",
                                    "match_method": "string",
                                    "product_id": "string",
                                    "product_id_decimal": "string",
                                    "product_name": "string",
                                    "serial_number": "string",
                                    "vendor_id": "string",
                                    "vendor_id_decimal": "string",
                                    "vendor_name": "string"
                                }
                                ],
                                "id": "string"
                            }
                            ],
                            "end_user_notification": "TRUE",
                            "enforcement_mode": "string",
                            "id": "string"
                        }
                    }
                ]
            }
        clone_id -- ID of the Device Control Policy to clone. String.
        description -- Device Control Policy description. String.
        name -- Device Control Policy name. String.
        platform_name -- Name of the operating system platform. String.
        settings -- Device Control policy specific settings. Dictionary.
                    See above for JSON dictionary format example.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
                    /device-control-policies/createDeviceControlPolicies
        """
        if not body:
            body = device_policy_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="createDeviceControlPolicies",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_policies(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Delete a set of Device Control Policies by specifying their IDs.

        Keyword arguments:
        ids -- List of Device Control Policy IDs to delete. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
                    /device-control-policies/createDeviceControlPolicies
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="deleteDeviceControlPolicies",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_policies(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Update Device Control Policies by specifying the ID of the policy and details to update.

        Keyword arguments:
        body -- full body payload, not required if keywords are used.
                {
                "resources": [
                    {
                        "clone_id": "string",
                        "description": "string",
                        "name": "string",
                        "platform_name": "Windows",
                        "settings": {
                            "classes": [
                            {
                                "action": "FULL_ACCESS",
                                "exceptions": [
                                {
                                    "action": "string",
                                    "class": "string",
                                    "combined_id": "string",
                                    "id": "string",
                                    "match_method": "string",
                                    "product_id": "string",
                                    "product_id_decimal": "string",
                                    "product_name": "string",
                                    "serial_number": "string",
                                    "vendor_id": "string",
                                    "vendor_id_decimal": "string",
                                    "vendor_name": "string"
                                }
                                ],
                                "id": "string"
                            }
                            ],
                            "end_user_notification": "TRUE",
                            "enforcement_mode": "string",
                            "id": "string"
                        }
                    }
                ]
            }
        id -- ID of the Device Control Policy to update. String.
        description -- Device Control Policy description. String.
        name -- Device Control Policy name. String.
        settings -- Device Control policy specific settings. Dictionary.
                    See above for JSON dictionary format example.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
                    /device-control-policies/updateDeviceControlPolicies
        """
        if not body:
            body = device_policy_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="updateDeviceControlPolicies",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policy_members(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Search for a Device Control Policy members and return their IDs.

        Search for members of a Device Control Policy in your environment by providing
        an FQL filter and paging details. Returns a set of Agent IDs which match the filter
        criteria.

        Keyword arguments:
        id -- The ID of the Device Control Policy to search for members of
        filter -- The filter expression that should be used to limit the results. FQL syntax.
        limit -- The maximum number of records to return in this response. [Integer, 1-5000]
                 Use with the offset parameter to manage pagination of results.
        offset -- The offset to start retrieving records from. Integer.
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.
        sort -- The property to sort by. FQL syntax.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
                    /device-control-policies/queryDeviceControlPolicyMembers
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryDeviceControlPolicyMembers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_policies(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Search for a Device Control Policies and return their IDs.

        Search for Device Control Policies in your environment by providing an
        FQL filter and paging details. Returns a set of Device Control Policy IDs
        which match the filter criteria.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
        limit -- The maximum number of records to return in this response. [Integer, 1-5000]
                 Use with the offset parameter to manage pagination of results.
        offset -- The offset to start retrieving records from. Integer.
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.
        sort -- The property to sort by. FQL syntax.
                created_by                      modified_timestamp
                created_timestamp               name
                enabled                         platform_name
                modified_by                     precedence

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
                    /device-control-policies/queryDeviceControlPolicyMembers
        """
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
