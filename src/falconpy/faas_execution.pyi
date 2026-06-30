"""Type stubs for faas_execution."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class FaaSExecution(ServiceClass):

    def read_request_body(
        self,
        *,
        id: Optional[str] = None,
        fn: Optional[str] = None,
        filename: Optional[str] = None,
        sha256: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ReadRequestBody = read_request_body
