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

_ioa_exclusions_endpoints = [
  [
    "ss_ioa_exclusions_aggregates_v2",
    "POST",
    "/exclusions/aggregates/ss-ioa-exclusions/GET/v2",
    "Get Self Service IOA Exclusion aggregates as specified via json in the request body.",
    "ioa_exclusions",
    [
      {
        "type": "string",
        "description": "The `ifn_regex` expression to filter exclusion aggregations by, used alongside filter "
        "expressions provided in the request body.",
        "name": "ifn_regex",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The cl_regex expression to filter exclusion aggregations by, used alongside filter "
        "expressions provided in the request body.",
        "name": "cl_regex",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The parent_ifn_regex expression to filter exclusion aggregations by, used alongside "
        "filter expressions provided in the request body.",
        "name": "parent_ifn_regex",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The parent_cl_regex expression to filter exclusion aggregations by, used alongside "
        "filter expressions provided in the request body.",
        "name": "parent_cl_regex",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The grandparent_ifn_regex expression to filter exclusion aggregations by, used "
        "alongside filter expressions provided in the request body.",
        "name": "grandparent_ifn_regex",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The grandparent_cl_regex expression to filter exclusion aggregations by, used "
        "alongside filter expressions provided in the request body.",
        "name": "grandparent_cl_regex",
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
    "ss_ioa_exclusions_get_reports_v2",
    "POST",
    "/exclusions/entities/ss-ioa-exclusions/reports/v2",
    "Create a report of Self Service IOA Exclusions scoped by the given filters",
    "ioa_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ss_ioa_exclusions_get_v2",
    "GET",
    "/exclusions/entities/ss-ioa-exclusions/v2",
    "Get the Self Service IOA Exclusions rules by id.",
    "ioa_exclusions",
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
    "ss_ioa_exclusions_create_v2",
    "POST",
    "/exclusions/entities/ss-ioa-exclusions/v2",
    "Create new Self Service IOA Exclusions.",
    "ioa_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ss_ioa_exclusions_update_v2",
    "PATCH",
    "/exclusions/entities/ss-ioa-exclusions/v2",
    "Update the Self Service IOA Exclusions rule by id.",
    "ioa_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ss_ioa_exclusions_delete_v2",
    "DELETE",
    "/exclusions/entities/ss-ioa-exclusions/v2",
    "Delete the Self Service IOA Exclusions rule by id.",
    "ioa_exclusions",
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
        "description": "The comment why these ss ioa exclusions were deleted",
        "name": "comment",
        "in": "query"
      }
    ]
  ],
  [
    "ss_ioa_exclusions_matched_rule_v2",
    "POST",
    "/exclusions/entities/ss-ioa-matched-rules/v2",
    "Get Self Service IOA Exclusions rules for matched IFN/CLI for child, parent and grandparent",
    "ioa_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ss_ioa_exclusions_new_rules_v2",
    "POST",
    "/exclusions/entities/ss-ioa-new-rules/v2",
    "Get defaults for Self Service IOA Exclusions based on provided IFN/CLI for child, parent and grandparent.",
    "ioa_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "ss_ioa_exclusions_search_v2",
    "GET",
    "/exclusions/queries/ss-ioa-exclusions/v2",
    "Search for Self Service IOA Exclusions.",
    "ioa_exclusions",
    [
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results. Filtered queries "
        "involving regex fields should specify their expressions in the `ifn_regex` and `cl_regex` parameters.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The ifn_regex expression to filter exclusions by, used alongside expressions specified "
        "in the filter query parameter.",
        "name": "ifn_regex",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The cl_regex expression to filter exclusions by, used alongside expressions specified "
        "in the filter query parameter.",
        "name": "cl_regex",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The parent_ifn_regex expression to filter exclusions by, used alongside expressions "
        "specified in the filter query parameter.",
        "name": "parent_ifn_regex",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The parent_cl_regex expression to filter exclusions by, used alongside expressions "
        "specified in the filter query parameter.",
        "name": "parent_cl_regex",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The grandparent_ifn_regex expression to filter exclusions by, used alongside "
        "expressions specified in the filter query parameter.",
        "name": "grandparent_ifn_regex",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The grandparent_cl_regex expression to filter exclusions by, used alongside "
        "expressions specified in the filter query parameter.",
        "name": "grandparent_cl_regex",
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
          "created_by.raw",
          "last_modified",
          "modified_by.raw",
          "name.raw",
          "pattern_id",
          "pattern_name.raw"
        ],
        "type": "string",
        "description": "The sort expression that should be used to sort the results.",
        "name": "sort",
        "in": "query"
      }
    ]
  ],
  [
    "getIOAExclusionsV1",
    "GET",
    "/policy/entities/ioa-exclusions/v1",
    "Get a set of IOA Exclusions by specifying their IDs",
    "ioa_exclusions",
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
    "createIOAExclusionsV1",
    "POST",
    "/policy/entities/ioa-exclusions/v1",
    "Create the IOA exclusions",
    "ioa_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "updateIOAExclusionsV1",
    "PATCH",
    "/policy/entities/ioa-exclusions/v1",
    "Update the IOA exclusions",
    "ioa_exclusions",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "deleteIOAExclusionsV1",
    "DELETE",
    "/policy/entities/ioa-exclusions/v1",
    "Delete the IOA exclusions by id",
    "ioa_exclusions",
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
        "description": "Explains why this exclusions was deleted",
        "name": "comment",
        "in": "query"
      }
    ]
  ],
  [
    "queryIOAExclusionsV1",
    "GET",
    "/policy/queries/ioa-exclusions/v1",
    "Search for IOA exclusions.",
    "ioa_exclusions",
    [
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results. Filtered queries "
        "involving regex fields should specify their expressions in the ifn_regex and cl_regex parameters.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The ifn_regex expression to filter exclusions by, used alongside expressions specified "
        "in the filter query parameter.",
        "name": "ifn_regex",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The cl_regex expression to filter exclusions by, used alongside expressions specified "
        "in the filter query parameter.",
        "name": "cl_regex",
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
          "applied_globally.asc",
          "applied_globally.desc",
          "created_by.asc",
          "created_by.desc",
          "created_on.asc",
          "created_on.desc",
          "last_modified.asc",
          "last_modified.desc",
          "modified_by.asc",
          "modified_by.desc",
          "name.asc",
          "name.desc",
          "pattern_id.asc",
          "pattern_id.desc",
          "pattern_name.asc",
          "pattern_name.desc"
        ],
        "type": "string",
        "description": "The sort expression that should be used to sort the results.",
        "name": "sort",
        "in": "query"
      }
    ]
  ]
]
