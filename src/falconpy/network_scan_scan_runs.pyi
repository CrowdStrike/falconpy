"""Type stubs for network_scan_scan_runs."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class NetworkScanScanRuns(ServiceClass):

    def aggregate_scan_runs(
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

    def get_scan_runs(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_scan_runs(
        self,
        *,
        config: Optional[dict] = None,
        scan_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_scan_runs(
        self,
        *,
        action: Optional[str] = None,
        id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_scan_runs(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    AggregateScanRuns = aggregate_scan_runs
    GetScanRuns = get_scan_runs
    CreateScanRuns = create_scan_runs
    UpdateScanRuns = update_scan_runs
    QueryScanRuns = query_scan_runs
