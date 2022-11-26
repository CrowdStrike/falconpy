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
from logging import Logger, getLogger
from typing import Dict, Optional, Union
from ._base_falcon_auth import BaseFalconAuth
from .._enum import TokenFailReason
from .._util import (
    autodiscover_region,
    perform_request,
    log_class_startup,
    login_payloads,
    logout_payloads
    )
from .._error import InvalidCredentials


# pylint: disable=R0902
class FalconInterface(BaseFalconAuth):
    """Standard Falcon API interface used by Service Classes."""

    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
    #
    # These attributes are present in all FalconInterface objects, regardless if we are referring
    # to APIHarness, OAuth2 or custom inheriting classes.
    #
    # The default credential dictionary, where the client_id and client_secret are stored.
    creds: Dict[str, str] = {}
    # Starting with v1.3.0 minimal python native logging is available. In order
    # to reduce potential impacts to customer configurations, this facility is
    # extremely limited and not implemented by default. (Meaning logs are not generated.)
    # To enable logging, pass the keyword "debug" with a value of True to the constructor.
    log: Optional[Logger] = None
    _debug_record_count: int = None
    _sanitize: bool = True
    _proxy: dict = None
    _timeout: int or float = None
    _renew_window: int = 120
    _user_agent: str = None
    # Flag indicating if we have the necessary information to automatically refresh the token.
    refreshable: bool = True
    # Integer specifying the amount of time remaining before the token expires (in seconds).
    token_expiration: int = 0
    # Float indicating the moment in time that the token was generated (timestamp).
    token_time: float = time.time()
    # String containing the error message received from the API when token generation failed.
    token_fail_reason: Optional[str] = None
    # Integer representing the HTTP status code received when generating the token.
    token_status: Optional[int] = None

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    # The default constructor for all authentication objects. Ingests provided credentials
    # and sets the necessary class attributes based upon the authentication detail received.
    # pylint: disable=R0913
    def __init__(self,
                 access_token: Optional[Union[str, bool]] = False,
                 base_url: Optional[str] = "https://api.crowdstrike.com",
                 creds: Optional[dict] = None,
                 client_id: Optional[str] = None,
                 client_secret: Optional[str] = None,
                 member_cid: Optional[str] = None,
                 ssl_verify: Optional[bool] = True,
                 proxy: Optional[dict] = None,
                 timeout: Optional[Union[float, tuple]] = None,
                 user_agent: Optional[str] = None,
                 renew_window: Optional[int] = 120,
                 debug: Optional[bool] = False,
                 debug_record_count: Optional[int] = None,
                 sanitize_log: Optional[bool] = None
                 ) -> "FalconInterface":
        """Construct an instance of the FalconInterface class."""
        self.base_url: str = base_url
        self.ssl_verify: bool = ssl_verify
        self._timeout: float or tuple = timeout
        self._proxy: Dict[str, str] = proxy
        self._user_agent: str = user_agent
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
        self.token_value: Optional[Union[str, bool]] = access_token
        if access_token:
            # Store this non-refreshable token
            self.token_value = access_token
            # We do not have API credentials, disable token refresh.
            self.refreshable = False
            # Assume the token was just generated.
            self.token_expiration = 1799

        # Set the token renewal window, ignored when using Legacy Authentication.
        self._renew_window: int = max(min(renew_window, 1200), 120)
        # Ignored when debugging is disabled
        self._debug_record_count: int = debug_record_count
        # Allow log sanitization to be overridden
        if isinstance(sanitize_log, bool):
            self._sanitize = sanitize_log
        # Log the creation of this object if debugging is enabled.
        if debug:
            self.log: Logger = getLogger(__name__.split(".", maxsplit=1)[0])
            log_class_startup(self, self.log)

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
    def _login_handler(self, stateful: bool = True) -> dict:
        """Login by requesting a new token.

        This method can also be leveraged to generate tokens without impacting authorization state.
        """
        def _token_failure(fail_reason: str, status: int):
            """Update the authentication status updater (failure conditions only)."""
            self.token_expiration = 403
            self.token_status = status
            self.token_fail_reason = fail_reason
        _returned_headers = {}
        try:  # pylint: disable=R1702
            if self.cred_format_valid:
                operation, target_url, data_payload = login_payloads(self.creds, self.base_url)
                # Log the call to this operation if debugging is enabled.
                if self.log:
                    self.log.debug("OPERATION: %s", operation)
                returned = perform_request(method="POST", endpoint=target_url, data=data_payload,
                                           headers={}, verify=self.ssl_verify, proxy=self.proxy,
                                           timeout=self.timeout, user_agent=self.user_agent,
                                           log_util=self.log, authenticating=True,
                                           sanitize=self.sanitize_log
                                           )
                _returned_headers = returned["headers"]
                if stateful:
                    self.token_status = returned["status_code"]
                    if self.token_status == 201:
                        self.token_expiration = returned["body"]["expires_in"]
                        self.token_time = time.time()
                        self.token_value = returned["body"]["access_token"]
                        self.token_fail_reason = None
                        # Cloud Region auto discovery
                        self.base_url = autodiscover_region(self.base_url, returned)
                    else:
                        self.token_expiration = 0  # Aligning to Uber class functionality
                        if "errors" in returned["body"]:
                            if returned["body"]["errors"]:
                                self.token_fail_reason = returned["body"]["errors"][0]["message"]
            else:
                if stateful:
                    _token_failure(TokenFailReason["INVALID"], 403)
                raise InvalidCredentials(headers=_returned_headers)

        except InvalidCredentials as bad_creds:
            returned = bad_creds.result
            if self.log:
                self.log.error(bad_creds.message)

        return returned

    def _logout_handler(self, token_value: str = None, stateful: bool = True) -> dict:
        """Log out by revoking the current token.

        This method can also be leveraged to revoke other tokens.
        """
        try:
            if self.cred_format_valid:
                if not token_value:
                    token_value = self.token_value
                operation, target_url, data_payload, header_payload = logout_payloads(
                    creds=self.creds,
                    base=self.base_url,
                    token_val=token_value
                    )
                # Log the call to this operation if debugging is enabled.
                if self.log:
                    self.log.debug("OPERATION: %s", operation)
                returned = perform_request(method="POST", endpoint=target_url, data=data_payload,
                                           headers=header_payload, verify=self.ssl_verify,
                                           proxy=self.proxy, timeout=self.timeout,
                                           user_agent=self.user_agent, log_util=self.log,
                                           sanitize=self.sanitize_log
                                           )
                if stateful:
                    self.token_expiration = 0
                    self.token_value = False
            else:
                raise InvalidCredentials
        except InvalidCredentials as bad_creds:
            returned = bad_creds.result
            if self.log:
                self.log.error(bad_creds.message)

        return returned

    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
    #
    # These properties are present in all FalconInterface derivatives.
    @property
    def proxy(self) -> dict:
        """Return the current proxy setting."""
        return self._proxy

    @proxy.setter
    def proxy(self, value: dict):
        self._proxy = value

    @property
    def user_agent(self) -> str:
        """Return the current user agent setting."""
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value: str):
        self._user_agent = value

    @property
    def renew_window(self) -> int:
        """Return the current token renew window setting."""
        return self._renew_window

    @renew_window.setter
    def renew_window(self, value: int):
        self._renew_window = value

    @property
    def timeout(self) -> dict:
        """Return the current timeout setting."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Union[int, float]):
        self._timeout = value

    @property
    def debug_record_count(self) -> int:
        """Return the current debug record count setting."""
        return self._debug_record_count

    @debug_record_count.setter
    def debug_record_count(self, value: int):
        self._debug_record_count = value

    @property
    def sanitize_log(self) -> bool:
        """Return the current log sanitization."""
        _sanitize = True
        if isinstance(self._sanitize, bool):
            _sanitize = self._sanitize
        return _sanitize

    @sanitize_log.setter
    def sanitize_log(self, value):
        self._sanitize = value

    # All properties defined here are by design IMMUTABLE.
    @property
    def token_expired(self) -> bool:
        """Return whether the token is ready to be renewed."""
        return (time.time() - self.token_time) >= (self.token_expiration - self.renew_window)

    @property
    def authenticated(self) -> bool:
        """Return if we are authenticated by retrieving the inverse of token_expired."""
        return not self.token_expired

    @property
    def cred_format_valid(self) -> bool:
        """Return a boolean that the creds dictionary is valid."""
        return bool("client_id" in self.creds and "client_secret" in self.creds)

    # The default functionality of a FalconInterface object performs a token
    # refresh whenever a request is made for the auth_headers property.
    @property
    def auth_headers(self) -> Dict[str, str]:
        """Return a Bearer token baked into an Authorization header ready for an HTTP request."""
        if self.token_expired and self.refreshable:
            self.login()

        return {"Authorization": f"Bearer {self.token_value}"}

    @property
    def debug(self) -> bool:
        """Return a boolean if we are in a debug mode."""
        return bool(self.log)
