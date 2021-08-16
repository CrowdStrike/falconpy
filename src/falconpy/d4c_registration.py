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
from ._util import force_default, process_service_request
from ._service_class import ServiceClass
from ._endpoint._d4c_registration import _d4c_registration_endpoints as Endpoints


class D4CRegistration(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_azure_account(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Return information about Azure account registration
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMAzureAccount
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAzureAccount",
            keywords=kwargs,
            params=parameters
            )

    def create_azure_account(self: object, body: dict) -> dict:
        """
        Creates a new account in our system for a customer and generates a
        script for them to run in their cloud environment to grant us access.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/CreateCSPMAzureAccount
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateCSPMAzureAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_azure_account_client_id(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Update an Azure service account in our system by with the
        user-created client_id created with the public key we've provided
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /d4c-registration/UpdateCSPMAzureAccountClientID
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateCSPMAzureAccountClientID",
            keywords=kwargs,
            params=parameters
            )

    def get_azure_user_scripts_attachment(self: object) -> dict:
        """
        Return a script for customer to run in their cloud environment to
        grant us access to their Azure environment as a downloadable attachment
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #          /d4c-registration/GetCSPMAzureUserScriptsAttachment
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAzureUserScriptsAttachment"
            )

    def get_azure_user_scripts(self: object) -> dict:
        """
        Return a script for customer to run in their cloud environment to grant us access to their Azure environment
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMAzureUserScripts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAzureUserScripts"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_gcp_account(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Returns information about the current status of an GCP account.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMCGPAccount
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMCGPAccount",
            keywords=kwargs,
            params=parameters
            )

    def create_gcp_account(self: object, body: dict) -> dict:
        """
        Creates a new account in our system for a customer and generates a new service
        account for them to add access to in their GCP environment to grant us access.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/CreateCSPMGCPAccount
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateCSPMGCPAccount",
            body=body
            )

    def get_gcp_user_scripts_attachment(self: object) -> dict:
        """
        Return a script for customer to run in their cloud environment to
        grant us access to their GCP environment as a downloadable attachment
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         /d4c-registration/GetCSPMGCPUserScriptsAttachment
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMGCPUserScriptsAttachment"
            )

    def get_gcp_user_scripts(self: object) -> dict:
        """
        Return a script for customer to run in their cloud environment to grant us access to their GCP environment
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMGCPUserScripts
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMGCPUserScripts"
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetCSPMAzureAccount = get_azure_account
    CreateCSPMAzureAccount = create_azure_account
    UpdateCSPMAzureAccountClientID = update_azure_account_client_id
    GetCSPMAzureUserScriptsAttachment = get_azure_user_scripts_attachment
    GetCSPMAzureUserScripts = get_azure_user_scripts
    GetCSPMGCPAccount = get_gcp_account   # Typo fix
    GetCSPMCGPAccount = get_gcp_account
    CreateCSPMGCPAccount = create_gcp_account
    GetCSPMGCPUserScriptsAttachment = get_gcp_user_scripts_attachment
    GetCSPMGCPUserScripts = get_gcp_user_scripts


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
D4C_Registration = D4CRegistration  # pylint: disable=C0103
