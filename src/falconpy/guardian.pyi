"""Type stubs for guardian."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Guardian(ServiceClass):

    def aggregate_aidr_agent_sessions(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        product: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_aidr_agents(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_aidr_detections(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        agent_id: Optional[str] = None,
        product: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_aidr_skill_usage(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        session_id: Optional[str] = None,
        aid: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_aidr_skills(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        name_filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_aidr_tool_usage(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        session_id: Optional[str] = None,
        aid: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_aidr_tools(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        sensor_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aidr_agent_installations(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aidr_agent_os_users(
        self,
        *,
        aid: Optional[str] = None,
        username: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aidr_agent_sessions(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aidr_agents(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aidr_classified_file_access(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aidr_executions(
        self,
        *,
        id: Optional[str] = None,
        context_process_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aidr_file_events(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aidr_model_names(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aidr_network_events(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aidr_process_tree(
        self,
        *,
        id: Optional[str] = None,
        depth: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aidr_session_activity(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aidr_skills(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aidr_tools(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aidr_agent_installations(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        sensor_id: Optional[str] = None,
        product: Optional[str] = None,
        hostname: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aidr_agent_os_users(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        object_sid: Optional[str] = None,
        aid: Optional[str] = None,
        username: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aidr_agent_sessions(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        product: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aidr_agents(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        product: Optional[str] = None,
        hostname: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aidr_detections(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        agent_id: Optional[str] = None,
        product: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aidr_executions(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        session_id: Optional[str] = None,
        aid: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aidr_mcp_server_names(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aidr_model_names(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aidr_prompts(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        session_id: Optional[str] = None,
        aid: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aidr_skill_usage(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        name: Optional[str] = None,
        session_id: Optional[str] = None,
        aid: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aidr_skills(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        name_filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aidr_tool_usage(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        tool_name: Optional[str] = None,
        session_id: Optional[str] = None,
        aid: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_aidr_tools(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
        sensor_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    aggregateAgentSessionsV1 = aggregate_aidr_agent_sessions
    aggregateAgentsV1 = aggregate_aidr_agents
    aggregateDetectionsV1 = aggregate_aidr_detections
    aggregateSkillUsageV1 = aggregate_aidr_skill_usage
    aggregateSkillsV1 = aggregate_aidr_skills
    aggregateToolUsageV1 = aggregate_aidr_tool_usage
    aggregateToolsV1 = aggregate_aidr_tools
    entitiesAgentInstallationsV1 = get_aidr_agent_installations
    entitiesAgentOSUsersV1 = get_aidr_agent_os_users
    entitiesAgentSessionsV1 = get_aidr_agent_sessions
    entitiesAgentsV1 = get_aidr_agents
    entitiesClassifiedFileAccessV1 = get_aidr_classified_file_access
    entitiesExecutionsV1 = get_aidr_executions
    entitiesFileEventsV1 = get_aidr_file_events
    entitiesModelNamesV1 = get_aidr_model_names
    entitiesNetworkEventsV1 = get_aidr_network_events
    entitiesProcessTreeV1 = get_aidr_process_tree
    entitiesSessionActivityV1 = get_aidr_session_activity
    entitiesSkillsV1 = get_aidr_skills
    entitiesToolsV1 = get_aidr_tools
    queryAgentInstallationsV1 = query_aidr_agent_installations
    queryAgentOSUsersV1 = query_aidr_agent_os_users
    queryAgentSessionsV1 = query_aidr_agent_sessions
    queryAgentsV1 = query_aidr_agents
    queryDetectionsV1 = query_aidr_detections
    queryExecutionsV1 = query_aidr_executions
    queryMcpServerNamesV1 = query_aidr_mcp_server_names
    queryModelNamesV1 = query_aidr_model_names
    queryPromptsV1 = query_aidr_prompts
    querySkillUsageV1 = query_aidr_skill_usage
    querySkillsV1 = query_aidr_skills
    queryToolUsageV1 = query_aidr_tool_usage
    queryToolsV1 = query_aidr_tools
