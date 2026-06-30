"""Type stubs for quick_scan_pro."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class QuickScanPro(ServiceClass):

    def upload_file(
        self,
        *,
        file_name: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_file(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_scan_result(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def launch_scan(
        self,
        *,
        password: Optional[str] = None,
        sha256: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_scan_result(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_scan_results(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    UploadFileMixin0Mixin93 = upload_file
    UploadFileMixin0Mixin94 = upload_file
    UploadFileQuickScanPro = upload_file
    DeleteFile = delete_file
    GetScanResult = get_scan_result
    LaunchScan = launch_scan
    DeleteScanResult = delete_scan_result
    QueryScanResults = query_scan_results
