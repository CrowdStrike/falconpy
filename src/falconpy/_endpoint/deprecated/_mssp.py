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

_mssp_endpoints = [
  [
    "getCIDGroupMembersBy",
    "GET",
    "/mssp/entities/cid-group-members/v1",
    "Deprecated : Please use getCIDGroupMembersBy. Get CID group members by CID group ID.",
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
    "deleteCIDGroupMembers",
    "DELETE",
    "/mssp/entities/cid-group-members/v1",
    "Deprecated : Please use deleteCIDGroupMembers. Delete CID group members.",
    "mssp",
    [
      {
        "description": "Both 'cid_group_id' and 'cids' fields are required.",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "getCIDGroupById",
    "GET",
    "/mssp/entities/cid-groups/v1",
    "Deprecated : Please use getCIDGroupById. Get CID groups by ID.",
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
    "getUserGroupMembersByID",
    "GET",
    "/mssp/entities/user-group-members/v1",
    "Deprecated : Please use getUserGroupMembersByID. Get user group members by user group ID.",
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
    "getUserGroupsByID",
    "GET",
    "/mssp/entities/user-groups/v1",
    "Deprecated : Please use getUserGroupsByID. Get user groups by ID.",
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
  ]
]
