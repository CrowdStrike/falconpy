"""Internal payload handling library - Agents.

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


def create_or_update_agent_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a CreateOrEditAgentExternalV3 request.

    {
        "duplicate_from_agent_id": "string",
        "id": "string",
        "template_id": "string",
        "version_definition": {
            "compaction_config": {
                "enabled": true,
                "threshold": "string"
            },
            "description": "string",
            "input_format": {
                "format": "string",
                "json_schema": "string",
                "usage_instructions": "string"
            },
            "knowledge_base_ids": [
                "string"
            ],
            "model": "string",
            "model_config": {
                "enable_reasoning": true,
                "frequency_penalty": "string",
                "max_tokens": 0,
                "reasoning_effort": "string",
                "temperature": "string",
                "top_k": 0,
                "top_p": "string"
            },
            "name": "string",
            "output_format": {
                "format": "string",
                "json_schema": "string",
                "usage_instructions": "string"
            },
            "parent_version_ids": [
                "string"
            ],
            "skill_ids": [
                "string"
            ],
            "system_prompt": "string",
            "targeting_config": {
                "agent_to_agent": true,
                "apigw": true,
                "charlotte_ai": true,
                "fusion_workflows": true
            },
            "tools": [
                "string"
            ]
        }
    }
    """
    returned_payload = {}
    keys = ["duplicate_from_agent_id", "id", "template_id", "version_definition"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    version_definition_keys = [
        "compaction_config",
        "description",
        "input_format",
        "knowledge_base_ids",
        "model",
        "model_config",
        "name",
        "output_format",
        "parent_version_ids",
        "skill_ids",
        "system_prompt",
        "targeting_config",
        "tools"
    ]
    if "version_definition" not in returned_payload:
        returned_payload["version_definition"] = {}
    for key in version_definition_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["version_definition"][key] = passed_keywords.get(key)

    return returned_payload


def update_agent_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a PatchAgentExternalV3 request.

    {
        "is_enabled": true,
        "is_published": true,
        "version_id": "string"
    }
    """
    returned_payload = {}
    keys = ["is_enabled", "is_published", "version_id"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload
