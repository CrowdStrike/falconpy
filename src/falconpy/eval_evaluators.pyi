"""Type stubs for eval_evaluators."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class EvalEvaluators(ServiceClass):

    def get_eval_evaluators(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_eval_evaluator(
        self,
        *,
        agent_ids: Optional[Union[str, List[str]]] = None,
        config: Optional[str] = None,
        created_at: Optional[str] = None,
        created_by: Optional[dict] = None,
        description: Optional[str] = None,
        evaluator_type: Optional[str] = None,
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

    def create_eval_evaluator(
        self,
        *,
        agent_ids: Optional[Union[str, List[str]]] = None,
        config: Optional[str] = None,
        created_at: Optional[str] = None,
        created_by: Optional[dict] = None,
        description: Optional[str] = None,
        evaluator_type: Optional[str] = None,
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

    def delete_eval_evaluator(
        self,
        *,
        id: Optional[str] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_eval_evaluators(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    EntitiesEvalEvaluatorsV1 = get_eval_evaluators
    EntitiesEvalEvaluatorsUpdateV1 = update_eval_evaluator
    EntitiesEvalEvaluatorsCreateV1 = create_eval_evaluator
    EntitiesEvalEvaluatorsDeleteV1 = delete_eval_evaluator
    QueriesEvalEvaluatorsV1 = query_eval_evaluators
