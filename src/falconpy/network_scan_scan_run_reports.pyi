"""Type stubs for network_scan_scan_run_reports."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class NetworkScanScanRunReports(ServiceClass):

    def get_scan_run_reports(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetScanRunReports = get_scan_run_reports
