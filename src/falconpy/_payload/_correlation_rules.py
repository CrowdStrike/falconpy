"""Internal payload handling library - Correlation rules.

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


def correlation_rules_payload(passed_keywords: dict) -> Dict[str, Union[str, int, list, bool]]:
    """Craft a properly formatted correlation rules payload.

    {
        "anomaly": {
            "event_field_name": "string",
            "lookback_timeframe": "string",
            "scope": "string",
            "type": "string",
            "use_established_entity_only": true
        },
        "comment": "string",
        "customer_id": "string",
        "description": "string",
        "guardrail_notifications": [
            {
            "config": {
                "cid": "string",
                "config_id": "string",
                "plugin_id": "string",
                "recipients": [
                "string"
                ],
                "severity": "string"
            },
            "options": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
            },
            "type": "string"
            }
        ],
        "mitre_attack": [
            {
            "tactic_id": "string",
            "technique_id": "string"
            }
        ],
        "name": "string",
        "notifications": [
            {
            "config": {
                "cid": "string",
                "config_id": "string",
                "plugin_id": "string",
                "recipients": [
                "string"
                ],
                "severity": "string"
            },
            "options": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
            },
            "type": "string"
            }
        ],
        "operation": {
            "schedule": {
            "definition": "string"
            },
            "start_on": "2026-04-17T16:10:23.160Z",
            "stop_on": "2026-04-17T16:10:23.160Z",
            "suppression": {
            "filter": {
                "field_based": {
                "field": "string"
                }
            },
            "suppression_period": "string"
            }
        },
        "search": {
            "case_template_id": "string",
            "execution_mode": "string",
            "filter": "string",
            "lookback": "string",
            "outcome": "string",
            "trigger_mode": "string",
            "use_ingest_time": true
        },
        "severity": 0,
        "status": "string",
        "tactic": "string",
        "technique": "string",
        "template_id": "string",
        "trigger_on_create": true
    }
    """
    returned = {}
    keys = ["anomaly", "comment", "customer_id", "description", "name",
            "operation", "search", "severity", "status", "tactic",
            "technique", "template_id", "id"
            ]
    list_keys = ["guardrail_notifications", "mitre_attack", "notifications"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned[key] = passed_keywords.get(key, None)
    for key in list_keys:
        if passed_keywords.get(key, None) is not None:
            key_value = passed_keywords.get(key, None)
            if isinstance(key_value, str):
                key_value = key_value.split(",")
            returned[key] = key_value
    if passed_keywords.get("trigger_on_create", None) is not None:
        returned["trigger_on_create"] = passed_keywords.get("trigger_on_create", None)

    return returned


def correlation_rules_export_payload(passed_keywords: dict) -> Dict[str, Union[str, bool, dict]]:
    """Craft a properly formatted correlation rule export payload.

    {
        "get_latest": boolean,
        "report_format": "string",
        "search": {
            "filter": "string",
            "sort": "string"
        }
    }
    """
    returned = {}
    search = {}
    keys = ["get_latest", "report_format", "search"]
    search_keys = ["filter", "sort"]
    for search_key in search_keys:
        if passed_keywords.get(search_key, None):
            search[search_key] = passed_keywords.get(search_key, None)
    if search:
        returned["search"] = search
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            # Search overrides provided filter and sort
            returned[key] = passed_keywords.get(key, None)

    return returned


def correlation_rules_template_payload(passed_keywords: dict) -> List[Dict[str, Union[str, list]]]:
    """Craft a properly formatted correlation rule export payload.

    [
    {
        "customer_id": "string",
        "templates": [
        {
            "comment": "string",
            "description": "string",
            "guardrail_notifications": [
            {
                "config": {
                "cid": "string",
                "config_id": "string",
                "plugin_id": "string",
                "recipients": [
                    "string"
                ],
                "severity": "string"
                },
                "options": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
                },
                "type": "string"
            }
            ],
            "mitre_attack": [
            {
                "tactic_id": "string",
                "technique_id": "string"
            }
            ],
            "name": "string",
            "notifications": [
            {
                "config": {
                "cid": "string",
                "config_id": "string",
                "plugin_id": "string",
                "recipients": [
                    "string"
                ],
                "severity": "string"
                },
                "options": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
                },
                "type": "string"
            }
            ],
            "operation": {
            "schedule": {
                "definition": "string"
            },
            "start_on": "2026-02-04T21:13:29.753Z",
            "stop_on": "2026-02-04T21:13:29.753Z",
            "suppression": {
                "filter": {
                "field_based": {
                    "field": "string"
                }
                },
                "suppression_period": "string"
            }
            },
            "search": {
            "case_template_id": "string",
            "execution_mode": "string",
            "filter": "string",
            "lookback": "string",
            "outcome": "string",
            "trigger_mode": "string",
            "use_ingest_time": true
            },
            "severity": 0,
            "status": "string",
            "template_id": "string",
            "trigger_on_create": true
        }
        ]
    }
    ]
    """
    returned_payload = []
    returned = {}
    keys = ["customer_id", "templates"]

    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned[key] = passed_keywords.get(key, None)

    returned_payload.append(returned)

    return returned_payload
