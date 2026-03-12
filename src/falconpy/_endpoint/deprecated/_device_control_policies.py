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

_device_control_policies_endpoints = [
  [
    "getDefaultDeviceControlPolicies",
    "GET",
    "/policy/entities/default-device-control/v1",
    "Retrieve the configuration for a Default Device Control Policy",
    "device_control_policies",
    []
  ],
  [
    "updateDefaultDeviceControlPolicies",
    "PATCH",
    "/policy/entities/default-device-control/v1",
    "Update the configuration for a Default Device Control Policy",
    "device_control_policies",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "getDeviceControlPolicies",
    "GET",
    "/policy/entities/device-control/v1",
    "Retrieve a set of Device Control Policies by specifying their IDs",
    "device_control_policies",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The IDs of the Device Control Policies to return",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "updateDeviceControlPolicies",
    "PATCH",
    "/policy/entities/device-control/v1",
    "Update Device Control Policies by specifying the ID of the policy and details to update",
    "device_control_policies",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "createDeviceControlPolicies",
    "POST",
    "/policy/entities/device-control/v1",
    "Create Device Control Policies by specifying details about the policy to create",
    "device_control_policies",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ]
]
