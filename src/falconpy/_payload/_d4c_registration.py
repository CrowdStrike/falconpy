"""Internal payload handling library - D4C Registration Payloads.

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


def aws_d4c_registration_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted AWS registration payload.

    {
        "resources": [
            {
                "account_id": "string",
                "account_type": "string",
                "cloudtrail_region": "string",
                "is_master": true,
                "organization_id": "string"
            }
        ]
    }
    """
    returned_payload = {}
    returned_payload["resources"] = []
    keys = ["account_id", "account_type", "cloudtrail_region", "organization_id"]
    item = {}
    for key in keys:
        if passed_keywords.get(key, None):
            item[key] = passed_keywords.get(key)
    if passed_keywords.get("is_master", None) is not None:
        item["is_master"] = passed_keywords.get("is_master")

    returned_payload["resources"].append(item)

    return returned_payload


def azure_registration_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted Azure registration payload.

    {
        "resources": [
            {
                "subscription_id": "string",
                "tenant_id": "string"
            }
        ]
    }
    """
    returned_payload = {}
    returned_payload["resources"] = []
    item = {}
    if passed_keywords.get("subscription_id", None):
        item["subscription_id"] = passed_keywords.get("subscription_id", None)
    if passed_keywords.get("tenant_id", None):
        item["tenant_id"] = passed_keywords.get("tenant_id", None)
    returned_payload["resources"].append(item)

    return returned_payload
