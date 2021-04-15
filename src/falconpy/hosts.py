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
from ._util import service_request, parse_id_list, generate_error_result
from ._service_class import ServiceClass


class Hosts(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def PerformActionV2(self: object, parameters: dict, body: dict, action_name: str = None) -> dict:
        """ Take various actions on the hosts in your environment.
            Contain or lift containment on a host. Delete or restore a host.
        """
        if "action_name" in parameters:
            action_name = parameters["action_name"].lower()
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/PerformActionV2
        ALLOWED_ACTIONS = ['contain', 'lift_containment', 'hide_host', 'unhide_host']
        if action_name.lower() in ALLOWED_ACTIONS:
            FULL_URL = self.base_url+'/devices/entities/devices-actions/v2'
            HEADERS = self.headers
            PARAMS = parameters
            BODY = body
            returned = service_request(caller=self,
                                       method="POST",
                                       endpoint=FULL_URL,
                                       params=PARAMS,
                                       body=BODY,
                                       headers=HEADERS,
                                       verify=self.ssl_verify
                                       )
        else:
            returned = generate_error_result("Invalid value specified for action_name parameter.")

        return returned

    def UpdateDeviceTags(self: object, action_name: str, ids: list or str, tags: list or str) -> dict:
        """
        allows for tagging hosts. If the tags are empty
        """
        ALLOWED_ACTIONS = ["add", "remove"]
        # validate action is allowed AND tags is "something"
        if action_name.lower() in ALLOWED_ACTIONS and tags is not None:
            FULL_URL = self.base_url + '/devices/entities/devices/tags/v1'
            HEADERS = self.headers
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
            BODY = {
                "action": action_name,
                "device_ids": ids,
                "tags": patch_tag
            }
            returned = service_request(caller=self,
                                       method="PATCH",
                                       endpoint=FULL_URL,
                                       body=BODY,
                                       headers=HEADERS,
                                       verify=self.ssl_verify
                                       )
        else:
            returned = generate_error_result("Invalid value specified for action_name parameter.")
        return returned

    def GetDeviceDetails(self: object, ids) -> dict:
        """ Get details on one or more hosts by providing agent IDs (AID).
            You can get a host's agent IDs (AIDs) from the /devices/queries/devices/v1 endpoint,
            the Falcon console or the Streaming API.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/GetDeviceDetails
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/devices/entities/devices/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def QueryHiddenDevices(self: object, parameters: dict = None) -> dict:
        """ Perform the specified action on the Prevention Policies specified in the request. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryHiddenDevices
        FULL_URL = self.base_url+'/devices/queries/devices-hidden/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def QueryDevicesByFilterScroll(self: object, parameters: dict = None) -> dict:
        """ Perform the specified action on the Prevention Policies specified in the request. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryDevicesByFilterScroll
        FULL_URL = self.base_url+'/devices/queries/devices-scroll/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def QueryDevicesByFilter(self: object, parameters: dict = None) -> dict:
        """ Search for hosts in your environment by platform, hostname, IP, and other criteria. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/hosts/QueryDevicesByFilter
        FULL_URL = self.base_url+'/devices/queries/devices/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned
