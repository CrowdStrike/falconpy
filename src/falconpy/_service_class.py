"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

_service_class - ServiceClass base class

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
from .oauth2 import OAuth2 as FalconAuth

# pylint: disable=R0902  # Eight is reasonable here


class ServiceClass:
    """
    Base class of all service classes. Contains the default __init__ method.
    """
    def __init__(self: object, auth_object: object = None,
                 creds: dict = None, base_url: str = "https://api.crowdstrike.com",
                 proxy: dict = None, **kwargs) -> object:
        """
        Instantiates the base class, ingests the authorization token,
        and initializes the headers and base_url global variables.
        """
        access_token, self.ssl_verify, self.timeout = self.parse_keywords(kwargs)
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
                    self.headers = {'Authorization': 'Bearer {}'.format(self.token)}
                else:
                    self.token = False
                    self.headers = {}
            else:
                self.token = self.auth_object.token_value
                self.headers = {'Authorization': 'Bearer {}'.format(self.token)}

            self.base_url = auth_object.base_url
            self.ssl_verify = auth_object.ssl_verify
            self.proxy = auth_object.proxy
            # At this point in time, you cannot override the auth_object's timeout per class
            self.timeout = auth_object.timeout
            self.refreshable = True
        else:
            if creds:
                auth_object = FalconAuth(creds=creds,
                                         base_url=base_url,
                                         proxy=proxy,
                                         ssl_verify=self.ssl_verify,
                                         timeout=self.timeout
                                         )
                self.auth_object = auth_object
                _ = self.auth_object.token()
                if _["status_code"] == 201:
                    self.token = _["body"]["access_token"]
                    self.headers = {'Authorization': 'Bearer {}'.format(self.token)}
                else:
                    self.token = False
                    self.headers = {}
                self.refreshable = True
            else:
                self.auth_object = None
                self.headers = {'Authorization': 'Bearer {}'.format(access_token)}

            self.base_url = base_url
            self.proxy = proxy

    def authenticated(self):
        """
        Authenticates using the credentials provided.
        """
        result = None
        if self.auth_object:
            result = self.auth_object.authenticated()

        return result

    def token_expired(self):
        """
        Returns a boolean reflecting token expiration status
        """
        result = None
        if self.auth_object:
            result = self.auth_object.token_expired()

        return result

    @staticmethod
    def parse_keywords(passed_keywords: dict):
        """
        Parses passed keywords to _init, setting defaults
        """
        access_token = None
        ssl_verify = True
        timeout = None
        for key, val in passed_keywords.items():
            if key.lower() == "access_token":
                access_token = val
            if key.lower() == "ssl_verify":
                ssl_verify = val
            if key.lower() == "timeout":
                timeout = val

        return access_token, ssl_verify, timeout
