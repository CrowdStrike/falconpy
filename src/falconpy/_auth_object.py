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
from abc import ABC, abstractmethod
from typing import Dict, Optional


class FalconAuth(ABC):
    """Abstract class to provide authentication to the CrowdStrike Falcon OAuth2 API.

    This class is not usable by developers alone.
    You must work with a derivative of this class, such as an OAuth2 object.
    """

    @property
    @abstractmethod
    def auth_headers(self) -> Dict[str, str]:
        """Get a dictionary of headers that can authenticate an HTTP request."""

    @property
    @abstractmethod
    def authenticated(self) -> bool:
        """Read-only property to return whether authentication is successful."""

    @property
    @abstractmethod
    def token_expired(self) -> bool:
        """Read-only property that returns the current token expiration status."""

    @abstractmethod
    def logout(self) -> dict:
        """Log out of Falcon by revoking the current token."""

    # pylint: disable=R0913
    def __init__(self,
                 base_url: Optional[str] = "https://api.crowdstrike.com",
                 ssl_verify: Optional[bool] = True,
                 timeout: Optional[float or tuple] = None,
                 proxy: Optional[Dict[str, str]] = None,
                 user_agent: Optional[str] = None
                 ):
        """Construct an instance of the base class."""
        self.base_url: str = base_url
        self.ssl_verify: bool = ssl_verify
        self.timeout: float or tuple = timeout
        self.proxy: Dict[str, str] = proxy
        self.user_agent: str = user_agent
