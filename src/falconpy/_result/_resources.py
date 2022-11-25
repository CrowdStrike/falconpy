from ._response_component import ResponseComponent
import json

class Resources(ResponseComponent):
    def __getitem__(self, item):
        return self._data[item]
    def contains(self, substr) -> list:
        _returned = []
        if self._data:
            #print(type(self._data))
            #print(self._data)
            _data = self._data
            if isinstance(_data, Resources):
                _data = self.data
            _returned = [x for x in _data if substr in x]
        return _returned
    @property
    def data(self) -> list:
        _returned = []
        if self._data:
            _data = self._data
            if isinstance(_data, Resources):
                _returned = _data.data

        return _returned

class BinaryFile(ResponseComponent):
    pass

class RawBody(ResponseComponent):
    pass
