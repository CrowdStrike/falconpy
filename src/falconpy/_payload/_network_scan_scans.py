"""Internal payload handling library - NetworkScanScans.

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


def network_scan_scan_create_payload(passed_keywords: dict) -> Dict[str, Union[str, bool, dict]]:
    """Create a body payload for the create_scans operation.

    {
        "block_windows": {
            "intervals": [
                {
                    "end_time": "string",
                    "start_time": "string"
                }
            ],
            "timezone": "string"
        },
        "credentialed": boolean,
        "credentials": {
            "auto_authorize_scanners": boolean,
            "ids": [
                "string"
            ]
        },
        "description": "string",
        "fragile_device_detection": boolean,
        "name": "string",
        "scheduling": {
            "days_of_month": [
                integer
            ],
            "days_of_week": [
                integer
            ],
            "end_date": "string",
            "frequency": "string",
            "occurrence": "string",
            "start_date": "string",
            "start_time": "string",
            "timeout_seconds": integer,
            "timezone": "string"
        },
        "target_asset": {
            "ids": [
                "string"
            ]
        },
        "target_asset_filter": {
            "fql_filter": "string"
        },
        "target_external_ip": {
            "ip_specs": [
                "string"
            ]
        },
        "target_ip": {
            "ip_specs": [
                "string"
            ],
            "zone_id": "string"
        },
        "target_type": "string",
        "template_id": "string"
    }
    """
    returned_payload = {}
    keys = [
        "block_windows",
        "credentialed",
        "credentials",
        "description",
        "fragile_device_detection",
        "name",
        "scheduling",
        "target_asset",
        "target_asset_filter",
        "target_external_ip",
        "target_ip",
        "target_type",
        "template_id"
    ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def network_scan_scan_update_payload(passed_keywords: dict) -> Dict[str, Union[str, bool, dict]]:
    """Create a body payload for the update_scans operation.

    {
        "block_windows": {
            "intervals": [
                {
                    "end_time": "string",
                    "start_time": "string"
                }
            ],
            "timezone": "string"
        },
        "credentialed": boolean,
        "credentials": {
            "auto_authorize_scanners": boolean,
            "ids": [
                "string"
            ]
        },
        "description": "string",
        "fragile_device_detection": boolean,
        "id": "string",
        "name": "string",
        "scheduling": {
            "days_of_month": [
                integer
            ],
            "days_of_week": [
                integer
            ],
            "end_date": "string",
            "frequency": "string",
            "occurrence": "string",
            "start_date": "string",
            "start_time": "string",
            "timeout_seconds": integer,
            "timezone": "string"
        },
        "target_asset": {
            "ids": [
                "string"
            ]
        },
        "target_asset_filter": {
            "fql_filter": "string"
        },
        "target_external_ip": {
            "ip_specs": [
                "string"
            ]
        },
        "target_ip": {
            "ip_specs": [
                "string"
            ],
            "zone_id": "string"
        },
        "target_type": "string",
        "template_id": "string"
    }
    """
    returned_payload = {}
    keys = [
        "block_windows",
        "credentialed",
        "credentials",
        "description",
        "fragile_device_detection",
        "id",
        "name",
        "scheduling",
        "target_asset",
        "target_asset_filter",
        "target_external_ip",
        "target_ip",
        "target_type",
        "template_id"
    ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload
