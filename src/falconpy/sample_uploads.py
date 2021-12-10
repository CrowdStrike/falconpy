"""CrowdStrike Falcon Sample Upload API interface class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

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
from ._util import force_default, process_service_request, handle_single_argument
from ._service_class import ServiceClass
from ._endpoint._sample_uploads import _sample_uploads_endpoints as Endpoints


class SampleUploads(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (OAuth2.token())
    """

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_sample(self: object, *args, parameters: dict = None, **kwargs) -> object:
        """Retrieve the file associated with the given ID (SHA256).

        Keyword arguments:
        ids -- List of SHA256s to retrieve. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.
        password_protected -- Flag whether the sample should be zipped and password protected
                              with the pass of 'infected'. Defaults to False.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sample-uploads/GetSampleV3
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSampleV3",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def upload_sample(self: object,
                      file_data: object = None,
                      body: dict = None,
                      parameters: dict = None,
                      **kwargs
                      ) -> dict:
        """Upload a file for further cloud analysis.

        After uploading, call the specific analysis API endpoint.

        Keyword arguments:
        comment -- A descriptive comment to identify the file for other users. String.
        file_data -- Content of the uploaded sample in binary format. Max file size is 256 MB.
                     'sample' and 'upfile' are also accepted as this parameter.

                     Accepted File Formats:
                     Portable executables: .exe, .scr, .pif, .dll, .com, .cpl, etc.
                     Office documents: .doc, .docx, .ppt, .pps, .pptx, .ppsx, .xls,
                                       .xlsx, .rtf, .pub
                     PDF
                     APK
                     Executable JAR
                     Windows script component: .sct
                     Windows shortcut: .lnk
                     Windows help: .chm
                     HTML application: .hta
                     Windows script file: .wsf
                     Javascript: .js
                     Visual Basic: .vbs, .vbe
                     Shockwave Flash: .swf
                     Perl: .pl
                     Powershell: .ps1, .psd1, .psm1
                     Scalable vector graphics: .svg
                     Python: .py
                     Linux ELF executables
                     Email files: MIME RFC 822 .eml, Outlook .msg
        file_name -- Name of the file. String.
        is_confidential -- Defines the visibility of this file in Falcon MalQuery, either
                           via the  API or the Falcon console.
                           True = File is only shown to users within your customer account.
                           False = File can be seen by other CrowdStrike customers.
                           Defaults to True.
        parameters -- full parameters payload, not required if using other keywords.


        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sample-uploads/UploadSampleV3
        """
        # Try to find the binary object they provided us
        if not file_data:
            file_data = kwargs.get("sample", None)
            if not file_data:
                file_data = kwargs.get("upfile", None)
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
    def delete_sample(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Remove a sample, including file, meta and submissions from the collection.

        Keyword arguments:
        ids -- List of SHA256s to delete. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sample-uploads/DeleteSampleV3
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteSampleV3",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
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
