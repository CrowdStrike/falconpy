"""Type stubs for d4c_registration."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class D4CRegistration(ServiceClass):

    def get_aws_account(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        status: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        migrated: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_aws_account(
        self,
        *,
        account_id: Optional[str] = None,
        account_type: Optional[str] = None,
        cloudtrail_region: Optional[str] = None,
        iam_role_arn: Optional[str] = None,
        is_master: Optional[bool] = None,
        organization_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_aws_account(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aws_console_setup(
        self,
        *args: Union[str, List[str]],
        region: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aws_account_scripts(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        template: Optional[str] = None,
        accounts: Optional[Union[str, List[str]]] = None,
        behavior_assessment_enabled: Optional[str] = None,
        sensor_management_enabled: Optional[str] = None,
        dspm_enabled: Optional[str] = None,
        dspm_regions: Optional[Union[str, List[str]]] = None,
        dspm_host_account_id: Optional[str] = None,
        dspm_host_integration_role_name: Optional[str] = None,
        dspm_host_scanner_role_name: Optional[str] = None,
        dspm_role: Optional[str] = None,
        vulnerability_scanning_enabled: Optional[str] = None,
        vulnerability_scanning_regions: Optional[Union[str, List[str]]] = None,
        vulnerability_scanning_host_account_id: Optional[str] = None,
        vulnerability_scanning_host_integration_role_name: Optional[str] = None,
        vulnerability_scanning_host_scanner_role_name: Optional[str] = None,
        vulnerability_scanning_role: Optional[str] = None,
        use_existing_cloudtrail: Optional[str] = None,
        organization_id: Optional[str] = None,
        organizational_unit_ids: Optional[Union[str, List[str]]] = None,
        aws_profile: Optional[str] = None,
        aws_region: Optional[str] = None,
        iam_role_arn: Optional[str] = None,
        falcon_client_id: Optional[str] = None,
        idp_enabled: Optional[str] = None,
        tags: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_azure_account(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        tenant_ids: Optional[Union[str, List[str]]] = None,
        status: Optional[str] = None,
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

    def update_azure_account_client_id(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        object_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_azure_user_scripts_attachment(
        self,
        *,
        subscription_ids: Optional[Union[str, List[str]]] = None,
        template: Optional[str] = None,
        azure_management_group: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_azure_user_scripts(
        self,
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

    def get_gcp_user_scripts_attachment_v2(
        self,
        *args: Union[str, List[str]],
        parent_type: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        status: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def azure_download_certificate(
        self,
        *args: Union[str, List[str]],
        tenant_id: Optional[Union[str, List[str]]] = None,
        refresh: Optional[bool] = None,
        years_valid: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_azure_tenant_ids(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_gcp_user_scripts(
        self,
        *args: Union[str, List[str]],
        parent_type: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aws_horizon_scripts(
        self,
        *,
        single_account: Optional[str] = None,
        delete: Optional[str] = None,
        account_type: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

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
    GetCSPMGCPAccount = get_gcp_account
    GetCSPMCGPAccount = get_gcp_account
    GetD4CGCPAccount = get_gcp_account
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
