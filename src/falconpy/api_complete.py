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
from typing import Dict, Optional, Tuple
from ._util import _ALLOWED_METHODS
from ._util import (
    perform_request,
    generate_b64cred,
    generate_error_result,
    confirm_base_url,
    args_to_params,
    return_preferred_default,
    autodiscover_region,
    )
from ._auth_object import FalconAuth
from ._base_url import BaseURL
from ._container_base_url import ContainerBaseURL
from ._uber_default_preference import PREFER_IDS_IN_BODY, MOCK_OPERATIONS
from ._token_fail_reason import TokenFailReason
from ._endpoint import api_endpoints


class APIHarness(FalconAuth):
    """This one does it all. It's like the One Ring with significantly fewer orcs."""

    # pylint: disable=too-many-instance-attributes
    _token_fail_headers = {}  # Issue #578
    refreshable: bool = True
    token_expiration: int = 0
    token_time: float = time.time()
    token_fail_reason: str = None
    token_status: int = None

    # pylint: disable=R0913
    def __init__(self,
                 access_token: Optional[str or bool] = False,
                 base_url: Optional[str] = "https://api.crowdstrike.com",
                 creds: Optional[dict] = None,
                 client_id: Optional[str] = None,
                 client_secret: Optional[str] = None,
                 member_cid: Optional[str] = None,
                 ssl_verify: Optional[bool] = True,
                 proxy: Optional[dict] = None,
                 timeout: Optional[float or tuple] = None,
                 user_agent: Optional[str] = None,
                 renew_window: Optional[int] = 120
                 ) -> "APIHarness":
        """Uber class constructor.

        Instantiates an instance of the class, ingests credentials,
        the base URL and the SSL verification boolean.
        Afterwards class attributes are initialized.

        Keyword arguments:
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
        member_cid: Child CID to connect to. (MSSP only) Mutually exclusive to creds.
        user_agent: User-Agent string to use for all requests made to the CrowdStrike API.
                    String. Defaults to crowdstrike-falconpy/VERSION.
        renew_window: Amount of time (in seconds) between now and the token expiration before
                      a refresh of the token is performed. Default: 120, Max: 1200
                      Values over 1200 will be reset to the maximum.

        This method only accepts keywords to specify arguments.
        """
        super().__init__(base_url=confirm_base_url(base_url),
                         ssl_verify=ssl_verify,
                         timeout=timeout,
                         proxy=proxy,
                         user_agent=user_agent
                         )
        # Direct Authentication
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
        # Credential Authentication (powers Direct Authentication)
        self.creds: Dict[str, str] = creds
        # Legacy (Token) Authentication
        self.token_value: str or bool = access_token
        if access_token:
            # We do not have API credentials, disable token refresh.
            self.refreshable = False
            # Assume the token was just generated.
            self.token_expiration = 1799

        # Complete list of available API operations.
        self.commands = api_endpoints

        # Maximum renewal window is 20 minutes, Minimum is 2 minutes
        self.token_renew_window = max(min(renew_window, 1200), 120)  # in seconds

    def valid_cred_format(self) -> bool:
        """Legacy property to confirm credential dictionary format."""
        return self.cred_format_valid

    def authenticate(self) -> bool:
        """Generate an authorization token."""
        operation_id = "oauth2AccessToken"
        target = f"{self.base_url}{[ep[2] for ep in self.commands if operation_id in ep[0]][0]}"
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
                self.token_value = result["body"]["access_token"]
                self.token_expiration = result["body"]["expires_in"]
                self.token_time = time.time()
                self.token_fail_reason = None
                self.base_url = autodiscover_region(self.base_url, result)
            else:
                self.token_expiration = 0
                self._token_fail_headers = result["headers"]
                if "errors" in result["body"]:
                    if result["body"]["errors"]:
                        self.token_fail_reason = result["body"]["errors"][0]["message"]
        else:
            self.token_expiration = 0
            self.token_fail_reason = TokenFailReason["UNEXPECTED"].value
            self.token_status = 403

        return self.authenticated

    def deauthenticate(self) -> bool:
        """Revoke the current authorization token."""
        operation_id = "oauth2RevokeToken"
        target = f"{self.base_url}{[ep[2] for ep in self.commands if operation_id in ep[0]][0]}"
        b64cred = generate_b64cred(self.creds["client_id"], self.creds["client_secret"])
        header_payload = {"Authorization": f"basic {b64cred}"}
        data_payload = {"token": f"{self.token_value}"}
        revoked = False
        if perform_request(method="POST", endpoint=target, data=data_payload,
                           headers=header_payload, verify=self.ssl_verify,
                           proxy=self.proxy, timeout=self.timeout, user_agent=self.user_agent
                           )["status_code"] == 200:
            self.token_expiration = 0
            self.token_value = False
            revoked = True

        return revoked

    def _create_header_payload(self, passed_arguments: dict) -> dict:
        """Create the HTTP header payload.

        Creates the HTTP header payload based upon the existing class headers and passed arguments.
        """
        payload = self.auth_headers
        if "headers" in passed_arguments:
            for item in passed_arguments["headers"]:
                payload[item] = passed_arguments["headers"][item]
        if "content_type" in passed_arguments:
            payload["Content-Type"] = str(passed_arguments["content_type"])

        return payload

    @staticmethod
    def _handle_field(tgt: str, kwa: dict, fld: str) -> str:
        """Embed the distinct_field value (SensorUpdatePolicy) within the endpoint URL."""
        # Could potentially be zero
        return tgt.format(str(kwa.get(fld, None))) if kwa.get(fld, None) is not None else tgt

    @staticmethod
    def _handle_body_payload_ids(kwa: dict) -> dict:
        if kwa.get("action", None) in PREFER_IDS_IN_BODY:
            if kwa.get("ids", None):
                # Handle the GET to POST method redirection for passed IDs
                if not kwa.get("body", {}).get("ids", None):
                    if "body" not in kwa:
                        kwa["body"] = {}
                    kwa["body"]["ids"] = kwa["ids"]
            # Handle any body payload ID lists that are still strings
            if isinstance(kwa.get("body", {}).get("ids", {}), str):
                kwa["body"]["ids"] = kwa["body"]["ids"].split(",")
        return kwa

    def _handle_container_operations(self, kwa: dict, base_string: str) -> Tuple[dict, str, bool]:
        """Handle Base URLs and keyword arguments for container registry operations."""
        # Default to non-container registry operations
        do_container = False
        if kwa.get("action", None) in MOCK_OPERATIONS:
            for base in [burl for burl in dir(BaseURL) if "__" not in burl]:
                if BaseURL[base].value == self.base_url.replace("https://", ""):
                    base_string = f"https://{ContainerBaseURL[base].value}"
                    do_container = True
            if kwa.get("action", None) == "ImageMatchesPolicy":
                if "parameters" not in kwa:
                    kwa["parameters"] = {}
                kwa["parameters"]["policy_type"] = "image-prevention-policy"
        return kwa, base_string, do_container

    def _request_keywords(self, meth: str, oper: str, tgt: str, kwa: dict, do_cont: bool) -> dict:
        """Generate a properly formatted mapping of the keywords for this request."""
        return {
            "method": meth,
            "endpoint": tgt,
            "body": kwa.get("body", return_preferred_default(oper)),
            "data": kwa.get("data", return_preferred_default(oper)),
            "params": args_to_params(kwa.get("parameters", {}), kwa, self.commands, oper),
            "headers": self._create_header_payload(kwa),
            "files": kwa.get("files", return_preferred_default(oper, "list")),
            "verify": self.ssl_verify,
            "proxy": self.proxy,
            "timeout": self.timeout,
            "user_agent": self.user_agent,
            "expand_result": kwa.get("expand_result", False),
            "container": do_cont
        }

    def _scrub_target(self, oper: str, scrubbed: str, kwas: dict) -> str:
        """Scrubs the endpoint target by performing any outstanding string replacements."""
        field_mapping = {
            "image_id": "DeleteImageDetails",
            "partition": "refreshActiveStreamSession",
            "distinct_field": "querySensorUpdateKernelsDistinct"
        }
        for field_name, field_value in field_mapping.items():
            if oper == field_value:  # Only perform replacements on mapped operation IDs.
                scrubbed = self._handle_field(scrubbed, kwas, field_name)

        return scrubbed

    def command(self, *args, **kwargs) -> dict or bytes:
        """Uber Class API command method.

        Checks token expiration, renewing when necessary, then performs the request.

        HTTP Method: Any

        Swagger URL
        ----
        https://assets.falcon.crowdstrike.com/support/api/swagger.html

        Keyword arguments
        ----
        action : str (Default: None)
            API Operation ID to perform
        parameters : dict (Default: {})
            Parameter payload (Query string)
        body : dict (Default: {})
            Body payload (Body)
        data : dict (Default: {})
            Data payload (Data)
        headers : dict (Default: {})
            Headers dictionary (HTTP Headers)
        ids : list or str (Default: None)
            ID list (IDs to handle)
        partition : int or str (Default: None)
            Partition number (Event Streams only)
        distinct_field : str (Default: None)
            Distinct Field (Sensor Update Policy only)
        override : str (Default: None)
            Override method and endpoint. Example: 'METHOD,ENDPOINT'
        action_name : str (Default: None)
            Action to perform (API specific)
        files : list (Default: [])
            List of files to upload
        file_name : str (Default: None)
            Name of the file to upload
        content_type : str (Default: None)
            Content_Type HTTP header
        expand_result : bool (Default: False)
            Request expanded results (returns a tuple)
        image_id : str (Default: None)
            Container image ID (Falcon Container only)

        Arguments
        ----
        The first argument passed to this method is assumed to be 'action'. All others are ignored.

        Returns
        ----
        dict or bytes
            Dictionary or binary object containing API response depending on requested operation.
        """
        if not self.authenticated or (self.token_expired and self.refreshable):
            # Authenticate them if they're not yet authenticated or expired.
            self.authenticate()

        try:
            if not kwargs.get("action", None):
                # Assume they're passing it in as the first argument.
                kwargs["action"] = args[0]
        except IndexError:
            pass  # They didn't specify an action, try for an override instead.

        uber_command = [a for a in self.commands if a[0] == kwargs.get("action", None)]
        if kwargs.get("override", None):
            uber_command = [["Manual"] + kwargs["override"].split(",")]
        if uber_command:
            # Which API operation to perform.
            operation = uber_command[0][0]
            # Retrieve our base URL and alter keywords if we are performing a container operation.
            kwargs, url_base, container = self._handle_container_operations(kwargs, self.base_url)
            # Retrieve the endpoint from the command list and append to our base URL and
            # then perform any outstanding string replacements on the target endpoint URL.
            target = self._scrub_target(operation, f"{url_base}{uber_command[0][2]}", kwargs)
            # Handle any IDs that are in the wrong payload
            kwargs = self._handle_body_payload_ids(kwargs)
            # Check for authentication
            if self.authenticated:
                # Which HTTP method to execute
                method = uber_command[0][1].upper()
                # Only accept allowed HTTP methods
                if method in _ALLOWED_METHODS:
                    returned = perform_request(
                        **self._request_keywords(method, operation, target, kwargs, container)
                        )
                else:
                    # Bad HTTP method
                    returned = generate_error_result(message="Invalid HTTP method specified.",
                                                     code=405
                                                     )
            else:
                # Invalid token / Bad creds
                returned = generate_error_result(message="Failed to issue token.",
                                                 code=401,
                                                 headers=self._token_fail_headers
                                                 )
        else:
            # That command doesn't exist, have a cup of tea instead
            returned = generate_error_result(message="Invalid API operation specified.", code=418)

        return returned

    # Legacy properties
    def headers(self) -> Dict[str, str]:
        """Legacy property getter for the current authorization headers."""
        return self.auth_headers

    # Generic logout interface
    logout = deauthenticate

    # Read only properties
    @property
    def auth_headers(self) -> Dict[str, str]:
        """Return a Bearer token baked into an Authorization header ready for an HTTP request."""
        return {"Authorization": f"Bearer {self.token_value}"}

    @property
    def token_expired(self) -> bool:
        """Return whether the token is ready to be renewed."""
        return (time.time() - self.token_time) >= (self.token_expiration - self.token_renew_window)

    @property
    def authenticated(self) -> bool:
        """Return if we are authenticated by retrieving the inverse of token_expired."""
        return not self.token_expired

    @property
    def token(self) -> str:
        """Return the token string."""
        return self.token_value
