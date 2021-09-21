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


def create_quick_scan_aggregate_payload(submitted_keywords: dict) -> dict:
    """Creates the standardized BODY payload necessary for using the
    GetScansAggregates operation (get_scans_aggregates).

    Creates the following payload, no parameters are required:
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
    date_ranges = submitted_keywords.get("date_ranges", None)
    if date_ranges:
        returned_payload["date_ranges"] = date_ranges
    field = submitted_keywords.get("field", None)
    if field:
        returned_payload["field"] = field
    filter = submitted_keywords.get("filter", None)
    if filter:
        returned_payload["filter"] = filter
    interval = submitted_keywords.get("interval", None)
    if interval:
        returned_payload["interval"] = interval
    min_doc_count = submitted_keywords.get("min_doc_count", -1)
    if min_doc_count >= 0:
        returned_payload["min_doc_count"] = min_doc_count
    missing = submitted_keywords.get("missing", None)
    if missing:
        returned_payload["missing"] = missing
    name = submitted_keywords.get("name", None)
    if name:
        returned_payload["name"] = name
    qstring = submitted_keywords.get("q", None)
    if qstring:
        returned_payload["q"] = qstring
    ranges = submitted_keywords.get("ranges", None)
    if ranges:
        returned_payload["ranges"] = ranges
    size = submitted_keywords.get("size", None)
    if size:
        returned_payload["size"] = size
    sort = submitted_keywords.get("sort", None)
    if sort:
        returned_payload["sort"] = sort
    sub_aggregates = submitted_keywords.get("sub_aggregates", None)
    if sub_aggregates:
        returned_payload["sub_aggregates"] = sub_aggregates
    time_zone = submitted_keywords.get("time_zone", None)
    if time_zone:
        returned_payload["time_zone"] = time_zone
    type_ = submitted_keywords.get("type", None)
    if type_:
        returned_payload["type"] = type_

    return returned_payload
