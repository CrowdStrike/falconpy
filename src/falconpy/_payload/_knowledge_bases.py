"""Internal payload handling library - KnowledgeBases.

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


def entities_knowledge_bases_create_v1_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a EntitiesKnowledgeBasesCreateV1 request.

    {
        "created_at": "string",
        "created_by": {
            "cid": "string",
            "created_at": "string",
            "factors": [
                "string"
            ],
            "first_name": "string",
            "last_login_at": "string",
            "last_name": "string",
            "status": "string",
            "uid": "string",
            "updated_at": "string",
            "user_type": "string",
            "uuid": "string"
        },
        "description": "string",
        "embedding_model": "string",
        "files_count": 0,
        "id": "string",
        "is_deleted": true,
        "name": "string",
        "updated_at": "string",
        "updated_by": {
            "cid": "string",
            "created_at": "string",
            "factors": [
                "string"
            ],
            "first_name": "string",
            "last_login_at": "string",
            "last_name": "string",
            "status": "string",
            "uid": "string",
            "updated_at": "string",
            "user_type": "string",
            "uuid": "string"
        }
    }
    """
    returned_payload = {}
    keys = [
        "created_at",
        "created_by",
        "description",
        "embedding_model",
        "files_count",
        "id",
        "is_deleted",
        "name",
        "updated_at",
        "updated_by"
    ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    created_by_keys = [
        "cid",
        "created_at",
        "factors",
        "first_name",
        "last_login_at",
        "last_name",
        "status",
        "uid",
        "updated_at",
        "user_type",
        "uuid"
    ]
    if "created_by" not in returned_payload:
        returned_payload["created_by"] = {}
    for key in created_by_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["created_by"][key] = passed_keywords.get(key)

    updated_by_keys = [
        "cid",
        "created_at",
        "factors",
        "first_name",
        "last_login_at",
        "last_name",
        "status",
        "uid",
        "updated_at",
        "user_type",
        "uuid"
    ]
    if "updated_by" not in returned_payload:
        returned_payload["updated_by"] = {}
    for key in updated_by_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["updated_by"][key] = passed_keywords.get(key)

    return returned_payload


def entities_knowledge_bases_update_v1_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a EntitiesKnowledgeBasesUpdateV1 request.

    {
        "created_at": "string",
        "created_by": {
            "cid": "string",
            "created_at": "string",
            "factors": [
                "string"
            ],
            "first_name": "string",
            "last_login_at": "string",
            "last_name": "string",
            "status": "string",
            "uid": "string",
            "updated_at": "string",
            "user_type": "string",
            "uuid": "string"
        },
        "description": "string",
        "embedding_model": "string",
        "files_count": 0,
        "id": "string",
        "is_deleted": true,
        "name": "string",
        "updated_at": "string",
        "updated_by": {
            "cid": "string",
            "created_at": "string",
            "factors": [
                "string"
            ],
            "first_name": "string",
            "last_login_at": "string",
            "last_name": "string",
            "status": "string",
            "uid": "string",
            "updated_at": "string",
            "user_type": "string",
            "uuid": "string"
        }
    }
    """
    returned_payload = {}
    keys = [
        "created_at",
        "created_by",
        "description",
        "embedding_model",
        "files_count",
        "id",
        "is_deleted",
        "name",
        "updated_at",
        "updated_by"
    ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    created_by_keys = [
        "cid",
        "created_at",
        "factors",
        "first_name",
        "last_login_at",
        "last_name",
        "status",
        "uid",
        "updated_at",
        "user_type",
        "uuid"
    ]
    if "created_by" not in returned_payload:
        returned_payload["created_by"] = {}
    for key in created_by_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["created_by"][key] = passed_keywords.get(key)

    updated_by_keys = [
        "cid",
        "created_at",
        "factors",
        "first_name",
        "last_login_at",
        "last_name",
        "status",
        "uid",
        "updated_at",
        "user_type",
        "uuid"
    ]
    if "updated_by" not in returned_payload:
        returned_payload["updated_by"] = {}
    for key in updated_by_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["updated_by"][key] = passed_keywords.get(key)

    return returned_payload
