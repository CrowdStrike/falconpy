"""Type stubs for knowledge_base_files."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class KnowledgeBaseFiles(ServiceClass):

    def entities_knowledge_base_files_download_v1(
        self,
        *,
        knowledge_base_id: Optional[str] = None,
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def entities_knowledge_base_files_v1(
        self,
        *,
        knowledge_base_id: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        include_deleted: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def entities_knowledge_base_files_update_v1(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def entities_knowledge_base_files_create_v1(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def entities_knowledge_base_files_delete_v1(
        self,
        *,
        knowledge_base_id: Optional[str] = None,
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def queries_knowledge_base_files_v1(
        self,
        *,
        knowledge_base_id: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        filter: Optional[str] = None,
        include_deleted: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    EntitiesKnowledgeBaseFilesDownloadV1 = entities_knowledge_base_files_download_v1
    EntitiesKnowledgeBaseFilesV1 = entities_knowledge_base_files_v1
    EntitiesKnowledgeBaseFilesUpdateV1 = entities_knowledge_base_files_update_v1
    EntitiesKnowledgeBaseFilesCreateV1 = entities_knowledge_base_files_create_v1
    EntitiesKnowledgeBaseFilesDeleteV1 = entities_knowledge_base_files_delete_v1
    QueriesKnowledgeBaseFilesV1 = queries_knowledge_base_files_v1
