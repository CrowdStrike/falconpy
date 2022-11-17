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
from __future__ import annotations
import inspect

from typing import Type

from ._auth_object import FalconPyAuth
from .oauth2 import OAuth2

# pylint: disable=R0902  # Nine is reasonable
# pylint: disable=R0912  # Currently at 13 branches
# pylint: disable=R0915  # 51/50 statements. Allowing for now. 10.07.21 - jshcodes


class ServiceClass:
    """Base class of all service classes. Contains the default __init__ method."""

    def __init__(
        self: object,
        auth_object: FalconPyAuth = None,
        default_auth_object_class: Type[FalconPyAuth] = OAuth2,
        **kwargs,
    ):
        """Service Class base constructor.

        Instantiates the object, ingests authorization credentials,
        and initializes attributes.

        Keyword arguments:
        access_token: Token string to use for all requests performed.
                      Mutually exclusive to all other authentication elements.
        auth_object: Properly authenticated instance of an authentication backend, such as
                     the OAuth2 Authentication service class. Mutually exclusive to all other
                     authentication elements.
        ext_headers: Additional headers to be prepended to the default headers dictionary.
                     Dictionary.

        # to be removed
        base_url: CrowdStrike API URL to use for requests. [Default: US-1]
        ssl_verify: Boolean specifying if SSL verification should be used or string representing
                    the path to a CA_BUNDLE file or directory of trusted certificates.
                    Default: True
        proxy: Dictionary of proxies to be used for requests.
        timeout: Float or tuple specifying timeouts to use for requests.
        creds: Dictionary containing CrowdStrike API credentials.
               Mutually exclusive to client_id / client_secret.
               {
                   "client_id": "CLIENT_ID_HERE",
                   "client_secret": "CLIENT_SECRET_HERE",
                   "member_cid": "CHILD_CID_MSSP_ONLY"
               }
        client_id: Client ID for the CrowdStrike API. Mutually exclusive to creds.
        client_secret: Client Secret for the CrowdStrike API. Mutually exclusive to creds.
        member_cid: CID of the child account to authenticate to (MSSP only)
        validate_payload: Boolean specifying if body payloads should be validated.
                          Defaults to True.
        user_agent: User-Agent string to use for all requests made to the CrowdStrike API.
                    String. Defaults to crowdstrike-falconpy/VERSION.
        renew_window: Amount of time (in seconds) between now and the token expiration before
                      a refresh of the token is performed. Default: 120, Max: 1200
                      Values over 1200 will be reset to the maximum.

        This method only accepts keywords to specify arguments.
        """
        self.headers = kwargs.get("ext_headers", {})
        # Currently defaulting to validation enabled
        self.validate_payloads = kwargs.get("validate_payloads", True)
        self.auth_object: FalconPyAuth = None

        # Passing an auth_object will automatically ignore the rest of the parameters, as
        # this can be treated as an atomic collection of all authentication information.
        if auth_object:
            if issubclass(type(FalconPyAuth), auth_object):
                self.auth_object = auth_object
            else:
                # Look for an OAuth2 object as an attribute to the object they provided.
                for attr in [x for x in dir(auth_object) if "__" not in x]:
                    if attr == "auth_object":
                        self.auth_object = auth_object.auth_object

        else:
            # Get all the arguments of the authentication class's constructor
            auth_object_class_sig = inspect.signature(default_auth_object_class)
            auth_kwargs = {}
            for param in auth_object_class_sig.parameters:
                if param in kwargs:
                    auth_kwargs[param] = kwargs[param]

            self.auth_object = default_auth_object_class(**auth_kwargs)

    def authenticated(self) -> bool:
        """Return the current authentication status."""
        return self.auth_object.authenticated

    def token_expired(self) -> bool:
        """Return a boolean reflecting token expiration status."""
        return not self.authenticated
