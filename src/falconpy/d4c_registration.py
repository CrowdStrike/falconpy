"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

d4c_registration - Falcon Discover for Azure / GCP API Interface Class

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
from ._endpoint._d4c_registration import _d4c_registration_endpoints as Endpoints


class D4C_Registration(ServiceClass):  # pylint: disable=C0103  # Matching API
    """The only requirement to instantiate an instance of this class
       is a valid token provided by the Falcon API SDK OAuth2 class, a
       existing instance of the authentication class as an object or a
       valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetCSPMAzureAccount(self: object, parameters: dict = None, **kwargs) -> dict:
        """Return information about Azure account registration"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMAzureAccount
        operation_id = "GetCSPMAzureAccount"
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

    def CreateCSPMAzureAccount(self: object, body: dict) -> dict:
        """Creates a new account in our system for a customer and generates a
           script for them to run in their cloud environment to grant us access.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/CreateCSPMAzureAccount
        operation_id = "CreateCSPMAzureAccount"
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
    def UpdateCSPMAzureAccountClientID(self: object, parameters: dict = None, **kwargs) -> dict:
        """Update an Azure service account in our system by with the
           user-created client_id created with the public key we've provided
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /d4c-registration/UpdateCSPMAzureAccountClientID
        operation_id = "UpdateCSPMAzureAccountClientID"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def GetCSPMAzureUserScriptsAttachment(self: object) -> dict:
        """Return a script for customer to run in their cloud environment to
           grant us access to their Azure environment as a downloadable attachment
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /d4c-registration/GetCSPMAzureUserScriptsAttachment
        operation_id = "GetCSPMAzureUserScriptsAttachment"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def GetCSPMAzureUserScripts(self: object) -> dict:
        """Return a script for customer to run in their cloud environment to grant us access to their Azure environment"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMAzureUserScripts
        operation_id = "GetCSPMAzureUserScripts"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    # I'm here to assist those who spell it correctly
    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetCSPMGCPAccount(self: object, *args, **kwargs) -> dict:
        """Returns information about the current status of an GCP account."""
        returned = self.GetCSPMCGPAccount(*args, **kwargs)
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def GetCSPMCGPAccount(self: object, parameters: dict = None, **kwargs) -> dict:
        """Returns information about the current status of an GCP account."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMCGPAccount
        operation_id = "GetCSPMCGPAccount"
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

    def CreateCSPMGCPAccount(self: object, body: dict) -> dict:
        """Creates a new account in our system for a customer and generates a new service
           account for them to add access to in their GCP environment to grant us access.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/CreateCSPMGCPAccount
        operation_id = "CreateCSPMGCPAccount"
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

    def GetCSPMGCPUserScriptsAttachment(self: object) -> dict:
        """Return a script for customer to run in their cloud environment to
           grant us access to their GCP environment as a downloadable attachment
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /d4c-registration/GetCSPMGCPUserScriptsAttachment
        operation_id = "GetCSPMGCPUserScriptsAttachment"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def GetCSPMGCPUserScripts(self: object) -> dict:
        """Return a script for customer to run in their cloud environment to grant us access to their GCP environment"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMGCPUserScripts
        operation_id = "GetCSPMGCPUserScripts"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned
