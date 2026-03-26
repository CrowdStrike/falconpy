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

_network_scan_scan_runs_endpoints = [
  [
    "aggregate_scan_runs",
    "POST",
    "/netscan/aggregates/scan-runs/GET/v1",
    "Returns \"scan-runs\" aggregations",
    "network_scan_scan_runs",
    [
      {
        "description": "Aggregation specification",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "get_scan_runs",
    "GET",
    "/netscan/entities/scan-runs/v1",
    "Get \"scan-runs\" by their IDs",
    "network_scan_scan_runs",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "IDs of \"scan-runs\" to be retrieved (Min: 1, Max: 100)",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "create_scan_runs",
    "POST",
    "/netscan/entities/scan-runs/v1",
    "Create \"scan-runs\" using provided specifications",
    "network_scan_scan_runs",
    [
      {
        "description": "\"scan-runs\" specifications",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "update_scan_runs",
    "PATCH",
    "/netscan/entities/scan-runs/v1",
    "Update \"scan-runs\" using provided specifications",
    "network_scan_scan_runs",
    [
      {
        "description": "\"scan-runs\" specifications for updating",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "query_scan_runs",
    "GET",
    "/netscan/queries/scan-runs/v1",
    "Get \"scan-runs IDs\" by filter",
    "network_scan_scan_runs",
    [
      {
        "minimum": 0,
        "type": "integer",
        "description": "An offset used with the `limit` parameter to manage pagination of results. On your "
        "first request, don’t provide an `offset`. On subsequent requests, add previous `offset` with the previous "
        "`limit` to continue from that place in the results",
        "name": "offset",
        "in": "query"
      },
      {
        "maximum": 100,
        "minimum": 1,
        "type": "integer",
        "description": "The number of \"scan-runs IDs\" to return in this response (Min: 1, Max: 100, Default: 100)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Sort \"scan-runs\" by their properties. A single sort field is allowed",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Search for \"scan-runs\" by providing an FQL filter",
        "name": "filter",
        "in": "query"
      }
    ]
  ]
]
