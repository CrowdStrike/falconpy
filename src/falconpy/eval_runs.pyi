"""Type stubs for eval_runs."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class EvalRuns(ServiceClass):

    def get_eval_runs(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_eval_run(
        self,
        *,
        actual_cost: Optional[float] = None,
        agent_id: Optional[str] = None,
        agent_version_id: Optional[str] = None,
        completed_at: Optional[str] = None,
        created_at: Optional[str] = None,
        created_by: Optional[dict] = None,
        dataset_entry_ids: Optional[Union[str, List[str]]] = None,
        dataset_ids: Optional[Union[str, List[str]]] = None,
        entry_tags: Optional[Union[str, List[str]]] = None,
        estimated_cost: Optional[float] = None,
        evaluator_ids: Optional[Union[str, List[str]]] = None,
        id: Optional[str] = None,
        is_deleted: Optional[bool] = None,
        metadata: Optional[dict] = None,
        name: Optional[str] = None,
        owner: Optional[str] = None,
        progress: Optional[dict] = None,
        project_id: Optional[str] = None,
        status: Optional[str] = None,
        summary: Optional[dict] = None,
        updated_at: Optional[str] = None,
        updated_by: Optional[dict] = None,
        variable_values: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_eval_run(
        self,
        *,
        id: Optional[str] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def perform_eval_run_action(
        self,
        *,
        id: Optional[str] = None,
        action_name: Optional[str] = None,
        action: Optional[str] = None,
        case_cost_limit: Optional[dict] = None,
        project_id: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_eval_runs(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    EntitiesEvalRunsV1 = get_eval_runs
    EntitiesEvalRunsCreateV1 = create_eval_run
    EntitiesEvalRunsDeleteV1 = delete_eval_run
    EntitiesEvalRunsActionV1 = perform_eval_run_action
    QueriesEvalRunsV1 = query_eval_runs
