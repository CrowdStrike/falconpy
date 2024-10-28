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

_aspm_endpoints = [
  [
    "UpsertBusinessApplications",
    "PUT",
    "/aspm-api-gateway/api/v1/business_applications",
    "Create or Update Business Applications",
    "aspm",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetExecutorNodes",
    "GET",
    "/aspm-api-gateway/api/v1/executor_nodes",
    "Get all the relay nodes",
    "aspm",
    [
      {
        "type": "string",
        "name": "node_type",
        "in": "query",
        "required": True
      },
      {
        "type": "integer",
        "name": "integration_type",
        "in": "query"
      }
    ]
  ],
  [
    "UpdateExecutorNode",
    "PUT",
    "/aspm-api-gateway/api/v1/executor_nodes",
    "Update an existing relay node",
    "aspm",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "CreateExecutorNode",
    "POST",
    "/aspm-api-gateway/api/v1/executor_nodes",
    "Create a new relay node",
    "aspm",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteExecutorNode",
    "DELETE",
    "/aspm-api-gateway/api/v1/executor_nodes/{}",
    "Delete a relay node",
    "aspm",
    [
      {
        "pattern": "[0-9]+",
        "type": "integer",
        "name": "ID",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "GetIntegrationTasks",
    "GET",
    "/aspm-api-gateway/api/v1/integration_tasks",
    "Get all the integration tasks",
    "aspm",
    [
      {
        "type": "integer",
        "name": "integration_task_type",
        "in": "query"
      },
      {
        "type": "string",
        "name": "category",
        "in": "query"
      }
    ]
  ],
  [
    "CreateIntegrationTask",
    "POST",
    "/aspm-api-gateway/api/v1/integration_tasks",
    "Create new integration task.",
    "aspm",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "UpdateIntegrationTask",
    "PUT",
    "/aspm-api-gateway/api/v1/integration_tasks/{}",
    "Update an existing integration task by its ID",
    "aspm",
    [
      {
        "pattern": "[0-9]+",
        "type": "integer",
        "name": "ID",
        "in": "path",
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
    "DeleteIntegrationTask",
    "DELETE",
    "/aspm-api-gateway/api/v1/integration_tasks/{}",
    "Delete an existing integration task by its ID",
    "aspm",
    [
      {
        "pattern": "[0-9]+",
        "type": "integer",
        "name": "ID",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "RunIntegrationTask",
    "POST",
    "/aspm-api-gateway/api/v1/integration_tasks/{}/run",
    "Run an integration task by its ID",
    "aspm",
    [
      {
        "pattern": "[0-9]+",
        "type": "integer",
        "name": "ID",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "name": "category",
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
    "GetIntegrationTypes",
    "GET",
    "/aspm-api-gateway/api/v1/integration_types",
    "Get all the integration types",
    "aspm",
    []
  ],
  [
    "GetIntegrations",
    "GET",
    "/aspm-api-gateway/api/v1/integrations",
    "Get a list of all the integrations",
    "aspm",
    [
      {
        "type": "integer",
        "name": "integration_type",
        "in": "query"
      },
      {
        "type": "string",
        "name": "category",
        "in": "query"
      }
    ]
  ],
  [
    "CreateIntegration",
    "POST",
    "/aspm-api-gateway/api/v1/integrations",
    "Create a new integration",
    "aspm",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "UpdateIntegration",
    "PUT",
    "/aspm-api-gateway/api/v1/integrations/{}",
    "Update an existing integration by its ID",
    "aspm",
    [
      {
        "pattern": "[0-9]+",
        "type": "integer",
        "name": "ID",
        "in": "path",
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
    "DeleteIntegration",
    "DELETE",
    "/aspm-api-gateway/api/v1/integrations/{}",
    "Delete an existing integration by its ID",
    "aspm",
    [
      {
        "pattern": "[0-9]+",
        "type": "integer",
        "name": "ID",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "ExecuteQuery",
    "POST",
    "/aspm-api-gateway/api/v1/query",
    "Execute a query. The syntax used is identical to that of the query page.",
    "aspm",
    [
      {
        "description": " **params details:**\n- selectFields:\n- **fields** - For filtering relevant fields "
        "only.\n- **withoutServices** - Default is set to **true**, you will not receive information about the "
        "services. If you want to get the relevant service, set to **false**.\n- **serviceFields**-  For filtering "
        "relevant fields of the service (if you chose to get it)",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ServiceNowGetDeployments",
    "GET",
    "/aspm-api-gateway/api/v1/servicenow/deployments",
    "",
    "aspm",
    [
      {
        "type": "string",
        "name": "ql_filters",
        "in": "query"
      },
      {
        "type": "integer",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "name": "orderBy",
        "in": "query"
      },
      {
        "type": "string",
        "name": "direction",
        "in": "query"
      }
    ]
  ],
  [
    "ServiceNowGetServices",
    "GET",
    "/aspm-api-gateway/api/v1/servicenow/services",
    "",
    "aspm",
    [
      {
        "type": "string",
        "name": "ql_filters",
        "in": "query"
      },
      {
        "type": "integer",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "name": "orderBy",
        "in": "query"
      },
      {
        "type": "string",
        "name": "direction",
        "in": "query"
      }
    ]
  ],
  [
    "GetServicesCount",
    "POST",
    "/aspm-api-gateway/api/v1/services/count",
    "Get the total amount of existing services",
    "aspm",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetServiceViolationTypes",
    "GET",
    "/aspm-api-gateway/api/v1/services/violations/types",
    "Get the different types of violation",
    "aspm",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetTags",
    "GET",
    "/aspm-api-gateway/api/v1/tags",
    "Get all the tags",
    "aspm",
    [
      {
        "type": "boolean",
        "name": "isUnique",
        "in": "query"
      },
      {
        "type": "string",
        "name": "tagName",
        "in": "query"
      },
      {
        "type": "integer",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "name": "name",
        "in": "query"
      }
    ]
  ],
  [
    "UpsertTags",
    "PUT",
    "/aspm-api-gateway/api/v1/tags",
    "Create new or update existing tag. You can update unique tags table or regular tags table",
    "aspm",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteTags",
    "POST",
    "/aspm-api-gateway/api/v1/tags",
    "Remove existing tags",
    "aspm",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ]
]
