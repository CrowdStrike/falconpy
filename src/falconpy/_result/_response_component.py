from inspect import isclass
from typing import Union


class ResponseComponent:
    _data: Union[dict, bytes, list, str] = None

    def __init__(self, data):
        self._data = data
        if isclass(data):
            if issubclass(data, ResponseComponent):
                self._data = data.data

        #print(f"Created {self.__class__.__name__}")
        #print(self._data)

    def __str__(self) -> str:
        return self.__repr__()
    def __repr__(self) -> dict:
        _returned = self._data
        if not self.binary:
            _returned = str(self._data)

        return _returned

    def __contains__(self, substr) -> bool:
        _returned = False
        if not self.binary:
            _returned = bool(substr in self._data)

        return _returned

    def __len__(self) -> int:
        _returned = None
        if not self.binary:
            _returned = len(self._data)

        return _returned

    @property
    def content(self) -> bytes:
        return self._data
    @property
    def binary(self) -> bool:
        return isinstance(self._data, bytes)