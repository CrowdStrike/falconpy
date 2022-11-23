"""Authentication Object Base Class.

This file contains the definition of the base class that provides the
necessary functions to authenticate to the CrowdStrike Falcon OAuth2 API.

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
from ._falcon_auth import FalconAuth

class UberInterface(FalconAuth):
    """Uber Class specific interface."""

    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
    #
    # Attributes present only within the Uber Class.
    #
    # A dictionary of every available API operation provided by the library.
    commands: dict = {}

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    # Starting in v1.3.0, the Uber Class constructs itself leveraging the generic
    # FalconAuth constructor. This results in the Uber Class benefiting from a new
    # authentication style; Legacy / Token authentication.
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
                 ) -> "UberInterface":
        """Construct an instance of the UberInterface class."""
        super().__init__(base_url=base_url,
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

    # _  _ ____ ___ _  _ ____ ___  ____
    # |\/| |___  |  |__| |  | |  \ [__
    # |  | |___  |  |  | |__| |__/ ___]
    #
    # Override the default login and logout handlers to
    # provide Uber Class-specific functionality.
    def login(self) -> bool:
        """Generate an authorization token."""
        super().login()

        return self.authenticated

    def logout(self) -> bool:
        """Revoke the current authorization token."""
        result = super().logout()

        return bool(result["status_code"] == 200)

    # _    ____ ____ ____ ____ _   _    _  _ ____ _  _ ___  _    ____ ____ ____
    # |    |___ | __ |__| |     \_/     |__| |__| |\ | |  \ |    |___ |__/ [__
    # |___ |___ |__] |  | |___   |      |  | |  | | \| |__/ |___ |___ |  \ ___]
    #
    # These handlers provide legacy Uber Class-specific functionality that will be
    # maintained for provide backwards compatibility purposes.
    def authenticate(self) -> bool:
        """Legacy Uber Class functionality handler.

        DEPRECATED
        ----
        Consider updating your code to leverage the login method.
        """
        return self.login()

    def deauthenticate(self) -> bool:
        """Legacy Uber Class functionality handler.

        DEPRECATED
        ----
        Consider updating your code to leverage the logout method.
        """
        return self.logout()

    def valid_cred_format(self) -> bool:
        """Legacy property to confirm credential dictionary format.
        
        DEPRECATED
        ----
        Consider updating your code to leverage the cred_format_valid property.
        """
        return self.cred_format_valid

    def headers(self) -> Dict[str, str]:
        """Legacy property getter for the current authorization headers.

        DEPRECATED
        ----
        Consider updating your code to leverage the auth_headers property.
        """
        return self.auth_headers

    @property
    def token(self) -> str:
        """Legacy attribute handler to return the token string.

        DEPRECATED
        ----
        Consider updating your code to leverage the token_value property.
        """
        return self.token_value
