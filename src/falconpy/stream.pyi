"""Type stubs for stream."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Stream(ServiceClass):

    def stream_invocation_response_v1(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    StreamInvocationResponseV1 = stream_invocation_response_v1
