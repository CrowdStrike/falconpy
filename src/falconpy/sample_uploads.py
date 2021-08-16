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
import json
from ._util import force_default, process_service_request
from ._service_class import ServiceClass
from ._endpoint._sample_uploads import _sample_uploads_endpoints as Endpoints


class SampleUploads(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, an
    authorization object (oauth2.py) or a credential dictionary with
    client_id and client_secret containing valid API credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_sample(self: object, parameters: dict = None, **kwargs) -> object:
        """
        Retrieves the file associated with the given ID (SHA256)
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSampleV3",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def upload_sample(self: object,
                      file_data: object,
                      body: dict = None,
                      parameters: dict = None,
                      **kwargs) -> dict:
        """
        Upload a file for further cloud analysis. After uploading, call the specific analysis API endpoint.
        """
        # Create a copy of our default header dictionary
        header_payload = json.loads(json.dumps(self.headers))
        # Set our content-type header
        header_payload["Content-Type"] = "application/octet-stream"
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UploadSampleV3",
            headers=header_payload,  # Pass our custom headers
            body=body,
            data=file_data,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_sample(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Removes a sample, including file, meta and submissions from the collection.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteSampleV3",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetSampleV3 = get_sample
    UploadSampleV3 = upload_sample
    DeleteSampleV3 = delete_sample


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Sample_Uploads = SampleUploads  # pylint: disable=C0103
