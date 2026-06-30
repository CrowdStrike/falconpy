"""Type stubs for serverless_vulnerabilities."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ServerlessVulnerabilities(ServiceClass):

    def get_vulnerabilities(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetCombinedVulnerabilitiesSARIF = get_vulnerabilities
