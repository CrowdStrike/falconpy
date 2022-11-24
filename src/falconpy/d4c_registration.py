"""Falcon Discover registration for Azure / GCP API Interface Class.

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
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import azure_registration_payload, aws_d4c_registration_payload
from ._service_class import ServiceClass
from ._endpoint._d4c_registration import _d4c_registration_endpoints as Endpoints


class D4CRegistration(ServiceClass):
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

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_account(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Return information about the current status of an AWS account.

        Keyword arguments:
        ids -- List of AWS Account IDs to retrieve. String or list of strings.
        limit -- The maximum records to return. Defaults to 100. Integer.
        migrated -- Only return migrated D4C accounts. Boolean.
        offset -- The offset to start retrieving records from. Integer.
        organization_ids -- List of AWS Organization IDs to retrieve. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.
        scan_type -- Type of scan, `dry` or `full`, to perform on selected accounts.
        status -- Account status to filter results by. String.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetD4CAwsAccount
        """
        if kwargs.get("scan_type", None):
            kwargs["scan-type"] = kwargs.get("scan_type", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetD4CAwsAccount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_aws_account(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Register a new AWS account.

        Creates a new account in our system for a customer and generates a
        script for them to run in their AWS cloud environment to grant us access.

        Keyword arguments:
        account_id -- AWS account ID. String.
        account_type -- AWS account type. String.
        body -- full body payload, not required if using other keywords.
                {
                    "resources": [
                        {
                            "account_id": "string",
                            "account_type": "string",
                            "cloudtrail_region": "string",
                            "is_master": true,
                            "organization_id": "string"
                        }
                    ]
                }
        cloudtrail_region -- AWS region for CloudTrail log access.
        is_master -- Flag indicating if this is the master account. Boolean.
        organization_id -- AWS organization ID. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/CreateD4CAwsAccount
        """
        if not body:
            body = aws_d4c_registration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateD4CAwsAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_aws_account(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Delete an existing AWS account or organization from the tenant.

        Keyword arguments:
        ids -- List of AWS Account IDs to retrieve. String or list of strings.
        organization_ids -- List of AWS Organization IDs to retrieve. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/DeleteD4CAwsAccount
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteD4CAwsAccount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_console_setup(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Return a URL for customer to visit in their cloud environment to grant CrowdStrike access.

        Keyword arguments:
        region -- AWS region to generate the URL for. String.
        parameters -- full parameters payload, not required if region is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'region'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetD4CAwsConsoleSetupURLs
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetD4CAwsConsoleSetupURLs",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "region")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_account_scripts(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Return a script for customer to run in their cloud environment to grant CrowdStrike access.

        Keyword arguments:
        ids -- List of AWS Account IDs to retrieve the script for. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetD4CAWSAccountScriptsAttachment
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetD4CAWSAccountScriptsAttachment",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_azure_account(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Return information about Azure account registration.

        Keyword arguments:
        ids -- List of Azure Account IDs to retrieve. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.
        scan_type -- Type of scan, `dry` or `full`, to perform on selected accounts.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMAzureAccount
        """
        if kwargs.get("scan_type", None):
            kwargs["scan-type"] = kwargs.get("scan_type", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAzureAccount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_azure_account(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Register a new Azure account.

        Creates a new account in our system for a customer and generates a
        script for them to run in their cloud environment to grant us access.

        Keyword arguments:
        body -- full body payload, not required if using other keywords.
                {
                    "resources": [
                        {
                            "subscription_id": "string",
                            "tenant_id": "string"
                        }
                    ]
                }
        subscription_id -- Azure subscription ID. String.
        tenant_id -- Azure tenant ID. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/CreateCSPMAzureAccount
        """
        if not body:
            body = azure_registration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateCSPMAzureAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_azure_account_client_id(self: object,
                                       *args,
                                       parameters: dict = None,
                                       **kwargs
                                       ) -> Dict[str, Union[int, dict]]:
        """Update Azure account client ID.

        Update an Azure service account in our system by with the
        user-created client_id created with the public key we've provided.

        Keyword arguments:
        id -- ClientID to use for the Service Principal associated
              with the customer's Azure Account.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'id'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/UpdateCSPMAzureAccountClientID
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateCSPMAzureAccountClientID",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    def get_azure_user_scripts_attachment(self: object) -> Dict[str, Union[int, dict]]:
        """Retrieve Azure user script attachment.

        Return a script for customer to run in their cloud environment to
        grant us access to their Azure environment as a downloadable attachment.

        This method does not accept arguments or keywords.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMAzureUserScriptsAttachment
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAzureUserScriptsAttachment"
            )

    def get_azure_user_scripts(self: object) -> Dict[str, Union[int, dict]]:
        """Retrieve Azure user script.

        Return a script for customer to run in their cloud
        environment to grant us access to their Azure environment.

        This method does not accept arguments or keywords.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMAzureUserScripts
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAzureUserScripts"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_gcp_account(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Return information about the current status of an GCP account.

        Keyword arguments:
        ids -- List of Response Policy IDs to retrieve. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.
        scan_type -- Type of scan, `dry` or `full`, to perform on selected accounts.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMCGPAccount
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMCGPAccount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_gcp_account(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Register new GCP account.

        Creates a new account in our system for a customer and generates a new service
        account for them to add access to in their GCP environment to grant us access.

        Keyword arguments:
        body -- full body payload, not required if using other keywords.
                {
                    "resources": [
                        {
                            "parent_id": "string"
                        }
                    ]
                }
        parent_id -- GCP parent ID. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/CreateCSPMGCPAccount
        """
        if not body:
            body = {}
            body["resources"] = []
            body["resources"].append({"parent_id": kwargs.get("parent_id", None)})

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateCSPMGCPAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def azure_download_certificate(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Download Azure Certificate.

        Returns JSON object(s) that contain the base64 encoded certificate for a service principal.

        Keyword arguments:
        tenant_id -- Azure Tenant ID to generate script for.
                     Defaults to the most recently registered tenant.
        parameters -- full parameters payload, not required if tenant-id keyword is used.
        refresh -- Force a refresh of the certificate. Boolean. Defaults to False.

        Arguments: When not specified, the first argument to this method is assumed to be
                   'tenant_id'. All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/DiscoverCloudAzureDownloadCertificate
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DiscoverCloudAzureDownloadCertificate",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "tenant_id")
            )

    def get_gcp_user_scripts_attachment(self: object) -> Dict[str, Union[int, dict]]:
        """Retrieve GCP user script attachment.

        Return a script for customer to run in their cloud environment to
        grant us access to their GCP environment as a downloadable attachment.

        This method does not accept arguments or keywords.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMGCPUserScriptsAttachment
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMGCPUserScriptsAttachment"
            )

    def get_gcp_user_scripts(self: object) -> Dict[str, Union[int, dict]]:
        """Retrieve GCP user script.

        Return a script for customer to run in their cloud
        environment to grant us access to their GCP environment.

        This method does not accept arguments or keywords.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetCSPMGCPUserScripts
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMGCPUserScripts"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_horizon_scripts(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Return a script for customer to run in their cloud environment to grant CrowdStrike access.

        Keyword arguments:
        account_type -- Account type (commercial, gov). Only applicable when registering AWS
                        commercial accounts in a Gov environment. String.
        delete -- Generate a delete script. Boolean.
        organization_id -- AWS organization ID. String.
        parameters -- full parameters payload, not required if using other keywords.
        single_account -- Get static script for single account. Boolean.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response or a binary script.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetHorizonD4CScripts
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetHorizonD4CScripts",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetD4CAwsAccount = get_aws_account
    CreateD4CAwsAccount = create_aws_account
    DeleteD4CAwsAccount = delete_aws_account
    GetD4CAwsConsoleSetupURLs = get_aws_console_setup
    GetD4CAWSAccountScriptsAttachment = get_aws_account_scripts
    GetCSPMAzureAccount = get_azure_account
    CreateCSPMAzureAccount = create_azure_account
    UpdateCSPMAzureAccountClientID = update_azure_account_client_id
    GetCSPMAzureUserScriptsAttachment = get_azure_user_scripts_attachment
    DiscoverCloudAzureDownloadCertificate = azure_download_certificate
    GetCSPMAzureUserScripts = get_azure_user_scripts
    GetCSPMGCPAccount = get_gcp_account   # Typo fix
    GetCSPMCGPAccount = get_gcp_account
    CreateCSPMGCPAccount = create_gcp_account
    GetCSPMGCPUserScriptsAttachment = get_gcp_user_scripts_attachment
    GetCSPMGCPUserScripts = get_gcp_user_scripts
    GetHorizonD4CScripts = get_aws_horizon_scripts


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
D4C_Registration = D4CRegistration  # pylint: disable=C0103
