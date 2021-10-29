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

_custom_ioa_endpoints = [
  [
    "get-patterns",
    "GET",
    "/ioarules/entities/pattern-severities/v1",
    "Get pattern severities by ID.",
    "custom_ioa",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The IDs of the entities",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "get-platformsMixin0",
    "GET",
    "/ioarules/entities/platforms/v1",
    "Get platforms by ID.",
    "custom_ioa",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The IDs of the entities",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "get-rule-groupsMixin0",
    "GET",
    "/ioarules/entities/rule-groups/v1",
    "Get rule groups by ID.",
    "custom_ioa",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The IDs of the entities",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "create-rule-groupMixin0",
    "POST",
    "/ioarules/entities/rule-groups/v1",
    "Create a rule group for a platform with a name and an optional description. Returns the rule group.",
    "custom_ioa",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "update-rule-groupMixin0",
    "PATCH",
    "/ioarules/entities/rule-groups/v1",
    "Update a rule group. The following properties can be modified: name, description, enabled.",
    "custom_ioa",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "delete-rule-groupsMixin0",
    "DELETE",
    "/ioarules/entities/rule-groups/v1",
    "Delete rule groups by ID.",
    "custom_ioa",
    [
      {
        "type": "string",
        "description": "Explains why the entity is being deleted",
        "name": "comment",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The IDs of the entities",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "get-rule-types",
    "GET",
    "/ioarules/entities/rule-types/v1",
    "Get rule types by ID.",
    "custom_ioa",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The IDs of the entities",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "get-rules-get",
    "POST",
    "/ioarules/entities/rules/GET/v1",
    "Get rules by ID and optionally version in the following format: `ID[:version]`.",
    "custom_ioa",
    [
      {
        "description": "The \"ids\" field contains a list of the rules to retrieve.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "get-rulesMixin0",
    "GET",
    "/ioarules/entities/rules/v1",
    "Get rules by ID and optionally version in the following format: `ID[:version]`. "
    "The max number of IDs is constrained by URL size.",
    "custom_ioa",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The IDs of the entities",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "create-rule",
    "POST",
    "/ioarules/entities/rules/v1",
    "Create a rule within a rule group. Returns the rule.",
    "custom_ioa",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "update-rules",
    "PATCH",
    "/ioarules/entities/rules/v1",
    "Update rules within a rule group. Return the updated rules.",
    "custom_ioa",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "delete-rules",
    "DELETE",
    "/ioarules/entities/rules/v1",
    "Delete rules from a rule group by ID.",
    "custom_ioa",
    [
      {
        "type": "string",
        "description": "The parent rule group",
        "name": "rule_group_id",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "Explains why the entity is being deleted",
        "name": "comment",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The IDs of the entities",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "query-patterns",
    "GET",
    "/ioarules/queries/pattern-severities/v1",
    "Get all pattern severity IDs.",
    "custom_ioa",
    [
      {
        "type": "string",
        "description": "Starting index of overall result set from which to return IDs",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Number of IDs to return",
        "name": "limit",
        "in": "query"
      }
    ]
  ],
  [
    "query-platformsMixin0",
    "GET",
    "/ioarules/queries/platforms/v1",
    "Get all platform IDs.",
    "custom_ioa",
    [
      {
        "type": "string",
        "description": "Starting index of overall result set from which to return IDs",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Number of IDs to return",
        "name": "limit",
        "in": "query"
      }
    ]
  ],
  [
    "query-rule-groups-full",
    "GET",
    "/ioarules/queries/rule-groups-full/v1",
    "Find all rule groups matching the query with optional filter.",
    "custom_ioa",
    [
      {
        "enum": [
          "created_by",
          "created_on",
          "description",
          "enabled",
          "modified_by",
          "modified_on",
          "name"
        ],
        "type": "string",
        "description": "Possible order by fields: {created_by, created_on, modified_by, "
        "modified_on, enabled, name, description}",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "FQL query specifying the filter parameters. Filter term criteria: "
        "[enabled platform name description rules.action_label rules.name rules.description "
        "rules.pattern_severity rules.ruletype_name rules.enabled]. Filter range criteria: "
        "created_on, modified_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Match query criteria, which includes all the filter string fields",
        "name": "q",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Starting index of overall result set from which to return IDs",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Number of IDs to return",
        "name": "limit",
        "in": "query"
      }
    ]
  ],
  [
    "query-rule-groupsMixin0",
    "GET",
    "/ioarules/queries/rule-groups/v1",
    "Finds all rule group IDs matching the query with optional filter.",
    "custom_ioa",
    [
      {
        "enum": [
          "created_by",
          "created_on",
          "description",
          "enabled",
          "modified_by",
          "modified_on",
          "name"
        ],
        "type": "string",
        "description": "Possible order by fields: {created_by, created_on, modified_by, "
        "modified_on, enabled, name, description}",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "FQL query specifying the filter parameters. Filter term criteria: "
        "[enabled platform name description rules.action_label rules.name rules.description "
        "rules.pattern_severity rules.ruletype_name rules.enabled]. Filter range criteria: "
        "created_on, modified_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Match query criteria, which includes all the filter string fields",
        "name": "q",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Starting index of overall result set from which to return IDs",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Number of IDs to return",
        "name": "limit",
        "in": "query"
      }
    ]
  ],
  [
    "query-rule-types",
    "GET",
    "/ioarules/queries/rule-types/v1",
    "Get all rule type IDs.",
    "custom_ioa",
    [
      {
        "type": "string",
        "description": "Starting index of overall result set from which to return IDs",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Number of IDs to return",
        "name": "limit",
        "in": "query"
      }
    ]
  ],
  [
    "query-rulesMixin0",
    "GET",
    "/ioarules/queries/rules/v1",
    "Finds all rule IDs matching the query with optional filter.",
    "custom_ioa",
    [
      {
        "enum": [
          "rules.created_by",
          "rules.created_on",
          "rules.current_version.action_label",
          "rules.current_version.description",
          "rules.current_version.modified_by",
          "rules.current_version.modified_on",
          "rules.current_version.name",
          "rules.current_version.pattern_severity",
          "rules.enabled",
          "rules.ruletype_name"
        ],
        "type": "string",
        "description": "Possible order by fields: {rules.ruletype_name, rules.enabled, rules.created_by, "
        "rules.current_version.name, rules.current_version.modified_by, rules.created_on, "
        "rules.current_version.description, rules.current_version.pattern_severity, "
        "rules.current_version.action_label, rules.current_version.modified_on}",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "FQL query specifying the filter parameters. Filter term criteria: "
        "[enabled platform name description rules.action_label rules.name rules.description "
        "rules.pattern_severity rules.ruletype_name rules.enabled]. Filter range criteria: "
        "created_on, modified_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Match query criteria, which includes all the filter string fields",
        "name": "q",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Starting index of overall result set from which to return IDs",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Number of IDs to return",
        "name": "limit",
        "in": "query"
      }
    ]
  ]
]
