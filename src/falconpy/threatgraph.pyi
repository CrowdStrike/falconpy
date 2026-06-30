"""Type stubs for threatgraph."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ThreatGraph(ServiceClass):

    def get_edges(
        self,
        *,
        ids: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        edge_type: Optional[str] = None,
        direction: Optional[str] = None,
        scope: Optional[str] = None,
        nano: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_ran_on(
        self,
        *,
        value: Optional[str] = None,
        type: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        nano: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_summary(
        self,
        *,
        vertex_type: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        scope: Optional[str] = None,
        nano: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_vertices_v1(
        self,
        *,
        vertex_type: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        scope: Optional[str] = None,
        nano: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_vertices(
        self,
        *,
        vertex_type: Optional[str] = None,
        ids: Optional[Union[str, List[str]]] = None,
        scope: Optional[str] = None,
        nano: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_edge_types(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    combined_edges_get = get_edges
    combined_ran_on_get = get_ran_on
    combined_summary_get = get_summary
    entities_vertices_get = get_vertices_v1
    entities_vertices_getv2 = get_vertices
    get_vertices_v2 = get_vertices
    queries_edgetypes_get = get_edge_types
