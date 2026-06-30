"""Type stubs for zero_trust_assessment."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ZeroTrustAssessment(ServiceClass):

    def get_assessment(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_audit(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_assessments_by_score(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        after: Optional[str] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    getAssessmentV1 = get_assessment
    getAuditV1 = get_audit
    getComplianceV1 = get_audit
    get_compliance = get_audit
    getAssessmentsByScoreV1 = get_assessments_by_score
