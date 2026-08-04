"""Type stubs for agent_templates."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class AgentTemplates(ServiceClass):

    def entities_agent_templates_v1(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def queries_agent_templates_v1(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    EntitiesAgentTemplatesV1 = entities_agent_templates_v1
    QueriesAgentTemplatesV1 = queries_agent_templates_v1
