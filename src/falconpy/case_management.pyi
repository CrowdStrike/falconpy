"""Type stubs for case_management."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CaseManagement(ServiceClass):

    def aggregates_file_details_post_v1(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_file_details(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_file_details(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_file_details(
        self,
        *,
        description: Optional[str] = None,
        id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def bulk_download_files(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def download_existing_files(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def upload_file(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_file_details(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_file_detail_ids(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rtr_file_metadata(
        self,
        *,
        aid: Optional[str] = None,
        file_path: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def retrieve_rtr_file(
        self,
        *,
        aid: Optional[str] = None,
        case_id: Optional[str] = None,
        description: Optional[str] = None,
        file_path: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def retrieve_rtr_recent_file(
        self,
        *,
        aid: Optional[str] = None,
        case_id: Optional[str] = None,
        description: Optional[str] = None,
        session_id: Optional[str] = None,
        sha256: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_notification_groups_aggregation(
        self,
        *,
        date_ranges: Optional[list] = None,
        field: Optional[str] = None,
        filter: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[int] = None,
        sort: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_notification_groups_aggregation_v2(
        self,
        *,
        date_ranges: Optional[list] = None,
        field: Optional[str] = None,
        filter: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[int] = None,
        sort: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_sla_aggregations(
        self,
        *,
        date_ranges: Optional[list] = None,
        field: Optional[str] = None,
        filter: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[int] = None,
        sort: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_template_aggregations(
        self,
        *,
        date_ranges: Optional[list] = None,
        field: Optional[str] = None,
        filter: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[int] = None,
        sort: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_access_tag_aggregations(
        self,
        *,
        date_ranges: Optional[list] = None,
        field: Optional[str] = None,
        filter: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[int] = None,
        sort: Optional[str] = None,
        type: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_access_tags(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        with_has_access: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_fields(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_notification_groups(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_notification_group(
        self,
        *,
        channels: Optional[list] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_notification_group(
        self,
        *,
        channels: Optional[list] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_notification_group(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_notification_groups_v2(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_notification_group_v2(
        self,
        *,
        channels: Optional[list] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_notification_group_v2(
        self,
        *,
        channels: Optional[list] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_notification_group_v2(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_slas(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_sla(
        self,
        *,
        description: Optional[str] = None,
        goals: Optional[list] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_sla(
        self,
        *,
        description: Optional[str] = None,
        goals: Optional[list] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_sla(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_template_snapshots(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        template_ids: Optional[Union[str, List[str]]] = None,
        versions: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def export_templates(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        format: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def import_template(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_templates(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        with_has_access: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_template(
        self,
        *,
        access_tags: Optional[list] = None,
        description: Optional[str] = None,
        fields: Optional[list] = None,
        name: Optional[str] = None,
        sla_id: Optional[str] = None,
        sla_rules: Optional[list] = None,
        workflows: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_template(
        self,
        *,
        access_tags: Optional[list] = None,
        description: Optional[str] = None,
        fields: Optional[list] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        sla_id: Optional[str] = None,
        sla_rules: Optional[list] = None,
        workflows: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_templates(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_access_tags(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        after: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_fields(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_notification_groups(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_notification_groups_v2(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_slas(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_template_snapshots(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_templates(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def add_case_alert_evidence(
        self,
        *,
        alerts: Optional[list] = None,
        id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def add_case_tags(
        self,
        *,
        id: Optional[str] = None,
        tags: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_case_tags(
        self,
        *,
        id: Optional[str] = None,
        tag: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_case(
        self,
        *,
        access_tags: Optional[list] = None,
        assigned_to_user_uuid: Optional[str] = None,
        description: Optional[str] = None,
        description_format: Optional[str] = None,
        description_tagged_users: Optional[Union[str, List[str]]] = None,
        evidence: Optional[dict] = None,
        name: Optional[str] = None,
        severity: Optional[int] = None,
        severity_info: Optional[dict] = None,
        status: Optional[str] = None,
        tags: Optional[Union[str, List[str]]] = None,
        template: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_cases(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_case_fields(
        self,
        *,
        expected_consistency_version: Optional[int] = None,
        expected_version: Optional[int] = None,
        fields: Optional[dict] = None,
        id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def add_case_event_evidence(
        self,
        *,
        events: Optional[list] = None,
        id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_case_ids(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    combined_file_details_get_v1 = query_file_details
    entities_file_details_get_v1 = get_file_details
    entities_file_details_patch_v1 = update_file_details
    entities_files_bulk_download_post_v1 = bulk_download_files
    entities_files_download_get_v1 = download_existing_files
    entities_files_upload_post_v1 = upload_file
    entities_files_delete_v1 = delete_file_details
    queries_file_details_get_v1 = query_file_detail_ids
    entities_get_rtr_file_metadata_post_v1 = get_rtr_file_metadata
    entities_retrieve_rtr_file_post_v1 = retrieve_rtr_file
    entities_retrieve_rtr_recent_file_post_v1 = retrieve_rtr_recent_file
    aggregates_notification_groups_post_v1 = get_notification_groups_aggregation
    aggregates_notification_groups_post_v2 = get_notification_groups_aggregation_v2
    aggregates_slas_post_v1 = get_sla_aggregations
    aggregates_templates_post_v1 = get_template_aggregations
    aggregates_access_tags_post_v1 = get_access_tag_aggregations
    entities_access_tags_get_v1 = get_access_tags
    entities_fields_get_v1 = get_fields
    entities_notification_groups_get_v1 = get_notification_groups
    entities_notification_groups_post_v1 = create_notification_group
    entities_notification_groups_patch_v1 = update_notification_group
    entities_notification_groups_delete_v1 = delete_notification_group
    entities_notification_groups_get_v2 = get_notification_groups_v2
    entities_notification_groups_post_v2 = create_notification_group_v2
    entities_notification_groups_patch_v2 = update_notification_group_v2
    entities_notification_groups_delete_v2 = delete_notification_group_v2
    entities_slas_get_v1 = get_slas
    entities_slas_post_v1 = create_sla
    entities_slas_patch_v1 = update_sla
    entities_slas_delete_v1 = delete_sla
    entities_template_snapshots_get_v1 = get_template_snapshots
    entities_templates_export_get_v1 = export_templates
    entities_templates_import_post_v1 = import_template
    entities_templates_get_v1 = get_templates
    entities_templates_post_v1 = create_template
    entities_templates_patch_v1 = update_template
    entities_templates_delete_v1 = delete_templates
    queries_fields_get_v1 = query_fields
    queries_access_tags_get_v1 = query_access_tags
    queries_notification_groups_get_v1 = query_notification_groups
    queries_notification_groups_get_v2 = query_notification_groups_v2
    queries_slas_get_v1 = query_slas
    queries_template_snapshots_get_v1 = query_template_snapshots
    queries_templates_get_v1 = query_templates
    entities_alert_evidence_post_v1 = add_case_alert_evidence
    entities_case_tags_post_v1 = add_case_tags
    entities_case_tags_delete_v1 = delete_case_tags
    entities_cases_put_v2 = create_case
    entities_cases_post_v2 = get_cases
    entities_cases_patch_v2 = update_case_fields
    entities_event_evidence_post_v1 = add_case_event_evidence
    queries_cases_get_v1 = query_case_ids
