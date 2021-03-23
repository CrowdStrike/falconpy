"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

api_complete.py - All-in-one CrowdStrike Falcon OAuth2 API harness

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
from ._util import perform_request, parse_id_list, generate_b64cred, _ALLOWED_METHODS, generate_error_result
from ._endpoint import api_endpoints


class APIHarness:
    """ This one does it all. It's like the One Ring with significantly fewer orcs. """

    def __init__(self: object, creds: dict, base_url: str = "https://api.crowdstrike.com",
                 ssl_verify: bool = True) -> object:
        """ Instantiates an instance of the base class, ingests credentials and the base URL and initializes global variables.
        """

        self.creds = creds
        self.base_url = base_url
        self.ssl_verify = ssl_verify
        self.token = False
        self.token_expiration = 0
        self.token_renew_window = 20
        self.token_time = time.time()
        self.token_expired = lambda: True if (
                                              time.time() - self.token_time
                                             ) >= (
                                                   self.token_expiration - self.token_renew_window
                                                  ) else False
        self.authenticated = False
        self.valid_cred_format = lambda: True if "client_id" in self.creds and "client_secret" in self.creds else False
        self.headers = lambda: {'Authorization': 'Bearer {}'.format(self.token)} if self.token else {}
        self.commands = api_endpoints

    def authenticate(self: object) -> bool:
        """ Generates an authorization token. """
        FULL_URL = self.base_url+'/oauth2/token'
        DATA = {}
        if self.valid_cred_format():
            DATA = {
                'client_id': self.creds['client_id'],
                'client_secret': self.creds['client_secret']
            }
        if "member_cid" in self.creds:
            DATA["member_cid"] = self.creds["member_cid"]

        result = perform_request(method="POST", endpoint=FULL_URL, data=DATA, headers={}, verify=self.ssl_verify)
        if result["status_code"] == 201:
            self.token = result["body"]["access_token"]
            self.token_expiration = result["body"]["expires_in"]
            self.token_time = time.time()
            self.authenticated = True
        else:
            self.authenticated = False

        return self.authenticated

    def deauthenticate(self: object) -> bool:
        """ Revokes the specified authorization token. """
        FULL_URL = str(self.base_url)+'/oauth2/revoke'
        HEADERS = {'Authorization': 'basic {}'.format(generate_b64cred(self.creds["client_id"], self.creds["client_secret"]))}
        DATA = {'token': '{}'.format(self.token)}
        revoked = False
        if perform_request(method="POST", endpoint=FULL_URL, data=DATA,
                           headers=HEADERS, verify=self.ssl_verify)["status_code"] == 200:
            self.authenticated = False
            self.token = False
            revoked = True
        else:
            revoked = False

        return revoked

    # NOTE: Not specifying datatypes for "ids" and "partition" parameters
    #       to allow developers to pass str / lists / integers as necessary
    def command(self: object, action: str = "", parameters: dict = {}, body: dict = {}, data: dict = {},
                headers: dict = {}, ids=None, partition=None, override: str = None, action_name: str = None,
                files: list = [], file_name: str = None, content_type: str = None):  # May return dict or object datatypes
        """ Checks token expiration, renewing when necessary, then performs the request. """
        if self.token_expired():
            self.authenticate()
        if override:
            CMD = [["Manual"] + override.split(",")]
        else:
            CMD = [a for a in self.commands if a[0] == action]
        if CMD:
            FULL_URL = self.base_url+"{}".format(CMD[0][2])
            if ids:
                ID_LIST = str(parse_id_list(ids)).replace(",", "&ids=")
                FULL_URL = FULL_URL.format(ID_LIST)
            if action_name:
                delim = "&" if "?" in FULL_URL else "?"
                FULL_URL = f"{FULL_URL}{delim}action_name={str(action_name)}"  # TODO: Additional action_name restrictions?
            if partition:
                FULL_URL = FULL_URL.format(str(partition))
            if file_name:
                delim = "&" if "?" in FULL_URL else "?"
                FULL_URL = f"{FULL_URL}{delim}file_name={str(file_name)}"
            HEADERS = self.headers()
            for item in headers:
                HEADERS[item] = headers[item]
            if content_type:
                HEADERS["Content-Type"] = str(content_type)
            DATA = data
            BODY = body
            PARAMS = parameters
            FILES = files
            if self.authenticated:
                METHOD = CMD[0][1].upper()
                if METHOD in _ALLOWED_METHODS:
                    returned = perform_request(method=METHOD, endpoint=FULL_URL, body=BODY, data=DATA,
                                               params=PARAMS, headers=HEADERS, files=FILES, verify=self.ssl_verify)
                else:
                    returned = generate_error_result(message="Invalid HTTP method specified.", code=405)
            else:
                returned = generate_error_result(message="Failed to issue token.", code=401)
        else:
            returned = generate_error_result(message="Invalid API operation specified.", code=418)

        return returned
