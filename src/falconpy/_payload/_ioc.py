"""Internal payload handling library - Indicators of Compromise.

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


def indicator_object(passed_keywords: dict) -> dict:  # pylint: disable=R0912  # noqa: C901
    """Create a properly formatted single indicator payload.

    {
      "action": "string",
      "applied_globally": true,
      "description": "string",
      "expiration": "2021-10-22T10:40:39.372Z",
      "host_groups": [
        "string"
      ],
      "metadata": {
        "filename": "string"
      },
      "mobile_action": "string",
      "platforms": [
        "string"
      ],
      "severity": "string",
      "source": "string",
      "tags": [
        "string"
      ],
      "type": "string",
      "value": "string"
    }
    """
    # flake8 / pylint both complain about complexity due to the number of if statements.
    # Ignoring the complaint as this is just running through the potential passed keywords.
    returned_payload = {}
    if passed_keywords.get("action", None):
        returned_payload["action"] = passed_keywords.get("action", None)
    if passed_keywords.get("applied_globally", None):
        returned_payload["applied_globally"] = passed_keywords.get("applied_globally", None)
    if passed_keywords.get("description", None):
        returned_payload["description"] = passed_keywords.get("description", None)
    if passed_keywords.get("expiration", None):
        returned_payload["expiration"] = passed_keywords.get("expiration", None)
    if passed_keywords.get("host_groups", None):
        returned_payload["host_groups"] = passed_keywords.get("host_groups", None)
    if passed_keywords.get("metadata", None):
        returned_payload["metadata"] = passed_keywords.get("metadata", None)
    if passed_keywords.get("filename", None):
        returned_payload["metadata"] = {
            "filename": passed_keywords.get("filename", None)
        }
    if passed_keywords.get("mobile_action", None):
        returned_payload["mobile_action"] = passed_keywords.get("mobile_action", None)
    if passed_keywords.get("platforms", None):
        returned_payload["platforms"] = passed_keywords.get("platforms", None)
    if passed_keywords.get("severity", None):
        returned_payload["severity"] = passed_keywords.get("severity", None)
    if passed_keywords.get("source", None):
        returned_payload["source"] = passed_keywords.get("source", None)
    if passed_keywords.get("tags", None):
        returned_payload["tags"] = passed_keywords.get("tags", None)
    if passed_keywords.get("type", None):
        returned_payload["type"] = passed_keywords.get("type", None)
    if passed_keywords.get("value", None):
        returned_payload["value"] = passed_keywords.get("value", None)
    if passed_keywords.get("id", None):
        returned_payload["id"] = passed_keywords.get("id", None)

    return returned_payload


def indicator_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted indicator payload.

    {
        "comment": "string",
        "indicators": [
            {
            "action": "string",
            "applied_globally": true,
            "description": "string",
            "expiration": "2021-10-22T10:40:39.372Z",
            "host_groups": [
                "string"
            ],
            "metadata": {
                "filename": "string"
            },
            "mobile_action": "string",
            "platforms": [
                "string"
            ],
            "severity": "string",
            "source": "string",
            "tags": [
                "string"
            ],
            "type": "string",
            "value": "string"
            }
        ]
    }
    """
    returned_payload = {}
    if passed_keywords.get("comment", None):
        returned_payload["comment"] = passed_keywords.get("comment", None)
    if passed_keywords.get("indicators", None):
        returned_payload["indicators"] = passed_keywords.get("indicators", None)
    else:
        returned_payload["indicators"] = [indicator_object(passed_keywords=passed_keywords)]

    return returned_payload


def indicator_update_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted indicator update payload.

    {
        "bulk_update": {
            "action": "string",
            "applied_globally": true,
            "description": "string",
            "expiration": "2021-10-22T11:03:16.123Z",
            "filter": "string",
            "host_groups": [
                "string"
            ],
            "mobile_action": "string",
            "platforms": [
                "string"
            ],
            "severity": "string",
            "source": "string",
            "tags": [
                "string"
            ]
        },
        "comment": "string",
        "indicators": [
            {
                "action": "string",
                "applied_globally": true,
                "description": "string",
                "expiration": "2021-10-22T11:03:16.123Z",
                "host_groups": [
                    "string"
                ],
                "id": "string",
                "metadata": {
                    "filename": "string"
                },
                "mobile_action": "string",
                "platforms": [
                    "string"
                ],
                "severity": "string",
                "source": "string",
                "tags": [
                    "string"
                ]
            }
        ]
    }
    """
    returned_payload = {}
    if passed_keywords.get("comment", None):
        returned_payload["comment"] = passed_keywords.get("comment", None)
    if passed_keywords.get("bulk_update", None):
        returned_payload["bulk_update"] = passed_keywords.get("bulk_update", None)
    if passed_keywords.get("indicators", None):
        returned_payload["indicators"] = passed_keywords.get("indicators", None)
    else:
        returned_payload["indicators"] = [indicator_object(passed_keywords=passed_keywords)]

    return returned_payload
