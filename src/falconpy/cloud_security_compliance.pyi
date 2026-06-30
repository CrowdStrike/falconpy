"""Type stubs for cloud_security_compliance."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CloudSecurityCompliance(ServiceClass):

    def framework_posture_summaries(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def rule_posture_summaries(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    cloud_compliance_framework_posture_summaries = framework_posture_summaries
    cloud_compliance_rule_posture_summaries = rule_posture_summaries
