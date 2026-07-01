"""Type stubs for cloud_security_risks."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CloudSecurityRisks(ServiceClass):

    def cloud_security_timeline_risks_enriched(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...
