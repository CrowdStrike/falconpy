"""Internal payload handling library - SAASSecurity.

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


def create_app_journal_comment_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a CreateAppJournalCommentV3 request.

    {
        "id": [
            "string"
        ],
        "note": "string"
    }
    """
    returned_payload = {}
    keys = ["id", "note"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def create_check_journal_comment_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a CreateCheckJournalCommentV3 request.

    {
        "id": [
            "string"
        ],
        "note": "string"
    }
    """
    returned_payload = {}
    keys = ["id", "note"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def set_check_param_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a SetCheckParamV3 request.

    {
        "all_future_instances": true,
        "param_name": "string",
        "reason": "string",
        "value": "string"
    }
    """
    returned_payload = {}
    keys = ["all_future_instances", "param_name", "reason", "value"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def restore_affected_entity_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a RestoreAffectedEntityV3 request.

    {
        "entities": "string"
    }
    """
    returned_payload = {}
    keys = ["entities"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload


def create_user_journal_comment_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a CreateUserJournalCommentV3 request.

    {
        "id": [
            "string"
        ],
        "note": "string"
    }
    """
    returned_payload = {}
    keys = ["id", "note"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    return returned_payload
