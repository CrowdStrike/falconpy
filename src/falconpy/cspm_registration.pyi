"""Type stubs for cspm_registration."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CSPMRegistration(ServiceClass):

    def get_aws_account(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        iam_role_arns: Optional[Union[str, List[str]]] = None,
        status: Optional[str] = None,
        limit: Optional[int] = None,
        cspm_lite: Optional[str] = None,
        migrated: Optional[str] = None,
        offset: Optional[int] = None,
        group_by: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_aws_account(
        self,
        *,
        account_id: Optional[str] = None,
        account_type: Optional[str] = None,
        behavior_assessment_enabled: Optional[bool] = None,
        cloudtrail_region: Optional[str] = None,
        deployment_method: Optional[str] = None,
        dspm_enabled: Optional[bool] = None,
        dspm_host_account_id: Optional[str] = None,
        dspm_role: Optional[str] = None,
        falcon_client_id: Optional[str] = None,
        iam_role_arn: Optional[str] = None,
        is_master: Optional[bool] = None,
        organization_id: Optional[str] = None,
        root_stack_id: Optional[str] = None,
        sensor_management_enabled: Optional[bool] = None,
        target_ous: Optional[Union[str, List[str]]] = None,
        use_existing_cloudtrail: Optional[bool] = None,
        vulnerability_scanning_enabled: Optional[bool] = None,
        vulnerability_scanning_host_account_id: Optional[str] = None,
        vulnerability_scanning_role: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_aws_account(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_aws_account(
        self,
        *,
        account_id: Optional[str] = None,
        behavior_assessment_enabled: Optional[bool] = None,
        cloudtrail_region: Optional[str] = None,
        deployment_method: Optional[str] = None,
        dspm_enabled: Optional[bool] = None,
        dspm_role: Optional[str] = None,
        environment: Optional[str] = None,
        falcon_client_id: Optional[str] = None,
        iam_role_arn: Optional[str] = None,
        remediation_region: Optional[str] = None,
        remediation_tou_accepted: Optional[str] = None,
        root_stack_id: Optional[str] = None,
        sensor_management_enabled: Optional[bool] = None,
        target_ous: Optional[Union[str, List[str]]] = None,
        vulnerability_scanning_enabled: Optional[bool] = None,
        vulnerability_scanning_role: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aws_console_setup_urls(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        use_existing_cloudtrail: Optional[str] = None,
        region: Optional[str] = None,
        tags: Optional[str] = None,
        template: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aws_account_scripts_attachment(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        template: Optional[str] = None,
        account_type: Optional[str] = None,
        accounts: Optional[Union[str, List[str]]] = None,
        behavior_assessment_enabled: Optional[str] = None,
        sensor_management_enabled: Optional[str] = None,
        dspm_enabled: Optional[str] = None,
        dspm_regions: Optional[Union[str, List[str]]] = None,
        dspm_role: Optional[str] = None,
        use_existing_cloudtrail: Optional[str] = None,
        organization_id: Optional[str] = None,
        aws_profile: Optional[str] = None,
        custom_role_name: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_azure_account(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        tenant_ids: Optional[Union[str, List[str]]] = None,
        status: Optional[str] = None,
        cspm_lite: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_azure_account(
        self,
        *,
        account_type: Optional[str] = None,
        client_id: Optional[str] = None,
        default_subscription: Optional[bool] = None,
        subscription_id: Optional[str] = None,
        tenant_id: Optional[str] = None,
        years_valid: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_azure_account(
        self,
        *,
        environment: Optional[str] = None,
        subscription_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_azure_account(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        tenant_ids: Optional[Union[str, List[str]]] = None,
        retain_tenant: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_azure_account_client_id(
        self,
        *,
        id: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_azure_tenant_default_subscription_id(
        self,
        *,
        subscription_id: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def azure_download_certificate(
        self,
        *args: Union[str, List[str]],
        tenant_id: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_azure_management_group(
        self,
        *args: Union[str, List[str]],
        tenant_ids: Optional[Union[str, List[str]]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_azure_management_group(
        self,
        *,
        default_subscription_id: Optional[str] = None,
        tenant_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_azure_management_group(
        self,
        *args: Union[str, List[str]],
        tenant_ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def azure_refresh_certificate(
        self,
        *args: Union[str, List[str]],
        tenant_id: Optional[Union[str, List[str]]] = None,
        years_valid: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_azure_user_scripts_attachment(
        self,
        *args: Union[str, List[str]],
        subscription_ids: Optional[Union[str, List[str]]] = None,
        account_type: Optional[str] = None,
        template: Optional[str] = None,
        azure_management_group: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_gcp_account(
        self,
        *,
        parent_type: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        status: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_gcp_account(
        self,
        *,
        parent_id: Optional[str] = None,
        parent_type: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_gcp_account(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_gcp_account(
        self,
        *,
        environment: Optional[str] = None,
        parent_id: Optional[str] = None,
        service_account: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def connect_gcp_account(
        self,
        *,
        client_email: Optional[str] = None,
        client_id: Optional[str] = None,
        parent_id: Optional[str] = None,
        parent_type: Optional[str] = None,
        private_key: Optional[str] = None,
        private_key_id: Optional[str] = None,
        project_id: Optional[str] = None,
        service_account_conditions: Optional[list] = None,
        service_account_id: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def validate_gcp_account(
        self,
        *args: Union[str, List[str]],
        parent_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def validate_gcp_service_account(
        self,
        *,
        client_email: Optional[str] = None,
        client_id: Optional[str] = None,
        private_key: Optional[str] = None,
        private_key_id: Optional[str] = None,
        project_id: Optional[str] = None,
        service_account_conditions: Optional[list] = None,
        service_account_id: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_gcp_service_account(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_gcp_service_account(
        self,
        *,
        client_email: Optional[str] = None,
        client_id: Optional[str] = None,
        private_key: Optional[str] = None,
        private_key_id: Optional[str] = None,
        project_id: Optional[str] = None,
        service_account_conditions: Optional[list] = None,
        service_account_id: Optional[int] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_gcp_user_scripts_attachment(
        self,
        *args: Union[str, List[str]],
        parent_type: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_behavior_detections(
        self,
        *,
        cloud_provider: Optional[str] = None,
        service: Optional[str] = None,
        account_id: Optional[str] = None,
        aws_account_id: Optional[str] = None,
        azure_subscription_id: Optional[str] = None,
        azure_tenant_id: Optional[str] = None,
        state: Optional[str] = None,
        date_time_since: Optional[str] = None,
        since: Optional[str] = None,
        severity: Optional[str] = None,
        next_token: Optional[str] = None,
        limit: Optional[int] = None,
        resource_id: Optional[Union[str, List[str]]] = None,
        resource_uuid: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_configuration_detections(
        self,
        *,
        cloud_provider: Optional[str] = None,
        account_id: Optional[str] = None,
        azure_subscription_id: Optional[str] = None,
        azure_tenant_id: Optional[str] = None,
        status: Optional[str] = None,
        region: Optional[str] = None,
        severity: Optional[str] = None,
        service: Optional[str] = None,
        next_token: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_configuration_detection_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_cloud_event_ids(
        self,
        *,
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_configuration_detection_ids_v2(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        next_token: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_ioa_events(
        self,
        *,
        policy_id: Optional[str] = None,
        cloud_provider: Optional[str] = None,
        account_id: Optional[str] = None,
        aws_account_id: Optional[str] = None,
        azure_subscription_id: Optional[str] = None,
        azure_tenant_id: Optional[str] = None,
        user_ids: Optional[Union[str, List[str]]] = None,
        state: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_ioa_users(
        self,
        *,
        policy_id: Optional[str] = None,
        state: Optional[str] = None,
        cloud_provider: Optional[str] = None,
        account_id: Optional[str] = None,
        aws_account_id: Optional[str] = None,
        azure_subscription_id: Optional[str] = None,
        azure_tenant_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_policy(
        self,
        *args: Union[str, List[str]],
        ids: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_policy_details(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_policy_settings(
        self,
        *,
        service: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_policy_settings(
        self,
        *,
        account_id: Optional[str] = None,
        account_ids: Optional[Union[str, List[str]]] = None,
        enabled: Optional[bool] = None,
        policy_id: Optional[int] = None,
        regions: Optional[Union[str, List[str]]] = None,
        severity: Optional[str] = None,
        tag_excluded: Optional[bool] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scan_schedule(
        self,
        *args: Union[str, List[str]],
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_scan_schedule(
        self,
        *,
        cloud_platform: Optional[str] = None,
        last_scan_completed_at: Optional[str] = None,
        next_scan_timestamp: Optional[str] = None,
        scan_interval: Optional[str] = None,
        scan_schedule: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

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
