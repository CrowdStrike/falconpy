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
# pylint: disable=C0103  # Aligning method names to API operation IDs
from ._util import service_request, force_default, args_to_params
from ._service_class import ServiceClass
from ._endpoint._sample_uploads import _sample_uploads_endpoints as Endpoints


class Sample_Uploads(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetSampleV3(self: object, parameters: dict = None, **kwargs) -> object:
        """
        Retrieves the file associated with the given ID (SHA256)
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sample-uploads/GetSampleV3
        operation_id = "GetSampleV3"
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

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def UploadSampleV3(self: object,
                       file_data: object,
                       body: dict = None,
                       parameters: dict = None,
                       **kwargs) -> dict:
        """
        Upload a file for further cloud analysis. After uploading, call the specific analysis API endpoint.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sample-uploads/UploadSampleV3
        operation_id = "UploadSampleV3"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        header_payload["Content-Type"] = "application/octet-stream"
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        body_payload = body
        data_payload = file_data
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   body=body_payload,
                                   data=data_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def DeleteSampleV3(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Removes a sample, including file, meta and submissions from the collection.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sample-uploads/DeleteSampleV3
        operation_id = "DeleteSampleV3"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned
