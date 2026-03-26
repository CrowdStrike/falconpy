"""Internal payload handling library - NetworkScanNetworks.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |        FalconPy
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
from typing import Dict, Union


def network_scan_network_create_payload(passed_keywords: dict) -> Dict[str, Union[str, list]]:
    """Create a body payload for the create_networks operation.

    {
        "name": "string",
        "scanner_aids": [
            "string"
        ],
        "scanner_assignment_type": "string",
        "subnet": "string",
        "zone_id": "string"
    }
    """
    returned_payload = {}
    keys = [
        "name",
        "scanner_aids",
        "scanner_assignment_type",
        "subnet",
        "zone_id"
    ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def network_scan_network_update_payload(passed_keywords: dict) -> Dict[str, Union[str, list]]:
    """Create a body payload for the update_networks operation.

    {
        "id": "string",
        "name": "string",
        "ownership": "string",
        "scanner_aids": [
            "string"
        ],
        "scanner_assignment_type": "string",
        "zone_id": "string"
    }
    """
    returned_payload = {}
    keys = [
        "id",
        "name",
        "ownership",
        "scanner_aids",
        "scanner_assignment_type",
        "zone_id"
    ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload
