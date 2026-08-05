"""Falcon Workflows API Interface Class.

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
# pylint: disable=C0302,R0904,R0912
import re
from os.path import exists
from typing import Dict, Union
from ._util import (
    force_default,
    process_service_request,
    handle_single_argument,
    generate_error_result
    )
from ._payload import (
    simple_action_parameter,
    generic_payload_list,
    workflow_deprovision_payload,
    workflow_template_payload,
    workflow_definition_payload,
    workflow_human_input,
    workflow_mock_payload
    )
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._workflows import _workflows_endpoints as Endpoints


class Workflows(ServiceClass):
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
    def search_activities(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search workflow activities based on the provided filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowActivitiesCombined

        Keyword arguments
        -----------------
        filter : str
            FQL query specifying filter parameters.
        offset : str
            Starting pagination offset of records to return.
        limit : int
            Maximum number of records to return.
        sort : str
            FQL formatted sort (ex: name.desc,time.asc). String.
            If direction is omitted, defaults to descending.
        skip_artifact_resolution : bool
            When true, skip Foundry artifact resolution and return the latest version of the activity,
            regardless of whether the associated Foundry app is
            installed.
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
            operation_id="WorkflowActivitiesCombined",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def search_activities_content(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for activities by name. Returns all supported activities if no filter specified.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowActivitiesContentCombined

        Keyword arguments
        -----------------
        filter : str
            FQL query specifying filter parameters.
        offset : str
            Starting pagination offset of records to return.
        limit : int
            Maximum number of records to return.
        sort : str
            FQL formatted sort (ex: name.desc,time.asc). String.
            If direction is omitted, defaults to descending.
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
            operation_id="WorkflowActivitiesContentCombined",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def search_definitions(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search workflow definitions based on the provided filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowDefinitionsCombined

        Keyword arguments
        -----------------
        filter : str
            FQL query specifying filter parameters.
        offset : str
            Starting pagination offset of records to return.
        limit : int
            Maximum number of records to return.
        sort : str
            FQL formatted sort (ex: name.desc,time.asc). String.
            If direction is omitted, defaults to descending.
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
            operation_id="WorkflowDefinitionsCombined",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def search_executions(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search workflow executions based on the provided filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowExecutionsCombined

        Keyword arguments
        -----------------
        filter : str
            FQL query specifying filter parameters.
        offset : str
            Starting pagination offset of records to return.
        limit : int
            Maximum number of records to return.
        sort : str
            FQL formatted sort (ex: name.desc,time.asc). String.
            If direction is omitted, defaults to descending.
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
            operation_id="WorkflowExecutionsCombined",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def search_triggers(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search workflow triggers based on the provided filter.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowTriggersCombined

        Keyword arguments
        -----------------
        filter : str
            FQL query specifying filter parameters.
        offset : str
            Starting pagination offset of records to return.
        limit : int
            Maximum number of records to return.
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
            operation_id="WorkflowTriggersCombined",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def export_definition(self: object,
                          *args,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Export a workflow definition for the given definition ID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowDefinitionsExport

        Keyword arguments
        -----------------
        id : str
            ID of workflow definitions to return details for.
        include_mocks : bool
            when enabled, includes referenced node-mocks inline in the exported YAML. Each
            mock's output_data field is a JSON-encoded string rather than native YAML.
        version : int
            version of the definition to export (e.g. 0 for draft); omit for active/published.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sanitize : bool
            Sanitize PII from workflow before it's exported.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'id'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowDefinitionsExport",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def import_definition(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Import a workflow definition based on the provided model.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowDefinitionsImport

        Keyword arguments
        -----------------
        data_file : bytes
            A workflow definition in YAML format to import. Can be the file location or file contents.
            Supports string or.
        name : str
            Workflow name to override.
        validate_only : bool
            When enabled, prevents saving workflow after validating.
        include_activity_metadata : bool
            When true, populates the definition model with Activity metadata which includes Activity
            Dependency and Vendor.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        data_file = kwargs.get("data_file", None)
        content_type = "application/x-yaml"
        # Retrieve data file contents from the specified location
        valid_format = False
        if exists(data_file):
            with open(data_file, "r", encoding="utf-8") as yaml_file:
                file_data = yaml_file.read()
        else:
            # Assume file contents are provided instead, can handle string or binary data
            file_data = data_file
            if isinstance(data_file, bytes):
                file_data = data_file.decode()
        if file_data:
            # Check yaml formatting
            # Look for key: value pairs
            if re.search(r'\s*:\s*[^:\n]+', file_data):
                valid_format = True
            # Look for list items
            if re.search(r'-\s+.*', file_data):
                valid_format = True
        if valid_format:
            # Create a multipart form payload for our upload file
            file_extended = [("data_file", ("yaml_upload", file_data, content_type))]
            # Remove the data file from the keywords dictionary before args_to_params processing
            kwargs.pop("data_file")
            returned = process_service_request(
                        calling_object=self,
                        endpoints=Endpoints,
                        operation_id="WorkflowDefinitionsImport",
                        keywords=kwargs,
                        params=parameters,
                        files=file_extended
                        )
        else:
            returned = generate_error_result(
                "You must provide a workflow file in YAML format or a workfile location to import.",
                caller=self
                )

        return returned

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_definition(self: object,
                          body: dict = None,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a workflow definition based on the provided model.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowDefinitionsUpdate

        Keyword arguments
        -----------------
        validate_only : bool
            When enabled, prevents saving workflow after validating.
        body : dict
            Full body payload in JSON format, not required when using other keywords.
        definition : dict
            Full workflow definition.
        change_log : str
            Optional description to outline changes made during the update.
        enabled : bool
            Specifies if the new definition should be enabled upon creation.
        flight_control : dict
            Flight control parameters.
        id : str
            Used to identify documents across versions.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = workflow_definition_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowDefinitionsUpdate",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def execute(self: object,
                body: dict = None,
                parameters: dict = None,
                **kwargs
                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Execute an on-demand workflow. Response will contain the execution ID.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowExecute

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if using other keywords.
                {
                    Workflow schema
                }
        definition_id : str or list[str]
            Definition ID to execute. Either a name or ID can be specified.
        execution_cid : str or list[str]
            CID(s) to execute on. This can be a child for Flight Control scenarios.
            If unset, the definition CID is used.
        name : str
            Workflow name to execute. Either a name or ID can be specified.
        parameters : dict
            Full parameters payload in dictionary (JSON) format. Not required
            if you are using other keywords.
        key : str
            Key used to help deduplicate executions. If unset a new UUID is used.
        depth : int
            Used to record the execution depth to help limit execution loops when a workflow
            triggers another. The maximum depth is 4.
        source_event_url : str
            Used to record a URL to the source that led to trigger the workflow.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowExecute",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def execute_internal(self: object,
                         body: dict = None,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Execute an on-demand workflow. Response will contain the execution ID.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowExecuteInternal

        Keyword arguments
        -----------------
        batch_size : int
            Used to set the size of the batch.
        body : dict
            full body payload, not required if using other keywords.
                {}
        definition_id : str or list[str]
            Definition ID to execute. Either a name or ID can be specified.
        execution_cid : str or list[str]
            CID(s) to execute on. This can be a child for Flight Control scenarios.
            If unset, the definition CID is used.
        name : str
            Workflow name to execute. Either a name or ID can be specified.
        parameters : dict
            Full parameters payload in dictionary (JSON) format. Not required
            if you are using other keywords.
        key : str
            Key used to help deduplicate executions. If unset a new UUID is used.
        depth : int
            Used to record the execution depth to help limit execution loops when a workflow
            triggers another. The maximum depth is 4.
        source_event_url : str
            Used to record a URL to the source that led to trigger the workflow.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowExecuteInternal",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def mock_execute(self: object,
                     body: dict = None,
                     parameters: dict = None,
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Execute a workflow definition with mocks.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowMockExecute

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if using other keywords.
                {
                    "definition" {
                        Workflow schema
                    },
                    "mocks": "string",
                    "on_demand_trigger": "string"
                }
        definition_id : str
            Definition ID to execute. Either a name or ID can be specified.
        execution_cid : str or list[str]
            CID(s) to execute on. This can be a child for Flight Control scenarios.
            If unset, the definition CID is used.
        ignore_activity_mock_references : bool
            When enabled, treats all activity mocks in the definition as disabled for this mock
            execution. Mocks provided in the request body are treated normally.
        name : str
            Workflow name to execute. Either a name or ID can be specified.
        parameters : dict
            Full parameters payload in dictionary (JSON) format. Not required
            if you are using other keywords.
        key : str
            Key used to help deduplicate executions. If unset a new UUID is used.
        depth : int
            Used to record the execution depth to help limit execution loops when a workflow
            triggers another. The maximum depth is 4.
        skip_validation : bool
            When enabled, skips validating mocks from the request body against the mocked entity's
            output schema. Mocks provided in the definition by reference are not validated in any case.
        source_event_url : str
            Used to record a URL to the source that led to trigger the workflow.
        validate_only : bool
            PRevent execution after validating mocks against definition.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = workflow_mock_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowMockExecute",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def execution_action(self: object,
                         body: dict = None,
                         parameters: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Allow a user to resume/retry a failed workflow execution.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowExecutionsAction

        Keyword arguments
        -----------------
        action_name : str
            Action to perform. String.
            Allowed values: resume
        action_parameters : list[dict]
            List of actions to perform.
        body : dict
            full body payload, not required if using other keywords.
                {
                    "action_parameters": [
                        {
                            "name": "string",
                            "value": "string"
                        }
                    ],
                    "ids": [
                        "string"
                    ]
                }
        ids : str or list[str]
            Execution IDs.
        name : str
            For single action parameter actions. Specifies the action parameter name.
        value : str
            For single action parameter actions. Specifies the action parameter value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = simple_action_parameter(kwargs,
                                           generic_payload_list(submitted_keywords=kwargs,
                                                                payload_value="ids"
                                                                )
                                           )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowExecutionsAction",
            keywords=kwargs,
            body=body,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def execution_results(self: object,
                          *args,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve results for a specified execution.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowExecutionResults

        Keyword arguments
        -----------------
        ids : str or list[str]
            Workflow execution ID to retrieve results for.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowExecutionResults",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_human_input(self: object,
                        *args,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get one or more specific human inputs by their IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowGetHumanInputV1

        Keyword arguments
        -----------------
        ids : str or list[str]
            IDs of human inputs to read.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowGetHumanInputV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_human_input(self: object,
                           body: dict = None,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update a human input.

        Provides an input in response to a human input action.
        Depending on action configuration, one or more of Approve, Decline, and/or Escalate are permitted.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowUpdateHumanInputV1

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format, not required when using other keywords.
                {
                    "input": "string",
                    "note": "string"
                }
        id : str
            ID of human input to provide an input to.
        input : str
            Input to insert.
        note : str
            Optional note to append.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = workflow_human_input(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowUpdateHumanInputV1",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def deprovision(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Deprovision a system definition that was previously provisioned on a target CID.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowSystemDefinitionsDeProvision

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if using other keywords.
                {
                    "definition_id": "string",
                    "deprovision_all": boolean,
                    "template_id": "string",
                    "template_name": "string"
                }
        definition_id : str
        deprovision_all : bool
        template_id : str
        template_name : str

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = workflow_deprovision_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowSystemDefinitionsDeProvision",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def promote(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Promote a version of a system definition.

        Tenant must be already provisioned. This allows the caller to apply an updated template
        version on a CID and expects all parameters to be supplied. If the template supports
        multi-instance, the customer scope definition ID must be supplied to determine which
        customer workflow should be update.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowSystemDefinitionsPromote

        Keyword arguments
        -----------------
        activities : dict
        body : dict
            Template to use for update. Not required if using other keywords.
                {
                    "customer_definition_id": "string",
                    "name": "string",
                    "parameters": {
                        "activities": {
                            "configuration": [
                                {
                                    "node_id": "string",
                                    "properties": {}
                                }
                            ],
                            "selection": [
                                {
                                    "id": "string",
                                    "properties": {},
                                    "source": "string"
                                }
                            ]
                        },
                        "conditions": [
                            {
                                "fields": [
                                    {
                                        "name": "string",
                                        "operator": "string"
                                    }
                                ],
                                "node_id": "string"
                            }
                        ],
                        "trigger": {
                            "fields": {},
                            "node_id": "string"
                        }
                    },
                    "template_id": "string",
                    "template_name": "string",
                    "template_version": "string"
                }
        conditions : list[dict]
        customer_definition_id : str
        name : str
        parameters : dict
            Dictionary. Overrides specified activities, conditions and trigger keywords.
        template_id : str
        template_name : str
        template_version : str
        trigger : dict

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = workflow_template_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowSystemDefinitionsPromote",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def provision(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Provision a system definition onto the target CID by using the template and provided parameters.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowSystemDefinitionsProvision

        Keyword arguments
        -----------------
        activities : dict
        body : dict
            Template to provision. Not required if using other keywords.
                {
                    "name": "string",
                    "parameters": {
                        "activities": {
                            "configuration": [
                                {
                                    "node_id": "string",
                                    "properties": {}
                                }
                            ],
                            "selection": [
                                {
                                    "id": "string",
                                    "properties": {},
                                    "source": "string"
                                }
                            ]
                        },
                        "conditions": [
                            {
                                "fields": [
                                    {
                                        "name": "string",
                                        "operator": "string"
                                    }
                                ],
                                "node_id": "string"
                            }
                        ],
                        "trigger": {
                            "fields": {},
                            "node_id": "string"
                        }
                    },
                    "template_id": "string",
                    "template_name": "string",
                    "template_version": "string"
                }
        conditions : list[dict]
        name : str
            Optional name to be set on the customer scope definition. Must be unique within a given CID.
        parameters : dict
            Runtime parameters to be interpolated to template model. Dictionary.
            Overrides specified activities, conditions and trigger keywords.
        template_id : str
            ID of the system definition template that was previously created.
        template_name : str
            Name of the system definition template to provision.
        template_version : str
            Version of system definition template, if omitted the latest version will be used.
        trigger : dict

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = workflow_template_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowSystemDefinitionsProvision",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict"])
    def workflow_definition_action(self: object,
                                   body: dict = None,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Enable or disable a workflow definition, or stop all executions for a definition.

        When a definition is disabled it will not execute against any new trigger events.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowDefinitionsAction

        Keyword arguments
        -----------------
        action_name : str
            action to perform, 'enable', 'disable', or 'cancel'.
        body : dict
            full body payload, not required if ids are provided as keyword.
            You must use body if you are going to specify action_parameters.
                {
                    "ids": [
                        "string"
                    ]
                }
        ids : str or list[str]
            IDs of workflow definitions to perform the action against.
        parameters : dict
            full parameters payload, not required if action_name is provide as a keyword.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = generic_payload_list(submitted_keywords=kwargs, payload_value="ids")

        returned = process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowDefinitionsAction",
            body=body,
            keywords=kwargs,
            params=parameters,
            )

        return returned

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def execute_single_activity_node(self: object,
                                     body: dict = None,
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Execute a single activity node.

        Results in an execution where test_mode=true and
        single_node_execution=true, associated with a definition ID if provided.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowExecuteSingleNodeV1

        Keyword arguments
        -----------------
        execution_cid : str or list[str]
            CID(s) to execute on. String or list of strings.
            This can be a child if this is a flight control enabled definition.
        definition_id : str
            Definition ID to execute.
        name : str
            Workflow name to execute. String.
            Either a name or an ID, or the definition itself in the request body, can be specified.
        key : str
            Key used to help deduplicate executions, if unset a new UUID is used.
        depth : int
            Used to record the execution depth to help limit execution loops when a workflow triggers another. Integer.
            The maximum depth is 4.
        body : dict
            full body payload, not required if ids are provided as keyword.
            Please visit the Swagger URL to view the full payload. It's long.
        definition : dict
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = {}
            if kwargs.get("definition", None):
                body["definition"] = kwargs.get("definition", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowExecuteSingleNodeV1",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_child_executions(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for child executions by providing a FQL filter and paging details.

        Returns the set of child workflow execution IDs which match the filter criteria.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/v1.child-executions.query

        Keyword arguments
        -----------------
        filter : str
            FQL query specifying filter parameters.
        offset : str
            Starting pagination offset of records to return.
        limit : int
            Maximum number of records to return.
        sort : str
            Sort items by providing a comma separated list of property and direction (eg name.desc,time.asc)
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
            operation_id="v1_child_executions_query",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def workflow_definitions_delete(self: object,
                                    *args,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Accept a list of workflow definition IDs and deletes those definitions and all their associated versions.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowDefinitionsDelete

        Keyword arguments
        -----------------
        ids : str or list[str]
            IDs of the workflow definitions to delete.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowDefinitionsDelete",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    WorkflowActivitiesCombined = search_activities
    WorkflowDefinitionsCombined = search_definitions
    WorkflowActivitiesContentCombined = search_activities_content
    WorkflowDefinitionsDelete = workflow_definitions_delete
    delete_definitions = workflow_definitions_delete
    WorkflowExecutionsCombined = search_executions
    WorkflowSystemDefinitionsDeProvision = deprovision
    WorkflowSystemDefinitionsPromote = promote
    WorkflowSystemDefinitionsProvision = provision
    WorkflowExecuteSingleNodeV1 = execute_single_activity_node
    v1_child_executions_query = query_child_executions
