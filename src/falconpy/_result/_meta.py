from typing import Dict
from ._response_component import ResponseComponent


class Meta(ResponseComponent):
    _pos: int = 0
    # Headers are always dictionaries
    _data: Dict[str, str] = {}
    @property
    def query_time(self) -> float:
        return self._data.get("query_time", None)
    @property
    def offset(self) -> int or str:
        return self._data.get("pagination", {}).get("offset", None)
    @property
    def limit(self) -> int or str:
        return self._data.get("pagination", {}).get("limit", None)
    @property
    def total(self) -> int or str:
        _returned = 0
        #print(type(self._data))
        _page = self._data.get("pagination", {})
        if _page:
            _returned = _page.get("total", None)
        return _returned
    @property
    def powered_by(self) -> str:
        return self._data.get("powered_by", None)
    @property
    def trace_id(self) -> str:
        return self._data.get("trace_id", None)
    def __iter__(self):
        return self
    def __next__(self):
        self._pos += 1
        #print(self._data.values())
        if self._pos > len(self._data):
            self._pos = 0
            raise StopIteration
        _returned = list(self._data.values())[self._pos - 1]

        return _returned