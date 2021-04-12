"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

host_groups - CrowdStrike Falcon Threat Intelligence API interface class

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


class Intel(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def QueryIntelActorEntities(self: object, parameters: dict = None) -> dict:
        """ Get info about actors that match provided FQL filters. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelActorEntities
        FULL_URL = self.base_url+'/intel/combined/actors/v1'
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

    def QueryIntelIndicatorEntities(self: object, parameters: dict = None) -> dict:
        """ Get info about indicators that match provided FQL filters. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelIndicatorEntities
        FULL_URL = self.base_url+'/intel/combined/indicators/v1'
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

    def QueryIntelReportEntities(self: object, parameters: dict = None) -> dict:
        """ Get info about reports that match provided FQL filters. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportEntities
        FULL_URL = self.base_url+'/intel/combined/reports/v1'
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

    def GetIntelActorEntities(self: object, ids, parameters: dict = None) -> dict:
        """ Retrieve specific actors using their actor IDs. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelActorEntities
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/intel/entities/actors/v1?ids={}'.format(ID_LIST)
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

    def GetIntelIndicatorEntities(self: object, body: dict) -> dict:
        """ Retrieve specific indicators using their indicator IDs. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelIndicatorEntities
        FULL_URL = self.base_url+'/intel/entities/indicators/GET/v1'
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

    def GetIntelReportPDF(self: object, parameters: dict) -> dict:
        """ Return a Report PDF attachment. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelReportPDF
        FULL_URL = self.base_url+'/intel/entities/report-files/v1'
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

    def GetIntelReportEntities(self: object, ids, parameters: dict = None) -> dict:
        """ Retrieve specific reports using their report IDs. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelReportEntities
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/intel/entities/reports/v1?ids={}'.format(ID_LIST)
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

    def GetIntelRuleFile(self: object, parameters: dict) -> dict:
        # There is an optional header you can see Accept to choose the result format. See Swagger.
        """ Download earlier rule sets. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelRuleFile
        FULL_URL = self.base_url+'/intel/entities/rules-files/v1'
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

    def GetLatestIntelRuleFile(self: object, parameters: dict) -> dict:
        # There is an optional header you can see Accept to choose the result format. See Swagger.
        """ Download the latest rule set. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetLatestIntelRuleFile
        FULL_URL = self.base_url+'/intel/entities/rules-latest-files/v1'
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

    def GetIntelRuleEntities(self: object, ids) -> dict:
        """ Retrieve details for rule sets for the specified ids. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/GetIntelRuleEntities
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/intel/entities/rules/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def QueryIntelActorIds(self: object, parameters: dict = None) -> dict:
        """ Get actor IDs that match provided FQL filters. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelActorIds
        FULL_URL = self.base_url+'/intel/queries/actors/v1'
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

    def QueryIntelIndicatorIds(self: object, parameters: dict = None) -> dict:
        """ Get indicators IDs that match provided FQL filters. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelIndicatorIds
        FULL_URL = self.base_url+'/intel/queries/indicators/v1'
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

    def QueryIntelReportIds(self: object, parameters: dict = None) -> dict:
        """ Get report IDs that match provided FQL filters. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportIds
        FULL_URL = self.base_url+'/intel/queries/reports/v1'
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

    def QueryIntelRuleIds(self: object, parameters: dict) -> dict:
        """ Search for rule IDs that match provided filter criteria. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intel/QueryIntelReportIds
        FULL_URL = self.base_url+'/intel/queries/rules/v1'
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
