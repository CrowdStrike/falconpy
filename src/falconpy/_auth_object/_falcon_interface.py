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
from .._constant import MAX_DEBUG_RECORDS
from .._enum import TokenFailReason
from .._util import (
    autodiscover_region,
    perform_request,
    generate_error_result,
    login_payloads,
    logout_payloads
    )


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
    debug_record_count: int = MAX_DEBUG_RECORDS
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
                 debug_record_count: Optional[int] = 100
                 ) -> "FalconInterface":
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
        # Ignored when debugging is disabled
        self.debug_record_count: int = debug_record_count
        # Log the creation of this object if debugging is enabled.
        if debug:
            self.log: Logger = getLogger(__name__.split(".")[0])
            self.log.debug("CREATED: %s interface class", self.__class__.__name__)
            self.log.debug("CONFIG: Base URL set to %s", self.base_url)
            self.log.debug("CONFIG: SSL verification is set to %s", str(self.ssl_verify))
            self.log.debug("CONFIG: Timeout set to %s seconds", str(self.timeout))
            self.log.debug("CONFIG: Proxy dictionary: %s", str(self.proxy))
            self.log.debug("CONFIG: User-Agent string set to: %s", self.user_agent)
            self.log.debug("CONFIG: Token renewal window set to %s seconds", str(self.token_renew_window))
            self.log.debug("CONFIG: Maximum number of records to log: %s", self.debug_record_count)
        

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
        """Default login handler."""
        def _token_failure(fail_reason: str, status: int):
            """Generic authentication status updater (failure conditions only)."""
            self.token_expiration = 0
            self.token_status = status
            self.token_fail_reason = fail_reason
            
        if self.cred_format_valid:
            operation, target_url, data_payload = login_payloads(self.creds, self.base_url)
            # Log the call to this operation if debugging is enabled.
            if self.log:
                self.log.debug("OPERATION: %s", operation)
            returned = perform_request(method="POST", endpoint=target_url, data=data_payload,
                                       headers={}, verify=self.ssl_verify,
                                       proxy=self.proxy, timeout=self.timeout,
                                       user_agent=self.user_agent, log_util=self.log)

            if isinstance(returned, dict):  # Issue 433
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
                returned = generate_error_result("Unexpected API response received", 403)
                if stateful:
                    _token_failure(TokenFailReason["UNEXPECTED"], 403)
        else:
            returned = generate_error_result("Invalid credentials specified", 403)
            if stateful:
                _token_failure(TokenFailReason["INVALID"], 403)

        return returned

    def _logout_handler(self, token_value: str = None, stateful: bool = True) -> dict:
        """Default logout handler."""
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
                                       user_agent=self.user_agent, log_util=self.log)
            if stateful:
                self.token_expiration = 0
                self.token_value = False
        else:
            returned = generate_error_result("Invalid credentials specified", 403)

        return returned

    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
    #
    # These properties are present in all FalconInterface derivatives.
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

    # The default functionality of a FalconInterface object performs a token
    # refresh whenever a request is made for the auth_headers property.
    @property
    def auth_headers(self) -> Dict[str, str]:
        """Return a Bearer token baked into an Authorization header ready for an HTTP request."""
        if self.token_expired and self.refreshable:
            self.login()

        return {"Authorization": f"Bearer {self.token_value}"}