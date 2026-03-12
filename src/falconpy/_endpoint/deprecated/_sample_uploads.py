"""Internal API endpoint constant library (deprecated operations).

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

_sample_uploads_endpoints = [
  [
    "ArchiveUploadV1",
    "POST",
    "/archives/entities/archives/v1",
    "Uploads an archive and extracts files list from it. Operation is asynchronous use "
    "`/archives/entities/archives/v1` to check the status. After uploading, use `/archives/entities/extractions/v1` "
    " to copy the file to internal storage making it available for content analysis.\nThis method is deprecated in "
    "favor of `/archives/entities/archives/v2`",
    "sample_uploads",
    [
      {
        "description": "Content of the uploaded archive in binary format. For example, use --data-binary "
        "@$FILE_PATH when using cURL. Max file size: 100 MB.\n\nAccepted file formats:\n  Portable executables: .zip, "
        ".7z.",
        "name": "body",
        "in": "body",
        "required": True
      },
      {
        "type": "string",
        "description": "Name of the archive.",
        "name": "name",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "Archive password.",
        "name": "password",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": True,
        "description": "Defines visibility of this file, either via the API or the Falcon console.\n  true: "
        "File is only shown to users within your customer account  false: File can be seen by other CrowdStrike "
        "customers \n\nDefault: True.",
        "name": "is_confidential",
        "in": "query"
      },
      {
        "type": "string",
        "description": "A descriptive comment to identify the file for other users.",
        "name": "comment",
        "in": "query"
      }
    ]
  ]
]
