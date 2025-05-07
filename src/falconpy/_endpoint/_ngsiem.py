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

_ngsiem_endpoints = [
  [
    "UploadLookupV1",
    "POST",
    "/humio/api/v1/repositories/{repository}/files",
    "Upload file to NGSIEM",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "type": "file",
        "description": "file to upload",
        "name": "file",
        "in": "formData",
        "required": True
      }
    ]
  ],
  [
    "GetLookupV1",
    "GET",
    "/humio/api/v1/repositories/{repository}/files/{filename}",
    "Download lookup file from NGSIEM",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "name of lookup file",
        "name": "filename",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "GetLookupFromPackageWithNamespaceV1",
    "GET",
    "/humio/api/v1/repositories/{repository}/files/{namespace}/{package}/{filename}",
    "Download lookup file in namespaced package from NGSIEM",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "name of namespace",
        "name": "namespace",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "name of package",
        "name": "package",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "name of lookup file",
        "name": "filename",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "GetLookupFromPackageV1",
    "GET",
    "/humio/api/v1/repositories/{repository}/files/{package}/{filename}",
    "Download lookup file in package from NGSIEM",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "name of package",
        "name": "package",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "name of lookup file",
        "name": "filename",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "StartSearchV1",
    "POST",
    "/humio/api/v1/repositories/{repository}/queryjobs",
    "Initiate search",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "description": "Query Job JSON request body",
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "GetSearchStatusV1",
    "GET",
    "/humio/api/v1/repositories/{repository}/queryjobs/{id}",
    "Get status of search",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "id of query",
        "name": "id",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "StopSearchV1",
    "DELETE",
    "/humio/api/v1/repositories/{repository}/queryjobs/{id}",
    "Stop search",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
        "in": "path",
        "required": True
      },
      {
        "type": "string",
        "description": "id of query",
        "name": "id",
        "in": "path",
        "required": True
      }
    ]
  ]
]
