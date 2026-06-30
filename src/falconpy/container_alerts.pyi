"""Type stubs for container_alerts."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ContainerAlerts(ServiceClass):

    def read_counts_by_severity(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_counts(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_and_read(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ReadContainerAlertsCountBySeverity = read_counts_by_severity
    ReadContainerAlertsCount = read_counts
    SearchAndReadContainerAlerts = search_and_read
