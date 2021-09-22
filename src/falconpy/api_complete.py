"""All-in-one CrowdStrike Falcon OAuth2 API harness

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
from ._util import _ALLOWED_METHODS
from ._util import perform_request, generate_b64cred, generate_error_result
from ._util import confirm_base_url, calc_url_from_args
from ._endpoint import api_endpoints


class APIHarness:
    """This one does it all. It's like the One Ring with significantly fewer orcs."""
    # pylint: disable=too-many-instance-attributes

    TOKEN_RENEW_WINDOW = 20  # in seconds

    def __init__(self: object,  # pylint: disable=R0913
                 base_url: str = "https://api.crowdstrike.com",
                 creds: dict = None,
                 client_id: str = None, client_secret: str = None,
                 ssl_verify: bool = True, proxy: dict = None,
                 timeout: float or tuple = None) -> object:
        """Instantiates an instance of the class, ingests credentials,
        the base URL and the SSL verification boolean.
        Afterwards class attributes are initialized.

        Keyword arguments:
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

        This method only accepts keywords to specify arguments.
        """
        if client_id and client_secret and not creds:
            creds = {
                "client_id": client_id,
                "client_secret": client_secret
            }
        elif not creds:
            creds = {}
        self.creds = creds
        self.base_url = confirm_base_url(base_url)
        self.ssl_verify = ssl_verify
        self.proxy = proxy
        self.timeout = timeout
        self.token = False
        self.token_expiration = 0
        self.token_time = time.time()
        self.authenticated = False
        self.headers = lambda: {"Authorization": f"Bearer {self.token}"} if self.token else {}
        self.commands = api_endpoints

    def valid_cred_format(self: object) -> bool:
        """Returns a boolean indicating if the client_id and
        client_secret are present in the creds dictionary."""
        retval = False
        if "client_id" in self.creds and "client_secret" in self.creds:
            retval = True

        return retval

    def token_expired(self: object) -> bool:
        """Returns a boolean based upon the token expiration status."""
        retval = False
        if (time.time() - self.token_time) >= (self.token_expiration - self.TOKEN_RENEW_WINDOW):
            retval = True

        return retval

    def authenticate(self: object) -> bool:
        """Generates an authorization token."""
        target = self.base_url+'/oauth2/token'
        data_payload = {}
        if self.valid_cred_format():
            data_payload = {
                'client_id': self.creds['client_id'],
                'client_secret': self.creds['client_secret']
            }
        if "member_cid" in self.creds:
            data_payload["member_cid"] = self.creds["member_cid"]

        result = perform_request(method="POST",
                                 endpoint=target,
                                 data=data_payload,
                                 headers={},
                                 verify=self.ssl_verify,
                                 proxy=self.proxy,
                                 timeout=self.timeout
                                 )
        if result["status_code"] == 201:
            self.token = result["body"]["access_token"]
            self.token_expiration = result["body"]["expires_in"]
            self.token_time = time.time()
            self.authenticated = True
        else:
            self.authenticated = False

        return self.authenticated

    def deauthenticate(self: object) -> bool:
        """Revokes the current authorization token. """
        target = str(self.base_url)+'/oauth2/revoke'
        b64cred = generate_b64cred(self.creds["client_id"], self.creds["client_secret"])
        header_payload = {"Authorization": f"basic {b64cred}"}
        data_payload = {"token": f"{self.token}"}
        revoked = False
        if perform_request(method="POST", endpoint=target, data=data_payload,
                           headers=header_payload, verify=self.ssl_verify,
                           proxy=self.proxy, timeout=self.timeout
                           )["status_code"] == 200:
            self.authenticated = False
            self.token = False
            revoked = True
        else:
            revoked = False

        return revoked

    def _create_header_payload(self: object, passed_arguments: dict) -> dict:
        """Creates the HTTP header payload based upon
        the existing class headers and passed arguments."""
        payload = self.headers()
        if "headers" in passed_arguments:
            for item in passed_arguments["headers"]:
                payload[item] = passed_arguments["headers"][item]
        if "content_type" in passed_arguments:
            payload["Content-Type"] = str(passed_arguments["content_type"])

        return payload

    def command(self: object, *args, **kwargs):
        """Checks token expiration, renewing when necessary, then performs the request.

        Keyword arguments:
        action: str = ""                                    - API Operation ID to perform
        parameters: dict = {}                               - Parameter payload (Query string)
        body: dict = {}                                     - Body payload (Body)
        data: dict = {}                                     - Data payload (Data)
        headers: dict = {}                                  - Headers dictionary (HTTP Headers)
        ids: list or str = None                             - ID list (IDs to handle)
        partition: int or str = None                        - Partition number
        override: str = None   (format: 'METHOD,ENDPOINT')  - Override method and endpoint
        action_name: str = None                             - Action to perform (API specific)
        files: list = []                                    - List of files to upload
        file_name: str = None                               - Name of the file to upload
        content_type: str = None                            - Content_Type HTTP header

        The first argument passed to this method is assumed to be 'action'. All others are ignored.

        Returns: dict object containing API response or binary object depending on operation ID.
        """
        if self.token_expired():
            # Authenticate them if we can
            self.authenticate()
        try:
            if not kwargs.get("action", None):
                # Assume they're passing it in as the first param
                kwargs["action"] = args[0]

        except IndexError:
            pass  # They didn't specify an action, use the default and try for an override instead
        uber_command = [a for a in self.commands if a[0] == kwargs["action"]]
        if "override" in kwargs:
            if kwargs["override"]:
                uber_command = [["Manual"] + kwargs["override"].split(",")]
        if uber_command:
            # Calculate our target endpoint based upon arguments passed to the function
            target = calc_url_from_args(f"{self.base_url}{uber_command[0][2]}", kwargs)
            # Calculate our header payload using arguments passed to the function and our token
            header_payload = self._create_header_payload(kwargs)
            # These have their defaults set by the force_defaults decorator
            data_payload = kwargs.get("data", {})
            body_payload = kwargs.get("body", {})
            file_list = kwargs.get("files", [])
            parameter_payload = kwargs.get("parameters", {})
            # Check for authentication
            if self.authenticated:
                # Which HTTP method to execute
                selected_method = uber_command[0][1].upper()
                # Only accept allowed HTTP methods
                if selected_method in _ALLOWED_METHODS:
                    returned = perform_request(method=selected_method,
                                               endpoint=target,
                                               body=body_payload,
                                               data=data_payload,
                                               params=parameter_payload,
                                               headers=header_payload,
                                               files=file_list,
                                               verify=self.ssl_verify,
                                               proxy=self.proxy,
                                               timeout=self.timeout
                                               )
                else:
                    # Bad HTTP method
                    returned = generate_error_result(message="Invalid HTTP method specified.",
                                                     code=405)
            else:
                # Invalid token / Bad creds
                returned = generate_error_result(message="Failed to issue token.", code=401)
        else:
            # That command doesn't exist, have a cup of tea instead
            returned = generate_error_result(message="Invalid API operation specified.", code=418)

        return returned
