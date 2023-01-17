"""Internal payload handling library - Device Control Policy Payloads.

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


def device_policy_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted device control policy payload.

    Supports create and update operations. Single policy only.
    {
        "resources": [
            {
                "clone_id": "string",
                "description": "string",
                "name": "string",
                "platform_name": "Windows",
                "settings": {
                    "classes": [
                    {
                        "action": "FULL_ACCESS",
                        "exceptions": [
                        {
                            "action": "string",
                            "class": "string",
                            "combined_id": "string",
                            "id": "string",
                            "match_method": "string",
                            "product_id": "string",
                            "product_id_decimal": "string",
                            "product_name": "string",
                            "serial_number": "string",
                            "vendor_id": "string",
                            "vendor_id_decimal": "string",
                            "vendor_name": "string"
                        }
                        ],
                        "id": "string"
                    }
                    ],
                    "end_user_notification": "TRUE",
                    "enforcement_mode": "string",
                    "id": "string"
                }
            }
        ]
    }
    """
    returned_payload = {}
    resources = []
    item = {}
    keys = ["clone_id", "description", "name", "platform_name", "id"]
    for key in keys:
        if passed_keywords.get(key, None):
            item[key] = passed_keywords.get(key, None)

    # Settings classes not currently abstracted
    if passed_keywords.get("settings", None):
        item["settings"] = passed_keywords.get("settings", None)

    resources.append(item)
    returned_payload["resources"] = resources

    return returned_payload


def default_device_policy_config_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted device control policy default configuration payload.

    {
        "custom_notifications": {
            "blocked_notification": {
                "custom_message": "string",
                "use_custom": boolean
            },
            "restricted_notification": {
                "custom_message": "string",
                "use_custom": boolean
            }
        }
    }
    """
    returned_payload = {}
    custom_notifications = {}
    blocked_notification = {}
    restricted_notification = {}

    # Blocked notifications
    if passed_keywords.get("blocked_custom_message", None):
        blocked_notification["custom_message"] = passed_keywords.get("blocked_custom_message", None)
        blocked_notification["use_custom"] = True
        custom_notifications["blocked_notification"] = blocked_notification

    # Restricted notifications
    if passed_keywords.get("restricted_custom_message", None):
        restricted_notification["custom_message"] = passed_keywords.get("restricted_custom_message", None)
        restricted_notification["use_custom"] = True
        custom_notifications["restricted_notification"] = restricted_notification

    # Passing the entire dictionary for either type will override other provided keywords
    keys = ["blocked_notification", "restricted_notification"]
    for key in keys:
        if passed_keywords.get(key, None):
            custom_notifications[key] = passed_keywords.get(key, None)

    if custom_notifications:
        returned_payload["custom_notifications"] = custom_notifications

    return returned_payload
