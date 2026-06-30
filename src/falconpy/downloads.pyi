"""Type stubs for downloads."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class Downloads(ServiceClass):

    def fetch_download_info(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def fetch_download_info_v2(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def download(
        self,
        *,
        file_name: Optional[str] = None,
        file_version: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def enumerate(
        self,
        *,
        file_name: Optional[str] = None,
        file_version: Optional[str] = None,
        platform: Optional[str] = None,
        os: Optional[str] = None,
        arch: Optional[str] = None,
        category: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    FetchFilesDownloadInfo = fetch_download_info
    FetchFilesDownloadInfoV2 = fetch_download_info_v2
    DownloadFile = download
    EnumerateFile = enumerate
