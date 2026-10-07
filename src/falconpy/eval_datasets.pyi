"""Type stubs for eval_datasets."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class EvalDatasets(ServiceClass):

    def download_eval_dataset(
        self,
        *,
        id: Optional[str] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_eval_datasets(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_eval_dataset(
        self,
        *,
        agent_ids: Optional[Union[str, List[str]]] = None,
        created_at: Optional[str] = None,
        created_by: Optional[dict] = None,
        default_prompt_template: Optional[str] = None,
        description: Optional[str] = None,
        entryschema: Optional[str] = None,
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

    def create_eval_dataset(
        self,
        *,
        agent_ids: Optional[Union[str, List[str]]] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        metadata: Optional[dict] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_eval_dataset(
        self,
        *,
        id: Optional[str] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_eval_datasets(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    EntitiesEvalDatasetsDownloadV1 = download_eval_dataset
    EntitiesEvalDatasetsV1 = get_eval_datasets
    EntitiesEvalDatasetsUpdateV1 = update_eval_dataset
    EntitiesEvalDatasetsCreateV1 = create_eval_dataset
    EntitiesEvalDatasetsDeleteV1 = delete_eval_dataset
    QueriesEvalDatasetsV1 = query_eval_datasets
