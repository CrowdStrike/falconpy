"""Internal payload handling library - Intel.

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


def cao_incidents_aggregates_v1_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a cao_incidents_aggregates_v1 request.

    {
        "date_ranges": [
            "string"
        ],
        "exclude": "string",
        "extended_bounds": {
            "max": "string",
            "min": "string"
        },
        "field": "string",
        "filter": "string",
        "filters_spec": {
            "filters": "string",
            "other_bucket": true,
            "other_bucket_key": "string"
        },
        "from": 0,
        "include": "string",
        "interval": "string",
        "max_doc_count": 0,
        "min_doc_count": 0,
        "missing": "string",
        "name": "string",
        "percents": [
            "string"
        ],
        "q": "string",
        "ranges": [
            "string"
        ],
        "size": 0,
        "sort": "string",
        "sub_aggregates": [
            "string"
        ],
        "time_zone": "string",
        "type": "string"
    }
    """
    returned_payload = {}
    keys = [
        "date_ranges",
        "exclude",
        "extended_bounds",
        "field",
        "filter",
        "filters_spec",
        "from",
        "include",
        "interval",
        "max_doc_count",
        "min_doc_count",
        "missing",
        "name",
        "percents",
        "q",
        "ranges",
        "size",
        "sort",
        "sub_aggregates",
        "time_zone",
        "type"
    ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    extended_bounds_keys = ["max", "min"]
    if "extended_bounds" not in returned_payload:
        returned_payload["extended_bounds"] = {}
    for key in extended_bounds_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["extended_bounds"][key] = passed_keywords.get(key)

    filters_spec_keys = ["filters", "other_bucket", "other_bucket_key"]
    if "filters_spec" not in returned_payload:
        returned_payload["filters_spec"] = {}
    for key in filters_spec_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["filters_spec"][key] = passed_keywords.get(key)

    return returned_payload


def cao_incidents_entities_v1_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a cao_incidents_entities_v1 request.

    {
        "ids": [
            "string"
        ]
    }
    """
    returned_payload = {}
    keys = ["ids"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload
