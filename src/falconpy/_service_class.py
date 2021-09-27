"""ServiceClass base class

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
from ._util import confirm_base_url
from .oauth2 import OAuth2 as FalconAuth

# pylint: disable=R0902  # Nine is reasonable


class ServiceClass:
    """Base class of all service classes. Contains the default __init__ method."""
    def __init__(self: object, auth_object: object = None,
                 creds: dict = None, base_url: str = "https://api.crowdstrike.com",
                 proxy: dict = None, **kwargs) -> object:
        """Instantiates the object, ingests authorization credentials,
        and initializes attributes.

        Keyword arguments:
        access_token -- Token string to use for all requests performed.
                        Mutually exclusive to all other authentication elements.
        auth_object - Properly authenticated instance of the OAuth2 Authentication service class.
        base_url -- CrowdStrike API URL to use for requests. [Default: US-1]
        ssl_verify -- Boolean specifying if SSL verification should be used. [Default: True]
        proxy -- Dictionary of proxies to be used for requests.
        timeout -- Float or tuple specifying timeouts to use for requests.
        creds -- Dictionary containing CrowdStrike API credentials.
                 Mutually exclusive to client_id / client_secret.
                 {
                     "client_id": "CLIENT_ID_HERE",
                     "client_secret": "CLIENT_SECRET_HERE"
                 }
        client_id -- Client ID for the CrowdStrike API. Mutually exclusive to creds.
        client_secret -- Client Secret for the CrowdStriek API. Mutually exclusive to creds.
        validate_payload -- Boolean specifying if body payloads should be validated.
                            Defaults to True.

        This method only accepts keywords to specify arguments.
        """
        access_token = kwargs.get("access_token", None)
        self.ssl_verify = kwargs.get("ssl_verify", True)
        self.timeout = kwargs.get("timeout", None)
        # Currently defaulting to validation enabled
        self.validate_payloads = kwargs.get("validate_payloads", True)
        self.refreshable = False
        client_id = kwargs.get("client_id", None)
        client_secret = kwargs.get("client_secret", None)
        if client_id and client_secret and not creds:
            # Passing client_id and client_secret will not
            # overwrite the contents of the creds dictionary
            creds = {
                "client_id": client_id,
                "client_secret": client_secret
            }
        if auth_object:
            self.auth_object = auth_object
            if not self.authenticated():
                _ = self.auth_object.token()
                if _["status_code"] == 201:
                    self.token = _["body"]["access_token"]
                    self.headers = {"Authorization": f"Bearer {self.token}"}
                else:
                    self.token = False
                    self.headers = {}
            else:
                self.token = self.auth_object.token_value
                self.headers = {"Authorization": f"Bearer {self.token}"}

            self.base_url = auth_object.base_url
            self.ssl_verify = auth_object.ssl_verify
            self.proxy = auth_object.proxy
            # At this point in time, you cannot override
            # the auth_object's timeout per class instance
            self.timeout = auth_object.timeout
            self.refreshable = True
        else:
            if creds:
                auth_object = FalconAuth(creds=creds,
                                         base_url=confirm_base_url(base_url),
                                         proxy=proxy,
                                         ssl_verify=self.ssl_verify,
                                         timeout=self.timeout
                                         )
                self.auth_object = auth_object
                _ = self.auth_object.token()
                if _["status_code"] == 201:
                    self.token = _["body"]["access_token"]
                    self.headers = {"Authorization": f"Bearer {self.token}"}
                else:
                    self.token = False
                    self.headers = {}
                self.refreshable = True
            else:
                self.auth_object = None
                self.headers = {"Authorization": f"Bearer {access_token}"}

            self.base_url = confirm_base_url(base_url)
            self.proxy = proxy

    def authenticated(self):
        """Returns the current authentication status."""
        result = None
        if self.auth_object:
            result = self.auth_object.authenticated()

        return result

    def token_expired(self):
        """Returns a boolean reflecting token expiration status."""
        result = None
        if self.auth_object:
            result = self.auth_object.token_expired()

        return result
