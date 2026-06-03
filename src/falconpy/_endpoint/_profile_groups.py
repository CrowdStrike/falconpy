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

_profile_groups_endpoints = [
  [
    "GroupActionsV1Mixin0",
    "POST",
    "/user-management/entities/group-actions/v1",
    "Perform actions on profile groups (add/remove roles, user groups, FGA objects)",
    "profile_groups",
    [
      {
        "type": "string",
        "enum": [
          "add_roles",
          "remove_roles",
          "add_user_groups",
          "remove_user_groups",
          "add_fga_objects",
          "remove_fga_objects"
        ],
        "description": "Action to perform",
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
    "GroupUsersActionsV1Mixin0",
    "POST",
    "/user-management/entities/group-users-actions/v1",
    "Add or remove users from profile groups",
    "profile_groups",
    [
      {
        "type": "string",
        "enum": [
          "add_users",
          "remove_users"
        ],
        "description": "Action to perform",
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
    "GetGroupUsersV1",
    "POST",
    "/user-management/entities/group-users/GET/v1",
    "Get a list of groups with users that belong to them",
    "profile_groups",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetGroupsV1Mixin0",
    "POST",
    "/user-management/entities/groups/GET/v1",
    "Get profile groups by IDs with full details",
    "profile_groups",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "CreateGroupV1Mixin0",
    "POST",
    "/user-management/entities/groups/v1",
    "Create a new profile group",
    "profile_groups",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteGroupsV1",
    "DELETE",
    "/user-management/entities/groups/v1",
    "Delete profile groups by IDs",
    "profile_groups",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Group IDs to delete",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "UpdateGroupV1Mixin0",
    "PATCH",
    "/user-management/entities/groups/v1",
    "Update profile group metadata (name, description)",
    "profile_groups",
    [
      {
        "type": "string",
        "description": "ID of the group to update",
        "name": "id",
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
    "GetUserGroupsV1",
    "POST",
    "/user-management/entities/user-groups/GET/v1",
    "Get a list of users with the groups that they belong to",
    "profile_groups",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "QueryGroupsV1Mixin0",
    "GET",
    "/user-management/queries/groups/v1",
    "Query profile group IDs with FQL filtering, pagination, and sorting",
    "profile_groups",
    [
      {
        "type": "string",
        "description": "FQL filter expression to filter groups by name or cid",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "string",
        "default": "name|desc",
        "description": "Sort by field|direction (name, updated_at, member_count)",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 0,
        "minimum": 0,
        "description": "Number of groups to skip",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 100,
        "maximum": 500,
        "minimum": 1,
        "description": "Maximum groups to return [1-500]",
        "name": "limit",
        "in": "query"
      }
    ]
  ]
]
