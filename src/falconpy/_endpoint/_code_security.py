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

_code_security_endpoints = [
  [
    "GetSCMRepositoryAggregates",
    "GET",
    "/scm-integration/aggregates/repositories/values-by-field/v1",
    "Get distinct values with counts for a repository field",
    "code_security",
    [
      {
        "type": "string",
        "description": "Field to aggregate: name, primary_language, visibility, artifact_types, topics, "
        "owner_org, default_branch",
        "name": "field",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "FQL filter expression to scope aggregation",
        "name": "filter",
        "in": "query"
      }
    ]
  ],
  [
    "GetBranchConfig",
    "GET",
    "/scm-integration/entities/branch-configs/v1",
    "Get branch config for a connection or repository",
    "code_security",
    [
      {
        "type": "string",
        "description": "Connection UUID",
        "name": "connection_id",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "Comma-separated Repository UUIDs (optional, for per-repo or bulk query)",
        "name": "repository_ids",
        "in": "query"
      }
    ]
  ],
  [
    "CreateBranchConfig",
    "POST",
    "/scm-integration/entities/branch-configs/v1",
    "Create a new branch config",
    "code_security",
    []
  ],
  [
    "DeleteBranchConfig",
    "DELETE",
    "/scm-integration/entities/branch-configs/v1",
    "Delete a branch config, or exclude a specific repository from a connection-level config when "
    "repository_id query param is provided",
    "code_security",
    [
      {
        "type": "string",
        "description": "Branch config UUID",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "UpdateBranchConfig",
    "PATCH",
    "/scm-integration/entities/branch-configs/v1",
    "Update an existing branch config",
    "code_security",
    [
      {
        "type": "string",
        "description": "Branch config UUID",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "ListSCMConnections",
    "GET",
    "/scm-integration/entities/connections/v1",
    "List SCM connections for a customer",
    "code_security",
    [
      {
        "type": "string",
        "description": "Filter by provider (github, gitlab, azure_devops)",
        "name": "provider",
        "in": "query"
      }
    ]
  ],
  [
    "GetSCMConnection",
    "GET",
    "/scm-integration/entities/connections/v1/{uuid}",
    "Get an SCM connection by UUID",
    "code_security",
    [
      {
        "type": "string",
        "description": "Connection UUID",
        "name": "uuid",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "DeleteSCMConnection",
    "DELETE",
    "/scm-integration/entities/connections/v1/{uuid}",
    "Delete an SCM connection",
    "code_security",
    [
      {
        "type": "string",
        "description": "Connection UUID",
        "name": "uuid",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "TriggerSCMSync",
    "POST",
    "/scm-integration/entities/connections/v1/{uuid}/sync",
    "Trigger an immediate sync for a connection",
    "code_security",
    [
      {
        "type": "string",
        "description": "Connection UUID",
        "name": "uuid",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "ListExclusionRules",
    "GET",
    "/scm-integration/entities/exclusions/v1",
    "List exclusion rules for a connection",
    "code_security",
    [
      {
        "type": "string",
        "description": "Connection UUID to list rules for",
        "name": "connection_id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "CreateExclusionRule",
    "POST",
    "/scm-integration/entities/exclusions/v1",
    "Create an exclusion rule",
    "code_security",
    []
  ],
  [
    "DeleteExclusionRule",
    "DELETE",
    "/scm-integration/entities/exclusions/v1/{id}",
    "Delete an exclusion rule",
    "code_security",
    [
      {
        "type": "string",
        "description": "Exclusion rule UUID",
        "name": "id",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "ListSCMRepositories",
    "GET",
    "/scm-integration/entities/repositories/v1",
    "List discovered SCM repositories for a customer",
    "code_security",
    [
      {
        "type": "string",
        "description": "FQL filter expression",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Sort field and direction in field.direction format (e.g. name.asc, created_date.desc)",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Maximum records to return (default 100, max 500)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Starting offset for pagination",
        "name": "offset",
        "in": "query"
      }
    ]
  ],
  [
    "ExchangeGitHubAppCode",
    "POST",
    "/scm-integration/github-apps/exchange/v1",
    "Exchange a GitHub App manifest code or complete registration after installation",
    "code_security",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "RegisterSCMApp",
    "POST",
    "/scm-integration/registrations",
    "Register a GitHub App via the wizard flow",
    "code_security",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ]
]
