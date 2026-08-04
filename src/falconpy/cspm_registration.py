"""Falcon Horizon for AWS API Interface Class.

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
# pylint: disable=R0904, C0302  # Matching API operation counts and allowing the long file for now
from typing import Dict, Union
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import (
    cspm_registration_payload,
    cspm_policy_payload,
    cspm_scan_payload,
    gcp_registration_payload,
    generic_payload_list,
    cspm_service_account_validate_payload
    )
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._cspm_registration import _cspm_registration_endpoints as Endpoints


class CSPMRegistration(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (OAuth2.token())
    """

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_account(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return information about the current status of an AWS account.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAwsAccount

        Keyword arguments
        -----------------
        scan_type : str
            Type of scan, `dry` or `full`, to perform on selected accounts
        cspm_lite : str
            Only return CSPM lite accounts.
        ids : str or list[str]
            AWS account IDs.
        iam_role_arns : str or list[str]
            AWS IAM role ARNs.
        organization_ids : str or list[str]
            AWS organization IDs.
        limit : int
            The maximum number of records to return in this response. [Integer, 1-1000]
            Use with the offset parameter to manage pagination of results. Defaults to 100.
        migrated : str
            Only return migrated d4c accounts. (true / false)
        offset : int
            The offset to start retrieving records from. Integer.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        status : str
            Account status to filter results by.
        group_by : str
            Field to group by. String. (Only acceptable value: `organization`)

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("scan_type", None):
            kwargs["scan-type"] = kwargs.get("scan_type", None)

        if kwargs.get("organization_ids", None):
            kwargs["organization-ids"] = kwargs.get("organization_ids", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAwsAccount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_aws_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Register a new AWS account.

        Creates a new account in our system for a customer and generates a script
        to run in their AWS cloud environment to grant CrowdStrike Horizon access.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/CreateCSPMAwsAccount

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "resources": [
                        {
                            "account_id": "string",
                            "account_type": "string",
                            "behavior_assessment_enabled": boolean,
                            "cloudtrail_region": "string",
                            "deployment_method": "string",
                            "dspm_enabled": boolean,
                            "dspm_role": "string",
                            "falcon_client_id": "string",
                            "iam_role_arn": "string",
                            "is_master": boolean,
                            "organization_id": "string",
                            "root_stack_id": "string",
                            "sensor_management_enabled": boolean,
                            "target_ous": [
                                "string"
                            ],
                            "use_existing_cloudtrail": boolean
                        }
                    ]
                }
        account_id : str
            AWS Account ID.
        account_type : str
            AWS account type.
        behavior_assessment_enabled : bool
            Indicate if behavior assessment should be enabled.
        cloudtrail_region : str
            AWS Cloudtrail Region.
        deployment_method : str
            Deployment method.
        dspm_enabled : bool
            Flag indicating if DSPM should be enabled.
        dspm_role : str
            DSPM role.
        falcon_client_id : str
            Falcon Client ID.
        iam_role_arn : str
            IAM role ARN to use.
        is_master : bool
            Indicate if this is the primary account.
        organization_id : str
            AWS Organization ID.
        root_stack_id : str
            Root stack ID.
        sensor_management_enabled : bool
            Indicate if sensor management should be enabled.
        target_ous : str or list[str]
            List of target OUs.
        use_existing_cloudtrail : bool
            Indicate if the existing CloudTrail should be used.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cspm_registration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateCSPMAwsAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_aws_account(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an existing AWS Account or Organization by specifying their IDs.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/DeleteCSPMAwsAccount

        Keyword arguments
        -----------------
        ids : str or list[str]
            AWS Account IDs to remove.
        organization_ids : str or list[str]
            AWS Organization IDs to be removed.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("organization_ids", None):
            kwargs["organization-ids"] = kwargs.get("organization_ids", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteCSPMAwsAccount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_aws_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Patches a existing account in our system for a customer.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/PatchCSPMAwsAccount

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "resources": [
                        {
                            "account_id": "string",
                            "behavior_assessment_enabled": true,
                            "cloudtrail_region": "string",
                            "iam_role_arn": "string",
                            "remediation_region": "string",
                            "remediation_tou_accepted": "2023-06-07T18:28:36.303Z",
                            "sensor_management_enabled": true
                        }
                    ]
                }
        account_id : str
            AWS Account ID.
        behavior_assessment_enabled : bool
            Indicate if behavior assessment should be enabled.
        cloudtrail_region : str
            AWS Cloudtrail Region.
        iam_role_arn : str
            IAM role ARN to use.
        remediation_region : str
            AWS region to remediation.
        remediation_tou_accepted : str
            Timestamp formatted.
        cloudtrail_region : str
            AWS Cloudtrail Region.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cspm_registration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PatchCSPMAwsAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_console_setup_urls(self: object,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve setup URLs for the AWS console.

        Returns a URL for customers to visit in their cloud environment
        to grant access to CrowdStrike.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAwsConsoleSetupURLs

        Keyword arguments
        -----------------
        ids : str or list[str]
            AWS Account IDs to retrieve setup URLs for.
        use_existing_cloudtrail : str
            Use the existing AWS cloudtrail. (true / false)
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        region : str
            AWS Region.
        tags : str
            Base64 encoded JSON string to be used as AWS tags.
        template : str
            Template to be rendered. String.
            Allowed values:
            aws-url         aws-sensor-management-url
            aws-iom-url     aws-dspm-url
            aws-ioa-url     aws-idp-ur
            aws-modular-cft-url
            aws-modular-cft-gov-commercial-url

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAwsConsoleSetupURLs",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_account_scripts_attachment(self: object,
                                           parameters: dict = None,
                                           **kwargs
                                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve AWS account scripts.

        Return a script for customers to run in their cloud environment
        to grant access to CrowdStrike for their AWS environment.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAwsAccountScriptsAttachment

        Keyword arguments
        -----------------
        account_type : str
            CSPM account type. String. Allowed values: gov, commercial
        accounts : str or list[str]
            List of accounts to register. String or list of strings. Format: account,profile
        aws_profile : str
            The AWS profile to be used during registration.
        behavior_assessment_enabled : str
            Enable behavior assessment. String. Allowed values: true, false
        custom_role_name : str
            The custom IAM role to be used during registration.
        dspm_enabled : str
            Flag indicating if DSPM is enabled. String. Allowed values: true, false
        dspm_regions : str or list[str]
            List of DSPM regions. Comma delimited.
        dspm_role : str
            DSPM role.
        ids : str or list[str]
            List of AWS Account IDs to retrieve the script for.
        organization_id : str
            The AWS organization ID to be registered.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.
        sensor_management_enabled : str
            Enable sensor management. String. Allowed values: true, false
        template : str
            Template to be rendered. String. Allowed values: aws-bash, aws-terraform
        use_existing_cloudtrail : str
            Use the existing cloudtrail log. String. Allowed values: true, false

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAwsAccountScriptsAttachment",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_azure_account(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return information about Azure account registration.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAzureAccount

        Keyword arguments
        -----------------
        scan_type : str
            Type of scan, `dry` or `full`, to perform on selected accounts
        cspm_lite : str
            Only return CSPM lite accounts.
        ids : str or list[str]
            Azure account IDs.
        limit : int
            The maximum number of records to return in this response. [Integer, 1-1000]
            Use with the offset parameter to manage pagination of results. Defaults to 100.
        offset : int
            The offset to start retrieving records from. Integer.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        status : str
            Account status to filter results by.
        tenant_ids : str or list[str]
            Azure tenant IDs to filter results.

        This method only supports keywords for providing arguments.

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
            operation_id="GetCSPMAzureAccount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_azure_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Register new Azure account.

        Creates a new account in our system for a customer and generates a script
        to run in their cloud environment to grant CrowdStrike Horizon access.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/CreateCSPMAzureAccount

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "resources": [
                        {
                            "account_type": "string",
                            "client_id": "string",
                            "default_subscription": true,
                            "subscription_id": "string"
                            "tenant_id": "string",
                            "years_valid": integer
                        }
                    ]
                }
        account_type : str
            Azure account type.
        client_id : str
            Azure Client ID.
        default_subscription : bool
            Indicate if this is the default subscription.
        subscription_id : str
            Azure Subscription ID.
        tenant_id : str
            Azure Tenant ID.
        years_valid : int
            Number of years this account is valid.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cspm_registration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateCSPMAzureAccount",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_azure_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Azure account.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/UpdateCSPMAzureAccount

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "resources": [
                        {
                            "environment": "string",
                            "subscription_id": "string"
                        }
                    ]
                }
        account_type : str
            Azure account type.
        client_id : str
            Azure Client ID.
        default_subscription : bool
            Indicate if this is the default subscription.
        subscription_id : str
            Azure Subscription ID.
        tenant_id : str
            Azure Tenant ID.
        years_valid : int
            Number of years this account is valid.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cspm_registration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateCSPMAzureAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_azure_account(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an existing Azure Subscription by specifying their IDs.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/DeleteCSPMAzureAccount

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of Azure Subscription IDs to delete.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.
        retain_tenant : str
            Should the tenant be retainined. (true / false)
        tenant_ids : str or list[str]
            Azure tenant IDs to remove.

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
            operation_id="DeleteCSPMAzureAccount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def update_azure_account_client_id(self: object,
                                       body: dict = None,
                                       parameters: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update Azure account Client ID.

        Update an Azure service account in our system with the
        user-created client_id created with the public key we've provided.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/UpdateCSPMAzureAccountClientID

        Keyword arguments
        -----------------
        body : dict
            There are no body payload parameters. This field is not used. Ignore.
        id : str
            List of Azure Subscription IDs to delete.
        tenant_id : str
            Azure Tenant ID to update client ID for.
            Required if multiple tenants are registered.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

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
            operation_id="UpdateCSPMAzureAccountClientID",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def update_azure_tenant_default_subscription_id(self: object,
                                                    body: dict = None,
                                                    parameters: dict = None,
                                                    **kwargs
                                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update default subscription ID.

        Update an Azure service account in our system with the
        user-created client_id created with the public key we've provided.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /cspm-registration/UpdateCSPMAzureTenantDefaultSubscriptionID

        Keyword arguments
        -----------------
        body : dict
            There are no body payload parameters. This field is not used. Ignore.
        subscription_id : str
            Default Subscription ID to patch for all subscriptions
            belonging to the tenant.
        tenant_id : str
            Azure Tenant ID to update client ID for.
            Required if multiple tenants are registered.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

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
            operation_id="UpdateCSPMAzureTenantDefaultSubscriptionID",
            keywords=kwargs,
            body=body,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def azure_download_certificate(self: object,
                                   *args,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Azure certificate.

        Returns JSON object(s) that contain the base64 encoded certificate for a service principal.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/AzureDownloadCertificate

        Keyword arguments
        -----------------
        tenant_id : str or list[str]
            Azure Tenant ID to generate script for.
            Defaults to the most recently registered tenant.
        parameters : dict
            full parameters payload, not required if tenant_id keyword is used.

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
            operation_id="AzureDownloadCertificate",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "tenant_id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_azure_management_group(self: object,
                                   *args,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return information about Azure management group registration.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAzureManagementGroup

        Keyword arguments
        -----------------
        limit : int
            The maximum number of records to return. Defaults to 100.
        offset : int
            The offset to start retrieving records from.
        parameters : dict
            full parameters payload, not required if tenant_id keyword is used.
        tenant_ids : str or list[str]
            Azure Tenant ID to filter by.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'tenant_ids'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAzureManagementGroup",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "tenant_ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_azure_management_group(self: object,
                                      body: dict = None,
                                      **kwargs
                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Register new Azure account.

        Creates a new account in our system for a customer and generates a script
        to run in their cloud environment to grant CrowdStrike Horizon access.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/CreateCSPMAzureManagementGroup

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "resources": [
                        {
                            "default_subscription_id": "string"
                            "tenant_id": "string",
                        }
                    ]
                }
        default_subscription_id : str
            ID of the default azure subscription.
        tenant_id : str
            Azure Tenant ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cspm_registration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateCSPMAzureManagementGroup",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_azure_management_group(self: object,
                                      *args,
                                      parameters: dict = None,
                                      **kwargs
                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an existing Azure Managment Group by specifying their IDs.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/DeleteCSPMAzureManagementGroup

        Keyword arguments
        -----------------
        tenant_ids : str or list[str]
            AWS Organization IDs to be removed.
        parameters : dict
            full parameters payload, not required if tenant_ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'tenant_ids'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteCSPMAzureManagementGroup",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "tenant_ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def azure_refresh_certificate(self: object,
                                  *args,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Refresh Azure certificate.

        Returns JSON object(s) that contain the base64 encoded certificate for a service principal.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/AzureRefreshCertificate

        Keyword arguments
        -----------------
        tenant_id : str or list[str]
            Azure Tenant ID to refresh.
        parameters : dict
            full parameters payload, not required if tenant_id keyword is used.
        years_valid : str
            Years the certificate should be valid. Integer. Max: 2

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
            operation_id="AzureRefreshCertificate",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "tenant_id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_azure_user_scripts_attachment(self: object,
                                          *args,
                                          parameters: dict = None,
                                          **kwargs
                                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Azure user script.

        Return a script for customers to run in their cloud environment
        to grant access to CrowdStrike for their Azure environment.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAzureUserScriptsAttachment

        Keyword arguments
        -----------------
        account_type : str
            Account type. ('commercial' or 'gov')
        azure_management_group : bool
            Use Azure Management Group.
        tenant_id : str
            Azure Tenant ID to generate script for.
            Defaults to the most recently registered tenant.
        parameters : dict
            full parameters payload, not required if tenant_id keyword is used.
        subscription_ids : str or list[str]
            Subscription IDs to generate script for. Defaults to all.
        template : str
            Template to be rendered.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'tenant_id'. All others are ignored.

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
            operation_id="GetCSPMAzureUserScriptsAttachment",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "tenant_id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_gcp_account(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return information about the current status of an GCP account.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMGCPAccount

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
        if kwargs.get("scan_type", None):
            kwargs["scan-type"] = kwargs.get("scan_type", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMGCPAccount",
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
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/CreateCSPMGCPAccount

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
            operation_id="CreateCSPMGCPAccount",
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
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/DeleteCSPMGCPAccount

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
            operation_id="DeleteCSPMGCPAccount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_gcp_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a GCP account.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/UpdateCSPMGCPAccount

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if using other keywords.
                {
                    "resources": [
                        {
                            "environment": "string",
                            "parent_id": "string"
                        }
                    ]
                }
        environment : str
            GCP environment.
        parent_id : str
            GCP parent ID.

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
            operation_id="UpdateCSPMGCPAccount",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def connect_gcp_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Register new GCP account.

        Creates a new account in our system for a customer and generates a new service
        account for them to add access to in their GCP environment to grant us access.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/ConnectCSPMGCPAccount

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
            operation_id="ConnectCSPMGCPAccount",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def validate_gcp_account(self: object, *args, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Run a synchronous health check.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMGCPValidateAccountsExt

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if using other keywords.
                {
                    "resources": [
                        "string"
                    ]
                }
        resources : str or list[str]
            GCP Account IDs to validate.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'resources'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = generic_payload_list(submitted_keywords=kwargs,
                                        submitted_arguments=args,
                                        payload_value="resources"
                                        )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMGCPValidateAccountsExt",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def validate_gcp_service_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Validate credentials for a GCP service account.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/ValidateCSPMGCPServiceAccountExt

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
                                    "last_transition": "2024-03-19T22:48:28.987Z",
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
            operation_id="ValidateCSPMGCPServiceAccountExt",
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
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMGCPServiceAccountsExt

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
            operation_id="GetCSPMGCPServiceAccountsExt",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_gcp_service_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a GCP service account.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/UpdateCSPMGCPServiceAccountsExt

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
            operation_id="UpdateCSPMGCPServiceAccountsExt",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_gcp_user_scripts_attachment(self: object,
                                        *args,
                                        parameters: dict = None,
                                        **kwargs
                                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve GCP user script attachment.

        Return a script for customer to run in their cloud environment to
        grants access to the GCP environment as a downloadable attachment.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMGCPUserScriptsAttachment

        Keyword arguments
        -----------------
        ids : str or list[str]
            Hierarchical Resource IDs of accounts.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.
        parent_type : str
            GCP Hierarchy Parent Type. String.
            Allowed values: organization, folder, project

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
            operation_id="GetCSPMGCPUserScriptsAttachment",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_behavior_detections(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve list of detected behaviors.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetBehaviorDetections

        Keyword arguments
        -----------------
        account_id : str
            Cloud Account ID (AWS account ID, Azure Subscription ID, etc.)
        aws_account_id : str
            AWS account ID.
        azure_subscription_id : str
            Azure subscription ID.
        azure_tenant_id : str
            Azure tenant ID.
        cloud_provider : str
            Cloud provider. Allowed values: `azure`, `aws`, `gcp`
        date_time_since : str
            Filter to retrieve all events after this date. RFC3339 formatted string.
            Example: 2006-01-01T12:00:01Z07:00
        limit : int (1-500)
            The maximum number of records to return in this response.
        next_token : str
            String to get next page of results, associated with the previous
            execution. Must include all filters from previous execution.
        resource_id : str or list[str]
            Resource ID.
        resource_uuid : str or list[str]
            Resource UUID.
        service : str
            Cloud Service (Example: `EC2` or `S3`). String.
            Available options
            ACM                      Identity
            ACR                      KMS
            Any                      KeyVault
            App Engine               Kinesis
            BigQuery                 Kubernetes
            Cloud Load Balancing     Lambda
            Cloud Logging            LoadBalancer
            Cloud SQL                Monitor
            Cloud Storage            NLB/ALB
            CloudFormation           NetworkSecurityGroup
            CloudTrail               PostgreSQL
            CloudWatch Logs          RDS
            Cloudfront               Redshift
            Compute Engine           S3
            Config                   SES
            Disk                     SNS
            DynamoDB                 SQLDatabase
            EBS                      SQLServer
            EC2                      SQS
            ECR                      SSM
            EFS                      Serverless Application Repository
            EKS                      StorageAccount
            ELB                      Subscriptions
            EMR                      VPC
            Elasticache              VirtualMachine
            GuardDuty                VirtualNetwork
            IAM
        severity : str
            Severity (e.g. `High`, `Medium` or `Informational`)
        since : str
            Filter events using a duration string (e.g. 24h). String. Default: 24h
        state : str
            State. (e.g. `open` or `closed`)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetBehaviorDetections",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_configuration_detections(self: object,
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve list of active misconfigurations.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetConfigurationDetections

        Keyword arguments
        -----------------
        account_id : str
            Cloud Account ID (AWS account ID, Azure Subscription ID, etc.)
        aws_account_id : str
            AWS account ID.
        azure_subscription_id : str
            Azure subscription ID.
        azure_tenant_id : str
            Azure tenant ID.
        cloud_provider : str
            Cloud provider. Allowed values: `azure`, `aws`, `gcp`
        limit : int (1-500)
            The maximum number of records to return in this response.
        next_token : str
            String to get next page of results, associated with the previous
            execution. Cannot be combined with any filter except `limit`
        region : str
            Cloud Provider Region (Example: `us-east-1`)
        service : str
            Cloud Service (Example: `EC2` or `S3`). String.
            Available options
            ACM                      Identity
            ACR                      KMS
            Any                      KeyVault
            App Engine               Kinesis
            BigQuery                 Kubernetes
            Cloud Load Balancing     Lambda
            Cloud Logging            LoadBalancer
            Cloud SQL                Monitor
            Cloud Storage            NLB/ALB
            CloudFormation           NetworkSecurityGroup
            CloudTrail               PostgreSQL
            CloudWatch Logs          RDS
            Cloudfront               Redshift
            Compute Engine           S3
            Config                   SES
            Disk                     SNS
            DynamoDB                 SQLDatabase
            EBS                      SQLServer
            EC2                      SQS
            ECR                      SSM
            EFS                      Serverless Application Repository
            EKS                      StorageAccount
            ELB                      Subscriptions
            EMR                      VPC
            Elasticache              VirtualMachine
            GuardDuty                VirtualNetwork
            IAM
        severity : str
            Severity (e.g. `High`, `Medium` or `Informational`)
        status : str
            Status (e.g. `new`, `reoccurring`, or `all`)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetConfigurationDetections",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_configuration_detection_entities(self: object,
                                             *args,
                                             parameters: dict = None,
                                             **kwargs
                                             ) -> dict:
        """Get misconfigurations based on the ID - including custom policy detections in addition to default policy detections.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetConfigurationDetectionEntities

        Keyword arguments
        -----------------
        ids : str or list[str]
            Detection IDs to retrieve.
        parameters : dict
            full parameters payload, not required ids keyword is used.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetConfigurationDetectionEntities",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_cloud_event_ids(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get list of related cloud event LogScale IDs for a given IOA.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/getCloudEventIDs

        Keyword arguments
        -----------------
        id : str
            IOA Aggregate Event ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getCloudEventIDs",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_configuration_detection_ids_v2(self: object,
                                           parameters: dict = None,
                                           **kwargs
                                           ) -> dict:
        """Get list of active misconfiguration ids - including custom and default policy detections.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetConfigurationDetectionIDsV2

        Keyword arguments
        -----------------
        filter : str
            FQL formatted string to filter result. String.
            Allowed filters
            account_name              policy_id
            account_id                policy_type
            agent_id                  resource_id
            attack_types              region
            azure_subscription_id     status
            cloud_provider            scan_time
            cloud_service_keyword     severity
            custom_policy_id          severity_string
            is_managed                use_current_scan_ids (*)
            (*) Use this to retrieve records for the latest scans
        limit : int
            Maximum number of detections to return. Integer. (Default: 500)
        next_token : str
            Token to use to retrieve the next page of results.
            Cannot be combined with any filter except limit.
        offset : int
            Starting offset for returned detections.
        sort : str
            FQL formatted sort. String. Default: timestamp|desc
            Allowed values
            account_name            policy_id
            accoud_id               policy_type
            attack_types            resource_id
            azure_subscription_id   region
            cloud_provider          scan_name
            cloud_service_keyword   severity
            status                  severity_string
            is_managed              timestamp
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetConfigurationDetectionIDsV2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_ioa_events(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """For CSPM IOA events, gets list of IOA events.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetIOAEvents

        Keyword arguments
        -----------------
        policy_id : str
            Policy ID.
        cloud_provider : str
            Cloud provider. Allowed values: `azure`, `aws`, `gcp`
        account_id : str
            Cloud Account ID (AWS account ID, Azure Subscription ID, etc.)
        aws_account_id : str
            AWS account ID.
        azure_subscription_id : str
            Azure subscription ID.
        azure_tenant_id : str
            Azure tenant ID.
        user_ids : str or list[str]
            User IDs.
        state : str
            State.
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results. Defaults to 100.
        offset : int
            The offset to start retrieving records from. Integer.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIOAEvents",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_ioa_users(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """For CSPM IOA users, gets list of IOA users.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetIOAUsers

        Keyword arguments
        -----------------
        policy_id : str
            Policy ID.
        cloud_provider : str
            Cloud provider. Allowed values: `azure`, `aws`, `gcp`
        account_id : str
            Cloud Account ID (AWS account ID, Azure Subscription ID, etc.)
        aws_account_id : str
            AWS account ID.
        azure_subscription_id : str
            Azure subscription ID.
        azure_tenant_id : str
            Azure tenant ID.
        state : str
            State.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIOAUsers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policy(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Given a policy ID, returns detailed policy information.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMPolicy

        Keyword arguments
        -----------------
        ids : int
            Policy IDs to retrieve.
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
            operation_id="GetCSPMPolicy",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policy_details(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Given an array of policy IDs, returns detailed policies information.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMPoliciesDetails

        Keyword arguments
        -----------------
        ids : str or list[str]
            Policy IDs to retrieve.
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
            operation_id="GetCSPMPoliciesDetails",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policy_settings(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return information about current policy settings.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMPolicySettings

        Keyword arguments
        -----------------
        policy_id : str
            Policy ID.
        cloud_platform : str
            Cloud platform. Allowed values: `azure`, `aws`, `gcp`
        service : str
            Service type to filter policy settings by.
            Available values:
            ACM                          Kinesis
            ACR                          Kubernetes
            AppService                   Lambda
            CloudFormation               LoadBalancer
            CloudTrail                   Monitor
            CloudWatch Logs              NLB/ALB
            Cloudfront                   NetworkSecurityGroup
            Config                       PostgreSQL
            Disk                         RDS
            DynamoDB                     Redshift
            EBS                          S3
            EC2                          SES
            ECR                          SNS
            EFS                          SQLDatabase
            EKS                          SQLServer
            ELB                          SQS
            EMR                          SSM
            Elasticache                  Serverless Application Repository
            GuardDuty                    StorageAccount
            IAM                          Subscriptions
            Identity                     VirtualMachine
            KMS                          VirtualNetwork
            KeyVault
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("cloud_platform", None):
            kwargs["cloud-platform"] = kwargs.get("cloud_platform", None)
        if kwargs.get("policy_id", None):
            kwargs["policy-id"] = kwargs.get("policy_id", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMPolicySettings",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_policy_settings(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a policy setting.

        Can be used to override policy severity or to disable a policy entirely.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/UpdateCSPMPolicySettings

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "resources": [
                        {
                            "account_id": "string",
                            "account_ids": [
                                "string"
                            ],
                            "enabled": boolean,
                            "policy_id": integer,
                            "regions": [
                                "string"
                            ],
                            "severity": "string",
                            "tag_excluded": boolean
                        }
                    ]
                }
        account_id : str
            Account ID to update.
        account_ids : str or list[str]
            Account IDs to update.
        enabled : bool
            Enabled / Disable flag.
        policy_id : int
            Policy ID to be updated.
        region : str or list[str]
            List of regions.
        severity : str
            Severity value to set for policy.
        tag_excluded : bool
            Exclude tags flag.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cspm_policy_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateCSPMPolicySettings",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_scan_schedule(self: object,
                          *args,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return scan schedule configuration for one or more cloud platforms.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMScanSchedule

        Keyword arguments
        -----------------
        cloud_platform : str
            Cloud Platform. String. Allowed Values: `azure`, `aws`, `gcp`
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
        if kwargs.get("cloud_platform", None):
            kwargs["cloud-platform"] = kwargs.get("cloud_platform", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMScanSchedule",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "cloud-platform")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_scan_schedule(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update scan schedule configuration for one or more cloud platforms.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/UpdateCSPMScanSchedule

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "resources": [
                        {
                            "cloud_platform": "string",
                            "next_scan_timestamp": "2021-10-25T05:22:27.365Z",
                            "scan_interval": "string",
                            "scan_schedule": "string"
                        }
                    ]
                }
        cloud_platform : str
            Cloud platform.
        next_scan_timestamp : str
            Time to schedule scan. UTC date formatted.
        scan_interval : str
            Scan interval.
        scan_schedule : str
            Scan schedule type.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = cspm_scan_payload(passed_keywords=kwargs)

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
    UpdateCSPMAzureAccount = update_azure_account
    DeleteCSPMAzureAccount = delete_azure_account
    UpdateCSPMAzureAccountClientID = update_azure_account_client_id
    UpdateCSPMAzureTenantDefaultSubscriptionID = update_azure_tenant_default_subscription_id
    GetCSPMAzureUserScriptsAttachment = get_azure_user_scripts_attachment
    AzureDownloadCertificate = azure_download_certificate
    GetCSPMAzureManagementGroup = get_azure_management_group
    DeleteCSPMAzureManagementGroup = delete_azure_management_group
    AzureRefreshCertificate = azure_refresh_certificate
    CreateCSPMAzureManagementGroup = create_azure_management_group
    GetCSPMCGPAccount = get_gcp_account
    GetCSPMGCPAccount = get_gcp_account
    CreateCSPMGCPAccount = create_gcp_account
    DeleteCSPMGCPAccount = delete_gcp_account
    UpdateCSPMGCPAccount = update_gcp_account
    ConnectCSPMGCPAccount = connect_gcp_account
    GetCSPMGCPValidateAccountsExt = validate_gcp_account
    ValidateCSPMGCPServiceAccountExt = validate_gcp_service_account
    GetCSPMGCPServiceAccountsExt = get_gcp_service_account
    UpdateCSPMGCPServiceAccountsExt = update_gcp_service_account
    GetCSPMGCPUserScriptsAttachment = get_gcp_user_scripts_attachment
    GetBehaviorDetections = get_behavior_detections
    GetConfigurationDetections = get_configuration_detections
    GetConfigurationDetectionEntities = get_configuration_detection_entities
    getCloudEventIDs = get_cloud_event_ids
    GetConfigurationDetectionIDsV2 = get_configuration_detection_ids_v2
    GetIOAEvents = get_ioa_events
    GetIOAUsers = get_ioa_users
    GetCSPMPolicy = get_policy
    GetCSPMPoliciesDetails = get_policy_details
    GetCSPMPolicySettings = get_policy_settings
    UpdateCSPMPolicySettings = update_policy_settings
    GetCSPMScanSchedule = get_scan_schedule
    UpdateCSPMScanSchedule = update_scan_schedule


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
CSPM_Registration = CSPMRegistration  # pylint: disable=C0103
