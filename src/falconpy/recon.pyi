"""Type stubs for recon."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Recon(ServiceClass):

    def aggregate_notifications_exposed_data_records(
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

    def aggregate_notifications(
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

    def preview_rule(
        self,
        *,
        filter: Optional[str] = None,
        lookback_days: Optional[int] = None,
        topic: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_actions(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_actions(
        self,
        *,
        actions: Optional[list] = None,
        rule_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_action(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_action(
        self,
        *,
        content_format: Optional[str] = None,
        frequency: Optional[str] = None,
        id: Optional[str] = None,
        recipients: Optional[Union[str, List[str]]] = None,
        status: Optional[str] = None,
        trigger_matchless: Optional[bool] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_export_job_file_contents(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_export_jobs(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_export_jobs(
        self,
        *,
        entity: Optional[str] = None,
        export_type: Optional[str] = None,
        filter: Optional[str] = None,
        human_readable: Optional[bool] = None,
        sort: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_export_jobs(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_notifications_detailed_translated(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_notifications_detailed(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_notifications_exposed_data_records(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_notifications_translated(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_notifications(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_notifications(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_notifications(
        self,
        *,
        assigned_to_uuid: Optional[str] = None,
        id: Optional[str] = None,
        idp_send_status: Optional[str] = None,
        message: Optional[str] = None,
        status: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_rules(
        self,
        *,
        breach_monitor_only: Optional[bool] = None,
        breach_monitoring_enabled: Optional[bool] = None,
        exposed_data_match_type: Optional[str] = None,
        filter: Optional[str] = None,
        lookback_period: Optional[int] = None,
        match_on_tsq_result_types: Optional[Union[str, List[str]]] = None,
        name: Optional[str] = None,
        originating_template_id: Optional[str] = None,
        permissions: Optional[str] = None,
        priority: Optional[str] = None,
        substring_matching_enabled: Optional[bool] = None,
        topic: Optional[str] = None,
        tsq_match_edit_distance: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_rules(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        notificationsDeletionRequested: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_rules(
        self,
        *,
        breach_monitor_only: Optional[bool] = None,
        breach_monitoring_enabled: Optional[bool] = None,
        exposed_data_match_type: Optional[str] = None,
        filter: Optional[str] = None,
        id: Optional[str] = None,
        match_on_tsq_result_types: Optional[Union[str, List[str]]] = None,
        name: Optional[str] = None,
        permissions: Optional[str] = None,
        priority: Optional[str] = None,
        substring_matching_enabled: Optional[bool] = None,
        tsq_match_edit_distance: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_actions(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_notifications_exposed_data_records(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_notifications(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_rules(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        secondarySort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    AggregateNotificationsExposedDataRecordsV1 = aggregate_notifications_exposed_data_records
    AggregateNotificationsV1 = aggregate_notifications
    PreviewRuleV1 = preview_rule
    GetActionsV1 = get_actions
    CreateActionsV1 = create_actions
    DeleteActionV1 = delete_action
    UpdateActionV1 = update_action
    GetFileContentForExportJobsV1 = get_export_job_file_contents
    GetExportJobsV1 = get_export_jobs
    CreateExportJobsV1 = create_export_jobs
    DeleteExportJobsV1 = delete_export_jobs
    GetNotificationsDetailedTranslatedV1 = get_notifications_detailed_translated
    GetNotificationsDetailedV1 = get_notifications_detailed
    GetNotificationsExposedDataRecordsV1 = get_notifications_exposed_data_records
    GetNotificationsTranslatedV1 = get_notifications_translated
    GetNotificationsV1 = get_notifications
    DeleteNotificationsV1 = delete_notifications
    UpdateNotificationsV1 = update_notifications
    GetRulesV1 = get_rules
    CreateRulesV1 = create_rules
    DeleteRulesV1 = delete_rules
    UpdateRulesV1 = update_rules
    QueryActionsV1 = query_actions
    QueryNotificationsExposedDataRecordsV1 = query_notifications_exposed_data_records
    QueryNotificationsV1 = query_notifications
    QueryRulesV1 = query_rules
