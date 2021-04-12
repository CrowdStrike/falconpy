"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

incidents - CrowdStrike Falcon X Sanbox API interface class

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


class FalconX_Sandbox(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def GetArtifacts(self: object, parameters: dict) -> object:
        """ Download IOC packs, PCAP files, and other analysis artifacts. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetArtifacts
        FULL_URL = self.base_url+'/falconx/entities/artifacts/v1'
        HEADERS = self.headers
        HEADERS['Accept-Encoding'] = 'gzip'  # Force gzip compression
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def GetSummaryReports(self: object, ids) -> dict:
        """ Get a short summary version of a sandbox report. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetSummaryReports
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/falconx/entities/report-summaries/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def GetSubmissions(self: object, ids) -> dict:
        """ Check the status of a sandbox analysis. Time required for analysis varies but is usually less than 15 minutes. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetSubmissions
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/falconx/entities/submissions/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def Submit(self: object, body: dict) -> dict:
        """ Submit an uploaded file or a URL for sandbox analysis.
            Time required for analysis varies but is usually less than 15 minutes.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/Submit
        FULL_URL = self.base_url+'/falconx/entities/submissions/v1'
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

    def QueryReports(self: object, parameters: dict = None) -> dict:
        """ Find sandbox reports by providing an FQL filter and paging details.
            Returns a set of report IDs that match your criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/QueryReports
        FULL_URL = self.base_url+'/falconx/queries/reports/v1'
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

    def QuerySubmissions(self: object, parameters: dict = None) -> dict:
        """ Find submission IDs for uploaded files by providing an FQL filter and paging details.
            Returns a set of submission IDs that match your criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/QuerySubmissions
        FULL_URL = self.base_url+'/falconx/queries/submissions/v1'
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

    def UploadSampleV2(self: object, parameters: dict, body: dict) -> dict:
        """ Upload a file for sandbox analysis. After uploading,
            use `/falconx/entities/submissions/v1` to start analyzing the file.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/UploadSampleV2
        FULL_URL = self.base_url+'/samples/entities/samples/v2'
        HEADERS = self.headers
        HEADERS['Content-Type'] = 'application/octet-stream'
        BODY = body     # TODO: Confirm this is a data element and update calling code to reflect the correct reference
        PARAMS = parameters
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   params=PARAMS,
                                   data=BODY,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def GetReports(self: object, ids) -> object:
        """ Retrieves a full sandbox report. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetReports
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/falconx/entities/reports/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def DeleteReport(self: object, ids) -> dict:
        """ Delete report based on the report ID. Operation can be checked for success
            by polling for the report ID on the report-summaries endpoint.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/DeleteReport
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/falconx/entities/reports/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def GetSampleV2(self: object, ids, password_protect: bool = False) -> object:
        """ Retrieves the file associated with the given ID (SHA256). """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetSampleV2
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/samples/entities/samples/v2?ids={}&password_protected={}'.format(
            ID_LIST,
            str(password_protect)
        )
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def DeleteSampleV2(self: object, ids) -> dict:
        """ Removes a sample, including file, meta and submissions from the collection. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/DeleteSampleV2
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/samples/entities/samples/v2?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def QuerySampleV1(self: object, ids) -> dict:
        """ Retrieves a list with sha256 of samples that exist and customer has rights to access them,
            maximum number of accepted items is 200.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/DeleteSampleV2
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/samples/queries/samples/GET/v1?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned
