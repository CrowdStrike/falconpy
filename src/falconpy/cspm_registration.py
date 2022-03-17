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
# pylint: disable=R0904  # Matching API operation counts
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import cspm_registration_payload, cspm_policy_payload, cspm_scan_payload
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
    def get_aws_account(self: object, parameters: dict = None, **kwargs) -> dict:
        """Return information about the current status of an AWS account.

        Keyword arguments:
        scan_type -- Type of scan, `dry` or `full`, to perform on selected accounts
        ids -- AWS account IDs. String or list of strings.
        organization_ids -- AWS organization IDs. String or list of strings.
        limit -- The maximum number of records to return in this response. [Integer, 1-1000]
                 Use with the offset parameter to manage pagination of results. Defaults to 100.
        offset -- The offset to start retrieving records from. Integer.
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.
        status -- Account status to filter results by. String.
        group_by -- Field to group by. String. (Only acceptable value: `organization`)

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAwsAccount
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
    def create_aws_account(self: object, body: dict = None, **kwargs) -> dict:
        """Register a new AWS account.

        Creates a new account in our system for a customer and generates a script
        to run in their AWS cloud environment to grant CrowdStrike Horizon access.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "resources": [
                        {
                            "account_id": "string",
                            "cloudtrail_region": "string",
                            "organization_id": "string"
                        }
                    ]
                }
        account_id -- AWS Account ID. String.
        cloudtrail_region -- AWS Cloudtrail Region. String.
        organization_id -- AWS Organization ID. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/CreateCSPMAwsAccount
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
    def delete_aws_account(self: object, parameters: dict = None, **kwargs) -> dict:
        """Delete an existing AWS Account or Organization by specifying their IDs.

        Keyword arguments:
        ids -- AWS Account IDs to remove. String or list of strings.
        organization_ids -- AWS Organization IDs to be removed. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/DeleteCSPMAwsAccount
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
    def update_aws_account(self: object, body: dict = None, **kwargs) -> dict:
        """Patches a existing account in our system for a customer.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "resources": [
                        {
                            "account_id": "string",
                            "cloudtrail_region": "string"
                        }
                    ]
                }
        account_id -- AWS Account ID. String.
        cloudtrail_region -- AWS Cloudtrail Region. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/PatchCSPMAwsAccount
        """
        if not body:
            body = cspm_registration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PatchCSPMAwsAccount",
            body=body
            )

    def get_aws_console_setup_urls(self: object) -> dict:
        """Retrieve setup URLs for the AWS console.

        Returns a URL for customers to visit in their cloud environment
        to grant access to CrowdStrike.

        This method does not accept arguments or keywords.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAwsConsoleSetupURLs
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAwsConsoleSetupURLs"
            )

    def get_aws_account_scripts_attachment(self: object) -> dict:
        """Retrieve AWS account scripts.

        Return a script for customers to run in their cloud environment
        to grant access to CrowdStrike for their AWS environment.

        This method does not accept arguments or keywords.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAwsAccountScriptsAttachment
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAwsAccountScriptsAttachment"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_azure_account(self: object, parameters: dict = None, **kwargs) -> dict:
        """Return information about Azure account registration.

        Keyword arguments:
        scan_type -- Type of scan, `dry` or `full`, to perform on selected accounts
        ids -- Azure account IDs. String or list of strings.
        limit -- The maximum number of records to return in this response. [Integer, 1-1000]
                 Use with the offset parameter to manage pagination of results. Defaults to 100.
        offset -- The offset to start retrieving records from. Integer.
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.
        status -- Account status to filter results by. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAzureAccount
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
    def create_azure_account(self: object, body: dict = None, **kwargs) -> dict:
        """Register new Azure account.

        Creates a new account in our system for a customer and generates a script
        to run in their cloud environment to grant CrowdStrike Horizon access.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "resources": [
                        {
                            "tenant_id": "string",
                            "subscription_id": "string"
                        }
                    ]
                }
        tenant_id -- Azure Tenant ID. String.
        subscription_id -- Azure Subscription ID. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/CreateCSPMAzureAccount
        """
        if not body:
            body = cspm_registration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateCSPMAzureAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_azure_account(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Delete an existing Azure Subscription by specifying their IDs.

        Keyword arguments:
        ids -- List of Azure Subscription IDs to delete. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/DeleteCSPMAzureAccount
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
                                       ) -> dict:
        """Update Azure account Client ID.

        Update an Azure service account in our system with the
        user-created client_id created with the public key we've provided.

        Keyword arguments:
        body -- There are no body payload parameters. This field is not used. Ignore.
        id -- List of Azure Subscription IDs to delete. String or list of strings.
        tenant_id -- Azure Tenant ID to update client ID for.
                     Required if multiple tenants are registered.
        parameters -- full parameters payload, not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/UpdateCSPMAzureAccountClientID
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
                                                    ) -> dict:
        """Update default subscription ID.

        Update an Azure service account in our system with the
        user-created client_id created with the public key we've provided.

        Keyword arguments:
        body -- There are no body payload parameters. This field is not used. Ignore.
        subscription_id -- Default Subscription ID to patch for all subscriptions
                           belonging to the tenant. String.
        tenant_id -- Azure Tenant ID to update client ID for.
                     Required if multiple tenants are registered.
        parameters -- full parameters payload, not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
                /cspm-registration/UpdateCSPMAzureTenantDefaultSubscriptionID
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
    def get_azure_user_scripts_attachment(self: object,
                                          *args,
                                          parameters: dict = None,
                                          **kwargs
                                          ) -> dict:
        """
        Retrieve Azure user script.

        Return a script for customers to run in their cloud environment
        to grant access to CrowdStrike for their Azure environment.

        Keyword arguments:
        tenant_id -- Azure Tenant ID to generate script for.
                     Defaults to the most recently registered tenant.
        parameters -- full parameters payload, not required if tenant-id keyword is used.

        Arguments: When not specified, the first argument to this method is assumed to be
                   'tenant-id'. All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMAzureUserScriptsAttachment
        """
        if kwargs.get("tenant_id", None):
            kwargs["tenant-id"] = kwargs.get("tenant_id", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMAzureUserScriptsAttachment",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "tenant-id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_behavior_detections(self: object, parameters: dict = None, **kwargs) -> dict:
        """Retrieve list of detected behaviors.

        Keyword arguments:
        account_id -- Cloud Account ID (AWS account ID, Azure Subscription ID, etc.)
        aws_account_id -- AWS account ID. String.
        azure_subscription_id -- Azure subscription ID. String.
        azure_tenant_id -- Azure tenant ID. String.
        cloud_provider -- Cloud provider. Allowed values: `azure`, `aws`, `gcp`. String.
        date_time_since -- Filter to retrieve all events after this date. RFC3339 formatted string.
                           Example: 2006-01-01T12:00:01Z07:00
        limit -- The maximum number of records to return in this response. [Integer, 1-500]
        next_token -- String to get next page of results, associated with the previous
                      execution. Must include all filters from previous execution. String.
        service -- Cloud Service (Example: `EC2` or `S3`). String.
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
        severity -- Severity (e.g. `High`, `Medium` or `Informational`). String.
        state -- State. (e.g. `open` or `closed`). String.
        parameters - full parameters payload, not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetBehaviorDetections
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetBehaviorDetections",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_configuration_detections(self: object, parameters: dict = None, **kwargs) -> dict:
        """Retrieve list of active misconfigurations.

        Keyword arguments:
        account_id -- Cloud Account ID (AWS account ID, Azure Subscription ID, etc.)
        aws_account_id -- AWS account ID. String.
        azure_subscription_id -- Azure subscription ID. String.
        azure_tenant_id -- Azure tenant ID. String.
        cloud_provider -- Cloud provider. Allowed values: `azure`, `aws`, `gcp`. String.
        limit -- The maximum number of records to return in this response. [Integer, 1-500]
        next_token -- String to get next page of results, associated with the previous
                      execution. Cannot be combined with any filter except `limit`. String.
        region -- Cloud Provider Region (Example: `us-east-1`). String.
        service -- Cloud Service (Example: `EC2` or `S3`). String.
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
        severity -- Severity (e.g. `High`, `Medium` or `Informational`). String.
        status -- Status (e.g. `new`, `reoccurring`, or `all`). String.
        parameters - full parameters payload, not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetConfigurationDetections
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetConfigurationDetections",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_ioa_events(self: object, parameters: dict = None, **kwargs) -> dict:
        """For CSPM IOA events, gets list of IOA events.

        Keyword arguments:
        policy_id -- Policy ID. String.
        cloud_provider -- Cloud provider. Allowed values: `azure`, `aws`, `gcp`. String.
        account_id -- Cloud Account ID (AWS account ID, Azure Subscription ID, etc.)
        aws_account_id -- AWS account ID. String.
        azure_subscription_id -- Azure subscription ID. String.
        azure_tenant_id -- Azure tenant ID. String.
        user_ids -- User IDs. String or list of strings.
        state -- State. String.
        limit -- The maximum number of records to return in this response. [Integer, 1-500]
                 Use with the offset parameter to manage pagination of results. Defaults to 100.
        offset -- The offset to start retrieving records from. Integer.
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetIOAEvents
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIOAEvents",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_ioa_users(self: object, parameters: dict = None, **kwargs) -> dict:
        """For CSPM IOA users, gets list of IOA users.

        Keyword arguments:
        policy_id -- Policy ID. String.
        cloud_provider -- Cloud provider. Allowed values: `azure`, `aws`, `gcp`. String.
        account_id -- Cloud Account ID (AWS account ID, Azure Subscription ID, etc.)
        aws_account_id -- AWS account ID. String.
        azure_subscription_id -- Azure subscription ID. String.
        azure_tenant_id -- Azure tenant ID. String.
        state -- State. String.
        parameters - full parameters payload, not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetIOAUsers
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIOAUsers",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policy(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Given a policy ID, returns detailed policy information.

        Keyword arguments:
        ids -- Policy IDs to retrieve. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMPolicy
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCSPMPolicy",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_policy_settings(self: object, parameters: dict = None, **kwargs) -> dict:
        """Return information about current policy settings.

        Keyword arguments:
        policy_id -- Policy ID. String.
        cloud_platform -- Cloud platform. Allowed values: `azure`, `aws`, `gcp`. String.
        service -- Service type to filter policy settings by.
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
        parameters - full parameters payload, not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMPolicySettings
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
    def update_policy_settings(self: object, body: dict = None, **kwargs) -> dict:
        """Update a policy setting.

        Can be used to override policy severity or to disable a policy entirely.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "resources": [
                        {
                            "account_id": "string",
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
        account_id -- Account ID to update. String.
        enabled -- Enabled / Disable flag. Boolean.
        policy_id -- Policy ID to be updated. Integer.
        region -- List of regions. String or list of strings.
        severity -- Severity value to set for policy. String.
        tag_excluded -- Exclude tags flag. Boolean.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/UpdateCSPMPolicySettings
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
    def get_scan_schedule(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Return scan schedule configuration for one or more cloud platforms.

        Keyword arguments:
        cloud_platform -- Cloud Platform. String. Allowed Values: `azure`, `aws`, `gcp`
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/GetCSPMScanSchedule
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
    def update_scan_schedule(self: object, body: dict = None, **kwargs) -> dict:
        """Update scan schedule configuration for one or more cloud platforms.

        Keyword arguments:
        body -- full body payload, not required when using other keywords.
                {
                    "resources": [
                        {
                            "cloud_platform": "string",
                            "next_scan_timestamp": "2021-10-25T05:22:27.365Z",
                            "scan_schedule": "string"
                        }
                    ]
                }
        cloud_platform -- Cloud platform. String.
        next_scan_timestamp -- Time to schedule scan. UTC date formatted string.
        scan_schedule -- Scan schedule type. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cspm-registration/UpdateCSPMScanSchedule
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
    DeleteCSPMAzureAccount = delete_azure_account
    UpdateCSPMAzureAccountClientID = update_azure_account_client_id
    UpdateCSPMAzureTenantDefaultSubscriptionID = update_azure_tenant_default_subscription_id
    GetCSPMAzureUserScriptsAttachment = get_azure_user_scripts_attachment
    GetBehaviorDetections = get_behavior_detections
    GetConfigurationDetections = get_configuration_detections
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
