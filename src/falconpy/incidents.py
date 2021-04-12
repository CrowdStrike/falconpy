"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

incidents - CrowdStrike Falcon Incidents API interface class

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
from ._util import service_request
from ._service_class import ServiceClass


class Incidents(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def CrowdScore(self: object, parameters: dict = None) -> dict:
        """ Query environment wide CrowdScore and return the entity data. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/CrowdScore
        FULL_URL = self.base_url+'/incidents/combined/crowdscores/v1'
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

    def GetBehaviors(self: object, body: dict) -> dict:
        """ Get details on behaviors by providing behavior IDs. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/GetBehaviors
        FULL_URL = self.base_url+'/incidents/entities/behaviors/GET/v1'
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

    def PerformIncidentAction(self: object, body: dict) -> dict:
        """ Perform a set of actions on one or more incidents, such as
            adding tags or comments or updating the incident name or description.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/PerformIncidentAction
        FULL_URL = self.base_url+'/incidents/entities/incident-actions/v1'
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

    def GetIncidents(self: object, body: dict) -> dict:
        """ Get details on incidents by providing incident IDs. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/GetIncidents
        FULL_URL = self.base_url+'/incidents/entities/incidents/GET/v1'
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

    def QueryBehaviors(self: object, parameters: dict = None) -> dict:
        """ Search for behaviors by providing an FQL filter, sorting, and paging details. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/QueryBehaviors
        FULL_URL = self.base_url+'/incidents/queries/behaviors/v1'
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

    def QueryIncidents(self: object, parameters: dict = None) -> dict:
        """ Search for incidents by providing an FQL filter, sorting, and paging details. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/QueryIncidents
        FULL_URL = self.base_url+'/incidents/queries/incidents/v1'
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
