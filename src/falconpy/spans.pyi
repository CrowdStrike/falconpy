"""Type stubs for spans."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Spans(ServiceClass):

    def entities_spans_v1(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def queries_spans_v1(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    EntitiesSpansV1 = entities_spans_v1
    QueriesSpansV1 = queries_spans_v1
