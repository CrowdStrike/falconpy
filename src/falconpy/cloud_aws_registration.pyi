"""Type stubs for cloud_aws_registration."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CloudAWSRegistration(ServiceClass):

    def trigger_health_check(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_accounts(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_account(
        self,
        *,
        account_id: Optional[str] = None,
        account_type: Optional[str] = None,
        cloudformation_stack_arn: Optional[str] = None,
        cloudtrail_region: Optional[str] = None,
        csp_events: Optional[bool] = None,
        deployment_method: Optional[str] = None,
        dspm_custom_vpc_configuration: Optional[dict] = None,
        dspm_host_account_id: Optional[str] = None,
        dspm_network_configuration_type: Optional[str] = None,
        dspm_regions: Optional[Union[str, List[str]]] = None,
        dspm_role: Optional[str] = None,
        dspm_service_permissions_override: Optional[Union[str, List[str]]] = None,
        falcon_client_id: Optional[str] = None,
        iam_role_arn: Optional[str] = None,
        ioa_regions: Optional[Union[str, List[str]]] = None,
        is_master: Optional[bool] = None,
        log_ingestion_method: Optional[str] = None,
        organization_id: Optional[str] = None,
        products: Optional[list] = None,
        resource_name_prefix: Optional[str] = None,
        resource_name_suffix: Optional[str] = None,
        root_stack_id: Optional[str] = None,
        s3_log_ingestion_bucket_name: Optional[str] = None,
        s3_log_ingestion_bucket_prefix: Optional[str] = None,
        s3_log_ingestion_kms_key_arn: Optional[str] = None,
        s3_log_ingestion_sns_topic_arn: Optional[str] = None,
        target_ous: Optional[Union[str, List[str]]] = None,
        use_existing_cloudtrail: Optional[bool] = None,
        vulnerability_scanning_custom_vpc_configuration: Optional[dict] = None,
        vulnerability_scanning_host_account_id: Optional[str] = None,
        vulnerability_scanning_network_configuration_type: Optional[str] = None,
        vulnerability_scanning_regions: Optional[Union[str, List[str]]] = None,
        vulnerability_scanning_role: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_account(
        self,
        *,
        account_id: Optional[str] = None,
        cloudformation_stack_arn: Optional[str] = None,
        cloudtrail_region: Optional[str] = None,
        csp_events: Optional[bool] = None,
        disable_products: Optional[list] = None,
        dspm_custom_vpc_configuration: Optional[dict] = None,
        dspm_host_account_id: Optional[str] = None,
        dspm_network_configuration_type: Optional[str] = None,
        dspm_regions: Optional[Union[str, List[str]]] = None,
        dspm_role: Optional[str] = None,
        dspm_service_permissions_override: Optional[Union[str, List[str]]] = None,
        falcon_client_id: Optional[str] = None,
        ioa_regions: Optional[Union[str, List[str]]] = None,
        log_ingestion_method: Optional[str] = None,
        organization_id: Optional[str] = None,
        products: Optional[list] = None,
        reader_role_arn: Optional[str] = None,
        remediation_region: Optional[str] = None,
        remediation_tou_accepted: Optional[str] = None,
        resource_name_prefix: Optional[str] = None,
        resource_name_suffix: Optional[str] = None,
        s3_log_ingestion_bucket_name: Optional[str] = None,
        s3_log_ingestion_bucket_prefix: Optional[str] = None,
        s3_log_ingestion_kms_key_arn: Optional[str] = None,
        s3_log_ingestion_sns_topic_arn: Optional[str] = None,
        target_ous: Optional[Union[str, List[str]]] = None,
        use_existing_cloudtrail: Optional[bool] = None,
        vulnerability_scanning_custom_vpc_configuration: Optional[dict] = None,
        vulnerability_scanning_host_account_id: Optional[str] = None,
        vulnerability_scanning_network_configuration_type: Optional[str] = None,
        vulnerability_scanning_regions: Optional[Union[str, List[str]]] = None,
        vulnerability_scanning_role: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_account(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def validate_accounts(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_accounts(
        self,
        *,
        products: Optional[Union[str, List[str]]] = None,
        features: Optional[Union[str, List[str]]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        group_by: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    cloud_registration_aws_trigger_health_check = trigger_health_check
    cloud_registration_aws_get_accounts = get_accounts
    cloud_registration_aws_create_account = create_account
    cloud_registration_aws_update_account = update_account
    cloud_registration_aws_delete_account = delete_account
    cloud_registration_aws_validate_accounts = validate_accounts
    cloud_registration_aws_query_accounts = query_accounts
