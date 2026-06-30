"""Type stubs for report_executions."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ReportExecutions(ServiceClass):

    def get_download(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def retry_reports(
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

    report_executions_download_get = get_download
    report_executions_get = get_reports
    reports_executions_query = query_reports
    report_executions_retry = retry_reports
