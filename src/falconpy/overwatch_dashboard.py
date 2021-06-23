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
# pylint: disable=C0103  # Aligning method names to API operation IDs
from ._util import service_request, force_default, args_to_params
from ._service_class import ServiceClass
from ._endpoint._overwatch_dashboard import _overwatch_dashboard_endpoints as Endpoints


class Overwatch_Dashboard(ServiceClass):
    """The only requirement to instantiate an instance of this class
       is a valid token provided by the Falcon API SDK OAuth2 class, a
       existing instance of the authentication class as an object or a
       valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def AggregatesDetectionsGlobalCounts(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get the total number of detections pushed across all customers"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Overwatch%20Dashboard/AggregatesDetectionsGlobalCounts
        fname = "AggregatesDetectionsGlobalCounts"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   params=parameter_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def AggregatesEventsCollections(self: object, body: list) -> dict:
        """Get OverWatch detection event collection info by providing an aggregate query"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /Overwatch%20Dashboard/AggregatesEventsCollections
        fname = "AggregatesEventsCollections"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}"
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

    def AggregatesEvents(self: object, body: list) -> dict:
        """Get aggregate OverWatch detection event info by providing an aggregate query"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/Overwatch%20Dashboard/AggregatesEvents
        fname = "AggregatesEvents"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}"
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
    def AggregatesIncidentsGlobalCounts(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get the total number of incidents pushed across all customers."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Overwatch%20Dashboard/AggregatesIncidentsGlobalCounts
        fname = "AggregatesIncidentsGlobalCounts"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   params=parameter_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def AggregatesOWEventsGlobalCounts(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get the total number of incidents pushed across all customers."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /Overwatch%20Dashboard/AggregatesOWEventsGlobalCounts
        fname = "AggregatesOWEventsGlobalCounts"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if fname in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, fname)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   params=parameter_payload,
                                   verify=self.ssl_verify
                                   )
        return returned
