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
import json
from ._util import force_default, process_service_request
from ._service_class import ServiceClass
from ._endpoint._falconx_sandbox import _falconx_sandbox_endpoints as Endpoints


class FalconXSandbox(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, an
    authorization object (oauth2.py) or a credential dictionary with
    client_id and client_secret containing valid API credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_artifacts(self: object, parameters: dict = None, **kwargs) -> object:
        """
        Download IOC packs, PCAP files, and other analysis artifacts.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetArtifacts
        # Create a copy of our default header dictionary
        header_payload = json.loads(json.dumps(self.headers))
        # Set our content-type header
        header_payload['Accept-Encoding'] = 'gzip'  # Force gzip compression
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetArtifacts",
            keywords=kwargs,
            params=parameters,
            headers=header_payload
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_summary_reports(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Get a short summary version of a sandbox report.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetSummaryReports
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSummaryReports",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_submissions(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Check the status of a sandbox analysis. Time required for analysis varies but is usually less than 15 minutes.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetSubmissions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSubmissions",
            keywords=kwargs,
            params=parameters
            )

    def submit(self: object, body: dict) -> dict:
        """
        Submit an uploaded file or a URL for sandbox analysis.
        Time required for analysis varies but is usually less than 15 minutes.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/Submit
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="Submit",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_reports(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Find sandbox reports by providing an FQL filter and paging details.
        Returns a set of report IDs that match your criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/QueryReports
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryReports",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_submissions(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Find submission IDs for uploaded files by providing an FQL filter and paging details.
        Returns a set of submission IDs that match your criteria.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/QuerySubmissions
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QuerySubmissions",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def upload_sample(self: object, file_data: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
        """
        Upload a file for sandbox analysis. After uploading,
        use `/falconx/entities/submissions/v1` to start analyzing the file.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/UploadSampleV2
        # Create a copy of our default header dictionary
        header_payload = json.loads(json.dumps(self.headers))
        # Set our content-type header
        header_payload["Content-Type"] = "application/octet-stream"
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UploadSampleV2",
            body=body,
            data=file_data,
            params=parameters,
            keywords=kwargs,
            headers=header_payload
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_reports(self: object, parameters: dict = None, **kwargs) -> object:
        """
        Retrieves a full sandbox report.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetReports
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetReports",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_report(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete report based on the report ID. Operation can be checked for success
        by polling for the report ID on the report-summaries endpoint.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/DeleteReport
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteReport",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_sample(self: object, parameters: dict = None, **kwargs) -> object:
        """
        Retrieves the file associated with the given ID (SHA256).
        Use the password_protected boolean to specify if you want your zip to have a password.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetSampleV2
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSampleV2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_sample(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Removes a sample, including file, meta and submissions from the collection.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/DeleteSampleV2
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteSampleV2",
            keywords=kwargs,
            params=parameters
            )

    def query_sample(self: object, body: dict) -> dict:
        """
        Retrieves a list with sha256 of samples that exist and customer has rights to access them,
        maximum number of accepted items is 200.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/QuerySampleV1
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QuerySampleV1",
            body=body
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetArtifacts = get_artifacts
    GetSummaryReports = get_summary_reports
    GetSubmissions = get_submissions
    Submit = submit
    QueryReports = query_reports
    QuerySubmissions = query_submissions
    UploadSampleV2 = upload_sample
    GetReports = get_reports
    DeleteReport = delete_report
    GetSampleV2 = get_sample
    DeleteSampleV2 = delete_sample
    QuerySampleV1 = query_sample


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
FalconX_Sandbox = FalconXSandbox  # pylint: disable=C0103
