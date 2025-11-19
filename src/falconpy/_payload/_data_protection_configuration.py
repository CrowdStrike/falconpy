"""Internal payload handling library - Data Protection Configuration.

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


def data_protection_classification_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, Union[str, int, bool, list, dict]]]]:
    """Create classifications.
    {
        "resources": [
            {
            "classification_properties": {
                "content_patterns": [
                "string"
                ],
                "evidence_duplication_enabled": true,
                "file_types": [
                "string"
                ],
                "protection_mode": "monitor",
                "rules": [
                {
                    "ad_groups": [
                    "string"
                    ],
                    "ad_users": [
                    "string"
                    ],
                    "created_time_stamp": "string",
                    "description": "string",
                    "detection_severity": "informational",
                    "enable_printer_egress": true,
                    "enable_usb_devices": true,
                    "enable_web_locations": true,
                    "id": "string",
                    "modified_time_stamp": "string",
                    "notify_end_user": true,
                    "response_action": "allow",
                    "trigger_detection": true,
                    "user_scope": "all",
                    "web_locations": [
                    "string"
                    ],
                    "web_locations_scope": "all"
                }
                ],
                "sensitivity_labels": [
                "string"
                ],
                "web_sources": [
                "string"
                ]
            },
            "name": "string"
            }
        ]
    }
    """
    returned_payload = {}
    resources = []
    resource = {}

    if passed_keywords.get("name", None) is not None:
        resource["name"] = passed_keywords.get("name", None)

    classification_properties = {}

    array_fields = ["content_patterns", "file_types", "sensitivity_labels", "web_sources"]
    for field in array_fields:
        if passed_keywords.get(field, None) is not None:
            classification_properties[field] = passed_keywords.get(field, None)

    simple_fields = ["evidence_duplication_enabled", "protection_mode"]
    for field in simple_fields:
        if passed_keywords.get(field, None) is not None:
            classification_properties[field] = passed_keywords.get(field, None)

    if passed_keywords.get("rules", None) is not None:
        classification_properties["rules"] = passed_keywords.get("rules", None)
    else:
        rule = {}
        rule_array_fields = ["ad_groups", "ad_users", "web_locations"]
        for field in rule_array_fields:
            if passed_keywords.get(field, None) is not None:
                rule[field] = passed_keywords.get(field, None)

        rule_string_fields = [
            "created_time_stamp", "description", "detection_severity", "id", 
            "modified_time_stamp", "response_action", "user_scope", "web_locations_scope"
        ]
        for field in rule_string_fields:
            if passed_keywords.get(field, None) is not None:
                rule[field] = passed_keywords.get(field, None)

        rule_boolean_fields = [
            "enable_printer_egress", "enable_usb_devices", "enable_web_locations",
            "notify_end_user", "trigger_detection"
        ]
        for field in rule_boolean_fields:
            if passed_keywords.get(field, None) is not None:
                rule[field] = passed_keywords.get(field, None)

        if rule:
            classification_properties["rules"] = [rule]

    if classification_properties:
        resource["classification_properties"] = classification_properties

    if resource:
        resources.append(resource)

    if resources:
        returned_payload["resources"] = resources

    return returned_payload

def data_protection_cloud_app_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, Union[str, int, bool, list, dict]]]]:
    """Persist the given cloud application for the provided entity instance.
    {
        "description": "string",
        "name": "string",
        "urls": [
            {
            "fqdn": "string",
            "path": "string"
            }
        ]
    }
    """
    returned_payload = {}
    urls = []
    url = {}
    keys = ["description", "name"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key, None)
    url_keys = ["fqdn", "path"]
    for key in url_keys:
        if passed_keywords.get(key, None) is not None:
            url[key] = passed_keywords.get(key, None)

    urls.append(url)
    returned_payload["urls"] = urls

    return returned_payload

def data_protection_content_pattern_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, Union[str, int, bool, list, dict]]]]:
    """Persist the given content pattern for the provided entity instance.
    {
        "category": "string",
        "description": "string",
        "example": "string",
        "min_match_threshold": 0,
        "name": "string",
        "regexes": [
            "string"
        ],
        "region": "string"
    }
    """
    returned_payload = {}
    keys = ["category", "description", "example", "min_match_threshold", "name", "regexes", "region"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key, None)

    return returned_payload

def data_protection_enterprise_account_payload(
        passed_keywords: dict
        ) -> Dict[str, List[Dict[str, Union[str, int, bool, list, dict]]]]:
    """Persist the given content pattern for the provided entity instance.
    {
        "application_group_id": "string",
        "domains": [
            "string"
        ],
        "name": "string",
        "plugin_config_id": "string"
    }
    """
    returned_payload = {}
    keys = ["application_group_id", "domains", "name", "plugin_config_id"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key, None)

    return returned_payload


def data_protection_sensitivity_label_payload(
        passed_keywords: dict
        ) -> Dict[str, List[Dict[str, Union[str, int, bool, list, dict]]]]:
    """Create new sensitivity label (V2)
    {
        "co_authoring": true,
        "display_name": "string",
        "external_id": "string",
        "label_provider": "string",
        "name": "string",
        "plugins_configuration_id": "string",
        "synced": true
    }
    """
    returned_payload = {}
    keys = ["co_authoring", "display_name", 
            "external_id", "label_provider", 
            "name", "plugins_configuration_id", 
            "synced"
            ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key, None)

    return returned_payload

def data_protection_policy_payload(passed_keywords: dict) -> Dict[str, List[Dict[str, Union[str, int, bool, list, dict]]]]:
    """Create data protection policies.
    {
        "resources": [
            {
            "description": "string",
            "name": "string",
            "policy_properties": {
                "allow_notifications": "default",
                "be_exclude_domains": "string",
                "be_paste_clipboard_max_size": 0,
                "be_paste_clipboard_max_size_unit": "Bytes",
                "be_paste_clipboard_min_size": 0,
                "be_paste_clipboard_min_size_unit": "Bytes",
                "be_paste_clipboard_over_size_behaviour_block": true,
                "be_paste_timeout_duration_milliseconds": 0,
                "be_paste_timeout_response": "block",
                "be_splash_custom_message": "string",
                "be_splash_enabled": true,
                "be_splash_message_source": "default",
                "be_upload_timeout_duration_seconds": 0,
                "be_upload_timeout_response": "block",
                "block_all_data_access": true,
                "block_notifications": "default",
                "browsers_without_active_extension": "allow",
                "classifications": [
                "string"
                ],
                "custom_allow_notification": "string",
                "custom_block_notification": "string",
                "enable_clipboard_inspection": true,
                "enable_content_inspection": true,
                "enable_context_inspection": true,
                "enable_end_user_notifications_unsupported_browser": true,
                "enable_network_inspection": true,
                "euj_dialog_box_logo": "string",
                "euj_dialog_timeout": 0,
                "euj_dropdown_options": {
                "justifications": [
                    {
                    "default": true,
                    "id": "string",
                    "justification": "string",
                    "selected": true
                    }
                ]
                },
                "euj_header_text": {
                    "headers": [
                        {
                        "default": true,
                        "header": "string",
                        "selected": true
                        }
                    ]
                },
                "euj_require_additional_details": true,
                "euj_response_cache_timeout": 0,
                "evidence_download_enabled": true,
                "evidence_duplication_enabled_default": true,
                "evidence_encrypted_enabled": true,
                "evidence_storage_free_disk_perc": 0,
                "evidence_storage_max_size": 0,
                "inspection_depth": "balanced",
                "max_file_size_to_inspect": 0,
                "max_file_size_to_inspect_unit": "Bytes",
                "min_confidence_level": "low",
                "network_inspection_files_exceeding_size_limit": "block",
                "similarity_detection": true,
                "similarity_threshold": "10",
                "unsupported_browsers_action": "allow"
            },
            "precedence": 0
            }
        ]
    }
    """
    returned_payload = {}

    if passed_keywords.get("resources", None) is not None:
        returned_payload["resources"] = passed_keywords.get("resources", None)
        return returned_payload

    resources = []
    resource = {}

    resource_fields = ["description", "name", "precedence"]
    for field in resource_fields:
        if passed_keywords.get(field, None) is not None:
            resource[field] = passed_keywords.get(field, None)

    policy_properties = {}

    string_fields = [
        "allow_notifications", "be_exclude_domains", "be_paste_clipboard_max_size_unit",
        "be_paste_clipboard_min_size_unit", "be_paste_timeout_response", "be_splash_custom_message",
        "be_splash_message_source", "be_upload_timeout_response", "block_notifications",
        "browsers_without_active_extension", "custom_allow_notification", "custom_block_notification",
        "euj_dialog_box_logo", "inspection_depth", "max_file_size_to_inspect_unit",
        "min_confidence_level", "network_inspection_files_exceeding_size_limit",
        "similarity_threshold", "unsupported_browsers_action"
    ]
    for field in string_fields:
        if passed_keywords.get(field, None) is not None:
            policy_properties[field] = passed_keywords.get(field, None)

    integer_fields = [
        "be_paste_clipboard_max_size", "be_paste_clipboard_min_size", "be_paste_timeout_duration_milliseconds",
        "be_upload_timeout_duration_seconds", "euj_dialog_timeout", "euj_response_cache_timeout",
        "evidence_storage_free_disk_perc", "evidence_storage_max_size", "max_file_size_to_inspect"
    ]
    for field in integer_fields:
        if passed_keywords.get(field, None) is not None:
            policy_properties[field] = passed_keywords.get(field, None)

    boolean_fields = [
        "be_paste_clipboard_over_size_behaviour_block", "be_splash_enabled", "block_all_data_access",
        "enable_clipboard_inspection", "enable_content_inspection", "enable_context_inspection",
        "enable_end_user_notifications_unsupported_browser", "enable_network_inspection",
        "euj_require_additional_details", "evidence_download_enabled", "evidence_duplication_enabled_default",
        "evidence_encrypted_enabled", "similarity_detection"
    ]
    for field in boolean_fields:
        if passed_keywords.get(field, None) is not None:
            policy_properties[field] = passed_keywords.get(field, None)

    if passed_keywords.get("classifications", None) is not None:
        policy_properties["classifications"] = passed_keywords.get("classifications", None)

    if passed_keywords.get("euj_dropdown_options", None) is not None:
        policy_properties["euj_dropdown_options"] = passed_keywords.get("euj_dropdown_options", None)
    elif any(passed_keywords.get(key, None) is not None for key in ["justifications"]):
        euj_dropdown = {}
        if passed_keywords.get("justifications", None) is not None:
            euj_dropdown["justifications"] = passed_keywords.get("justifications", None)
        if euj_dropdown:
            policy_properties["euj_dropdown_options"] = euj_dropdown

    if passed_keywords.get("euj_header_text", None) is not None:
        policy_properties["euj_header_text"] = passed_keywords.get("euj_header_text", None)
    elif passed_keywords.get("headers", None) is not None:
        policy_properties["euj_header_text"] = {"headers": passed_keywords.get("headers", None)}

    if policy_properties:
        resource["policy_properties"] = policy_properties

    if resource:
        resources.append(resource)

    if resources:
        returned_payload["resources"] = resources

    return returned_payload

def data_protection_web_locations_payload(
        passed_keywords: dict
        ) -> Dict[str, List[Dict[str, Union[str, int, bool, list, dict]]]]:
    """Persist the given web-locations.
    {
    "web_locations": [
        {
            "application_id": "string",
            "cid": "string",
            "created": "2025-11-12T00:48:40.309Z",
            "deleted": true,
            "enterprise_account_id": "string",
            "id": "string",
            "last_updated": "2025-11-12T00:48:40.309Z",
            "location_type": "string",
            "name": "string",
            "provider_location_id": "string",
            "provider_location_name": "string",
            "type": "string"
        }
    ]
    }
    """
    returned_payload = {}
    web_locations = []
    web_location = {}
    keys = ["application_id", "cid", "created",
            "deleted", "enterprise_account_id", "id",
            "last_updated", "location_type", "name",
            "provider_location_id", "provider_location_name", "type"
            ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            web_location[key] = passed_keywords.get(key, None)
    web_locations.append(web_location)
    returned_payload["web_locations"] = web_locations

    return returned_payload
