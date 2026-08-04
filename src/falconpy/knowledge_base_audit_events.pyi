"""Type stubs for knowledge_base_audit_events."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class KnowledgeBaseAuditEvents(ServiceClass):

    def aggregates_knowledge_base_audit_events_v1(
        self,
        *,
        include_deleted: Optional[bool] = None,
        body: Optional[list] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def combined_knowledge_base_audit_events_v1(
        self,
        *,
        knowledge_base_id: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        include_deleted: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def entities_knowledge_base_audit_events_v1(
        self,
        *,
        knowledge_base_id: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        include_deleted: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def queries_knowledge_base_audit_events_v1(
        self,
        *,
        knowledge_base_id: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        include_deleted: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    AggregatesKnowledgeBaseAuditEventsV1 = aggregates_knowledge_base_audit_events_v1
    CombinedKnowledgeBaseAuditEventsV1 = combined_knowledge_base_audit_events_v1
    EntitiesKnowledgeBaseAuditEventsV1 = entities_knowledge_base_audit_events_v1
    QueriesKnowledgeBaseAuditEventsV1 = queries_knowledge_base_audit_events_v1
