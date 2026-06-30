"""Type stubs for saas_security."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class SaasSecurity(ServiceClass):

    def get_metrics(
        self,
        *,
        status: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        integration_id: Optional[str] = None,
        impact: Optional[str] = None,
        compliance: Optional[bool] = None,
        check_type: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_alerts(
        self,
        *,
        id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        last_id: Optional[str] = None,
        type: Optional[str] = None,
        integration_id: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        ascending: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_application_users(
        self,
        *args: Union[str, List[str]],
        item_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_application_inventory(
        self,
        *,
        type: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        status: Optional[str] = None,
        access_level: Optional[str] = None,
        scopes: Optional[str] = None,
        users: Optional[str] = None,
        groups: Optional[str] = None,
        last_activity: Optional[str] = None,
        integration_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_security_check(
        self,
        *,
        id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def dismiss_affected_entity(
        self,
        *,
        id: Optional[str] = None,
        entities: Optional[str] = None,
        reason: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def dismiss_security_check(
        self,
        *,
        id: Optional[str] = None,
        reason: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_security_checks(
        self,
        *,
        id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        status: Optional[str] = None,
        integration_id: Optional[str] = None,
        impact: Optional[str] = None,
        compliance: Optional[bool] = None,
        check_type: Optional[str] = None,
        check_tags: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_security_check_compliance(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def complete_integration_upload(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def reset_integration_builder(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_integration_builder_status(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def upload_integration_builder(
        self,
        *,
        id: Optional[str] = None,
        source_id: Optional[str] = None,
        data: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_asset_inventory(
        self,
        *,
        integration_id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        resource_type: Optional[str] = None,
        access_level: Optional[str] = None,
        last_accessed: Optional[str] = None,
        last_modified: Optional[str] = None,
        resource_name: Optional[str] = None,
        password_protected: Optional[bool] = None,
        resource_owner: Optional[str] = None,
        resource_owner_enabled: Optional[bool] = None,
        unmanaged_domain: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_device_inventory(
        self,
        *,
        integration_id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        email: Optional[str] = None,
        privileged_only: Optional[bool] = None,
        unassociated_devices: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_integrations(
        self,
        *,
        saas_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_activity_monitor(
        self,
        *,
        integration_id: Optional[str] = None,
        actor: Optional[str] = None,
        category: Optional[str] = None,
        projection: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_supported_saas(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_system_logs(
        self,
        *,
        from_date: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        to_date: Optional[str] = None,
        total_count: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_system_users(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_user_inventory(
        self,
        *,
        integration_id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        email: Optional[str] = None,
        privileged_only: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetMetricsV3 = get_metrics
    GetAlertsV3 = get_alerts
    GetAppInventoryUsers = get_application_users
    GetAppInventory = get_application_inventory
    GetSecurityCheckAffectedV3 = get_security_check
    DismissAffectedEntityV3 = dismiss_affected_entity
    DismissSecurityCheckV3 = dismiss_security_check
    GetSecurityChecksV3 = get_security_checks
    GetSecurityCheckComplianceV3 = get_security_check_compliance
    IntegrationBuilderEndTransactionV3 = complete_integration_upload
    IntegrationBuilderResetV3 = reset_integration_builder
    IntegrationBuilderGetStatusV3 = get_integration_builder_status
    IntegrationBuilderUploadV3 = upload_integration_builder
    GetAssetInventoryV3 = get_asset_inventory
    GetDeviceInventoryV3 = get_device_inventory
    GetIntegrationsV3 = get_integrations
    GetActivityMonitorV3 = get_activity_monitor
    GetSupportedSaasV3 = get_supported_saas
    GetSystemLogsV3 = get_system_logs
    GetSystemUsersV3 = get_system_users
    GetUserInventoryV3 = get_user_inventory
