"""Service Class generic classes.

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
from typing import Dict, Type, Any, Optional
from ._auth_object import FalconAuth
from .oauth2 import OAuth2


class BaseServiceClass(ABC):
    """Base class for all Service Classes."""

    #  _______ _     _ _______ _     _        _____  ______  _____ _______ _______ _______
    #  |_____| |     |    |    |_____|       |     | |_____]   |   |______ |          |
    #  |     | |_____|    |    |     |       |_____| |_____] __|   |______ |_____     |

    # All Service Classes contain a FalconAuth derivative as an attribute.
    # This object can be shared between instances of Service Classes, and
    # is leveraged for all authentication processing. Unlike the Uber Class,
    # Service Classes maintain no authentication detail within the class.
    auth_object: FalconAuth = None

    #  _______  _____  __   _ _______ _______  ______ _     _ _______ _______  _____   ______
    #  |       |     | | \  | |______    |    |_____/ |     | |          |    |     | |_____/
    #  |_____  |_____| |  \_| ______|    |    |    \_ |_____| |_____     |    |_____| |    \_

    def __init__(self: "BaseServiceClass",
                 auth_object: Optional[FalconAuth] = None,
                 default_auth_object_class: Optional[Type[FalconAuth]] = FalconAuth,
                 **kwargs
                 ):
        """Construct an instance of the base class."""
        # An auth_object is treated as an atomic collection.
        if auth_object:
            if issubclass(type(auth_object), FalconAuth):
                self.auth_object = auth_object
            else:
                # Easy Object Authentication
                # Look for an auth_object as an attribute to the object they
                # provided. This attribute must be a FalconAuth derivative.
                if hasattr(auth_object, "auth_object"):
                    if issubclass(type(auth_object.auth_object), FalconAuth):
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

    #  ______  _______ _______ _______ _     _        _______
    #  |     \ |______ |______ |_____| |     | |         |
    #  |_____/ |______ |       |     | |_____| |_____    |

    #  _______ _______ _______ _     _  _____  ______  _______
    #  |  |  | |______    |    |_____| |     | |     \ |______
    #  |  |  | |______    |    |     | |_____| |_____/ ______|

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

    #  _______ _     _ _______ _______ ______         _______
    #  |  |  | |     |    |    |_____| |_____] |      |______
    #  |  |  | |_____|    |    |     | |_____] |_____ |______
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

    #  _____ _______ _______ _     _ _______ _______ ______         _______
    #    |   |  |  | |  |  | |     |    |    |_____| |_____] |      |______
    #  __|__ |  |  | |  |  | |_____|    |    |     | |_____] |_____ |______
    #
    # These properties cannot be changed in the base implementation of a Service Class.
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


class ServiceClass(BaseServiceClass):
    r"""This is the Falconpy standard Service Class base class.

    This class inherits all functionality provided by the BaseServiceClass object.
    All current Service Classes (as of v1.3.0) inherit from this base class.

    ┌──────────────────────┐
    │     Encapsulated     ├─── Attributes
    │      Base Class      ├─── Constructor (__init__)
    │    ______________    ├─── Properties
    └──/│ Inherited by │\──┘
      /─┴──────────────┴─\
      │ Service  Classes ├─── Methods (API operations)
      └──────────────────┘

    This class is intended to be inherited by a class that represents a
    CrowdStrike API service collection.
    """
    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
    #
    # Extended headers that can be set on a Service Class and provided
    # with every request to the CrowdStrike API. These do not override
    # authorization headers.
    ext_headers: Dict[str, Any] = {}
    # Minimal payload validation is included in a few Service Classes.
    # This defaults to True but is not heavily used as ingested keywords
    # are reviewed by the parameter and body payload abstraction handlers.
    # Currently retained as we may leverage the functionality to provide
    # expanded required value validation in future versions.
    validate_payloads: bool = True
    # These private attributes are used to store instantiated class-specific
    # settings for the proxy, timeout and user_agent properties. This results
    # in our being able to use multiple Service Classes that share the same
    # auth_object but maintain different values for these properties.
    _override_proxy: Dict[str, str] = None
    _override_timeout: int = None
    _override_user_agent: str = None

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    # Override the default auth_object class to be our extended Service Class
    # object (OAuth2). Implement extended headers and payload validation and
    # provide a solution for maintaining instantiated class specific properties.
    #
    def __init__(self: "ServiceClass",
                 auth_object: Optional[FalconAuth or OAuth2] = None,
                 default_auth_object_class: Optional[Type[FalconAuth]] = OAuth2,
                 **kwargs
                 ):
        """Service Class base constructor.

        Instantiates the object, ingests authorization, and initializes attributes.

        Keyword arguments
        ----
        access_token : str
            Token string to use for all requests performed.
            Mutually exclusive to all other authentication elements.
        auth_object : object (FalconAuth derivative)
            Properly authenticated instance of an authentication backend,
            such as the OAuth2 Service Class.
        base_url : str
            CrowdStrike API URL to use for requests. [Default: US-1]
        ext_headers : dict
            Additional headers to be prepended to the default headers dictionary.
        ssl_verify : bool
            Flag specifying if SSL verification should be used. [Default: True]
        proxy : dict
            Dictionary of proxies to be used for requests.
        timeout : float or tuple
            Timeouts to use for requests.
        creds : dict
            Dictionary containing CrowdStrike API credentials.
            Mutually exclusive to client_id / client_secret.
            {
                "client_id": "CLIENT_ID_HERE",
                "client_secret": "CLIENT_SECRET_HERE",
                "member_cid": "CHILD_CID_MSSP_ONLY"
            }
        client_id : str
            Client ID for the CrowdStrike API. Mutually exclusive to creds.
        client_secret : str
            Client Secret for the CrowdStrike API. Mutually exclusive to creds.
        member_cid : str
            CID of the child account to authenticate to (MSSP only)
        validate_payload : bool
            Flag specifying if body payloads should be validated. Defaults to True.
        user_agent : str
            User-Agent string to use for all requests made to the CrowdStrike API.
            Defaults to crowdstrike-falconpy/VERSION.
        renew_window : int
            Amount of time (in seconds) between now and the token expiration before
            a refresh of the token is performed. Default: 120, Max: 1200
            Values over 1200 will be reset to the maximum.

        Arguments
        ----
        This method only accepts keywords to specify arguments.

        Returns
        ----
        class
            Instance of a ServiceClass derivative.
        """
        super().__init__(auth_object=auth_object,
                         default_auth_object_class=default_auth_object_class,
                         **kwargs
                         )
        self.ext_headers: dict = kwargs.get("ext_headers", {})
        # Currently defaulting to validation enabled
        self.validate_payloads: bool = kwargs.get("validate_payloads", True)

        # The following properties can be overridden per Service Class.
        for item in ["proxy", "timeout", "user_agent"]:
            if kwargs.get(item, None) is not None:
                setattr(self, f"_override_{item}", kwargs.get(item))

    # _  _ ____ ___ _  _ ____ ___  ____
    # |\/| |___  |  |__| |  | |  \ [__
    # |  | |___  |  |  | |__| |__/ ___]
    #
    # Provide our required login and logout method handlers.
    def login(self) -> dict:
        """Login to the CrowdStrike API by requesting a new token."""
        return self.auth_object.login()

    def logout(self) -> dict:
        """Logout from the CrowdStrike API by revoking the current token."""
        return self.auth_object.logout()

    # Legacy property getters maintained for backwards functionality.
    def authenticated(self) -> bool:
        """Return the current authentication status."""
        return self.auth_object.authenticated

    def token_expired(self) -> bool:
        """Return a boolean reflecting token expiration status."""
        return self.auth_object.token_expired

    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
    #
    # Allow these mutable properties to be set per Service Class in memory.
    @property
    def proxy(self) -> dict:
        """Provide the proxy from the auth_object if it's not been set."""
        if self._override_proxy:
            returned = self._override_proxy
        else:
            returned = self.auth_object.proxy

        return returned

    @proxy.setter
    def proxy(self, value: dict):
        """Allow the proxy to be changed for this instance of the class."""
        self._override_proxy = value

    @property
    def timeout(self) -> int:
        """Provide the timeout from the auth_object if it's not been set."""
        if self._override_timeout:
            returned = self._override_timeout
        else:
            returned = self.auth_object.timeout

        return returned

    @timeout.setter
    def timeout(self, value: int):
        """Allow the timeout to be changed for this instance of the class."""
        self._override_timeout = value

    @property
    def token_renew_window(self) -> int:
        """Provide the token_renew_window from the auth_object."""
        return self.auth_object.token_renew_window

    @token_renew_window.setter
    def token_renew_window(self, value: int):
        """Allow the token_renew_window to be changed.
        
        Changing this value will impact the renew window for all classes
        using this auth_object.
        """
        self.auth_object.token_renew_window = value

    @property
    def user_agent(self) -> int:
        """Provide the user_agent from the auth_object if it's not been set."""
        if self._override_user_agent:
            returned = self._override_user_agent
        else:
            returned = self.auth_object.user_agent

        return returned

    @user_agent.setter
    def user_agent(self, value: int):
        """Allow the user_agent to be changed for this instance of the class."""
        self._override_user_agent = value

    # Override the headers read only property to inject our ext_headers.
    # The Uber Class accomplishes this functionality differently.
    @property
    def headers(self) -> Dict[str, str]:
        """Provide a complete set of request headers."""
        return {
            ** self.auth_object.auth_headers,
            ** self.ext_headers
        }
