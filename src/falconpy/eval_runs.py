"""CrowdStrike Falcon EvalRuns API interface class.

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
from ._util import force_default, process_service_request
from ._payload import create_eval_run_payload, perform_eval_run_action_payload, update_eval_run_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._eval_runs import _eval_runs_endpoints as Endpoints


class EvalRuns(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (oauth2.py)
    """

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_eval_runs(self: object,
                      parameters: dict = None,
                      **kwargs
                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve evaluation run entities for the provided id.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/eval-runs/EntitiesEvalRunsV1

        Keyword arguments
        -----------------
        ids : list
            IDs of entities to retrieve.
        project_id : str
            Scope the operation to a project.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesEvalRunsV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_eval_run(self: object,
                        body: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create or update an evaluation run.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/eval-runs/EntitiesEvalRunsCreateV1

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "actual_cost": 0.0,
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
                    "estimated_cost": 0.0,
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
                        "average_score": 0.0,
                        "error_cases": 0,
                        "evaluator_results": [
                            {
                                "average_score": 0.0,
                                "error_cases": 0,
                                "evaluator_id": "string",
                                "evaluator_name": "string",
                                "failed_cases": 0,
                                "passed_cases": 0
                            }
                        ],
                        "failed_cases": 0,
                        "median_score": 0.0,
                        "passed_cases": 0,
                        "std_deviation": 0.0,
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
        actual_cost : str
            The actual_cost value. Float.
        agent_id : str
            The agent_id value.
        agent_version_id : str
            The agent_version_id value.
        completed_at : str
            The completed_at value.
        created_at : str
            The created_at value.
        created_by : dict
            The created_by value.
        dataset_entry_ids : list
            The dataset_entry_ids value.
        dataset_ids : list
            The dataset_ids value.
        entry_tags : list
            The entry_tags value.
        estimated_cost : str
            The estimated_cost value. Float.
        evaluator_ids : list
            The evaluator_ids value.
        id : str
            The id value.
        is_deleted : bool
            The is_deleted value.
        metadata : dict
            The metadata value.
        name : str
            The name value.
        owner : str
            The owner value.
        progress : dict
            The progress value.
        project_id : str
            The project_id value.
        status : str
            The status value.
        summary : dict
            The summary value.
        updated_at : str
            The updated_at value.
        updated_by : dict
            The updated_by value.
        variable_values : dict
            The variable_values value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = create_eval_run_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesEvalRunsCreateV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_eval_run(self: object,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an evaluation run by ID.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/eval-runs/EntitiesEvalRunsDeleteV1

        Keyword arguments
        -----------------
        id : str
            ID of the evaluation run to delete.
        project_id : str
            Scope the operation to a project.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesEvalRunsDeleteV1",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_eval_run(self: object,
                        body: dict = None,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an existing evaluation run metadata.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/eval-runs/EntitiesEvalRunsUpdateV1

        Keyword arguments
        -----------------
        project_id : str
            Scope the operation to a project.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "actual_cost": 0.0,
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
                    "estimated_cost": 0.0,
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
                        "average_score": 0.0,
                        "error_cases": 0,
                        "evaluator_results": [
                            {
                                "average_score": 0.0,
                                "error_cases": 0,
                                "evaluator_id": "string",
                                "evaluator_name": "string",
                                "failed_cases": 0,
                                "passed_cases": 0
                            }
                        ],
                        "failed_cases": 0,
                        "median_score": 0.0,
                        "passed_cases": 0,
                        "std_deviation": 0.0,
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
        actual_cost : str
            The actual_cost value. Float.
        agent_id : str
            The agent_id value.
        agent_version_id : str
            The agent_version_id value.
        completed_at : str
            The completed_at value.
        created_at : str
            The created_at value.
        created_by : dict
            The created_by value.
        dataset_entry_ids : list
            The dataset_entry_ids value.
        dataset_ids : list
            The dataset_ids value.
        entry_tags : list
            The entry_tags value.
        estimated_cost : str
            The estimated_cost value. Float.
        evaluator_ids : list
            The evaluator_ids value.
        id : str
            The id value.
        is_deleted : bool
            The is_deleted value.
        metadata : dict
            The metadata value.
        name : str
            The name value.
        owner : str
            The owner value.
        progress : dict
            The progress value.
        project_id : str
            The project_id value.
        status : str
            The status value.
        summary : dict
            The summary value.
        updated_at : str
            The updated_at value.
        updated_by : dict
            The updated_by value.
        variable_values : dict
            The variable_values value.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = update_eval_run_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesEvalRunsUpdateV1",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def perform_eval_run_action(self: object,
                                body: dict = None,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Perform an action on an evaluation run (start or stop).

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/eval-runs/EntitiesEvalRunsActionV1

        Keyword arguments
        -----------------
        id : str
            ID of the evaluation run.
        action_name : str
            Action to perform: 'start' or 'stop'
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "action": "string",
                    "case_cost_limit": {
                        "agent_run_credit_cents": 0,
                        "judge_run_credit_cents": 0
                    },
                    "id": "string",
                    "project_id": "string"
                }
        action : str
            The action value.
        case_cost_limit : dict
            The case_cost_limit value.
        id : str
            The id value.
        project_id : str
            The project_id value.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = perform_eval_run_action_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="EntitiesEvalRunsActionV1",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_eval_runs(self: object,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query evaluation runs based on the provided filters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/eval-runs/QueriesEvalRunsV1

        Keyword arguments
        -----------------
        offset : int
            Starting index of overall result set from which to return ids.
        limit : int
            Number of IDs to return. Offset + limit should NOT be above 10K.
        sort : str
            Possible order by fields: name, created_at. Ex: 'created_at|desc' or 'name|asc'
        filter : str
            FQL query specifying the filter parameters.
        project_id : str
            Scope the operation to a project.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueriesEvalRunsV1",
            keywords=kwargs,
            params=parameters
            )
    EntitiesEvalRunsV1 = get_eval_runs
    EntitiesEvalRunsCreateV1 = create_eval_run
    EntitiesEvalRunsDeleteV1 = delete_eval_run
    EntitiesEvalRunsUpdateV1 = update_eval_run
    EntitiesEvalRunsActionV1 = perform_eval_run_action
    QueriesEvalRunsV1 = query_eval_runs
