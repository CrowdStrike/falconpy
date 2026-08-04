"""CrowdStrike Falcon AgentInvocation API interface class.

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
from ._payload import invoke_agent_version_external_v1_payload, invoke_published_agent_external_v1_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._agent_invocation import _agent_invocation_endpoints as Endpoints


class AgentInvocation(ServiceClass):
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

    @force_default(defaults=["body"], default_types=["dict"])
    def invoke_published_agent_external_v1(self: object,
                                           body: dict = None,
                                           **kwargs
                                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Invoke a published agent by ID with the specified input.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/agent-invocation/InvokePublishedAgentExternalV1

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "credit_cents_limit": 0,
                    "deadline_seconds": 0,
                    "id": "string",
                    "messages": [
                        {
                            "content": "string",
                            "error": {
                                "code": "string",
                                "message": "string",
                                "param": "string",
                                "type": "string"
                            },
                            "reasoning": "string",
                            "role": "string",
                            "tool": {
                                "calls": [
                                    {
                                        "function": {
                                            "arguments": "string",
                                            "name": "string"
                                        },
                                        "id": "string",
                                        "type": "string"
                                    }
                                ],
                                "tool_id": "string"
                            },
                            "tool_approval": {
                                "external_approval": {
                                    "external_id": "string",
                                    "provider": "string"
                                },
                                "id": "string",
                                "invocation_id": "string",
                                "parameters": "string",
                                "request_message": "string",
                                "requested_at": "string",
                                "responded_at": "string",
                                "responded_by": {
                                    "customer_id": "string",
                                    "service_id": "string",
                                    "user_id": "string"
                                },
                                "response_message": "string",
                                "source_agent_id": "string",
                                "source_invocation_id": "string",
                                "status": "string",
                                "tool_call_id": "string",
                                "tool_id": "string",
                                "tool_name": "string"
                            }
                        }
                    ]
                }
        credit_cents_limit : int
            The credit_cents_limit value.
        deadline_seconds : int
            The deadline_seconds value.
        id : str
            The id value.
        messages : list
            The messages value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = invoke_published_agent_external_v1_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="InvokePublishedAgentExternalV1",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_agent_invocation_v3(self: object,
                                *args,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve the list of of messages that are resulted from the specified invocation.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/agent-invocation/GetAgentInvocationV3

        Keyword arguments
        -----------------
        id : str or list[str]
            Invocation ID.
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
            operation_id="GetAgentInvocationV3",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "id")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def invoke_agent_version_external_v1(self: object,
                                         body: dict = None,
                                         **kwargs
                                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Invoke a specific agent version by agent ID and version ID with the specified input.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/agent-invocation/InvokeAgentVersionExternalV1

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "credit_cents_limit": 0,
                    "deadline_seconds": 0,
                    "id": "string",
                    "messages": [
                        {
                            "content": "string",
                            "error": {
                                "code": "string",
                                "message": "string",
                                "param": "string",
                                "type": "string"
                            },
                            "reasoning": "string",
                            "role": "string",
                            "tool": {
                                "calls": [
                                    {
                                        "function": {
                                            "arguments": "string",
                                            "name": "string"
                                        },
                                        "id": "string",
                                        "type": "string"
                                    }
                                ],
                                "tool_id": "string"
                            },
                            "tool_approval": {
                                "external_approval": {
                                    "external_id": "string",
                                    "provider": "string"
                                },
                                "id": "string",
                                "invocation_id": "string",
                                "parameters": "string",
                                "request_message": "string",
                                "requested_at": "string",
                                "responded_at": "string",
                                "responded_by": {
                                    "customer_id": "string",
                                    "service_id": "string",
                                    "user_id": "string"
                                },
                                "response_message": "string",
                                "source_agent_id": "string",
                                "source_invocation_id": "string",
                                "status": "string",
                                "tool_call_id": "string",
                                "tool_id": "string",
                                "tool_name": "string"
                            }
                        }
                    ],
                    "version_id": "string"
                }
        credit_cents_limit : int
            The credit_cents_limit value.
        deadline_seconds : int
            The deadline_seconds value.
        id : str
            The id value.
        messages : list
            The messages value.
        version_id : str
            The version_id value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = invoke_agent_version_external_v1_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="InvokeAgentVersionExternalV1",
            body=body
            )
    InvokePublishedAgentExternalV1 = invoke_published_agent_external_v1
    GetAgentInvocationV3 = get_agent_invocation_v3
    InvokeAgentVersionExternalV1 = invoke_agent_version_external_v1
