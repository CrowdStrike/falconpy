"""Type stubs for intelligence_indicator_graph."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class IntelligenceIndicatorGraph(ServiceClass):

    def search(
        self,
        *,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def lookup(
        self,
        *args: Union[str, List[str]],
        values: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    SearchIndicators = search
    LookupIndicators = lookup
