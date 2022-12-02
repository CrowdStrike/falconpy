"""FalconPy Request Behavior class.

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
from typing import Optional, Dict, List, Type
from ._request_validator import RequestValidator


class RequestBehavior:
    """This class represents specified behaviors for an API request."""

    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
    #
    _expand_result: bool = False
    _container: bool = False
    _authenticating: bool = False
    _perform: bool = True
    _validator = RequestValidator()

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    def __init__(self,
                 expand_result: Optional[bool] = None,
                 container: Optional[bool] = None,
                 authenticating: Optional[bool] = None,
                 perform: Optional[bool] = None,
                 body_validator: Optional[Dict[str, Type]] = None,
                 body_required: Optional[List[str]] = None
                 ):
        """Construct an instance of RequestBehavior class."""
        if isinstance(expand_result, bool):
            self.expand_result = expand_result
        if isinstance(container, bool):
            self.container = container
        if isinstance(authenticating, bool):
            self.authenticating = authenticating
        if isinstance(perform, bool):
            self.perform = perform
        if isinstance(body_validator, dict) or isinstance(body_required, list):
            self.validator = RequestValidator(validator=body_validator,
                                              required=body_required
                                              )

    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
    #
    @property
    def expand_result(self) -> bool:
        """Indicate if the result for this request be expanded into a tuple."""
        return self._expand_result

    @expand_result.setter
    def expand_result(self, value: bool):
        """Enable or disable results expansion."""
        self._expand_result = value

    @property
    def container(self) -> bool:
        """Indicate if this request interacts with a Falcon Container endpoint."""
        return self._container

    @container.setter
    def container(self, value: bool):
        """Change the container value."""
        self._container = value

    @property
    def authenticating(self) -> bool:
        """Indicate if this request is for authentication."""
        return self._authenticating

    @authenticating.setter
    def authenticating(self, value: bool):
        """Specify if this is an authenticating request."""
        self._authenticating = value

    @property
    def perform(self) -> bool:
        """Flag indicating if this request should be performed. (Set by the payload validation)."""
        return self._perform

    @perform.setter
    def perform(self, value: bool):
        """Enable or disable the perform bit."""
        self._perform = value

    @property
    def validator(self) -> RequestValidator:
        """Object representing the request validation performed on any provided payloads."""
        return self._validator

    @validator.setter
    def validator(self, value: RequestValidator):
        """Change the validator object."""
        self._validator = value

    @property
    def body_validator(self) -> Optional[Dict[str, Type]]:
        """Reflection into the validator object for the body payload validator."""
        return self.validator.validator

    @property
    def body_required(self) -> Optional[List[str]]:
        """Reflection into the validator object for the body payload required list."""
        return self.validator.required
