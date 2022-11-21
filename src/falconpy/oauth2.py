"""Falcon OAuth2 Authentication API Interface Class.

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
# pylint: disable=R0902,R0913
import time
from typing import Dict, Optional
from ._auth_object import FalconAuth
from ._endpoint._oauth2 import _oauth2_endpoints as Endpoints
from ._token_fail_reason import TokenFailReason
from ._util import (
    perform_request,
    generate_b64cred,
    confirm_base_url,
    generate_error_result,
    generate_ok_result,
    autodiscover_region,
    )


class OAuth2(FalconAuth):
    """OAuth2 Service Class.

    To create an instance of this class you must provide either:
        - your client_id and client_secret.
        - a properly formatted dictionary containing your client_id and client_secret
          Example:
          {
              "client_id": FALCON_CLIENT_ID,
              "client_secret": FALCON_CLIENT_SECRET,
              "member_cid": OPTIONAL_CHILD_CID
          }
        - a valid access_token

    All other class constructor arguments are optional.
    """

    # Default attributes
    refreshable: bool = True
    token_expiration: int = 0
    token_time: float = time.time()
    token_fail_reason: str = None
    token_status: int = None

    def __init__(self,
                 access_token: Optional[str or bool] = False,
                 base_url: Optional[str] = "https://api.crowdstrike.com",
                 ssl_verify: Optional[bool] = True,
                 proxy: Optional[Dict[str, str]] = None,
                 timeout: Optional[float or tuple] = None,
                 creds: Optional[Dict[str, str]] = None,
                 client_id: Optional[str] = None,
                 client_secret: Optional[str] = None,
                 user_agent: Optional[str] = None,
                 member_cid: Optional[str] = None,
                 renew_window: Optional[int] = 120
                 ) -> "OAuth2":
        """Construct an instance of the class.

        Initializes the base class by ingesting credentials,
        the proxy dictionary and specifications for other attributes
        such as the base URL, SSL verification, and timeout.

        Keyword arguments
        ----
        base_url : str
            CrowdStrike API URL to use for requests. [Default: US-1]
        ssl_verify : bool
            Flag specifying if SSL verification should be used. [Default: True]
        proxy : dict
            Dictionary of proxies to be used for requests.
        timeout : float or tuple
            Value specifying timeouts to use for requests.
        creds : dict
            Dictionary containing CrowdStrike API credentials.
            Mutually exclusive to client_id / client_secret.
        client_id : str
            Client ID for the CrowdStrike API. Mutually exclusive to creds.
        client_secret : str
            Client Secret for the CrowdStrike API. Mutually exclusive to creds.
        member_cid : str
            Child CID to connect to. Mutually exclusive to creds.
        renew_window : int
            Amount of time (in seconds) between now and the token expiration before
            a refresh of the token is performed. Default: 120, Max: 1200
            Values over 1200 will be reset to the maximum.

        Arguments
        ----
        This method only supports keywords to specify arguments.

        Returns
        ----
        class (OAuth2)
            A constructed instance of the OAuth2 Service Class.
        """
        super().__init__(base_url=confirm_base_url(base_url),
                         ssl_verify=ssl_verify,
                         timeout=timeout,
                         proxy=proxy,
                         user_agent=user_agent
                         )
        # Direct Authentication
        if client_id and client_secret and not creds:
            creds = {
                "client_id": client_id,
                "client_secret": client_secret
            }
            # You must pass member_cid the same way you pass client_id / secret.
            # If you use a creds dictionary, pass the member_cid there instead.
            if member_cid:
                creds["member_cid"] = member_cid
        elif not creds:
            creds = {}
        # Credential Authentication (also powers Direct Authentication)
        self.creds: Dict[str, str] = creds
        # Legacy (Token) Authentication (fallback)
        self.token_value: str or bool = access_token
        if access_token:
            # We do not have API credentials, disable token refresh.
            self.refreshable = False
            # Assume the token was just generated.
            self.token_expiration = 1799
        # Set the token renewal window, ignored when using Legacy Authentication.
        self.token_renew_window: int = max(min(renew_window, 1200), 120)

    def token(self) -> dict:
        """Generate an authorization token.

        HTTP Method: POST

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/oauth2/oauth2AccessToken

        Keyword arguments
        ----
        This method does not accept keyword arguments.

        Arguments
        ----
        This method does not accept arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        operation_id = "oauth2AccessToken"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = {}
        if self.cred_format_valid:
            data_payload = {
                'client_id': self.creds['client_id'],
                'client_secret': self.creds['client_secret']
            }
            if "member_cid" in self.creds:
                data_payload["member_cid"] = self.creds["member_cid"]
            returned = perform_request(method="POST", endpoint=target_url, data=data_payload,
                                       headers=header_payload, verify=self.ssl_verify,
                                       proxy=self.proxy, timeout=self.timeout,
                                       user_agent=self.user_agent)
            if isinstance(returned, dict):  # Issue #433
                self.token_status = returned["status_code"]
                if self.token_status == 201:
                    self.token_expiration = returned["body"]["expires_in"]
                    self.token_time = time.time()
                    self.token_value = returned["body"]["access_token"]
                    self.token_fail_reason = None
                    self.base_url = autodiscover_region(self.base_url, returned)
                else:
                    if "errors" in returned["body"]:
                        if returned["body"]["errors"]:
                            self.token_fail_reason = returned["body"]["errors"][0]["message"]
            else:
                returned = generate_error_result("Unexpected API response received", 403)
                self.token_fail_reason = TokenFailReason["UNEXPECTED"].value
                self.token_status = 403
        else:
            returned = generate_error_result("Invalid credentials specified", 403)
            self.token_fail_reason = TokenFailReason["INVALID"].value
            self.token_status = 403

        return returned

    def revoke(self, token: str) -> dict:
        """Revoke the specified authorization token.

        HTTP Method: POST

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/oauth2/oauth2RevokeToken

        Keyword arguments
        ----
        token : str
            Token string to be revoked.

        Arguments
        ----
        When not specified as a keyword, token is assumed as the only accepted argument.

        Returns
        ----
        dict
            Dictionary containing API response.
        """
        operation_id = "oauth2RevokeToken"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        if self.cred_format_valid:
            b64cred = generate_b64cred(self.creds["client_id"], self.creds["client_secret"])
            header_payload = {"Authorization": f"basic {b64cred}"}
            data_payload = {"token": f"{token}"}
            returned = perform_request(method="POST", endpoint=target_url, data=data_payload,
                                       headers=header_payload, verify=self.ssl_verify,
                                       proxy=self.proxy, timeout=self.timeout,
                                       user_agent=self.user_agent)
            self.token_expiration = 0
            self.token_value = False
        else:
            returned = generate_error_result("Invalid credentials specified", 403)

        return returned

    def logout(self) -> dict:
        """Revoke the current token.

        Keyword arguments
        ----
        This method does not accept keyword arguments.

        Arguments
        ----
        This method does not accept arguments.

        Returns
        ----
        dict
            Dictionary object containing API response.
        """
        returned = self.revoke(self.token_value)
        if returned["status_code"] == 200:
            returned = generate_ok_result(message="Current token successfully revoked.",
                                          headers=returned["headers"]
                                          )
        else:
            returned = generate_error_result("Unable to revoke current token.", 500)

        return returned

    @property
    def auth_headers(self) -> Dict[str, str]:
        """Return a Bearer token baked into an Authorization header ready for an HTTP request."""
        if self.token_expired and self.refreshable:
            self.token()

        return {"Authorization": f"Bearer {self.token_value}"}

    @property
    def token_expired(self) -> bool:
        """Return whether the token is ready to be renewed."""
        return (time.time() - self.token_time) >= (self.token_expiration - self.token_renew_window)

    @property
    def authenticated(self) -> bool:
        """Return if we are authenticated by retrieving the inverse of token_expired."""
        return not self.token_expired

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    oauth2AccessToken = token
    oAuth2AccessToken = token
    oauth2RevokeToken = revoke
    oAuth2RevokeToken = revoke
