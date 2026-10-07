"""Internal payload handling library - EvalRuns.

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


def create_eval_run_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a EntitiesEvalRunsCreateV1 request.

    {
        "actual_cost": "string",
        "agent_id": "string",
        "agent_version_id": "string",
        "completed_at": "string",
        "created_at": "string",
        "created_by": {
            "access_granted_at": "string",
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
            "uuid": "string",
            "api_client_id": "string",
            "email": "string",
            "name": "string"
        },
        "dataset_entry_ids": [
            "string"
        ],
        "dataset_ids": [
            "string"
        ],
        "entry_tags": [
            "string"
        ],
        "estimated_cost": "string",
        "evaluator_ids": [
            "string"
        ],
        "id": "string",
        "is_deleted": true,
        "metadata": "string",
        "name": "string",
        "owner": "string",
        "progress": {
            "completed_cases": 0,
            "error_cases": 0,
            "total_cases": 0
        },
        "project_id": "string",
        "status": "string",
        "summary": {
            "average_latency": 0,
            "average_score": "string",
            "error_cases": 0,
            "evaluator_results": [
                "string"
            ],
            "failed_cases": 0,
            "median_score": "string",
            "passed_cases": 0,
            "std_deviation": "string",
            "total_cases": 0,
            "total_duration": 0
        },
        "updated_at": "string",
        "updated_by": {
            "access_granted_at": "string",
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
            "uuid": "string",
            "api_client_id": "string",
            "email": "string",
            "name": "string"
        },
        "variable_values": "string"
    }
    """
    returned_payload = {}
    keys = [
        "actual_cost",
        "agent_id",
        "agent_version_id",
        "completed_at",
        "created_at",
        "created_by",
        "dataset_entry_ids",
        "dataset_ids",
        "entry_tags",
        "estimated_cost",
        "evaluator_ids",
        "id",
        "is_deleted",
        "metadata",
        "name",
        "owner",
        "progress",
        "project_id",
        "status",
        "summary",
        "updated_at",
        "updated_by",
        "variable_values"
    ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    created_by_keys = [
        "access_granted_at",
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
        "uuid",
        "api_client_id",
        "email",
        "name"
    ]
    if "created_by" not in returned_payload:
        returned_payload["created_by"] = {}
    for key in created_by_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["created_by"][key] = passed_keywords.get(key)

    progress_keys = ["completed_cases", "error_cases", "total_cases"]
    if "progress" not in returned_payload:
        returned_payload["progress"] = {}
    for key in progress_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["progress"][key] = passed_keywords.get(key)

    summary_keys = [
        "average_latency",
        "average_score",
        "error_cases",
        "evaluator_results",
        "failed_cases",
        "median_score",
        "passed_cases",
        "std_deviation",
        "total_cases",
        "total_duration"
    ]
    if "summary" not in returned_payload:
        returned_payload["summary"] = {}
    for key in summary_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["summary"][key] = passed_keywords.get(key)

    updated_by_keys = [
        "access_granted_at",
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
        "uuid",
        "api_client_id",
        "email",
        "name"
    ]
    if "updated_by" not in returned_payload:
        returned_payload["updated_by"] = {}
    for key in updated_by_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["updated_by"][key] = passed_keywords.get(key)

    return returned_payload


def update_eval_run_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a EntitiesEvalRunsUpdateV1 request.

    {
        "actual_cost": "string",
        "agent_id": "string",
        "agent_version_id": "string",
        "completed_at": "string",
        "created_at": "string",
        "created_by": {
            "access_granted_at": "string",
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
            "uuid": "string",
            "api_client_id": "string",
            "email": "string",
            "name": "string"
        },
        "dataset_entry_ids": [
            "string"
        ],
        "dataset_ids": [
            "string"
        ],
        "entry_tags": [
            "string"
        ],
        "estimated_cost": "string",
        "evaluator_ids": [
            "string"
        ],
        "id": "string",
        "is_deleted": true,
        "metadata": "string",
        "name": "string",
        "owner": "string",
        "progress": {
            "completed_cases": 0,
            "error_cases": 0,
            "total_cases": 0
        },
        "project_id": "string",
        "status": "string",
        "summary": {
            "average_latency": 0,
            "average_score": "string",
            "error_cases": 0,
            "evaluator_results": [
                "string"
            ],
            "failed_cases": 0,
            "median_score": "string",
            "passed_cases": 0,
            "std_deviation": "string",
            "total_cases": 0,
            "total_duration": 0
        },
        "updated_at": "string",
        "updated_by": {
            "access_granted_at": "string",
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
            "uuid": "string",
            "api_client_id": "string",
            "email": "string",
            "name": "string"
        },
        "variable_values": "string"
    }
    """
    returned_payload = {}
    keys = [
        "actual_cost",
        "agent_id",
        "agent_version_id",
        "completed_at",
        "created_at",
        "created_by",
        "dataset_entry_ids",
        "dataset_ids",
        "entry_tags",
        "estimated_cost",
        "evaluator_ids",
        "id",
        "is_deleted",
        "metadata",
        "name",
        "owner",
        "progress",
        "project_id",
        "status",
        "summary",
        "updated_at",
        "updated_by",
        "variable_values"
    ]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    created_by_keys = [
        "access_granted_at",
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
        "uuid",
        "api_client_id",
        "email",
        "name"
    ]
    if "created_by" not in returned_payload:
        returned_payload["created_by"] = {}
    for key in created_by_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["created_by"][key] = passed_keywords.get(key)

    progress_keys = ["completed_cases", "error_cases", "total_cases"]
    if "progress" not in returned_payload:
        returned_payload["progress"] = {}
    for key in progress_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["progress"][key] = passed_keywords.get(key)

    summary_keys = [
        "average_latency",
        "average_score",
        "error_cases",
        "evaluator_results",
        "failed_cases",
        "median_score",
        "passed_cases",
        "std_deviation",
        "total_cases",
        "total_duration"
    ]
    if "summary" not in returned_payload:
        returned_payload["summary"] = {}
    for key in summary_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["summary"][key] = passed_keywords.get(key)

    updated_by_keys = [
        "access_granted_at",
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
        "uuid",
        "api_client_id",
        "email",
        "name"
    ]
    if "updated_by" not in returned_payload:
        returned_payload["updated_by"] = {}
    for key in updated_by_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["updated_by"][key] = passed_keywords.get(key)

    return returned_payload


def perform_eval_run_action_payload(passed_keywords: dict) -> dict:
    """Create a properly formatted payload for a EntitiesEvalRunsActionV1 request.

    {
        "action": "string",
        "case_cost_limit": {
            "agent_run_credit_cents": 0,
            "judge_run_credit_cents": 0
        },
        "id": "string",
        "project_id": "string"
    }
    """
    returned_payload = {}
    keys = ["action", "case_cost_limit", "id", "project_id"]
    for key in keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload[key] = passed_keywords.get(key)

    case_cost_limit_keys = ["agent_run_credit_cents", "judge_run_credit_cents"]
    if "case_cost_limit" not in returned_payload:
        returned_payload["case_cost_limit"] = {}
    for key in case_cost_limit_keys:
        if passed_keywords.get(key, None) is not None:
            returned_payload["case_cost_limit"][key] = passed_keywords.get(key)

    return returned_payload
