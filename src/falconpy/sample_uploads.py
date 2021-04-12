"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

sample_uploads - CrowdStrike Falcon Sample Upload API interface class

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


class Sample_Uploads(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def GetSampleV3(self: object, ids: list or str, parameters: dict = None) -> object:
        """ Retrieves the file associated with the given ID (SHA256)"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sample-uploads/GetSampleV3
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/samples/entities/samples/v3?ids={}'.format(ID_LIST)
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

    def UploadSampleV3(self: object,
                       file_data: object,
                       body: dict = None,
                       file_name: str = "",
                       parameters: dict = None) -> dict:
        """ Upload a file for further cloud analysis. After uploading, call the specific analysis API endpoint. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sample-uploads/UploadSampleV3
        FULL_URL = self.base_url+f"/samples/entities/samples/v3?file_name={str(file_name)}"
        HEADERS = self.headers
        HEADERS["Content-Type"] = "application/octet-stream"
        if parameters is None:
            parameters = {}
        PARAMS = parameters
        DATA = file_data
        if body is None:
            body = {}
        BODY = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=FULL_URL,
                                   body=BODY,
                                   data=DATA,
                                   params=PARAMS,
                                   headers=HEADERS,
                                   verify=self.ssl_verify
                                   )
        return returned

    def DeleteSampleV3(self: object, ids: str or list) -> dict:
        """ Removes a sample, including file, meta and submissions from the collection. """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sample-uploads/DeleteSampleV3
        ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
        FULL_URL = self.base_url+'/samples/entities/samples/v3?ids={}'.format(ID_LIST)
        HEADERS = self.headers
        returned = service_request(caller=self, method="DELETE", endpoint=FULL_URL, headers=HEADERS, verify=self.ssl_verify)

        return returned
