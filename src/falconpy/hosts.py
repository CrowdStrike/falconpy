"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

hosts - CrowdStrike Falcon Hosts API interface class

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
# pylint: disable=C0103  # Aligning method names to API operation IDs
from ._util import generate_error_result, force_default, args_to_params, process_service_request, handle_single_argument
from ._service_class import ServiceClass
from ._endpoint._hosts import _hosts_endpoints as Endpoints


class Hosts(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, an
    authorization object (oauth2.py) or a credential dictionary with
    client_id and client_secret containing valid API credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def perform_action(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Take various actions on the hosts in your environment.
        Contain or lift containment on a host. Delete or restore a host.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/PerformActionV2
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
                params=parameters
                )
        else:
            returned = generate_error_result("Invalid value specified for action_name parameter.")

        return returned

    def update_device_tags(self: object, action_name: str, ids: list or str, tags: list or str) -> dict:
        """
        Allows for tagging hosts. If the tags are empty
        """
        _allowed_actions = ["add", "remove"]
        # validate action is allowed AND tags is "something"
        if action_name.lower() in _allowed_actions and tags is not None:
            # convert ids/tags to be a list object if not already
            if isinstance(ids, str):
                ids = ids.split(",")
            if isinstance(tags, str):
                tags = tags.split(",")
            # tags must start with FalconGroupingTags, users probably won't know this so add it for them
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
    def get_device_details(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get details on one or more hosts by providing agent IDs (AID).
        You can get a host's agent IDs (AIDs) from the /devices/queries/devices/v1 endpoint,
        the Falcon console or the Streaming API.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/GetDeviceDetails
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetDeviceDetails",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_hidden_devices(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Perform the specified action on the Prevention Policies specified in the request.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryHiddenDevices
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryHiddenDevices",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_devices_by_filter_scroll(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Perform the specified action on the Prevention Policies specified in the request.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryDevicesByFilterScroll
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryDevicesByFilterScroll",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_devices_by_filter(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for hosts in your environment by platform, hostname, IP, and other criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryDevicesByFilter
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryDevicesByFilter",
            keywords=kwargs,
            params=parameters
            )
    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    PerformActionV2 = perform_action
    UpdateDeviceTags = update_device_tags
    GetDeviceDetails = get_device_details
    QueryHiddenDevices = query_hidden_devices
    QueryDevicesByFilterScroll = query_devices_by_filter_scroll
    QueryDevicesByFilter = query_devices_by_filter
