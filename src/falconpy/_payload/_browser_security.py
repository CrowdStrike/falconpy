"""Internal payload handling library - BrowserSecurity.

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


def query_combined_seraphic_agents_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a CombinedQueryAgents request.

    {
        "filter": {
            "application": [
                "string"
            ],
            "application_name": [
                "string"
            ],
            "application_version": [
                "string"
            ],
            "browser_name": [
                "string"
            ],
            "browser_version": [
                "string"
            ],
            "deployment_method": [
                "string"
            ],
            "email": [
                "string"
            ],
            "first_seen": {
                "end": "string",
                "start": "string"
            },
            "host_id": [
                "string"
            ],
            "hostname": [
                "string"
            ],
            "id": [
                "string"
            ],
            "last_seen": {
                "end": "string",
                "start": "string"
            },
            "os_name": [
                "string"
            ],
            "platform": [
                "string"
            ],
            "policy_updated": [
                "string"
            ],
            "protection_type": [
                "string"
            ],
            "status": [
                "string"
            ],
            "username": [
                "string"
            ]
        },
        "limit": 0,
        "search": "string",
        "skip": 0,
        "sort": [
            "string"
        ]
    }
    """
    returned_payload = {}
    keys = ["filter", "limit", "search", "skip", "sort"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    filter_keys = [
        "application",
        "application_name",
        "application_version",
        "browser_name",
        "browser_version",
        "deployment_method",
        "email",
        "first_seen",
        "host_id",
        "hostname",
        "id",
        "last_seen",
        "os_name",
        "platform",
        "policy_updated",
        "protection_type",
        "status",
        "username"
    ]
    if "filter" not in returned_payload:
        returned_payload["filter"] = {}
    for key in filter_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["filter"][key] = passed_keywords.get(key)

    return returned_payload


def classify_domains_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a ClassifyDomains request.

    {
        "domains": [
            "string"
        ]
    }
    """
    returned_payload = {}
    keys = ["domains"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def activate_agents_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a ActivateAgents request.

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


def deactivate_agents_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a DeactivateAgents request.

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


def apply_agent_tasks_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a ApplyAgentTasks request.

    {
        "actions": [
            "string"
        ],
        "ttl": 0
    }
    """
    returned_payload = {}
    keys = ["actions", "ttl"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def create_destination_group_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a CreateDestinationGroup request.

    {
        "classification": [
            "string"
        ],
        "countries": [
            "string"
        ],
        "description": "string",
        "domains": [
            "string"
        ],
        "ipsRange": [
            "string"
        ],
        "match_ips": true,
        "name": "string",
        "singleIps": [
            "string"
        ],
        "top_level_domains": [
            "string"
        ]
    }
    """
    returned_payload = {}
    keys = [
        "classification",
        "countries",
        "description",
        "domains",
        "ipsRange",
        "match_ips",
        "name",
        "singleIps",
        "top_level_domains"
    ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def update_destination_group_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a UpdateDestinationGroup request.

    {
        "classification": [
            "string"
        ],
        "countries": [
            "string"
        ],
        "description": "string",
        "domains": [
            "string"
        ],
        "ipsRange": [
            "string"
        ],
        "match_ips": true,
        "name": "string",
        "singleIps": [
            "string"
        ],
        "top_level_domains": [
            "string"
        ]
    }
    """
    returned_payload = {}
    keys = [
        "classification",
        "countries",
        "description",
        "domains",
        "ipsRange",
        "match_ips",
        "name",
        "singleIps",
        "top_level_domains"
    ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def update_seraphic_rule_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a UpdateRuleMixin0 request.

    {
        "addExtensionIds": [
            "string"
        ],
        "addExtensionNames": [
            "string"
        ],
        "destinations": "string",
        "removeExtensionIds": [
            "string"
        ],
        "removeExtensionNames": [
            "string"
        ],
        "status": "string",
        "targets": "string"
    }
    """
    returned_payload = {}
    keys = [
        "addExtensionIds",
        "addExtensionNames",
        "destinations",
        "removeExtensionIds",
        "removeExtensionNames",
        "status",
        "targets"
    ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def add_url_domain_list_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a AddUrlDomainList request.

    {
        "integrationId": "string",
        "urls": [
            "string"
        ]
    }
    """
    returned_payload = {}
    keys = ["integrationId", "urls"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def query_seraphic_agents_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a QueryAgents request.

    {
        "filter": {
            "application": [
                "string"
            ],
            "application_name": [
                "string"
            ],
            "application_version": [
                "string"
            ],
            "browser_name": [
                "string"
            ],
            "browser_version": [
                "string"
            ],
            "deployment_method": [
                "string"
            ],
            "email": [
                "string"
            ],
            "first_seen": {
                "end": "string",
                "start": "string"
            },
            "host_id": [
                "string"
            ],
            "hostname": [
                "string"
            ],
            "id": [
                "string"
            ],
            "last_seen": {
                "end": "string",
                "start": "string"
            },
            "os_name": [
                "string"
            ],
            "platform": [
                "string"
            ],
            "policy_updated": [
                "string"
            ],
            "protection_type": [
                "string"
            ],
            "status": [
                "string"
            ],
            "username": [
                "string"
            ]
        },
        "limit": 0,
        "search": "string",
        "skip": 0,
        "sort": [
            "string"
        ]
    }
    """
    returned_payload = {}
    keys = ["filter", "limit", "search", "skip", "sort"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    filter_keys = [
        "application",
        "application_name",
        "application_version",
        "browser_name",
        "browser_version",
        "deployment_method",
        "email",
        "first_seen",
        "host_id",
        "hostname",
        "id",
        "last_seen",
        "os_name",
        "platform",
        "policy_updated",
        "protection_type",
        "status",
        "username"
    ]
    if "filter" not in returned_payload:
        returned_payload["filter"] = {}
    for key in filter_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["filter"][key] = passed_keywords.get(key)

    return returned_payload


def query_destination_groups_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a QueryDestinationGroups request.

    {
        "exclude": [
            "string"
        ],
        "filter": "string",
        "limit": 0,
        "search": "string",
        "skip": 0,
        "sort": [
            "string"
        ]
    }
    """
    returned_payload = {}
    keys = ["exclude", "filter", "limit", "search", "skip", "sort"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def query_seraphic_rules_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a QueryRulesMixin0 request.

    {
        "advanced_filter": "string",
        "exclude": [
            "string"
        ],
        "filter": "string",
        "limit": 0,
        "rule_ids": [
            "string"
        ],
        "search": "string",
        "skip": 0,
        "sort": [
            "string"
        ]
    }
    """
    returned_payload = {}
    keys = ["advanced_filter", "exclude", "filter", "limit", "rule_ids", "search", "skip", "sort"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload
