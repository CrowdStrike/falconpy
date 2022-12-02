"""FalconPy Request Validator class.

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
from typing import Type, Dict, Optional, List


class RequestValidator:
    """This class represents a request payload validator."""

    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
    #
    _validator: Optional[Dict[str, Type]] = None
    _required: Optional[List[str]] = None

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    def __init__(self,
                 validator: Optional[Dict[str, Type]] = None,
                 required: Optional[List[str]] = None
                 ):
        """Construct an instance of RequestValidator class."""
        self.validator = validator
        self.required = required

    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
    #
    @property
    def validator(self) -> Optional[Dict[str, Type]]:
        """Return the validator dictionary."""
        return self._validator

    @validator.setter
    def validator(self, value: Optional[Dict[str, Type]]):
        """Set the validator dictionary."""
        self._validator = value

    @property
    def required(self) -> Optional[List[str]]:
        """Return the required list."""
        return self._required

    @required.setter
    def required(self, value: Optional[List[str]]):
        """Set the required list."""
        self._required = value

# Python 3.7
# This code will be updated to the following once Python 3.6 support is dropped.
#
# from dataclasses import dataclass
# from typing import Type, Dict, Optional, List


# @dataclass
# class RequestValidator:
#     """This class represents a request payload validator."""

#     # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
#     # |__|  |   |  |__/ | |__] |  |  |  |___ [__
#     # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
#     #
#     validator: Optional[Dict[str, Type]] = None
#     required: Optional[List[str]] = None
