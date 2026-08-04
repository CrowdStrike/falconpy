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
from ._payload import (
    azure_registration_payload,
    aws_d4c_registration_payload,
    gcp_registration_payload,
    cspm_service_account_validate_payload
    )
from ._result import Result
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
    def get_aws_account(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return information about the current status of an AWS account.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetD4CAwsAccount

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of AWS Account IDs to retrieve.
        limit : int
            The maximum records to return. Defaults to 100.
        migrated : str
            Only return migrated D4C accounts.
        offset : int
            The offset to start retrieving records from.
        organization_ids : str or list[str]
            List of AWS Organization IDs to retrieve.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.
        scan_type : str
            Type of scan, `dry` or `full`, to perform on selected accounts.
        status : str
            Account status to filter results by.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
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
    def create_aws_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Register a new AWS account.

        Creates a new account in our system for a customer and generates a
        script for them to run in their AWS cloud environment to grant us access.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/CreateD4CAwsAccount

        Keyword arguments
        -----------------
        account_id : str
            AWS account ID.
        account_type : str
            AWS account type.
        body : dict
            full body payload, not required if using other keywords.
                {
                    "resources": [
                        {
                            "account_id": "string",
                            "account_type": "string",
                            "cloudtrail_region": "string",
                            "iam_role_arn": "string",
                            "is_master": true,
                            "organization_id": "string"
                        }
                    ]
                }
        cloudtrail_region : str
            AWS region for CloudTrail log access.
        iam_role_arn : str
            AWS IAM role ARN.
        is_master : bool
            Flag indicating if this is the master account.
        organization_id : str
            AWS organization ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
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
    def delete_aws_account(self: object,
                           *args,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an existing AWS account or organization from the tenant.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/DeleteD4CAwsAccount

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of AWS Account IDs to retrieve.
        organization_ids : str or list[str]
            List of AWS Organization IDs to retrieve.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteD4CAwsAccount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_console_setup(self: object,
                              *args,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return a URL for customer to visit in their cloud environment to grant CrowdStrike access.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetD4CAwsConsoleSetupURLs

        Keyword arguments
        -----------------
        region : str
            AWS region to generate the URL for.
        parameters : dict
            full parameters payload, not required if region is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'region'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetD4CAwsConsoleSetupURLs",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "region")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_account_scripts(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return a script for customer to run in their cloud environment to grant CrowdStrike access.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetD4CAWSAccountScriptsAttachment

        Keyword arguments
        -----------------
        ids : str or list[str]
            AWS account IDs.
        template : str
            Template to be rendered.
        accounts : str or list[str]
            The list of accounts to register.
        behavior_assessment_enabled : str
            Available values: true, false.
        sensor_management_enabled : str
            Available values: true, false.
        dspm_enabled : str
            Available values: true, false.
        dspm_regions : str or list[str]
            DSPM Regions.
        dspm_host_account_id : str
            DSPM Host Account ID.
        dspm_host_integration_role_name : str
            DSPM Host Integration Role Name.
        dspm_host_scanner_role_name : str
            DSPM Host Scanner Role Name.
        dspm_role : str
            DSPM Role.
        vulnerability_scanning_enabled : str
            Enabled. Available values: true, false.
        vulnerability_scanning_regions : str or list[str]
            Regions.
        vulnerability_scanning_host_account_id : str
            Account ID.
        vulnerability_scanning_host_integration_role_name : str
            Host Integration Role Name.
        vulnerability_scanning_host_scanner_role_name : str
            Host Scanner Role Name.
        vulnerability_scanning_role : str
            Role.
        use_existing_cloudtrail : str
            Use Existing CloudTrail. Available values: true, false.
        organization_id : str
            The AWS organization ID to be registered.
        organizational_unit_ids : str or list[str]
            The AWS Organizational Unit IDs to be registered.
        aws_profile : str
            The AWS profile to be used during registration.
        aws_region : str
            The AWS region to be used during registration.
        iam_role_arn : str
            The custom IAM role to be used during registration.
        falcon_client_id : str
            The Falcon client ID used during registration.
        idp_enabled : str
            Set to true to enable Identity Protection feature.
        tags : str
            Base64 encoded JSON string to be used as AWS tags.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetD4CAWSAccountScriptsAttachment",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_azure_account(self: object,
                          *args,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return information about Azure account registration.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetDiscoverCloudAzureAccount

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of Azure Account IDs to retrieve. If this is empty then all accounts are returned.
        limit : int
            The maximum records to return. Defaults to 100.
        offset : int
            The offset to start retrieving records from.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.
        scan_type : str
            Type of scan, `dry` or `full`, to perform on selected accounts.
        status : str
            Account status to filter results by, 'provisioned' or 'operational'
        tenant_ids : str or list[str]
            Tenant ids to filter azure accounts returned.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("scan_type", None):
            kwargs["scan-type"] = kwargs.get("scan_type", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetDiscoverCloudAzureAccount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_azure_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Register a new Azure account.

        Creates a new account in our system for a customer and generates a
        script for them to run in their cloud environment to grant us access.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/CreateDiscoverCloudAzureAccount

        Keyword arguments
        -----------------
        account_type : str
            Azure Account type.
        body : dict
            full body payload, not required if using other keywords.
                {
                    "resources": [
                        {
                            "account_type": "string",
                            "client_id": "string",
                            "default_subscription": true,
                            "subscription_id": "string",
                            "tenant_id": "string",
                            "years_valid": integer
                        }
                    ]
                }
        client_id : str
            Azure Client ID.
        default_subscription : bool
            Is this the default subscription?
        subscription_id : str
            Azure subscription ID.
        tenant_id : str
            Azure tenant ID.
        years_valid : int
            Years valid.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = azure_registration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateDiscoverCloudAzureAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_azure_account_client_id(self: object,
                                       *args,
                                       parameters: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Azure account client ID.

        Update an Azure service account in our system by with the
        user-created client_id created with the public key we've provided.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /d4c-registration/UpdateDiscoverCloudAzureAccountClientID

        Keyword arguments
        -----------------
        id : str
            ClientID to use for the Service Principal associated
            with the customer's Azure Account.
        object_id : str
            Object ID to use for the Service Principal associated
            with the customer's Azure account.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.
        tenant_id : str
            Tenant ID to update client ID for.
            Required if multiple tenants are registered.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("tenant_id", None):
            kwargs["tenant-id"] = kwargs.get("tenant_id", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateDiscoverCloudAzureAccountClientID",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_azure_user_scripts_attachment(self: object,
                                          parameters: dict = None,
                                          **kwargs
                                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Azure user script attachment.

        Return a script for customer to run in their cloud environment to
        grant us access to their Azure environment as a downloadable attachment.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /d4c-registration/GetDiscoverCloudAzureUserScriptsAttachment

        Keyword arguments
        -----------------
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        azure_management_group : bool
            Use Azure Management Group.
        subscription_ids : str or list[str]
            Azure subscription IDs.
        template : str
            Template to be rendered.
        tenant_id : str
            Azure tenant ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("tenant_id", None):
            kwargs["tenant-id"] = kwargs.get("tenant_id", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetDiscoverCloudAzureUserScriptsAttachment",
            keywords=kwargs,
            params=parameters
            )

    def get_azure_user_scripts(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Azure user script.

        Return a script for customer to run in their cloud
        environment to grant us access to their Azure environment.

        This method does not accept arguments or keywords.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetDiscoverCloudAzureUserScripts

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetDiscoverCloudAzureUserScripts"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_gcp_account(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return information about the current status of an GCP account.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetD4CCGPAccount

        Keyword arguments
        -----------------
        ids : str or list[str]
            Hierarchical Resource IDs of accounts.
        limit : int
            The maximum records to return. Defaults to 100.
        offset : int
            The offset to start retrieving records from.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.
        parent_type : str
            GCP Hierarchy Parent Type, organization/folder/project.
        scan_type : str
            Type of scan, `dry` or `full`, to perform on selected accounts.
        sort : str
            Order fields in ascending or descending order. Ex: parent_type|asc.
        status : str
            Account status to filter results by, 'operational' or 'provisioned'. String.
            This method does not accept arguments or keywords.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetD4CCGPAccount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_gcp_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Register new GCP account.

        Creates a new account in our system for a customer and generates a new service
        account for them to add access to in their GCP environment to grant us access.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/CreateD4CGCPAccount

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if using other keywords.
                {
                    "resources": [
                        {
                            "parent_id": "string",
                            "parent_type": "string"
                        }
                    ]
                }
        parent_id : str
            GCP parent ID.
        parent_type : str
            GCP parent type.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = gcp_registration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateD4CGCPAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_gcp_account(self: object,
                           *args,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete a GCP account from the system.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/DeleteD4CGCPAccount

        Keyword arguments
        -----------------
        ids : str or list[str]
            Hierarchical Resource IDs of accounts.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteD4CGCPAccount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def connect_gcp_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Register new GCP account.

        Creates a new account in our system for a customer and generates a new service
        account for them to add access to in their GCP environment to grant us access.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/ConnectD4CGCPAccount

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if using other keywords.
                {
                    "resources": [
                        {
                            "client_email": "string",
                            "client_id": "string",
                            "parent_id": "string",
                            "parent_type": "string",
                            "private_key": "string",
                            "private_key_id": "string",
                            "project_id": "string",
                            "service_account_id": 0
                        }
                    ]
                }
        client_email : str
            GCP account email.
        client_id : str
            GCP account client ID.
        parent_id : str
            GCP parent ID.
        parent_type : str
            GCP parent type.
        private_key : str
            GCP private key.
        private_key_id : str
            GCP private key ID.
        project_id : str
            GCP project ID.
        service_account_id : int
            GCP service account ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = gcp_registration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ConnectD4CGCPAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_gcp_service_account(self: object,
                                *args,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return the service account id and client email for external clients.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetD4CGCPServiceAccountsExt

        Keyword arguments
        -----------------
        id : str
            Service Account ID.
        parameters : dict
            full parameters payload, not required if id is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetD4CGCPServiceAccountsExt",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_gcp_service_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a GCP service account.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/UpdateD4CGCPServiceAccountsExt

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if using other keywords.
                {
                    "resources": [
                        {
                            "client_email": "string",
                            "client_id": "string",
                            "private_key": "string",
                            "private_key_id": "string",
                            "project_id": "string",
                            "service_account_conditions": [
                                {
                                    "feature": "string",
                                    "is_visible": boolean,
                                    "last_transition": "UTC date string",
                                    "message": "string",
                                    "reason": "string",
                                    "status": "string",
                                    "type": "string"
                                }
                            ],
                            "service_account_id": 0
                        }
                    ]
                }
        client_email : str
            Client email associated with the service account.
        client_id : str
            GCP Client ID.
        private_key : str
            GCP private key.
        private_key_id : str
            GCP private key ID.
        project_id : str
            GCP project ID.
        resources : str
            List of GCP service accounts to validate. List of dictionaries.
            Overrides other keywords except for body.
        service_account_conditions : list[dict]
            GCP service account conditions.
        service_account_id : int
            GCP service account ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cspm_service_account_validate_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateD4CGCPServiceAccountsExt",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_gcp_user_scripts_attachment_v2(self: object,
                                           *args,
                                           parameters: dict = None,
                                           **kwargs
                                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve GCP user script attachment.

        Return a script for customer to run in their cloud environment to
        grant us access to their GCP environment as a downloadable attachment.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetD4CGCPUserScriptsAttachment

        Keyword arguments
        -----------------
        ids : str or list[str]
            Hierarchical Resource IDs of accounts.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.
        parent_type : str
            GCP Hierarchy Parent Type. String.
            Allowed values: organization, folder, project
        status : str
            Account status to filter results by.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetD4CGCPUserScriptsAttachment",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def azure_download_certificate(self: object,
                                   *args,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download Azure Certificate.

        Returns JSON object(s) that contain the base64 encoded certificate for a service principal.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/DiscoverCloudAzureDownloadCertificate

        Keyword arguments
        -----------------
        tenant_id : str or list[str]
            Azure Tenant ID to generate script for.
            Defaults to the most recently registered tenant.
        parameters : dict
            full parameters payload, not required if tenant-id keyword is used.
        refresh : bool
            Force a refresh of the certificate. Boolean. Defaults to False.
        years_valid : str
            Years the certificate should be valid (only used when refresh=true)

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'tenant_id'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DiscoverCloudAzureDownloadCertificate",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "tenant_id")
            )

    def get_azure_tenant_ids(self: object) -> dict:
        """Return all available Azure tenant ids.

        This method does not accept keywords or arguments.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetDiscoverCloudAzureTenantIDs

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetDiscoverCloudAzureTenantIDs"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_gcp_user_scripts(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve GCP user script.

        Return a script for customer to run in their cloud
        environment to grant us access to their GCP environment.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetD4CGCPUserScripts

        Keyword arguments
        -----------------
        parent_type : str
            GCP Hierarchy Parent Type, organization/folder/project.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'parent_type'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetD4CGCPUserScripts",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "parent_type")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_horizon_scripts(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return a script for customer to run in their cloud environment to grant CrowdStrike access.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/d4c-registration/GetHorizonD4CScripts

        Keyword arguments
        -----------------
        account_type : str
            Account type (commercial, gov). Only applicable when registering AWS
            commercial accounts in a Gov environment.
        delete : str
            Generate a delete script.
        organization_id : str
            AWS organization ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        single_account : str
            Get static script for single account.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict object containing API response or a binary script.
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
    GetDiscoverCloudAzureAccount = get_azure_account
    CreateCSPMAzureAccount = create_azure_account
    CreateDiscoverCloudAzureAccount = create_azure_account
    UpdateCSPMAzureAccountClientID = update_azure_account_client_id
    UpdateDiscoverCloudAzureAccountClientID = update_azure_account_client_id
    GetCSPMAzureUserScriptsAttachment = get_azure_user_scripts_attachment
    GetDiscoverCloudAzureUserScriptsAttachment = get_azure_user_scripts_attachment
    DiscoverCloudAzureDownloadCertificate = azure_download_certificate
    GetDiscoverCloudAzureTenantIDs = get_azure_tenant_ids
    GetCSPMAzureUserScripts = get_azure_user_scripts
    GetDiscoverCloudAzureUserScripts = get_azure_user_scripts
    GetCSPMGCPAccount = get_gcp_account   # Typo fix
    GetCSPMCGPAccount = get_gcp_account
    GetD4CGCPAccount = get_gcp_account  # Typo fix
    GetD4CCGPAccount = get_gcp_account
    CreateCSPMGCPAccount = create_gcp_account
    CreateD4CGCPAccount = create_gcp_account
    DeleteD4CGCPAccount = delete_gcp_account
    ConnectD4CGCPAccount = connect_gcp_account
    GetD4CGCPUserScriptsAttachment = get_gcp_user_scripts_attachment_v2
    GetD4CGCPServiceAccountsExt = get_gcp_service_account
    UpdateD4CGCPServiceAccountsExt = update_gcp_service_account
    GetCSPMGCPUserScripts = get_gcp_user_scripts
    GetD4CGCPUserScripts = get_gcp_user_scripts
    GetHorizonD4CScripts = get_aws_horizon_scripts


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
D4C_Registration = D4CRegistration  # pylint: disable=C0103
