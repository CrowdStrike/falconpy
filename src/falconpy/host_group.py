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
from ._util import parse_id_list, service_request, generate_error_result
from ._service_class import ServiceClass


class Host_Group(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def queryCombinedGroupMembers(self: object, parameters: dict = None) -> dict:
        """ Search for members of a Host Group in your environment by providing an FQL filter
            and paging details. Returns a set of host details which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/queryCombinedGroupMembers
        FULL_URL = self.base_url+'/devices/combined/host-group-members/v1'
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

    def queryCombinedHostGroups(self: object, parameters: dict = None) -> dict:
        """ Search for Host Groups in your environment by providing an FQL filter and
            paging details. Returns a set of Host Groups which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/queryCombinedHostGroups
        FULL_URL = self.base_url+'/devices/combined/host-groups/v1'
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

    def performGroupAction(self: object, parameters: dict, body: dict, action_name: str = None) -> dict:
        """ Perform the specified action on the Host Groups specified in the request. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/performGroupAction
        if "action_name" in parameters:
            action_name = parameters["action_name"].lower()
        ALLOWED_ACTIONS = ['add-hosts', 'remove-hosts']
        if action_name.lower() in ALLOWED_ACTIONS:
            FULL_URL = self.base_url+'/devices/entities/host-group-actions/v1'
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

    def getHostGroups(self: object, ids) -> dict:
        """ Retrieve a set of Host Groups by specifying their IDs. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/getHostGroups
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/devices/entities/host-groups/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def createHostGroups(self: object, body: dict) -> dict:
        """ Create Host Groups by specifying details about the group to create. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/createHostGroups
        FULL_URL = self.base_url+'/devices/entities/host-groups/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def deleteHostGroups(self: object, ids) -> dict:
        """ Delete a set of Host Groups by specifying their IDs. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/deleteHostGroups
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/devices/entities/host-groups/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def updateHostGroups(self: object, body: dict) -> dict:
        """ Update Host Groups by specifying the ID of the group and details to update. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/updateHostGroups
        FULL_URL = self.base_url+'/devices/entities/host-groups/v1'
        HEADERS = self.headers
        BODY = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def queryGroupMembers(self: object, parameters: dict = None) -> dict:
        """ Search for members of a Host Group in your environment by providing an FQL filter
            and paging details. Returns a set of Agent IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/queryGroupMembers
        FULL_URL = self.base_url+'/devices/queries/host-group-members/v1'
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

    def queryHostGroups(self: object, parameters: dict = None) -> dict:
        """ Search for Host Groups in your environment by providing an FQL filter and
            paging details. Returns a set of Host Group IDs which match the filter criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/host-group/queryHostGroups
        FULL_URL = self.base_url+'/devices/queries/host-groups/v1'
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
