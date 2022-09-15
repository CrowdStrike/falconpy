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
from ._util import confirm_base_url, autodiscover_region
from .oauth2 import OAuth2

# pylint: disable=R0902  # Nine is reasonable
# pylint: disable=R0912  # Currently at 13 branches
# pylint: disable=R0915  # 51/50 statements. Allowing for now. 10.07.21 - jshcodes


class ServiceClass:
    """Base class of all service classes. Contains the default __init__ method."""

    def __init__(self: object, auth_object: object = None,
                 creds: dict = None, base_url: str = "https://api.crowdstrike.com",
                 proxy: dict = None, **kwargs) -> object:
        """Service Class base constructor.

        Instantiates the object, ingests authorization credentials,
        and initializes attributes.

        Keyword arguments:
        access_token: Token string to use for all requests performed.
                        Mutually exclusive to all other authentication elements.
        auth_object: Properly authenticated instance of the OAuth2 Authentication service class.
        base_url: CrowdStrike API URL to use for requests. [Default: US-1]
        ssl_verify: Boolean specifying if SSL verification should be used. [Default: True]
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
        ext_headers: Additional headers to be prepended to the default headers dictionary.
                     Dictionary.

        This method only accepts keywords to specify arguments.
        """
        access_token = kwargs.get("access_token", None)
        self.ssl_verify = kwargs.get("ssl_verify", True)
        self.timeout = kwargs.get("timeout", None)
        self.token_renew_window = kwargs.get("renew_window", 120)
        user_agent = kwargs.get("user_agent", None)
        member_cid = kwargs.get("member_cid", None)
        self.headers = kwargs.get("ext_headers", {})
        # Currently defaulting to validation enabled
        self.validate_payloads = kwargs.get("validate_payloads", True)
        self.refreshable = False
        self.token_fail_reason = None
        self.token_status = None
        self.auth_object = None
        client_id = kwargs.get("client_id", None)
        client_secret = kwargs.get("client_secret", None)
        if client_id and client_secret and not creds:
            # Passing client_id and client_secret will not
            # overwrite the contents of the creds dictionary
            creds = {
                "client_id": client_id,
                "client_secret": client_secret
            }
            if member_cid:
                # Passing member_cid will not overwrite the
                # existing value in the creds dictionary
                creds["member_cid"] = member_cid
        if auth_object:
            # Assume they've passed us an OAuth2 object
            self.auth_object = auth_object
            if not isinstance(auth_object, OAuth2):
                # If they didn't, look for one as an attribute to the object they provided.
                for attr in [x for x in dir(auth_object) if "__" not in x]:
                    if attr == "auth_object":
                        self.auth_object = auth_object.auth_object
            if not self.authenticated():
                token_result = self.auth_object.token()
                self.token_status = token_result["status_code"]
                if self.token_status == 201:
                    self.token = token_result["body"]["access_token"]
                    self.headers["Authorization"] = f"Bearer {self.token}"
                else:
                    self.token = False
                    self.token_fail_reason = self.auth_object.token_fail_reason
            else:
                self.token = self.auth_object.token_value
                self.headers["Authorization"] = f"Bearer {self.token}"

            self.base_url = auth_object.base_url
            self.ssl_verify = auth_object.ssl_verify
            self.proxy = auth_object.proxy
            # Supports overriding user-agent per class
            if not user_agent:
                self.user_agent = auth_object.user_agent
            else:
                self.user_agent = user_agent
            # At this point in time, you cannot override
            # the auth_object's timeout per class instance
            self.timeout = auth_object.timeout
            self.refreshable = True
        else:
            confirmed_base = confirm_base_url(base_url)
            self.base_url = confirmed_base
            if creds:
                self.auth_object = OAuth2(creds=creds,
                                          base_url=confirmed_base,
                                          proxy=proxy,
                                          ssl_verify=self.ssl_verify,
                                          timeout=self.timeout,
                                          user_agent=user_agent,
                                          renew_window=self.token_renew_window
                                          )
                token_result = self.auth_object.token()
                self.token_status = token_result["status_code"]
                if self.token_status == 201:
                    self.token = token_result["body"]["access_token"]
                    self.headers["Authorization"] = f"Bearer {self.token}"
                    self.base_url = autodiscover_region(confirmed_base, token_result)
                else:
                    self.token = False
                    self.token_fail_reason = self.auth_object.token_fail_reason
                self.refreshable = True
            else:
                self.headers["Authorization"] = f"Bearer {access_token}"

            self.proxy = proxy
            self.user_agent = user_agent

    def authenticated(self):
        """Return the current authentication status."""
        result = None
        if self.auth_object:
            result = self.auth_object.authenticated()

        return result

    def token_expired(self):
        """Return a boolean reflecting token expiration status."""
        result = None
        if self.auth_object:
            result = self.auth_object.token_expired()

        return result
