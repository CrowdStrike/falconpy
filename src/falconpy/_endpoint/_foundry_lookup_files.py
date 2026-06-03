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

_foundry_lookup_files_endpoints = [
  [
    "CreateFileV1",
    "POST",
    "/loggingapi/entities/lookup-files/v1",
    "Creates a lookup file within a foundry app",
    "foundry_lookup_files",
    [
      {
        "type": "file",
        "description": "File to be uploaded",
        "name": "file",
        "in": "formData",
        "required": True
      },
      {
        "type": "string",
        "maxLength": 50,
        "minLength": 5,
        "description": "Name used to identify the file",
        "name": "name",
        "in": "formData",
        "required": True
      },
      {
        "type": "string",
        "maxLength": 255,
        "minLength": 5,
        "description": "File description",
        "name": "description",
        "in": "formData"
      },
      {
        "type": "string",
        "maxLength": 32,
        "minLength": 32,
        "description": "Unique identifier of the file being updated.",
        "name": "id",
        "in": "formData"
      },
      {
        "type": "string",
        "maxLength": 255,
        "minLength": 1,
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
    "Updates a lookup file within a Foundry app",
    "foundry_lookup_files",
    [
      {
        "type": "string",
        "minLength": 32,
        "description": "Unique identifier of the file being updated.",
        "name": "id",
        "in": "formData",
        "required": True
      },
      {
        "type": "string",
        "maxLength": 255,
        "minLength": 5,
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
