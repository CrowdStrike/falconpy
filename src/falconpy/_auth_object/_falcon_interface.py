"""API Interface base class.

This file contains the definition of the standard base class that provides
necessary functionality to authenticate to the CrowdStrike Falcon OAuth2 API.

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
import warnings
from logging import Logger, getLogger
from typing import Dict, Optional, Union
from ._base_falcon_auth import BaseFalconAuth
from ._bearer_token import BearerToken
from .._log import LogFacility
from .._constant import MIN_TOKEN_RENEW_WINDOW, MAX_TOKEN_RENEW_WINDOW
from ._interface_config import InterfaceConfiguration
from .._enum import TokenFailReason
from .._util import (
    autodiscover_region,
    perform_request,
    log_class_startup,
    login_payloads,
    logout_payloads
    )
from .._error import InvalidCredentials, NoAuthenticationMechanism


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
    _creds: Dict[str, str] = {}
    # Starting with v1.3.0 minimal python native logging is available. In order to reduce
    # potential impacts to developer configurations, this facility is extremely limited
    # and not implemented by default. (Meaning logs are not generated.)
    # To enable logging, pass the keyword "debug" with a value of True to the constructor.
    _log: LogFacility = LogFacility()
    # Our token is stored within a BearerToken object.
    _token: BearerToken = BearerToken()
    # Configuration detail for this interface.
    _config: InterfaceConfiguration = None
    # Pythonic behavior.
    _pythonic: bool = False

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    # The default constructor for all authentication objects. Ingests provided credentials
    # and sets the necessary class attributes based upon the authentication detail received.
    # pylint: disable=R0913,R0914
    def __init__(self,
                 access_token: Optional[Union[str, bool]] = False,
                 base_url: Optional[str] = "https://api.crowdstrike.com",
                 creds: Optional[Dict[str, str]] = None,
                 client_id: Optional[str] = None,
                 client_secret: Optional[str] = None,
                 member_cid: Optional[str] = None,
                 ssl_verify: Optional[bool] = True,
                 proxy: Optional[Dict[str, str]] = None,
                 timeout: Optional[Union[float, tuple]] = None,
                 user_agent: Optional[str] = None,
                 renew_window: Optional[int] = 120,
                 debug: Optional[bool] = False,
                 debug_record_count: Optional[int] = None,
                 sanitize_log: Optional[bool] = None,
                 pythonic: Optional[bool] = None
                 ) -> "FalconInterface":
        """Construct an instance of the FalconInterface class."""
        # Set the pythonic behavior mode.
        if isinstance(pythonic, bool):
            self._pythonic = pythonic
        # Setup our configuration object using the provided keywords.
        self.config: InterfaceConfiguration = InterfaceConfiguration(base_url=base_url,
                                                                     proxy=proxy,
                                                                     timeout=timeout,
                                                                     user_agent=user_agent,
                                                                     ssl_verify=ssl_verify
                                                                     )            # \ o /
        # ____ _  _ ___ _  _ ____ _  _ ___ _ ____ ____ ___ _ ____ _  _                |
        # |__| |  |  |  |__| |___ |\ |  |  | |    |__|  |  | |  | |\ |               / \
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
        # Credential Authentication (also powers Direct Authentication).
        self.creds: Dict[str, str] = creds
        # Set the token renewal window, ignored when using Legacy Authentication.
        self.renew_window: int = max(min(renew_window, MAX_TOKEN_RENEW_WINDOW),
                                     MIN_TOKEN_RENEW_WINDOW
                                     )
        # Legacy (Token) Authentication (fallback)
        if access_token:
            # Store this non-refreshable token, assuming it was just generated.
            self._token: BearerToken = BearerToken(access_token, 1799)

        # Log the creation of this object if debugging is enabled.
        if debug:
            # Ignored when debugging is disabled.
            _debug_record_count: int = debug_record_count if debug_record_count else None
            # Allow log sanitization to be overridden.
            _sanitize = sanitize_log if isinstance(sanitize_log, bool) else None
            # Logging facility for all classes using this interface, defaults to disabled.
            self._log: LogFacility = LogFacility(getLogger(__name__),
                                                 _debug_record_count,
                                                 _sanitize
                                                 )
            # Log the startup of this class.
            log_class_startup(self, self.log)

        try:
            if not self.cred_format_valid and not self.token_value:
                raise NoAuthenticationMechanism
        except NoAuthenticationMechanism as no_auth_mechanism:
            if pythonic:
                warnings.warn(no_auth_mechanism.message, NoAuthenticationMechanism, stacklevel=2)
            if self.log:
                self.log.warning(no_auth_mechanism.message)

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
        _returned_headers = {}
        try:
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
                        # Token generation was successful.
                        self._token = BearerToken(token_value=returned["body"]["access_token"],
                                                  expiration=returned["body"]["expires_in"],
                                                  status=201
                                                  )
                        # Cloud Region auto discovery.
                        self.base_url = autodiscover_region(self.base_url, returned)
                    else:
                        # Token generation failure, reset the current token and check for an error response.
                        self._token = BearerToken(status=returned["status_code"])
                        # Retrieve the list of errors, there should only be one item in the list.
                        error_list = returned["body"].get("errors", [])
                        if error_list:
                            self.bearer_token.fail_token(returned["status_code"],
                                                         error_list[0]["message"]
                                                         )
            else:
                if stateful:
                    self.bearer_token.fail_token(403, TokenFailReason["INVALID"])
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
                    self._token: BearerToken = BearerToken()
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
    def creds(self) -> Dict[str, str]:
        """Return the current credential dictionary."""
        return self._creds

    @creds.setter
    def creds(self, value: Dict[str, str]):
        self._creds = value

    @property
    def config(self) -> InterfaceConfiguration:
        """Return the interface configuration object for this interface."""
        return self._config

    @config.setter
    def config(self, value: InterfaceConfiguration):
        if not isinstance(value, InterfaceConfiguration):
            raise ValueError
        self._config = value

    @property
    def base_url(self) -> str:
        """Return the base URL for this interface from the configuration object."""
        return self._config.base_url

    @base_url.setter
    def base_url(self, value):
        self._config.base_url = value

    @property
    def ssl_verify(self) -> bool:
        """Return the SSL verification setting from the configuration object."""
        return self._config.ssl_verify

    @ssl_verify.setter
    def ssl_verify(self, value: bool):
        self._config.ssl_verify = value

    @property
    def proxy(self) -> Dict[str, str]:
        """Return the current proxy setting."""
        return self._config.proxy

    @proxy.setter
    def proxy(self, value: Dict[str, str]):
        self._config.proxy = value

    @property
    def user_agent(self) -> str:
        """Return the current user agent setting."""
        return self._config.user_agent

    @user_agent.setter
    def user_agent(self, value: str):
        self._config.user_agent = value

    @property
    def timeout(self) -> Union[int, tuple]:
        """Return the current timeout setting."""
        return self._config.timeout

    @timeout.setter
    def timeout(self, value: Union[int, tuple]):
        self._config.timeout = value

    @property
    def debug_record_count(self) -> int:
        """Return the current debug record count setting."""
        return self.log_facility.debug_record_count

    @debug_record_count.setter
    def debug_record_count(self, value: int):
        self.log_facility.debug_record_count = value

    @property
    def sanitize_log(self) -> bool:
        """Return the current log sanitization."""
        return self.log_facility.sanitize_log

    @sanitize_log.setter
    def sanitize_log(self, value):
        self.log_facility.sanitize_log = value

    # These properties provide reflection into the token object
    @property
    def bearer_token(self) -> BearerToken:
        """Return the bearer token object for this configuration."""
        return self._token

    @property
    def renew_window(self) -> int:
        """Return the current token renew window setting."""
        return self.bearer_token.renew_window

    @renew_window.setter
    def renew_window(self, value: int):
        self.bearer_token.renew_window = value

    @property
    def token_expiration(self) -> int:
        """Return the current expiration setting."""
        return self.bearer_token.expiration

    @token_expiration.setter
    def token_expiration(self, value: int):
        self.bearer_token.expiration = value

    @property
    def token_time(self) -> float:
        """Return the current token_time setting."""
        return self.bearer_token.token_time

    @token_time.setter
    def token_time(self, value: float):
        self.bearer_token.token_time = value

    @property
    def token_fail_reason(self) -> str:
        """Return the current fail_reason setting."""
        return self.bearer_token.fail_reason

    @token_fail_reason.setter
    def token_fail_reason(self, value: str):
        self.bearer_token.fail_reason = value

    @property
    def token_status(self) -> int:
        """Return the current status setting."""
        return self.bearer_token.status

    @token_status.setter
    def token_status(self, value: int):
        self.bearer_token.status = value

    @property
    def token_value(self) -> str:
        """Return the current value setting."""
        return self.bearer_token.value

    @token_value.setter
    def token_value(self, value: str):
        self.bearer_token.value = value

    # All properties defined here are by design IMMUTABLE.
    @property
    def refreshable(self) -> bool:
        """Return a boolean if this interface can automatically refresh tokens when they expire."""
        return self.cred_format_valid

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

    @property
    def log(self) -> Logger:
        """Return the logger from our log facility."""
        return self.log_facility.log

    @property
    def log_facility(self) -> LogFacility:
        """Return the entire log facility."""
        return self._log

    # The default functionality of a FalconInterface object performs a token refresh
    # whenever a request is made for the auth_headers property and the token is stale.
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

    @property
    def pythonic(self) -> bool:
        """Return a boolean if we are in a pythonic mode."""
        return self._pythonic

    @pythonic.setter
    def pythonic(self, value: bool):
        """Enable or disable pythonic mode."""
        self._pythonic = value
