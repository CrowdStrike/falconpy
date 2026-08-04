"""Type stubs for scanning_orchestrator."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ScanningOrchestrator(ServiceClass):

    def get_combined_schedules(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def trigger_scan_by_schedule(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_schedules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_schedules(
        self,
        *,
        account_ids: Optional[Union[str, List[str]]] = None,
        all_accounts: Optional[bool] = None,
        all_regions: Optional[bool] = None,
        cadence: Optional[dict] = None,
        cloud_group_ids: Optional[Union[str, List[str]]] = None,
        dspm_scanning_config: Optional[dict] = None,
        enable: Optional[bool] = None,
        name: Optional[str] = None,
        provider_type: Optional[dict] = None,
        scan_product: Optional[dict] = None,
        selected_regions: Optional[Union[str, List[str]]] = None,
        service_names: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_schedules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_schedules(
        self,
        *,
        asset_filter: Optional[dict] = None,
        cadence: Optional[dict] = None,
        enable: Optional[bool] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        scan_config: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_service_types(
        self,
        *,
        scan_product: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_schedules(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...
