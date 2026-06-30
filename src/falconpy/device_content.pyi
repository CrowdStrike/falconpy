"""Type stubs for device_content."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class DeviceContent(ServiceClass):

    def get_states(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_states(
        self,
        *,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    entities_states_v1 = get_states
    queries_states_v1 = query_states
