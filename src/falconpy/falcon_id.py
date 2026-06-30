"""CrowdStrike Falcon FalconId API interface class.

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
from ._payload import update_third_party_passkey_registry_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._falcon_id import _falcon_id_endpoints as Endpoints


class FalconId(ServiceClass):
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
    def get_third_party_passkey_registry(self: object,
                                         *args,
                                         parameters: dict = None,
                                         **kwargs
                                         ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Fetch third party passkey registries.

        Keyword arguments:
        ids -- Third party passkey registry IDs to retrieve String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-id/GetThirdPartyPasskeyRegistry
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetThirdPartyPasskeyRegistry",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_third_party_passkey_registry(self: object,
                                            *args,
                                            parameters: dict = None,
                                            **kwargs
                                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete third party passkey registries.

        Keyword arguments:
        ids -- Third party passkey registry IDs to delete String or list of strings.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-id/DeleteThirdPartyPasskeyRegistry
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteThirdPartyPasskeyRegistry",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def update_third_party_passkey_registry(self: object,
                                            body: dict = None,
                                            **kwargs
                                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update third party passkey registries.

        Keyword arguments:
        body -- Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "enabled": true,
                    "id": "string"
                }
        enabled -- The enabled value. Boolean.
        id -- The id value. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-id/UpdateThirdPartyPasskeyRegistry
        """
        if not body:
            body = update_third_party_passkey_registry_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateThirdPartyPasskeyRegistry",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_third_party_passkey_registry(self: object,
                                           parameters: dict = None,
                                           **kwargs
                                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Query third party passkey registries.

        Keyword arguments:
        filter -- FQL filter. String.
        offset -- Paging offset. Integer.
        limit -- Paging limit. Integer.
        sort -- Sorting field and direction. String.
        parameters -- Full parameters payload dictionary. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falcon-id/QueryThirdPartyPasskeyRegistry
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="QueryThirdPartyPasskeyRegistry",
            keywords=kwargs,
            params=parameters
            )
    GetThirdPartyPasskeyRegistry = get_third_party_passkey_registry
    DeleteThirdPartyPasskeyRegistry = delete_third_party_passkey_registry
    UpdateThirdPartyPasskeyRegistry = update_third_party_passkey_registry
    QueryThirdPartyPasskeyRegistry = query_third_party_passkey_registry
