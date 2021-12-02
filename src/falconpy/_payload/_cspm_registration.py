"""Internal payload handling library - CSPM Registration (Horizon) Payloads.

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


def cspm_registration_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted CSPM registration payload.

    {
        "resources": [
            {
                "account_id": "string",
                "cloudtrail_region": "string",
                "organization_id": "string",
                "tenant_id": "string",
                "subscription_id": "string"
            }
        ]
    }
    """
    returned_payload = {}
    returned_payload["resources"] = []
    item = {}
    keys = ["account_id", "cloudtrail_region", "organization_id", "tenant_id", "subscription_id"]
    for key in keys:
        if passed_keywords.get(key, None):
            item[key] = passed_keywords.get(key, None)

    returned_payload["resources"].append(item)

    return returned_payload


def cspm_policy_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted CSPM policy update payload.

    {
    "resources": [
        {
            "account_id": "string",
            "enabled": boolean,
            "policy_id": integer,
            "regions": [
                "string"
            ],
            "severity": "string",
            "tag_excluded": boolean
        }
    ]
    }
    """
    returned_payload = {}
    returned_payload["resources"] = []
    item = {}
    if passed_keywords.get("account_id", None):
        item["account_id"] = passed_keywords.get("account_id", None)
    if passed_keywords.get("enabled", None) is not None:
        item["enabled"] = passed_keywords.get("enabled", None)
    if passed_keywords.get("policy_id", -1) > 0:
        item["policy_id"] = passed_keywords.get("policy_id", None)
    if passed_keywords.get("severity", None):
        item["severity"] = passed_keywords.get("severity", None)
    if passed_keywords.get("tag_excluded", None) is not None:
        item["tag_excluded"] = passed_keywords.get("tag_excluded", None)
    region_list = passed_keywords.get("regions", None)
    if region_list:
        if isinstance(region_list, str):
            region_list = region_list.split(",")
        item["regions"] = region_list

    returned_payload["resources"].append(item)

    return returned_payload


def cspm_scan_payload(passed_keywords: dict) -> dict:
    """Create a properly formmatted CSPM scan schedule payload.

    {
        "resources": [
            {
                "cloud_platform": "string",
                "next_scan_timestamp": "2021-10-25T05:22:27.365Z",
                "scan_schedule": "string"
            }
        ]
    }
    """
    returned_payload = {}
    returned_payload["resources"] = []
    item = {}
    for key in ["cloud_platform", "next_scan_timestamp", "scan_schedule"]:
        if passed_keywords.get(key, None):
            item[key] = passed_keywords.get(key, None)

    returned_payload["resources"].append(item)

    return returned_payload
