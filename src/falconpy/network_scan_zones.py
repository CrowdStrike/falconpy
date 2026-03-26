"""CrowdStrike Falcon NetworkScanZones API interface class.

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
from ._payload import aggregate_payload, network_scan_zone_create_payload, network_scan_zone_update_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._network_scan_zones import _network_scan_zones_endpoints as Endpoints


class NetworkScanZones(ServiceClass):
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
    def aggregate_zones(self: object,
                        body: list = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return zone aggregations.

        Keyword arguments:
        body -- Full body payload as a list of dictionaries in JSON format. Not required if using other keywords.
                [
                    {
                        "date_ranges": [
                            {
                                "from": "string",
                                "to": "string"
                            }
                        ],
                        "exclude": "string",
                        "field": "string",
                        "filter": "string",
                        "from": integer,
                        "include": "string",
                        "interval": "string",
                        "max_doc_count": integer,
                        "min_doc_count": integer,
                        "missing": "string",
                        "name": "string",
                        "q": "string",
                        "ranges": [
                            {
                                "From": integer,
                                "To": integer
                            }
                        ],
                        "size": integer,
                        "sort": "string",
                        "sub_aggregates": [
                            {}
                        ],
                        "time_zone": "string",
                        "type": "string"
                    }
                ]
        date_ranges -- Array of date range specifications for date-based aggregations. List of dictionaries.
        exclude -- Fields to exclude from the aggregation. String.
        field -- The field to aggregate on. String.
        filter -- FQL query to filter the data before aggregating. String.
        from -- Starting index for the aggregation. Integer.
        include -- Fields to include in the aggregation. String.
        interval -- Time interval for date histogram aggregations (e.g., day, week, month). String.
        max_doc_count -- Maximum document count for bucket inclusion. Integer.
        min_doc_count -- Minimum document count for bucket inclusion. Integer.
        missing -- The value to use for documents missing the aggregation field. String.
        name -- The name of the aggregation query. String.
        q -- Full-text search query string. String.
        ranges -- Numeric range specifications for range aggregations. List of dictionaries.
        size -- The maximum number of results to return per aggregate. Integer.
        sort -- The field to sort aggregate results on. String.
        sub_aggregates -- Nested sub-aggregation specifications. List of dictionaries.
        time_zone -- The time zone to use for date aggregations. String.
        type -- The type of aggregate query to perform. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-zones/aggregate_zones
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_zones",
            body=body
        )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def combined_zones(self: object,
                       parameters: dict = None,
                       **kwargs
                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get zones by filter.

        Keyword arguments:
        offset -- An offset used with the `limit` parameter to manage pagination of results.
                  On your first request, don't provide an `offset`. On subsequent requests,
                  add previous `offset` with the previous `limit` to continue from that place
                  in the results. Integer.
        limit -- The number of zones to return in this response (Min: 1, Max: 100, Default: 100). Integer.
        sort -- Sort zones by their properties. A single sort field is allowed. String.
        filter -- Search for zones by providing an FQL filter. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-zones/combined_zones
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="combined_zones",
            keywords=kwargs,
            params=parameters
        )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_zones(self: object,
                  *args,
                  parameters: dict = None,
                  **kwargs
                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get zones by their IDs.

        Keyword arguments:
        ids -- IDs of zones to be retrieved (Min: 1, Max: 100). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-zones/get_zones
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_zones",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
        )

    @force_default(defaults=["body"], default_types=["list"])
    def create_zones(self: object,
                     body: list = None,
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create zones using provided specifications.

        Keyword arguments:
        body -- Full body payload as a list of dictionaries in JSON format. Not required if using other keywords.
                [
                    {
                        "name": "string",
                        "scanners": [
                            "string"
                        ]
                    }
                ]
        name -- The name given to the zone. Required. String.
        scanners -- The set of scanner AIDs assigned to the zone. List of strings.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-zones/create_zones
        """
        if not body:
            body = [network_scan_zone_create_payload(passed_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="create_zones",
            body=body
        )

    @force_default(defaults=["body"], default_types=["list"])
    def update_zones(self: object,
                     body: list = None,
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update zones using provided specifications.

        Keyword arguments:
        body -- Full body payload as a list of dictionaries in JSON format. Not required if using other keywords.
                [
                    {
                        "id": "string",
                        "name": "string",
                        "scanners_to_add": [
                            "string"
                        ],
                        "scanners_to_remove": [
                            "string"
                        ]
                    }
                ]
        id -- The unique identifier of the zone to update. Required. String.
        name -- The name given to the zone. String.
        scanners_to_add -- The scanner AIDs to be added to the zone. List of strings.
        scanners_to_remove -- The scanner AIDs to be removed from the zone. List of strings.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-zones/update_zones
        """
        if not body:
            body = [network_scan_zone_update_payload(passed_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_zones",
            body=body
        )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_zones(self: object,
                     *args,
                     parameters: dict = None,
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete zones by their IDs.

        Keyword arguments:
        ids -- IDs of zones to be deleted (Min: 1, Max: 100). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-zones/delete_zones
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="delete_zones",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
        )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_zones(self: object,
                    parameters: dict = None,
                    **kwargs
                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get zone IDs by filter.

        Keyword arguments:
        offset -- An offset used with the `limit` parameter to manage pagination of results.
                  On your first request, don't provide an `offset`. On subsequent requests,
                  add previous `offset` with the previous `limit` to continue from that place
                  in the results. Integer.
        limit -- The number of zone IDs to return in this response (Min: 1, Max: 100, Default: 100). Integer.
        sort -- Sort zones by their properties. A single sort field is allowed. String.
        filter -- Search for zones by providing an FQL filter. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-zones/query_zones
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_zones",
            keywords=kwargs,
            params=parameters
        )

    # Backward compatibility aliases
    AggregateZones = aggregate_zones
    CombinedZones = combined_zones
    GetZones = get_zones
    CreateZones = create_zones
    UpdateZones = update_zones
    DeleteZones = delete_zones
    QueryZones = query_zones
