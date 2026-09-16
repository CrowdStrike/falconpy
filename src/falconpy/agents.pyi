"""Type stubs for agents."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Agents(ServiceClass):

    def delete_agent(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_studio_agents(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_or_update_agent(
        self,
        *,
        duplicate_from_agent_id: Optional[str] = None,
        id: Optional[str] = None,
        template_id: Optional[str] = None,
        version_definition: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_agent(
        self,
        *,
        id: Optional[str] = None,
        dry_run: Optional[bool] = None,
        is_enabled: Optional[bool] = None,
        is_published: Optional[bool] = None,
        version_id: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_studio_agents(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    DeleteAgentV1 = delete_agent
    GetAgentsV2 = get_studio_agents
    CreateOrEditAgentExternalV3 = create_or_update_agent
    PatchAgentExternalV3 = update_agent
    QueryAgentsV2 = query_studio_agents
