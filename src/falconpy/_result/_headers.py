from ._response_component import ResponseComponent

class Headers(ResponseComponent):
    @property
    def content_encoding(self) -> str:
        return self._data.get("Content-Encoding", None)
    @property
    def content_length(self) -> int:
        return self._data.get("Content-Length", 0)
    @property
    def content_type(self) -> str:
        return self._data.get("Content-Type", None)
    @property
    def date(self) -> str:
        return self._data.get("Date", None)
    @property
    def region(self) -> str:
        return self._data.get("X-Cs-Region", None)
    @property
    def ratelimit_limit(self) -> int:
        return self._data.get("X-Ratelimit-Limit", None)
    @property
    def ratelimit_remaining(self) -> int:
        return self._data.get("X-Ratelimit-Remaining", None)
    @property
    def data(self) -> dict:
        return self._data