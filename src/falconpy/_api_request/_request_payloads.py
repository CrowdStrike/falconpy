"""FalconPy Request Payloads class.

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
from typing import Optional, Dict, List, Union


class RequestPayloads:
    """This class contains all of the payloads sent as part of the API request."""

    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
    #
    _params: Optional[Dict[str, Optional[Union[str, int, float, list, dict]]]] = None
    _body: Optional[Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]] = None
    _data: Optional[Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]] = None
    _files: Optional[List[tuple]] = None

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    def __init__(self,
                 params: Optional[Dict[str, Optional[Union[str, int, float, list, dict]]]] = None,
                 body: Optional[Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]] = None,
                 data: Optional[Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]] = None,
                 files: Optional[List[tuple]] = None
                 ):
        """Construct an instance of RequestPayloads class."""
        self.params = params
        self.body = body
        self.data = data
        self.files = files

    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
    #
    @property
    def params(self) -> Optional[Dict[str, Optional[Union[str, int, float, list, dict]]]]:
        """Return the query string parameter payload."""
        return self._params

    @params.setter
    def params(self, value: Optional[Dict[str, Optional[Union[str, int, float, list, dict]]]]):
        """Set the query string parameter payload."""
        self._params = value

    @property
    def body(self) -> Optional[Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]]:
        """Return the body payload."""
        return self._body

    @body.setter
    def body(self, value: Optional[Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]]):
        """Set the body payload."""
        self._body = value

    @property
    def data(self) -> Optional[Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]]:
        """Return the data payload."""
        return self._data

    @data.setter
    def data(self, value: Optional[Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]]):
        """Set the data payload."""
        self._data = value

    @property
    def files(self) -> Optional[List[tuple]]:
        """Return the files payload."""
        return self._files

    @files.setter
    def files(self, value: Optional[List[tuple]]):
        """Set the files payload."""
        self._files = value


# Python 3.7
# This code will be updated to leverage dataclasses once Python 3.6 support is dropped.
#
# from dataclasses import dataclass
# from typing import Optional, Dict, List, Union


# @dataclass
# class RequestPayloads:
#     """This class contains all of the payloads sent as part of the API request."""
#
#     # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
#     # |__|  |   |  |__/ | |__] |  |  |  |___ [__
#     # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
#     #
#     params: Optional[Dict[str, Optional[Union[str, int, float, list, dict]]]] = None
#     body: Optional[Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]] = None
#     data: Optional[Union[bytes, Dict[str, Union[str, int, dict, list, bytes]]]] = None
#     files: Optional[List[tuple]] = None
