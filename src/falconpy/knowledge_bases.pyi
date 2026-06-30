"""Type stubs for knowledge_bases."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class KnowledgeBases(ServiceClass):

    def aggregates_knowledge_bases_v1(
        self,
        *,
        include_deleted: Optional[bool] = None,
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
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def entities_knowledge_bases_v1(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        include_deleted: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def entities_knowledge_bases_create_v1(
        self,
        *,
        created_at: Optional[str] = None,
        created_by: Optional[dict] = None,
        description: Optional[str] = None,
        embedding_model: Optional[str] = None,
        files_count: Optional[int] = None,
        id: Optional[str] = None,
        is_deleted: Optional[bool] = None,
        name: Optional[str] = None,
        updated_at: Optional[str] = None,
        updated_by: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def entities_knowledge_bases_update_v1(
        self,
        *,
        created_at: Optional[str] = None,
        created_by: Optional[dict] = None,
        description: Optional[str] = None,
        embedding_model: Optional[str] = None,
        files_count: Optional[int] = None,
        id: Optional[str] = None,
        is_deleted: Optional[bool] = None,
        name: Optional[str] = None,
        updated_at: Optional[str] = None,
        updated_by: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def queries_knowledge_bases_v1(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        include_deleted: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def combined_knowledge_bases_v1(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        include_deleted: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    AggregatesKnowledgeBasesV1 = aggregates_knowledge_bases_v1
    CombinedKnowledgeBasesV1 = combined_knowledge_bases_v1
    EntitiesKnowledgeBasesV1 = entities_knowledge_bases_v1
    EntitiesKnowledgeBasesCreateV1 = entities_knowledge_bases_create_v1
    EntitiesKnowledgeBasesUpdateV1 = entities_knowledge_bases_update_v1
    QueriesKnowledgeBasesV1 = queries_knowledge_bases_v1
