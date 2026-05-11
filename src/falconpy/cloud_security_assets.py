"""CrowdStrike Falcon CloudSecurityAssets API interface class.

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
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._cloud_security_assets import _cloud_security_assets_endpoints as Endpoints


class CloudSecurityAssets(ServiceClass):
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
    def combined_application_findings(self: object,
                                      parameters: dict = None,
                                      **kwargs
                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get findings for an application resource with pagination.

        Keyword arguments:
        crn -- Deprecated: Use 'gcrn' instead. Application CRN. String.
        gcrn -- Application GCRN. String.
        type -- Finding type. String.
        filter -- FQL string to filter findings. String.
        offset -- Pagination offset. Integer.
        limit -- Page size. Integer.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-security-assets/cloud-security-assets-combined-application-findings
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_security_assets_combined_application_findings",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_combined_compliance_by_account(self: object,
                                           parameters: dict = None,
                                           **kwargs
                                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get combined compliance data aggregated by account and region.

        Results can be filtered and sorted.

        Keyword arguments:
        filter -- FQL string to filter on asset contents. String.
                  Filterable fields include:
                    account_id                   account_name
                    assessment_id                business_impact
                    cloud_group                  cloud_label
                    cloud_label_id               cloud_provider
                    cloud_scope                  compliant
                    control.benchmark.name       control.benchmark.version
                    control.extension.status     control.framework
                    control.name                 control.type
                    control.version              environment
                    last_evaluated               region
                    resource_gcrn                resource_provider
                    resource_type                resource_type_name
                    service                      service_category
                    severities                   tag_key
                    tag_value                    tags_string
        sort -- FQL formatted sort expression. String.
                    Sort expression in format: field|direction (e.g., last_evaluated|desc).
                    Allowed sort fields:
                        account_id                      last_evaluated
                        account_name                    region
                        assessment_id                   resource_counts.compliant
                        cloud_provider                  resource_counts.non_compliant
                        control.benchmark.name          resource_counts.total
                        control.benchmark.version       resource_provider
                        control.framework               resource_type
                        control.name                    resource_type_name
                        control.type                    service
                        control.version                 service_category
        limit -- The maximum number of items to return. Integer.
                 When not specified or 0, 20 is used. When larger than 10000, 10000 is used.
        offset -- Offset returned controls. Integer.
                  Use only one of 'offset' and 'after' parameter for paginating.
                  'offset' can only be used on offsets < 10,000.
                  For paginating through the entire result set, use 'after' parameter.
        after -- Token-based pagination position. String.
                 Use for paginating through an entire result set.
                 Use only one of 'offset' and 'after' parameters for paginating.
        include_failing_iom_severity_counts -- Include counts of failing IOMs by severity level. Boolean.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
            /cloud-security-assets/cloud-security-assets-combined-compliance-by-account-region-and-resource-type-get
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_security_assets_combined_compliance_by_account",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_assets(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get raw resources based on the provided IDs.

        Keyword arguments:
        ids -- List of assets to return (maximum 100 IDs allowed). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
            /cloud-security-assets/cloud-security-assets-entities-get
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_security_assets_entities_get",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_assets(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a list of resource IDs for the given parameters, filters and sort criteria.

        Keyword arguments:
        after -- Token-based pagination. Use for paginating through an entire result set. String.
                 Use only one of 'offset' and 'after' parameters for paginating.
        filter -- FQL string to filter on asset contents. String.
                  Filterable fields include:
                    account_id                           account_name
                    active                               aspm.deployment_cloud_resource_id
                    aspm.deployment_provider             aspm.deployment_type
                    aspm.technologies                    azure.resource_group
                    azure.vm_id                          business_impact
                    cloud_group                          cloud_label
                    cloud_label_id                       cloud_provider
                    cloud_risks.rule                     cloud_risks.severity
                    cloud_risks.status                   cloud_scope
                    cluster_id                           cluster_name
                    compartment_ocid                     compliant.benchmark_name
                    compliant.benchmark_version          compliant.framework
                    compliant.policy_id                  compliant.requirement
                    compliant.rule                       compliant.section
                    configuration.id                     control.benchmark.name
                    control.benchmark.version            control.framework
                    control.requirement                  control.type
                    control.version                      creation_time
                    cve_ids                              data_classifications.found
                    data_classifications.label           data_classifications.label_id
                    data_classifications.scanned         data_classifications.tag
                    data_classifications.tag_id          environment
                    exprt_ratings                        first_seen
                    highest_severity                     id
                    insights.boolean_value               insights.date_value
                    insights.id                          insights.integer_value
                    insights.string_list_value           insights.string_value
                    instance_id                          instance_state
                    ioa_count                            iom_count
                    legacy_resource_id                   legacy_uuid
                    managed_by                           non_compliant.benchmark_name
                    non_compliant.benchmark_version      non_compliant.framework
                    non_compliant.policy_id              non_compliant.requirement
                    non_compliant.rule                   non_compliant.rule_name
                    non_compliant.section                non_compliant.severity
                    organization_Id                      os_version
                    platform_name                        publicly_exposed
                    region                               resource_gcrn
                    resource_id                          resource_name
                    resource_parent                      resource_type
                    resource_type_name                   sensor_priority
                    service                              service_category
                    severity                             snapshot_detections
                    ssm_managed                          status
                    tag_key                              tag_value
                    tags                                 tags_string
                    tenant_id                            updated_at
                    vmware.guest_os_id                   vmware.guest_os_version
                    vmware.host_system_name              vmware.host_type
                    vmware.instance_uuid                 vmware.vm_host_name
                    vmware.vm_tools_status               zone
        sort -- The field to sort on. String.
                Use `|asc` or `|desc` suffix to specify sort direction.
                Sortable fields include:
                    account_id                      publicly_exposed
                    account_name                    region
                    active                          resource_id
                    cloud_provider                  resource_name
                    cloud_risks.open_risk_count     resource_type
                    cluster_id                      resource_type_name
                    cluster_name                    service
                    creation_time                   service_category
                    data_classifications.found      ssm_managed
                    data_classifications.scanned    status
                    first_seen                      tenant_id
                    id                              updated_at
                    instance_id                     vmware.guest_os_id
                    instance_state                  vmware.guest_os_version
                    ioa_count                       vmware.host_system_name
                    iom_count                       vmware.host_type
                    managed_by                      vmware.instance_uuid
                    organization_Id                 vmware.vm_host_name
                    os_version                      vmware.vm_tools_status
                    platform_name                   zone
                    service_category                tenancy_name
                    compartment_name                tenancy_ocid
                    compartment_ocid                tenancy_type
                    compartment_path                aspm.deployment_cloud_resource_id
                    aspm.deployment_provider        aspm.deployment_type
                    aspm.technologies               publiclyExposedToTheInternet
                    publiclyExposedAccessRange      publiclyExposedExposureMethod
        limit -- The maximum number of items to return. Integer.
                 When not specified or 0, 500 is used. When larger than 1000, 1000 is used.
        offset -- Offset returned assets. Use only one of 'offset' and 'after' parameter for paginating. Integer.
                  'offset' can only be used on offsets < 10,000.
                  For paginating through the entire result set, use 'after' parameter.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/cloud-security-assets/cloud-security-assets-queries
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="cloud_security_assets_queries",
            keywords=kwargs,
            params=parameters
            )

    cloud_security_assets_combined_application_findings = combined_application_findings
    cloud_security_assets_combined_compliance_by_account = get_combined_compliance_by_account
    cloud_security_assets_entities_get = get_assets
    cloud_security_assets_queries = query_assets
