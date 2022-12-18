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

_mssp_endpoints = [
  [
    "getChildrenV2",
    "POST",
    "/mssp/entities/children/GET/v2",
    "Get link to child customer by child CID(s)",
    "mssp",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "getChildren",
    "GET",
    "/mssp/entities/children/v1",
    "Get link to child customer by child CID(s)",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "CID of a child customer",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "getCIDGroupMembersByV1",
    "GET",
    "/mssp/entities/cid-group-members/v1",
    "Get CID group members by CID group ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "CID group IDs to search for",
        "name": "cid_group_ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "addCIDGroupMembers",
    "POST",
    "/mssp/entities/cid-group-members/v1",
    "Add new CID Group member.",
    "mssp",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "deleteCIDGroupMembers",
    "DELETE",
    "/mssp/entities/cid-group-members/v1",
    "Delete CID Group members entry.",
    "mssp",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "getCIDGroupMembersBy",
    "GET",
    "/mssp/entities/cid-group-members/v2",
    "Get CID group members by CID Group ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "CID group IDs search for",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "getCIDGroupMembersByV2",
    "GET",
    "/mssp/entities/cid-group-members/v2",
    "Get CID group members by CID Group ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "CID group IDs search for",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "getCIDGroupByIdV1",
    "GET",
    "/mssp/entities/cid-groups/v1",
    "Get CID groups by ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "CID group IDs to be searched on",
        "name": "cid_group_ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "createCIDGroups",
    "POST",
    "/mssp/entities/cid-groups/v1",
    "Create new CID Group(s). Maximum 500 CID Group(s) allowed.",
    "mssp",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "updateCIDGroups",
    "PATCH",
    "/mssp/entities/cid-groups/v1",
    "Update existing CID Group(s). CID Group ID is expected for each CID Group definition provided in request body. "
    "CID Group member(s) remain unaffected.",
    "mssp",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "deleteCIDGroups",
    "DELETE",
    "/mssp/entities/cid-groups/v1",
    "Delete CID groups by ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "CID group ids to delete",
        "name": "cid_group_ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "getCIDGroupById",
    "GET",
    "/mssp/entities/cid-groups/v2",
    "Get CID Groups by ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "CID group IDs to search for",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "getCIDGroupByIdV2",
    "GET",
    "/mssp/entities/cid-groups/v2",
    "Get CID Groups by ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "CID group IDs to search for",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "getRolesByID",
    "GET",
    "/mssp/entities/mssp-roles/v1",
    "Get MSSP Role assignment(s). MSSP Role assignment is of the format :.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "MSSP Role assignment is of the format <user_group_id>:<cid_group_id>",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "addRole",
    "POST",
    "/mssp/entities/mssp-roles/v1",
    "Assign new MSSP Role(s) between User Group and CID Group. It does not revoke existing role(s) "
    "between User Group and CID Group. User Group ID and CID Group ID have to be specified in request. ",
    "mssp",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "deletedRoles",
    "DELETE",
    "/mssp/entities/mssp-roles/v1",
    "Delete MSSP Role assignment(s) between User Group and CID Group. User Group ID and CID Group ID have to be "
    "specified in request. Only specified roles are removed if specified in request payload, else association between "
    "User Group and CID Group is dissolved completely (if no roles specified).",
    "mssp",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "getUserGroupMembersByIDV1",
    "GET",
    "/mssp/entities/user-group-members/v1",
    "Get user group members by user group ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "User group IDs to search for",
        "name": "user_group_ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "addUserGroupMembers",
    "POST",
    "/mssp/entities/user-group-members/v1",
    "Add new User Group member. Maximum 500 members allowed per User Group.",
    "mssp",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "deleteUserGroupMembers",
    "DELETE",
    "/mssp/entities/user-group-members/v1",
    "Delete User Group members entry.",
    "mssp",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "getUserGroupMembersByID",
    "GET",
    "/mssp/entities/user-group-members/v2",
    "Get user group members by user group ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "User group IDs to search for",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "getUserGroupMembersByIDV2",
    "GET",
    "/mssp/entities/user-group-members/v2",
    "Get user group members by user group ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "User group IDs to search for",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "getUserGroupsByIDV1",
    "GET",
    "/mssp/entities/user-groups/v1",
    "Get user groups by ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "User Group IDs to search for",
        "name": "user_group_ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "createUserGroups",
    "POST",
    "/mssp/entities/user-groups/v1",
    "Create new User Group(s). Maximum 500 User Group(s) allowed per customer.",
    "mssp",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "updateUserGroups",
    "PATCH",
    "/mssp/entities/user-groups/v1",
    "Update existing User Group(s). User Group ID is expected for each User Group definition provided in request body. "
    "User Group member(s) remain unaffected.",
    "mssp",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "deleteUserGroups",
    "DELETE",
    "/mssp/entities/user-groups/v1",
    "Delete user groups by ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "User group IDs to delete",
        "name": "user_group_ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "getUserGroupsByID",
    "GET",
    "/mssp/entities/user-groups/v2",
    "Get user groups by ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "User group IDs to search for",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "getUserGroupsByIDV2",
    "GET",
    "/mssp/entities/user-groups/v2",
    "Get user groups by ID.",
    "mssp",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "User group IDs to search for",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "queryChildren",
    "GET",
    "/mssp/queries/children/v1",
    "Query for customers linked as children",
    "mssp",
    [
      {
        "enum": [
          "last_modified_timestamp"
        ],
        "type": "string",
        "default": "last_modified_timestamp|desc",
        "description": "The sort expression used to sort the results",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 0,
        "description": "Starting index of overall result set from which to return ids",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 10,
        "description": "Number of ids to return",
        "name": "limit",
        "in": "query"
      }
    ]
  ],
  [
    "queryCIDGroupMembers",
    "GET",
    "/mssp/queries/cid-group-members/v1",
    "Query a CID groups members by associated CID.",
    "mssp",
    [
      {
        "type": "string",
        "description": "CID to lookup associated CID group ID",
        "name": "cid",
        "in": "query",
        "required": True
      },
      {
        "enum": [
          "last_modified_timestamp|asc",
          "last_modified_timestamp|desc"
        ],
        "type": "string",
        "default": "last_modified_timestamp|desc",
        "description": "The sort expression used to sort the results",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 0,
        "description": "Starting index of overall result set from which to return id",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 10,
        "description": "Maximum number of results to return",
        "name": "limit",
        "in": "query"
      }
    ]
  ],
  [
    "queryCIDGroups",
    "GET",
    "/mssp/queries/cid-groups/v1",
    "Query CID Groups.",
    "mssp",
    [
      {
        "type": "string",
        "description": "Name to lookup groups for",
        "name": "name",
        "in": "query"
      },
      {
        "enum": [
          "last_modified_timestamp",
          "name"
        ],
        "type": "string",
        "default": "name|asc",
        "description": "The sort expression used to sort the results",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 0,
        "description": "Starting index of overall result set from which to return ids",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 10,
        "description": "Number of ids to return",
        "name": "limit",
        "in": "query"
      }
    ]
  ],
  [
    "queryRoles",
    "GET",
    "/mssp/queries/mssp-roles/v1",
    "Query MSSP Role assignment. At least one of CID Group ID or User Group ID should also be provided. Role ID is optional.",
    "mssp",
    [
      {
        "type": "string",
        "description": "User group ID to fetch MSSP role for",
        "name": "user_group_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "CID group ID to fetch MSSP role for",
        "name": "cid_group_id",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Role ID to fetch MSSP role for",
        "name": "role_id",
        "in": "query"
      },
      {
        "enum": [
          "last_modified_timestamp|asc",
          "last_modified_timestamp|desc"
        ],
        "type": "string",
        "default": "last_modified_timestamp|desc",
        "description": "The sort expression used to sort the results",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 0,
        "description": "Starting index of overall result set from which to return ids",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 10,
        "description": "Maximum number of results to return",
        "name": "limit",
        "in": "query"
      }
    ]
  ],
  [
    "queryUserGroupMembers",
    "GET",
    "/mssp/queries/user-group-members/v1",
    "Query User Group member by User UUID.",
    "mssp",
    [
      {
        "type": "string",
        "description": "User UUID to lookup associated user group ID",
        "name": "user_uuid",
        "in": "query",
        "required": True
      },
      {
        "enum": [
          "last_modified_timestamp"
        ],
        "type": "string",
        "default": "last_modified_timestamp|desc",
        "description": "The sort expression used to sort the results",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 0,
        "description": "Starting index of overall result set from which to return ids",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 10,
        "description": "Number of ids to return",
        "name": "limit",
        "in": "query"
      }
    ]
  ],
  [
    "queryUserGroups",
    "GET",
    "/mssp/queries/user-groups/v1",
    "Query User Groups.",
    "mssp",
    [
      {
        "type": "string",
        "description": "Name to lookup groups for",
        "name": "name",
        "in": "query"
      },
      {
        "enum": [
          "last_modified_timestamp",
          "name"
        ],
        "type": "string",
        "default": "name|asc",
        "description": "The sort expression used to sort the results",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 0,
        "description": "Starting index of overall result set from which to return ids",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 10,
        "description": "Number of ids to return",
        "name": "limit",
        "in": "query"
      }
    ]
  ]
]
