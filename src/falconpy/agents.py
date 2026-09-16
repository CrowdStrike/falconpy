"""CrowdStrike Falcon Agents API interface class.

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
from ._payload import create_or_update_agent_payload, update_agent_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._agents import _agents_endpoints as Endpoints


class Agents(ServiceClass):
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
    def delete_agent(self: object,
                     *args,
                     parameters: dict = None,
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an agent and all of its versions.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/agents/DeleteAgentV1

        Keyword arguments
        -----------------
        id : str or list[str]
            Agent ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

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
            operation_id="DeleteAgentV1",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_studio_agents(self: object,
                          *args,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve agents entities for the provided ids.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/agents/GetAgentsV2

        Keyword arguments
        -----------------
        ids : str or list[str]
            IDs of entities to retrieve.
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
            operation_id="GetAgentsV2",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_or_update_agent(self: object,
                               body: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create or update an agent.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/agents/CreateOrEditAgentExternalV3

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "duplicate_from_agent_id": "string",
                    "id": "string",
                    "template_id": "string",
                    "version_definition": {
                        "compaction_config": {
                            "enabled": true,
                            "threshold": 0.0
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
                            "frequency_penalty": 0.0,
                            "max_tokens": 0,
                            "reasoning_effort": "string",
                            "temperature": 0.0,
                            "top_k": 0,
                            "top_p": 0.0
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
                            {
                                "description_override": "string",
                                "id": "string",
                                "meta": "string",
                                "name": "string",
                                "name_override": "string",
                                "parameter_overrides": "string",
                                "type": "string"
                            }
                        ]
                    }
                }
        duplicate_from_agent_id : str
            The duplicate_from_agent_id value.
        id : str
            The id value.
        template_id : str
            The template_id value.
        version_definition : dict
            The version_definition value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = create_or_update_agent_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateOrEditAgentExternalV3",
            body=body
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_agent(self: object,
                     body: dict = None,
                     parameters: dict = None,
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Modify existing agents.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/agents/PatchAgentExternalV3

        Keyword arguments
        -----------------
        id : str
            Agent ID.
        dry_run : bool
            Validate publishing without publishing the agent.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "is_enabled": true,
                    "is_published": true,
                    "version_id": "string"
                }
        is_enabled : bool
            The is_enabled value.
        is_published : bool
            The is_published value.
        version_id : str
            The version_id value.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = update_agent_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PatchAgentExternalV3",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_studio_agents(self: object,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query agents based on the provided filters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/agents/QueryAgentsV2

        Keyword arguments
        -----------------
        offset : int
            Starting index of overall result set from which to return ids.
        limit : int
            Number of IDs to return. Offset + limit should NOT be above 10K.
        sort : str
            Possible order by String.
            fields:
                  'created_date|desc'.    Ex:
        filter : str
            FQL query specifying the filter parameters.
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
            operation_id="QueryAgentsV2",
            keywords=kwargs,
            params=parameters
            )
    DeleteAgentV1 = delete_agent
    GetAgentsV2 = get_studio_agents
    CreateOrEditAgentExternalV3 = create_or_update_agent
    PatchAgentExternalV3 = update_agent
    QueryAgentsV2 = query_studio_agents
