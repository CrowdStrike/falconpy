"""Type stubs for detects."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Detects(ServiceClass):

    def get_aggregate_detects(
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

    def update_detects_by_ids(
        self,
        *args: Union[str, List[str]],
        assigned_to_uuid: Optional[str] = None,
        comment: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        new_behaviors_processed: Optional[Union[str, List[str]]] = None,
        show_in_ui: Optional[bool] = None,
        status: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_detect_summaries(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_detects(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetAggregateDetects = get_aggregate_detects
    UpdateDetectsByIdsV2 = update_detects_by_ids
    GetDetectSummaries = get_detect_summaries
    QueryDetects = query_detects
