"""CrowdStrike Falcon NetworkScanNetworks API interface class.

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
from ._payload import aggregate_payload, network_scan_network_create_payload, network_scan_network_update_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._network_scan_networks import _network_scan_networks_endpoints as Endpoints


class NetworkScanNetworks(ServiceClass):
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
    def aggregate_networks(self: object,
                           body: list = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return network aggregations.

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
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-networks/aggregate_networks
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregate_networks",
            body=body
        )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_networks(self: object,
                     *args,
                     parameters: dict = None,
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get networks by their IDs.

        Keyword arguments:
        ids -- IDs of networks to be retrieved (Min: 1, Max: 100). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-networks/get_networks
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="get_networks",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
        )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_networks(self: object,
                        body: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create networks using provided specifications.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "name": "string",
                    "scanner_aids": [
                        "string"
                    ],
                    "scanner_assignment_type": "string",
                    "subnet": "string",
                    "zone_id": "string"
                }
        name -- The name given to the network. Required. String.
        scanner_aids -- The set of scanners assigned to the network. List of strings.
        scanner_assignment_type -- The scanner assignment type for the network.
                                   Allowed values: local, zone, manual. String.
        subnet -- The subnet included in the network. Required. String.
        zone_id -- The zone to which the network is assigned. Required. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-networks/create_networks
        """
        if not body:
            body = network_scan_network_create_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="create_networks",
            body=body
        )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_networks(self: object,
                        body: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update networks using provided specifications.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "id": "string",
                    "name": "string",
                    "ownership": "string",
                    "scanner_aids": [
                        "string"
                    ],
                    "scanner_assignment_type": "string",
                    "zone_id": "string"
                }
        id -- The unique identifier of the network to update. Required. String.
        name -- The name given to the network. String.
        ownership -- Indicates ownership of the network.
                     Allowed values: unknown, confirmed, denied. String.
        scanner_aids -- The set of scanners assigned to the network. List of strings.
        scanner_assignment_type -- The scanner assignment type for the network.
                                   Allowed values: local, zone, manual. String.
        zone_id -- The zone to which the network is assigned. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-networks/update_networks
        """
        if not body:
            body = network_scan_network_update_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="update_networks",
            body=body
        )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_networks(self: object,
                        *args,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete networks by their IDs.

        Keyword arguments:
        ids -- IDs of networks to be deleted (Min: 1, Max: 100). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-networks/delete_networks
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="delete_networks",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
        )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_networks(self: object,
                       parameters: dict = None,
                       **kwargs
                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get network IDs by filter.

        Keyword arguments:
        offset -- An offset used with the `limit` parameter to manage pagination of results.
                  On your first request, don't provide an `offset`. On subsequent requests,
                  add previous `offset` with the previous `limit` to continue from that place
                  in the results. Integer.
        limit -- The number of network IDs to return in this response
                 (Min: 1, Max: 100, Default: 100). Integer.
        sort -- Sort networks by their properties. A single sort field is allowed. String.
        filter -- Search for networks by providing an FQL filter. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/network-scan-networks/query_networks
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="query_networks",
            keywords=kwargs,
            params=parameters
        )

    # Backward compatibility aliases
    AggregateNetworks = aggregate_networks
    GetNetworks = get_networks
    CreateNetworks = create_networks
    UpdateNetworks = update_networks
    DeleteNetworks = delete_networks
    QueryNetworks = query_networks
