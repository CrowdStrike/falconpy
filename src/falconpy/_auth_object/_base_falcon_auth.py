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
from typing import Dict


class BaseFalconAuth(ABC):
    """Abstract class to provide an interface to the CrowdStrike Falcon OAuth2 API.

    This class does not implement a generic constructor and is not intended to be used by
    developers directly. You must work with a derivative of this class, such as a FalconAuth object.
    """
    #  ______  _______ _______ _______ _     _        _______
    #  |     \ |______ |______ |_____| |     | |         |
    #  |_____/ |______ |       |     | |_____| |_____    |

    #  _______ _______ _______ _     _  _____  ______  _______
    #  |  |  | |______    |    |_____| |     | |     \ |______
    #  |  |  | |______    |    |     | |_____| |_____/ ______|

    # The generic login and logout handlers must be individually defined by all
    # inheriting classes. The private methods defined here are used to allow for
    # easy overridding of login and logout processing by inheriting classes without
    # altering the parent handler method that may be leveraged by other inheriting
    # class types.
    @abstractmethod
    def _login_handler(self) -> dict or bool:
        """Login to the Falcon API by requesting a new token."""

    @abstractmethod
    def _logout_handler(self) -> dict or bool:
        """Log out of the Falcon API by revoking the current token."""

    @abstractmethod
    def login(self) -> dict or bool:
        """Generic login handler interface."""

    @abstractmethod
    def logout(self) -> dict or bool:
        """Generic logout handler interface."""

    #   _____   ______  _____   _____  _______  ______ _______ _____ _______ _______
    #  |_____] |_____/ |     | |_____] |______ |_____/    |      |   |______ |______
    #  |       |    \_ |_____| |       |______ |    \_    |    __|__ |______ ______|
    #
    # These properties are present within all BaseFalconAuth derivatives.
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

    @property
    @abstractmethod
    def cred_format_valid(self) -> bool:
        """Read-only property that returns a boolean if the creds dictionary is valid."""
