"""API Response formatting class.

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
# pylint: disable=R0903  # Using a class so that the data structure is callable
from abc import ABC, abstractmethod
from typing import Dict, Union
from json import loads, dumps
from requests.structures import CaseInsensitiveDict
from ._meta import Meta
from ._errors import Errors
from ._headers import Headers
from ._resources import Resources, BinaryFile, RawBody


class BaseResult:
    # _______ _______ _______  ______ _____ ______  _     _ _______ _______ _______
    # |_____|    |       |    |_____/   |   |_____] |     |    |    |______ |______
    # |     |    |       |    |    \_ __|__ |_____] |_____|    |    |______ ______|
    # The attributes contain response data by category.
    status_code: int = 0
    headers: Headers = None
    meta: Meta = None
    resources: Resources = Resources([])
    errors: Errors = []
    raw: RawBody = None

    # Privates used for iteration
    _pos: int = 0
    _reversed: bool = False

    # _______ _______ _______ _     _  _____  ______  _______
    # |  |  | |______    |    |_____| |     | |     \ |______
    # |  |  | |______    |    |     | |_____| |_____/ ______|
    #
    def __init__(self, status_code: int = None, headers: dict = None, body: dict = None):
        """Generic init method"""
        
        if status_code and headers and body:
            self.status_code = status_code
            _headers = headers
            try:
                if isinstance(_headers, CaseInsensitiveDict):
                    print(type(_headers))
                    _headers = dict(headers)
                self.headers = Headers(_headers)
                print(self.headers)
            except Exception as err:
                print(err)
            if body.get("access_token", None):
                print("Setting raw body")
                self.raw = RawBody(body)
            else:
                print("Passed Headers")
                print(self.meta)
                try:
                    print(body.get("meta", {}))
                    print(type(body.get("meta", {})))
                    self.meta = Meta(data=dict(body.get("meta", {})))
                except Exception as err:
                    print(err)
                print("Passed Meta")
                try:
                    if isinstance(body, bytes):
                        self.resources = BinaryFile(body)
                        
                    else:
                        received = body.get("resources", [])
                        if isinstance(body, Resources):
                            self.resources = Resources(received.data)
                        else:
                            self.resources = Resources(received)
                    print("Passed Body")
                except Exception as err:
                    print(err)
                try:
                    self.errors = Errors(body.get("errors", []))
                    print("Passed Errors")
                except Exception as err:
                    print(err)

    # Iteration handlers
    def __iter__(self):
        """Return this object for iteration handling."""
        return self
    def __reversed__(self):
        """Reverse the iteration order."""
        self._reversed = True
        self._pos = len(self.resources) + 1
        return self
    def __next__(self):
        """Retrieve the next item in the list."""
        _returned = None
        if self._reversed:
            self._pos -= 1
        else:
            self._pos += 1
        if self._pos == len(self.resources) + 1:
            self._reversed = False
            raise StopIteration
        if self._pos == 0:
            self._reversed = False
            raise StopIteration
        if self.resources.data:
            self.resources.data[self._pos-1]
        return _returned

    def __getitem__(self, pos):
        """Retrieve an item by position from the resources list."""
        _returned = 0
        print(type(self.resources.data))
        print(pos)
        print(len(self.resources._data))
        if self.resources:
            _returned = self.resources._data[pos]
        return _returned
    # Returns the length of the resources data attribute
    def __len__(self) -> int:
        """Return the length of the resources list when taking the length of this object."""
        _returned = 0
        if self.resources:
            _returned = len(self.resources)
        return _returned
    # Return a boolean if the string matches
    def __contains__(self, substr):
        """Return a boolean if the search string is found within the list. Exact matches only."""
        return bool(substr in self.resources)

    # Legacy handler that emulates functionality in versions prior to v1.3.
    def __call__(self, status_code = None, headers = None, body = None):
        return {
            "status_code" : status_code,
            # force standard dictionary to prevent json issues
            "headers" : dict(headers),
            "body" : body
        }

    # Return the entire structure as a JSON formatted string.
    # I'm back and forth on how to best implement this.
    def __repr__(self) -> str:
        body = self.raw
        if not body:
            body = {
                "meta": self.meta,
                "resources": self.resources,
                "errors": self.errors
            }
        return str({
            "status_code": self.status_code,
            "headers": self.headers,
            "body": body
        })

class Result(BaseResult):

    def __init__(self,
                 status_code: int = None,
                 headers: Dict[str, str] = None,
                 body: Dict[str, Union[list, dict]] = None,
                 full: Dict[str, Union[int, Dict[str, str], Dict[str, Union[list, dict]]]] = None,
                 log = None
                 ):
        # Default behavior is to create an empty object to emulate previous functionality.
        if full:
            if isinstance(full, dict):
                status_code = full.get("status_code", None)
                headers = full.get("headers", None)
                body = full.get("body", None)
            else:
                status_code = full.status_code
                headers = full.headers
                body = full.body
        if log:
            log.debug(status_code)
            log.debug(headers)
            log.debug(body)
        super().__init__(status_code=status_code, headers=headers, body=body)
        if log:
            log.debug(self.resources)

    # _  _ ____ ___ _  _ ____ ___  ____
    # |\/| |___  |  |__| |  | |  \ [__
    # |  | |___  |  |  | |__| |__/ ___]
    def dictify(self) -> dict:
        return loads(str(self))
    
    # Easy filter method
    def prune(self, substr) -> list:
        """Return a list of matches for the search string from the result list."""
        _returned = [x for x in self.resources.contains(substr)]
        return _returned
    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
    @property
    def total(self) -> int:
        _returned = 0
        if self.meta:
            _returned = self.meta.total
        return _returned
    @property
    def offset(self) -> Union[str, int]:
        _returned = None
        if self.meta:
            _returned = self.meta.offset
        return _returned
    @property
    def limit(self) -> int:
        _returned = 0
        if self.meta:
            _returned = self.meta.limit
        return _returned
    @property
    def query_time(self) -> float:
        _returned = 0
        if self.meta:
            _returned = self.meta.query_time
        return _returned
    @property
    def powered_by(self) -> str:
        _returned = None
        if self.meta:
            _returned = self.meta.powered_by
        return _returned
    @property
    def trace_id(self) -> str:
        _returned = None
        if self.meta:
            _returned = self.meta.trace_id
        return _returned
    @property
    def content_encoding(self) -> str:
        _returned = None
        if self.headers:
            _returned = self.headers.content_encoding
        return _returned
    @property
    def content_type(self) -> str:
        _returned = None
        if self.headers:
            _returned = self.headers.content_type
        return _returned
    @property
    def content_length(self) -> int:
        _returned = 0
        if self.headers:
            _returned = self.headers.content_length
        return _returned
    @property
    def date(self) -> str:
        _returned = None
        if self.headers:
            _returned = self.headers.date
        return _returned
    @property
    def region(self) -> str:
        _returned = None
        if self.headers:
            _returned = self.headers.region
        return _returned
    @property
    def ratelimit_limit(self) -> int:
        _returned = 0
        if self.headers:
            _returned = self.headers.ratelimit_limit
        return _returned
    @property
    def ratelimit_remaining(self) -> int:
        _returned = 0
        if self.headers:
            _returned = self.headers.ratelimit_remaining
        return _returned
    @property
    def data(self) -> list:
        _returned = []
        if self.resources:
            _returned = self.resources._data
        return _returned
    @property
    def current_index(self) -> int:
        return self._pos
    @property
    def reversed(self) -> bool:
        return self._reversed
    @property
    def tupled(self) -> dict:
        if self.resources.binary:
            content = self.resources
        else:
            content = {
                "meta": self.meta,
                "resources": self.resources,
                "errors": self.errors
            }
        return (self.status_code, self.headers, content)
    @property
    def body(self) -> dict:
        _body = {
                "meta": self.meta,
                "resources": self.resources,
                "errors": self.errors
                }
        return _body
# class Result:
#     """Callable subclass to handle parsing of result client output."""

#     def __call__(self,
#                  status_code: int,
#                  headers: Dict[str, str],
#                  body: Dict[str, Dict]
#                  ) -> Dict[str, Union[int, Dict[str, str], Dict[str, Union[Dict, List]]]]:
#         """Format values into a properly formatted result object."""
#         return {
#             "status_code" : status_code,
#             # force standard dictionary to prevent json issues
#             "headers" : dict(headers),
#             "body" : body
#         }
