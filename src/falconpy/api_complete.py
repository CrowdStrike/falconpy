"""All-in-one CrowdStrike Falcon OAuth2 API harness.

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
from ._util import confirm_base_url, args_to_params, confirm_base_region
from ._endpoint import api_endpoints


class APIHarness:
    """This one does it all. It's like the One Ring with significantly fewer orcs."""

    # pylint: disable=too-many-instance-attributes

    TOKEN_RENEW_WINDOW = 20  # in seconds

    def __init__(self: object,  # pylint: disable=R0913
                 base_url: str = "https://api.crowdstrike.com",
                 creds: dict = None,
                 client_id: str = None,
                 client_secret: str = None,
                 member_cid: str = None,
                 ssl_verify: bool = True,
                 proxy: dict = None,
                 timeout: float or tuple = None,
                 user_agent: str = None
                 ) -> object:
        """Uber class constructor.

        Instantiates an instance of the class, ingests credentials,
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
                     "client_secret": "CLIENT_SECRET_HERE",
                     "member_cid": "CHILD_CID_MSSP_ONLY"
                 }
        client_id -- Client ID for the CrowdStrike API. Mutually exclusive to creds.
        client_secret -- Client Secret for the CrowdStrike API. Mutually exclusive to creds.
        member_cid -- Child CID to connect to. (MSSP only) Mutually exclusive to creds.
        user_agent -- User-Agent string to use for all requests made to the CrowdStrike API.
                      String. Defaults to crowdstrike-falconpy/VERSION.

        This method only accepts keywords to specify arguments.
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
        self.proxy = proxy
        self.timeout = timeout
        self.token = False
        self.token_expiration = 0
        self.token_time = time.time()
        self.authenticated = False
        self.token_fail_reason = None
        self.token_status = None
        self.headers = lambda: {"Authorization": f"Bearer {self.token}"} if self.token else {}
        self.commands = api_endpoints
        self.user_agent = user_agent  # Issue #365

    def valid_cred_format(self: object) -> bool:
        """Confirm credential dictionary format.

        Returns a boolean indicating if the client_id and
        client_secret are present in the creds dictionary.
        """
        retval = False
        if "client_id" in self.creds and "client_secret" in self.creds:
            retval = True

        return retval

    def token_expired(self: object) -> bool:
        """Return a boolean based upon the token expiration status."""
        retval = False
        if (time.time() - self.token_time) >= (self.token_expiration - self.TOKEN_RENEW_WINDOW):
            retval = True

        return retval

    def authenticate(self: object) -> bool:
        """Generate an authorization token."""
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
                                 timeout=self.timeout,
                                 user_agent=self.user_agent
                                 )
        if isinstance(result, dict):  # Issue #433
            self.token_status = result["status_code"]
            if self.token_status == 201:
                self.token = result["body"]["access_token"]
                self.token_expiration = result["body"]["expires_in"]
                self.token_time = time.time()
                self.authenticated = True
                self.token_fail_reason = None
                # Swap to the correct region if they've provided the incorrect one
                if "X-Cs-Region" not in result["headers"]:
                    # GovCloud autodiscovery is not currently supported
                    token_region = confirm_base_region(confirm_base_url(self.base_url))
                else:
                    token_region = result["headers"]["X-Cs-Region"].replace("-", "")
                requested_region = confirm_base_region(confirm_base_url(self.base_url))
                if token_region != requested_region:
                    self.base_url = confirm_base_url(token_region.upper())
            else:
                self.authenticated = False
                if "errors" in result["body"]:
                    if result["body"]["errors"]:
                        self.token_fail_reason = result["body"]["errors"][0]["message"]
        else:
            self.authenticated = False
            self.token_fail_reason = "Unexpected API response received"
            self.token_status = 403

        return self.authenticated

    def deauthenticate(self: object) -> bool:
        """Revoke the current authorization token."""
        target = str(self.base_url)+'/oauth2/revoke'
        b64cred = generate_b64cred(self.creds["client_id"], self.creds["client_secret"])
        header_payload = {"Authorization": f"basic {b64cred}"}
        data_payload = {"token": f"{self.token}"}
        revoked = False
        if perform_request(method="POST", endpoint=target, data=data_payload,
                           headers=header_payload, verify=self.ssl_verify,
                           proxy=self.proxy, timeout=self.timeout, user_agent=self.user_agent
                           )["status_code"] == 200:
            self.authenticated = False
            self.token = False
            revoked = True
        else:
            revoked = False

        return revoked

    def _create_header_payload(self: object, passed_arguments: dict) -> dict:
        """Create the HTTP header payload.

        Creates the HTTP header payload based upon the existing class headers and passed arguments.
        """
        payload = self.headers()
        if "headers" in passed_arguments:
            for item in passed_arguments["headers"]:
                payload[item] = passed_arguments["headers"][item]
        if "content_type" in passed_arguments:
            payload["Content-Type"] = str(passed_arguments["content_type"])

        return payload

    def command(self: object, *args, **kwargs):
        """Uber Class API command method.

        Checks token expiration, renewing when necessary, then performs the request.

        Keyword arguments:
        action: str = ""                                    - API Operation ID to perform
        parameters: dict = {}                               - Parameter payload (Query string)
        body: dict = {}                                     - Body payload (Body)
        data: dict = {}                                     - Data payload (Data)
        headers: dict = {}                                  - Headers dictionary (HTTP Headers)
        ids: list or str = None                             - ID list (IDs to handle)
        partition: int or str = None                        - Partition number
        distinct_field: str = None                          - Distinct Field
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
        if kwargs.get("override", None):
            uber_command = [["Manual"] + kwargs["override"].split(",")]
        if uber_command:
            # Retrieve the endpoint URL from the command list
            target = f"{self.base_url}{uber_command[0][2]}"
            if kwargs.get("partition", None) is not None:
                # Partition needs to be embedded into the endpoint URL
                target = target.format(str(kwargs.get("partition", None)))
            if kwargs.get("distinct_field", None) is not None:
                # distinct_field also needs to be embedded into the endpoint URL
                target = target.format(str(kwargs.get("distinct_field", None)))
            # Check for authentication
            if self.authenticated:
                # Which HTTP method to execute
                selected_method = uber_command[0][1].upper()
                # Only accept allowed HTTP methods
                if selected_method in _ALLOWED_METHODS:
                    returned = perform_request(method=selected_method,
                                               endpoint=target,
                                               body=kwargs.get("body", {}),
                                               data=kwargs.get("data", {}),
                                               params=args_to_params(kwargs.get("parameters", {}),
                                                                     kwargs,
                                                                     self.commands,
                                                                     uber_command[0][0]
                                                                     ),
                                               headers=self._create_header_payload(kwargs),
                                               files=kwargs.get("files", []),
                                               verify=self.ssl_verify,
                                               proxy=self.proxy,
                                               timeout=self.timeout,
                                               user_agent=self.user_agent
                                               )
                else:
                    # Bad HTTP method
                    returned = generate_error_result(message="Invalid HTTP method specified.",
                                                     code=405
                                                     )
            else:
                # Invalid token / Bad creds
                returned = generate_error_result(message="Failed to issue token.", code=401)
        else:
            # That command doesn't exist, have a cup of tea instead
            returned = generate_error_result(message="Invalid API operation specified.", code=418)

        return returned
