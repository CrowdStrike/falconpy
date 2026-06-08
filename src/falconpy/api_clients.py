"""CrowdStrike Falcon APIClients API interface class.

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
from ._payload import create_api_client_payload, update_api_client_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._api_clients import _api_clients_endpoints as Endpoints


class APIClients(ServiceClass):
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
    def get_accessible_scopes(self: object,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get all available scopes for customer.

        Keyword arguments:
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/api-clients/GetAccessibleScopes
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAccessibleScopes",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def reset_api_client_secret(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Reset existing API Client(s)'s secret based on API Client ID(s) provided as request parameter(s) 'ids'.

        Keyword arguments:
        ids -- The API Client ID(s) for which to perform action on API Client(s). List.
        action_name -- Action to perform as part of API Client update. Only allowed value is 'reset_secret'. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/api-clients/ResetAPIClientSecret
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ResetAPIClientSecret",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_api_clients(self: object,
                        *args,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get API Client(s) based on API Client ID(s) provided as request parameter(s) 'ids'.

        Keyword arguments:
        ids -- The API Client ID(s) for which to obtain API Client definition(s). String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/api-clients/GetAPIClients
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAPIClients",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_api_client(self: object,
                          body: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create new API Client.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "description": "string",
                    "name": "string",
                    "scopes": [
                        "string"
                    ]
                }
        description -- The description value. String.
        name -- The name value. String.
        scopes -- The scopes value. List.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/api-clients/CreateAPIClient
        """
        if not body:
            body = create_api_client_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateAPIClient",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_api_clients(self: object,
                           *args,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete existing API Client(s) based on API Client ID(s) provided as request parameter(s) 'ids'.

        Keyword arguments:
        ids -- The API Client ID(s) for which API Client(s) have to be deleted. String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/api-clients/DeleteAPIClients
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteAPIClients",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def update_api_client(self: object,
                          body: dict = None,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update existing API Client based on API Client ID provided as request parameter 'ids'.

        Keyword arguments:
        ids -- The API Client ID for which to update the API Client definition. String.
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "description": "string",
                    "name": "string",
                    "scopes": [
                        "string"
                    ]
                }
        description -- The description value. String.
        name -- The name value. String.
        scopes -- The scopes value. List.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/api-clients/UpdateAPIClient
        """
        if not body:
            body = update_api_client_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateAPIClient",
            keywords=kwargs,
            params=parameters,
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_all_api_client_ids_for_customer(self: object,
                                            parameters: dict = None,
                                            **kwargs
                                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get All API client ID(s) for customer.

        Keyword arguments:
        offset -- Starting index of overall result set from which to return ids. Integer.
        limit -- Number of ids to return. Integer.
        sort -- Possible values for sort by field includes id, name, created_by, updated_by, created_timestamp, last_modified.
                Ex: 'name|asc', 'name|desc', etc. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/api-clients/GetAllAPIClientIdsForCustomer
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAllAPIClientIdsForCustomer",
            keywords=kwargs,
            params=parameters
            )
    GetAccessibleScopes = get_accessible_scopes
    ResetAPIClientSecret = reset_api_client_secret
    GetAPIClients = get_api_clients
    CreateAPIClient = create_api_client
    DeleteAPIClients = delete_api_clients
    UpdateAPIClient = update_api_client
    GetAllAPIClientIdsForCustomer = get_all_api_client_ids_for_customer
