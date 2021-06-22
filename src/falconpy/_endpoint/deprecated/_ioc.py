"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

_endpoint.deprecated._ioc - Internal API endpoint constant library

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

_ioc_endpoints = [
  [
    "indicator.combined.v1",
    "GET",
    "/iocs/combined/indicator/v1",
    "Get Combined for Indicators.",
    "ioc",
    [
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The offset to start retrieving records from. Offset and After params are mutually exclusive. "
        "If none provided then scrolling will be used by default.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The maximum records to return.",
        "name": "limit",
        "in": "query"
      },
      {
        "enum": [
          "action",
          "applied_globally",
          "metadata.av_hits",
          "metadata.company_name.raw",
          "created_by",
          "created_on",
          "expiration",
          "expired",
          "metadata.filename.raw",
          "modified_by",
          "modified_on",
          "metadata.original_filename.raw",
          "metadata.product_name.raw",
          "metadata.product_version",
          "severity_number",
          "source",
          "type",
          "value"
        ],
        "type": "string",
        "description": "The sort expression that should be used to sort the results.",
        "name": "sort",
        "in": "query"
      }
    ]
  ],
  [
    "indicator.get.v1",
    "GET",
    "/iocs/entities/indicators/v1?ids={}",
    "Get Indicators by ids.",
    "ioc",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "The ids of the Indicators to retrieve",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "indicator.create.v1",
    "POST",
    "/iocs/entities/indicators/v1",
    "Create Indicators.",
    "ioc",
    [
      {
        "type": "string",
        "description": "The username",
        "name": "X-CS-USERNAME",
        "in": "header"
      },
      {
        "type": "bool",
        "description": "Whether to submit to retrodetects",
        "name": "retrodetects",
        "in": "query"
      },
      {
        "type": "bool",
        "default": False,
        "description": "Set to true to ignore warnings and add all IOCs",
        "name": "ignore_warnings",
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
    "indicator.update.v1",
    "PATCH",
    "/iocs/entities/indicators/v1",
    "Update Indicators.",
    "ioc",
    [
      {
        "type": "string",
        "description": "The username",
        "name": "X-CS-USERNAME",
        "in": "header"
      },
      {
        "type": "bool",
        "description": "Whether to submit to retrodetects",
        "name": "retrodetects",
        "in": "query"
      },
      {
        "type": "bool",
        "default": False,
        "description": "Set to true to ignore warnings and add all IOCs",
        "name": "ignore_warnings",
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
    "indicator.delete.v1",
    "DELETE",
    "/iocs/entities/indicators/v1?ids={}",
    "Delete Indicators by ids.",
    "ioc",
    [
      {
        "type": "string",
        "description": "The FQL expression to delete Indicators in bulk. If both 'filter' and 'ids' are provided, "
        "then filter takes precedence and ignores ids.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "The ids of the Indicators to delete. If both 'filter' and 'ids' are provided, "
        "then filter takes precedence and ignores ids",
        "name": "ids",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The comment why these indicators were deleted",
        "name": "comment",
        "in": "query"
      }
    ]
  ],
  [
    "indicator.search.v1",
    "GET",
    "/iocs/queries/indicators/v1",
    "Search for Indicators.",
    "ioc",
    [
      {
        "type": "string",
        "description": "The filter expression that should be used to limit the results.",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The offset to start retrieving records from. Offset and After params are mutually exclusive. "
        "If none provided then scrolling will be used by default.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The maximum records to return.",
        "name": "limit",
        "in": "query"
      },
      {
        "enum": [
          "action",
          "applied_globally",
          "metadata.av_hits",
          "metadata.company_name.raw",
          "created_by",
          "created_on",
          "expiration",
          "expired",
          "metadata.filename.raw",
          "modified_by",
          "modified_on",
          "metadata.original_filename.raw",
          "metadata.product_name.raw",
          "metadata.product_version",
          "severity_number",
          "source",
          "type",
          "value"
        ],
        "type": "string",
        "description": "The sort expression that should be used to sort the results.",
        "name": "sort",
        "in": "query"
      }
    ]
  ]
]
