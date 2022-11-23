"""Authentication Object Base Class.

This file contains the definition of the base class that provides the
necessary functions to authenticate to the CrowdStrike Falcon OAuth2 API.

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
import time
from typing import Dict, Optional
from ._base_falcon_auth import BaseFalconAuth
from .._enum import TokenFailReason
from .._util import generate_b64cred, autodiscover_region, perform_request, generate_error_result
from .._endpoint._oauth2 import _oauth2_endpoints as AuthEndpoints


class FalconAuth(BaseFalconAuth):
    """Standard Falcon API interface used by Service Classes."""

    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
    #
    # These attributes are present in all FalconAuth objects, regardless if we are referring
    # to APIHarness, OAuth2 or custom inheriting classes.
    #
    # The default credential dictionary, where the client_id and client_secret are stored.
    creds: Dict[str, str] = {}
    # Flag indicating if we have the necessary information to automatically refresh the token.
    refreshable: bool = True
    # Integer specifying the amount of time remaining before the token expires (in seconds).
    token_expiration: int = 0
    # Float indicating the moment in time that the token was generated (timestamp).
    token_time: float = time.time()
    # String containing the error message received from the API when token generation failed.
    token_fail_reason: str = None
    # Integer representing the HTTP status code received when generating the token.
    token_status: int = None

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    # The default constructor for all authentication objects. Ingests provided credentials
    # and sets the necessary class attributes based upon the authentication detail received.
    def __init__(self,
                 access_token: Optional[str or bool] = False,
                 base_url: Optional[str] = "https://api.crowdstrike.com",
                 creds: Optional[dict] = None,
                 client_id: Optional[str] = None,
                 client_secret: Optional[str] = None,
                 member_cid: Optional[str] = None,
                 ssl_verify: Optional[bool] = True,
                 proxy: Optional[dict] = None,
                 timeout: Optional[float or tuple] = None,
                 user_agent: Optional[str] = None,
                 renew_window: Optional[int] = 120
                 ) -> "FalconAuth":
        """Construct an instance of the FalconInterface class."""
        self.base_url: str = base_url
        self.ssl_verify: bool = ssl_verify
        self.timeout: float or tuple = timeout
        self.proxy: Dict[str, str] = proxy
        self.user_agent: str = user_agent

        # ____ _  _ ___ _  _ ____ _  _ ___ _ ____ ____ ___ _ ____ _  _
        # |__| |  |  |  |__| |___ |\ |  |  | |    |__|  |  | |  | |\ |
        # |  | |__|  |  |  | |___ | \|  |  | |___ |  |  |  | |__| | \|
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

    # _  _ ____ ___ _  _ ____ ___  ____
    # |\/| |___  |  |__| |  | |  \ [__
    # |  | |___  |  |  | |__| |__/ ___]
    #
    # The generic login and logout handlers are provided here and leverage private methods
    # to perform the operation. These private methods can be overridden to provide individual
    # login and logout functionality to different inheriting class types.
    def login(self) -> dict or bool:
        """Login to the Falcon API by requesting a new token."""
        return self._login_handler()

    def logout(self) -> dict or bool:
        """Log out of the Falcon API by revoking the current token."""
        return self._logout_handler()

    # The default behavior for both the login and logout handlers is to return
    # the entire dictionary created by the token API response.
    def _login_handler(self) -> dict:
        operation_id = "oauth2AccessToken"
        target_url = f"{self.base_url}{[ep[2] for ep in AuthEndpoints if operation_id in ep[0]][0]}"
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
                    self.token_expiration = 0  # Aligning to Uber class functionality
                    if "errors" in returned["body"]:
                        if returned["body"]["errors"]:
                            self.token_fail_reason = returned["body"]["errors"][0]["message"]
            else:
                returned = generate_error_result("Unexpected API response received", 403)
                self.token_expiration = 0
                self.token_fail_reason = TokenFailReason["UNEXPECTED"].value
                self.token_status = 403
        else:
            returned = generate_error_result("Invalid credentials specified", 403)
            self.token_expiration = 0
            self.token_fail_reason = TokenFailReason["INVALID"].value
            self.token_status = 403

        return returned

    def _logout_handler(self, token_value: str = None) -> dict:
        if not token_value:
            token_value = self.token_value
        operation_id = "oauth2RevokeToken"
        target_url = f"{self.base_url}{[ep[2] for ep in AuthEndpoints if operation_id in ep[0]][0]}"
        if self.cred_format_valid:
            b64cred = generate_b64cred(self.creds["client_id"], self.creds["client_secret"])
            header_payload = {"Authorization": f"basic {b64cred}"}
            data_payload = {"token": f"{token_value}"}
            returned = perform_request(method="POST", endpoint=target_url, data=data_payload,
                                       headers=header_payload, verify=self.ssl_verify,
                                       proxy=self.proxy, timeout=self.timeout,
                                       user_agent=self.user_agent)
            self.token_expiration = 0
            self.token_value = False
        else:
            returned = generate_error_result("Invalid credentials specified", 403)

        return returned

    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
    #
    # These properties are present in all FalconAuth derivatives.
    # All properties defined here are by design IMMUTABLE.
    @property
    def token_expired(self) -> bool:
        """Return whether the token is ready to be renewed."""
        return (time.time() - self.token_time) >= (self.token_expiration - self.token_renew_window)

    @property
    def authenticated(self) -> bool:
        """Return if we are authenticated by retrieving the inverse of token_expired."""
        return not self.token_expired

    @property
    def cred_format_valid(self) -> bool:
        """Return a boolean creds dictionary is valid."""
        return ("client_id" in self.creds and "client_secret" in self.creds)

    # The default functionality of a FalconAuth object performs a token
    # refresh whenever a request is made for the auth_headers property.
    @property
    def auth_headers(self) -> Dict[str, str]:
        """Return a Bearer token baked into an Authorization header ready for an HTTP request."""
        if self.token_expired and self.refreshable:
            self.login()

        return {"Authorization": f"Bearer {self.token_value}"}