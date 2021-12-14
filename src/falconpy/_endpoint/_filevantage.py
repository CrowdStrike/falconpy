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

_filevantage_endpoints = [
  [
    "getChanges",
    "GET",
    "/filevantage/entities/changes/v2",
    "Retrieve information on changes",
    "filevantage",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Comma separated values of change ids",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "queryChanges",
    "GET",
    "/filevantage/queries/changes/v2",
    "Returns one or more change IDs",
    "filevantage",
    [
      {
        "minimum": 0,
        "type": "integer",
        "description": "The first change index to return in the response. "
        "If not provided it will default to '0'. "
        "Use with the `limit` parameter to manage pagination of results.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The maximum number of changes to return in the response "
        "(default: 100; max: 500). "
        "Use with the `offset` parameter to manage pagination of results",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Sort changes using options like:\n\n"
        "- `action_timestamp` (timestamp of the change occurrence) \n\n "
        "Sort either `asc` (ascending) or `desc` (descending). "
        "For example: `action_timestamp|asc`.\n"
        "The full list of allowed sorting options can be reviewed in our API documentation.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Filter changes using a query in Falcon Query Language (FQL). \n\n"
        "Common filter options include:\n\n - `host.host_name`\n - `action_timestamp`\n\n "
        "The full list of allowed filter parameters can be reviewed in our API documentation.",
        "name": "filter",
        "in": "query"
      }
    ]
  ]
]
