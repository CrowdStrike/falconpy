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

_network_containment_endpoints = [
  [
    "GetContainmentAllowlistRules",
    "GET",
    "/customers/entities/containment-allowlist-rules/v1",
    "Get network containment allowlist rules for the specified IDs",
    "network_containment",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Containment allowlist rule ID",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "CreateContainmentAllowlistRules",
    "POST",
    "/customers/entities/containment-allowlist-rules/v1",
    "Add new network containment allowlist rules",
    "network_containment",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteContainmentAllowlistRules",
    "DELETE",
    "/customers/entities/containment-allowlist-rules/v1",
    "Delete network containment allowlist rules by ID",
    "network_containment",
    [
      {
        "type": "string",
        "description": "Containment allowlist rule ID",
        "name": "ids",
        "in": "query"
      }
    ]
  ],
  [
    "UpdateContainmentAllowlistRules",
    "PATCH",
    "/customers/entities/containment-allowlist-rules/v1",
    "Update network containment allowlist rules",
    "network_containment",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "QueryContainmentAllowlistRules",
    "GET",
    "/customers/queries/containment-allowlist-rules/v1",
    "Search for network containment allowlist rules by context",
    "network_containment",
    [
      {
        "type": "string",
        "description": "Allowlist FQL filter. Can only filter based on the context parameter",
        "name": "filter",
        "in": "query"
      }
    ]
  ]
]
