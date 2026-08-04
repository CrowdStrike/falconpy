"""CrowdStrike Falcon ApiIntegrations API interface class.

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
from ._payload import api_plugin_command_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._api_integrations import _api_integrations_endpoints as Endpoints


class APIIntegrations(ServiceClass):
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
    def get_plugin_configs(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query for config resources and returns details.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/api-integrations/GetCombinedPluginConfigs

        Keyword arguments
        -----------------
        filter : str
            Filter items using a query in Falcon Query Language (FQL)
        limit : int
            The number of items to return in this response (default: 100, max: 500).
            Use with the offset parameter to manage pagination of results.
        offset : int
            The first item to return, where 0 is the latest item.
            Use with the limit parameter to manage pagination of results.
        sort : str
            Sort items using their properties.
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
            operation_id="GetCombinedPluginConfigs",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def execute_command_proxy(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Execute a command and proxy the response directly.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/api-integrations/ExecuteCommandProxy

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a dictionary. Not required if other keywords are provided.
                {
                    "resources": [
                        {
                        "config_auth_type": "string",
                        "config_id": "string",
                        "definition_id": "string",
                        "id": "string",
                        "operation_id": "string",
                        "request": {
                            "data": "string",
                            "params": {
                                "cookie": {},
                                "header": {},
                                "path": {},
                                "query": {}
                            },
                            "x-www-form-urlencoded": {}
                        },
                        "version": integer
                        }
                    ]
                }
        config_auth_type : str
            Configuration authorization type for plugin to execute.
            Only application for security scheme plugins. If not
            provided, execution will use the default authorization type.
        config_id : str
            Configuration ID. If omitted, the oldest configuration ID will be used.
        cookie : dict
            Request cookies. Part of the request parameters.
        data : str
            Request data.
        definition_id : str
            ID of the definition containing the operation to execute.
        header : dict
            Request headers. Part of the request parameters.
        id : str
            ID of the specific plugin to execute provided in "definition_name.operation_name"
            format.
        operation_id : str
            The specific operation to execute.
        path : dict
            Request path. Part of the request parameters.
        params : dict
            Request parameters. Not required if using other request parameter keywords.
            Can be overridden by values specified using individual keywords.
        query : dict
            Request query. Part of the request parameters.
        version : int
            The version of the definition to execute.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = api_plugin_command_payload(kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExecuteCommandProxy",
            keywords=kwargs,
            body=body
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def execute_command(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Execute a command.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/api-integrations/ExecuteCommand

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a dictionary. Not required if other keywords are provided.
                {
                    "resources": [
                        {
                        "config_auth_type": "string",
                        "config_id": "string",
                        "definition_id": "string",
                        "id": "string",
                        "operation_id": "string",
                        "request": {
                            "description": "string"
                        },
                        "version": integer
                        }
                    ]
                }
        config_auth_type : str
            Configuration authorization type for plugin to execute.
            Only application for security scheme plugins. If not
            provided, execution will use the default authorization type.
        config_id : str
            Configuration ID. If omitted, the oldest configuration ID will be used.
        definition_id : str
            ID of the definition containing the operation to execute.
        id : str
            ID of the specific plugin to execute provided in "definition_name.operation_name"
            format.
        operation_id : str
            The specific operation to execute.
        description : str
            Command description.
        version : int
            The version of the definition to execute.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = api_plugin_command_payload(kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ExecuteCommand",
            keywords=kwargs,
            body=body
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes.
    GetCombinedPluginConfigs = get_plugin_configs
    ExecuteCommandProxy = execute_command_proxy
    ExecuteCommand = execute_command
