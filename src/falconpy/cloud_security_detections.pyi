"""Type stubs for cloud_security_detections."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class CloudSecurityDetections(ServiceClass):

    def get_combined_iom_by_rule(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_iom_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_iom_entities(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        after: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    cspm_evaluations_combined_iom_by_rule = get_combined_iom_by_rule
    cspm_evaluations_iom_entities = get_iom_entities
    cspm_evaluations_iom_queries = query_iom_entities
