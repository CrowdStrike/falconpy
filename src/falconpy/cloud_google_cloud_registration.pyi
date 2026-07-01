"""Type stubs for cloud_google_cloud_registration."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CloudGoogleCloudRegistration(ServiceClass):

    def get_entities(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def trigger_health_check(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_registration(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_registration(
        self,
        *,
        additional_properties: Optional[dict] = None,
        deployment_method: Optional[str] = None,
        dspm_settings: Optional[dict] = None,
        entity_id: Optional[Union[str, List[str]]] = None,
        excluded_project_patterns: Optional[Union[str, List[str]]] = None,
        falcon_client_key_id: Optional[str] = None,
        falcon_client_key_type: Optional[str] = None,
        infra_manager_region: Optional[str] = None,
        infra_project_id: Optional[str] = None,
        labels: Optional[dict] = None,
        products: Optional[list] = None,
        registration_description: Optional[str] = None,
        registration_name: Optional[str] = None,
        registration_scope: Optional[str] = None,
        resource_name_prefix: Optional[str] = None,
        resource_name_suffix: Optional[str] = None,
        tags: Optional[dict] = None,
        vulnerability_scanning_settings: Optional[dict] = None,
        wif_project_id: Optional[str] = None,
        wif_project_number: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_registration(
        self,
        *,
        additional_properties: Optional[dict] = None,
        deployment_method: Optional[str] = None,
        dspm_settings: Optional[dict] = None,
        entity_id: Optional[Union[str, List[str]]] = None,
        excluded_project_patterns: Optional[Union[str, List[str]]] = None,
        falcon_client_key_id: Optional[str] = None,
        falcon_client_key_type: Optional[str] = None,
        infra_manager_region: Optional[str] = None,
        infra_project_id: Optional[str] = None,
        labels: Optional[dict] = None,
        products: Optional[list] = None,
        registration_description: Optional[str] = None,
        registration_name: Optional[str] = None,
        registration_scope: Optional[str] = None,
        resource_name_prefix: Optional[str] = None,
        resource_name_suffix: Optional[str] = None,
        tags: Optional[dict] = None,
        vulnerability_scanning_settings: Optional[dict] = None,
        wif_project_id: Optional[str] = None,
        wif_project_number: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cloud_registration_gcp_update_registration(
        self,
        *,
        ids: Optional[str] = None,
        additional_properties: Optional[dict] = None,
        deployment_method: Optional[str] = None,
        dspm_settings: Optional[dict] = None,
        entity_id: Optional[Union[str, List[str]]] = None,
        excluded_project_patterns: Optional[Union[str, List[str]]] = None,
        falcon_client_key_id: Optional[str] = None,
        falcon_client_key_type: Optional[str] = None,
        infra_manager_region: Optional[str] = None,
        infra_project_id: Optional[str] = None,
        labels: Optional[dict] = None,
        log_ingestion_sink_name: Optional[str] = None,
        log_ingestion_subscription_name: Optional[str] = None,
        log_ingestion_topic_id: Optional[str] = None,
        products: Optional[list] = None,
        registration_description: Optional[str] = None,
        registration_name: Optional[str] = None,
        registration_scope: Optional[str] = None,
        resource_name_prefix: Optional[str] = None,
        resource_name_suffix: Optional[str] = None,
        tags: Optional[dict] = None,
        vulnerability_scanning_settings: Optional[dict] = None,
        wif_pool_name: Optional[str] = None,
        wif_project_id: Optional[str] = None,
        wif_project_number: Optional[str] = None,
        wif_provider_name: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_registration(
        self,
        *,
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cloud_registration_gcp_post_terraform_script(
        self,
        *,
        entity_id: Optional[Union[str, List[str]]] = None,
        excluded_project_patterns: Optional[Union[str, List[str]]] = None,
        falcon_client_key_id: Optional[str] = None,
        falcon_client_key_type: Optional[str] = None,
        infra_project_id: Optional[str] = None,
        labels: Optional[str] = None,
        realtime_visibility_enabled: Optional[bool] = None,
        registration_id: Optional[str] = None,
        registration_name: Optional[str] = None,
        resource_name_prefix: Optional[str] = None,
        resource_name_suffix: Optional[str] = None,
        tags: Optional[str] = None,
        vars_only: Optional[bool] = None,
        wif_project_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    cloud_registration_gcp_get_entities = get_entities
    cloud_registration_gcp_trigger_health_check = trigger_health_check
    cloud_registration_gcp_get_registration = get_registration
    cloud_registration_gcp_put_registration = update_registration
    cloud_registration_gcp_create_registration = create_registration
    cloud_registration_gcp_delete_registration = delete_registration
