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

_discover_endpoints = [
  [
    "get_accounts",
    "GET",
    "/discover/entities/accounts/v1",
    "Get details on accounts by providing one or more IDs.",
    "discover",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "One or more account IDs (max: 100). Find account IDs with GET `/discover/queries/accounts/v1`",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "get_hosts",
    "GET",
    "/discover/entities/hosts/v1",
    "Get details on assets by providing one or more IDs.",
    "discover",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "One or more asset IDs (max: 100). Find asset IDs with GET `/discover/queries/hosts/v1`",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "get_logins",
    "GET",
    "/discover/entities/logins/v1",
    "Get details on logins by providing one or more IDs.",
    "discover",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "One or more login IDs (max: 100). Find login IDs with GET `/discover/queries/logins/v1`",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "query_accounts",
    "GET",
    "/discover/queries/accounts/v1",
    "Search for accounts in your environment by providing an FQL (Falcon Query Language) filter and paging details. "
    "Returns a set of account IDs which match the filter criteria.",
    "discover",
    [
      {
        "minimum": 0,
        "type": "integer",
        "description": "An offset used with the `limit` parameter to manage pagination of results. "
        "On your first request, don’t provide an `offset`. On subsequent requests, provide the `offset` "
        "from the previous response to continue from that place in the results.",
        "name": "offset",
        "in": "query"
      },
      {
        "maximum": 100,
        "minimum": 1,
        "type": "integer",
        "description": "The number of account IDs to return in this response (min: 1, max: 100, default: 100). "
        "Use with the `offset` parameter to manage pagination of results.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Sort accounts by their properties. A single sort field is allowed. "
        "Common sort options include:\n\n<ul><li>username|asc</li><li>last_failed_login_timestamp|desc</li></ul>",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter accounts using an FQL query. "
        "Common filter options include:\n\n<ul><li>account_type:'Local'</li><li>admin_privileges:'Yes'</li>"
        "<li>first_seen_timestamp:<'now-7d'</li><li>last_successful_login_type:'Terminal server'</li></ul>",
        "name": "filter",
        "in": "query"
      }
    ]
  ],
  [
    "query_hosts",
    "GET",
    "/discover/queries/hosts/v1",
    "Search for assets in your environment by providing an FQL (Falcon Query Language) filter and paging details. "
    "Returns a set of asset IDs which match the filter criteria.",
    "discover",
    [
      {
        "minimum": 0,
        "type": "integer",
        "description": "An offset used with the `limit` parameter to manage pagination of results. "
        "On your first request, don’t provide an `offset`. On subsequent requests, provide the `offset` "
        "from the previous response to continue from that place in the results.",
        "name": "offset",
        "in": "query"
      },
      {
        "maximum": 100,
        "minimum": 1,
        "type": "integer",
        "description": "The number of asset IDs to return in this response (min: 1, max: 100, default: 100). "
        "Use with the `offset` parameter to manage pagination of results.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Sort assets by their properties. A single sort field is allowed. "
        "Common sort options include:\n\n<ul><li>hostname|asc</li><li>product_type_desc|desc</li></ul>",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter assets using an FQL query. Common filter options include:\n\n"
        "<ul><li>entity_type:'managed'</li><li>product_type_desc:'Workstation'</li><li>platform_name:'Windows'</li>"
        "<li>last_seen_timestamp:>'now-7d'</li></ul>",
        "name": "filter",
        "in": "query"
      }
    ]
  ],
  [
    "query_logins",
    "GET",
    "/discover/queries/logins/v1",
    "Search for logins in your environment by providing an FQL (Falcon Query Language) filter and paging details. "
    "Returns a set of login IDs which match the filter criteria.",
    "discover",
    [
      {
        "minimum": 0,
        "type": "integer",
        "description": "An offset used with the `limit` parameter to manage pagination of results. "
        "On your first request, don’t provide an `offset`. On subsequent requests, provide the `offset` "
        "from the previous response to continue from that place in the results.",
        "name": "offset",
        "in": "query"
      },
      {
        "maximum": 100,
        "minimum": 1,
        "type": "integer",
        "description": "The number of asset IDs to return in this response (min: 1, max: 100, default: 100). "
        "Use with the `offset` parameter to manage pagination of results.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Sort assets by their properties. A single sort field is allowed. "
        "Common sort options include:\n\n<ul><li>hostname|asc</li><li>product_type_desc|desc</li></ul>",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter assets using an FQL query. Common filter options include:\n\n"
        "<ul><li>entity_type:'managed'</li><li>product_type_desc:'Workstation'</li><li>platform_name:'Windows'</li>"
        "<li>last_seen_timestamp:>'now-7d'</li></ul>",
        "name": "filter",
        "in": "query"
      }
    ]
  ]
]
