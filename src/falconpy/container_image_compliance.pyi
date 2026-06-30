"""Type stubs for container_image_compliance."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class ContainerImageCompliance(ServiceClass):

    def aggregate_cluster_assessments(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_image_assessments(
        self,
        *,
        filter: Optional[str] = None,
        after: Optional[str] = None,
        limit: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_rules_assessments(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_failed_containers_by_rules(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_failed_containers_count_by_severity(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_failed_images_by_rules(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_failed_images_count_by_severity(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_failed_rules_by_clusters(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_failed_rules_by_image(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_failed_rules_count_by_severity(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_rules_by_status(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    extAggregateClusterAssessments = aggregate_cluster_assessments
    extAggregateImageAssessments = aggregate_image_assessments
    extAggregateRulesAssessments = aggregate_rules_assessments
    extAggregateFailedContainersByRulesPath = aggregate_failed_containers_by_rules
    extAggregateFailedContainersCountBySeverity = aggregate_failed_containers_count_by_severity
    extAggregateFailedImagesByRulesPath = aggregate_failed_images_by_rules
    extAggregateFailedImagesCountBySeverity = aggregate_failed_images_count_by_severity
    extAggregateFailedRulesByClusters = aggregate_failed_rules_by_clusters
    extAggregateFailedRulesByImages = aggregate_failed_rules_by_image
    extAggregateFailedRulesCountBySeverity = aggregate_failed_rules_count_by_severity
    extAggregateRulesByStatus = aggregate_rules_by_status
