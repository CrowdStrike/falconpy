"""Type stubs for audit."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Audit(ServiceClass):

    def export_audit_query_results(
        self,
        *,
        id: Optional[str] = None,
        format: Optional[str] = None,
        include_descriptions: Optional[bool] = None,
        include_extension_metadata: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_audit_query_results(
        self,
        *,
        id: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        include_descriptions: Optional[bool] = None,
        include_extension_metadata: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def poll_audit_query_status(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_audit_query_job(
        self,
        *,
        action: Optional[Union[str, List[str]]] = None,
        action_description: Optional[Union[str, List[str]]] = None,
        actor_id: Optional[Union[str, List[str]]] = None,
        actor_ip: Optional[Union[str, List[str]]] = None,
        actor_type: Optional[Union[str, List[str]]] = None,
        category: Optional[Union[str, List[str]]] = None,
        category_description: Optional[Union[str, List[str]]] = None,
        cid: Optional[Union[str, List[str]]] = None,
        end_time: Optional[str] = None,
        event_id: Optional[Union[str, List[str]]] = None,
        event_version: Optional[Union[str, List[str]]] = None,
        extensions: Optional[dict] = None,
        geo_city: Optional[Union[str, List[str]]] = None,
        geo_country: Optional[Union[str, List[str]]] = None,
        sort: Optional[str] = None,
        start_time: Optional[str] = None,
        target_display_name: Optional[Union[str, List[str]]] = None,
        target_id: Optional[Union[str, List[str]]] = None,
        target_type: Optional[Union[str, List[str]]] = None,
        user_agent: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ExportQueryResults = export_audit_query_results
    GetQueryResults = get_audit_query_results
    PollQueryJobStatus = poll_audit_query_status
    CreateQueryJob = create_audit_query_job
