"""CrowdStrike Falcon ServerlessExports API interface class.

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
from typing import Dict, Union
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import serverless_exports_launch_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._serverless_exports import _serverless_exports_endpoints as Endpoints


class ServerlessExports(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (oauth2.py)
    """

    @force_default(defaults=["parameters"], default_types=["dict"])
    def download_export_file(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download an export file.

        Keyword arguments:
        id -- Export job ID. String. Required.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'id'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/serverless-exports/DownloadExportFileMixin0
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DownloadExportFileMixin0",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_export_jobs(self: object,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Read export jobs entities.

        Keyword arguments:
        ids -- Export Job IDs to read. Allowed up to 100 IDs per request.
               String or list of strings. Required.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/serverless-exports/ReadExportJobsMixin0
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadExportJobsMixin0",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def launch_export_job(self: object,
                          body: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Launch an export job of a Lambda Security resource.

        Maximum of 1 job in progress per resource. Use expand_vulnerabilities=true
        to get detailed vulnerability information.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using
                other keywords.
                {
                    "expand_vulnerabilities": boolean,
                    "format": "string",
                    "fql": "string",
                    "resource": "string",
                    "sort": "string"
                }
        expand_vulnerabilities -- Flag to include detailed vulnerability information. Boolean.
        format -- The export file format. String.
        fql -- Filter the export using Falcon Query Language (FQL). String.
        resource -- The resource to export. Supported resources:
                    function.detections, function.vulnerabilities-expanded,
                    function.vulnerabilities. String.
        sort -- The fields to sort the records on. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/serverless-exports/LaunchExportJobMixin0
        """
        if not body:
            body = serverless_exports_launch_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="LaunchExportJobMixin0",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_export_jobs(self: object,
                          *args,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query export jobs entities.

        Keyword arguments:
        filter -- Filter exports using a query in Falcon Query Language (FQL).
                  Only the last 100 jobs are returned.
                  Supported filter fields: resource, status. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be
                   'filter'. All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/serverless-exports/QueryExportJobsMixin0
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryExportJobsMixin0",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_vulnerabilities(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve all lambda vulnerabilities that match the given query and return in the SARIF format.

        Keyword arguments:
        filter -- Filter lambda vulnerabilities using a query in Falcon Query Language (FQL). String.
                  Supported filters:
                    application_name                function_name
                    application_name_version        function_resource_id
                    cid                             is_supported
                    cloud_account_id                is_valid_asset_id
                    cloud_account_name              layer
                    cloud_provider                  region
                    cve_id                          runtime
                    cve_reachable                   severity
                    cvss_base_score                 timestamp
                    exprt_rating                    type
                    first_seen_timestamp
        limit -- The upper-bound on the number of records to retrieve. Integer.
        offset -- The offset from where to begin. Integer.
        sort -- The fields to sort the records on.
                Supported columns:
                    application_name                first_seen_timestamp
                    application_name_version        function_resource_id
                    cid                             is_supported
                    cloud_account_id                layer
                    cloud_account_name              region
                    cloud_provider                  runtime
                    cve_id                          severity
                    cvss_base_score                 timestamp
                    exprt_rating                    type
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/serverless-vulnerabilities/GetCombinedVulnerabilitiesSARIF
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCombinedVulnerabilitiesSARIF",
            keywords=kwargs,
            params=parameters
            )

    DownloadExportFileMixin0 = download_export_file
    ReadExportJobsMixin0 = read_export_jobs
    LaunchExportJobMixin0 = launch_export_job
    QueryExportJobsMixin0 = query_export_jobs
    GetCombinedVulnerabilitiesSARIF = get_vulnerabilities
