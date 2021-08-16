"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

cspm_registration - Falcon Horizon for AWS API Interface Class

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
from ._util import force_default, process_service_request, handle_single_argument
from ._service_class import ServiceClass
from ._endpoint._cspm_registration import _cspm_registration_endpoints as Endpoints


class CSPMRegistration(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, an
    authorization object (oauth2.py) or a credential dictionary with
    client_id and client_secret containing valid API credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_account(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Returns information about the current status of an AWS account.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAwsAccount
        # Since there are multiple inbound "id" possibilities here. We are unable
        # to make calls leveraging a single argument, keywords only are supported
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAwsAccount",
            keywords=kwargs,
            params=parameters
            )

    def create_aws_account(self: object, body: dict) -> dict:
        """
        Creates a new account in our system for a customer and generates a script
        to run in their AWS cloud environment to grant CrowdStrike Horizon access.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/CreateCSPMAwsAccount
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateCSPMAwsAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_aws_account(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Delete an existing AWS Account or Organization by specifying their IDs.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/DeleteCSPMAwsAccount
        # Since there are multiple inbound "id" possibilities here.
        # we are unable to calls leveraging a single argument, keywords only are supported
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteCSPMAwsAccount",
            keywords=kwargs,
            params=parameters
            )

    def update_aws_account(self: object, body: dict) -> dict:
        """
        Patches a existing account in our system for a customer.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/PatchCSPMAwsAccount
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PatchCSPMAwsAccount",
            body=body
            )

    def get_aws_console_setup_urls(self: object) -> dict:
        """
        Returns a URL for customers to visit in their cloud environment to grant access to CrowdStrike
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAwsConsoleSetupURLs
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAwsConsoleSetupURLs"
            )

    def get_aws_account_scripts_attachment(self: object) -> dict:
        """
        Return a script for customers to run in their cloud environment
        to grant access to CrowdStrike for their AWS environment.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /cspm-registration/GetCSPMAwsAccountScriptsAttachment
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAwsAccountScriptsAttachment"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_azure_account(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Return information about Azure account registration.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAzureAccount
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAzureAccount",
            keywords=kwargs,
            params=parameters
            )

    def create_azure_account(self: object, body: dict) -> dict:
        """
        Creates a new account in our system for a customer and generates a script
        to run in their cloud environment to grant CrowdStrike Horizon access.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/CreateCSPMAzureAccount
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateCSPMAzureAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_azure_account(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Delete an existing Azure Subscription by specifying their IDs.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/DeleteCSPMAzureAccount
        # This method supports calls using a single argument as opposed to keywords
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteCSPMAzureAccount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_azure_account_client_id(self: object, body: dict = None, parameters: dict = None, **kwargs) -> dict:
        """
        Update an Azure service account in our system with the
        user-created client_id created with the public key we've provided.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         ...   /cspm-registration/UpdateCSPMAzureAccountClientID2
        # This shows up as UpdateCSPMAzureAccountClientID2 in the Uber class
        if body is None:
            body = {}   # Force a default body
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateCSPMAzureAccountClientID",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_azure_tenant_default_subscription_id(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Update an Azure service account in our system with the
        user-created client_id created with the public key we've provided.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         ...  /cspm-registration/UpdateCSPMAzureTenantDefaultSubscriptionID
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateCSPMAzureTenantDefaultSubscriptionID",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_azure_user_scripts_attachment(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Return a script for customers to run in their cloud environment
        to grant access to CrowdStrike for their Azure environment.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #       ...     /cspm-registration/GetCSPMAzureUserScriptsAttachment
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAzureUserScriptsAttachment",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "tenant-id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_ioa_events(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        For CSPM IOA events, gets list of IOA events.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetIOAEvents
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIOAEvents",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_ioa_users(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        For CSPM IOA users, gets list of IOA users.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetIOAUsers
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIOAUsers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policy(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Given a policy ID, returns detailed policy information.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMPolicy
        # Supports single argument calls
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMPolicy",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policy_settings(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Returns information about current policy settings.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMPolicySettings
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMPolicySettings",
            keywords=kwargs,
            params=parameters
            )

    def update_policy_settings(self: object, body: dict) -> dict:
        """
        Updates a policy setting - can be used to override policy severity or to disable a policy entirely.
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #         ...   /cspm-registration/UpdateCSPMPolicySettings
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateCSPMPolicySettings",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_scan_schedule(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Returns scan schedule configuration for one or more cloud platforms.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMScanSchedule
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMScanSchedule",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "cloud-platform")
            )

    def update_scan_schedule(self: object, body: dict) -> dict:
        """
        Updates scan schedule configuration for one or more cloud platforms.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/UpdateCSPMScanSchedule
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateCSPMScanSchedule",
            body=body
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetCSPMAwsAccount = get_aws_account
    CreateCSPMAwsAccount = create_aws_account
    DeleteCSPMAwsAccount = delete_aws_account
    PatchCSPMAwsAccount = update_aws_account
    GetCSPMAwsConsoleSetupURLs = get_aws_console_setup_urls
    GetCSPMAwsAccountScriptsAttachment = get_aws_account_scripts_attachment
    GetCSPMAzureAccount = get_azure_account
    CreateCSPMAzureAccount = create_azure_account
    DeleteCSPMAzureAccount = delete_azure_account
    UpdateCSPMAzureAccountClientID = update_azure_account_client_id
    UpdateCSPMAzureTenantDefaultSubscriptionID = update_azure_tenant_default_subscription_id
    GetCSPMAzureUserScriptsAttachment = get_azure_user_scripts_attachment
    GetIOAEvents = get_ioa_events
    GetIOAUsers = get_ioa_users
    GetCSPMPolicy = get_policy
    GetCSPMPolicySettings = get_policy_settings
    UpdateCSPMPolicySettings = update_policy_settings
    GetCSPMScanSchedule = get_scan_schedule
    UpdateCSPMScanSchedule = update_scan_schedule


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
CSPM_Registration = CSPMRegistration  # pylint: disable=C0103
