"""Type stubs for tools."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Tools(ServiceClass):

    def entities_tools_v1(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def queries_tools_v1(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    EntitiesToolsV1 = entities_tools_v1
    QueriesToolsV1 = queries_tools_v1
