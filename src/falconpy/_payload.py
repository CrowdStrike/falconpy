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


def create_generic_payload_list(submitted_keywords: dict,
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


def create_aggregate_payload(submitted_keywords: dict) -> dict:  # pylint: disable=R0912
    """Creates the standardized BODY payload necessary for using the
    GetScansAggregates (get_scans_aggregates) and GetAggregateDetects
    (get_aggregate_detects) operations.

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


def create_update_detects_payload(current_payload: dict, passed_keywords: dict) -> dict:
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
