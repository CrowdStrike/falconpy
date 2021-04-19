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


class ServiceClass:
    """ Base class of all service classes. Contains the default __init__ method. """
    def __init__(self: object, access_token: str = None, auth_object: object = None, creds: dict = None,
                 base_url: str = "https://api.crowdstrike.com", ssl_verify: bool = True) -> object:
        """ Instantiates the base class, ingests the authorization token,
            and initializes the headers and base_url global variables.
        """
        self.refreshable = False
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
            self.refreshable = True
        else:
            if creds:
                auth_object = FalconAuth(creds=creds)
                self.auth_object = auth_object
                _ = self.auth_object.token()
                if _["status_code"] == 201:
                    self.token = _["body"]["access_token"]
                    self.headers = {'Authorization': 'Bearer {}'.format(self.token)}
                else:
                    self.token = False
                    self.headers = {}
                self.base_url = base_url
                self.ssl_verify = ssl_verify
                self.refreshable = True
            else:
                self.auth_object = None
                self.headers = {'Authorization': 'Bearer {}'.format(access_token)}
                self.base_url = base_url
                self.ssl_verify = ssl_verify

    def authenticated(self):
        result = None
        if self.auth_object:
            result = self.auth_object.authenticated()

        return result

    def token_expired(self):
        result = None
        if self.auth_object:
            result = self.auth_object.token_expired()

        return result
