"""Internal payload handling library - NGSIEM.

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
from typing import Dict, List, Union


def ngsiem_search_payload(passed_keywords: dict) -> Dict[str, Union[str, bool, int, dict]]:
    """Generate a properly formatted NGSIEM search payload.

    {
        "allowEventSkipping": boolean,
        "arguments": {},
        "around": {
            "eventId": "string",
            "numberOfEventsAfter": integer,
            "numberOfEventsBefore": integer,
            "timestamp": integer
        },
        "autobucketCount": integer,
        "end": "string",
        "ingestEnd": "string",
        "ingestStart": "string",
        "isLive": boolean,
        "queryString": "string",
        "start": "string",
        "timeZone": "string",
        "timeZoneOffsetMinutes": integer,
        "useIngestTime": boolean
    }
    """
    key_map = {
        "allow_event_skipping": "allowEventSkipping",
        "autobucket_count": "autobucketCount",
        "ingest_end": "ingestEnd",
        "ingest_start": "ingestStart",
        "is_live": "isLive",
        "query_string": "queryString",
        "timezone": "timeZone",
        "timezone_offset_minutes": "timeZoneOffsetMinutes",
        "use_ingest_time": "useIngestTime"
    }
    returned: dict = {}
    bool_int_keys = ["allow_event_skipping", "is_live", "use_ingest_time", "autobucket_count",
                     "timezone_offset_minutes"
                     ]
    keys = ["arguments", "around", "end", "ingest_end", "ingest_start", "query_string", "start",
            "timezone"
            ]
    for key in keys:
        if passed_keywords.get(key, None):
            keystr = key_map[key] if key in key_map else key
            returned[keystr] = passed_keywords.get(key, None)
    for key in bool_int_keys:
        if passed_keywords.get(key, None) is not None:
            keystr = key_map[key] if key in key_map else key
            returned[keystr] = passed_keywords.get(key, None)

    return returned


def ngsiem_parser_payload(passed_keywords: dict) -> Dict[str, Union[str, list]]:
    """Craft a properly formatted parser payload.

    {
        "fields_to_be_removed_before_parsing": [
            "string"
        ],
        "fields_to_tag": [
            "string"
        ],
        "name": "string",
        "id": "string",
        "repository": "string",
        "script": "string",
        "test_cases": [
            {
                "event": {
                    "raw_string": "string"
                },
                "output_assertions": [
                    {
                        "assertions": {
                            "fields_have_values": [
                                {
                                    "expected_value": "string",
                                    "field_name": "string"
                                }
                            ],
                            "fields_not_present": [
                                "string"
                            ]
                        },
                        "output_event_index": 0
                    }
                ]
            }
        ]
    }
    """
    returned: dict = {}
    keys = ["fields_to_be_removed_before_parsing", "fields_to_tag", "name", "repository", "script",
            "test_cases", "id"
            ]
    list_keys = ["fields_to_be_removed_before_parsing", "fields_to_tag"]
    for key in keys:
        if passed_keywords.get(key, None):
            keyval = passed_keywords.get(key, None)
            if key in list_keys and isinstance(keyval, str):
                keyval = keyval.split(",")
            returned[key] = keyval

    return returned


def ngsiem_auto_update_policy_payload(passed_keywords: dict) -> Dict[str, str]:
    """Create a properly formatted parser auto update policy payload.

    {
        "autoupdate_policy": "string",
        "reason": "string"
    }
    """
    returned: dict = {}
    keys = ["autoupdate_policy", "reason"]
    for key in keys:
        if passed_keywords.get(key, None):
            returned[key] = passed_keywords.get(key, None)

    return returned


def ngsiem_install_parser_payload(passed_keywords: dict) -> Dict[str, str]:
    """Create a properly formatted install parser payload.

    {
        "parser_id": "string",
        "version": "string"
    }
    """
    returned: dict = {}
    keys = ["parser_id", "version"]
    for key in keys:
        if passed_keywords.get(key, None):
            returned[key] = passed_keywords.get(key, None)

    return returned


def ngsiem_bulk_install_parsers_payload(passed_keywords: dict) -> Dict[str, List[dict]]:
    """Create a properly formatted bulk install parsers payload.

    {
        "parsers": [
            {
                "parser_id": "string",
                "version": "string"
            }
        ]
    }
    """
    returned: dict = {}
    if passed_keywords.get("parsers", None) is not None:
        returned["parsers"] = passed_keywords["parsers"]

    return returned


def ngsiem_connector_config_payload(passed_keywords: dict) -> Dict[str, Union[str, dict]]:
    """Create a properly formatted connector config payload.

    {
        "config": {
            "auth": {},
            "name": "string",
            "params": {}
        },
        "connector_id": "string"
    }
    """
    returned: dict = {}
    keys = ["config", "connector_id"]
    for key in keys:
        if passed_keywords.get(key, None):
            returned[key] = passed_keywords.get(key, None)

    return returned


def ngsiem_data_connection_payload(passed_keywords: dict) -> Dict[str, Union[str, bool, dict, list]]:
    """Create data connection payload.

    {
        "config": {
            "auth": {},
            "name": "string",
            "params": {}
        },
        "config_id": "string",
        "connector_id": "string",
        "connector_type": "string",
        "description": "string",
        "enable_host_enrichment": true,
        "enable_user_enrichment": true,
        "log_sources": [
            "string"
        ],
        "name": "string",
        "parser": "string",
        "vendor_name": "string",
        "vendor_product_name": "string"
    }
    """
    returned: dict = {}
    keys = ["config", "config_id", "connector_id", "connector_type", "description",
            "enable_host_enrichment", "enable_user_enrichment", "log_sources", "name",
            "parser", "vendor_name", "vendor_product_name"
            ]
    list_keys = ["log_sources"]
    for key in keys:
        if passed_keywords.get(key, None):
            keyval = passed_keywords.get(key, None)
            if key in list_keys and isinstance(keyval, str):
                keyval = keyval.split(",")
            returned[key] = keyval

    return returned
