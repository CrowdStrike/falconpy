"""Internal payload handling library - ML Exclusions.

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


def ml_exclusions_actions_payload(passed_keywords: dict) -> dict:
    """Actions used to manipulate the content of exclusions, with ancestor fields.

    {
        "action_parameters": [
            {
            "name": "string",
            "value": "string"
            }
        ],
        "available": true,
        "description": "string",
        "group": "string",
        "label": "string",
        "name": "string"
    }
    """
    returned_payload = {}
    keys = ["action_parameters", "available", "description", "group", "label", "name"]

    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key, None)

    return returned_payload


def ml_exclusions_report_payload(passed_keywords: dict) -> dict:
    """Create a report of ML exclusions scoped by the given filters.

    {
        "report_format": "string",
        "search": {
            "filter": "string",
            "sort": "string"
        }
    }
    """
    returned_payload = {}

    keys = ["report_format", "search"]
    for key in keys:
        if passed_keywords.get(key, None):
            returned_payload[key] = passed_keywords.get(key, None)

    return returned_payload


def ml_exclusions_update_payload(passed_keywords: dict) -> dict:
    """Update the exclusions by id, with ancestor fields.

    {
        "comment": "string",
        "excluded_from": [
            "string"
        ],
        "grandparent_value": "string",
        "groups": [
            "string"
        ],
        "id": "string",
        "is_descendant_process": boolean,
        "parent_value": "string",
        "value": "string"
    }
    """
    returned_payload = {}

    keys = ["comment", "excluded_from", "grandparent_value", "groups", "id", "parent_value", "value", "is_descendant_process"]
    list_keys = ["excluded_from", "groups"]
    for key in keys:
        if passed_keywords.get(key, None):
            if key in list_keys:
                provided = passed_keywords.get(key, None)
                if isinstance(provided, str):
                    provided = provided.split(",")
                    returned_payload[key] = provided
            else:
                returned_payload[key] = passed_keywords.get(key, None)

    return returned_payload
