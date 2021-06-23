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
# pylint: disable=C0103  # Aligning method names to API operation IDs
from ._util import service_request, force_default, args_to_params
from ._service_class import ServiceClass
from ._endpoint._falcon_complete_dashboard import _falcon_complete_dashboard_endpoints as Endpoints


class Complete_Dashboard(ServiceClass):
    """The only requirement to instantiate an instance of this class
       is a valid token provided by the Falcon API SDK OAuth2 class, a
       existing instance of the authentication class as an object or a
       valid set of credentials.
    """
    def AggregateAllowList(self: object, body: list) -> dict:
        """Retrieve aggregate allowlist ticket values based on the matched filter"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateAllowList
        operation_id = "AggregateAllowList"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def AggregateBlockList(self: object, body: list) -> dict:
        """Retrieve aggregate blocklist ticket values based on the matched filter"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateBlockList
        operation_id = "AggregateBlockList"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def AggregateDetections(self: object, body: list) -> dict:
        """Retrieve aggregate detection values based on the matched filter"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateDetections
        operation_id = "AggregateDetections"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def AggregateDeviceCountCollection(self: object, body: list) -> dict:
        """Retrieve aggregate host/devices count based on the matched filter"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateDeviceCountCollection
        operation_id = "AggregateDeviceCountCollection"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def AggregateEscalations(self: object, body: list) -> dict:
        """Retrieve aggregate escalation ticket values based on the matched filter"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateEscalations
        operation_id = "AggregateEscalations"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def AggregateFCIncidents(self: object, body: list) -> dict:
        """Retrieve aggregate incident values based on the matched filter"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateFCIncidents
        operation_id = "AggregateFCIncidents"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def AggregateRemediations(self: object, body: list) -> dict:
        """Retrieve aggregate remediation ticket values based on the matched filter"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Falcon%20Complete%20Dashboard/AggregateRemediations
        operation_id = "AggregateRemediations"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryAllowListFilter(self: object, parameters: dict = None, **kwargs) -> dict:
        """Retrieve allowlist tickets that match the provided filter criteria with scrolling enabled"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/QueryAllowListFilter
        operation_id = "QueryAllowListFilter"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   params=parameter_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryBlockListFilter(self: object, parameters: dict = None, **kwargs) -> dict:
        """Retrieve block listtickets that match the provided filter criteria with scrolling enabled"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/QueryBlockListFilter
        operation_id = "QueryBlockListFilter"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   params=parameter_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryDetectionIdsByFilter(self: object, parameters: dict = None, **kwargs) -> dict:
        """Retrieve DetectionsIds that match the provided FQL filter, criteria with scrolling enabled"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/QueryDetectionIdsByFilter
        operation_id = "QueryDetectionIdsByFilter"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   params=parameter_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetDeviceCountCollectionQueriesByFilter(self: object, parameters: dict = None, **kwargs) -> dict:
        """Retrieve device count collection Ids that match the provided FQL filter, criteria with scrolling enabled"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/GetDeviceCountCollectionQueriesByFilter
        operation_id = "GetDeviceCountCollectionQueriesByFilter"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   params=parameter_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryEscalationsFilter(self: object, parameters: dict = None, **kwargs) -> dict:
        """Retrieve escalation tickets that match the provided filter criteria with scrolling enabled"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/QueryEscalationsFilter
        operation_id = "QueryEscalationsFilter"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   params=parameter_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryIncidentIdsByFilter(self: object, parameters: dict = None, **kwargs) -> dict:
        """Retrieve incidents that match the provided filter criteria with scrolling enabled"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/QueryIncidentIdsByFilter
        operation_id = "QueryIncidentIdsByFilter"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   params=parameter_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryRemediationsFilter(self: object, parameters: dict = None, **kwargs) -> dict:
        """Retrieve remediation tickets that match the provided filter criteria with scrolling enabled"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Falcon%20Complete%20Dashboard/QueryRemediationsFilter
        operation_id = "QueryRemediationsFilter"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   params=parameter_payload,
                                   verify=self.ssl_verify
                                   )
        return returned
