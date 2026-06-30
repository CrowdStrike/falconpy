"""Type stubs for fdr."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class FDR(ServiceClass):

    def get_event_combined(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_event_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_event_entities(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_field_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_field_entities(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    fdrschema_combined_event_get = get_event_combined
    fdrschema_entities_event_get = get_event_entities
    fdrschema_queries_event_get = query_event_entities
    fdrschema_entities_field_get = get_field_entities
    fdrschema_queries_field_get = query_field_entities
