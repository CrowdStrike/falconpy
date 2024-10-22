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

_quick_scan_pro_endpoints = [
  [
    "UploadFileMixin0Mixin94",
    "POST",
    "/quickscanpro/entities/files/v1",
    "Uploads a file to be further analyzed with QuickScan Pro. The samples expire after 90 days.",
    "quick_scan_pro",
    [
      {
        "type": "file",
        "description": "Binary file to be uploaded. Max file size: 256 MB.",
        "name": "file",
        "in": "formData",
        "required": True
      },
      {
        "type": "boolean",
        "default": False,
        "description": "If true, after upload, it starts scanning immediately. Default scan mode is 'false'",
        "name": "scan",
        "in": "formData"
      }
    ]
  ],
  [
    "DeleteFile",
    "DELETE",
    "/quickscanpro/entities/files/v1",
    "Deletes file by its sha256 identifier.",
    "quick_scan_pro",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "File's SHA256",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "GetScanResult",
    "GET",
    "/quickscanpro/entities/scans/v1",
    "Gets the result of an QuickScan Pro scan.",
    "quick_scan_pro",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Scan job IDs previously created by LaunchScan",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "LaunchScan",
    "POST",
    "/quickscanpro/entities/scans/v1",
    "Starts scanning a file uploaded through '/quickscanpro/entities/files/v1'.",
    "quick_scan_pro",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "DeleteScanResult",
    "DELETE",
    "/quickscanpro/entities/scans/v1",
    "Deletes the result of an QuickScan Pro scan.",
    "quick_scan_pro",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Scan job IDs previously created by LaunchScan",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "QueryScanResults",
    "GET",
    "/quickscanpro/queries/scans/v1",
    "Gets QuickScan Pro scan jobs for a given FQL filter.",
    "quick_scan_pro",
    [
      {
        "type": "string",
        "description": "FQL query which mentions the SHA256 field",
        "name": "filter",
        "in": "query",
        "required": True
      },
      {
        "type": "integer",
        "description": "The offset to start retrieving ids from.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "default": 50,
        "description": "Maximum number of IDs to return. Max: 5000.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Sort order: `asc` or `desc`. Sort supported fields `created_timestamp`",
        "name": "sort",
        "in": "query"
      }
    ]
  ]
]
