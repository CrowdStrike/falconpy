"""CrowdStrike Falcon CloudAzureRegistration API interface class.

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
    cloud_azure_registration_payload,
    cloud_azure_registration_create_payload,
    generic_payload_list,
    cloud_azure_registration_legacy_payload,
    cloud_registration_azure_create_suppressions_payload,
    cloud_registration_azure_update_suppressions_payload,
    )
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._cloud_azure_registration import _cloud_azure_registration_endpoints as Endpoints


class CloudAzureRegistration(ServiceClass):
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

    @force_default(defaults=["body"], default_types=["dict"])
    def delete_legacy_subscription(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete existing legacy Azure subscriptions.

        Keyword arguments:
        body -- Full body payload as a dictionary. Not required if using other keywords.
                {
                    "resources": [
                        {
                            "retain_client": true,
                            "subscription_id": "string",
                            "tenant_id": "string"
                        }
                    ]
                }
        retain_client -- Boolean.
        subscription_id -- String.
        tenant_id -- String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud-registration-azure-delete-legacy-subscription
        """
        if not body:
            body = cloud_azure_registration_legacy_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_delete_legacy_subscription",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def health_check(self: object, *args, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Trigger health check scan for Azure registrations.

        Keyword arguments:
        tenant_ids -- Azure tenant IDs. String or list of string.
        body -- Full body payload as a dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'tenant_ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud-registration-azure-trigger-health-check
        """
        kwargs = handle_single_argument(args, kwargs, "tenant_ids")
        if not body:
            body = generic_payload_list(submitted_keywords=kwargs, payload_value="tenant_ids")

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_trigger_health_check",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_registration(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve existing Azure registration for a tenant.

        Keyword arguments:
        tenant_id -- Tenant ID to retrieve. String.
        registration_id -- Registration ID. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud-registration-azure-get-registration
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_get_registration",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_registration(self: object,
                            body: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create an Azure registration for a tenant.

        Keyword arguments:
        body -- Full body payload as a JSON dictionary. Not required if using other keywords.
                {
                    "resource": {
                        "account_type": "string",
                        "additional_features": [
                            {
                                "feature": "string",
                                "product": "string",
                                "subscription_ids": [
                                    "string"
                                ]
                            }
                        ],
                        "additional_properties": {},
                        "api_client_key_id": "string",
                        "api_client_key_type": "string",
                        "cs_infra_region": "string",
                        "cs_infra_subscription_id": "string",
                        "deployment_method": "string",
                        "deployment_stack_host_id": "string",
                        "deployment_stack_name": "string",
                        "dspm_regions": [
                            "string"
                        ],
                        "environment": "string",
                        "event_hub_settings": [
                            {
                                "cid": "string",
                                "consumer_group": "string",
                                "event_hub_id": "string",
                                "purpose": "string",
                                "tenant_id": "string"
                            }
                        ],
                        "management_group_ids": [
                            "string"
                        ],
                        "microsoft_graph_permission_ids": [
                            "string"
                        ],
                        "microsoft_graph_permission_ids_readonly": true,
                        "products": [
                        {
                            "features": [
                                "string"
                            ],
                            "product": "string"
                        }
                        ],
                        "resource_name_prefix": "string",
                        "resource_name_suffix": "string",
                        "status": "string",
                        "subscription_ids": [
                            "string"
                        ],
                        "tags": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "template_version": "string",
                        "tenant_id": "string"
                    }
                }
            account_type -- Azure account type. String.
            additional_features -- Additional features. List of dictionaries.
            additional_properties -- Additional properties. Dictionary.
            api_client_key_id -- Azure API client key ID. String.
            api_client_key_type -- Azure API client key type. String.
            cs_infra_region -- CrowdStrike infrastructure region. String.
            cs_infra_subscription_id -- CrowdStrike infrastructure subscription ID. String.
            deployment_method -- Deployment method. String.
            deployment_stack_host_id -- Azure deployment stack host ID. String.
            deployment_stack_name -- Azure deployment stack name. String.
            dspm_regions -- DSPM regions. String or list of strings.
            environment -- Azure environment. String.
            event_hub_settings -- Azure Event Hub settings. List of dictionaries.
            management_group_ids -- Azure management group IDs. String or list of strings.
            microsoft_graph_permission_ids -- Microsoft Graph permission IDs. String or list of strings.
            microsoft_graph_permissions_ids_readonly -- Flag indicating if Microsoft Graph permission IDs
                                                        are read-only. Boolean.
            products -- Products. List of dictionaries.
            resource_name_prefix -- Resource naming prefix. String.
            resource_name_suffix -- Resource naming suffix. String.
            status -- Registration status. String.
            subscription_ids -- Azure subscription IDs. String or list of strings.
            tags -- Additional tags. Dictionary.
            template_version -- Deployment template version. String.
            tenant_id -- Azure tenant ID. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud-registration-azure-create-registration
        """
        if not body:
            body = cloud_azure_registration_create_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_create_registration",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_registration(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an existing Azure registration for a tenant.

        Keyword arguments:
        body -- Full body payload as a JSON dictionary. Not required if using other keywords.
                {
                    "resource": {
                        "account_type": "string",
                        "additional_features": [
                            {
                                "feature": "string",
                                "product": "string",
                                "subscription_ids": [
                                    "string"
                                ]
                            }
                        ],
                        "additional_properties": {},
                        "api_client_key_id": "string",
                        "api_client_key_type": "string",
                        "cs_infra_region": "string",
                        "cs_infra_subscription_id": "string",
                        "deployment_method": "string",
                        "deployment_stack_host_id": "string",
                        "deployment_stack_name": "string",
                        "dspm_regions": [
                            "string"
                        ],
                        "environment": "string",
                        "event_hub_settings": [
                            {
                                "cid": "string",
                                "consumer_group": "string",
                                "event_hub_id": "string",
                                "purpose": "string",
                                "tenant_id": "string"
                            }
                        ],
                        "management_group_ids": [
                            "string"
                        ],
                        "microsoft_graph_permission_ids": [
                            "string"
                        ],
                        "microsoft_graph_permission_ids_readonly": true,
                        "products": [
                            {
                                "features": [
                                    "string"
                                ],
                                "product": "string"
                            }
                        ],
                        "resource_name_prefix": "string",
                        "resource_name_suffix": "string",
                        "status": "string",
                        "subscription_ids": [
                            "string"
                        ],
                        "tags": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "template_version": "string",
                        "tenant_id": "string"
                    }
                }
            account_type -- Azure account type. String.
            additional_features -- Additional features. List of dictionaries.
            additional_properties -- Additional properties. Dictionary.
            api_client_key_id -- Azure API client key ID. String.
            api_client_key_type -- Azure API client key type. String.
            cs_infra_region -- CrowdStrike infrastructure region. String.
            cs_infra_subscription_id -- CrowdStrike infrastructure subscription ID. String.
            deployment_method -- Deployment method. String.
            deployment_stack_host_id -- Azure deployment stack host ID. String.
            deployment_stack_name -- Azure deployment stack name. String.
            dspm_regions -- DSPM regions. String or list of strings.
            environment -- Azure environment. String.
            event_hub_settings -- Azure Event Hub settings. List of dictionaries.
            management_group_ids -- Azure management group IDs. String or list of strings.
            microsoft_graph_permission_ids -- Microsoft Graph permission IDs. String or list of strings.
            microsoft_graph_permissions_ids_readonly -- Flag indicating if Microsoft Graph permission IDs
                                                        are read-only. Boolean.
            products -- Products. List of dictionaries.
            resource_name_prefix -- Resource naming prefix. String.
            resource_name_suffix -- Resource naming suffix. String.
            status -- Registration status. String.
            subscription_ids -- Azure subscription IDs. String or list of strings.
            tags -- Additional tags. Dictionary.
            template_version -- Deployment template version. String.
            tenant_id -- Azure tenant ID. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud-registration-azure-delete-registration
        """
        if not body:
            body = cloud_azure_registration_create_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_update_registration",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_registration(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete existing Azure registrations.

        Keyword arguments:
        tenant_ids -- Azure tenant IDs to be removed. String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud-registration-azure-delete-registration
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_delete_registration",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def deployment_script(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download Azure deployment script (Terraform or Bicep).

        DECOMMISSIONED: This operation is no longer available in CrowdStrike's API.
        Calling this method will result in an error from the API.


        Keyword arguments:
        tenant_id -- Azure tenant ID to retrieve deployment scripts for. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/download_azure_script
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="download_azure_script",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def download_script(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve script to create resources.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "resources": [
                        {
                            "tenantId": "string"
                        }
                    ]
                }
        tenant_id -- Azure Tenant ID. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud-registration-azure-download-script
        """
        if not body:
            body = cloud_azure_registration_payload(kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_download_script",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def validate_registration(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Validate an Azure registration by checking service principal, role assignments and deployment stack.

        Keyword arguments:
        tenant_id -- Azure tenant ID to be validated. String.
        stack_name -- Azure deployment stack name to be validated. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud-registration-azure-validate-registration
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_validate_registration",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def cloud_registration_azure_create_suppressions(self: object,
                                                     body: dict = None,
                                                     **kwargs
                                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create new issue suppression rules.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "resources": [
                        {
                            "reason": "string",
                            "registration_id": "string",
                            "target": {
                                "entity_id": "string",
                                "entity_type": "string",
                                "issue_name": "string"
                            },
                            "type": "string"
                        }
                    ]
                }
        resources -- The resources value. List.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud_registration_azure_create_suppressions
        """
        if not body:
            body = cloud_registration_azure_create_suppressions_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_create_suppressions",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def cloud_registration_azure_delete_suppressions(self: object,
                                                     parameters: dict = None,
                                                     **kwargs
                                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Remove/revoke suppression rules.

        Keyword arguments:
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud_registration_azure_delete_suppressions
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_delete_suppressions",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def cloud_registration_azure_get_issue_suppression_values_by_field(self: object,
                                                                       parameters: dict = None,
                                                                       **kwargs
                                                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve distinct filterable values for issue suppression fields.

        Keyword arguments:
        registration_id -- Registration ID to filter values by. String.
        field -- Field to get values for. Available values: issue_name, entity_id, suppressed_by, created_at, reason. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud_registration_azure_get_issue_suppression_values_by_field
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_get_issue_suppression_values_by_field",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def cloud_registration_azure_get_issue_values_by_field(self: object,
                                                           parameters: dict = None,
                                                           **kwargs
                                                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve distinct filterable values for issue fields.

        Keyword arguments:
        registration_id -- Registration ID to filter values by. String.
        filter -- FQL (Falcon Query Language) string for filtering results. Allowed filters are
                  name,issue,severity,category,impact,entity_type,entity_id,entity_name,status. String.
        field -- Field to get values for. Available values: issue, name, severity, category, impact, entity_type, entity_id,
                 entity_name, status, feature. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud_registration_azure_get_issue_values_by_field
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_get_issue_values_by_field",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def cloud_registration_azure_get_issues(self: object,
                                            parameters: dict = None,
                                            **kwargs
                                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve issues for Azure registrations.

        Keyword arguments:
        registration_id -- Registration ID. String.
        filter -- FQL (Falcon Query Language) string for filtering results. Allowed filters are
                  name,issue,severity,category,impact,entity_type,entity_id,entity_name,status. String.
        sort -- Field and direction for sorting results - allowed sort fields are
                issue,name,severity,category,impact,entity_type,entity_id,entity_name,impacted_entities. String.
        group_by -- Grouping method: 'name' (optional, default: ungrouped). Available values: name. String.
        limit -- Maximum number of records to return (default: 100, max: 1000). Integer.
        offset -- Starting index of result. Integer.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud_registration_azure_get_issues
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_get_issues",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def cloud_registration_azure_get_script(self: object,
                                            parameters: dict = None,
                                            **kwargs
                                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Download Azure deployment script (Terraform or Bicep).

        Keyword arguments:
        tenant_id -- Azure tenant ID. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud_registration_azure_get_script
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_get_script",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def cloud_registration_azure_get_script_versions(self: object,
                                                     parameters: dict = None,
                                                     **kwargs
                                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve all available script versions with filtering and sorting.

        Keyword arguments:
        deployment_method -- Filter by deployment method (e.g., 'bicep-legacy', 'bicep-deployment-stack'). String.
        sort -- Field and direction for sorting results - allowed sort fields are version,deployment_method,published_date
                String.
        limit -- Maximum number of records to return (default: 100, max: 1000). Integer.
        offset -- Starting index of result. Integer.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud_registration_azure_get_script_versions
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_get_script_versions",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def cloud_registration_azure_get_suppressions(self: object,
                                                  parameters: dict = None,
                                                  **kwargs
                                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve existing suppression rules with filtering.

        Keyword arguments:
        registration_id -- Registration ID. String.
        filter -- FQL (Falcon Query Language) string for filtering results. Allowed filters are
                  issue_name,entity_id,suppressed_by,created_at,reason. String.
        sort -- Field and direction for sorting results - allowed sort fields are
                issue_name,entity_id,suppressed_by,created_at,reason. String.
        limit -- Maximum number of records to return (default: 100, max: 1000). Integer.
        offset -- Starting index of result. Integer.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud_registration_azure_get_suppressions
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_get_suppressions",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def cloud_registration_azure_update_suppressions(self: object,
                                                     body: dict = None,
                                                     **kwargs
                                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update existing suppression rules.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "resources": [
                        {
                            "reason": "string",
                            "suppression_id": "string"
                        }
                    ]
                }
        resources -- The resources value. List.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-azure-registration/cloud_registration_azure_update_suppressions
        """
        if not body:
            body = cloud_registration_azure_update_suppressions_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_registration_azure_update_suppressions",
            body=body
            )

    cloud_registration_azure_create_suppressions = cloud_registration_azure_create_suppressions
    cloud_registration_azure_delete_legacy_subscription = delete_legacy_subscription
    cloud_registration_azure_delete_suppressions = cloud_registration_azure_delete_suppressions
    cloud_registration_azure_get_issue_suppression_values_by_field = \
        cloud_registration_azure_get_issue_suppression_values_by_field
    cloud_registration_azure_get_issue_values_by_field = cloud_registration_azure_get_issue_values_by_field
    cloud_registration_azure_get_issues = cloud_registration_azure_get_issues
    cloud_registration_azure_get_script = cloud_registration_azure_get_script
    cloud_registration_azure_get_script_versions = cloud_registration_azure_get_script_versions
    cloud_registration_azure_get_suppressions = cloud_registration_azure_get_suppressions
    cloud_registration_azure_trigger_health_check = health_check
    cloud_registration_azure_get_registration = get_registration
    cloud_registration_azure_create_registration = create_registration
    cloud_registration_azure_update_registration = update_registration
    cloud_registration_azure_delete_registration = delete_registration
    cloud_registration_azure_update_suppressions = cloud_registration_azure_update_suppressions
    download_azure_script = deployment_script
    cloud_registration_azure_download_script = download_script
    cloud_registration_azure_validate_registration = validate_registration
