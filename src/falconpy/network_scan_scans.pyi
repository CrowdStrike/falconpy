"""Type stubs for network_scan_scans."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class NetworkScanScans(ServiceClass):

    def aggregate_scans(
        self,
        *,
        date_ranges: Optional[list] = None,
        exclude: Optional[str] = None,
        extended_bounds: Optional[dict] = None,
        field: Optional[str] = None,
        filter: Optional[str] = None,
        filters_spec: Optional[dict] = None,
        include: Optional[str] = None,
        interval: Optional[str] = None,
        max_doc_count: Optional[int] = None,
        min_doc_count: Optional[int] = None,
        missing: Optional[str] = None,
        name: Optional[str] = None,
        percents: Optional[list] = None,
        q: Optional[str] = None,
        ranges: Optional[list] = None,
        size: Optional[int] = None,
        sort: Optional[str] = None,
        sub_aggregates: Optional[list] = None,
        time_zone: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[list] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scans(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_scans(
        self,
        *,
        block_windows: Optional[dict] = None,
        credentialed: Optional[bool] = None,
        credentials: Optional[dict] = None,
        description: Optional[str] = None,
        fragile_device_detection: Optional[bool] = None,
        name: Optional[str] = None,
        scheduling: Optional[dict] = None,
        target_asset: Optional[dict] = None,
        target_asset_filter: Optional[dict] = None,
        target_external_ip: Optional[dict] = None,
        target_ip: Optional[dict] = None,
        target_type: Optional[str] = None,
        template_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_scans(
        self,
        *,
        block_windows: Optional[dict] = None,
        credentialed: Optional[bool] = None,
        credentials: Optional[dict] = None,
        description: Optional[str] = None,
        fragile_device_detection: Optional[bool] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        scheduling: Optional[dict] = None,
        target_asset: Optional[dict] = None,
        target_asset_filter: Optional[dict] = None,
        target_external_ip: Optional[dict] = None,
        target_ip: Optional[dict] = None,
        target_type: Optional[str] = None,
        template_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_scans(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_scans(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    AggregateScansMixin0 = aggregate_scans
    GetScans = get_scans
    CreateScans = create_scans
    UpdateScans = update_scans
    DeleteScans = delete_scans
    QueryScansMixin0 = query_scans
