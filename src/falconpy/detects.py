"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

detects - CrowdStrike Falcon Detections API interface class

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


class Detects(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def GetAggregateDetects(self: object, body: dict) -> dict:
        """ Get detect aggregates as specified via json in request body. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects/GetAggregateDetects
        FULL_URL = self.base_url+'/detects/aggregates/detects/GET/v1'
        HEADERS = self.headers
        BODY = body
        # VALIDATOR = {"resources": list}  # TODO: Confirm body payload format
        # REQUIRED = ["resources"]
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   body=BODY,
                                   # body_validator=VALIDATOR,
                                   # body_required=REQUIRED,
                                   verify=self.ssl_verify
                                   )
        return returned

    def UpdateDetectsByIdsV2(self: object, body: dict) -> dict:
        """ Modify the state, assignee, and visibility of detections. """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects/UpdateDetectsByIdsV2
        FULL_URL = self.base_url+'/detects/entities/detects/v2'
        HEADERS = self.headers
        BODY = body
        VALIDATOR = {
            "assigned_to_uuid": str,
            "ids": list,
            "show_in_ui": bool,
            "status": str,
            "comment": str
        }
        REQUIRED = ["ids"]
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   body=BODY,
                                   body_validator=VALIDATOR,
                                   body_required=REQUIRED,
                                   verify=self.ssl_verify
                                   )
        return returned

    def GetDetectSummaries(self: object, body: dict) -> dict:
        """ View information about detections. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects/GetDetectSummaries
        FULL_URL = self.base_url+'/detects/entities/summaries/GET/v1'
        HEADERS = self.headers
        BODY = body
        VALIDATOR = {"ids": list}   # TODO: Confirm list datatype for ingested IDs via the body payload
        REQUIRED = ["ids"]
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   body=BODY,
                                   body_validator=VALIDATOR,
                                   body_required=REQUIRED,
                                   verify=self.ssl_verify
                                   )
        return returned

    def QueryDetects(self: object, parameters: dict = None) -> dict:
        """ Search for detection IDs that match a given query. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/detects/QueryDetects
        FULL_URL = self.base_url+'/detects/queries/detects/v1'
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        VALIDATOR = {
            "limit": int,
            "offset": int,
            "sort": str,
            "filter": str,
            "q": str
        }
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   params_validator=VALIDATOR,
                                   verify=self.ssl_verify
                                   )
        return returned
