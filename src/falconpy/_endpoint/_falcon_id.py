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

_falcon_id_endpoints = [
  [
    "GetThirdPartyPasskeyRegistry",
    "GET",
    "/falcon-id/entities/third-party-passkeys/v1",
    "Fetches third party passkey registries",
    "falcon_id",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Third party passkey registry IDs to retrieve",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "DeleteThirdPartyPasskeyRegistry",
    "DELETE",
    "/falcon-id/entities/third-party-passkeys/v1",
    "Deletes third party passkey registries",
    "falcon_id",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Third party passkey registry IDs to delete",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "UpdateThirdPartyPasskeyRegistry",
    "PATCH",
    "/falcon-id/entities/third-party-passkeys/v1",
    "Updates third party passkey registries",
    "falcon_id",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "QueryThirdPartyPasskeyRegistry",
    "GET",
    "/falcon-id/queries/third-party-passkeys/v1",
    "Query third party passkey registries",
    "falcon_id",
    [
      {
        "type": "string",
        "description": "FQL filter",
        "name": "filter",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Paging offset",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "Paging limit",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "Sorting field and direction",
        "name": "sort",
        "in": "query"
      }
    ]
  ]
]
