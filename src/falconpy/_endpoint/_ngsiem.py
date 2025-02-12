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
    "StartSearchStreamingV1",
    "POST",
    "/humio/api/v1/repositories/{repository}/query",
    "Initiate streaming (synchronous) search",
    "ngsiem",
    [
      {
        "type": "string",
        "description": "name of repository",
        "name": "repository",
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
  ],
  [
    "proxy_http_get",
    "GET",
    "/humio/{path}",
    "Routes a request to Humio",
    "ngsiem",
    [
      {
        "pattern": ".*",
        "type": "string",
        "description": "LogScale path",
        "name": "path",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "proxy_http_post",
    "POST",
    "/humio/{path}",
    "Routes a request to Humio",
    "ngsiem",
    [
      {
        "pattern": ".*",
        "type": "string",
        "description": "LogScale path",
        "name": "path",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "proxy_http_delete",
    "DELETE",
    "/humio/{path}",
    "Routes a request to Humio",
    "ngsiem",
    [
      {
        "pattern": ".*",
        "type": "string",
        "description": "LogScale path",
        "name": "path",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "CreateFileV1",
    "POST",
    "/loggingapi/entities/lookup-files/v1",
    "Creates a lookup file",
    "ngsiem",
    [
      {
        "type": "file",
        "description": "File to be uploaded",
        "name": "file",
        "in": "formData",
        "required": True
      },
      {
        "maxLength": 50,
        "minLength": 5,
        "type": "string",
        "description": "Name used to identify the file",
        "name": "name",
        "in": "formData",
        "required": True
      },
      {
        "maxLength": 255,
        "minLength": 5,
        "type": "string",
        "description": "File description",
        "name": "description",
        "in": "formData"
      },
      {
        "maxLength": 32,
        "minLength": 32,
        "type": "string",
        "description": "Unique identifier of the file being updated.",
        "name": "id",
        "in": "formData"
      },
      {
        "maxLength": 255,
        "minLength": 5,
        "type": "string",
        "description": "Name of repository or view to save the file",
        "name": "repo",
        "in": "formData"
      }
    ]
  ],
  [
    "UpdateFileV1",
    "PATCH",
    "/loggingapi/entities/lookup-files/v1",
    "Updates a lookup file",
    "ngsiem",
    [
      {
        "minLength": 32,
        "type": "string",
        "description": "Unique identifier of the file being updated.",
        "name": "id",
        "in": "formData",
        "required": True
      },
      {
        "maxLength": 255,
        "minLength": 5,
        "type": "string",
        "description": "File description",
        "name": "description",
        "in": "formData"
      },
      {
        "type": "file",
        "description": "File to be uploaded",
        "name": "file",
        "in": "formData"
      }
    ]
  ]
]
