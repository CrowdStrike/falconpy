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

_cloud_azure_registration_endpoints = [
  [
    "cloud_registration_azure_get_issue_suppression_values_by_field",
    "GET",
    "/cloud-security-registration-azure/aggregates/issue-suppressions-values-by-fields/v1",
    "Retrieve distinct filterable values for issue suppression fields",
    "cloud_azure_registration",
    [
      {
        "type": "string",
        "description": "Registration ID to filter values by",
        "name": "registration_id",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "enum": [
          "issue_name",
          "entity_id",
          "suppressed_by",
          "created_at",
          "reason"
        ],
        "description": "Field to get values for",
        "name": "field",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "cloud_registration_azure_get_issue_values_by_field",
    "GET",
    "/cloud-security-registration-azure/aggregates/issues-values-by-fields/v1",
    "Retrieve distinct filterable values for issue fields",
    "cloud_azure_registration",
    [
      {
        "type": "string",
        "description": "Registration ID to filter values by",
        "name": "registration_id",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "FQL (Falcon Query Language) string for filtering results. Allowed filters are "
        "name,issue,severity,category,impact,entity_type,entity_id,entity_name,status",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "enum": [
          "issue",
          "name",
          "severity",
          "category",
          "impact",
          "entity_type",
          "entity_id",
          "entity_name",
          "status",
          "feature"
        ],
        "description": "Field to get values for",
        "name": "field",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "cloud_registration_azure_delete_legacy_subscription",
    "DELETE",
    "/cloud-security-registration-azure/entities/accounts/legacy/v1",
    "Delete existing legacy Azure subscriptions.",
    "cloud_azure_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "cloud_registration_azure_get_suppressions",
    "GET",
    "/cloud-security-registration-azure/entities/issue-suppressions/v1",
    "Retrieve existing suppression rules with filtering",
    "cloud_azure_registration",
    [
      {
        "type": "string",
        "description": "Registration ID",
        "name": "registration_id",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "FQL (Falcon Query Language) string for filtering results. Allowed filters are "
        "issue_name,entity_id,suppressed_by,created_at,reason",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Field and direction for sorting results - allowed sort fields are "
        "issue_name,entity_id,suppressed_by,created_at,reason",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 100,
        "maximum": 1000,
        "minimum": 0,
        "description": "Maximum number of records to return (default: 100, max: 1000)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 0,
        "minimum": 0,
        "description": "Starting index of result",
        "name": "offset",
        "in": "query"
      }
    ]
  ],
  [
    "cloud_registration_azure_create_suppressions",
    "POST",
    "/cloud-security-registration-azure/entities/issue-suppressions/v1",
    "Create new issue suppression rules",
    "cloud_azure_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "cloud_registration_azure_delete_suppressions",
    "DELETE",
    "/cloud-security-registration-azure/entities/issue-suppressions/v1",
    "Remove/revoke suppression rules",
    "cloud_azure_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "cloud_registration_azure_update_suppressions",
    "PATCH",
    "/cloud-security-registration-azure/entities/issue-suppressions/v1",
    "Update existing suppression rules",
    "cloud_azure_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "cloud_registration_azure_get_issues",
    "GET",
    "/cloud-security-registration-azure/entities/issues/v1",
    "Retrieve issues for Azure registrations",
    "cloud_azure_registration",
    [
      {
        "type": "string",
        "description": "Registration ID",
        "name": "registration_id",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "FQL (Falcon Query Language) string for filtering results. Allowed filters are "
        "name,issue,severity,category,impact,entity_type,entity_id,entity_name,status",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Field and direction for sorting results - allowed sort fields are "
        "issue,name,severity,category,impact,entity_type,entity_id,entity_name,impacted_entities",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "enum": [
          "name"
        ],
        "description": "Grouping method: 'name' (optional, default: ungrouped)",
        "name": "group_by",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 100,
        "maximum": 1000,
        "minimum": 0,
        "description": "Maximum number of records to return (default: 100, max: 1000)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 0,
        "minimum": 0,
        "description": "Starting index of result",
        "name": "offset",
        "in": "query"
      }
    ]
  ],
  [
    "cloud_registration_azure_trigger_health_check",
    "POST",
    "/cloud-security-registration-azure/entities/registrations/healthcheck/v1",
    "Trigger health check scan for Azure registrations",
    "cloud_azure_registration",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Azure tenant IDs",
        "name": "tenant_ids",
        "in": "query"
      }
    ]
  ],
  [
    "cloud_registration_azure_get_registration",
    "GET",
    "/cloud-security-registration-azure/entities/registrations/v1",
    "Retrieve existing Azure registration for a tenant.",
    "cloud_azure_registration",
    [
      {
        "type": "string",
        "description": "Tenant ID",
        "name": "tenant_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Registration ID",
        "name": "registration_id",
        "in": "query"
      }
    ]
  ],
  [
    "cloud_registration_azure_create_registration",
    "POST",
    "/cloud-security-registration-azure/entities/registrations/v1",
    "Create an Azure registration for a tenant.",
    "cloud_azure_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "cloud_registration_azure_delete_registration",
    "DELETE",
    "/cloud-security-registration-azure/entities/registrations/v1",
    "Deletes existing Azure registrations.",
    "cloud_azure_registration",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Azure tenant IDs",
        "name": "tenant_ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "cloud_registration_azure_update_registration",
    "PATCH",
    "/cloud-security-registration-azure/entities/registrations/v1",
    "Update an existing Azure registration for a tenant.",
    "cloud_azure_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "cloud_registration_azure_validate_registration",
    "POST",
    "/cloud-security-registration-azure/entities/registrations/validate/v1",
    "Validate an Azure registration by checking service principal, role assignments and deployment stack (if "
    "the deployment method is Bicep)",
    "cloud_azure_registration",
    [
      {
        "type": "string",
        "maxLength": 36,
        "minLength": 36,
        "pattern": "^[0-9a-z-]{36}$",
        "description": "Azure tenant ID to be validated",
        "name": "tenant_id",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "Azure deployment stack name to be validated",
        "name": "stack_name",
        "in": "query"
      }
    ]
  ],
  [
    "cloud_registration_azure_get_script_versions",
    "GET",
    "/cloud-security-registration-azure/entities/script-versions/v1",
    "Retrieve all available script versions with filtering and sorting",
    "cloud_azure_registration",
    [
      {
        "type": "string",
        "description": "Filter by deployment method (e.g., 'bicep-legacy', 'bicep-deployment-stack')",
        "name": "deployment_method",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "Field and direction for sorting results - allowed sort fields are "
        "version,deployment_method,published_date",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 100,
        "maximum": 1000,
        "minimum": 0,
        "description": "Maximum number of records to return (default: 100, max: 1000)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 0,
        "minimum": 0,
        "description": "Starting index of result",
        "name": "offset",
        "in": "query"
      }
    ]
  ],
  [
    "cloud_registration_azure_get_script",
    "GET",
    "/cloud-security-registration-azure/entities/scripts/v1",
    "Download Azure deployment script (Terraform or Bicep)",
    "cloud_azure_registration",
    [
      {
        "type": "string",
        "description": "Azure tenant ID",
        "name": "tenant_id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "cloud_registration_azure_download_script",
    "POST",
    "/cloud-security-registration-azure/entities/scripts/v1",
    "Retrieve script to create resources",
    "cloud_azure_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "download_azure_script",
    "GET",
    "/cloud-security-registration-azure/entities/scripts/v1",
    "DECOMMISSIONED: Download Azure deployment script (Terraform or Bicep)",
    "cloud_azure_registration",
    [
      {
        "type": "string",
        "description": "Azure tenant ID",
        "name": "tenant_id",
        "in": "query",
        "required": True
      }
    ]
  ]
]
