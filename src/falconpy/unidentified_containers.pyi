"""Type stubs for unidentified_containers."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class UnidentifiedContainers(ServiceClass):

    def read_count_by_date_range(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_count(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_and_read(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ReadUnidentifiedContainersByDateRangeCount = read_count_by_date_range
    ReadUnidentifiedContainersCount = read_count
    SearchAndReadUnidentifiedContainers = search_and_read
