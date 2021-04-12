"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

iocs - CrowdStrike Falcon Indicators of Compromise API interface class

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
from ._util import parse_id_list, service_request
from ._service_class import ServiceClass


class Iocs(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def DevicesCount(self: object, parameters: dict) -> dict:
        """ Number of hosts in your customer account that have observed a given custom IOC. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/DevicesCount
        FULL_URL = self.base_url+'/indicators/aggregates/devices-count/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def GetIOC(self: object, parameters: dict) -> dict:
        """ Get an IOC by providing a type and value. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/GetIOC
        FULL_URL = self.base_url+'/indicators/entities/iocs/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def CreateIOC(self: object, body: dict) -> dict:
        """ Create a new IOC. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/CreateIOC
        FULL_URL = self.base_url+'/indicators/entities/iocs/v1'
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

    def DeleteIOC(self: object, parameters: dict) -> dict:
        """ Delete an IOC by providing a type and value. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/DeleteIOC
        FULL_URL = self.base_url+'/indicators/entities/iocs/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def UpdateIOC(self: object, parameters: dict, body: dict) -> dict:
        """ Update an IOC by providing a type and value. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/UpdateIOC
        FULL_URL = self.base_url+'/indicators/entities/iocs/v1'
        HEADERS = self.headers
        PARAMS = parameters
        BODY = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   body=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def DevicesRanOn(self: object, parameters: dict) -> dict:
        """ Find hosts that have observed a given custom IOC.
            For details about those hosts, use the hosts API interface.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/DevicesRanOn
        FULL_URL = self.base_url+'/indicators/queries/devices/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def QueryIOCs(self: object, parameters: dict = None) -> dict:
        """ Search the custom IOCs in your customer account. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/QueryIOCs
        FULL_URL = self.base_url+'/indicators/queries/iocs/v1'
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

    def ProcessesRanOn(self: object, parameters: dict) -> dict:
        """ Search for processes associated with a custom IOC. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/QueryIOCs
        FULL_URL = self.base_url+'/indicators/queries/processes/v1'
        HEADERS = self.headers
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def entities_processes(self: object, ids) -> dict:
        """ For the provided ProcessID retrieve the process details. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/iocs/entities_processes
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/processes/entities/processes/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned
