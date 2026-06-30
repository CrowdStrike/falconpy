"""Type stubs for serverless_exports."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ServerlessExports(ServiceClass):

    def download_export_file(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_export_jobs(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def launch_export_job(
        self,
        *,
        expand_vulnerabilities: Optional[bool] = None,
        format: Optional[str] = None,
        fql: Optional[str] = None,
        resource: Optional[str] = None,
        sort: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_export_jobs(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    DownloadExportFileMixin0 = download_export_file
    ReadExportJobsMixin0 = read_export_jobs
    LaunchExportJobMixin0 = launch_export_job
    QueryExportJobsMixin0 = query_export_jobs
