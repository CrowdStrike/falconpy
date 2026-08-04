"""Type stubs for agent_invocation."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class AgentInvocation(ServiceClass):

    def invoke_published_agent_external_v1(
        self,
        *,
        credit_cents_limit: Optional[int] = None,
        deadline_seconds: Optional[int] = None,
        id: Optional[str] = None,
        messages: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_agent_invocation_v3(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def invoke_agent_version_external_v1(
        self,
        *,
        credit_cents_limit: Optional[int] = None,
        deadline_seconds: Optional[int] = None,
        id: Optional[str] = None,
        messages: Optional[list] = None,
        version_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    InvokePublishedAgentExternalV1 = invoke_published_agent_external_v1
    GetAgentInvocationV3 = get_agent_invocation_v3
    InvokeAgentVersionExternalV1 = invoke_agent_version_external_v1
