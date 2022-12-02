"""FalconPy Request Connection class.

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
from typing import Optional, Dict, Union


class RequestConnection:
    """This class represents connection details related to an API request."""

    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
    #
    _user_agent: Optional[str] = None
    _verify: bool = True
    _timeout: Optional[Union[int, tuple]] = None
    _proxy: Optional[Dict[str, str]] = None

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    def __init__(self,
                 user_agent: Optional[str] = None,
                 proxy: Optional[Dict[str, str]] = None,
                 timeout: Optional[Union[int, tuple]] = None,
                 verify: Optional[bool] = None
                 ):
        """Construct an instance of RequestConnection class."""
        self.user_agent: Optional[str] = user_agent
        self.proxy: Optional[Dict[str, str]] = proxy
        self.timeout: Optional[Union[int, tuple]] = timeout
        if isinstance(verify, bool):
            self.verify: bool = verify

    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
    #
    @property
    def user_agent(self) -> Optional[str]:
        """User agent string to be sent along with connection headers."""
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value: str):
        """Set the user agent string."""
        self._user_agent = value

    @property
    def proxy(self) -> Optional[Dict[str, str]]:
        """Return the dictionary containing proxy information that is used for requests."""
        return self._proxy

    @proxy.setter
    def proxy(self, value: Dict[str, str]):
        """Specify a new proxy dictionary."""
        self._proxy = value

    @property
    def timeout(self) -> Optional[Union[int, tuple]]:
        """Timeout in seconds for the connection specified as either an integer or tuple.

        Tuple format: (connect, read)
        """
        return self._timeout

    @timeout.setter
    def timeout(self, value: Union[int, tuple]):
        """Specify a new timeout setting for the connection."""
        self._timeout = value

    @property
    def verify(self) -> bool:
        """Flag indicating if SSL verification is enabled for the connection."""
        return self._verify

    @verify.setter
    def verify(self, value: bool):
        """Enable or disable SSL verification for the connection."""
        self._verify = value


# Python 3.7+ version
# This code will be updated to the following once Python 3.6 support is dropped.
#
# from dataclasses import dataclass
# from typing import Optional, Dict, Union


# @dataclass
# class RequestConnection:
#     """This class represents connection details related to an API request."""

#     # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
#     # |__|  |   |  |__/ | |__] |  |  |  |___ [__
#     # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
#     #
#     user_agent: Optional[str] = None
#     verify: bool = True
#     timeout: Optional[Union[int, tuple]] = None
#     proxy: Optional[Dict[str, str]] = None
