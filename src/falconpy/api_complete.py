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
from typing import Dict, Optional
from ._util import _ALLOWED_METHODS
from ._util import (
    perform_request,
    generate_error_result,
    confirm_base_url,
    )
from ._auth_object import UberInterface
from ._util import (
    handle_body_payload_ids,
    scrub_target,
    handle_container_operations,
    uber_request_keywords
    )
from ._endpoint import api_endpoints


class APIHarness(UberInterface):
    """This one does it all. It's like the One Ring with significantly fewer orcs.

    The Uber Class inherits from the UberInterface class, which is a stand alone
    class that encapsulates the FalconAuth class. This allows the Uber Class to
    inherit all the functionality from the FalconAuth class while maintaining
    additional functionality only provided by the Uber Class.

    This means the Uber Class does not include an auth_object, as it is one.
    As of FalconPy v1.3.0, Object Authentication is still unssupported for
    Uber Class usage scenarios.
    """
    # pylint: disable=R0913
    #                                 `-.
    #                     -._ `. `-.`-. `-.
    #                     _._ `-._`.   .--.  `.
    #                  .-'   '-.  `-|\/    \|   `-.
    #                .'         '-._\   (o)O) `-.
    #               /         /         _.--.\ '. `-. `-.
    #              /|    (    |  /  -. ( -._( -._ '. '.
    #             /  \    \-.__\ \_.-'`.`.__'.   `-, '. .'
    #             |  /\    |  / \ \     `--')/  .-'.'.'
    #          .._/  /  /  /  / / \ \          .' . .' .'
    #         /  ___/  |  /   \ \  \ \__       '.'. . .
    #         \  \___  \ (     \ \  `._ `.     .' . ' .'
    #          \ `-._\ (  `-.__ | \    )//   .'  .' .-'
    #           \_-._\  \  `-._\)//    ""_.-' .-' .' .'
    #             `-'    \ -._\ ""_..--''  .-' .'
    #                     \/    .' .-'.-'  .-' .-'
    #                         .-'.' .'  .' .-
    def __init__(self,
                 access_token: Optional[str or bool] = False,
                 base_url: Optional[str] = "https://api.crowdstrike.com",
                 creds: Optional[Dict[str, str]] = None,
                 client_id: Optional[str] = None,
                 client_secret: Optional[str] = None,
                 member_cid: Optional[str] = None,
                 ssl_verify: Optional[bool] = True,
                 proxy: Optional[Dict[str, str]] = None,
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
                         user_agent=user_agent,
                         access_token=access_token,
                         creds=creds,
                         client_id=client_id,
                         client_secret=client_secret,
                         member_cid=member_cid,
                         renew_window=renew_window
                         )

        # Complete list of available API operations.
        self.commands = api_endpoints

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
            # Which HTTP method to execute
            method = uber_command[0][1].upper()
            # Retrieve our base URL and alter keywords if we are performing a container operation.
            kwargs, url_base, container = handle_container_operations(kwargs, self.base_url)
            # Retrieve the endpoint from the command list and append to our base URL and
            # then perform any outstanding string replacements on the target endpoint URL.
            target = scrub_target(operation, f"{url_base}{uber_command[0][2]}", kwargs)
            # Handle any IDs that are in the wrong payload
            kwargs = handle_body_payload_ids(kwargs)
            # Only accept allowed HTTP methods
            if method in _ALLOWED_METHODS:
                returned = perform_request(
                    **uber_request_keywords(self, method, operation, target, kwargs, container)
                    )
            else:
                # Bad HTTP method
                returned = generate_error_result(message="Invalid HTTP method specified.",
                                                    code=405
                                                    )
        else:
            # That command doesn't exist, have a cup of tea instead
            returned = generate_error_result(message="Invalid API operation specified.", code=418)

        return returned
