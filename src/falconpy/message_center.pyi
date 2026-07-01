"""Type stubs for message_center."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class MessageCenter(ServiceClass):

    def aggregate_cases(
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

    def get_case_activity(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def add_case_activity(
        self,
        *,
        body: Optional[str] = None,
        case_id: Optional[str] = None,
        type: Optional[str] = None,
        user_uuid: Optional[str] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def download_case_attachment(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def add_case_attachment(
        self,
        *,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_case_v2(
        self,
        *,
        body: Optional[str] = None,
        detections: Optional[list] = None,
        incidents: Optional[list] = None,
        malware_submission_id: Optional[str] = None,
        recon_rule_type: Optional[str] = None,
        title: Optional[str] = None,
        type: Optional[str] = None,
        user_uuid: Optional[str] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_cases(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_activities(
        self,
        *,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        case_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_cases(
        self,
        *,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    AggregateCases = aggregate_cases
    GetCaseActivityByIds = get_case_activity
    get_case_activity_by_ids = get_case_activity
    CaseAddActivity = add_case_activity
    case_add_activity = add_case_activity
    CaseDownloadAttachment = download_case_attachment
    case_download_attachment = download_case_attachment
    CaseAddAttachment = add_case_attachment
    case_add_attachment = add_case_attachment
    CreateCaseV2 = create_case_v2
    GetCaseEntitiesByIDs = get_cases
    get_case_entities_by_ids = get_cases
    QueryActivityByCaseID = query_activities
    query_activity_by_case_id = query_activities
    QueryCasesIdsByFilter = query_cases
    QueryCaseIdsByFilter = query_cases
    query_cases_ids_by_filter = query_cases
    query_case_ids_by_filter = query_cases
