"""Internal payload handling library - Case Management.

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


def case_management_notification_groups_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, Union[str, int]]]]:
    """Get notification groups aggregations.
    [
        {
            "date_ranges": [
            {
                "from": "string",
                "to": "string"
            }
            ],
            "field": "string",
            "filter": "string",
            "from": 0,
            "name": "string",
            "size": 0,
            "sort": "string",
            "type": "terms"
        }
    ]
    """
    body = {}
    returned_payload = []
    date_ranges = []
    date_range = {}
    date_range_keys = ["from", "to"]
    for key in date_range_keys:
        if passed_keywords.get(key, None) is not None:
            date_range[key] = passed_keywords.get(key, None)
    date_ranges.append(date_range)
    body["date_ranges"]= date_ranges

    body_keys = ["field", "filter", "from", "name", "size", "sort", "type"]
    for key in body_keys:
        if passed_keywords.get(key, None) is not None:
            body[key] = passed_keywords.get(key, None)

    returned_payload.append(body)

    return returned_payload

def case_management_create_notification_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, Union[str, int]]]]:
    """Create notification group.
    {
        "channels": [
            {
            "config_id": "string",
            "config_name": "string",
            "recipients": [
                "string"
            ],
            "severity": "string",
            "type": "email"
            }
        ],
        "description": "string",
        "name": "string",
        "id": "string"
        }
    """
    returned_payload = {}
    channels = []
    channel = {}
    channel_keys = ["config_id", "config_name", "recipients", "severity", "type", "params"]
    for key in channel_keys:
        if passed_keywords.get(key, None) is not None:
            channel[key] = passed_keywords.get(key, None)
    channels.append(channel)
    returned_payload["channels"] = channels

    keys = ["description", "name", "id"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key, None)

    return returned_payload

def case_management_sla_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, Union[str, int]]]]:
    """Create SLA.
    {
        "description": "string",
        "goals": [
            {
            "duration_seconds": 0,
            "escalation_policy": {
                "steps": [
                {
                    "escalate_after_seconds": 0,
                    "notification_group_id": "string"
                }
                ]
            },
            "type": "string"
            }
        ],
        "name": "string"
    }
    """
    returned_payload = {}
    goals = []
    goal = {}
    goal_keys = ["duration_seconds", "type"]
    steps = []
    step = {}
    step_keys = ["escalate_after_seconds", "notification_group_id"]
    for key in step_keys:
        if passed_keywords.get(key, None) is not None:
            step[key] = passed_keywords.get(key, None)
    steps.append(step)
    goal["escalation_policy"] = steps

    for key in goal_keys:
        if passed_keywords.get(key, None) is not None:
            goal[key] = passed_keywords.get(key, None)
    goals.append(goal)
    returned_payload["goals"] = goals

    keys = ["description", "name", "id"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key, None)

    return returned_payload

def case_management_template_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, Union[str, int]]]]:
    """Generic template handler.
    {
        "description": "string",
        "fields": [
            {
            "data_type": "string",
            "default_value": "string",
            "id"
            "input_type": "string",
            "multivalued": true,
            "name": "string",
            "options": [
                {
                "id": "string"
                "value": "string"
                }
            ],
            "required": true
            }
        ],
        "id": "string"
        "name": "string",
        "sla_id": "string"
    }
    """
    returned_payload = {}

    field = {}
    field_keys = [
        "data_type", "default_value",
        "input_type", "multivalued",
        "name", "required", "id"
        ]
    for key in field_keys:
        if passed_keywords.get(key, None) is not None:
            field[key] = passed_keywords.get(key, None)

    option = {}
    option_keys = ["id", "value"]
    for key in option_keys:
        if passed_keywords.get(key, None) is not None:
            option[key] = passed_keywords.get(key, None)
    field["options"] = [option]
    returned_payload["fields"] = [field]

    keys = ["description", "name", "sla_id", "id"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key, None)

    return returned_payload
