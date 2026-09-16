"""Type stubs for agent_templates."""
from typing import Dict, List, Optional, Union
from typing_extensions import deprecated
from ._service_class import ServiceClass
from ._result import Result


class AgentTemplates(ServiceClass):

    def entities_agent_templates_v1(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    @deprecated("This operation is no longer available in CrowdStrike's API. Calling this method will result in an error from the API.")
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
