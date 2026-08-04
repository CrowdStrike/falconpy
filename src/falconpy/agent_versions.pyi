"""Type stubs for agent_versions."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class AgentVersions(ServiceClass):

    def get_agent_versions_v1(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_agent_versions_v1(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetAgentVersionsV1 = get_agent_versions_v1
    QueryAgentVersionsV1 = query_agent_versions_v1
