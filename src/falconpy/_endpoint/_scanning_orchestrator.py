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

_scanning_orchestrator_endpoints = [
  [
    "get_combined_schedules",
    "GET",
    "/agentless-scanning/combined/schedules/v1",
    "Get combined scanning schedules",
    "scanning_orchestrator",
    [
      {
        "type": "string",
        "description": "Bearer Token",
        "name": "Authorization",
        "in": "header",
        "required": True
      },
      {
        "type": "integer",
        "default": 100,
        "maximum": 100,
        "minimum": 1,
        "description": "Number of results to return",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 0,
        "minimum": 0,
        "description": "Starting offset for pagination",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Sort field and direction. Available fields: scan_product, provider_type, enabled, "
        "name, created_at. Example: name|asc",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "FQL filter expression. Available fields: scan_product, provider_type, enabled, name, "
        "created_at. Example: enabled:true",
        "name": "filter",
        "in": "query"
      }
    ]
  ],
  [
    "trigger_scan_by_schedule",
    "POST",
    "/agentless-scanning/entities/scan-by-schedule/v1",
    "Trigger scan by schedule IDs",
    "scanning_orchestrator",
    [
      {
        "type": "string",
        "description": "Bearer Token",
        "name": "Authorization",
        "in": "header",
        "required": True
      },
      {
        "description": "Schedule IDs to trigger",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "get_schedules",
    "GET",
    "/agentless-scanning/entities/schedules/v1",
    "Get scanning schedules",
    "scanning_orchestrator",
    [
      {
        "type": "string",
        "description": "Bearer Token",
        "name": "Authorization",
        "in": "header",
        "required": True
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Schedule IDs to retrieve",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "create_schedules",
    "POST",
    "/agentless-scanning/entities/schedules/v1",
    "Create scanning schedules",
    "scanning_orchestrator",
    [
      {
        "type": "string",
        "description": "Bearer Token",
        "name": "Authorization",
        "in": "header",
        "required": True
      },
      {
        "description": "Schedule resources to create",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "delete_schedules",
    "DELETE",
    "/agentless-scanning/entities/schedules/v1",
    "Delete scanning schedules",
    "scanning_orchestrator",
    [
      {
        "type": "string",
        "description": "Bearer Token",
        "name": "Authorization",
        "in": "header",
        "required": True
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Schedule IDs to delete",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "update_schedules",
    "PATCH",
    "/agentless-scanning/entities/schedules/v1",
    "Update scanning schedules",
    "scanning_orchestrator",
    [
      {
        "type": "string",
        "description": "Bearer Token",
        "name": "Authorization",
        "in": "header",
        "required": True
      },
      {
        "description": "Schedule resources to update (ID required in each resource)",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "get_service_types",
    "GET",
    "/agentless-scanning/entities/supported-service-types/v1",
    "Get allowed service types",
    "scanning_orchestrator",
    [
      {
        "type": "string",
        "description": "Bearer Token",
        "name": "Authorization",
        "in": "header",
        "required": True
      },
      {
        "type": "string",
        "enum": [
          "dspm_scanning",
          "vulnerability_scanning"
        ],
        "description": "Scan product filter",
        "name": "scan_product",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "search_schedules",
    "GET",
    "/agentless-scanning/queries/schedules/v1",
    "Search scanning schedules",
    "scanning_orchestrator",
    [
      {
        "type": "string",
        "description": "Bearer Token",
        "name": "Authorization",
        "in": "header",
        "required": True
      },
      {
        "type": "integer",
        "default": 100,
        "maximum": 100,
        "minimum": 1,
        "description": "Number of results to return",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 0,
        "minimum": 0,
        "description": "Starting offset for pagination",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Sort field and direction. Available fields: scan_product, provider_type, enabled, "
        "name, created_at. Example: name|asc",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "FQL filter expression. Available fields: scan_product, provider_type, enabled, name, "
        "created_at. Example: enabled:true",
        "name": "filter",
        "in": "query"
      }
    ]
  ]
]
