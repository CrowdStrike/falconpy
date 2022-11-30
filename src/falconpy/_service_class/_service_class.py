"""Service Class generic class.

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
from typing import Dict, Type, Any, Optional
from ._base_service_class import BaseServiceClass
from .._auth_object import FalconInterface
from .._util import log_class_startup
from ..oauth2 import OAuth2


class ServiceClass(BaseServiceClass):
    r"""This is the Falconpy standard Service Class base class.

    This class inherits all functionality provided by the BaseServiceClass object.
    All current Service Classes (as of v1.3.0) inherit from this base class.

    ┌──────────────────────┐
    │     Encapsulated     ├─── Attributes
    │  Service Base Class  ├─── Constructor (__init__)
    │                      ├─── Methods (helpers)
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
    # auth_object but maintain different connection handling configurations.
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
                 auth_object: Optional[FalconInterface or OAuth2] = None,
                 default_auth_object_class: Optional[Type[FalconInterface]] = OAuth2,
                 **kwargs
                 ):
        """Service Class base constructor.

        Instantiates the object, ingests authorization, and initializes attributes.

        Keyword arguments
        ----
        access_token : str
            Token string to use for all requests performed.
            Mutually exclusive to all other authentication elements.
        auth_object : object (FalconInterface derivative)
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

        # Log the creation of this Service Class if debugging is enabled.
        if self.log:
            log_class_startup(self, self.log)

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
    def renew_window(self) -> int:
        """Provide the renew_window from the auth_object."""
        return self.auth_object.renew_window

    @renew_window.setter
    def renew_window(self, value: int):
        """Allow the renew_window to be changed.

        Changing this value will impact the renew window for all classes
        using this auth_object.
        """
        self.auth_object.renew_window = value

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
