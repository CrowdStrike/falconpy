"""Internal payload handling library - IOA Payloads

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


def ioa_exclusion_payload(passed_keywords: dict) -> dict:
    """Creates a properly formatted exclusion payload
       {
            "cl_regex": "string",
            "comment": "string",
            "description": "string",
            "detection_json": "string",
            "groups": [
                "string"
            ],
            "ifn_regex": "string",
            "name": "string",
            "pattern_id": "string",
            "pattern_name": "string"
        }
    """
    returned_payload = {}
    if passed_keywords.get("comment", None):
        returned_payload["comment"] = passed_keywords.get("comment", None)
    if passed_keywords.get("groups", None):
        returned_payload["groups"] = passed_keywords.get("groups", None)
    if passed_keywords.get("cl_regex", None):
        returned_payload["cl_regex"] = passed_keywords.get("cl_regex", None)
    if passed_keywords.get("description", None):
        returned_payload["description"] = passed_keywords.get("description", None)
    if passed_keywords.get("detection_json", None):
        returned_payload["detection_json"] = passed_keywords.get("detection_json", None)
    if passed_keywords.get("groups", None):
        returned_payload["groups"] = passed_keywords.get("groups", None)
    if passed_keywords.get("ifn_regex", None):
        returned_payload["ifn_regex"] = passed_keywords.get("ifn_regex", None)
    if passed_keywords.get("name", None):
        returned_payload["name"] = passed_keywords.get("name", None)
    if passed_keywords.get("pattern_id", None):
        returned_payload["pattern_id"] = passed_keywords.get("pattern_id", None)
    if passed_keywords.get("pattern_name", None):
        returned_payload["pattern_name"] = passed_keywords.get("pattern_name", None)

    return returned_payload
