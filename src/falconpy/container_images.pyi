"""Type stubs for container_images."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ContainerImages(ServiceClass):

    def aggregate_assessment_history(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_count_by_base_os(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_count_by_state(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_count(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_combined_base_images(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_combined_images(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_combined_images_by_vulnerability_count(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_combined_detail(
        self,
        *,
        filter: Optional[str] = None,
        with_config: Optional[bool] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_combined_export(
        self,
        *,
        filter: Optional[str] = None,
        expand_vulnerabilities: Optional[bool] = None,
        expand_detections: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_combined_issues_summary(
        self,
        *,
        cid: Optional[str] = None,
        registry: Optional[str] = None,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        image_digest: Optional[str] = None,
        include_base_image_vuln: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_combined_vulnerabilities_summary(
        self,
        *,
        cid: Optional[str] = None,
        registry: Optional[str] = None,
        repository: Optional[str] = None,
        tag: Optional[str] = None,
        image_digest: Optional[str] = None,
        include_base_image_vuln: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_base_images(
        self,
        *,
        base_images: Optional[list] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_base_images(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    AggregateImageAssessmentHistory = aggregate_assessment_history
    AggregateImageCountByBaseOS = aggregate_count_by_base_os
    AggregateImageCountByState = aggregate_count_by_state
    AggregateImageCount = aggregate_count
    GetCombinedImages = get_combined_images
    CombinedBaseImages = get_combined_base_images
    CombinedImageByVulnerabilityCount = get_combined_images_by_vulnerability_count
    CombinedImageDetail = get_combined_detail
    ReadCombinedImagesExport = read_combined_export
    CombinedImageIssuesSummary = get_combined_issues_summary
    CombinedImageVulnerabilitySummary = get_combined_vulnerabilities_summary
    DeleteBaseImages = delete_base_images
