"""Internal payload handling library - Real Time Response

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


def command_payload(passed_keywords: dict) -> dict:  # pylint: disable=R0912  # noqa: C901
    """Creates a properly formatted payload for RTR command.
    {
        "base_command": "string",
        "batch_id": "string",
        "command_string": "string",
        "optional_hosts": [
            "string"
        ],
        "file_path": "string",
        "persist_all": true,
        "existing_batch_id": "string",
        "host_ids": [
            "string"
        ],
        "queue_offline": true,
        "hosts_to_remove": [
            "string"
        ]
        "device_id": "string",
        "id": integer,
        "persist": boolean,
        "session_id": "string",
        "origin": "string"
    }
    """
    # flake8 / pylint both complain about complexity due to the number of if statements.
    # Ignoring the complaint as this is just running through the potential passed keywords.
    returned_payload = {}
    if passed_keywords.get("base_command", None):
        returned_payload["base_command"] = passed_keywords.get("base_command", None)
    if passed_keywords.get("batch_id", None):
        returned_payload["batch_id"] = passed_keywords.get("batch_id", None)
    if passed_keywords.get("command_string", None):
        returned_payload["command_string"] = passed_keywords.get("command_string", None)
    if passed_keywords.get("optional_hosts", None):
        returned_payload["optional_hosts"] = passed_keywords.get("optional_hosts", None)
    if passed_keywords.get("persist_all", None):
        returned_payload["persist_all"] = passed_keywords.get("persist_all", None)
    if passed_keywords.get("file_path", None):
        returned_payload["file_path"] = passed_keywords.get("file_path", None)
    if passed_keywords.get("existing_batch_id", None):
        returned_payload["existing_batch_id"] = passed_keywords.get("existing_batch_id", None)
    if passed_keywords.get("host_ids", None):
        returned_payload["host_ids"] = passed_keywords.get("host_ids", None)
    if passed_keywords.get("queue_offline", None):
        returned_payload["queue_offline"] = passed_keywords.get("queue_offline", None)
    if passed_keywords.get("hosts_to_remove", None):
        returned_payload["hosts_to_remove"] = passed_keywords.get("hosts_to_remove", None)
    if passed_keywords.get("device_id", None):
        returned_payload["device_id"] = passed_keywords.get("device_id", None)
    if passed_keywords.get("id", -1) > -1:
        returned_payload["id"] = passed_keywords.get("id", None)
    if passed_keywords.get("persist", None):
        returned_payload["persist"] = passed_keywords.get("persist", None)
    if passed_keywords.get("session_id", None):
        returned_payload["session_id"] = passed_keywords.get("session_id", None)
    if passed_keywords.get("origin", None):
        returned_payload["origin"] = passed_keywords.get("origin", None)

    return returned_payload


def data_payload(passed_keywords: dict) -> dict:
    """Creates a properly formatted formData payload for
    RTR file uploads.
    {
        "id": "string",
        "description": "string",
        "name": "string",
        "comments_for_audit_log": "string",
        "content": "string",
        "platform": "string",
        "permission_type": "string"
    }
    """
    returned_payload = {}
    if passed_keywords.get("id", None):
        returned_payload["id"] = passed_keywords.get("id", None)
    if passed_keywords.get("description", None):
        returned_payload["description"] = passed_keywords.get("description", None)
    if passed_keywords.get("name", None):
        returned_payload["name"] = passed_keywords.get("name", None)
    if passed_keywords.get("comments_for_audit_log", None):
        returned_payload["comments_for_audit_log"] = passed_keywords.get("comments_for_audit_log", None)
    if passed_keywords.get("content", None):
        returned_payload["content"] = passed_keywords.get("content", None)
    if passed_keywords.get("platform", None):
        returned_payload["platform"] = passed_keywords.get("platform", None)
    if passed_keywords.get("permission_type", None):
        returned_payload["permission_type"] = passed_keywords.get("permission_type", None)

    return returned_payload
