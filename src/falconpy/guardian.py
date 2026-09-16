"""CrowdStrike Falcon Guardian API interface class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
# pylint: disable=C0302,R0904
from typing import Dict, Union
from ._util import force_default, process_service_request, handle_single_argument
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._guardian import _guardian_endpoints as Endpoints


class Guardian(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (oauth2.py)
    """

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_aidr_agent_sessions(self: object,
                                      parameters: dict = None,
                                      **kwargs
                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Aggregate agent-session counts by product.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/aggregateAgentSessionsV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        product : str
            Filter by AI product name (e.g., CLAUDE_CODE, CURSOR)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregateAgentSessionsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_aidr_agents(self: object,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Aggregate agent counts by product.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/aggregateAgentsV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregateAgentsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_aidr_detections(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Max detection severity per agent and product.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/aggregateDetectionsV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        agent_id : str
            Filter by agent ID (see endpoint notes: some use the 64-hex AIAgent.Id, detections use the 32-hex
            SensorId)
        product : str
            Filter by AI product name (e.g., CLAUDE_CODE, CURSOR)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregateDetectionsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_aidr_skill_usage(self: object,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Aggregate skill invocation counts by name (LogScale).

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/aggregateSkillUsageV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 2h, 24h). Max 7d; defaults to 2h if omitted (LogScale-backed)
        session_id : str
            Filter by AgenticSessionId.
        aid : str
            Filter by sensor ID (aid) — identifies a host, not a single agent.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregateSkillUsageV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_aidr_skills(self: object,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Aggregate skill usage counts by name.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/aggregateSkillsV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        name_filter : str
            Filter by name pattern (supports wildcards via like)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregateSkillsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_aidr_tool_usage(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Aggregate tool invocation counts by name (LogScale).

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/aggregateToolUsageV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 2h, 24h). Max 7d; defaults to 2h if omitted (LogScale-backed)
        session_id : str
            Filter by AgenticSessionId.
        aid : str
            Filter by sensor ID (aid) — identifies a host, not a single agent.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregateToolUsageV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_aidr_tools(self: object,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Aggregate tool usage counts by name.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/aggregateToolsV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        sensor_id : str
            Filter by sensor ID (32-hex aid / AIAgent.SensorId)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="aggregateToolsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aidr_agent_installations(self: object,
                                     *args,
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get AI agent installation details by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/entitiesAgentInstallationsV1

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more installation IDs (repeatable). Use the Id value from queryAgentInstallationsV1.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entitiesAgentInstallationsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aidr_agent_os_users(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get an OS user by aid + username.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/entitiesAgentOSUsersV1

        Keyword arguments
        -----------------
        aid : str
            The OS user's sensor ID (aid). Required — AIAgentOSUser is keyed on Aid + Username.
        username : str
            The OS username. Required — AIAgentOSUser is keyed on Aid + Username.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entitiesAgentOSUsersV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aidr_agent_sessions(self: object,
                                *args,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get AI agent session details by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/entitiesAgentSessionsV1

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more session IDs (repeatable: ids=A&ids=B). Use the Id value from queryAgentSessionsV1 This is the
            AIAgentSession entity key, not a ThreatGraph vertex key.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entitiesAgentSessionsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aidr_agents(self: object,
                        *args,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get AI agent details by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/entitiesAgentsV1

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more AIAgent IDs (repeatable: ids=A&ids=B). This is the 64-hex content hash from the Id field of
            queryAgentsV1 — NOT the 32-hex SensorId.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entitiesAgentsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aidr_classified_file_access(self: object,
                                        *args,
                                        parameters: dict = None,
                                        **kwargs
                                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get FDP classified file access for a process.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/entitiesClassifiedFileAccessV1

        Keyword arguments
        -----------------
        id : str or list[str]
            A process vertex ID of the form pid:{aid}:{process_id}. Obtain it from a process node in entitiesProcessTreeV1 or
            entitiesSessionActivityV1 (the process __id). A session ID is NOT accepted here — this endpoint does not resolve
            it.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entitiesClassifiedFileAccessV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aidr_executions(self: object,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get AI agent execution detail by session ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/entitiesExecutionsV1

        Keyword arguments
        -----------------
        id : str
            A session ID (AgenticSessionId from queryExecutionsV1 or queryAgentSessionsV1). Returns the process invocation(s)
            for that session; add context_process_id to narrow to a single execution.
        context_process_id : str
            Narrow an execution to a single process invocation (ContextProcessId from queryExecutionsV1).
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entitiesExecutionsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aidr_file_events(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get file write activity from AI session processes.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/entitiesFileEventsV1

        Keyword arguments
        -----------------
        id : str or list[str]
            A session ID. Accepts either the AgenticSessionId from queryExecutionsV1 (resolved automatically) or a ThreatGraph
            vertex key aisess:{aid}:{session_id}. This is session-scoped — pass a session ID, not a process ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entitiesFileEventsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aidr_model_names(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get AI model name details by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/entitiesModelNamesV1

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more AIModelName IDs (repeatable). Use the Id value from queryModelNamesV1.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entitiesModelNamesV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aidr_network_events(self: object,
                                *args,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get outbound network connections from AI session processes.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/entitiesNetworkEventsV1

        Keyword arguments
        -----------------
        id : str or list[str]
            A session ID. Accepts either the AgenticSessionId from queryExecutionsV1 (resolved automatically) or a ThreatGraph
            vertex key aisess:{aid}:{session_id}. This is session-scoped — pass a session ID, not a process ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entitiesNetworkEventsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aidr_process_tree(self: object,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get spawned process tree for an AI session.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/entitiesProcessTreeV1

        Keyword arguments
        -----------------
        id : str
            A session ID. Accepts either the AgenticSessionId from queryExecutionsV1 (resolved automatically) or a
            ThreatGraph vertex key aisess:{aid}:{session_id}. This is session-scoped — pass a session ID, not a process ID.
        depth : int
            Process tree depth (1=direct spawns, 2=grandchildren, 3=max). Default 2.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entitiesProcessTreeV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aidr_session_activity(self: object,
                                  *args,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get ThreatGraph session activity (tools, models, processes).

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/entitiesSessionActivityV1

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more session IDs (repeatable). Accepts either the AgenticSessionId from queryExecutionsV1 (resolved to a
            graph vertex automatically) or a ThreatGraph vertex key aisess:{aid}:{session_id} (aid = the session's aid; the
            sess- prefix is stripped)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entitiesSessionActivityV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aidr_skills(self: object,
                        *args,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get AI skill frontmatter details by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/entitiesSkillsV1

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more skill frontmatter IDs (repeatable). Use the Id value from querySkillsV1.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entitiesSkillsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aidr_tools(self: object,
                       *args,
                       parameters: dict = None,
                       **kwargs
                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get AI tool details by IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/entitiesToolsV1

        Keyword arguments
        -----------------
        ids : str or list[str]
            One or more AITool IDs (repeatable: ids=A&ids=B). Use the Id value from queryToolsV1.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="entitiesToolsV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aidr_agent_installations(self: object,
                                       parameters: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List AI agent installations.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/queryAgentInstallationsV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        sensor_id : str
            Filter by sensor ID (32-hex aid / AIAgent.SensorId)
        product : str
            Filter by AI product name (e.g., CLAUDE_CODE, CURSOR)
        hostname : str
            Filter by hostname of the device running the agent.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryAgentInstallationsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aidr_agent_os_users(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List OS users that ran AI agents.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/queryAgentOSUsersV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        object_sid : str
            Filter by the OS user's ObjectSid (AD security identifier)
        aid : str
            Filter by sensor ID (aid) — identifies a host, not a single agent.
        username : str
            Filter by OS username.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryAgentOSUsersV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aidr_agent_sessions(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List AI agent sessions.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/queryAgentSessionsV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        product : str
            Filter by AI product name (e.g., CLAUDE_CODE, CURSOR)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryAgentSessionsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aidr_agents(self: object,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List AI agent instances.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/queryAgentsV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        product : str
            Filter by AI product name (e.g., CLAUDE_CODE, CURSOR)
        hostname : str
            Filter by hostname of the device running the agent.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryAgentsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aidr_detections(self: object,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List detections involving AI agent processes.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/queryDetectionsV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        agent_id : str
            Filter by agent ID (see endpoint notes: some use the 64-hex AIAgent.Id, detections use the 32-hex
            SensorId)
        product : str
            Filter by AI product name (e.g., CLAUDE_CODE, CURSOR)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryDetectionsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aidr_executions(self: object,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List AI agent process executions.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/queryExecutionsV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 2h, 24h). Max 7d; defaults to 2h if omitted (LogScale-backed)
        session_id : str
            Filter by AgenticSessionId.
        aid : str
            Filter by sensor ID (aid) — identifies a host, not a single agent.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryExecutionsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aidr_mcp_server_names(self: object,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List MCP server names.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/queryMcpServerNamesV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryMcpServerNamesV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aidr_model_names(self: object,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List AI model names.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/queryModelNamesV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryModelNamesV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aidr_prompts(self: object,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List AI prompt records.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/queryPromptsV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 2h, 24h). Max 7d; defaults to 2h if omitted (LogScale-backed)
        session_id : str
            Filter by AgenticSessionId.
        aid : str
            Filter by sensor ID (aid) — identifies a host, not a single agent.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryPromptsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aidr_skill_usage(self: object,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List AI skill invocations (LogScale, session-scoped).

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/querySkillUsageV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 2h, 24h). Max 7d; defaults to 2h if omitted (LogScale-backed)
        name : str
            Filter skill invocations by skill name (matches AgenticSkill exactly)
        session_id : str
            Filter by AgenticSessionId.
        aid : str
            Filter by sensor ID (aid) — identifies a host, not a single agent.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="querySkillUsageV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aidr_skills(self: object,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List AI skill frontmatters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/querySkillsV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        name_filter : str
            Filter by name pattern (supports wildcards via like)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="querySkillsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aidr_tool_usage(self: object,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List AI tool invocations (LogScale, session-scoped).

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/queryToolUsageV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 2h, 24h). Max 7d; defaults to 2h if omitted (LogScale-backed)
        tool_name : str
            Filter tool invocations by tool name (e.g., Bash, Read, Write, Edit)
        session_id : str
            Filter by AgenticSessionId.
        aid : str
            Filter by sensor ID (aid) — identifies a host, not a single agent.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryToolUsageV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_aidr_tools(self: object,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List AI tools.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/guardian/queryToolsV1

        Keyword arguments
        -----------------
        limit : int
            Maximum number of results to return (1-500, default 50)
        offset : int
            Pagination offset (0-1000)
        time_range : str
            Lookback period (e.g., 7d, 24h). Max 90d.
        sensor_id : str
            Filter by sensor ID (32-hex aid / AIAgent.SensorId)
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="queryToolsV1",
            keywords=kwargs,
            params=parameters
            )
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
