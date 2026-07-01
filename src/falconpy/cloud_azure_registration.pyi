"""Type stubs for cloud_azure_registration."""
from typing import Dict, List, Optional, Union
from typing_extensions import deprecated
from ._service_class import ServiceClass
from ._result import Result


class CloudAzureRegistration(ServiceClass):

    def delete_legacy_subscription(
        self,
        *,
        retain_client: Optional[bool] = None,
        subscription_id: Optional[str] = None,
        tenant_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def health_check(
        self,
        *args: Union[str, List[str]],
        tenant_ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_registration(
        self,
        *,
        tenant_id: Optional[str] = None,
        registration_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_registration(
        self,
        *,
        resource: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_registration(
        self,
        *,
        resource: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_registration(
        self,
        *,
        tenant_ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    @deprecated("This operation is no longer available in CrowdStrike's API. Calling this method will result in an error from the API.")
    def deployment_script(
        self,
        *,
        tenant_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def download_script(
        self,
        *,
        tenantId: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def validate_registration(
        self,
        *,
        tenant_id: Optional[str] = None,
        stack_name: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cloud_registration_azure_create_suppressions(
        self,
        *,
        reason: Optional[str] = None,
        registration_id: Optional[str] = None,
        target: Optional[dict] = None,
        type: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cloud_registration_azure_delete_suppressions(
        self,
        *,
        suppression_ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cloud_registration_azure_get_issue_suppression_values_by_field(
        self,
        *,
        registration_id: Optional[str] = None,
        field: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cloud_registration_azure_get_issue_values_by_field(
        self,
        *,
        registration_id: Optional[str] = None,
        filter: Optional[str] = None,
        field: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cloud_registration_azure_get_issues(
        self,
        *,
        registration_id: Optional[str] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        group_by: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cloud_registration_azure_get_script(
        self,
        *,
        tenant_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cloud_registration_azure_get_script_versions(
        self,
        *,
        deployment_method: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cloud_registration_azure_get_suppressions(
        self,
        *,
        registration_id: Optional[str] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def cloud_registration_azure_update_suppressions(
        self,
        *,
        reason: Optional[str] = None,
        suppression_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    cloud_registration_azure_delete_legacy_subscription = delete_legacy_subscription
    cloud_registration_azure_trigger_health_check = health_check
    cloud_registration_azure_get_registration = get_registration
    cloud_registration_azure_create_registration = create_registration
    cloud_registration_azure_update_registration = update_registration
    cloud_registration_azure_delete_registration = delete_registration
    download_azure_script = deployment_script
    cloud_registration_azure_download_script = download_script
    cloud_registration_azure_validate_registration = validate_registration
