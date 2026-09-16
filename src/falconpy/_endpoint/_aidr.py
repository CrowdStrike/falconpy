"""Internal API endpoint constant library.

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
# pylint: disable=C0302

_aidr_endpoints = [
  [
    "aggregateAgentSessionsV1",
    "GET",
    "/aidr/aggregates/agent-sessions/v1",
    "Aggregate agent-session counts by product",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by AI product name (e.g., CLAUDE_CODE, CURSOR)",
        "name": "product",
        "in": "query"
      }
    ]
  ],
  [
    "aggregateAgentsV1",
    "GET",
    "/aidr/aggregates/agents/v1",
    "Aggregate agent counts by product",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      }
    ]
  ],
  [
    "aggregateDetectionsV1",
    "GET",
    "/aidr/aggregates/detections/v1",
    "Max detection severity per agent and product",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by agent ID (see endpoint notes: some use the 64-hex AIAgent.Id, detections use "
        "the 32-hex SensorId)",
        "name": "agent_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by AI product name (e.g., CLAUDE_CODE, CURSOR)",
        "name": "product",
        "in": "query"
      }
    ]
  ],
  [
    "aggregateSkillUsageV1",
    "GET",
    "/aidr/aggregates/skill-usage/v1",
    "Aggregate skill invocation counts by name (LogScale)",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 2h, 24h). Max 7d; defaults to 2h if omitted (LogScale-backed)",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by AgenticSessionId",
        "name": "session_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by sensor ID (aid) — identifies a host, not a single agent",
        "name": "aid",
        "in": "query"
      }
    ]
  ],
  [
    "aggregateSkillsV1",
    "GET",
    "/aidr/aggregates/skills/v1",
    "Aggregate skill usage counts by name",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by name pattern (supports wildcards via like)",
        "name": "name_filter",
        "in": "query"
      }
    ]
  ],
  [
    "aggregateToolUsageV1",
    "GET",
    "/aidr/aggregates/tool-usage/v1",
    "Aggregate tool invocation counts by name (LogScale)",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 2h, 24h). Max 7d; defaults to 2h if omitted (LogScale-backed)",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by AgenticSessionId",
        "name": "session_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by sensor ID (aid) — identifies a host, not a single agent",
        "name": "aid",
        "in": "query"
      }
    ]
  ],
  [
    "aggregateToolsV1",
    "GET",
    "/aidr/aggregates/tools/v1",
    "Aggregate tool usage counts by name",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by sensor ID (32-hex aid / AIAgent.SensorId)",
        "name": "sensor_id",
        "in": "query"
      }
    ]
  ],
  [
    "entitiesAgentInstallationsV1",
    "GET",
    "/aidr/entities/agent-installations/v1",
    "Get AI agent installation details by IDs",
    "aidr",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "One or more installation IDs (repeatable). Use the Id value from queryAgentInstallationsV1",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "entitiesAgentOSUsersV1",
    "GET",
    "/aidr/entities/agent-os-users/v1",
    "Get an OS user by aid + username",
    "aidr",
    [
      {
        "type": "string",
        "description": "The OS user's sensor ID (aid). Required — AIAgentOSUser is keyed on Aid + Username.",
        "name": "aid",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "The OS username. Required — AIAgentOSUser is keyed on Aid + Username.",
        "name": "username",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "entitiesAgentSessionsV1",
    "GET",
    "/aidr/entities/agent-sessions/v1",
    "Get AI agent session details by IDs",
    "aidr",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "One or more session IDs (repeatable: ids=A&ids=B). Use the Id value from "
        "queryAgentSessionsV1 This is the AIAgentSession entity key, not a ThreatGraph vertex key.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "entitiesAgentsV1",
    "GET",
    "/aidr/entities/agents/v1",
    "Get AI agent details by IDs",
    "aidr",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "One or more AIAgent IDs (repeatable: ids=A&ids=B). This is the 64-hex content hash "
        "from the Id field of queryAgentsV1 — NOT the 32-hex SensorId.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "entitiesClassifiedFileAccessV1",
    "GET",
    "/aidr/entities/classified-file-access/v1",
    "Get FDP classified file access for a process",
    "aidr",
    [
      {
        "type": "string",
        "description": "A process vertex ID of the form pid:{aid}:{process_id}. Obtain it from a process node "
        "in entitiesProcessTreeV1 or entitiesSessionActivityV1 (the process __id). A session ID is NOT accepted here — "
        "this endpoint does not resolve it.",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "entitiesExecutionsV1",
    "GET",
    "/aidr/entities/executions/v1",
    "Get AI agent execution detail by session ID",
    "aidr",
    [
      {
        "type": "string",
        "description": "A session ID (AgenticSessionId from queryExecutionsV1 or queryAgentSessionsV1). "
        "Returns the process invocation(s) for that session; add context_process_id to narrow to a single execution.",
        "name": "id",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "Narrow an execution to a single process invocation (ContextProcessId from queryExecutionsV1)",
        "name": "context_process_id",
        "in": "query"
      }
    ]
  ],
  [
    "entitiesFileEventsV1",
    "GET",
    "/aidr/entities/file-events/v1",
    "Get file write activity from AI session processes",
    "aidr",
    [
      {
        "type": "string",
        "description": "A session ID. Accepts either the AgenticSessionId from queryExecutionsV1 (resolved "
        "automatically) or a ThreatGraph vertex key aisess:{aid}:{session_id}. This is session-scoped — pass a session "
        "ID, not a process ID.",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "entitiesModelNamesV1",
    "GET",
    "/aidr/entities/model-names/v1",
    "Get AI model name details by IDs",
    "aidr",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "One or more AIModelName IDs (repeatable). Use the Id value from queryModelNamesV1",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "entitiesNetworkEventsV1",
    "GET",
    "/aidr/entities/network-events/v1",
    "Get outbound network connections from AI session processes",
    "aidr",
    [
      {
        "type": "string",
        "description": "A session ID. Accepts either the AgenticSessionId from queryExecutionsV1 (resolved "
        "automatically) or a ThreatGraph vertex key aisess:{aid}:{session_id}. This is session-scoped — pass a session "
        "ID, not a process ID.",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "entitiesProcessTreeV1",
    "GET",
    "/aidr/entities/process-tree/v1",
    "Get spawned process tree for an AI session",
    "aidr",
    [
      {
        "type": "string",
        "description": "A session ID. Accepts either the AgenticSessionId from queryExecutionsV1 (resolved "
        "automatically) or a ThreatGraph vertex key aisess:{aid}:{session_id}. This is session-scoped — pass a session "
        "ID, not a process ID.",
        "name": "id",
        "in": "query",
        "required": True
      },
      {
        "type": "integer",
        "description": "Process tree depth (1=direct spawns, 2=grandchildren, 3=max). Default 2",
        "name": "depth",
        "in": "query"
      }
    ]
  ],
  [
    "entitiesSessionActivityV1",
    "GET",
    "/aidr/entities/session-activity/v1",
    "Get ThreatGraph session activity (tools, models, processes)",
    "aidr",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "One or more session IDs (repeatable). Accepts either the AgenticSessionId from "
        "queryExecutionsV1 (resolved to a graph vertex automatically) or a ThreatGraph vertex key "
        "aisess:{aid}:{session_id} (aid = the session's aid; the sess- prefix is stripped).",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "entitiesSkillsV1",
    "GET",
    "/aidr/entities/skills/v1",
    "Get AI skill frontmatter details by IDs",
    "aidr",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "One or more skill frontmatter IDs (repeatable). Use the Id value from querySkillsV1",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "entitiesToolsV1",
    "GET",
    "/aidr/entities/tools/v1",
    "Get AI tool details by IDs",
    "aidr",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "One or more AITool IDs (repeatable: ids=A&ids=B). Use the Id value from queryToolsV1",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "queryAgentInstallationsV1",
    "GET",
    "/aidr/queries/agent-installations/v1",
    "List AI agent installations",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by sensor ID (32-hex aid / AIAgent.SensorId)",
        "name": "sensor_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by AI product name (e.g., CLAUDE_CODE, CURSOR)",
        "name": "product",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by hostname of the device running the agent",
        "name": "hostname",
        "in": "query"
      }
    ]
  ],
  [
    "queryAgentOSUsersV1",
    "GET",
    "/aidr/queries/agent-os-users/v1",
    "List OS users that ran AI agents",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by the OS user's ObjectSid (AD security identifier)",
        "name": "object_sid",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by sensor ID (aid) — identifies a host, not a single agent",
        "name": "aid",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by OS username",
        "name": "username",
        "in": "query"
      }
    ]
  ],
  [
    "queryAgentSessionsV1",
    "GET",
    "/aidr/queries/agent-sessions/v1",
    "List AI agent sessions",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by AI product name (e.g., CLAUDE_CODE, CURSOR)",
        "name": "product",
        "in": "query"
      }
    ]
  ],
  [
    "queryAgentsV1",
    "GET",
    "/aidr/queries/agents/v1",
    "List AI agent instances",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by AI product name (e.g., CLAUDE_CODE, CURSOR)",
        "name": "product",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by hostname of the device running the agent",
        "name": "hostname",
        "in": "query"
      }
    ]
  ],
  [
    "queryDetectionsV1",
    "GET",
    "/aidr/queries/detections/v1",
    "List detections involving AI agent processes",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by agent ID (see endpoint notes: some use the 64-hex AIAgent.Id, detections use "
        "the 32-hex SensorId)",
        "name": "agent_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by AI product name (e.g., CLAUDE_CODE, CURSOR)",
        "name": "product",
        "in": "query"
      }
    ]
  ],
  [
    "queryExecutionsV1",
    "GET",
    "/aidr/queries/executions/v1",
    "List AI agent process executions",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 2h, 24h). Max 7d; defaults to 2h if omitted (LogScale-backed)",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by AgenticSessionId",
        "name": "session_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by sensor ID (aid) — identifies a host, not a single agent",
        "name": "aid",
        "in": "query"
      }
    ]
  ],
  [
    "queryMcpServerNamesV1",
    "GET",
    "/aidr/queries/mcp-server-names/v1",
    "List MCP server names",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      }
    ]
  ],
  [
    "queryModelNamesV1",
    "GET",
    "/aidr/queries/model-names/v1",
    "List AI model names",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      }
    ]
  ],
  [
    "queryPromptsV1",
    "GET",
    "/aidr/queries/prompts/v1",
    "List AI prompt records",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 2h, 24h). Max 7d; defaults to 2h if omitted (LogScale-backed)",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by AgenticSessionId",
        "name": "session_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by sensor ID (aid) — identifies a host, not a single agent",
        "name": "aid",
        "in": "query"
      }
    ]
  ],
  [
    "querySkillUsageV1",
    "GET",
    "/aidr/queries/skill-usage/v1",
    "List AI skill invocations (LogScale, session-scoped)",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 2h, 24h). Max 7d; defaults to 2h if omitted (LogScale-backed)",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter skill invocations by skill name (matches AgenticSkill exactly)",
        "name": "name",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by AgenticSessionId",
        "name": "session_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by sensor ID (aid) — identifies a host, not a single agent",
        "name": "aid",
        "in": "query"
      }
    ]
  ],
  [
    "querySkillsV1",
    "GET",
    "/aidr/queries/skills/v1",
    "List AI skill frontmatters",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by name pattern (supports wildcards via like)",
        "name": "name_filter",
        "in": "query"
      }
    ]
  ],
  [
    "queryToolUsageV1",
    "GET",
    "/aidr/queries/tool-usage/v1",
    "List AI tool invocations (LogScale, session-scoped)",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 2h, 24h). Max 7d; defaults to 2h if omitted (LogScale-backed)",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter tool invocations by tool name (e.g., Bash, Read, Write, Edit)",
        "name": "tool_name",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by AgenticSessionId",
        "name": "session_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by sensor ID (aid) — identifies a host, not a single agent",
        "name": "aid",
        "in": "query"
      }
    ]
  ],
  [
    "queryToolsV1",
    "GET",
    "/aidr/queries/tools/v1",
    "List AI tools",
    "aidr",
    [
      {
        "type": "integer",
        "description": "Maximum number of results to return (1-500, default 50)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Pagination offset (0-1000)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Lookback period (e.g., 7d, 24h). Max 90d",
        "name": "time_range",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter by sensor ID (32-hex aid / AIAgent.SensorId)",
        "name": "sensor_id",
        "in": "query"
      }
    ]
  ]
]
