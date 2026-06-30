"""Type stubs for ioc."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class IOC(ServiceClass):

    def indicator_aggregate(
        self,
        *,
        filter: Optional[str] = None,
        from_parent: Optional[bool] = None,
        date_ranges: Optional[list] = None,
        exclude: Optional[str] = None,
        extended_bounds: Optional[dict] = None,
        field: Optional[str] = None,
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
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def indicator_combined(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        after: Optional[str] = None,
        from_parent: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def action_get(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_indicators_report(
        self,
        *,
        from_parent: Optional[bool] = None,
        report_format: Optional[str] = None,
        search: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def indicator_get(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def indicator_create(
        self,
        *,
        retrodetects: Optional[bool] = None,
        ignore_warnings: Optional[bool] = None,
        comment: Optional[str] = None,
        indicators: Optional[list] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def indicator_delete(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        comment: Optional[str] = None,
        from_parent: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def indicator_update(
        self,
        *,
        retrodetects: Optional[bool] = None,
        ignore_warnings: Optional[bool] = None,
        bulk_update: Optional[dict] = None,
        comment: Optional[str] = None,
        indicators: Optional[list] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def action_query(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def indicator_search(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        after: Optional[str] = None,
        from_parent: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def ioc_type_query(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def platform_query(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def severity_query(
        self,
        *,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def devices_count_legacy(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def devices_count(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def devices_ran_on_legacy(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def devices_ran_on(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def processes_ran_on_legacy(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def processes_ran_on(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def entities_processes(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def indicator_sdmf_query_v1(
        self,
        *,
        control_info: Optional[dict] = None,
        id: Optional[str] = None,
        nodes: Optional[list] = None,
        res_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    action_get_v1 = action_get
    action_query_v1 = action_query
    GetIndicatorsReport = get_indicators_report
    indicator_aggregate_v1 = indicator_aggregate
    indicator_combined_v1 = indicator_combined
    indicator_get_v1 = indicator_get
    indicator_create_v1 = indicator_create
    indicator_delete_v1 = indicator_delete
    indicator_update_v1 = indicator_update
    indicator_search_v1 = indicator_search
    ioc_type_query_v1 = ioc_type_query
    platform_query_v1 = platform_query
    severity_query_v1 = severity_query
    DevicesCount = devices_count_legacy
    indicator_get_device_count_v1 = devices_count
    DevicesRanOn = devices_ran_on_legacy
    indicator_get_devices_ran_on_v1 = devices_ran_on
    ProcessesRanOn = processes_ran_on_legacy
    indicator_get_processes_ran_on_v1 = processes_ran_on
