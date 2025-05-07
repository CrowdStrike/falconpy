"""CrowdStrike NGSIEM API HEC payload.

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
from datetime import datetime, timezone
from inspect import getmembers
from json import dumps
from typing import Dict, List, Union
from .._enum import TimeUnit
from .._version import version


class IngestPayload:  # pylint: disable=R0902
    """Class to represent a JSON formatted ingest payload."""

    _host: str = "UNKNOWN"
    _source: str = version(agent_string=True)
    _sourcetype: str = "json-hec"
    _kind: str = "event"
    _module: str = "crowdstrike-falconpy-hec"
    _type: List[str] = ["info"]
    _category: List[str] = ["host"]
    _timestamp: int = None
    _timeunit: str = None
    _custom: Dict[str, Union[str, int, dict, list]] = {}
    _fields: Dict[str, Union[str, int, dict, list]] = {}

    # pylint: disable=R0912,R0913
    def __init__(self,
                 host: str = None,
                 kind: str = None,
                 module: str = None,
                 event_type: List[str] = None,
                 category: List[str] = None,
                 timestamp: int = None,
                 timeunit: str = None,
                 custom: Dict[str, Union[str, int, dict, list]] = None,
                 fields: Dict[str, Union[str, int, dict, list]] = None,
                 **kwargs
                 ):
        """Create an instance of the class."""
        if host:
            self.host = host
        if kind:
            self.kind = kind
        if module:
            self.module = module
        if event_type:
            if isinstance(event_type, list):
                self.type = event_type
            else:
                self.type.clear()
                self.type.append(event_type)
        if category:
            if isinstance(category, list):
                self.category = category
            else:
                self.category.clear()
                self.category.append(category)
        if timestamp:
            self.timestamp = timestamp
        if timeunit:
            self.timeunit = timeunit
        if custom:
            self.custom = custom
        else:
            self.custom = {}
        if fields:
            self.fields = fields
        for provided_key, provided_value in kwargs.items():
            if provided_key not in [key[0] for key in getmembers(self) if "_" not in key[0]]:
                self.custom[provided_key] = provided_value

    def to_json(self, raw: bool = False) -> Dict[str, Union[str, int, dict, list]]:
        """Convert the class to a JSON compliant dictionary or JSON string."""
        returned = {}
        items = [key[0] for key in getmembers(self) if "_" not in key[0]]
        event = {
            item_key: getattr(self, item_key)
            for item_key in items if item_key not in ["fields", "custom", "timeunit"]
        }
        for unit in TimeUnit:
            if unit.value == self.timeunit:
                event["timeunit"] = unit.name.lower()
        for key, value in self.custom.items():
            event[key] = value

        returned["event"] = event
        if not raw:
            # Raw payloads cannot specify the fields array
            if getattr(self, "fields"):
                returned["fields"] = self.fields
        else:
            # Convert to a JSON string for raw payloads
            returned = dumps(returned)

        return returned

    @property
    def host(self) -> str:
        """Return the host property."""
        return self._host

    @host.setter
    def host(self, value: str):
        """Set the host property."""
        self._host = value

    @property
    def kind(self) -> str:
        """Return the kind property."""
        return self._kind

    @kind.setter
    def kind(self, value: str):
        """Set the kind property."""
        self._kind = value

    @property
    def module(self) -> str:
        """Return the module property."""
        return self._module

    @module.setter
    def module(self, value: str):
        """Set the module property."""
        self._module = value

    @property
    def type(self) -> List[str]:
        """Return the type property."""
        return self._type

    @type.setter
    def type(self, value: List[str]):
        """Set the type property."""
        self._type = value

    @property
    def category(self) -> List[str]:
        """Return the category property."""
        return self._category

    @category.setter
    def category(self, value: List[str]):
        """Set the category property."""
        self._category = value

    @property
    def timeunit(self) -> int:
        """Return the timestamp time unit."""
        if not self._timeunit:
            self._timeunit = TimeUnit["NANOSECONDS"].value
        return self._timeunit

    @timeunit.setter
    def timeunit(self, value: str):
        self._timeunit = TimeUnit[value.upper()].value

    @property
    def timestamp(self) -> int:
        """Return the timestamp property."""
        if not self._timestamp:
            self._timestamp = int(datetime.now(timezone.utc).timestamp() * self.timeunit)
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: int):
        """Set the timestamp property."""
        self._timestamp = value

    @property
    def custom(self) -> Dict[str, Union[str, int, dict, list]]:
        """Return the custom properties."""
        return self._custom

    @custom.setter
    def custom(self, value: Dict[str, Union[str, int, dict, list]]):
        """Set the custom properties."""
        self._custom = value

    @property
    def fields(self) -> Dict[str, Union[str, int, dict, list]]:
        """Return the fields dictionary."""
        return self._fields

    @fields.setter
    def fields(self, value: Dict[str, Union[str, int, dict, list]]):
        """Set the fields dictionary."""
        self._fields = value
