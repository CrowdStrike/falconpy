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

_serverless_exports_endpoints = [
  [
    "DownloadExportFileMixin0",
    "GET",
    "/lambdas/entities/exports/files/v1",
    "Download an export file",
    "serverless_exports",
    [
      {
        "type": "string",
        "description": "Export job ID.",
        "name": "id",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "ReadExportJobsMixin0",
    "GET",
    "/lambdas/entities/exports/v1",
    "Read export jobs entities",
    "serverless_exports",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Export Job IDs to read. Allowed up to 100 IDs per request.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "LaunchExportJobMixin0",
    "POST",
    "/lambdas/entities/exports/v1",
    "Launch an export job of a Lambda Security resource. Maximum of 1 job in progress per resource. Use "
    "expand_vulnerabilities=true to get detailed vulnerability information.",
    "serverless_exports",
    [
      {
        "description": "Supported resources:  function.detections  function.vulnerabilities-expanded  "
        "function.vulnerabilities",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "QueryExportJobsMixin0",
    "GET",
    "/lambdas/queries/exports/v1",
    "Query export jobs entities",
    "serverless_exports",
    [
      {
        "type": "string",
        "description": "Filter exports using a query in Falcon Query Language (FQL). Only the last 100 jobs "
        "are returned. Supported filter fields:  resource  status",
        "name": "filter",
        "in": "query"
      }
    ]
  ]
]
