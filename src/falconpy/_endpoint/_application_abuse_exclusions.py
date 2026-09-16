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

_application_abuse_exclusions_endpoints = [
  [
    "app_abuse_exclusions_aggregates_v1",
    "POST",
    "/exclusions/aggregates/app-abuse-exclusions/GET/v1",
    "Get Application Abuse Exclusion aggregates as specified via json in the request body",
    "application_abuse_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "app_abuse_exclusions_report_v1",
    "POST",
    "/exclusions/entities/app-abuse-exclusions/reports/v1",
    "Create a report of Application Abuse Exclusions scoped by the given filters",
    "application_abuse_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "app_abuse_exclusions_get_v1",
    "GET",
    "/exclusions/entities/app-abuse-exclusions/v1",
    "Get Application Abuse Exclusions by IDs",
    "application_abuse_exclusions",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The ids of the exclusions to retrieve",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "app_abuse_exclusions_create_v1",
    "POST",
    "/exclusions/entities/app-abuse-exclusions/v1",
    "Create new Application Abuse Exclusions",
    "application_abuse_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "app_abuse_exclusions_delete_v1",
    "DELETE",
    "/exclusions/entities/app-abuse-exclusions/v1",
    "Delete Application Abuse Exclusions by IDs",
    "application_abuse_exclusions",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The ids of the exclusions to delete",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "The comment why these exclusions were deleted",
        "name": "comment",
        "in": "query"
      }
    ]
  ],
  [
    "app_abuse_exclusions_update_v1",
    "PATCH",
    "/exclusions/entities/app-abuse-exclusions/v1",
    "Update existing Application Abuse Exclusions",
    "application_abuse_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "app_abuse_exclusions_get_apps_by_category_v1",
    "GET",
    "/exclusions/entities/combined-app-abuse-prevention-apps/v1",
    "Get available applications filtered by Application Abuse Prevention category",
    "application_abuse_exclusions",
    [
      {
        "type": "string",
        "description": "Filter applications by category (e.g. rmm)",
        "name": "category",
        "in": "query"
      },
      {
        "type": "boolean",
        "description": "Filter out applications that already have exclusions",
        "name": "show_available_only",
        "in": "query"
      }
    ]
  ],
  [
    "app_abuse_exclusions_get_categories_v1",
    "GET",
    "/exclusions/entities/combined-app-abuse-prevention-categories/v1",
    "Get available Application Abuse Prevention categories",
    "application_abuse_exclusions",
    []
  ],
  [
    "app_abuse_exclusions_query_v1",
    "GET",
    "/exclusions/queries/app-abuse-exclusions/v1",
    "Search for Application Abuse Exclusions",
    "application_abuse_exclusions",
    [
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The offset to start retrieving records from",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The maximum records to return. [1-100]",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The sort expression that should be used to sort the results",
        "name": "sort",
        "in": "query"
      }
    ]
  ]
]
