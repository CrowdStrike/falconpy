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
from typing import Dict, List, Union


def cspm_registration_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, str]]]:
    """Create a properly formatted CSPM registration payload.

    {
        "resources": [
            {
                "account_id": "string",
                "account_type": "string",
                "behavior_assessment_enabled": true,
                "client_id": "string",
                "cloudtrail_region": "string",
                "default_subscription": true,
                "iam_role_arn": "string",
                "is_master": true,
                "organization_id": "string",
                "remediation_region": "string",
                "remediation_tou_accepted": "timestamp",
                "sensor_management_enabled": true,
                "subscription_id": "string"
                "tenant_id": "string",
                "use_existing_cloudtrail": true
                "years_valid": integer
            }
        ]
    }
    """
    returned_payload: Dict[str, List[Dict[str, str]]] = {}
    returned_payload["resources"] = []
    item = {}
    keys = ["account_id", "account_type", "cloudtrail_region", "iam_role_arn",
            "organization_id", "tenant_id", "subscription_id", "remediation_region",
            "remediation_tou_accepted", "client_id"
            ]
    bool_keys = ["behavior_assessment_enabled", "is_master", "sensor_management_enabled",
                 "use_existing_cloudtrail", "default_subscription"
                 ]
    int_keys = ["years_valid"]
    for key in keys:
        if passed_keywords.get(key, None):
            item[key] = passed_keywords.get(key, None)

    for key in bool_keys:
        if passed_keywords.get(key, None) is not None:
            item[key] = passed_keywords.get(key, None)

    for key in int_keys:
        if passed_keywords.get(key, -1) >= 0:
            item[key] = passed_keywords.get(key, -1)

    returned_payload["resources"].append(item)

    return returned_payload


def cspm_policy_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, Union[str, bool, List[str]]]]]:
    """Create a properly formatted CSPM policy update payload.

    {
    "resources": [
        {
            "account_id": "string",
            "account_ids": [
                "string"
            ],
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
    returned_payload: Dict[str, List[Dict[str, Union[str, bool, List[str]]]]] = {}
    returned_payload["resources"] = []
    keys = ["account_id", "severity"]
    bool_keys = ["enabled", "tag_excluded"]
    int_keys = ["policy_id"]
    list_keys = ["account_ids", "regions"]
    item = {}
    for key in keys:
        if passed_keywords.get(key, None):
            item[key] = passed_keywords.get(key, None)

    for key in bool_keys:
        if passed_keywords.get(key, None) is not None:
            item[key] = passed_keywords.get(key, None)

    for key in int_keys:
        if passed_keywords.get(key, -1) >= 0:
            item[key] = passed_keywords.get(key, -1)

    for key in list_keys:
        if passed_keywords.get(key, None) is not None:
            provided = passed_keywords.get(key, None)
            if isinstance(provided, str):
                provided = provided.split(",")
            item[key] = provided

    returned_payload["resources"].append(item)

    return returned_payload


def cspm_scan_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, str]]]:
    """Create a properly formmatted CSPM scan schedule payload.

    {
        "resources": [
            {
                "cloud_platform": "string",
                "next_scan_timestamp": "2021-10-25T05:22:27.365Z",
                "scan_interval": "string",
                "scan_schedule": "string"
            }
        ]
    }
    """
    returned_payload: Dict[str, List[Dict[str, str]]] = {}
    returned_payload["resources"] = []
    item = {}
    for key in ["cloud_platform", "next_scan_timestamp", "scan_interval", "scan_schedule"]:
        if passed_keywords.get(key, None):
            item[key] = passed_keywords.get(key, None)

    returned_payload["resources"].append(item)

    return returned_payload
