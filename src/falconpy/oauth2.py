"""Falcon OAuth2 Authentication API Interface Class.

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
import time
from ._util import perform_request, generate_b64cred, confirm_base_region
from ._util import confirm_base_url, generate_error_result
from ._endpoint._oauth2 import _oauth2_endpoints as Endpoints


class OAuth2:
    """To create an instance of this class, you must pass your client_id and client_secret.

    OR a properly formatted dictionary containing your client_id and client_secret
    for the key you wish to use to connect to the API.

    Credential dictionary example:
    {
        "client_id": FALCON_CLIENT_ID,
        "client_secret": FALCON_CLIENT_SECRET
    }
    """

    # pylint: disable=too-many-instance-attributes,too-many-arguments
    def __init__(self: object, base_url: str = "https://api.crowdstrike.com",
                 ssl_verify: bool = True, proxy: dict = None, timeout: float or tuple = None,
                 creds: dict = None, client_id: str = None, client_secret: str = None,
                 user_agent: str = None, member_cid: str = None, renew_window: int = 120):
        """Class constructor.

        Initializes the base class by ingesting credentials,
        the proxies dictionary and specifications
        for the base URL, SSL verification, and timeouts.

        Keyword arguments:
        base_url: CrowdStrike API URL to use for requests. [Default: US-1]
        ssl_verify: Boolean specifying if SSL verification should be used. [Default: True]
        proxy: Dictionary of proxies to be used for requests.
        timeout: Float or tuple specifying timeouts to use for requests.
        creds: Dictionary containing CrowdStrike API credentials.
               Mutually exclusive to client_id / client_secret.
        client_id: Client ID for the CrowdStrike API. Mutually exclusive to creds.
        client_secret: Client Secret for the CrowdStrike API. Mutually exclusive to creds.
        member_cid: Child CID to connect to. Mutually exclusive to creds.
        renew_window: Amount of time (in seconds) between now and the token expiration before
                      a refresh of the token is performed. Default: 120, Max: 1200
                      Values over 1200 will be reset to the maximum.

        This method only supports keywords to specify arguments.
        """
        if client_id and client_secret and not creds:
            creds = {
                "client_id": client_id,
                "client_secret": client_secret
            }
            # Have to pass member_cid the same way you pass client_id / secret
            # If you use a creds dictionary, pass the member_cid there instead
            if member_cid:
                creds["member_cid"] = member_cid
        elif not creds:
            creds = {}

        self.creds = creds
        self.base_url = confirm_base_url(base_url)
        self.ssl_verify = ssl_verify
        self.timeout = timeout
        self.proxy = proxy
        self.user_agent = user_agent
        self.token_expiration = 0
        # Maximum renewal window is 20 minutes, Minimum is 2 minutes
        self.token_renew_window = max(min(renew_window, 1200), 120)
        self.token_time = time.time()
        self.token_value = False
        self.token_expired = lambda: bool(
            (time.time() - self.token_time) >= (self.token_expiration - self.token_renew_window)
            )
        self.token_fail_reason = None
        self.token_status = None
        self.authenticated = lambda: not bool(self.token_expired())

    def token(self: object) -> dict:
        """Generate an authorization token.

        This method does not accept arguments or keywords.

        Returns: dict object containing API response.
        """
        operation_id = "oauth2AccessToken"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = {}
        if "client_id" in self.creds and "client_secret" in self.creds:
            data_payload = {
                'client_id': self.creds['client_id'],
                'client_secret': self.creds['client_secret']
            }
            if "member_cid" in self.creds:
                data_payload["member_cid"] = self.creds["member_cid"]
            returned = perform_request(method="POST", endpoint=target_url, data=data_payload,
                                       headers=header_payload, verify=self.ssl_verify,
                                       proxy=self.proxy, timeout=self.timeout,
                                       user_agent=self.user_agent)
            if isinstance(returned, dict):  # Issue #433
                self.token_status = returned["status_code"]
                if self.token_status == 201:
                    self.token_expiration = returned["body"]["expires_in"]
                    self.token_time = time.time()
                    self.token_value = returned["body"]["access_token"]
                    self.token_fail_reason = None
                    # Swap to the correct region if they've provided the incorrect one
                    if "X-Cs-Region" not in returned["headers"]:
                        # GovCloud autodiscovery is not currently supported
                        token_region = confirm_base_region(confirm_base_url(self.base_url))
                    else:
                        token_region = returned["headers"]["X-Cs-Region"].replace("-", "")
                    requested_region = confirm_base_region(confirm_base_url(self.base_url))
                    if token_region != requested_region:
                        self.base_url = confirm_base_url(token_region.upper())
                else:
                    if "errors" in returned["body"]:
                        if returned["body"]["errors"]:
                            self.token_fail_reason = returned["body"]["errors"][0]["message"]
            else:
                returned = generate_error_result("Unexpected API response received", 403)
                self.token_fail_reason = "Unexpected API response received"
                self.token_status = 403
        else:
            returned = generate_error_result("Invalid credentials specified", 403)
            self.token_fail_reason = "Invalid credentials specified"
            self.token_status = 403

        return returned

    def revoke(self: object, token: str) -> dict:
        """Revoke the specified authorization token.

        Keyword arguments:
        token: Token string to be revoked.

        When not specified as a keyword, token is assumed as the only accepted argument.

        Returns: dict object containing API response.
        """
        operation_id = "oauth2RevokeToken"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        if "client_id" in self.creds and "client_secret" in self.creds:
            b64cred = generate_b64cred(self.creds["client_id"], self.creds["client_secret"])
            header_payload = {"Authorization": f"basic {b64cred}"}
            data_payload = {"token": f"{token}"}
            returned = perform_request(method="POST", endpoint=target_url, data=data_payload,
                                       headers=header_payload, verify=self.ssl_verify,
                                       proxy=self.proxy, timeout=self.timeout,
                                       user_agent=self.user_agent)
            self.token_expiration = 0
            self.token_value = False
        else:
            returned = generate_error_result("Invalid credentials specified", 403)

        return returned

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    oauth2AccessToken = token
    oAuth2AccessToken = token
    oauth2RevokeToken = revoke
    oAuth2RevokeToken = revoke
