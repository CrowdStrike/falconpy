"""Type stubs for ml_exclusions."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class MLExclusions(ServiceClass):

    def aggregate_exclusions(
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

    def get_all_exclusions(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def perform_actions(
        self,
        *,
        action_name: Optional[str] = None,
        action_parameters: Optional[list] = None,
        available: Optional[bool] = None,
        description: Optional[str] = None,
        group: Optional[str] = None,
        label: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_reports(
        self,
        *,
        report_format: Optional[str] = None,
        search: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_exclusions_by_id(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_exclusions_v2(
        self,
        *,
        exclusions: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_exclusions_v2(
        self,
        *,
        comment: Optional[str] = None,
        excluded_from: Optional[Union[str, List[str]]] = None,
        grandparent_value: Optional[str] = None,
        groups: Optional[Union[str, List[str]]] = None,
        id: Optional[str] = None,
        parent_value: Optional[str] = None,
        value: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_exclusions_v2(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        comment: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_exclusions_v2(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_ml_exclusion_sets(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_ml_exclusions_v2(
        self,
        *,
        comment: Optional[str] = None,
        excluded_from: Optional[Union[str, List[str]]] = None,
        groups: Optional[Union[str, List[str]]] = None,
        value: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_ml_exclusions(
        self,
        *,
        comment: Optional[str] = None,
        groups: Optional[Union[str, List[str]]] = None,
        id: Optional[str] = None,
        is_descendant_process: Optional[bool] = None,
        value: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_exclusions(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_exclusions(
        self,
        *,
        comment: Optional[str] = None,
        excluded_from: Optional[Union[str, List[str]]] = None,
        groups: Optional[Union[str, List[str]]] = None,
        value: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_exclusions(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        comment: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_exclusions(
        self,
        *,
        comment: Optional[str] = None,
        groups: Optional[Union[str, List[str]]] = None,
        id: Optional[str] = None,
        is_descendant_process: Optional[bool] = None,
        value: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_exclusions(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    getMLExclusionsV1 = get_exclusions
    createMLExclusionsV1 = create_exclusions
    deleteMLExclusionsV1 = delete_exclusions
    updateMLExclusionsV1 = update_exclusions
    queryMLExclusionsV1 = query_exclusions
    exclusions_aggregates_v2 = aggregate_exclusions
    exclusions_get_all_v2 = get_all_exclusions
    exclusions_perform_action_v2 = perform_actions
    exclusions_get_reports_v2 = get_reports
    exclusions_get_v2 = get_exclusions_by_id
    exclusions_create_v2 = create_exclusions_v2
    exclusions_update_v2 = update_exclusions_v2
    exclusions_delete_v2 = delete_exclusions_v2
    exclusions_search_v2 = search_exclusions_v2
