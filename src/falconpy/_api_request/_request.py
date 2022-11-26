"""FalconPy API Request object.

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
from typing import Union
from logging import Logger
from .._constant import MAX_DEBUG_RECORDS


# pylint: disable=R0902  # Should be fine
class APIRequest:
    """This class represents a request made to the CrowdStrike API."""

    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
    #
    method: str = "GET"
    body_payload: Union[dict, bytes] = None
    param_payload: dict = None
    data_payload: Union[dict, bytes] = None
    body_validator: dict = None
    body_required: list = None
    user_agent: str = None
    expand_result: bool = False
    log_util: Logger = None
    container: bool = False
    authenticating: bool = False
    verify: bool = True
    timeout: Union[int, float] = None
    files: list = []
    proxy: dict = None
    _perform: bool = True
    _endpoint: str = None
    max_debug: int = MAX_DEBUG_RECORDS
    _debug_headers: dict = {}
    sanitize_log: bool = True

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    def __init__(self, endpoint: str, initializer: dict = None):
        """Construct an instance of the class."""
        if initializer:
            self.endpoint = endpoint
            self.method = initializer.get("method", "GET")
            self.body_payload = initializer.get("body", None)
            self.param_payload = initializer.get("params", None)
            self.data_payload = initializer.get("data", None)
            self.body_validator = initializer.get("body_validator", None)
            self.body_required = initializer.get("body_required", None)
            self.user_agent = initializer.get("user_agent", None)
            self.expand_result = initializer.get("expand_result", False)
            self.log_util = initializer.get("log_util", None)
            self.files = initializer.get("files", [])
            self.proxy = initializer.get("proxy", {})
            self.container = initializer.get("container", False)
            self.authenticating = initializer.get("authenticating", False)
            self.verify = initializer.get("verify", True)
            self.timeout = initializer.get("timeout", None)
            _max_debug = initializer.get("debug_record_count", None)
            if _max_debug:
                self.max_debug = int(_max_debug)
            _sanitize = initializer.get("sanitize", None)
            if isinstance(_sanitize, bool):
                self.sanitize_log = _sanitize

    # _  _ ____ ___ _  _ ____ ___  ____
    # |\/| |___  |  |__| |  | |  \ [__
    # |  | |___  |  |  | |__| |__/ ___]
    #
    def log_error(self, code: int = 500, msg: str = None, content: Union[dict, str, bytes] = None):
        """Leverage the attached log utility to log the passed error detail if logging is enabled."""
        if self.log_util:
            self.log_util.error(msg)
            self.log_util.debug("STATUS CODE: %s", code)
            self.log_util.debug("RESULT: %s", content)

    def log_warning(self, code: int = 500, msg: str = None, content: Union[dict, str, bytes] = None):
        """Leverage the attached log utility to log the passed warning detail if logging is enabled."""
        if self.log_util:
            self.log_util.warning(msg)
            self.log_util.debug("STATUS CODE: %s", code)
            self.log_util.debug("RESULT: %s", content)

    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
    #
    @property
    def debug_headers(self) -> dict:
        """Return the debug headers."""
        return self._debug_headers

    @debug_headers.setter
    def debug_headers(self, value):
        """Set the debug headers."""
        self._debug_headers = value

    @property
    def perform(self) -> bool:
        """Return the perform boolean."""
        return self._perform

    @perform.setter
    def perform(self, value):
        """Set the perform boolean (this request has passed validation)."""
        self._perform = value

    @property
    def endpoint(self) -> bool:
        """Return the endpoint attribute."""
        return self._endpoint

    @endpoint.setter
    def endpoint(self, value):
        """Set the endpoint attribute."""
        self._endpoint = value
