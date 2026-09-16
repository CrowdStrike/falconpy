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

_audit_endpoints = [
  [
    "ExportQueryResults",
    "GET",
    "/audit-logs/entities/queryjob-exports/v1",
    "Exports the results of a completed query job in CSV or JSON format",
    "audit",
    [
      {
        "type": "string",
        "description": "Job ID from a previously created query job",
        "name": "id",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "Export format: csv or json",
        "name": "format",
        "in": "query",
        "required": True
      },
      {
        "type": "boolean",
        "description": "When true, includes descriptions for category and action fields (default: False)",
        "name": "include_descriptions",
        "in": "query"
      },
      {
        "type": "boolean",
        "description": "When true, filters extension keys based on audit definition YAML and includes "
        "descriptions for extension keys (default: False)",
        "name": "include_extension_metadata",
        "in": "query"
      }
    ]
  ],
  [
    "GetQueryResults",
    "GET",
    "/audit-logs/entities/queryjob-results/v1",
    "Retrieves the results of a completed query job with pagination",
    "audit",
    [
      {
        "type": "string",
        "description": "Job ID from a previously created query job",
        "name": "id",
        "in": "query",
        "required": True
      },
      {
        "type": "integer",
        "description": "Starting position for pagination (default: 0)",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Maximum number of records to return (default: 100)",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "boolean",
        "description": "When true, includes descriptions for category and action fields (default: False)",
        "name": "include_descriptions",
        "in": "query"
      },
      {
        "type": "boolean",
        "description": "When true, filters extension keys based on audit definition YAML and includes "
        "descriptions for extension keys (default: False)",
        "name": "include_extension_metadata",
        "in": "query"
      }
    ]
  ],
  [
    "PollQueryJobStatus",
    "GET",
    "/audit-logs/entities/queryjobs/v1",
    "Checks the status of a previously created query job",
    "audit",
    [
      {
        "type": "string",
        "description": "Job ID from a previously created query job",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "CreateQueryJob",
    "POST",
    "/audit-logs/queries/queryjobs/v1",
    "Creates an asynchronous query job to retrieve audit log entries based on specified filters",
    "audit",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ]
]
