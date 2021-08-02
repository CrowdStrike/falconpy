"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

oauth2 - Falcon OAuth2 Authentication API Interface Class

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
from ._util import perform_request, generate_b64cred
from ._endpoint._oauth2 import _oauth2_endpoints as Endpoints


class OAuth2:
    """ To create an instance of this class, you must pass a properly formatted JSON object containing your falcon
        client_id and falcon client_secret for the key you wish to use to connect to the API.

        Example:
        {
            "client_id": FALCON_CLIENT_ID,
            "client_secret": FALCON_CLIENT_SECRET
        }
    """
    # pylint: disable=too-many-instance-attributes,too-many-arguments
    def __init__(self: object, creds: dict, base_url: str = "https://api.crowdstrike.com",
                 ssl_verify: bool = True, proxy: dict = None, timeout: float or tuple = None):
        """
        Initializes the base class by ingesting credentials, the proxies dictionary and specifications
        for the base URL, SSL verification, and timeouts.
        """
        self.creds = creds
        self.base_url = base_url
        self.ssl_verify = ssl_verify
        self.timeout = timeout
        self.proxy = proxy
        self.token_expiration = 0
        self.token_renew_window = 20
        self.token_time = time.time()
        self.token_value = False
        self.token_expired = lambda: bool(
            (time.time() - self.token_time) >= (self.token_expiration - self.token_renew_window)
            )
        self.authenticated = lambda: not bool(self.token_expired())

    def token(self: object) -> dict:
        """
        Generates an authorization token.
        """
        operation_id = "oauth2AccessToken"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = {}
        data_payload = {
            'client_id': self.creds['client_id'],
            'client_secret': self.creds['client_secret']
        }
        if "member_cid" in self.creds:
            data_payload["member_cid"] = self.creds["member_cid"]
        returned = perform_request(method="POST", endpoint=target_url, data=data_payload, headers=header_payload,
                                   verify=self.ssl_verify, proxy=self.proxy, timeout=self.timeout)
        if returned["status_code"] == 201:
            self.token_expiration = returned["body"]["expires_in"]
            self.token_time = time.time()
            self.token_value = returned["body"]["access_token"]

        return returned

    def revoke(self: object, token: str) -> dict:
        """
        Revokes the specified authorization token.
        """
        operation_id = "oauth2RevokeToken"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = {'Authorization': 'basic {}'.format(
            generate_b64cred(self.creds["client_id"], self.creds["client_secret"])
            )}
        data_payload = {'token': '{}'.format(token)}
        returned = perform_request(method="POST", endpoint=target_url, data=data_payload, headers=header_payload,
                                   verify=self.ssl_verify, proxy=self.proxy, timeout=self.timeout)
        self.token_expiration = 0
        self.token_value = False

        return returned
