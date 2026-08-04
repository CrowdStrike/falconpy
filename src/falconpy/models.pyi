"""Type stubs for models."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Models(ServiceClass):

    def entities_models_v1(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def queries_models_v1(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    EntitiesModelsV1 = entities_models_v1
    QueriesModelsV1 = queries_models_v1
