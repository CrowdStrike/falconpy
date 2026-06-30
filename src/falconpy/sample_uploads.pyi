"""Type stubs for sample_uploads."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class SampleUploads(ServiceClass):

    def list_archive(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_archive(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        include_files: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_archive(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def upload_archive_v1(
        self,
        *,
        name: Optional[str] = None,
        password: Optional[str] = None,
        is_confidential: Optional[bool] = None,
        comment: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def upload_archive(
        self,
        *,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_extraction(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_extraction(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        include_files: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_extraction(
        self,
        *,
        extract_all: Optional[bool] = None,
        files: Optional[list] = None,
        sha256: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_sample(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        password_protected: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def upload_sample(
        self,
        *,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_sample(
        self,
        *args: Union[str, List[str]],
        ids: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ArchiveListV1 = list_archive
    ArchiveGetV1 = get_archive
    ArchiveDeleteV1 = delete_archive
    ArchiveUploadV1 = upload_archive_v1
    archive_upload_v1 = upload_archive_v1
    ArchiveUploadV2 = upload_archive
    archive_upload = upload_archive
    ExtractionListV1 = list_extraction
    ExtractionGetV1 = get_extraction
    ExtractionCreateV1 = create_extraction
    GetSampleV3 = get_sample
    UploadSampleV3 = upload_sample
    DeleteSampleV3 = delete_sample
