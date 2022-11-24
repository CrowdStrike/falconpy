"""Service Class generic base class.

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
import inspect
from abc import ABC, abstractmethod
from logging import Logger, getLogger
from typing import Dict, Type, Union, Optional
from .._auth_object import FalconInterface


class BaseServiceClass(ABC):
    """Base class for all Service Classes."""
    #  _______ _______ _______  ______ _____ ______  _     _ _______ _______ _______
    #  |_____|    |       |    |_____/   |   |_____] |     |    |    |______ |______
    #  |     |    |       |    |    \_ __|__ |_____] |_____|    |    |______ ______|
    #
    # These attributes are available within all derivatives of a Service Class.
    # ____ _  _ ___ _  _    ____ ___   _ ____ ____ ___
    # |__| |  |  |  |__|    |  | |__]  | |___ |     |
    # |  | |__|  |  |  |    |__| |__] _| |___ |___  |
    #
    # All Service Classes excluding OAuth2 contain a FalconInterface derivative
    # as an attribute (auth_object). This object can be shared between
    # instances of Service Classes, and is leveraged for all authentication
    # processing. Unlike the OAuth2 and Uber Class, regular Service Classes
    # do not maintain authentication detail outside of the auth_object.
    auth_object: FalconInterface = None
    # Service Classes can enable logging individually, allowing developers to
    # debug API activity for only that service collection within their code.
    _log: Union[Logger, bool] = None

    #  _______  _____  __   _ _______ _______  ______ _     _ _______ _______  _____   ______
    #  |       |     | | \  | |______    |    |_____/ |     | |          |    |     | |_____/
    #  |_____  |_____| |  \_| ______|    |    |    \_ |_____| |_____     |    |_____| |    \_

    def __init__(self: "BaseServiceClass",
                 auth_object: Optional[FalconInterface] = None,
                 default_auth_object_class: Optional[Type[FalconInterface]] = FalconInterface,
                 **kwargs
                 ):
        """Construct an instance of the base class."""
        # An auth_object is treated as an atomic collection.
        if auth_object:
            if issubclass(type(auth_object), FalconInterface):
                self.auth_object = auth_object
            else:
                # Easy Object Authentication
                # Look for an auth_object as an attribute to the object they
                # provided. This attribute must be a FalconInterface derivative.
                if hasattr(auth_object, "auth_object"):
                    if issubclass(type(auth_object.auth_object), FalconInterface):
                        self.auth_object = auth_object.auth_object
        else:
            # Get all constructor arguments for the default authentication class.
            auth_kwargs = {
                param: kwargs[param]
                for param in inspect.signature(default_auth_object_class).parameters
                if param in kwargs
            }
            # Create an instance of the default auth_object using the provided keywords.
            self.auth_object = default_auth_object_class(**auth_kwargs)

        if kwargs.get("debug", False) and not self.log:
            # Allow a Service Class to enable logging individually.
            self._log: Logger = getLogger(__name__.split(".")[0])
        if self.log and kwargs.get("debug", None) == False:
            # Allow a Service Class to disable logging individually.
            self._log: bool = False

    #  _______ _______ _______ _     _  _____  ______  _______
    #  |  |  | |______    |    |_____| |     | |     \ |______
    #  |  |  | |______    |    |     | |_____| |_____/ ______|
    #
    # The generic login and logout handlers must be individually defined by all
    # inheriting classes. The default functionality provided by the embedded
    # auth_object is a perfectly acceptable option for this, and is what is used
    # by the standard ServiceClass object.
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
    # These properties are present within all Service Class derivatives. These are
    # typically maintained within the underlying auth_object, but can be overridden
    # to implement additional functionality as necessary.

    # _  _ _  _ ___ ____ ___  _    ____
    # |\/| |  |  |  |__| |__] |    |___
    # |  | |__|  |  |  | |__] |___ |___
    #
    # Changes made to these properties will effect the underlying auth_object
    # and all Service Classes that happen to be sharing the same auth_object.
    @property
    def base_url(self) -> str:
        """Provide the base_url to code that reads it straight from the service class."""
        return self.auth_object.base_url

    @base_url.setter
    def base_url(self, value: str):
        """Set the base_url in the underlying auth_object."""
        self.auth_object.base_url = value

    @property
    def ssl_verify(self) -> bool:
        """Provide the ssl_verify value to legacy code."""
        return self.auth_object.ssl_verify

    @ssl_verify.setter
    def ssl_verify(self, value: bool):
        """Allow code to flip the underlying SSL verify flag via the this class."""
        self.auth_object.ssl_verify = value

    @property
    def proxy(self) -> dict:
        """Provide the proxy from the auth_object."""
        return self.auth_object.proxy

    @proxy.setter
    def proxy(self, value: dict):
        """Allow the proxy to be overriden."""
        self.auth_object.proxy = value

    @property
    def timeout(self) -> int:
        """Provide the timeout from the auth_object."""
        return self.auth_object.timeout

    @timeout.setter
    def timeout(self, value: int):
        """Allow the timeout to be overriden."""
        self.auth_object.timeout = value

    @property
    def token_renew_window(self) -> int:
        """Provide the token_renew_window from the auth_object."""
        return self.auth_object.token_renew_window

    @token_renew_window.setter
    def token_renew_window(self, value: int):
        """Allow the token_renew_window to be changed."""
        self.auth_object.token_renew_window = value

    @property
    def user_agent(self) -> int:
        """Provide the user_agent from the auth_object."""
        return self.auth_object.user_agent

    @user_agent.setter
    def user_agent(self, value: int):
        """Allow the user_agent to be overriden."""
        self.auth_object.user_agent = value

    # _ _  _ _  _ _  _ ___ ____ ___  _    ____
    # | |\/| |\/| |  |  |  |__| |__] |    |___
    # | |  | |  | |__|  |  |  | |__] |___ |___
    #
    # These properties cannot be changed in the base implementation of a Service Class.
    @property
    def log(self) -> Logger:
        if self._log:
            returned = self._log
        elif self._log == False:
            # Logging is disabled for this Service Class.
            returned = None
        else:
            returned = self.auth_object.log

        return returned

    @property
    def headers(self) -> Dict[str, str]:
        """Provide a complete set of request headers."""
        return {**self.auth_object.auth_headers}

    @property
    def token_status(self) -> int:
        """Provide the current token_status."""
        return self.auth_object.token_status

    @property
    def token_fail_reason(self) -> str:
        """Error message received on token generation failure."""
        return self.auth_object.token_fail_reason

    @property
    def refreshable(self) -> bool:
        """Flag indicating if the token for this auth_object is refreshable."""
        return self.auth_object.refreshable