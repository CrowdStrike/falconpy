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

_agent_invocation_endpoints = [
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
  ],
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
  ]
]
