"""CrowdStrike Falcon Aspm API interface class.

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
from typing import Dict, Union
from json import loads, dumps
from ._util import force_default, process_service_request, generate_error_result
from ._payload import (
    aspm_delete_tag_payload,
    aspm_violations_search_payload,
    aspm_get_services_count_payload,
    aspm_query_payload,
    aspm_integration_payload,
    aspm_integration_task_payload,
    aspm_node_payload,
    aspm_application_payload,
    aspm_update_tag_payload,
    retrieve_relay_node_payload,
    aspm_group_payload
    )
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._aspm import _aspm_endpoints as Endpoints


class ASPM(ServiceClass):
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
    def execute_function_data_count(self: object,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a selected list of query language count queries.

        Request and response are in MSA format.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/ExecuteFunctionDataCount

        Keyword arguments
        -----------------
        aws_lambda_arn : str
            ARN for the lambda. Required when using the aws cloud provider.
        azure_function_app_name : str
            Azure function name. Required when using the azure cloud provider.
        azure_site_resource_group : str
            Azure resource group ID. Required when using the azure cloud provider.
        azure_site_subscription_id : str
            Azure site ID. Required when using the azure cloud provider.
        cloud_provider : str
            Cloud provider name. String. Available values: aws, azure, gcp
        gcp_cloud_function_url : str
            GCP cloud function URL. Required when using the gcp cloud provider.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        query_name : str
            Query name. String.
            Available values:
              sensitive_data          vulnerable_libraries
              reachable               risk_severity
              sensitive_datasources   sensitive_data_tags
              dependencies

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExecuteFunctionDataCount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def execute_functions_count(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a selected list of query language count queries.

        Request and response are in MSA format.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/ExecuteFunctionsCount

        Keyword arguments
        -----------------
        cid : str or list[str]
            Customer ID. String or list of strings. Required when using the azure cloud provider.
        cloud_account_id : str or list[str]
            AWS cloud account ID. String or list of strings.
            Required when using the aws cloud provider.
        cloud_provider : str or list[str]
            Cloud provider name. String or list of strings. Available values: aws, azure, gcp
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        query_name : str
            Query name. String.
            Available values:
              sensitive_data          dependencies
              reachable               vulnerable_libraries
              sensitive_datasources
        region : str or list[str]
            GCP region. String or list of string. Required when using the gcp cloud provider.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExecuteFunctionsCount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def execute_function_data_query_count(self: object,
                                          parameters: dict = None,
                                          **kwargs
                                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a selected list of query language count queries.

        Request and response are in MSA format.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/ExecuteFunctionDataQueryCount

        Keyword arguments
        -----------------
        field : str
            Field to retrieve.
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
            operation_id="ExecuteFunctionDataQueryCount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def execute_functions_query_count(self: object,
                                      parameters: dict = None,
                                      **kwargs
                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a selected list of query language count queries.

        Request and response are in MSA format.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/ExecuteFunctionsQueryCount

        Keyword arguments
        -----------------
        field : str
            Field to retrieve.
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
            operation_id="ExecuteFunctionsQueryCount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def execute_function_data(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a selected list of query language count queries.

        Request and response are in MSA format.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/ExecuteFunctionData

        Keyword arguments
        -----------------
        field : str
            Field to retrieve.
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
            operation_id="ExecuteFunctionData",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def execute_functions_over_time(self: object,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a selected list of query language count queries.

        Request and response are in MSA format.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/ExecuteFunctionsOvertime

        Keyword arguments
        -----------------
        field : str
            Field to retrieve.
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
            operation_id="ExecuteFunctionsOvertime",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def execute_functions(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a selected list of query language count queries.

        Request and response are in MSA format.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/ExecuteFunctions

        Keyword arguments
        -----------------
        field : str
            Field to retrieve.
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
            operation_id="ExecuteFunctions",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def execute_function_data_query(self: object,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a selected list of query language count queries.

        Request and response are in MSA format.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/ExecuteFunctionDataQuery

        Keyword arguments
        -----------------
        field : str
            Field to retrieve.
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
            operation_id="ExecuteFunctionDataQuery",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def execute_functions_query_over_time(self: object,
                                          parameters: dict = None,
                                          **kwargs
                                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a selected list of query language count queries.

        Request and response are in MSA format.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/ExecuteFunctionsQueryOvertime

        Keyword arguments
        -----------------
        field : str
            Field to retrieve.
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
            operation_id="ExecuteFunctionsQueryOvertime",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def execute_functions_query(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve a selected list of query language count queries.

        Request and response are in MSA format.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/ExecuteFunctionsQuery

        Keyword arguments
        -----------------
        field : str
            Field to retrieve.
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
            operation_id="ExecuteFunctionsQuery",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_service_artifacts(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve service artifacts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/getServiceArtifacts

        Keyword arguments
        -----------------
        persistent_signature : str
            Persistent signature.
        optional_time : str
            Optional time.
        revision_id : str
            Revision ID.
        limit : int
            Upper bound for records returned.
        offset : int
            Starting position for records returned.
        order_by : str or list[str]
            Sort order field.
        direction : str
            Sort order direction. String. Available values: asc, desc
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("persistent_signature", None):
            kwargs["persistentSignature"] = kwargs.get("persistent_signature", None)
        if kwargs.get("optional_time", None):
            kwargs["optionalTime"] = kwargs.get("optional_time", None)
        if kwargs.get("revision_id", None):
            kwargs["revisionId"] = kwargs.get("revision_id", None)
        if kwargs.get("order_by", None):
            kwargs["orderBy"] = kwargs.get("order_by", None)
        param_list = loads(dumps(parameters))
        for key, value in param_list.items():
            if key == "persistent_signature":
                parameters["persistentSignature"] = value
            if key == "optional_time":
                parameters["optionalTime"] = value
            if key == "revision_id":
                parameters["revisionId"] = value
            if key == "order_by":
                parameters["orderBy"] = value
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="getServiceArtifacts",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_business_applications(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create or Update Business Applications.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/UpsertBusinessApplications

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "name": "string",
                    "persistentSignatures": [
                        "string"
                    ]
                }
        name : str
            Application name.
        persistent_signatures : list[str]
            Signatures.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aspm_application_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpsertBusinessApplications",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_cloud_security_integration_state(self: object,
                                             parameters: dict = None,
                                             **kwargs
                                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get Cloud Security integration state.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/GetCloudSecurityIntegrationState

        Keyword arguments
        -----------------
        This method does not support keyword arguments.
        This method does not support positional arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCloudSecurityIntegrationState",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def set_cloud_security_integration_state(self: object,
                                             body: dict = None,
                                             **kwargs
                                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Set Cloud Security integration state.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/SetCloudSecurityIntegrationState

        Keyword arguments
        -----------------
        body : dict
            Full body payload in JSON format. Not required if using other keywords.
        is_enabled : bool
            Flag indicating if the state should be enabled.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("is_enabled", None) is not None:
            body["isEnabled"] = kwargs.get("is_enabled", None)

        body_list = loads(dumps(body))
        for key, value in body_list.items():
            if key == "is_enabled":
                body["isEnabled"] = value

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="SetCloudSecurityIntegrationState",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_executor_nodes(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get all the relay nodes.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/GetExecutorNodes

        Keyword arguments
        -----------------
        direction : str
            Sort order direction. String. Allowed values: asc, desc
        executor_node_ids : str or list[str]
            Executor node IDs.
        executor_node_names : str or list[str]
            Executor node names.
        executor_node_states : str or list[str]
            Executor node states.
        executor_node_types : str or list[str]
            Executor node types.
        node_type : str
            Node type.
        integration_type : int
            Integration type.
        limit : int
            Maximum number of records to return.
        offset : int
            Starting position for records returned.
        order_by : str
            Field to use for sorting results. String. Allowed values: name, id, state, type
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
            operation_id="GetExecutorNodes",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_executor_node(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an existing relay node.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/UpdateExecutorNode

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "additional_header": "string",
                    "current_aws_arn": "string",
                    "dashboard_url": "string",
                    "id": integer,
                    "last_health_check": integer,
                    "name": "string",
                    "node_type": "string",
                    "password": "string",
                    "pod_settings": {
                        "imageAddress": "string",
                        "imagePullSecrets": [
                            "string"
                        ],
                        "podLabels": [
                            {
                                "key": "string",
                                "value": "string"
                            }
                        ]
                    },
                    "proxy_address": "string",
                    "type": "string",
                    "useJobs": boolean,
                    "username": "string"
                }
        current_aws_arn : str
        dashboard_url : str
        id : str
        last_health_check : int
        name : str
        node_type : str
        password : str
        pod_settings : dict
        proxy_address : str
        type : str
        use_jobs : str
        username : str

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aspm_node_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateExecutorNode",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_executor_node(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new relay node.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/CreateExecutorNode

        Keyword arguments
        -----------------
        additional_header : str
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "additional_header": "string",
                    "current_aws_arn": "string",
                    "dashboard_url": "string",
                    "id": integer,
                    "last_health_check": integer,
                    "name": "string",
                    "node_type": "string",
                    "password": "string",
                    "pod_settings": {
                        "imageAddress": "string",
                        "imagePullSecrets": [
                            "string"
                        ],
                        "podLabels": [
                            {
                                "key": "string",
                                "value": "string"
                            }
                        ]
                    },
                    "proxy_address": "string",
                    "type": "string",
                    "useJobs": boolean,
                    "username": "string"
                }
        current_aws_arn : str
        dashboard_url : str
        id : str
        last_health_check : int
        name : str
        node_type : str
        password : str
        pod_settings : dict
        proxy_address : str
        type : str
        use_jobs : str
        username : str

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aspm_node_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateExecutorNode",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_executor_nodes_metadata(self: object,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get metadata about all executor nodes.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/GetExecutorNodesMetadata

        Keyword arguments
        -----------------
        executor_node_ids : str or list[str]
            Executor node ids.
        executor_node_names : str or list[str]
            Executor node names.
        executor_node_states : str or list[str]
            Executor node states.
        executor_node_types : str or list[str]
            Executor node types.
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
            operation_id="GetExecutorNodesMetadata",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_node(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete a relay node.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/DeleteExecutorNode

        Keyword arguments
        -----------------
        id : int
            ID of the node to remove.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_id = kwargs.get("id", parameters.get("id", None))
        if not target_id:
            return generate_error_result(
                message="You must provide the id keyword or parameter in order to use this operation.",
                code=400
                )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteExecutorNode",
            path_id=target_id
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def retrieve_relay_instances(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve the relay instance in CSV format.

        HTTP Method: DELETE

        Swagger URL
        -----------
        Swagger unavailable

        Keyword arguments
        -----------------
        additional_header : str
            Additional header to provide.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "additional_header": "string",
                    "current_aws_arn": "string",
                    "dashboard_url": "string",
                    "id": integer,
                    "last_health_check": integer,
                    "name": "string",
                    "node_type": "string",
                    "password": "string",
                    "pod_settings": {
                        "imageAddress": "string",
                        "imagePullSecrets": [
                        "string"
                        ],
                        "podLabels": [
                        {
                            "key": "string",
                            "value": "string"
                        }
                        ]
                    },
                    "proxy_address": "string",
                    "status": {
                        "State": integer,
                        "StateLastUpdated": integer,
                        "StateReason": integer
                    },
                    "type": "string",
                    "useJobs": true,
                    "username": "string"
                }
        current_aws_arn : str
            Current AWS ARN.
        dashboard_url : str
            URL for the related dashboard.
        id : str
            ID of the node to remove.
        last_health_check : int
            Last health check.
        name : str
            Name.
        node_type : str
            Node type.
        pod_settings : dict
            Related pod settings.
        proxy_address : str
            Address of the proxy.
        status : dict
            Current status.
        type : str
            Relay type.
        use_jobs : bool
            Flag indicating if jobs should be used.
        username : str
            Account username.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = retrieve_relay_node_payload(kwargs)
        target_id = kwargs.get("id", body.get("id", None))
        if not target_id:
            return generate_error_result(
                message="You must provide the id keyword or parameter in order to use this operation.",
                code=400
                )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RetrieveRelayInstances",
            path_id=target_id,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_integration_tasks(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get all integration tasks.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/GetIntegrationTasks

        Keyword arguments
        -----------------
        integration_task_type : int
            Integration task type.
        category : str
            Integration category.
        offset : int
            Starting position to returned records.
        limit : int
            Total number of records to return.
        order_by : str
            Field to use for sort order. String. Available values: name, id, integrationTask
        direction : str
            Sort direction. String. Allowed values: asc, desc
        integration_task_types : int
            Integration task types.
        ids : int
            Integration IDs.
        names : str
            Integration names.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("order_by", None):
            kwargs["orderBy"] = kwargs.get("order_by", None)
        param_list = loads(dumps(parameters))
        for key, value in param_list.items():
            if key == "order_by":
                parameters["orderBy"] = value
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntegrationTasks",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_integration_task(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create new integration task.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/CreateIntegrationTask

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "integration_task": {
                        "access_token": "string",
                        "additional_header": "string",
                        "business_application": "string",
                        "data": "string",
                        "enabled": true,
                        "id": 0,
                        "integration": {
                        "data": "string",
                        "enabled": true,
                        "id": 0,
                        "integration_type": {
                            "configured": true,
                            "display_name": "string",
                            "enabled": true,
                            "id": 0,
                            "name": "string"
                        },
                        "name": "string",
                        "node": {
                            "additional_header": "string",
                            "current_aws_arn": "string",
                            "dashboard_url": "string",
                            "id": 0,
                            "last_health_check": 0,
                            "name": "string",
                            "node_type": "string",
                            "password": "string",
                            "pod_settings": {
                            "imageAddress": "string",
                            "imagePullSecrets": [
                                "string"
                            ],
                            "podLabels": [
                                {
                                "key": "string",
                                "value": "string"
                                }
                            ]
                            },
                            "proxy_address": "string",
                            "type": "string",
                            "useJobs": true,
                            "username": "string"
                        },
                        "type": {
                            "configured": true,
                            "display_name": "string",
                            "enabled": true,
                            "id": 0,
                            "name": "string"
                        },
                        "update_time": 0
                        },
                        "integration_task_type": {
                        "category": "string",
                        "display_name": "string",
                        "enabled": true,
                        "id": 0,
                        "name": "string",
                        "required_integration_types": [
                            {
                            "configured": true,
                            "display_name": "string",
                            "enabled": true,
                            "id": 0,
                            "name": "string"
                            }
                        ]
                        },
                        "latest_task_run": {
                        "create_time": {
                            "nanos": 0,
                            "seconds": 0
                        },
                        "events": [
                            {
                            "FlatData": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            },
                            "additional_data": "string",
                            "data": {
                                "additional_info": "string",
                                "aws": {
                                "accountArn": "string",
                                "region": "string"
                                },
                                "azureSite": {
                                "location": "string",
                                "resourceGroup": "string",
                                "siteId": "string",
                                "siteKind": "string",
                                "siteName": "string",
                                "subscriptionId": "string"
                                },
                                "azureVm": {
                                "id": "string",
                                "region": "string",
                                "resourceGroup": "string",
                                "subscriptionId": "string",
                                "vmName": "string"
                                },
                                "cloud_function": {
                                "function_name": "string"
                                },
                                "crowdstrike_cloud_security": {
                                "baseUrl": "string",
                                "clientId": "string",
                                "cloudProvider": "string",
                                "iomID": "string",
                                "policyId": 0,
                                "resourceId": "string",
                                "resourceType": "string"
                                },
                                "ec2": {
                                "instance_id": "string",
                                "instance_name": "string"
                                },
                                "ecs": {
                                "clusterName": "string",
                                "collectionMethod": 0,
                                "resourceArn": "string",
                                "resourceName": "string",
                                "resourceType": "string"
                                },
                                "gcp": {
                                "project": "string",
                                "region": "string"
                                },
                                "host": {
                                "address": "string"
                                },
                                "k8s": {
                                "container": "string",
                                "namespace": "string",
                                "pod_name": "string"
                                },
                                "lambda": {
                                "lambdaArn": "string",
                                "lambdaName": "string"
                                },
                                "remedy": {
                                "content": "string",
                                "url": "string"
                                },
                                "snyk": {
                                "apiEndpointUrl": "string",
                                "appEndpointUrl": "string",
                                "groupId": "string"
                                },
                                "sonatype": {
                                "CVEId": "string",
                                "applicationPublicId": "string",
                                "componentNameVersion": "string",
                                "iqServerUrl": "string"
                                }
                            },
                            "flat_fields": [
                                "string"
                            ],
                            "id": 0,
                            "message": "string",
                            "object": "string",
                            "object_type": "string",
                            "send_time": {
                                "nanos": 0,
                                "seconds": 0
                            },
                            "status": 0
                            }
                        ],
                        "id": 0,
                        "latest_event": {
                            "FlatData": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                            },
                            "additional_data": "string",
                            "data": {
                            "additional_info": "string",
                            "aws": {
                                "accountArn": "string",
                                "region": "string"
                            },
                            "azureSite": {
                                "location": "string",
                                "resourceGroup": "string",
                                "siteId": "string",
                                "siteKind": "string",
                                "siteName": "string",
                                "subscriptionId": "string"
                            },
                            "azureVm": {
                                "id": "string",
                                "region": "string",
                                "resourceGroup": "string",
                                "subscriptionId": "string",
                                "vmName": "string"
                            },
                            "cloud_function": {
                                "function_name": "string"
                            },
                            "crowdstrike_cloud_security": {
                                "baseUrl": "string",
                                "clientId": "string",
                                "cloudProvider": "string",
                                "iomID": "string",
                                "policyId": 0,
                                "resourceId": "string",
                                "resourceType": "string"
                            },
                            "ec2": {
                                "instance_id": "string",
                                "instance_name": "string"
                            },
                            "ecs": {
                                "clusterName": "string",
                                "collectionMethod": 0,
                                "resourceArn": "string",
                                "resourceName": "string",
                                "resourceType": "string"
                            },
                            "gcp": {
                                "project": "string",
                                "region": "string"
                            },
                            "host": {
                                "address": "string"
                            },
                            "k8s": {
                                "container": "string",
                                "namespace": "string",
                                "pod_name": "string"
                            },
                            "lambda": {
                                "lambdaArn": "string",
                                "lambdaName": "string"
                            },
                            "remedy": {
                                "content": "string",
                                "url": "string"
                            },
                            "snyk": {
                                "apiEndpointUrl": "string",
                                "appEndpointUrl": "string",
                                "groupId": "string"
                            },
                            "sonatype": {
                                "CVEId": "string",
                                "applicationPublicId": "string",
                                "componentNameVersion": "string",
                                "iqServerUrl": "string"
                            }
                            },
                            "flat_fields": [
                            "string"
                            ],
                            "id": 0,
                            "message": "string",
                            "object": "string",
                            "object_type": "string",
                            "send_time": {
                            "nanos": 0,
                            "seconds": 0
                            },
                            "status": 0
                        },
                        "metadata": {
                            "collected_objects": 0,
                            "end_time": {
                            "nanos": 0,
                            "seconds": 0
                            },
                            "integration_task_id": 0,
                            "integration_task_name": "string",
                            "integration_task_type": {
                            "category": "string",
                            "display_name": "string",
                            "enabled": true,
                            "id": 0,
                            "name": "string",
                            "required_integration_types": [
                                {
                                "configured": true,
                                "display_name": "string",
                                "enabled": true,
                                "id": 0,
                                "name": "string"
                                }
                            ]
                            },
                            "start_time": {
                            "nanos": 0,
                            "seconds": 0
                            },
                            "total_objects": 0
                        },
                        "progress": 0,
                        "scheduled": true,
                        "trace_uuid": "string"
                        },
                        "name": "string",
                        "next_run": {
                        "nanos": 0,
                        "seconds": 0
                        },
                        "progress": 0,
                        "schedule": {
                        "every": 0,
                        "every_unit": 0,
                        "hour": 0,
                        "minute": 0,
                        "startTimeTimezoneOffsetMinutes": 0,
                        "start_time": {
                            "nanos": 0,
                            "seconds": 0
                        },
                        "timezone": 0,
                        "weekdays": [
                            0
                        ]
                        },
                        "schedule_every_unit_display_name": "string",
                        "trigger": "string",
                        "type": {
                        "category": "string",
                        "display_name": "string",
                        "enabled": true,
                        "id": 0,
                        "name": "string",
                        "required_integration_types": [
                            {
                            "configured": true,
                            "display_name": "string",
                            "enabled": true,
                            "id": 0,
                            "name": "string"
                            }
                        ]
                        }
                    }
                }



        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aspm_integration_task_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateIntegrationTask",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_integration_tasks_admin(self: object,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get all the integration tasks, requires admin scope.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/GetIntegrationTasksAdmin

        Keyword arguments
        -----------------
        integration_task_type : int
            Integration task type.
        category : str
            Integration task category.
        offset : int
            Offset from which to start returning records.
        limit : int
            Maximum number of records to return.
        order_by : str
            Fields to use for sort order.
        direction : str
            Sort order direction. String. Allowed values: asc or desc
        integration_task_types : int
            Integration task types.
        ids : int
            Integration task ID.
        names : str
            Integration task name.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("order_by", None):
            kwargs["orderBy"] = kwargs.get("order_by", None)
        param_list = loads(dumps(parameters))
        for key, value in param_list.items():
            if key == "order_by":
                parameters["orderBy"] = value
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntegrationTasksAdmin",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_integration_tasks_metadata(self: object,
                                       parameters: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get metadata about all integration tasks.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/GetIntegrationTasksMetadata

        Keyword arguments
        -----------------
        category : str
            Integration category. String. Allowed values: collection, exporting
        integration_task_types : int
            Integration task types.
        ids : int
            Integration IDs.
        names : str
            Integration names.
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
            operation_id="GetIntegrationTasksMetadata",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_integration_tasks_v2(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get all the integration tasks.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/GetIntegrationTasksV2

        Keyword arguments
        -----------------
        integration_task_type : int
            Integration task type.
        category : str
            Integration category.
        offset : int
            Starting position to returned records.
        limit : int
            Total number of records to return.
        order_by : str
            Field to use for sort order. String. Available values: name, id, integrationTask
        direction : str
            Sort direction. String. Allowed values: asc, desc
        integration_task_types : int
            Integration task types.
        ids : int
            Integration IDs.
        names : str
            Integration names.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("order_by", None):
            kwargs["orderBy"] = kwargs.get("order_by", None)
        param_list = loads(dumps(parameters))
        for key, value in param_list.items():
            if key == "order_by":
                parameters["orderBy"] = value
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntegrationTasksV2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def update_integration_task(self: object,
                                body: dict = None,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an existing integration task by its ID.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/UpdateIntegrationTask

        Keyword arguments
        -----------------
        ID : int
            ID of the integration task to update.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                "integration_task": {
                    "access_token": "string",
                    "additional_header": "string",
                    "business_application": "string",
                    "data": "string",
                    "enabled": true,
                    "id": 0,
                    "integration": {
                    "data": "string",
                    "enabled": true,
                    "id": 0,
                    "integration_type": {
                        "configured": true,
                        "display_name": "string",
                        "enabled": true,
                        "id": 0,
                        "name": "string"
                    },
                    "name": "string",
                    "node": {
                        "additional_header": "string",
                        "current_aws_arn": "string",
                        "dashboard_url": "string",
                        "id": 0,
                        "last_health_check": 0,
                        "name": "string",
                        "node_type": "string",
                        "password": "string",
                        "pod_settings": {
                        "imageAddress": "string",
                        "imagePullSecrets": [
                            "string"
                        ],
                        "podLabels": [
                            {
                            "key": "string",
                            "value": "string"
                            }
                        ]
                        },
                        "proxy_address": "string",
                        "type": "string",
                        "useJobs": true,
                        "username": "string"
                    },
                    "type": {
                        "configured": true,
                        "display_name": "string",
                        "enabled": true,
                        "id": 0,
                        "name": "string"
                    },
                    "update_time": 0
                    },
                    "integration_task_type": {
                    "category": "string",
                    "display_name": "string",
                    "enabled": true,
                    "id": 0,
                    "name": "string",
                    "required_integration_types": [
                        {
                        "configured": true,
                        "display_name": "string",
                        "enabled": true,
                        "id": 0,
                        "name": "string"
                        }
                    ]
                    },
                    "latest_task_run": {
                    "create_time": {
                        "nanos": 0,
                        "seconds": 0
                    },
                    "events": [
                        {
                        "FlatData": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "additional_data": "string",
                        "data": {
                            "additional_info": "string",
                            "aws": {
                            "accountArn": "string",
                            "region": "string"
                            },
                            "azureSite": {
                            "location": "string",
                            "resourceGroup": "string",
                            "siteId": "string",
                            "siteKind": "string",
                            "siteName": "string",
                            "subscriptionId": "string"
                            },
                            "azureVm": {
                            "id": "string",
                            "region": "string",
                            "resourceGroup": "string",
                            "subscriptionId": "string",
                            "vmName": "string"
                            },
                            "cloud_function": {
                            "function_name": "string"
                            },
                            "crowdstrike_cloud_security": {
                            "baseUrl": "string",
                            "clientId": "string",
                            "cloudProvider": "string",
                            "iomID": "string",
                            "policyId": 0,
                            "resourceId": "string",
                            "resourceType": "string"
                            },
                            "ec2": {
                            "instance_id": "string",
                            "instance_name": "string"
                            },
                            "ecs": {
                            "clusterName": "string",
                            "collectionMethod": 0,
                            "resourceArn": "string",
                            "resourceName": "string",
                            "resourceType": "string"
                            },
                            "gcp": {
                            "project": "string",
                            "region": "string"
                            },
                            "host": {
                            "address": "string"
                            },
                            "k8s": {
                            "container": "string",
                            "namespace": "string",
                            "pod_name": "string"
                            },
                            "lambda": {
                            "lambdaArn": "string",
                            "lambdaName": "string"
                            },
                            "remedy": {
                            "content": "string",
                            "url": "string"
                            },
                            "snyk": {
                            "apiEndpointUrl": "string",
                            "appEndpointUrl": "string",
                            "groupId": "string"
                            },
                            "sonatype": {
                            "CVEId": "string",
                            "applicationPublicId": "string",
                            "componentNameVersion": "string",
                            "iqServerUrl": "string"
                            }
                        },
                        "flat_fields": [
                            "string"
                        ],
                        "id": 0,
                        "message": "string",
                        "object": "string",
                        "object_type": "string",
                        "send_time": {
                            "nanos": 0,
                            "seconds": 0
                        },
                        "status": 0
                        }
                    ],
                    "id": 0,
                    "latest_event": {
                        "FlatData": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                        },
                        "additional_data": "string",
                        "data": {
                        "additional_info": "string",
                        "aws": {
                            "accountArn": "string",
                            "region": "string"
                        },
                        "azureSite": {
                            "location": "string",
                            "resourceGroup": "string",
                            "siteId": "string",
                            "siteKind": "string",
                            "siteName": "string",
                            "subscriptionId": "string"
                        },
                        "azureVm": {
                            "id": "string",
                            "region": "string",
                            "resourceGroup": "string",
                            "subscriptionId": "string",
                            "vmName": "string"
                        },
                        "cloud_function": {
                            "function_name": "string"
                        },
                        "crowdstrike_cloud_security": {
                            "baseUrl": "string",
                            "clientId": "string",
                            "cloudProvider": "string",
                            "iomID": "string",
                            "policyId": 0,
                            "resourceId": "string",
                            "resourceType": "string"
                        },
                        "ec2": {
                            "instance_id": "string",
                            "instance_name": "string"
                        },
                        "ecs": {
                            "clusterName": "string",
                            "collectionMethod": 0,
                            "resourceArn": "string",
                            "resourceName": "string",
                            "resourceType": "string"
                        },
                        "gcp": {
                            "project": "string",
                            "region": "string"
                        },
                        "host": {
                            "address": "string"
                        },
                        "k8s": {
                            "container": "string",
                            "namespace": "string",
                            "pod_name": "string"
                        },
                        "lambda": {
                            "lambdaArn": "string",
                            "lambdaName": "string"
                        },
                        "remedy": {
                            "content": "string",
                            "url": "string"
                        },
                        "snyk": {
                            "apiEndpointUrl": "string",
                            "appEndpointUrl": "string",
                            "groupId": "string"
                        },
                        "sonatype": {
                            "CVEId": "string",
                            "applicationPublicId": "string",
                            "componentNameVersion": "string",
                            "iqServerUrl": "string"
                        }
                        },
                        "flat_fields": [
                        "string"
                        ],
                        "id": 0,
                        "message": "string",
                        "object": "string",
                        "object_type": "string",
                        "send_time": {
                        "nanos": 0,
                        "seconds": 0
                        },
                        "status": 0
                    },
                    "metadata": {
                        "collected_objects": 0,
                        "end_time": {
                        "nanos": 0,
                        "seconds": 0
                        },
                        "integration_task_id": 0,
                        "integration_task_name": "string",
                        "integration_task_type": {
                        "category": "string",
                        "display_name": "string",
                        "enabled": true,
                        "id": 0,
                        "name": "string",
                        "required_integration_types": [
                            {
                            "configured": true,
                            "display_name": "string",
                            "enabled": true,
                            "id": 0,
                            "name": "string"
                            }
                        ]
                        },
                        "start_time": {
                        "nanos": 0,
                        "seconds": 0
                        },
                        "total_objects": 0
                    },
                    "progress": 0,
                    "scheduled": true,
                    "trace_uuid": "string"
                    },
                    "name": "string",
                    "next_run": {
                    "nanos": 0,
                    "seconds": 0
                    },
                    "progress": 0,
                    "schedule": {
                    "every": 0,
                    "every_unit": 0,
                    "hour": 0,
                    "minute": 0,
                    "startTimeTimezoneOffsetMinutes": 0,
                    "start_time": {
                        "nanos": 0,
                        "seconds": 0
                    },
                    "timezone": 0,
                    "weekdays": [
                        0
                    ]
                    },
                    "schedule_every_unit_display_name": "string",
                    "trigger": "string",
                    "type": {
                    "category": "string",
                    "display_name": "string",
                    "enabled": true,
                    "id": 0,
                    "name": "string",
                    "required_integration_types": [
                        {
                        "configured": true,
                        "display_name": "string",
                        "enabled": true,
                        "id": 0,
                        "name": "string"
                        }
                    ]
                    }
                }
                }
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_id = kwargs.get("id", parameters.get("id", None))
        if not target_id:
            return generate_error_result(
                message="You must provide the id keyword or parameter in order to use this operation.",
                code=400
                )

        if not body:
            body = aspm_integration_task_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateIntegrationTask",
            keywords=kwargs,
            params=parameters,
            body=body,
            path_id=target_id
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_integration_task(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an existing integration task by its ID.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/DeleteIntegrationTask

        Keyword arguments
        -----------------
        ID : int
            ID of the integration task to remove.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_id = kwargs.get("id", parameters.get("id", None))
        if not target_id:
            return generate_error_result(
                message="You must provide the id keyword or parameter in order to use this operation.",
                code=400
                )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteIntegrationTask",
            path_id=target_id
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def run_integration_task(self: object,
                             body: dict = None,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Run an integration task by its ID.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/RunIntegrationTask

        Keyword arguments
        -----------------
        access_token : str
            Integration access token.
        body : dict
            Full body payload dictionary in JSON format. Not required if using other keywords.
                {
                    "access_token": "string",
                    "category": "string",
                    "data": "string",
                    "override": boolean,
                    "scheduled": boolean,
                    "task_id": integer
                }
        category : str
            Integration task category.
        data : str
            Integration task data.
        ID : int
            ID of the integration task to execute.
        override : bool
            Override previous task.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        scheduled : bool
            Schedule task.
        task_id : int
            Integration task ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_id = kwargs.get("id", parameters.get("id", None))
        if not target_id:
            return generate_error_result(
                message="You must provide the id keyword or parameter in order to use this operation.",
                code=400
                )

        if not body:
            body = aspm_integration_task_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RunIntegrationTask",
            keywords=kwargs,
            body=body,
            params=parameters,
            path_id=target_id
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def run_integration_task_admin(self: object,
                                   body: dict = None,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Run an integration task by its ID - for admin scope.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/RunIntegrationTaskAdmin

        Keyword arguments
        -----------------
        ID : int
            Integration task ID.
        category : str
            Integration task category.
        body : dict
            Full body payload in JSON format. Not required when using other keywords.
                {
                    "access_token": "string",
                    "category": "string",
                    "data": "string",
                    "override": boolean,
                    "scheduled": boolean,
                    "task_id": integer
                }
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aspm_integration_task_payload(kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RunIntegrationTaskAdmin",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def run_integration_task_v2(self: object,
                                body: dict = None,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Run an integration task by its ID.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/RunIntegrationTaskV2

        Keyword arguments
        -----------------
        ID : int
            Integration task ID.
        category : str
            Integration task category.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "access_token": "string",
                    "category": "string",
                    "data": "string",
                    "override": boolean,
                    "scheduled": bolean,
                    "task_id": integer
                }
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aspm_integration_task_payload(kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RunIntegrationTaskV2",
            keywords=kwargs,
            params=parameters
            )

    def get_integration_types(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get all the integration types.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/GetIntegrationTypes

        Keyword arguments
        -----------------
        This operation does not accept keyword arguments.

        Arguments
        ---------
        This operation does not accept arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetIntegrationTypes"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_integrations(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a list of all the integrations.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/GetIntegrations

        Keyword arguments
        -----------------
        integration_type : int
            Type of integration.
        category : str
            Integration category.
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
            operation_id="GetIntegrations",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_integration(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new integration.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/CreateIntegration

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "integration": {
                        "data": "string",
                        "enabled": boolean,
                        "id": integer,
                        "integration_type": {
                            "configured": boolean,
                            "display_name": "string",
                            "enabled": boolean,
                            "id": integer,
                            "name": "string"
                        },
                        "name": "string",
                        "node": {
                            "additional_header": "string",
                            "current_aws_arn": "string",
                            "dashboard_url": "string",
                            "id": integer,
                            "last_health_check": integer,
                            "name": "string",
                            "node_type": "string",
                            "password": "string",
                            "pod_settings": {
                                "imageAddress": "string",
                                "imagePullSecrets": [
                                    "string"
                                ],
                                "podLabels": [
                                    {
                                        "key": "string",
                                        "value": "string"
                                    }
                                ]
                            },
                            "proxy_address": "string",
                            "type": "string",
                            "useJobs": boolean,
                            "username": "string"
                        },
                        "type": {
                            "configured": boolean,
                            "display_name": "string",
                            "enabled": boolean,
                            "id": integer,
                            "name": "string"
                        },
                        "update_time": integer
                    }
                }
        integration : dict
            Integration details.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aspm_integration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateIntegration",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_integrations_v2(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get a list of all the integrations.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/GetIntegrationsV2

        Keyword arguments
        -----------------
        integration_type : int
            Integration type.
        category : str
            Integration category.
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
            operation_id="GetIntegrationsV2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_integration(self: object,
                           body: dict = None,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an existing integration by its ID.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/UpdateIntegration

        Keyword arguments
        -----------------
        id : int
            ID of the integration to update.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "integration": {
                        "data": "string",
                        "enabled": boolean,
                        "id": integer,
                        "integration_type": {
                            "configured": boolean,
                            "display_name": "string",
                            "enabled": boolean,
                            "id": integer,
                            "name": "string"
                        },
                        "name": "string",
                        "node": {
                            "additional_header": "string",
                            "current_aws_arn": "string",
                            "dashboard_url": "string",
                            "id": integer,
                            "last_health_check": integer,
                            "name": "string",
                            "node_type": "string",
                            "password": "string",
                            "pod_settings": {
                                "imageAddress": "string",
                                "imagePullSecrets": [
                                    "string"
                                ],
                                "podLabels": [
                                    {
                                        "key": "string",
                                        "value": "string"
                                    }
                                ]
                            },
                            "proxy_address": "string",
                            "type": "string",
                            "useJobs": boolean,
                            "username": "string"
                        },
                        "type": {
                            "configured": boolean,
                            "display_name": "string",
                            "enabled": boolean,
                            "id": integer,
                            "name": "string"
                        },
                        "update_time": integer
                    },
                    "overwriteFields": [
                        "string"
                    ]
                }
        integration : dict
            Integration details.
        overwrite_fields : list[str]
            Fields to overwrite.
        parameters : dict
            Full parameters payload dictionary. Not required if using the 'id' keyword.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_id = kwargs.get("id", parameters.get("id", None))
        if not target_id:
            return generate_error_result(
                message="You must provide the id keyword or parameter in order to use this operation.",
                code=400
                )

        if not body:
            body = aspm_integration_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateIntegration",
            body=body,
            path_id=target_id
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_integration(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an existing integration by its ID.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/DeleteIntegration

        Keyword arguments
        -----------------
        id : int
            ID of the integration to remove.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_id = kwargs.get("id", parameters.get("id", None))
        if not target_id:
            return generate_error_result(
                message="You must provide the id keyword or parameter in order to use this operation.",
                code=400
                )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteIntegration",
            path_id=target_id
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def execute_query(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Execute a query. The syntax used is identical to that of the query page.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/ExecuteQuery

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "paginate": {
                        "direction": "string",
                        "limit": integer,
                        "offset": integer,
                        "orderBy": [
                            "string"
                        ]
                    },
                    "query": "string",
                    "selectFields": {
                        "fields": [
                            "string"
                        ],
                        "serviceFields": [
                            "string"
                        ],
                        "withoutServices": boolean
                    },
                    "timestamp": integer
                }
        paginate : dict
            Pagination detail.
        query : str
            Query to perform.
        select_fields : str
            Field selection detail. Dictionary.
            Dictionary contents:
            fields - For filtering relevant fields only.
            withoutServices - Default is set to True,
               you will not receive information about the services.
               If you want to get the relevant service, set to False.
            serviceFields - For filtering relevant fields of the service
                            (if you chose to get it)
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        timestamp : int
            Timestamp.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aspm_query_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExecuteQuery",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_servicenow_deployments(self: object,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve ServiceNow deployments.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/ServiceNowGetDeployments

        Keyword arguments
        -----------------
        ql_filters : str
            Query filter.
        limit : int
            Maximum number of records to return.
        offset : int
            Starting position of return records.
        orderBy : str
            Sort order field.
        direction : str
            Sort direction.
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
            operation_id="ServiceNowGetDeployments",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_servicenow_services(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve ServiceNow services.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/ServiceNowGetServices

        Keyword arguments
        -----------------
        exclude_artifacts : bool
            Flag indicating if artifacts should be excluded.
        ql_filters : str
            Query filter.
        limit : int
            Maximum number of records to return.
        offset : int
            Starting position of return records.
        orderBy : str
            Sort order field.
        direction : str
            Sort direction.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if kwargs.get("order_by", None):
            kwargs["orderBy"] = kwargs.get("order_by")

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ServiceNowGetServices",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_services_count(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get the total amount of existing services.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/GetServicesCount

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "deploymentTupleFilters": [
                        {
                        "excludes": [
                            {
                                "key": "string",
                                "value": "string"
                            }
                        ],
                        "includes": [
                            {
                                "key": "string",
                                "value": "string"
                            }
                        ]
                        }
                    ],
                    "nestingLevel": integer,
                    "onlyCount": boolean,
                    "optionalTime": integer,
                    "pagination": {
                        "direction": "string",
                        "limit": integer,
                        "offset": integer,
                        "order_by": [
                            "string"
                        ]
                    },
                    "persistentSignatures": [
                        "string"
                    ],
                    "qlFilters": "string",
                    "relatedEntities": [
                        {
                            "aggregation_type": integer,
                            "entity_type": integer,
                            "filters": {
                                "include_du_services": boolean,
                                "only_du_types": boolean,
                                "only_get_brokers": boolean
                            },
                            "groupByFields": {
                                "fields": [
                                    "string"
                                ]
                            }
                        }
                    ],
                    "revisionId": integer,
                    "rolesSignature": "string"
                }
        deployment_tuple_filters : str
        nesting : str
            level --
        only_count : str
        optional_time : str
        pagination : dict
        persistent_signatures : str
        ql_filters : str
        related_entities : str
        revision_id : str
        roles_signatures : str

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aspm_get_services_count_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetServicesCount",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def get_service_violation_types(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get the different types of violation.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/GetServiceViolationTypes

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "filter": {
                        "order_by": {
                            "by_field": "string",
                            "direction": integer
                        },
                        "paginate": {
                            "direction": "string",
                            "limit": integer,
                            "offset": integer,
                            "orderBy": [
                                "string"
                            ]
                        }
                    },
                    "optionalTime": integer,
                    "revisionId": integer
                }
        filter : dict
            Query filter.
        optional_time : int
        revision_id : int
            Revision ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aspm_violations_search_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetServiceViolationTypes",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_tags(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get all the tags.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/GetTags

        Keyword arguments
        -----------------
        is_unique : bool
            Flag indicating if the tag is unique.
        tag_name : str
            Tag name.
        limit : int
            Total number of tags to return.
        offset : int
            Starting position from which to return records.
        name : str or list[str]
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        keymap = {"is_unique": "isUnique", "tag_name": "tagName"}
        for key, camelkey in keymap.items():
            if kwargs.get(key, None):
                kwargs[camelkey] = kwargs.get(key)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetTags",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_tags(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create new or update existing tag. You can update unique tags table or regular tags table.

        HTTP Method: PUT

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/UpsertTags

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "entries": [
                        {
                            "isSensitive": true,
                            "name": "string",
                            "tag_type": "string",
                            "value": "string"
                        }
                    ]
                }
        entries : list
            Tag entries. List of dictionaries.
            Overrides the is_sensitive, persistent_signature, and value keywords.
        is_sensitive : bool
            Sensitive.
        name : str
            Tag name.
        tag_type : str
            Tag type.
        value : str
            Tag value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aspm_update_tag_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpsertTags",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def delete_tags(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Remove existing tags.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/DeleteTags

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "entries": [
                        {
                            "isSensitive": boolean,
                            "persistentSignature": "string",
                            "value": "string"
                        }
                    ],
                    "name": "string"
                }
        entries : list
            Tag entries. List of dictionaries.
            Overrides the is_sensitive, persistent_signature, and value keywords.
        is_sensitive : bool
            Sensitive.
        name : str
            Tag name.
        persistent_signature : str
            Persistent signature.
        value : str
            Tag value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aspm_delete_tag_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteTags",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_users_v2(self: object,
                     parameters: dict = None,
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List users.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/get_%2Fusers%2Fv2

        Keyword arguments
        -----------------
        pagination : str
            URL encoded pagination JSON - limit, offset, direction, orderBy.
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
            operation_id="GetUsersV2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def post_group_v2(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create group.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/post_%2Fgroup%2Fv2

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "children": [
                        0
                    ],
                    "description": "string",
                    "groupType": "string",
                    "isDefault": true,
                    "name": "string",
                    "parentId": 0,
                    "scope": "string"
                }
        children : list[int]
            IDs of child groups.
        description : str
            Description of the group.
        group_type : str
            Type of the group.
        is_default : bool
            Flag indicating if this is the default group.
        name : str
            Name of the group.
        parent_id : int
            ID of the parent group.
        scope : str
            Scope of the group.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = aspm_group_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PostGroupV2",
            body=body,
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_group(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete group.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/delete_%2Fgroup%2F%7BID%3A%5B0-9%5D%2B%7D

        Keyword arguments
        -----------------
        id : int
            Group ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_id = kwargs.get("id", parameters.get("id", None))
        if not target_id:
            return generate_error_result(
                message="You must provide the id keyword or parameter in order to use this operation.",
                code=400
                )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteGroup",
            path_id=target_id
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_default_group(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update default group.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/post_%2Fgroup%2F%7BID%3A%5B0-9%5D%2B%7D%2Fupdate_default

        Keyword arguments
        -----------------
        id : int
            Group ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_id = kwargs.get("id", parameters.get("id", None))
        if not target_id:
            return generate_error_result(
                message="You must provide the id keyword or parameter in order to use this operation.",
                code=400
                )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateDefaultGroup",
            path_id=target_id
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_group_v2(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get group details.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/get_%2Fgroup%2F%7BID%3A%5B0-9%5D%2B%7D%2Fv2

        Keyword arguments
        -----------------
        id : int
            Group ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_id = kwargs.get("id", parameters.get("id", None))
        if not target_id:
            return generate_error_result(
                message="You must provide the id keyword or parameter in order to use this operation.",
                code=400
                )

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetGroupV2",
            path_id=target_id
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_group(self: object,
                     body: dict = None,
                     parameters: dict = None,
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update group.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/post_%2Fgroup%2F%7BID%3A%5B0-9%5D%2B%7D%2Fv2

        Keyword arguments
        -----------------
        id : int
            Group ID.
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "children": [
                        0
                    ],
                    "description": "string",
                    "groupType": "string",
                    "isDefault": true,
                    "name": "string",
                    "parentId": 0,
                    "scope": "string"
                }
        children : list[int]
            IDs of child groups.
        description : str
            Description of the group.
        group_type : str
            Type of the group.
        is_default : bool
            Flag indicating if this is the default group.
        name : str
            Name of the group.
        parent_id : int
            ID of the parent group.
        scope : str
            Scope of the group.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_id = kwargs.get("id", parameters.get("id", None))
        if not target_id:
            return generate_error_result(
                message="You must provide the id keyword or parameter in order to use this operation.",
                code=400
                )

        if not body:
            body = aspm_group_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateGroup",
            body=body,
            path_id=target_id
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_group_hierarchy(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get group hierarchy.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/get_%2Fgroups%2Fhier%2Fv2

        Keyword arguments
        -----------------
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
            operation_id="GetGroupHierarchy",
            params=parameters,
            keywords=kwargs
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_groups_v2(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get groups V2.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ASPM/get_%2Fgroups%2Flist%2Fv2

        Keyword arguments
        -----------------
        type : str
            Group types to query - can either be empty (all), parents, children.
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
            operation_id="GetGroupsV2",
            keywords=kwargs,
            params=parameters
            )

    ExecuteFunctionDataCount = execute_function_data_count
    ExecuteFunctionsCount = execute_functions_count
    ExecuteFunctionDataQueryCount = execute_function_data_query_count
    ExecuteFunctionsQueryCount = execute_functions_query_count
    ExecuteFunctionData = execute_function_data
    ExecuteFunctionsOvertime = execute_functions_over_time
    ExecuteFunctions = execute_functions
    ExecuteFunctionDataQuery = execute_function_data_query
    ExecuteFunctionsQueryOvertime = execute_functions_query_over_time
    ExecuteFunctionsQuery = execute_functions_query
    getServiceArtifacts = get_service_artifacts
    UpsertBusinessApplications = update_business_applications
    GetCloudSecurityIntegrationState = get_cloud_security_integration_state
    SetCloudSecurityIntegrationState = set_cloud_security_integration_state
    GetExecutorNodes = get_executor_nodes
    UpdateExecutorNode = update_executor_node
    CreateExecutorNode = create_executor_node
    GetExecutorNodesMetadata = get_executor_nodes_metadata
    RetrieveRelayInstances = retrieve_relay_instances
    DeleteExecutorNode = delete_node
    GetIntegrationTasks = get_integration_tasks
    CreateIntegrationTask = create_integration_task
    GetIntegrationTasksAdmin = get_integration_tasks_admin
    GetIntegrationTasksMetadata = get_integration_tasks_metadata
    GetIntegrationTasksV2 = get_integration_tasks_v2
    UpdateIntegrationTask = update_integration_task
    DeleteIntegrationTask = delete_integration_task
    RunIntegrationTask = run_integration_task
    RunIntegrationTaskV2 = run_integration_task_v2
    RunIntegrationTaskAdmin = run_integration_task_admin
    GetIntegrationTypes = get_integration_types
    GetIntegrations = get_integrations
    CreateIntegration = create_integration
    GetIntegrationsV2 = get_integrations_v2
    UpdateIntegration = update_integration
    DeleteIntegration = delete_integration
    ExecuteQuery = execute_query
    ServiceNowGetDeployments = get_servicenow_deployments
    ServiceNowGetServices = get_servicenow_services
    GetServicesCount = get_services_count
    GetServiceViolationTypes = get_service_violation_types
    GetTags = get_tags
    UpsertTags = update_tags
    DeleteTags = delete_tags
    GetUsersV2 = get_users_v2
    PostGroupV2 = post_group_v2
    DeleteGroup = delete_group
    UpdateDefaultGroup = update_default_group
    GetGroupV2 = get_group_v2
    UpdateGroup = update_group
    GetGroupHierarchy = get_group_hierarchy
    GetGroupsV2 = get_groups_v2
