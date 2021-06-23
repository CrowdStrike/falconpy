"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

recon - CrowdStrike Falcon X Recon API interface class

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
from ._endpoint._recon import _recon_endpoints as Endpoints


class Recon(ServiceClass):
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """
    def AggregateNotificationsV1(self: object, body: dict) -> dict:
        """Get notification aggregates as specified via JSON in request body."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/AggregateNotificationsV1
        operation_id = "AggregateNotificationsV1"
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

    def PreviewRuleV1(self: object, body: dict) -> dict:
        """Get notification aggregates as specified via JSON in request body."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/PreviewRuleV1
        operation_id = "PreviewRuleV1"
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
    def GetActionsV1(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get actions based on their IDs. IDs can be retrieved using the GET /queries/actions/v1 endpoint."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetActionsV1
        operation_id = "GetActionsV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def CreateActionsV1(self: object, body: dict) -> dict:
        """Create actions for a monitoring rule. Accepts a list of actions that will be attached to the monitoring rule"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/CreateActionsV1
        operation_id = "CreateActionsV1"
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
    def DeleteActionV1(self: object, parameters: dict = None, **kwargs) -> dict:
        """Delete an action from a monitoring rule based on the action ID."""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/DeleteActionV1
        operation_id = "DeleteActionV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def UpdateActionV1(self: object, body: dict) -> dict:
        """Update an action for a monitoring rule."""
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/UpdateActionV1
        operation_id = "UpdateActionV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetNotificationsDetailedTranslatedV1(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get detailed notifications based on their IDs. These include the raw intelligence content that generated the match.
           This endpoint will return translated notification content.
           The only target language available is English. A single notification can be translated per request
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetNotificationsDetailedTranslatedV1
        operation_id = "GetNotificationsDetailedTranslatedV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetNotificationsDetailedV1(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get detailed notifications based on their IDs.
           These include the raw intelligence content that generated the match.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetNotificationsDetailedV1
        operation_id = "GetNotificationsDetailedV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetNotificationsTranslatedV1(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get notifications based on their IDs. IDs can be retrieved using the GET /queries/notifications/v1 endpoint.
           This endpoint will return translated notification content. The only target language available is English.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetNotificationsTranslatedV1
        operation_id = "GetNotificationsTranslatedV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetNotificationsV1(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get notifications based on their IDs. IDs can be retrieved using the GET /queries/notifications/v1 endpoint."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetNotificationsV1
        operation_id = "GetNotificationsV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def DeleteNotificationsV1(self: object, parameters: dict = None, **kwargs) -> dict:
        """Delete notifications based on IDs. Notifications cannot be recovered after they are deleted."""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/DeleteNotificationsV1
        operation_id = "DeleteNotificationsV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def UpdateNotificationsV1(self: object, body: dict) -> dict:
        """Update notification status or assignee. Accepts bulk requests"""
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/UpdateNotificationsV1
        operation_id = "UpdateNotificationsV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetRulesV1(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get monitoring rules rules by provided IDs."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/GetRulesV1
        operation_id = "GetRulesV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def CreateRulesV1(self: object, body: dict) -> dict:
        """Create monitoring rules."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/CreateRulesV1
        operation_id = "CreateRulesV1"
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
    def DeleteRulesV1(self: object, parameters: dict = None, **kwargs) -> dict:
        """Delete monitoring rules."""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/DeleteRulesV1
        operation_id = "DeleteRulesV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def UpdateRulesV1(self: object, body: dict) -> dict:
        """Update monitoring rules."""
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/UpdateRulesV1
        operation_id = "UpdateRulesV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryActionsV1(self: object, parameters: dict = None, **kwargs) -> dict:
        """Query actions based on provided criteria.
           Use the IDs from this response to get the action entities on GET /entities/actions/v1.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/QueryActionsV1
        operation_id = "QueryActionsV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryNotificationsV1(self: object, parameters: dict = None, **kwargs) -> dict:
        """Query notifications based on provided criteria.
           Use the IDs from this response to get the notification entities on GET /entities/notifications/v1
           or GET /entities/notifications-detailed/v1.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/QueryNotificationsV1
        operation_id = "QueryNotificationsV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def QueryRulesV1(self: object, parameters: dict = None, **kwargs) -> dict:
        """Query monitoring rules based on provided criteria.
           Use the IDs from this response to fetch the rules on /entities/rules/v1.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/recon/QueryRulesV1
        operation_id = "QueryRulesV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned
