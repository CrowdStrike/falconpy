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

_workflows_endpoints = [
  [
    "WorkflowExecute",
    "POST",
    "/workflows/entities/execute/v1",
    "Executes an on-demand Workflow, the body is JSON used to trigger the execution, the response the execution ID(s)",
    "workflows",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Definition ID to execute, either a name or an ID can be specified.",
        "name": "definition_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Workflow name to execute, either a name or an ID can be specified.",
        "name": "name",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Key used to help deduplicate executions, if unset a new UUID is used",
        "name": "key",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Used to record the execution depth to help limit execution "
        "loops when a workflow triggers another. The maximum depth is 4.",
        "name": "depth",
        "in": "query"
      },
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "WorkflowExecutionsAction",
    "POST",
    "/workflows/entities/execution-actions/v1",
    "Allows a user to resume/retry a failed workflow execution.",
    "workflows",
    [
      {
        "enum": [
          "resume"
        ],
        "type": "string",
        "description": "Specify one of these actions:\n\n- `resume`: resume/retry the workflow execution(s) specified in ids",
        "name": "action_name",
        "in": "query",
        "required": True
      },
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "WorkflowExecutionResults",
    "GET",
    "/workflows/entities/execution-results/v1",
    "Get execution result of a given execution",
    "workflows",
    [
      {
        "maxItems": 500,
        "minItems": 1,
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "workflow execution id to return results for.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "WorkflowSystemDefinitionsDeProvision",
    "POST",
    "/workflows/system-definitions/deprovision/v1",
    "Deprovisions a system definition that was previously provisioned on the target CID",
    "workflows",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "WorkflowSystemDefinitionsPromote",
    "POST",
    "/workflows/system-definitions/promote/v1",
    "Promotes a version of a system definition on a customer. "
    "The customer must already have been provisioned. This allows the callerto apply an "
    "updated template version to a specific cid and expects all parameters to be supplied. "
    "If the template supports multi-instancethe customer scope definition ID must be supplied "
    "to determine which customer workflow should be updated.",
    "workflows",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "WorkflowSystemDefinitionsProvision",
    "POST",
    "/workflows/system-definitions/provision/v1",
    "Provisions a system definition onto the target CID by using the template and provided parameters",
    "workflows",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ]
]
