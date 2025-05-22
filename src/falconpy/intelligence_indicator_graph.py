"""CrowdStrike Falcon IntelligenceIndicatorGraph API interface class.

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
from ._util import force_default, process_service_request
from ._payload import indicator_graph_payload, aggregate_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._intelligence_indicator_graph import _intelligence_indicator_graph_endpoints as Endpoints


class IntelligenceIndicatorGraph(ServiceClass):
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
    def aggregate_indicators(self: object,
                             body: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get indicator aggregates.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "requests": [
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
                            }
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
                                null
                            ],
                            "time_zone": "string",
                            "type": "string"
                        }
                    ]
                }
        date_ranges -- If peforming a date range query specify the from and to date ranges.
                       These can be in common date formats like 2019-07-18 or now.
                       List of dictionaries.
        exclude -- Fields to exclude. String.
        extended_bounds -- Extended bounds. Dictionary containing "min" and "max" as strings.
        field -- Term you want to aggregate on. If doing a date_range query,
                 this is the date field you want to apply the date ranges to. String.
        filter -- Optional filter criteria in the form of an FQL query.
                  For more information about FQL queries, see our FQL documentation in Falcon.
                  String.
        from -- Integer.
        include -- Fields to include. String.
        interval -- String.
        max_doc_count -- Maximum number of documents. Integer.
        min_doc_count -- Minimum number of documents. Integer.
        missing -- String.
        name -- Scan name. String.
        q -- FQL syntax. String.
        ranges -- List of dictionaries.
        size -- Integer.
        sort -- FQL syntax. String.
        sub_aggregates -- List of strings.
        time_zone -- String.
        type -- String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/user-management/aggregateUsersV1
        """
        if not body:
            body = {"requests": [aggregate_payload(submitted_keywords=kwargs)]}

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIndicatorAggregates",
            body=body
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def search(self: object,
               body: dict = None,
               parameters: dict = None,
               **kwargs
               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search indicators based on FQL filter.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "filter": "string",
                    "sort": [
                        {
                            "field": "string",
                            "order": "string"
                        }
                    ]
                }
        filter -- FQL formatted filter. String.
        limit -- Returned record limit. Integer.
        offset -- Offset to start returning results. Integer.
        sort -- List of sort operations to perform on the returnset. List of dictionaries.

        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/intelligence-indicator-graph/SearchIndicators
        """
        if not body:
            body = indicator_graph_payload(kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="SearchIndicators",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    GetIndicatorAggregates = aggregate_indicators
    SearchIndicators = search
