"""Internal payload handling library

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


def generic_payload_list(submitted_keywords: dict,
                         payload_value: str,
                         submitted_arguments: list = None
                         ) -> dict:
    """Creates a standardized BODY payload based upon the
    requested payload value and passed keywords.

    Resulting payload provides passed keywords values in list format.

    Creates the following payload:
    {
      "payload_value": [
        "keyword provided values"
      ]
    }
    """
    returned_payload = {}
    submitted_values = submitted_keywords.get(payload_value, None)
    if submitted_values:
        if not isinstance(submitted_values, list):
            submitted_values = submitted_values.split(",")
        returned_payload[payload_value] = submitted_values
    else:
        if submitted_arguments:
            if isinstance(submitted_arguments[0], dict):
                # They're passing us a full payload
                returned_payload = submitted_arguments[0]
            else:
                # They're just passing us values
                submitted_values = submitted_arguments[0]
                if not isinstance(submitted_values, list):
                    submitted_values = submitted_values.split(",")
                returned_payload[payload_value] = submitted_values

    return returned_payload


def aggregate_payload(submitted_keywords: dict) -> dict:  # pylint: disable=R0912
    """Creates the standardized BODY payload necessary for aggregate operations.

    Creates the following payload, no parameters shown below are required:
    {
        "date_ranges": [
            {
                "from": "string",
                "to": "string"
            }
        ],
        "field": "string",
        "filter": "string",
        "interval": "string",
        "min_doc_count": 0,
        "missing": "string",
        "name": "string",
        "q": "string",
        "ranges": [
            {
                "From": 0,
                "To": 0
            }
        ],
        "size": 0,
        "sort": "string",
        "sub_aggregates": [
            null
        ],
        "time_zone": "string",
        "type": "string"
    }
    """
    returned_payload = {}

    if submitted_keywords.get("date_ranges", None):
        returned_payload["date_ranges"] = submitted_keywords.get("date_ranges", None)

    if submitted_keywords.get("field", None):
        returned_payload["field"] = submitted_keywords.get("field", None)

    if submitted_keywords.get("filter", None):
        returned_payload["filter"] = submitted_keywords.get("filter", None)

    if submitted_keywords.get("interval", None):
        returned_payload["interval"] = submitted_keywords.get("interval", None)

    if submitted_keywords.get("min_doc_count", -1) >= 0:
        returned_payload["min_doc_count"] = submitted_keywords.get("min_doc_count", -1)

    if submitted_keywords.get("missing", None):
        returned_payload["missing"] = submitted_keywords.get("missing", None)

    if submitted_keywords.get("name", None):
        returned_payload["name"] = submitted_keywords.get("name", None)

    if submitted_keywords.get("q", None):
        returned_payload["q"] = submitted_keywords.get("q", None)

    if submitted_keywords.get("ranges", None):
        returned_payload["ranges"] = submitted_keywords.get("ranges", None)

    if submitted_keywords.get("size", None):
        returned_payload["size"] = submitted_keywords.get("size", None)

    if submitted_keywords.get("sort", None):
        returned_payload["sort"] = submitted_keywords.get("sort", None)

    if submitted_keywords.get("sub_aggregates", None):
        returned_payload["sub_aggregates"] = submitted_keywords.get("sub_aggregates", None)

    if submitted_keywords.get("time_zone", None):
        returned_payload["time_zone"] = submitted_keywords.get("time_zone", None)

    if submitted_keywords.get("type", None):
        returned_payload["type"] = submitted_keywords.get("type", None)

    return returned_payload


def update_detects_payload(current_payload: dict, passed_keywords: dict) -> dict:
    """Updates the provided payload with any viable parameters provided as keywords."""
    if passed_keywords.get("assigned_to_uuid", None):
        current_payload["assigned_to_uuid"] = passed_keywords.get("assigned_to_uuid", None)
    if passed_keywords.get("show_in_ui", None):
        current_payload["show_in_ui"] = passed_keywords.get("show_in_ui", None)
    if passed_keywords.get("status", None):
        current_payload["status"] = passed_keywords.get("status", None)
    if passed_keywords.get("comment", None):
        current_payload["comment"] = passed_keywords.get("comment", None)

    return current_payload


def handle_recon_rule_params(inbound: dict) -> dict:
    """Handles the payload formatting for a single rule object"""
    returned_dict = {}
    if inbound.get("filter", None):
        returned_dict["filter"] = inbound.get("filter", None)
    if inbound.get("id", None):
        returned_dict["id"] = inbound.get("id", None)
    if inbound.get("name", None):
        returned_dict["name"] = inbound.get("name", None)
    if inbound.get("permissions", None):
        returned_dict["permissions"] = inbound.get("permissions", None)
    if inbound.get("priority", None):
        returned_dict["priority"] = inbound.get("priority", None)

    return returned_dict


def recon_rules_payload(passed_keywords: dict) -> dict:
    """Creates a properly formatted payload for recon rule handling.
    Creates a list of dictionaries.
            [
                {
                    "filter": "string",
                    "id": "string",
                    "name": "string",
                    "permissions": "string",
                    "priority": "string"
                }
            ]
    """
    returned_rules = []
    provided_rules = passed_keywords.get("rules", None)
    if provided_rules:
        # Not entirely sure why you wouldn't just pass the body
        if isinstance(provided_rules, list):
            for rule in passed_keywords.get("rules", None):
                returned_rules.append(handle_recon_rule_params(rule))
        else:
            # Fall back to a single rule
            returned_rules.append(handle_recon_rule_params(passed_keywords))
    else:
        # Only one rule was provided, use the keywords
        returned_rules.append(handle_recon_rule_params(passed_keywords))

    return returned_rules


def recon_notifications_payload(passed_keywords: dict) -> dict:
    """Creates a properly formatted payload for a recon notification
    payload. Generates a list of dictionaries, but is designed to handle
    just one notification. (For multiple notifications use the body
    payload keyword.)
    [
        {
            "assigned_to_uuid": "string",
            "id": "string",
            "status": "string"
        }
    ]
    """
    returned_payload = []
    notification = {}
    if passed_keywords.get("assigned_to_uuid", None):
        notification["assigned_to_uuid"] = passed_keywords.get("assigned_to_uuid", None)
    if passed_keywords.get("id", None):
        notification["id"] = passed_keywords.get("id", None)
    if passed_keywords.get("status", None):
        notification["status"] = passed_keywords.get("status", None)

    returned_payload.append(notification)

    return returned_payload


def recon_action_update_payload(passed_keywords: dict) -> dict:
    """Creates a properly formatted payload for handling recon actions.
    {
        "frequency": "string",
        "id": "string",
        "recipients": [
            "string"
        ],
        "status": "string"
    }
    """
    returned_payload = {}
    if passed_keywords.get("frequency", None):
        returned_payload["frequency"] = passed_keywords.get("frequency", None)
    if passed_keywords.get("id", None):
        returned_payload["id"] = passed_keywords.get("id", None)
    if passed_keywords.get("recipients", None):
        returned_payload["recipients"] = passed_keywords.get("recipients", None)
    if passed_keywords.get("status", None):
        returned_payload["status"] = passed_keywords.get("status", None)

    return returned_payload


def recon_action_payload(passed_keywords: dict) -> dict:
    """Creates a properly formatted payload for attaching recon
    actions to a monitoring rule.
    {
        "actions": [
            {
                "frequency": "string",
                "recipients": [
                    "string"
                ],
                "type": "string"
            }
        ],
        "rule_id": "string"
    }
    """
    returned_payload = {}
    returned_payload["rule_id"] = passed_keywords.get("rule_id", None)
    if passed_keywords.get("actions", None):
        returned_payload["actions"] = passed_keywords.get("actions", None)
    else:
        action = {}
        if passed_keywords.get("frequency", None):
            action["frequency"] = passed_keywords.get("frequency", None)
        if passed_keywords.get("recipients", None):
            action["recipients"] = passed_keywords.get("recipients", None)
        if passed_keywords.get("type", None):
            action["type"] = passed_keywords.get("type", None)
        returned_payload["actions"] = []
        returned_payload["actions"].append(action)

    return returned_payload


def recon_rule_preview_payload(passed_keywords: dict) -> dict:
    """Creates a properly formatted payload for retrieving
    a rule preview from recon.
    {
        "filter": "string",
        "topic": "string"
    }
    """
    returned_payload = {}
    if passed_keywords.get("filter", None):
        returned_payload["filter"] = passed_keywords.get("filter", None)
    if passed_keywords.get("topic", None):
        returned_payload["topic"] = passed_keywords.get("topic", None)

    return returned_payload


def malquery_fuzzy_payload(passed_keywords: dict) -> dict:
    """Generates a properly formatted MalQuery fuzzy search payload
    {
        "options": {
            "filter_meta": [
                "string"
            ],
            "limit": 0
        },
        "patterns": [
            {
            "type": "string",
            "value": "string"
            }
        ]
    }
    """
    returned_payload = {}
    filters = passed_keywords.get("filter_meta", None)
    limit = passed_keywords.get("limit", None)
    if filters or limit:
        returned_payload["options"] = {}
    if filters:
        returned_payload["options"]["filter_meta"] = filters
    if limit:
        returned_payload["options"]["limit"] = limit
    patterns = passed_keywords.get("patterns", None)
    if patterns:
        returned_payload["patterns"] = patterns

    return returned_payload


def handle_malquery_search_params(passed_params: dict) -> dict:
    """Creates the base payload used by exact_search and hunt"""
    returned_base = {}
    filters = passed_params.get("filter_filetypes", None)
    filter_meta = passed_params.get("filter_meta", None)
    limit = passed_params.get("limit", None)
    max_date = passed_params.get("max_date", None)
    max_size = passed_params.get("max_size", None)
    min_date = passed_params.get("min_date", None)
    min_size = passed_params.get("min_size", None)
    if filters or filter_meta or limit or max_date or max_size or min_date or min_size:
        returned_base["options"] = {}
    if filters:
        returned_base["options"]["filter_filetypes"] = filters
    if filter_meta:
        returned_base["options"]["filter_meta"] = filter_meta
    if limit:
        returned_base["options"]["limit"] = limit
    if max_date:
        returned_base["options"]["max_date"] = max_date
    if min_date:
        returned_base["options"]["min_date"] = min_date
    if max_size:
        returned_base["options"]["max_size"] = max_size
    if min_size:
        returned_base["options"]["min_size"] = min_size

    return returned_base


def malquery_exact_search_payload(passed_keywords: dict) -> dict:
    """Creates a properly formatted payload for performing
    a MalQuery exact search request
    {
    "options": {
        "filter_filetypes": [
            "string"
        ],
        "filter_meta": [
            "string"
        ],
        "limit": 0,
        "max_date": "string",
        "max_size": "string",
        "min_date": "string",
        "min_size": "string"
    },
    "patterns": [
        {
        "type": "string",
        "value": "string"
        }
    ]
    }
    """
    returned_payload = handle_malquery_search_params(passed_params=passed_keywords)
    if passed_keywords.get("patterns", None):
        returned_payload["patterns"] = passed_keywords.get("patterns", None)

    return returned_payload


def malquery_hunt_payload(passed_keywords: dict) -> dict:
    """Creates a properly formatted payload for performing
    a MalQuery hunt request.

    {
        "options": {
            "filter_filetypes": [
                "string"
            ],
            "filter_meta": [
                "string"
            ],
            "limit": 0,
            "max_date": "string",
            "max_size": "string",
            "min_date": "string",
            "min_size": "string"
        },
        "yara_rule": "string"
    }
    """
    returned_payload = handle_malquery_search_params(passed_params=passed_keywords)
    if passed_keywords.get("yara_rule", None):
        returned_payload["yara_rule"] = passed_keywords.get("yara_rule", None)

    return returned_payload


def exclusion_payload(passed_keywords: dict) -> dict:
    """Creates a properly formatted exclusion payload
        {
            "comment": "string",
            "groups": [
                "string"
            ],
            "value": "string"
        }
    """
    returned_payload = {}
    if passed_keywords.get("comment", None):
        returned_payload["comment"] = passed_keywords.get("comment", None)
    if passed_keywords.get("groups", None):
        returned_payload["groups"] = passed_keywords.get("groups", None)
    if passed_keywords.get("value", None):
        returned_payload["value"] = passed_keywords.get("value", None)

    return returned_payload
