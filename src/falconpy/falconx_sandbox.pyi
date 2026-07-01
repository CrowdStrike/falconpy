"""Type stubs for falconx_sandbox."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class FalconXSandbox(ServiceClass):

    def get_artifacts(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        name: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_dump_extracted_strings(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        name: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_hex_dump(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        name: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_memory_dump(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        name: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_summary_reports(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_submissions(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def submit(
        self,
        *,
        aid: Optional[str] = None,
        auto_detect_environment: Optional[bool] = None,
        sandbox: Optional[list] = None,
        send_email_notification: Optional[bool] = None,
        user_tags: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_reports(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_submissions(
        self,
        *,
        filter: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def upload_sample(
        self,
        *,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_reports(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_report(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_sample(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        password_protected: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_sample(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def query_sample(
        self,
        *,
        sha256s: Optional[Union[str, List[str]]] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    GetArtifacts = get_artifacts
    GetSummaryReports = get_summary_reports
    GetSubmissions = get_submissions
    Submit = submit
    QueryReports = query_reports
    QuerySubmissions = query_submissions
    UploadSampleV2 = upload_sample
    GetReports = get_reports
    DeleteReport = delete_report
    GetSampleV2 = get_sample
    DeleteSampleV2 = delete_sample
    QuerySampleV1 = query_sample
    GetMemoryDumpExtractedStrings = get_dump_extracted_strings
    GetMemoryDumpHexDump = get_hex_dump
    GetMemoryDump = get_memory_dump
