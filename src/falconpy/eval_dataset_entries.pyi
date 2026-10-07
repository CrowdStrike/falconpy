"""Type stubs for eval_dataset_entries."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class EvalDatasetEntries(ServiceClass):

    def get_eval_dataset_entries(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_eval_dataset_entry(
        self,
        *,
        created_at: Optional[str] = None,
        created_by: Optional[dict] = None,
        data: Optional[dict] = None,
        dataset_id: Optional[str] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        is_deleted: Optional[bool] = None,
        metadata: Optional[dict] = None,
        name: Optional[str] = None,
        owner: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[Union[str, List[str]]] = None,
        updated_at: Optional[str] = None,
        updated_by: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_eval_dataset_entry(
        self,
        *,
        created_at: Optional[str] = None,
        created_by: Optional[dict] = None,
        data: Optional[dict] = None,
        dataset_id: Optional[str] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        is_deleted: Optional[bool] = None,
        metadata: Optional[dict] = None,
        name: Optional[str] = None,
        owner: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[Union[str, List[str]]] = None,
        updated_at: Optional[str] = None,
        updated_by: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_eval_dataset_entry(
        self,
        *,
        id: Optional[str] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_eval_dataset_entries(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    EntitiesEvalDatasetEntriesV1 = get_eval_dataset_entries
    EntitiesEvalDatasetEntriesUpdateV1 = update_eval_dataset_entry
    EntitiesEvalDatasetEntriesCreateV1 = create_eval_dataset_entry
    EntitiesEvalDatasetEntriesDeleteV1 = delete_eval_dataset_entry
    QueriesEvalDatasetEntriesV1 = query_eval_dataset_entries
