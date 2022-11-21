"""ServiceClass base class.

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
from typing import Dict, Type
from ._auth_object import FalconAuth
from .oauth2 import OAuth2


class ServiceClass:
    """ServiceClass base class.
    
    Contains the default __init__ method leveraged by all service classes.

    This class is intended to be inherited by a class that represents a service collection.
    """

    def __init__(self: object,
                 auth_object: FalconAuth = None,
                 default_auth_object_class: Type[FalconAuth] = OAuth2,
                 **kwargs
                 ):
        """Service Class base constructor.

        Instantiates the object, ingests authorization credentials,
        and initializes attributes.

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
            Instance of ServiceClass derivative
        """
        self.ext_headers: dict = kwargs.get("ext_headers", {})
        # Currently defaulting to validation enabled
        self.validate_payloads: bool = kwargs.get("validate_payloads", True)
        self.auth_object: FalconAuth = None

        # An auth_object is treated as an atomic collection of all necessary authentication detail.
        if auth_object:
            if issubclass(type(auth_object), FalconAuth):
                self.auth_object = auth_object
            else:
                # Look for an OAuth2 object as an attribute to the object they provided.
                if hasattr(auth_object, "auth_object"):
                    if issubclass(type(auth_object.auth_object), FalconAuth):
                        self.auth_object = auth_object.auth_object
        else:
            # Get all constructor arguments for the authentication class.
            auth_kwargs = {
                param: kwargs[param]
                for param in inspect.signature(default_auth_object_class).parameters
                if param in kwargs
            }
            # Create an instance of the default auth object using the provided keywords.
            self.auth_object = default_auth_object_class(**auth_kwargs)

    def logout(self) -> dict:
        """Logout from the CrowdStrike API by revoking the current token."""
        return self.auth_object.logout()

    # Legacy properties
    def authenticated(self) -> bool:
        """Return the current authentication status."""
        return self.auth_object.authenticated

    def token_expired(self) -> bool:
        """Return a boolean reflecting token expiration status."""
        return self.auth_object.token_expired

    # Mutable properties
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
        """Allow the token_renew_window to be overriden."""
        self.auth_object.token_renew_window = value

    # Read only properties
    @property
    def headers(self) -> Dict[str, str]:
        """Provide a combination of headers needed for auth and additional supplied headers."""
        return {
            ** self.auth_object.auth_headers,
            ** self.ext_headers,
        }

    @property
    def token_status(self) -> int:
        """Provide the token_status from the auth_object."""
        return self.auth_object.token_status

    @property
    def token_fail_reason(self) -> str:
        """Error message received on token generation failure."""
        return self.auth_object.token_fail_reason

    @property
    def refreshable(self) -> bool:
        """Flag indicating if the token for this auth_object is refreshable."""
        return self.auth_object.refreshable
