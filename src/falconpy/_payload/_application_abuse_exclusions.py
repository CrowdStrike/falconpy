"""Internal payload handling library - ApplicationAbuseExclusions.

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


def create_app_abuse_report_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a app_abuse_exclusions_report_v1 request.

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
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    search_keys = ["filter", "sort"]
    if "search" not in returned_payload:
        returned_payload["search"] = {}
    for key in search_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["search"][key] = passed_keywords.get(key)

    return returned_payload


def create_app_abuse_exclusion_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a app_abuse_exclusions_create_v1 request.

    {
        "exclusions": [
            "string"
        ]
    }
    """
    returned_payload = {}
    keys = ["exclusions"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def update_app_abuse_exclusions_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a app_abuse_exclusions_update_v1 request.

    {
        "exclusions": [
            "string"
        ]
    }
    """
    returned_payload = {}
    keys = ["exclusions"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload
