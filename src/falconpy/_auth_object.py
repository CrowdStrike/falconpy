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
from abc import ABC, abstractmethod
from typing import Dict, Optional
from ._token_fail_reason import TokenFailReason
from ._util import generate_b64cred, autodiscover_region, perform_request, generate_error_result
from ._endpoint._oauth2 import _oauth2_endpoints as AuthEndpoints


class BaseFalconAuth(ABC):
    """Abstract class to provide an interface to the CrowdStrike Falcon OAuth2 API.

    This class does not implement a generic constructor and is not intended to be used by
    developers directly. You must work with a derivative of this class, such as a FalconAuth object.
    """
    #  ______  _______ _______ _______ _     _        _______
    #  |     \ |______ |______ |_____| |     | |         |
    #  |_____/ |______ |       |     | |_____| |_____    |

    #  _______ _______ _______ _     _  _____  ______  _______
    #  |  |  | |______    |    |_____| |     | |     \ |______
    #  |  |  | |______    |    |     | |_____| |_____/ ______|

    # The generic login and logout handlers must be individually defined by all
    # inheriting classes. The private methods defined here are used to allow for
    # easy overridding of login and logout processing by inheriting classes without
    # altering the parent handler method that may be leveraged by other inheriting
    # class types.
    @abstractmethod
    def _login_handler(self) -> dict or bool:
        """Login to the Falcon API by requesting a new token."""

    @abstractmethod
    def _logout_handler(self) -> dict or bool:
        """Log out of the Falcon API by revoking the current token."""

    @abstractmethod
    def login(self) -> dict or bool:
        """Generic login handler interface."""

    @abstractmethod
    def logout(self) -> dict or bool:
        """Generic logout handler interface."""

    #   _____   ______  _____   _____  _______  ______ _______ _____ _______ _______
    #  |_____] |_____/ |     | |_____] |______ |_____/    |      |   |______ |______
    #  |       |    \_ |_____| |       |______ |    \_    |    __|__ |______ ______|
    #
    # These properties are present within all BaseFalconAuth derivatives.
    @property
    @abstractmethod
    def auth_headers(self) -> Dict[str, str]:
        """Get a dictionary of headers that can authenticate an HTTP request."""

    @property
    @abstractmethod
    def authenticated(self) -> bool:
        """Read-only property to return whether authentication is successful."""

    @property
    @abstractmethod
    def token_expired(self) -> bool:
        """Read-only property that returns the current token expiration status."""

    @property
    @abstractmethod
    def cred_format_valid(self) -> bool:
        """Read-only property that returns a boolean if the creds dictionary is valid."""


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


class UberInterface(FalconAuth):
    """Uber Class specific interface."""

    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
    #
    # Attributes present only within the Uber Class.
    #
    # A dictionary of every available API operation provided by the library.
    commands: dict = {}

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    # Starting in v1.3.0, the Uber Class constructs itself leveraging the generic
    # FalconAuth constructor. This results in the Uber Class benefiting from a new
    # authentication style; Legacy / Token authentication.
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
                 ) -> "UberInterface":
        """Construct an instance of the UberInterface class."""
        super().__init__(base_url=base_url,
                         ssl_verify=ssl_verify,
                         timeout=timeout,
                         proxy=proxy,
                         user_agent=user_agent,
                         access_token=access_token,
                         creds=creds,
                         client_id=client_id,
                         client_secret=client_secret,
                         member_cid=member_cid,
                         renew_window=renew_window
                         )

    # _  _ ____ ___ _  _ ____ ___  ____
    # |\/| |___  |  |__| |  | |  \ [__
    # |  | |___  |  |  | |__| |__/ ___]
    #
    # Override the default login and logout handlers to
    # provide Uber Class-specific functionality.
    def _login_handler(self) -> bool:
        """Generate an authorization token."""
        super()._login_handler()

        return self.authenticated

    def _logout_handler(self) -> bool:
        """Revoke the current authorization token."""
        result = super()._logout_handler()

        return bool(result["status_code"] == 200)

    # _    ____ ____ ____ ____ _   _    _  _ ____ _  _ ___  _    ____ ____ ____
    # |    |___ | __ |__| |     \_/     |__| |__| |\ | |  \ |    |___ |__/ [__
    # |___ |___ |__] |  | |___   |      |  | |  | | \| |__/ |___ |___ |  \ ___]
    #
    # These handlers provide legacy Uber Class-specific functionality that will be
    # maintained for provide backwards compatibility purposes.
    def authenticate(self) -> bool:
        """Legacy Uber Class functionality handler.

        DEPRECATED
        ----
        Consider updating your code to leverage the login method.
        """
        return super().login()

    def deauthenticate(self) -> bool:
        """Legacy Uber Class functionality handler.

        DEPRECATED
        ----
        Consider updating your code to leverage the logout method.
        """
        return super().logout()

    def valid_cred_format(self) -> bool:
        """Legacy property to confirm credential dictionary format.
        
        DEPRECATED
        ----
        Consider updating your code to leverage the cred_format_valid property.
        """
        return self.cred_format_valid

    def headers(self) -> Dict[str, str]:
        """Legacy property getter for the current authorization headers.

        DEPRECATED
        ----
        Consider updating your code to leverage the auth_headers property.
        """
        return self.auth_headers

    @property
    def token(self) -> str:
        """Legacy attribute handler to return the token string.

        DEPRECATED
        ----
        Consider updating your code to leverage the token_value property.
        """
        return self.token_value
