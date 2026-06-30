"""Type stubs for configuration_assessment."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ConfigurationAssessment(ServiceClass):

    def query_combined_assessments(
        self,
        *,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        facet: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rule_details(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    getCombinedAssessmentsQuery = query_combined_assessments
    getRuleDetails = get_rule_details
