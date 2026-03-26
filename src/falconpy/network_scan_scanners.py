"""CrowdStrike Falcon NetworkScanScanners API interface class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |        FalconPy
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
from ._payload import aggregate_payload, network_scan_scanners_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._network_scan_scanners import _network_scan_scanners_endpoints as Endpoints


class NetworkScanScanners(ServiceClass):
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

    @force_default(defaults=["body"], default_types=["list"])
    def aggregate_scanners(self: object,
                           body: list = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return scanners aggregations.

        Keyword arguments:
        body -- Full body payload as a list of dictionaries in JSON format.
                [{
                    "date_ranges": [{}],
                    "exclude": "string",
                    "field": "string",
                    "filter": "string",
                    "from": integer,
                    "include": "string",
                    "interval": "string",
                    "missing": "string",
                    "min_doc_count": integer,
                    "name": "string",
                    "q": "string",
                    "ranges": [{}],
                    "size": integer,
                    "sort": "string",
                    "sub_aggregates": [{}],
                    "time_zone": "string",
                    "type": "string"
                }]

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-scanners/aggregate_scanners
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_scanners",
            body=body
        )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_scanners(self: object,
                     *args,
                     parameters: dict = None,
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get scanners by their IDs.

        Keyword arguments:
        ids -- IDs of scanners to be retrieved (Min: 1, Max: 100). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-scanners/get_scanners
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_scanners",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
        )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_scanners(self: object,
                        body: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update scanners using provided specifications.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "action": "string",
                    "aids": [
                        "string"
                    ]
                }
        action -- The action to take on the provided set of scanners.
                  Allowed values: add, remove. Required. String.
        aids -- The AIDs of scanners to act on. Required. List of strings.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-scanners/update_scanners
        """
        if not body:
            body = network_scan_scanners_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_scanners",
            body=body
        )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_scanners(self: object,
                       parameters: dict = None,
                       **kwargs
                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get scanner IDs by filter.

        Keyword arguments:
        offset -- An offset used with the `limit` parameter to manage pagination of results.
                  On your first request, don't provide an `offset`. On subsequent requests,
                  add previous `offset` with the previous `limit` to continue from that place
                  in the results. Integer.
        limit -- The number of scanner IDs to return in this response (Min: 1, Max: 100,
                 Default: 100). Integer.
        sort -- Sort scanners by their properties. A single sort field is allowed. String.
        filter -- Search for scanners by providing an FQL filter. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-scanners/query_scanners
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_scanners",
            keywords=kwargs,
            params=parameters
        )

    # Backward compatibility aliases
    AggregateScanners = aggregate_scanners
    GetScanners = get_scanners
    UpdateScanners = update_scanners
    QueryScanners = query_scanners
