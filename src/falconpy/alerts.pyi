"""Type stubs for alerts."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Alerts(ServiceClass):

    def get_aggregate_alerts_v1(
        self,
        *,
        date_ranges: Optional[list] = None,
        exclude: Optional[str] = None,
        field: Optional[str] = None,
        filter: Optional[str] = None,
        include: Optional[str] = None,
        interval: Optional[str] = None,
        max_doc_count: Optional[int] = None,
        min_doc_count: Optional[int] = None,
        missing: Optional[str] = None,
        name: Optional[str] = None,
        q: Optional[str] = None,
        ranges: Optional[list] = None,
        size: Optional[int] = None,
        sort: Optional[str] = None,
        sub_aggregates: Optional[list] = None,
        time_zone: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[list] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aggregate_alerts_v2(
        self,
        *,
        include_hidden: Optional[bool] = None,
        date_ranges: Optional[list] = None,
        exclude: Optional[str] = None,
        field: Optional[str] = None,
        filter: Optional[str] = None,
        include: Optional[str] = None,
        interval: Optional[str] = None,
        max_doc_count: Optional[int] = None,
        min_doc_count: Optional[int] = None,
        missing: Optional[str] = None,
        name: Optional[str] = None,
        q: Optional[str] = None,
        ranges: Optional[list] = None,
        size: Optional[int] = None,
        sort: Optional[str] = None,
        sub_aggregates: Optional[list] = None,
        time_zone: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[list] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_alerts_v2(
        self,
        *args: Union[str, List[str]],
        action_parameters: Optional[list] = None,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_alerts_v3(
        self,
        *args: Union[str, List[str]],
        include_hidden: Optional[bool] = None,
        action_parameters: Optional[list] = None,
        composite_ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_alerts_combined(
        self,
        *,
        after: Optional[str] = None,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_alerts_v1(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_alerts_v2(
        self,
        *args: Union[str, List[str]],
        include_hidden: Optional[bool] = None,
        composite_ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_alerts_v1(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_alerts_v2(
        self,
        *,
        include_hidden: Optional[bool] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    PostAggregatesAlertsV1 = get_aggregate_alerts_v1
    PostAggregatesAlertsV2 = get_aggregate_alerts_v2
    get_aggregate_alerts = get_aggregate_alerts_v1
    PatchEntitiesAlertsV2 = update_alerts_v2
    update_alerts = update_alerts_v2
    PatchEntitiesAlertsV3 = update_alerts_v3
    PostEntitiesAlertsV1 = get_alerts_v1
    PostEntitiesAlertsV2 = get_alerts_v2
    PostCombinedAlertsV1 = get_alerts_combined
    get_alerts = get_alerts_v1
    GetQueriesAlertsV1 = query_alerts_v1
    GetQueriesAlertsV2 = query_alerts_v2
    query_alerts = query_alerts_v1
    update_alerts = update_alerts_v2
    PatchEntitiesAlertsV1 = update_alerts_v2
