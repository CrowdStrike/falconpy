"""CrowdStrike Falcon Hosts API interface class.

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
from ._util import generate_error_result, force_default, args_to_params
from ._util import process_service_request, handle_single_argument
from ._payload import generic_payload_list, simple_action_parameter
from ._service_class import ServiceClass
from ._endpoint._hosts import _hosts_endpoints as Endpoints


class Hosts(ServiceClass):
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

    @force_default(defaults=["parameters", "body"], default_types=["dict"])
    def perform_action(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
        """Take various actions on the hosts in your environment.

        Contain or lift containment on a host. Delete or restore a host.

        Keyword arguments:
        action_name -- action to perform, 'contain', 'lift_containment',
                       'hide_host', 'unhide_host', 'detection_suppress', or
                       'detection_unsuppress'.
        body -- full body payload, not required if ids are provided as keyword.
                You must use body if you are going to specify action_parameters.
                {
                    "action_parameters": [
                        {
                        "name": "string",
                        "value": "string"
                        }
                    ],
                    "ids": [
                        "string"
                    ]
                }
        ids -- AID(s) to perform actions against. String or list of strings.
        note -- a custom note that is attached to the action. String.
        parameters - full parameters payload, not required if action_name is provide as a keyword.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/PerformActionV2
        """
        if not body:
            body = generic_payload_list(submitted_keywords=kwargs, payload_value="ids")

        _allowed_actions = ['contain', 'lift_containment', 'hide_host', 'unhide_host']
        operation_id = "PerformActionV2"
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        action_name = parameter_payload.get("action_name", "Not Specified")
        # Only process allowed actions
        if action_name.lower() in _allowed_actions:
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id=operation_id,
                body=body,
                keywords=kwargs,
                params=parameters,
                body_validator={"ids": list} if self.validate_payloads else None,
                body_required=["ids"] if self.validate_payloads else None
                )
        else:
            returned = generate_error_result("Invalid value specified for action_name parameter.")

        return returned

    @force_default(defaults=["parameters", "body"], default_types=["dict"])
    def perform_group_action(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
        """Take various actions on the provided prevention policy IDs.

        Keyword arguments:
        action_name -- action to perform, 'add_group_member', 'remove_all',
                       'remove_group_member'. String.
        action_parameters -- Action parameter payload. List of dictionaries.
        body -- full body payload, not required if ids are provided as keyword.
                You must use body if you are going to specify action_parameters.
                {
                    "action_parameters": [
                        {
                        "name": "string",
                        "value": "string"
                        }
                    ]
                }
        ids -- Group ID(s) to perform actions against. String or list of strings.
        parameters - full parameters payload, not required if action_name is provide as a keyword.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/PerformActionV2
        """
        if not body:
            body = simple_action_parameter(passed_keywords=kwargs)

        _allowed_actions = ['add_group_member', 'remove_all', 'remove_group_member']
        operation_id = "entities_perform_action"
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        action_name = parameter_payload.get("action_name", "Not Specified")
        # Only process allowed actions
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
            returned = generate_error_result("Invalid value specified for action_name parameter.",
                                             code=400
                                             )

        return returned

    def update_device_tags(self: object,
                           action_name: str,
                           ids: list or str,
                           tags: list or str
                           ) -> dict:
        """Append or remove one or more Falcon Grouping Tags on one or more hosts.

        Keyword arguments:
        action_name -- action to perform, 'add' or 'remove'.
        ids -- AID(s) of the hosts to update. String or list of strings.
        tags -- Tag(s) to update. String or list of strings.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/UpdateDeviceTags
        """
        # BODY PAYLOAD MODEL (For Uber class reference)
        # {
        #   "action": "string",
        #   "device_ids": [
        #     "string"
        #   ],
        #   "tags": [
        #     "string"
        #   ]
        # }
        #
        _allowed_actions = ["add", "remove"]
        # validate action is allowed AND tags is "something"
        if action_name.lower() in _allowed_actions and tags is not None:
            # convert ids/tags to be a list object if not already
            if isinstance(ids, str):
                ids = ids.split(",")
            if isinstance(tags, str):
                tags = tags.split(",")
            # tags must start with FalconGroupingTags,
            # users may won't know this so add it for them
            patch_tag = []
            for tag in tags:
                if tag.startswith("FalconGroupingTags/"):
                    patch_tag.append(tag)
                else:
                    tag_name = "FalconGroupingTags/" + tag
                    patch_tag.append(tag_name)
            body_payload = {
                "action": action_name,
                "device_ids": ids,
                "tags": patch_tag
            }
            returned = process_service_request(
                calling_object=self,
                endpoints=Endpoints,
                operation_id="UpdateDeviceTags",
                body=body_payload,
                )
        else:
            returned = generate_error_result("Invalid value specified for action_name parameter.")
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_device_details_v1(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get details on one or more hosts by providing agent IDs (AID).

        You can get a host's agent IDs (AIDs) from query_devices_by_filter,
        the Falcon console or the Streaming API.

        Keyword arguments:
        ids -- AID(s) of the hosts to retrieve. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/GetDeviceDetails
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetDeviceDetailsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_device_details_v2(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get details on one or more hosts by providing agent IDs (AID).

        You can get a host's agent IDs (AIDs) from query_devices_by_filter,
        the Falcon console or the Streaming API. Supports up to a maximum of 100 IDs.

        For most scenarios, developers should leverage the 'get_device_details' method
        (PostDeviceDetailsV2 operation) instead of this method.

        Keyword arguments:
        ids -- AID(s) of the hosts to retrieve. String or list of strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/GetDeviceDetailsV2
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetDeviceDetailsV2",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def get_device_details(self: object,
                           *args,
                           body: dict = None,
                           parameters: dict = None,
                           **kwargs
                           ) -> dict:
        """Get details on one or more hosts by providing agent IDs (AID).

        You can get a host's agent IDs (AIDs) from query_devices_by_filter,
        the Falcon console or the Streaming API. Supports up to a maximum of 5000 IDs.

        FOR DEVELOPERS: This Operation ID is `PostDeviceDetailsV2`, and is the preferred method
        for retrieving device details from the API. In order to assist developers leveraging the
        legacy GetDeviceDetails operation, this method has been updated to handle IDs passed as
        a query string parameter, allowing for legacy aliases and methods to be redirected to this
        new method.

        Keyword arguments:
        body -- full body payload, not required if ids is provided as a keyword.
        ids -- AID(s) of the hosts to retrieve. String or list of strings.
        parameters - full parameters payload, ignored unless this is the only location of the
                     'ids' list. Should not be used.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/PostDeviceDetailsV2
        """
        # Catch any IDs passed as arguments, will be discarded if a body payload is provided
        parameters = handle_single_argument(args, parameters, "ids")

        if not body:
            body = generic_payload_list(submitted_keywords=kwargs, payload_value="ids")
            # Try to gracefully catch IDs passed incorrectly as a query string parameter
            if parameters:
                if "ids" in parameters and "ids" not in body:
                    body["ids"] = parameters["ids"]

        if "ids" in body:
            # Make sure the provided ids are a properly formatted list
            if isinstance(body["ids"], str):
                body["ids"] = body["ids"].split(",")

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PostDeviceDetailsV2",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_online_state(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Get the online status for one or more hosts by specifying each host’s unique ID.

        Successful requests return an HTTP 200 response and the status for each host identified
        by a `state` of `online`, `offline`, or `unknown` for each host, identified by host `id`.
        Make a `GET` request to `QueryDevicesByFilter` or `QueryDevicesByFilterScroll` to get a
        list of host IDs.

        Keyword arguments:
        ids -- AID(s) of the hosts to retrieve state information. String or list of strings.
        parameters - full parameters payload, not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/GetOnlineState.V1
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetOnlineState_V1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_hidden_devices(self: object, parameters: dict = None, **kwargs) -> dict:
        """Retrieve hidden hosts that match the provided filter criteria.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
        limit -- The maximum number of records to return. [integer, 1-5000]
        offset -- The integer offset to start retrieving records from.
        parameters - full parameters payload, not required if using other keywords.
        sort -- The property to sort by. FQL syntax (e.g. status.desc or hostname.asc).
                Available sort fields
                device_id               machine_domain
                agent_load_flags        major_version
                agent_version           minor_version
                bios_manufacturer       modified_timestamp
                bios_version            os_version
                config_id_base          ou
                config_id_build         platform_id
                config_id_platform      platform_name
                cpu_signature           product_type_desc
                external_ip             reduced_functionality_mode
                first_seen              release_group
                hostname                serial_number
                last_login_timestamp    site_name
                last_seen               status
                local_ip                system_manufacturer
                local_ip.raw            system_product_name
                mac_address

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryHiddenDevices
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryHiddenDevices",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_devices_by_filter_scroll(self: object, parameters: dict = None, **kwargs) -> dict:
        """Search for hosts in your environment by platform, hostname, IP, and other criteria.

        Provides continuous pagination capability (based on offset pointer which expires after
        2 minutes with no maximum limit)

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
        limit -- The maximum number of records to return. [integer, 1-5000]
        offset -- The string offset to page from, for the next result set.
        parameters - full parameters payload, not required if using other keywords.
        sort -- The property to sort by. FQL syntax (e.g. status.desc or hostname.asc).
                Available sort fields
                device_id               machine_domain
                agent_load_flags        major_version
                agent_version           minor_version
                bios_manufacturer       modified_timestamp
                bios_version            os_version
                config_id_base          ou
                config_id_build         platform_id
                config_id_platform      platform_name
                cpu_signature           product_type_desc
                external_ip             reduced_functionality_mode
                first_seen              release_group
                hostname                serial_number
                last_login_timestamp    site_name
                last_seen               status
                local_ip                system_manufacturer
                local_ip.raw            system_product_name
                mac_address

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryDevicesByFilterScroll
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryDevicesByFilterScroll",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_devices_by_filter(self: object, parameters: dict = None, **kwargs) -> dict:
        """Search for hosts in your environment by platform, hostname, IP, and other criteria.

        Keyword arguments:
        filter -- The filter expression that should be used to limit the results. FQL syntax.
        limit -- The maximum number of records to return. [integer, 1-5000]
        offset -- The integer offset to start retrieving records from.
        parameters - full parameters payload, not required if using other keywords.
        sort -- The property to sort by. FQL syntax (e.g. status.desc or hostname.asc).
                Available sort fields
                device_id               machine_domain
                agent_load_flags        major_version
                agent_version           minor_version
                bios_manufacturer       modified_timestamp
                bios_version            os_version
                config_id_base          ou
                config_id_build         platform_id
                config_id_platform      platform_name
                cpu_signature           product_type_desc
                external_ip             reduced_functionality_mode
                first_seen              release_group
                hostname                serial_number
                last_login_timestamp    site_name
                last_seen               status
                local_ip                system_manufacturer
                local_ip.raw            system_product_name
                mac_address

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryDevicesByFilter
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryDevicesByFilter",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def query_device_login_history(self: object, *args, body: dict = None, **kwargs) -> dict:
        """Retrieve details about recent login sessions for a set of devices.

        Keyword arguments:
        body -- full body payload, not required when ids keyword is provided.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids -- AID(s) of the hosts to retrieve. String or list of strings.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryDeviceLoginHistory
        """
        if not body:
            body = generic_payload_list(submitted_arguments=args,
                                        submitted_keywords=kwargs,
                                        payload_value="ids"
                                        )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryDeviceLoginHistory",
            body=body,
            body_validator={"ids": list} if self.validate_payloads else None,
            body_required=["ids"] if self.validate_payloads else None
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def query_network_address_history(self: object, *args, body: dict = None, **kwargs) -> dict:
        """Retrieve history of IP and MAC addresses of devices.

        Keyword arguments:
        body -- full body payload, not required when ids keyword is provided.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids -- AID(s) of the hosts to retrieve. String or list of strings.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryGetNetworkAddressHistoryV1
        """
        if not body:
            body = generic_payload_list(submitted_arguments=args,
                                        submitted_keywords=kwargs,
                                        payload_value="ids"
                                        )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryGetNetworkAddressHistoryV1",
            body=body,
            body_validator={"ids": list} if self.validate_payloads else None,
            body_required=["ids"] if self.validate_payloads else None
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    PerformActionV2 = perform_action
    entities_perform_action = perform_group_action
    PerformGroupAction = perform_group_action
    UpdateDeviceTags = update_device_tags
    GetDeviceDetails = get_device_details  # v1.2 - Now redirects to PostDeviceDetailsV2
    GetDeviceDetailsV1 = get_device_details_v1
    GetDeviceDetailsV2 = get_device_details_v2
    PostDeviceDetailsV2 = get_device_details
    post_device_details_v2 = get_device_details
    QueryHiddenDevices = query_hidden_devices
    GetOnlineState_V1 = get_online_state
    get_online_state_v1 = get_online_state  # Issue 739  Helper alias
    QueryDevicesByFilterScroll = query_devices_by_filter_scroll
    QueryDevicesByFilter = query_devices_by_filter
    QueryDevices = query_devices_by_filter_scroll
    query_devices = query_devices_by_filter_scroll
    QueryDeviceLoginHistory = query_device_login_history
    QueryGetNetworkAddressHistoryV1 = query_network_address_history
