"""Type stubs for spotlight_evaluation_logic."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class SpotlightEvaluationLogic(ServiceClass):

    def query_evaluation_logic_combined(
        self,
        *,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_evaluation_logic(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_evaluation_logic(
        self,
        *,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_supported_evaluations(
        self,
        *,
        after: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        risk_provider: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    combinedQueryEvaluationLogic = query_evaluation_logic_combined
    getEvaluationLogic = get_evaluation_logic
    queryEvaluationLogic = query_evaluation_logic
    combinedSupportedEvaluationExt = get_supported_evaluations
