"""CrowdStrike Falcon CodeSecurity API interface class.

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
from ._util import force_default, process_service_request, handle_single_argument, generate_error_result
from ._payload import exchange_github_app_code_payload, register_scm_app_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._code_security import _code_security_endpoints as Endpoints


class CodeSecurity(ServiceClass):
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
    def get_scm_repository_aggregates(self: object,
                                      parameters: dict = None,
                                      **kwargs
                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get distinct values with counts for a repository field.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-inventory/GetSCMRepositoryAggregates

        Keyword arguments
        -----------------
        field : str
            Field to aggregate: name, primary_language, visibility, artifact_types, topics, owner_org, default_branch.
        filter : str
            FQL filter expression to scope aggregation.
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
            operation_id="GetSCMRepositoryAggregates",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_branch_config(self: object,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get branch config for a connection or repository.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-integration/GetBranchConfig

        Keyword arguments
        -----------------
        connection_id : str
            Connection UUID.
        repository_ids : str
            Comma-separated Repository UUIDs (optional, for per-repo or bulk query)
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
            operation_id="GetBranchConfig",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_branch_config(self: object,
                             body: dict = None,
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new branch config.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-integration/CreateBranchConfig

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateBranchConfig",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_branch_config(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete a branch config.

        Delete a branch config, or exclude a specific repository from a connection-level config when repository_id query
        param is provided.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-integration/DeleteBranchConfig

        Keyword arguments
        -----------------
        ids : str or list[str]
            Branch config UUID.
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
            operation_id="DeleteBranchConfig",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_branch_config(self: object,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update an existing branch config.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-integration/UpdateBranchConfig

        Keyword arguments
        -----------------
        id : str
            Branch config UUID.
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
            operation_id="UpdateBranchConfig",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_scm_connections(self: object,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List SCM connections for a customer.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-integration/ListSCMConnections

        Keyword arguments
        -----------------
        provider : str
            Filter by provider (github, gitlab, azure_devops)
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
            operation_id="ListSCMConnections",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_scm_connection(self: object,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get an SCM connection by UUID.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-integration/GetSCMConnection

        Keyword arguments
        -----------------
        uuid : str
            Connection UUID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_uuid = kwargs.get("uuid", None)
        if not target_uuid:
            return generate_error_result(
                message="The uuid keyword is required for this operation.",
                code=400
            )
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetSCMConnection",
            keywords=kwargs,
            params=parameters,
            path_id=target_uuid
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_scm_connection(self: object,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an SCM connection.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-integration/DeleteSCMConnection

        Keyword arguments
        -----------------
        uuid : str
            Connection UUID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_uuid = kwargs.get("uuid", None)
        if not target_uuid:
            return generate_error_result(
                message="The uuid keyword is required for this operation.",
                code=400
            )
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteSCMConnection",
            keywords=kwargs,
            params=parameters,
            path_id=target_uuid
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def trigger_scm_sync(self: object,
                         body: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Trigger an immediate sync for a connection.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-integration/TriggerSCMSync

        Keyword arguments
        -----------------
        uuid : str
            Connection UUID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_uuid = kwargs.get("uuid", None)
        if not target_uuid:
            return generate_error_result(
                message="The uuid keyword is required for this operation.",
                code=400
            )
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="TriggerSCMSync",
            body=body,
            path_id=target_uuid
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_scm_exclusion_rules(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List exclusion rules for a connection.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-integration/ListExclusionRules

        Keyword arguments
        -----------------
        connection_id : str
            Connection UUID to list rules for.
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
            operation_id="ListExclusionRules",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_scm_exclusion_rule(self: object,
                                  body: dict = None,
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create an exclusion rule.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-integration/CreateExclusionRule

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateExclusionRule",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_scm_exclusion_rule(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an exclusion rule.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-integration/DeleteExclusionRule

        Keyword arguments
        -----------------
        id : str
            Exclusion rule UUID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        target_id = kwargs.get("id", None)
        if not target_id:
            return generate_error_result(
                message="The id keyword is required for this operation.",
                code=400
            )
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteExclusionRule",
            keywords=kwargs,
            params=parameters,
            path_id=target_id
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_scm_repositories(self: object,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """List discovered SCM repositories for a customer.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-inventory/ListSCMRepositories

        Keyword arguments
        -----------------
        filter : str
            FQL filter expression.
        sort : str
            Sort field and direction in field.direction format (e.g. name.asc, created_date.desc)
        limit : int
            Maximum records to return (default 100, max 500)
        offset : int
            Starting offset for pagination.
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
            operation_id="ListSCMRepositories",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def exchange_github_app_code(self: object,
                                 body: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Exchange a GitHub App manifest code or complete registration after installation.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-integration/ExchangeGitHubAppCode

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "code": "string",
                    "installation_id": "string",
                    "org": "string",
                    "state": "string"
                }
        code : str
            The code value.
        installation_id : str
            The installation_id value.
        org : str
            The org value.
        state : str
            The state value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = exchange_github_app_code_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExchangeGitHubAppCode",
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def register_scm_app(self: object,
                         body: dict = None,
                         **kwargs
                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Register a GitHub App via the wizard flow.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/code-security-scm-integration/RegisterSCMApp

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "app_id": "string",
                    "installation_id": "string",
                    "org": "string",
                    "private_key": "string",
                    "webhook_secret": "string"
                }
        app_id : str
            The app_id value.
        installation_id : str
            The installation_id value.
        org : str
            The org value.
        private_key : str
            The private_key value.
        webhook_secret : str
            The webhook_secret value.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = register_scm_app_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RegisterSCMApp",
            body=body
            )
    GetSCMRepositoryAggregates = get_scm_repository_aggregates
    GetBranchConfig = get_branch_config
    CreateBranchConfig = create_branch_config
    DeleteBranchConfig = delete_branch_config
    UpdateBranchConfig = update_branch_config
    ListSCMConnections = list_scm_connections
    GetSCMConnection = get_scm_connection
    DeleteSCMConnection = delete_scm_connection
    TriggerSCMSync = trigger_scm_sync
    ListExclusionRules = list_scm_exclusion_rules
    CreateExclusionRule = create_scm_exclusion_rule
    DeleteExclusionRule = delete_scm_exclusion_rule
    ListSCMRepositories = list_scm_repositories
    ExchangeGitHubAppCode = exchange_github_app_code
    RegisterSCMApp = register_scm_app
