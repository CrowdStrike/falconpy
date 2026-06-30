"""Type stubs for configuration_assessment_evaluation_logic."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ConfigurationAssessmentEvaluationLogic(ServiceClass):

    def get_evaluation_logic(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    getEvaluationLogicMixin0 = get_evaluation_logic
