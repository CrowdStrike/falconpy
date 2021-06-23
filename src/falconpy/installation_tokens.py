"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

installation_tokens - Falcon Installation Tokens API Interface Class

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
from ._util import service_request, args_to_params, force_default
from ._service_class import ServiceClass
from ._endpoint._installation_tokens import _installation_tokens_endpoints as Endpoints


class Installation_Tokens(ServiceClass):  # pylint: disable=C0103  # Matching API
    """The only requirement to instantiate an instance of this class
       is a valid token provided by the Falcon API SDK OAuth2 class, a
       existing instance of the authentication class as an object or a
       valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def audit_events_read(self: object, parameters: dict = None, **kwargs) -> dict:
        """Gets the details of one or more audit events by id."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/audit-events-read
        operation_id = "audit_events_read"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        header_payload = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def customer_settings_read(self: object) -> dict:
        """Check current installation token settings."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/customer-settings-read
        operation_id = "customer_settings_read"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def tokens_read(self: object, parameters: dict = None, **kwargs) -> dict:
        """Gets the details of one or more tokens by id."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/tokens-read
        operation_id = "tokens_read"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        header_payload = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def tokens_create(self: object, body: dict) -> dict:
        """Creates a token."""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/tokens-create
        operation_id = "tokens_create"
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
    def tokens_delete(self: object, parameters: dict = None, **kwargs) -> dict:
        """Deletes a token immediately. To revoke a token, use PATCH /installation-tokens/entities/tokens/v1 instead."""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/tokens-delete
        operation_id = "tokens_delete"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        header_payload = self.headers
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def tokens_update(self: object, body: dict, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103
        """Updates one or more tokens. Use this endpoint to edit labels, change expiration, revoke, or restore."""
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/tokens-update
        operation_id = "tokens_update"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=target_url,
                                   body=body_payload,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def audit_events_query(self: object, parameters: dict = None, **kwargs) -> dict:
        """Search for audit events by providing an FQL filter and paging details."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/audit-events-query
        operation_id = "audit_events_query"
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
    def tokens_query(self: object, parameters: dict = None, **kwargs) -> dict:
        """Search for tokens by providing an FQL filter and paging details."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/tokens-query
        operation_id = "tokens_query"
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
