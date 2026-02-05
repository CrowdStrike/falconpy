"""Internal API endpoint constant library (deprecated operations).

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

_ml_exclusions_endpoints = [
  [
    "exclusions.aggregates.v2",
    "POST",
    "/exclusions/aggregates/exclusions/GET/v2",
    "Get exclusion aggregates as specified via json in request body.",
    "ml_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "exclusions.get-all.v2",
    "GET",
    "/exclusions/entities/all-exclusions/v2",
    "Get all exclusions.",
    "ml_exclusions",
    []
  ],
  [
    "exclusions.perform-action.v2",
    "POST",
    "/exclusions/entities/exclusion-actions/v2",
    "Actions used to manipulate the content of exclusions, with ancestor fields.",
    "ml_exclusions",
    [
      {
        "enum": [
          "add_item",
          "remove_item",
          "validate_filepath"
        ],
        "type": "string",
        "description": "The action to perform.",
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
    "exclusions.get-reports.v2",
    "POST",
    "/exclusions/entities/exclusions/reports/v2",
    "Create a report of ML exclusions scoped by the given filters",
    "ml_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "exclusions.get.v2",
    "GET",
    "/exclusions/entities/exclusions/v2",
    "Get the exclusions by id, with ancestor fields.",
    "ml_exclusions",
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
    "exclusions.create.v2",
    "POST",
    "/exclusions/entities/exclusions/v2",
    "Create the exclusions, with ancestor fields.",
    "ml_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "exclusions.update.v2",
    "PATCH",
    "/exclusions/entities/exclusions/v2",
    "Update the exclusions by id, with ancestor fields.",
    "ml_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "exclusions.delete.v2",
    "DELETE",
    "/exclusions/entities/exclusions/v2",
    "Delete the exclusions by id, with ancestor fields.",
    "ml_exclusions",
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
    "exclusions.search.v2",
    "GET",
    "/exclusions/queries/exclusions/v2",
    "Search for exclusions, with ancestor fields.",
    "ml_exclusions",
    [
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results.",
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
        "description": "The maximum records to return. [1-500]",
        "name": "limit",
        "in": "query"
      },
      {
        "enum": [
          "parent_value",
          "value",
          "grandparent_value",
          "applied_globally",
          "created_on",
          "created_by",
          "last_modified",
          "modified_by",
          "is_descendant_process"
        ],
        "type": "string",
        "description": "The sort expression that should be used to sort the results.",
        "name": "sort",
        "in": "query"
      }
    ]
  ]
]
