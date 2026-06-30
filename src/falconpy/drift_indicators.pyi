"""Type stubs for drift_indicators."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class DriftIndicators(ServiceClass):

    def get_drift_indicators_by_date(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_drift_indicator_counts(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_and_read_drift_indicators(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_drift_indicator_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_drift_indicators(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetDriftIndicatorsValuesByDate = get_drift_indicators_by_date
    ReadDriftIndicatorsCount = read_drift_indicator_counts
    ReadDriftIndicatorEntities = read_drift_indicator_entities
    SearchAndReadDriftIndicatorEntities = search_and_read_drift_indicators
    SearchDriftIndicators = search_drift_indicators
