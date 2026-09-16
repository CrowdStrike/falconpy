"""CrowdStrike Falcon NetworkScanDetections API interface class.

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
from ._payload import aggregate_netscan_detections_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._network_scan_detections import _network_scan_detections_endpoints as Endpoints


class NetworkScanDetections(ServiceClass):
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
    def aggregate_netscan_detections(self: object,
                                     body: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return "detections" aggregations.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-detections/aggregate_detections

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                    ],
                    "exclude": "string",
                    "extended_bounds": {
                        "max": "string",
                        "min": "string"
                    },
                    "field": "string",
                    "filter": "string",
                    "filters_spec": {
                        "filters": "string",
                        "other_bucket": true,
                        "other_bucket_key": "string"
                    },
                    "from": 0,
                    "include": "string",
                    "interval": "string",
                    "max_doc_count": 0,
                    "min_doc_count": 0,
                    "missing": "string",
                    "name": "string",
                    "percents": [
                        "string"
                    ],
                    "q": "string",
                    "ranges": [
                        {
                            "From": 0.0,
                            "To": 0.0
                        }
                    ],
                    "size": 0,
                    "sort": "string",
                    "sub_aggregates": [
                        "string"
                    ],
                    "time_zone": "string",
                    "type": "string"
                }
        date_ranges : list
            The date_ranges value.
        exclude : str
            The exclude value.
        extended_bounds : dict
            The extended_bounds value.
        field : str
            The field value.
        filter : str
            The filter value.
        filters_spec : dict
            The filters_spec value.
        from : int
            The from value.
        include : str
            The include value.
        interval : str
            The interval value.
        max_doc_count : int
            The max_doc_count value.
        min_doc_count : int
            The min_doc_count value.
        missing : str
            The missing value.
        name : str
            The name value.
        percents : list
            The percents value.
        q : str
            The q value.
        ranges : list
            The ranges value.
        size : int
            The size value.
        sort : str
            The sort value.
        sub_aggregates : list
            The sub_aggregates value.
        time_zone : str
            The time_zone value.
        type : str
            The type value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aggregate_netscan_detections_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_detections",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_combined_netscan_detections(self: object,
                                        parameters: dict = None,
                                        **kwargs
                                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get "detections" by filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-detections/combined_detections

        Keyword arguments
        -----------------
        offset : int
            An offset used with the limit parameter to manage pagination of results. On your first request, don’t provide
            an offset. On subsequent requests, add previous offset with the previous limit to continue from that place in
            the results.
        limit : int
            The number of "detections" to return in this response (Min: 1, Max: 100, Default: 100)
        sort : str
            Sort "detections" by their properties. A single sort field is allowed.
        filter : str
            Search for "detections" by providing an FQL filter.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="combined_detections",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_netscan_detections(self: object,
                               *args,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get "detections" by their IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-detections/get_detections

        Keyword arguments
        -----------------
        ids : str or list[str]
            IDs of "detections" to be retrieved (Min: 1, Max: 100)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

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
            operation_id="get_detections",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_netscan_detections(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get "detections IDs" by filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-detections/query_detections

        Keyword arguments
        -----------------
        offset : int
            An offset used with the limit parameter to manage pagination of results. On your first request, don’t provide
            an offset. On subsequent requests, add previous offset with the previous limit to continue from that place in
            the results.
        limit : int
            The number of "detections IDs" to return in this response (Min: 1, Max: 100, Default: 100)
        sort : str
            Sort "detections" by their properties. A single sort field is allowed.
        filter : str
            Search for "detections" by providing an FQL filter.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_detections",
            keywords=kwargs,
            params=parameters
            )
    aggregate_detections = aggregate_netscan_detections
    combined_detections = get_combined_netscan_detections
    get_detections = get_netscan_detections
    query_detections = query_netscan_detections
