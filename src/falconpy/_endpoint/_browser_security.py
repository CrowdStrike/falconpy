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

_browser_security_endpoints = [
  [
    "CombinedQueryAgents",
    "POST",
    "/seraphic-enterprise-browser/combined/agents/v1",
    "Query agents and return their details in a single call. limit accepts up to 2500.",
    "browser_security",
    [
      {
        "description": "Request body.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ClassifyDomains",
    "POST",
    "/seraphic-enterprise-browser/combined/domain-classifications/v1",
    "Classify domains via the Seraphic Enterprise Browser classification engine.",
    "browser_security",
    [
      {
        "description": "Request body.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ActivateAgents",
    "POST",
    "/seraphic-enterprise-browser/entities/agent-activation/v1",
    "Activate agents by ID.",
    "browser_security",
    [
      {
        "description": "Request body.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeactivateAgents",
    "POST",
    "/seraphic-enterprise-browser/entities/agent-deactivation/v1",
    "Deactivate agents by ID.",
    "browser_security",
    [
      {
        "description": "Request body.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ApplyAgentTasks",
    "POST",
    "/seraphic-enterprise-browser/entities/agent-tasks/v1",
    "Apply tasks to a Seraphic Enterprise Browser agent.",
    "browser_security",
    [
      {
        "type": "string",
        "description": "The agent ID to apply the tasks to.",
        "name": "agent_id",
        "in": "query",
        "required": True
      },
      {
        "description": "Request body.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetAgents",
    "GET",
    "/seraphic-enterprise-browser/entities/agents/v1",
    "Retrieve agents by ID.",
    "browser_security",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "One or more resource IDs.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "GetAuditLogsMixin0",
    "GET",
    "/seraphic-enterprise-browser/entities/audit-logs/v1",
    "Retrieve audit log entries by ID.",
    "browser_security",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "One or more resource IDs.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "GetDestinationGroups",
    "GET",
    "/seraphic-enterprise-browser/entities/destination-groups/v1",
    "Retrieve destination groups by ID.",
    "browser_security",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "One or more resource IDs.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "CreateDestinationGroup",
    "POST",
    "/seraphic-enterprise-browser/entities/destination-groups/v1",
    "Create a destination group.",
    "browser_security",
    [
      {
        "description": "Request body.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteDestinationGroup",
    "DELETE",
    "/seraphic-enterprise-browser/entities/destination-groups/v1",
    "Delete a destination group.",
    "browser_security",
    [
      {
        "type": "string",
        "description": "The resource ID.",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "UpdateDestinationGroup",
    "PATCH",
    "/seraphic-enterprise-browser/entities/destination-groups/v1",
    "Partial-update a destination group.",
    "browser_security",
    [
      {
        "type": "string",
        "description": "The resource ID.",
        "name": "id",
        "in": "query",
        "required": True
      },
      {
        "description": "Request body.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetExtensionAnalysis",
    "GET",
    "/seraphic-enterprise-browser/entities/extension-analysis/v1",
    "Retrieve browser-extension risk analysis by store and extension ID.",
    "browser_security",
    [
      {
        "type": "string",
        "description": "The extension store.",
        "name": "store",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "The extension ID.",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "GetRules",
    "GET",
    "/seraphic-enterprise-browser/entities/rules/v1",
    "Retrieve rules by ID.",
    "browser_security",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "One or more resource IDs.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "UpdateRuleMixin0",
    "PATCH",
    "/seraphic-enterprise-browser/entities/rules/v1",
    "Partial-update a rule (extensions, targets, destination groups, status).",
    "browser_security",
    [
      {
        "type": "string",
        "description": "The resource ID.",
        "name": "id",
        "in": "query",
        "required": True
      },
      {
        "description": "Request body.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetTenantSettings",
    "GET",
    "/seraphic-enterprise-browser/entities/tenant-settings/v1",
    "Retrieve Seraphic Enterprise Browser tenant settings.",
    "browser_security",
    []
  ],
  [
    "GetUrlDomainLists",
    "GET",
    "/seraphic-enterprise-browser/entities/url-domain-lists/v1",
    "Retrieve URL/domain integration lists by ID.",
    "browser_security",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "One or more resource IDs.",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "type": "integer",
        "description": "Number of items to skip. Default 0.",
        "name": "skip",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Maximum items to return. Default 50.",
        "name": "limit",
        "in": "query"
      }
    ]
  ],
  [
    "AddUrlDomainList",
    "POST",
    "/seraphic-enterprise-browser/entities/url-domain-lists/v1",
    "Add URLs and domains to an integration list.",
    "browser_security",
    [
      {
        "description": "Request body.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteUrlDomainList",
    "DELETE",
    "/seraphic-enterprise-browser/entities/url-domain-lists/v1",
    "Delete URLs and domains from an integration list.",
    "browser_security",
    [
      {
        "type": "string",
        "description": "The resource ID.",
        "name": "id",
        "in": "query",
        "required": True
      },
      {
        "description": "Request body.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "QueryAgents",
    "POST",
    "/seraphic-enterprise-browser/queries/agents/v1",
    "Query agent IDs by filter, sort and pagination. limit accepts up to 1000.",
    "browser_security",
    [
      {
        "description": "Request body.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "QueryDestinationGroups",
    "POST",
    "/seraphic-enterprise-browser/queries/destination-groups/v1",
    "Query destination groups by filter, sort and pagination.",
    "browser_security",
    [
      {
        "description": "Request body.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "QueryRulesMixin0",
    "POST",
    "/seraphic-enterprise-browser/queries/rules/v1",
    "Query rules within a category by filter, sort and pagination.",
    "browser_security",
    [
      {
        "type": "string",
        "description": "The rule category to query.",
        "name": "category",
        "in": "query",
        "required": True
      },
      {
        "description": "Request body.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ]
]
