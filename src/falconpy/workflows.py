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
from typing import Dict, Union
from ._util import force_default, process_service_request, handle_single_argument
from ._payload import (
    simple_action_parameter,
    generic_payload_list,
    workflow_deprovision_payload,
    workflow_template_payload
    )
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

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def execute(self: object, body: dict = None, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Execute an on-demand workflow. Response will contain the execution ID.

        Keyword arguments:
        body -- full body payload, not required if using other keywords.
                {
                    Workflow schema
                }
        definition_id -- Definition ID to execute. Either a name or ID can be specified.
                         String or List of Strings.
        name -- Workflow name to execute. Either a name or ID can be specified. String.
        parameters -- Full parameters payload in dictionary (JSON) format. Not required
                      if you are using other keywords. Dictionary.
        key -- Key used to help deduplicate executions. If unset a new UUID is used. String.
        depth -- Used to record the execution depth to help limit execution loops when a workflow
                 triggers another. The maximum depth is 4. Integer.
        source_event_url -- Used to record a URL to the source that led to trigger the workflow.
                            String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowExecute
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
    def execution_action(self: object, body: dict = None, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Allow a user to resume/retry a failed workflow execution.

        Keyword arguments:
        action_name -- Action to perform. String.
                       Allowed values: resume
        action_parameters -- List of actions to perform. List of dictionaries.
        body -- full body payload, not required if using other keywords.
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
        ids -- Execution IDs. String or List of Strings.
        name -- For single action parameter actions. Specifies the action parameter name. String.
        value -- For single action parameter actions. Specifies the action parameter value. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowExecutionsAction
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
    def execution_results(self: object, *args, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Retrieve results for a specified execution.

        Keyword arguments:
        ids -- Workflow execution ID to retrieve results for. String or List of Strings.
        parameters - full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowExecutionResults
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="WorkflowExecutionResults",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def deprovision(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Deprovision a system definition that was previously provisioned on a target CID.

        Keyword arguments:
        body -- full body payload, not required if using other keywords.
                {
                    "definition_id": "string",
                    "deprovision_all": boolean,
                    "template_id": "string",
                    "template_name": "string"
                }
        definition_id -- String.
        deprovision_all -- Boolean.
        template_id -- String.
        template_name -- String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowSystemDefinitionsDeProvision
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
    def promote(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Promote a version of a system definition.

        Tenant must be already provisioned. This allows the caller to apply an updated template
        version on a CID and expects all parameters to be supplied. If the template supports
        multi-instance, the customer scope definition ID must be supplied to determine which
        customer workflow should be update.

        Keyword arguments:
        activities -- Dictionary.
        body -- Template to use for update. Not required if using other keywords. Dictionary.
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
        conditions -- List of dictionaries.
        customer_definition_id -- String.
        name -- String.
        parameters -- Dictionary. Overrides specified activities, conditions and trigger keywords.
        template_id -- String.
        template_name -- String.
        template_version -- String.
        trigger -- Dictionary.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowSystemDefinitionsPromote
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
    def provision(self: object, body: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Promote a version of a system definition.

        Tenant must be already provisioned. This allows the caller to apply an updated template
        version on a CID and expects all parameters to be supplied. If the template supports
        multi-instance, the customer scope definition ID must be supplied to determine which
        customer workflow should be update.

        Keyword arguments:
        activities -- Dictionary.
        body -- Template to use for update. Not required if using other keywords. Dictionary.
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
        conditions -- List of dictionaries.
        customer_definition_id -- String.
        name -- String.
        parameters -- Dictionary. Overrides specified activities, conditions and trigger keywords.
        template_id -- String.
        template_name -- String.
        template_version -- String.
        trigger -- Dictionary.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/workflows/WorkflowSystemDefinitionsProvision
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

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    WorkflowExecute = execute
    WorkflowExecutionsAction = execution_action
    WorkflowExecutionResults = execution_results
    WorkflowSystemDefinitionsDeProvision = deprovision
    WorkflowSystemDefinitionsPromote = promote
    WorkflowSystemDefinitionsProvision = provision
