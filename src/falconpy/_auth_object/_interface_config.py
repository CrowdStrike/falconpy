"""Interface Configuration class.

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
from typing import Dict, Union, Optional
from .._error import InvalidBaseURL


class InterfaceConfiguration:
    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
    #
    # The base URL for this interface.    
    _base_url: str = None
    # The proxy to use for communication with the CrowdStrike Falcon API.
    _proxy: Optional[Dict[str, str]] = None
    # The timeout to use for communication.
    # Either an integer for the entire operation or a float for (connect, read).
    _timeout: Optional[Union[int, float]] = None
    # The user-agent string to use for requests to the CrowdStrike Falcon API.
    _user_agent: Optional[str] = None
    # SSL Verification boolean, defaults to True.
    _ssl_verify: bool = True

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    def __init__(self,
                 base_url: str,
                 proxy: Optional[Dict[str, str]] = None,
                 timeout: Optional[Union[int, float]] = None,
                 user_agent: Optional[str] = None,
                 ssl_verify: Optional[bool] = True
                 ):
        if not base_url:
            raise InvalidBaseURL
        self._base_url = base_url
        if proxy:
            self._proxy = proxy
        if timeout:
            self._timeout = timeout
        if user_agent:
            self._user_agent = user_agent
        if ssl_verify:
            self._ssl_verify = ssl_verify

    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
    #
    @property
    def base_url(self) -> str:
        """Return the base URL."""
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    @property
    def proxy(self) -> dict:
        """Return the proxy."""
        return self._proxy

    @proxy.setter
    def proxy(self, value):
        self._proxy = value

    @property
    def timeout(self) -> Union[int, float]:
        """Return the timeout."""
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value

    @property
    def user_agent(self) -> str:
        """Return the user agent string."""
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value):
        self._user_agent = value

    @property
    def ssl_verify(self) -> bool:
        """Return the SSL verification setting."""
        return self._ssl_verify

    @ssl_verify.setter
    def ssl_verify(self, value):
        self._ssl_verify = value
