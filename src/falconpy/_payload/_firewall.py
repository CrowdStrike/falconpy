"""Internal payload handling library - Firewall Payloads.

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


def firewall_policy_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted firewall policy payload.

    Supports create and update operations. Single policy only.
    {
        "resources": [
            {
                "clone_id": "string",
                "description": "string",
                "name": "string",
                "platform_name": "Windows",
            }
        ]
    }
    """
    returned_payload = {}
    resources = []
    item = {}
    keys = ["clone_id", "description", "name", "platform_name"]
    for key in keys:
        if passed_keywords.get(key, None):
            item[key] = passed_keywords.get(key, None)

    resources.append(item)
    returned_payload["resources"] = resources

    return returned_payload


def firewall_container_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted firewall policy container payload.

    {
        "default_inbound": "string",
        "default_outbound": "string",
        "enforce": true,
        "is_default_policy": true,
        "platform_id": "string",
        "policy_id": "string",
        "rule_group_ids": [
            "string"
        ],
        "test_mode": true,
        "tracking": "string"
    }
    """
    returned_payload = {}
    keys = ["default_inbound", "default_outbound", "platform_id", "tracking"]
    for key in keys:
        if passed_keywords.get(key, None):
            returned_payload[key] = passed_keywords.get(key, None)
    if passed_keywords.get("enforce", None) is not None:
        returned_payload["enforce"] = passed_keywords.get("enforce", None)
    if passed_keywords.get("is_default_policy", None) is not None:
        returned_payload["is_default_policy"] = passed_keywords.get("is_default_policy", None)
    if passed_keywords.get("test_mode", None) is not None:
        returned_payload["test_mode"] = passed_keywords.get("test_mode", None)
    rg_list = passed_keywords.get("rule_group_ids", None)
    if rg_list:
        if isinstance(rg_list, str):
            rg_list = rg_list.split(",")
        returned_payload["rule_group_ids"] = rg_list

    return returned_payload


def firewall_rule_group_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted firewall rule group payload.

    {
        "description": "string",
        "enabled": true,
        "name": "string",
        "rules": [
            {
                "action": "string",
                "address_family": "string",
                "description": "string",
                "direction": "string",
                "enabled": true,
                "fields": [
                    {
                        "final_value": "string",
                        "label": "string",
                        "name": "string",
                        "type": "string",
                        "value": "string",
                        "values": [
                            "string"
                        ]
                    }
                ],
                "icmp": {
                    "icmp_code": "string",
                    "icmp_type": "string"
                },
                "local_address": [
                    {
                        "address": "string",
                        "netmask": 0
                    }
                ],
                "local_port": [
                    {
                        "end": 0,
                        "start": 0
                    }
                ],
                "log": true,
                "monitor": {
                    "count": "string",
                    "period_ms": "string"
                },
                "name": "string",
                "platform_ids": [
                    "string"
                ],
                "protocol": "string",
                "remote_address": [
                    {
                        "address": "string",
                        "netmask": 0
                    }
                ],
                "remote_port": [
                    {
                        "end": 0,
                        "start": 0
                    }
                ],
                "temp_id": "string"
            }
        ]
    }
    """
    returned_payload = {}
    keys = ["description", "name"]
    for key in keys:
        if passed_keywords.get(key, None):
            returned_payload[key] = passed_keywords.get(key, None)
    if passed_keywords.get("enabled", None) is not None:
        returned_payload["enabled"] = passed_keywords.get("enabled", None)
    rules = passed_keywords.get("rules", None)
    if rules:
        if isinstance(rules, list):
            returned_payload["rules"] = rules
        else:
            returned_payload["rules"] = [rules]

    return returned_payload


def firewall_rule_group_update_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted firewall rule group payload.

    {
        "diff_operations": [
            {
                "from": "string",
                "op": "string",
                "path": "string"
            }
        ],
        "diff_type": "string",
        "id": "string",
        "rule_ids": [
            "string"
        ],
        "rule_versions": [
            0
        ],
        "tracking": "string"
    }
    """
    returned_payload = {}
    keys = ["diff_type", "id", "tracking"]
    for key in keys:
        if passed_keywords.get(key, None):
            returned_payload[key] = passed_keywords.get(key, None)
    id_list = passed_keywords.get("rule_ids", None)
    if id_list:
        if isinstance(id_list, str):
            id_list = id_list.split(",")
        returned_payload["rule_ids"] = id_list
    ver_list = passed_keywords.get("rule_versions", None)
    if ver_list:
        if isinstance(ver_list, str):
            ver_list = ver_list.split(",")
        returned_payload["rule_versions"] = ver_list
    diffs = passed_keywords.get("diff_operations", None)
    if diffs:
        if isinstance(diffs, list):
            returned_payload["diff_operations"] = diffs
        else:
            returned_payload["diff_operations"] = [diffs]

    return returned_payload
