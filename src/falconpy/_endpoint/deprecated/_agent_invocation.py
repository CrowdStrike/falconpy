"""Internal API endpoint constant library (deprecated operations)."""

_agent_invocation_endpoints = [
  [
    "GetAgentInvocationV3",
    "GET",
    "/agentic-studio/entities/agent-invocations/v3",
    "Retrieves the list of of messages that are resulted from the specified invocation",
    "agent_invocation",
    [
      {
        "type": "string",
        "description": "Invocation ID",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "InvokeAgentVersionExternalV1",
    "POST",
    "/agentic-studio/entities/agent-version-invocations/v1",
    "Invoke a specific agent version by agent ID and version ID with the specified input. Returns the agent's "

    "completion response.",

    "agent_invocation",
    [
      {
        "description": "Agent version invocation request containing agent ID, version ID and input",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "InvokePublishedAgentExternalV1",
    "POST",
    "/agentic-studio/entities/agent-invocations/v1",
    "Invoke a published agent by ID with the specified input. Returns the agent's completion response.",
    "agent_invocation",
    [
      {
        "description": "Published agent invocation request containing agent ID and input. Optional "

        "deadline_seconds must be at least 90; smaller values are rejected with a 400.",

        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ]
]
