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
from ._util import service_request, generate_error_result, force_default, args_to_params
from ._service_class import ServiceClass
from ._endpoint._hosts import _hosts_endpoints as Endpoints


class Hosts(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def PerformActionV2(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:
        """
        Take various actions on the hosts in your environment.
        Contain or lift containment on a host. Delete or restore a host.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/PerformActionV2
        _allowed_actions = ['contain', 'lift_containment', 'hide_host', 'unhide_host']
        operation_id = "PerformActionV2"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        if "action_name" not in parameter_payload:
            parameter_payload["action_name"] = "Not Specified"
        # Only process allowed actions
        if parameter_payload["action_name"].lower() in _allowed_actions:
            returned = service_request(caller=self,
                                       method="POST",
                                       endpoint=target_url,
                                       body=body_payload,
                                       params=parameter_payload,
                                       headers=header_payload,
                                       verify=self.ssl_verify
                                       )
        else:
            returned = generate_error_result("Invalid value specified for action_name parameter.")

        return returned

    def UpdateDeviceTags(self: object, action_name: str, ids: list or str, tags: list or str) -> dict:
        """
        Allows for tagging hosts. If the tags are empty
        """
        _allowed_actions = ["add", "remove"]
        # validate action is allowed AND tags is "something"
        if action_name.lower() in _allowed_actions and tags is not None:
            operation_id = "UpdateDeviceTags"
            target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
            header_payload = self.headers
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
            returned = service_request(caller=self,
                                       method="PATCH",
                                       endpoint=target_url,
                                       body=body_payload,
                                       headers=header_payload,
                                       verify=self.ssl_verify
                                       )
        else:
            returned = generate_error_result("Invalid value specified for action_name parameter.")
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetDeviceDetails(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get details on one or more hosts by providing agent IDs (AID).
        You can get a host's agent IDs (AIDs) from the /devices/queries/devices/v1 endpoint,
        the Falcon console or the Streaming API.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/GetDeviceDetails
        operation_id = "GetDeviceDetails"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryHiddenDevices(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Perform the specified action on the Prevention Policies specified in the request.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryHiddenDevices
        operation_id = "QueryHiddenDevices"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryDevicesByFilterScroll(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Perform the specified action on the Prevention Policies specified in the request.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryDevicesByFilterScroll
        operation_id = "QueryDevicesByFilterScroll"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryDevicesByFilter(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Search for hosts in your environment by platform, hostname, IP, and other criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryDevicesByFilter
        operation_id = "QueryDevicesByFilter"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned
