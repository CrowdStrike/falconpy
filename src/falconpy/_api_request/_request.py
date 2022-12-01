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
from typing import Union, Dict, Optional
from logging import Logger
from ._request_behavior import RequestBehavior
from ._request_connection import RequestConnection
from ._request_log import RequestLog
from ._request_meta import RequestMeta
from ._request_payloads import RequestPayloads


class APIRequest:
    """This class represents a request made to the CrowdStrike API."""

    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
    #
    _meta: Optional[RequestMeta] = None
    _payloads: Optional[RequestPayloads] = None
    _connection: RequestConnection = RequestConnection()
    _behavior = RequestBehavior()
    _request_log: Optional[RequestLog] = None

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    def __init__(self,
                 endpoint: str,
                 initializer: Optional[Dict[str, Optional[Union[str, int, bool, list, dict]]]] = None
                 ):
        """Construct an instance of the APIRequest class."""
        if initializer:
            # Key metadata regarding this API request
            self.meta = RequestMeta(endpoint, initializer.get("method", "GET"))
            # Payloads for the request
            self.payloads = RequestPayloads(params=initializer.get("params", None),
                                            body=initializer.get("body", None),
                                            data=initializer.get("data", None),
                                            files=initializer.get("files", [])
                                            )
            # Connection specific details for creating the request
            self.connection = RequestConnection(user_agent=initializer.get("user_agent", None),
                                                proxy=initializer.get("proxy", {}),
                                                timeout=initializer.get("timeout", None),
                                                verify=initializer.get("verify", True)
                                                )
            # Behavioral flags that alter the behavior of request processing
            self.behavior = RequestBehavior(expand_result=initializer.get("expand_result", False),
                                            container=initializer.get("container", False),
                                            authenticating=initializer.get("authenticating", False),
                                            body_validator=initializer.get("body_validator", None),
                                            body_required=initializer.get("body_required", None)
                                            )
            # Logging functionality
            self.request_log = RequestLog(log=initializer.get("log_util", None),
                                          max_debug=initializer.get("debug_record_count", None),
                                          sanitize_log=initializer.get("sanitize", None)
                                          )

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

    def debug(self, msg: str):
        """Leverage the attached log utility to update the debug log."""
        if self.log_util:
            self.log_util.debug(msg)

    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
    #
    # All of these properties reflect states for properties of connected attribute objects.

    # _  _ ____ ___ ____
    # |\/| |___  |  |__|
    # |  | |___  |  |  |
    @property
    def meta(self) -> RequestMeta:
        """Return the RequestMeta object."""
        return self._meta

    @meta.setter
    def meta(self, value: RequestMeta):
        """Set the RequestMeta object."""
        self._meta = value

    @property
    def endpoint(self) -> bool:
        """Return the endpoint attribute."""
        return self._meta.endpoint

    @endpoint.setter
    def endpoint(self, value):
        """Set the endpoint attribute."""
        self._meta.endpoint = value

    @property
    def method(self) -> bool:
        """Return the method attribute."""
        return self._meta.method

    @method.setter
    def method(self, value):
        """Set the method attribute."""
        self._meta.method = value

    @property
    def debug_headers(self) -> dict:
        """Return the debug headers."""
        return self._meta.debug_headers

    @debug_headers.setter
    def debug_headers(self, value):
        """Set the debug headers."""
        self._meta.debug_headers = value

    # ___  ____ _   _ _    ____ ____ ___  ____
    # |__] |__|  \_/  |    |  | |__| |  \ [__
    # |    |  |   |   |___ |__| |  | |__/ ___]
    @property
    def payloads(self) -> RequestPayloads:
        """Retrieve the payloads object."""
        return self._payloads

    @payloads.setter
    def payloads(self, value: RequestPayloads):
        """Set the payloads object."""
        self._payloads = value

    # Body
    @property
    def body_payload(self) -> Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]:
        """Retrieve the body payload from the payloads object."""
        return self.payloads.body

    @body_payload.setter
    def body_payload(self, value: Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]):
        """Set the body payload within the payloads object."""
        self.payloads.body = value

    # Params
    @property
    def param_payload(self) -> Dict[str, str]:
        """Retrieve the param payload from the payloads object."""
        return self.payloads.params

    @param_payload.setter
    def param_payload(self, value: Dict[str, str]):
        """Set the param payload within the payloads object."""
        self.payloads.params = value

    # Data
    @property
    def data_payload(self) -> Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]:
        """Retrieve the data payload from the data object."""
        return self.payloads.data

    @data_payload.setter
    def data_payload(self, value: Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]):
        """Set the data payload within the payloads object."""
        self.payloads.data = value

    # Files
    @property
    def files(self) -> list:
        """Retrieve the files payload from the files object."""
        return self.payloads.files

    @files.setter
    def files(self, value: list):
        """Set the files payload within the payloads object."""
        self.payloads.files = value

    # ___  ____ _  _ ____ _  _ _ ____ ____
    # |__] |___ |__| |__| |  | | |  | |__/
    # |__] |___ |  | |  |  \/  | |__| |  \
    @property
    def behavior(self) -> RequestBehavior:
        """Return the RequestBehavior object."""
        return self._behavior

    @behavior.setter
    def behavior(self, value: RequestBehavior):
        """Set the RequestBehavior object."""
        self._behavior = value

    @property
    def expand_result(self) -> bool:
        """Return a boolean indicator if result expansion is requested."""
        return self.behavior.expand_result

    @expand_result.setter
    def expand_result(self, value: bool):
        """Set the result expansion setting."""
        self.behavior.expand_result = value

    @property
    def container(self) -> bool:
        """Return a boolean indicating if this is a container API request."""
        return self.behavior.container

    @container.setter
    def container(self, value: bool):
        """Set the container API request flag."""
        self.behavior.container = value

    @property
    def authenticating(self) -> bool:
        """Return a boolean indicating if this is an authentication request."""
        return self.behavior.authenticating

    @authenticating.setter
    def authenticating(self, value: bool):
        """Set the authenticating boolean."""
        self.behavior.authenticating = value

    @property
    def perform(self) -> bool:
        """Return the perform boolean."""
        return self.behavior.perform

    @perform.setter
    def perform(self, value: bool):
        """Set the perform boolean (this request has passed validation)."""
        self.behavior.perform = value

    @property
    def body_validator(self) -> dict:
        """Return the body payload validator from the behavior object."""
        return self.behavior.body_validator

    @body_validator.setter
    def body_validator(self, value: dict):
        """Set the body payload validator within the behavior object."""
        self.behavior.body_validator = value

    @property
    def body_required(self) -> list:
        """Return the body required list from the behavior object."""
        return self.behavior.body_required

    @body_required.setter
    def body_required(self, value: list):
        """Set the body payload required list within the behavior object."""
        self.behavior.body_required = value

    # _    ____ ____
    # |    |  | | __
    # |___ |__| |__]
    @property
    def request_log(self) -> RequestLog:
        """Return the RequestLog object."""
        return self._request_log

    @request_log.setter
    def request_log(self, value: RequestLog):
        """Set the RequestLog object."""
        self._request_log = value

    @property
    def log_util(self) -> Logger:
        """Return the Logger from the request log object."""
        return self.request_log.log

    @log_util.setter
    def log_util(self, value: Logger):
        """Set the Logger within the request log object."""
        self.request_log.log = value

    @property
    def debugging(self) -> bool:
        """Return the debugging status. This is a helper property to ease the syntax."""
        return bool(self.log_util)

    @property
    def max_debug(self) -> int:
        """Return the maximum number of records to log per debug entry setting."""
        return self.request_log.max_debug

    @max_debug.setter
    def max_debug(self, value: int):
        """Set the maximum number of records to log per debug entry setting."""
        self.request_log.max_debug = value

    @property
    def sanitize_log(self) -> bool:
        """Return the sanitize logs setting."""
        return self.request_log.sanitize_log

    @sanitize_log.setter
    def sanitize_log(self, value: bool):
        """Set the sanitize logs setting."""
        self.request_log.sanitize_log = value

    # ____ ____ _  _ _  _ ____ ____ ___ _ ____ _  _
    # |    |  | |\ | |\ | |___ |     |  | |  | |\ |
    # |___ |__| | \| | \| |___ |___  |  | |__| | \|
    @property
    def connection(self) -> RequestConnection:
        """Return the RequestConnection object."""
        return self._connection

    @connection.setter
    def connection(self, value: RequestConnection):
        """Set the RequestConnection object."""
        self._connection = value

    @property
    def user_agent(self) -> str:
        """Return the User Agent string."""
        return self.connection.user_agent

    @user_agent.setter
    def user_agent(self, value: str):
        """Set the User Agent string."""
        self.connection.user_agent = value

    @property
    def proxy(self) -> Dict[str, str]:
        """Return the proxy dictionary."""
        return self.connection.proxy

    @proxy.setter
    def proxy(self, value: Dict[str, str]):
        """Set the proxy dictionary."""
        self.connection.proxy = value

    @property
    def timeout(self) -> Union[int, tuple]:
        """Return the timeout from the connection object.."""
        return self.connection.timeout

    @timeout.setter
    def timeout(self, value: Union[int, tuple]):
        """Set an integer or a tuple for the timeout."""
        self.connection.timeout = value

    @property
    def verify(self) -> bool:
        """Return the SSL verification setting."""
        return self.connection.verify

    @verify.setter
    def verify(self, value: bool):
        """Set the SSL verification setting."""
        self.connection.verify = value
