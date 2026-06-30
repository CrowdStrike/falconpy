"""Type stubs for scheduled_reports."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ScheduledReports(ServiceClass):

    def launch(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_reports(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_reports(
        self,
        *,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        q: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    scheduled_reports_get = get_reports
    scheduled_reports_query = query_reports
    scheduled_reports_launch = launch
