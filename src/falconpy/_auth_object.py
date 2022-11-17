"""Authentication Object Base Class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

This file contains the definition of the base class that provides the necessary
functions to authenticate to the API. Out of the box we will provide only one
authentication object implementation in OAuth2.py, but this structure provides
both future extensibility, as well as the ability to reason about encapsulation of
authentication data.
"""
from abc import (
    ABC,
    abstractmethod,
)
from typing import Any, Dict


class FalconPyAuth(ABC):
    """Abstract class to provide authentication to Falcon.

    This class is not usable by developers alone. You must expect to work with
    a derivative of this class, such as an OAuth2 object.
    """
    @property
    @abstractmethod
    def auth_headers(self) -> Dict[str, str]:
        """Get a dictionary of headers that can authenticate an HTTP request.

        This function will always return a dictionary (which could be empty), containing
        all the HTTP headers required to authenticate a request. For example, an OAuth2
        implementation of this class should return a dictionary containing a 
        key -> value pair of the Authorization header and a Bearer token.

        If the headers need renewed data, such as updated tokens that can expire, the logic
        required for this should either be implemented or called from this function. Code
        dependent on this function should not need to check token validity.
        """

    @property
    @abstractmethod
    def authenticated(self) -> bool:
        """Read-only property can will return whether authentication is complete."""

    @abstractmethod
    def logout(self) -> Any:
        """Log out of Falcon, such as by revoking a token.

        This function may return any reasonable type, such as a dictionary.
        """
