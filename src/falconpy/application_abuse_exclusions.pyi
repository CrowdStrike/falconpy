"""Type stubs for application_abuse_exclusions."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ApplicationAbuseExclusions(ServiceClass):

    def aggregate_app_abuse_exclusions(
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

    def create_app_abuse_report(
        self,
        *,
        report_format: Optional[str] = None,
        search: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_app_abuse_exclusions(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_app_abuse_exclusion(
        self,
        *,
        exclusions: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_app_abuse_exclusions(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        comment: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_app_abuse_exclusions(
        self,
        *,
        exclusions: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_app_abuse_apps_by_category(
        self,
        *,
        category: Optional[str] = None,
        show_available_only: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_app_abuse_categories(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_app_abuse_exclusions(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    app_abuse_exclusions_aggregates_v1 = aggregate_app_abuse_exclusions
    app_abuse_exclusions_report_v1 = create_app_abuse_report
    app_abuse_exclusions_get_v1 = get_app_abuse_exclusions
    app_abuse_exclusions_create_v1 = create_app_abuse_exclusion
    app_abuse_exclusions_delete_v1 = delete_app_abuse_exclusions
    app_abuse_exclusions_update_v1 = update_app_abuse_exclusions
    app_abuse_exclusions_get_apps_by_category_v1 = get_app_abuse_apps_by_category
    app_abuse_exclusions_get_categories_v1 = get_app_abuse_categories
    app_abuse_exclusions_query_v1 = query_app_abuse_exclusions
