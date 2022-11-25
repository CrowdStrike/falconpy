from ._response_component import ResponseComponent

class Errors(ResponseComponent):
    def __repr__(self) -> str:
        _returned = []
        if self._data:
            _returned = ",".join([f"[{x['code']}] {x['message']}" for x in self._data])
        return str(_returned)
