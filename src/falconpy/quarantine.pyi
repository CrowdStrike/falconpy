"""Type stubs for quarantine."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Quarantine(ServiceClass):

    def action_update_count(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aggregate_files(
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

    def get_quarantine_files(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_quarantined_detects_by_id(
        self,
        *,
        action: Optional[str] = None,
        comment: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_quarantine_files(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_quarantined_detects_by_query(
        self,
        *,
        action: Optional[str] = None,
        comment: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ActionUpdateCount = action_update_count
    GetAggregateFiles = get_aggregate_files
    GetQuarantineFiles = get_quarantine_files
    UpdateQuarantinedDetectsByIds = update_quarantined_detects_by_id
    QueryQuarantineFiles = query_quarantine_files
    UpdateQfByQuery = update_quarantined_detects_by_query
