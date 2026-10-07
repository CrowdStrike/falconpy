"""Type stubs for eval_cases."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class EvalCases(ServiceClass):

    def get_eval_cases(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_eval_cases(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        project_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    EntitiesEvalCasesV1 = get_eval_cases
    QueriesEvalCasesV1 = query_eval_cases
