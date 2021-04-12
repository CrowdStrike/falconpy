"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

quick_scan - Falcon Quick Scan API Interface Class

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
from ._util import service_request, parse_id_list
from ._service_class import ServiceClass


class Quick_Scan(ServiceClass):
    """The only requirement to instantiate an instance of this class
       is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def GetScansAggregates(self: object, body: dict) -> dict:
        """Get scans aggregations as specified via json in request body."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan/GetScansAggregates
        FULL_URL = self.base_url+"/scanner/aggregates/scans/GET/v1"
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

    def GetScans(self: object, ids) -> dict:
        """Check the status of a volume scan. Time required for analysis increases with the number
           of samples in a volume but usually it should take less than 1 minute
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan/GetScans
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+"/scanner/entities/scans/v1?ids={}".format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def ScanSamples(self: object, body: dict) -> dict:
        """Get scans aggregations as specified via json in request body."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan/ScanSamples
        FULL_URL = self.base_url+"/scanner/entities/scans/v1"
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

    def QuerySubmissionsMixin0(self: object, parameters: dict = None) -> dict:
        """Find IDs for submitted scans by providing an FQL filter and paging details.
           Returns a set of volume IDs that match your criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan/QuerySubmissionsMixin0
        FULL_URL = self.base_url+"/scanner/queries/scans/v1"
        HEADERS = self.headers
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   params=PARAMS,
                                   verify=self.ssl_verify
                                   )
        return returned
