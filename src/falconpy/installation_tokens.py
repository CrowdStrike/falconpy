"""Falcon Installation Tokens API Interface Class.

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
from ._payload import installation_token_payload, token_settings_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._installation_tokens import _installation_tokens_endpoints as Endpoints


class InstallationTokens(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (OAuth2.token())
    """

    @force_default(defaults=["parameters"], default_types=["dict"])
    def audit_events_read(self: object,
                          *args,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get the details of one or more audit events by id.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/audit-events-read

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of audit event IDs to retrieve.
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
            operation_id="audit_events_read",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    def customer_settings_read(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Check current installation token settings.

        This method does not accept arguments or keywords.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/customer-settings-read

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="customer_settings_read"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def tokens_read(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get the details of one or more tokens by id.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/tokens-read

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of installation token IDs to retrieve.
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
            operation_id="tokens_read",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def tokens_create(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a token.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/tokens-create

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "expires_timestamp": "2021-09-22T02:28:11.762Z",
                    "label": "string",
                    "type": "string"
                }
        expires_timestamp : str
            Installation token expiration date. UTC formatted.
        label : str
            Installation token label.
        type : str
            Installation token type.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = installation_token_payload(passed_keywords=kwargs)
            if kwargs.get("type", None):
                body["type"] = kwargs.get("type", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="tokens_create",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def tokens_delete(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete a token immediately. To revoke a token, use PATCH tokens_update instead.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/tokens-delete

        Keyword arguments
        -----------------
        ids : str or list[str]
            List of installation token IDs to delete.
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
            operation_id="tokens_delete",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def tokens_update(self: object,
                      body: dict,
                      parameters: dict = None,
                      **kwargs
                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update one or more tokens.

        Use this endpoint to edit labels, change expiration, revoke, or restore.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/tokens-update

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "expires_timestamp": "2021-09-22T02:28:11.762Z",
                    "label": "string",
                    "revoked": boolean
                }
        expires_timestamp : str
            Installation token expiration date. UTC formatted.
        ids : str or list[str]
            The token IDs to be updated.
        label : str
            Installation token label.
        revoked : bool
            Boolean representing if this token is revoked.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = installation_token_payload(passed_keywords=kwargs)
            if kwargs.get("revoked", None) is not None:
                body["revoked"] = kwargs.get("revoked", None)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="tokens_update",
            body=body,
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def audit_events_query(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for audit events by providing an FQL filter and paging details.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/audit-events-query

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
            Example: action:'token_create'
        limit : int
            The maximum number of records to return in this response. [Integer, 1-1000]
            Use with the offset parameter to manage pagination of results. Defaults to 50.
        offset : int
            The offset to start retrieving records from. Integer.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax (e.g. timestamp|asc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="audit_events_query",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def tokens_query(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for tokens by providing an FQL filter and paging details.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens/tokens-query

        Keyword arguments
        -----------------
        filter : str
            The filter expression that should be used to limit the results. FQL syntax.
            Example: status:'valid'
        limit : int
            The maximum number of records to return in this response. [Integer, 1-1000]
            Use with the offset parameter to manage pagination of results. Defaults to 50.
        offset : int
            The offset to start retrieving records from. Integer.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        sort : str
            The property to sort by. FQL syntax (e.g. created_timestamp|desc).

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="tokens_query",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def customer_settings_update(self: object, body: dict = None, **kwargs) -> dict:
        """Create a token.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/installation-tokens-settings/customer-settings-update

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required when using other keywords.
                {
                    "max_active_tokens": 0,
                    "tokens_required": true
                }
        max_active_tokens : int
            Maximum number of active tokens within the CID.
        tokens_required : bool (required)
            Flag indicating if installation tokens are.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = token_settings_payload(passed_keywords=kwargs)

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="customer_settings_update",
            body=body
            )


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Installation_Tokens = InstallationTokens  # pylint: disable=C0103
