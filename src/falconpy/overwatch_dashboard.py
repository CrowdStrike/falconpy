"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

overwatch_dashboard - Falcon Overwatch Dashboard API Interface Class

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
from ._util import force_default, handle_single_argument, process_service_request
from ._service_class import ServiceClass
from ._endpoint._overwatch_dashboard import _overwatch_dashboard_endpoints as Endpoints


class OverwatchDashboard(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregates_detections_global_counts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get the total number of detections pushed across all customers
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Overwatch%20Dashboard/AggregatesDetectionsGlobalCounts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregatesDetectionsGlobalCounts",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    def aggregates_events_collections(self: object, body: list) -> dict:
        """
        Get OverWatch detection event collection info by providing an aggregate query
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Overwatch%20Dashboard/AggregatesEventsCollections
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregatesEventsCollections",
            body=body
            )

    def aggregates_events(self: object, body: list) -> dict:
        """
        Get aggregate OverWatch detection event info by providing an aggregate query
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Overwatch%20Dashboard/AggregatesEvents
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregatesEvents",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregates_incidents_global_counts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get the total number of incidents pushed across all customers.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Overwatch%20Dashboard/AggregatesIncidentsGlobalCounts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregatesIncidentsGlobalCounts",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregates_events_global_counts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get the total number of incidents pushed across all customers.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Overwatch%20Dashboard/AggregatesOWEventsGlobalCounts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregatesOWEventsGlobalCounts",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    AggregatesDetectionsGlobalCounts = aggregates_detections_global_counts
    AggregatesEventsCollections = aggregates_events_collections
    AggregatesEvents = aggregates_events
    AggregatesIncidentsGlobalCounts = aggregates_incidents_global_counts
    AggregatesOWEventsGlobalCounts = aggregates_events_global_counts


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Overwatch_Dashboard = OverwatchDashboard  # pylint: disable=C0103
