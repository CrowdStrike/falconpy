"""Type stubs for quick_scan."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class QuickScan(ServiceClass):

    def get_scans_aggregates(
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

    def scan_samples(
        self,
        *args: Union[str, List[str]],
        samples: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_submissions(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetScansAggregates = get_scans_aggregates
    GetScans = get_scans
    ScanSamples = scan_samples
    QuerySubmissionsMixin0 = query_submissions
    QuerySubmissions = query_submissions
