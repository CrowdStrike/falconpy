"""CrowdStrike Falcon FederatedConnections API interface class.

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
from ._payload import patch_federated_connections_config_payload, post_federated_connections_config_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._federated_connections import _federated_connections_endpoints as Endpoints


class FederatedConnections(ServiceClass):
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
    def post_federated_connections_config(self: object,
                                          body: dict = None,
                                          **kwargs
                                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create configuration for a federated connection.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "cluster_url": "string",
                    "connection_id": "string",
                    "view_token": "string"
                }
        cluster_url -- URL of the external cluster. String.
        connection_id -- ID of the federated connection. String.
        view_token -- token for accessing external cluster. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/federated-connections/PostFederatedConnectionsConfig
        """
        if not body:
            body = post_federated_connections_config_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PostFederatedConnectionsConfig",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_federated_connections_config(self: object,
                                            parameters: dict = None,
                                            **kwargs
                                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete configuration for a federated connection.

        Keyword arguments:
        connection_id -- Connection ID to delete configuration for. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/federated-connections/DeleteFederatedConnectionsConfig
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteFederatedConnectionsConfig",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def patch_federated_connections_config(self: object,
                                           body: dict = None,
                                           parameters: dict = None,
                                           **kwargs
                                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update configuration for a federated connection.

        Keyword arguments:
        connection_id -- Connection ID to update configuration for. String.
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "cluster_url": "string",
                    "view_token": "string"
                }
        cluster_url -- URL of the external cluster. String.
        view_token -- token for accessing external cluster. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/federated-connections/PatchFederatedConnectionsConfig
        """
        if not body:
            body = patch_federated_connections_config_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PatchFederatedConnectionsConfig",
            keywords=kwargs,
            params=parameters,
            body=body
            )
    PostFederatedConnectionsConfig = post_federated_connections_config
    DeleteFederatedConnectionsConfig = delete_federated_connections_config
    PatchFederatedConnectionsConfig = patch_federated_connections_config
