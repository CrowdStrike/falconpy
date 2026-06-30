"""Type stubs for kubernetes_container_compliance."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class KubernetesContainerCompliance(ServiceClass):

    def aggregate_assessments_by_cluster(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_compliance_by_asset_type(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_compliance_by_cluster_type(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_compliance_by_framework(
        self,
        *,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_failed_rules_by_clusters(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_assessments_by_rules(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def aggregate_top_failed_images(
        self,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def image_findings(
        self,
        *,
        filter: Optional[str] = None,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def node_findings(
        self,
        *,
        filter: Optional[str] = None,
        after: Optional[str] = None,
        limit: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_rules_metadata(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    AggregateAssessmentsGroupedByClustersV2 = aggregate_assessments_by_cluster
    AggregateComplianceByAssetType = aggregate_compliance_by_asset_type
    AggregateComplianceByClusterType = aggregate_compliance_by_cluster_type
    AggregateComplianceByFramework = aggregate_compliance_by_framework
    AggregateFailedRulesByClustersV3 = aggregate_failed_rules_by_clusters
    AggregateFailedRulesByClustersV3 = aggregate_failed_rules_by_clusters
    AggregateAssessmentsGroupedByRulesV2 = aggregate_assessments_by_rules
    AggregateTopFailedImages = aggregate_top_failed_images
    CombinedImagesFindings = image_findings
    CombinedNodesFindings = node_findings
    getRulesMetadataByID = get_rules_metadata
