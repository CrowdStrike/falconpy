"""Internal payload handling library - NetworkScanScanRuns.

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
from typing import Dict, Union


def scan_run_create_payload(passed_keywords: dict) -> Dict[str, Union[str, dict]]:
    """Create a body payload for the create_scan_runs operation.

    {
        "config": {
            "additional_tcp_ports": ["string"],
            "additional_udp_ports": ["string"],
            "auto_include_new_detections": boolean,
            "detections": ["string"],
            "fragile_device_detection": boolean,
            "ignore_tcp_resets": boolean,
            "ports_scan_level": "string",
            "scan_exclusion": {
                "cidrs": [
                    {
                        "active": boolean,
                        "value": "string"
                    }
                ],
                "host_groups": ["string"],
                "hosts": ["string"],
                "ip_ranges": [
                    {
                        "active": boolean,
                        "from": "string",
                        "to": "string"
                    }
                ],
                "ips": [
                    {
                        "active": boolean,
                        "value": "string"
                    }
                ]
            },
            "scan_intensity": "string",
            "target_asset": {
                "ids": ["string"]
            },
            "target_asset_filter": {
                "fql_filter": "string"
            },
            "target_asset_vuln": {
                "asset_ids": ["string"],
                "cve_ids": ["string"]
            },
            "target_external_ip": {
                "ip_specs": ["string"]
            },
            "target_ip": {
                "ip_specs": ["string"],
                "zone_id": "string"
            },
            "target_type": "string",
            "type": "string"
        },
        "scan_id": "string"
    }
    """
    returned_payload = {}
    keys = ["config", "scan_id"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def scan_run_update_payload(passed_keywords: dict) -> Dict[str, str]:
    """Create a body payload for the update_scan_runs operation.

    {
        "action": "string",
        "id": "string"
    }
    """
    returned_payload = {}
    keys = ["action", "id"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload
