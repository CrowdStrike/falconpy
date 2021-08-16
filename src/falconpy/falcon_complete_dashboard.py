"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

falcon_complete_dashboard - Falcon Complete Dashboard API Interface Class

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
from ._util import process_service_request, force_default
from ._service_class import ServiceClass
from ._endpoint._falcon_complete_dashboard import _falcon_complete_dashboard_endpoints as Endpoints


class CompleteDashboard(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    def aggregate_allow_list(self: object, body: list) -> dict:
        """
        Retrieve aggregate allowlist ticket values based on the matched filter
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateAllowList
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateAllowList",
            body=body
            )

    def aggregate_block_list(self: object, body: list) -> dict:
        """
        Retrieve aggregate blocklist ticket values based on the matched filter
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateBlockList
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateBlockList",
            body=body
            )

    def aggregate_detections(self: object, body: list) -> dict:
        """
        Retrieve aggregate detection values based on the matched filter
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateDetections
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateDetections",
            body=body
            )

    def aggregate_device_count_collection(self: object, body: list) -> dict:
        """
        Retrieve aggregate host/devices count based on the matched filter
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateDeviceCountCollection
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            methods="POST",
            operation_id="AggregateDeviceCountCollection",
            body=body
            )

    def aggregate_escalations(self: object, body: list) -> dict:
        """
        Retrieve aggregate escalation ticket values based on the matched filter
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateEscalations
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateEscalations",
            body=body
            )

    def aggregate_fc_incidents(self: object, body: list) -> dict:
        """
        Retrieve aggregate incident values based on the matched filter
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateFCIncidents
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateFCIncidents",
            body=body
            )

    def aggregate_remediations(self: object, body: list) -> dict:
        """
        Retrieve aggregate remediation ticket values based on the matched filter
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateRemediations
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="AggregateRemediations",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_allow_list_filter(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve allowlist tickets that match the provided filter criteria with scrolling enabled
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/QueryAllowListFilter
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryAllowListFilter",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_block_list_filter(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve block listtickets that match the provided filter criteria with scrolling enabled
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/QueryBlockListFilter
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryBlockListFilter",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_detection_ids_by_filter(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve DetectionsIds that match the provided FQL filter, criteria with scrolling enabled
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/QueryDetectionIdsByFilter
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryDetectionIdsByFilter",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_device_count_collection_queries_by_filter(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve device count collection Ids that match the provided FQL filter, criteria with scrolling enabled
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/GetDeviceCountCollectionQueriesByFilter
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetDeviceCountCollectionQueriesByFilter",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_escalations_filter(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve escalation tickets that match the provided filter criteria with scrolling enabled
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/QueryEscalationsFilter
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryEscalationsFilter",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_incident_ids_by_filter(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve incidents that match the provided filter criteria with scrolling enabled
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/QueryIncidentIdsByFilter
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryIncidentIdsByFilter",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_remediations_filter(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve remediation tickets that match the provided filter criteria with scrolling enabled
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/QueryRemediationsFilter
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryRemediationsFilter",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    AggregateAllowList = aggregate_allow_list
    AggregateBlockList = aggregate_block_list
    AggregateDetections = aggregate_detections
    AggregateDeviceCountCollection = aggregate_device_count_collection
    AggregateEscalations = aggregate_escalations
    AggregateFCIncidents = aggregate_fc_incidents
    AggregateRemediations = aggregate_remediations
    QueryAllowListFilter = query_allow_list_filter
    QueryBlockListFilter = query_block_list_filter
    QueryDetectionIdsByFilter = query_detection_ids_by_filter
    GetDeviceCountCollectionQueriesByFilter = get_device_count_collection_queries_by_filter
    QueryEscalationsFilter = query_escalations_filter
    QueryIncidentIdsByFilter = query_incident_ids_by_filter
    QueryRemediationsFilter = query_remediations_filter


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Complete_Dashboard = CompleteDashboard  # pylint: disable=C0103
