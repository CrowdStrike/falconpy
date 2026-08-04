"""Falcon Quick Scan API Interface Class.

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
from ._payload import generic_payload_list, aggregate_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._quick_scan import _quick_scan_endpoints as Endpoints


class QuickScan(ServiceClass):
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

    @force_default(defaults=["body"], default_types=["dict"])
    def get_scans_aggregates(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get scans aggregations as specified via json in request body.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan/GetScansAggregates

        Keyword arguments
        -----------------
        body : list
            full body payload, not required when using other keywords.
                {
                    "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                    ],
                    "field": "string",
                    "filter": "string",
                    "interval": "string",
                    "min_doc_count": 0,
                    "missing": "string",
                    "name": "string",
                    "q": "string",
                    "ranges": [
                        {
                            "From": 0,
                            "To": 0
                        }
                    ],
                    "size": 0,
                    "sort": "string",
                    "sub_aggregates": [
                        null
                    ],
                    "time_zone": "string",
                    "type": "string"
                }
        date_ranges : list[dict]
        field : str
        filter : str
            FQL syntax.
        interval : str
        min_doc_count : int
            Minimum number of documents required to match.
        missing : str
        name : str
            Scan name.
        q : str
            FQL syntax.
        ranges : list[dict]
        size : int
        sort : str
            FQL syntax.
        sub_aggregates : list[str]
        time_zone : str
        type : str
            String.
            This method does not support body payload validation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aggregate_payload(submitted_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetScansAggregates",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_scans(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Check the status of a volume scan.

        Time required for analysis increases with the number of samples in a volume
        but usually it should take less than 1 minute.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan/GetScans

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more remediation IDs.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetScans",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def scan_samples(self: object, *args, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get scans aggregations as specified via json in request body.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan/ScanSamples

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when samples keyword is provided.
                {
                    "samples": [
                        "string"
                    ]
                }
        samples : str or list[str]
            SHA256(s) of the samples to scan. Must have been previously submitted using
            SampleUploadV3 (SampleUploads class)

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'samples'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = generic_payload_list(submitted_arguments=args,
                                        submitted_keywords=kwargs,
                                        payload_value="samples"
                                        )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ScanSamples",
            body=body,
            body_validator={"samples": list} if self.validate_payloads else None,
            body_required=["samples"] if self.validate_payloads else None
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_submissions(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Find IDs for submitted scans by providing an FQL filter and paging details.

        Returns a set of volume IDs that match your criteria.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/quick-scan/QuerySubmissionsMixin0

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
        limit : int (1-5000)
            The maximum number of records to return.
        offset : str
            The integer offset to start retrieving records from.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QuerySubmissionsMixin0",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetScansAggregates = get_scans_aggregates
    GetScans = get_scans
    ScanSamples = scan_samples
    QuerySubmissionsMixin0 = query_submissions
    QuerySubmissions = query_submissions


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Quick_Scan = QuickScan  # pylint: disable=C0103
