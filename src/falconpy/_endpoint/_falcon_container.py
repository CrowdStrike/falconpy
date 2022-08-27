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

_falcon_container_endpoints = [
  [
    "GetCredentials",
    "GET",
    "/container-security/entities/image-registry-credentials/v1",
    "Gets the registry credentials",
    "falcon_container",
    []
  ],
  [
    "GetImageAssessmentReport",
    "GET",
    "/reports",
    "Retrieves the Assessment report for the Image ID provided.",
    "falcon_container",
    [
      {
        "type": "string",
        "description": "The repository the image resides within.",
        "name": "repository",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "The image tag.",
        "name": "tag",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "DeleteImageDetails",
    "DELETE",
    "/images/{}",
    "Delete Images by ids.",
    "falcon_container",
    [
      {
        "type": "string",
        "description": "The ID of the image to be deleted.",
        "name": "image_id",
        "in": "path",
        "required": True
      }
    ]
  ],
  [
    "ImageMatchesPolicy",
    "GET",
    "/policy-checks",
    "After an image scan, use this operation to see if any images match a policy. If deny is true,"
    " the policy suggestion is that you do not deploy the image in your environment.",
    "falcon_container",
    [
      {
        "type": "string",
        "description": "The repository the image resides within.",
        "name": "repository",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "The image tag.",
        "name": "tag",
        "in": "query",
        "required": True
      }
    ]
  ]
]
