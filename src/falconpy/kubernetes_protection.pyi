"""Type stubs for kubernetes_protection."""
from typing import Dict, List, Optional, Union
from ._service_class import ServiceClass
from ._result import Result


class KubernetesProtection(ServiceClass):

    def read_clusters_by_date_range(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_clusters_by_version(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_clusters_by_status(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_cluster_count(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_containers_by_date_range(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_containers_by_registry(
        self,
        *,
        under_assessment: Optional[bool] = None,
        limit: Optional[int] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_zero_day_affected_counts(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_vulnerable_container_count(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_container_counts(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def find_containers_by_runtime_version(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def group_managed_containers(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_detections_count_by_date(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_images_by_state(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_sensor_coverage(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_namespace_count(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_namespaces_by_date_range_count(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_vulnerability_counts_by_severity(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_deployment_counts_by_date_range(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_deployment_count(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_cluster_enrichment(
        self,
        *,
        cluster_id: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_container_enrichment(
        self,
        *,
        container_id: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_pod_enrichment(
        self,
        *,
        pod_id: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_deployment_enrichment(
        self,
        *,
        deployment_id: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_node_enrichment(
        self,
        *,
        node_name: Optional[Union[str, List[str]]] = None,
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_distinct_image_count(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_images_by_most_used(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_iom_count_by_date_range(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_iom_count(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_node_counts_by_cloud(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_nodes_by_container_engine_version(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_node_counts_by_date_range(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_node_count(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_pod_counts_by_date_range(
        self,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_pod_counts(
        self,
        *args: Union[str, List[str]],
        filter: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_clusters_combined(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_clusters_combined_v2(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        include_counts: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_running_images(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_containers_combined(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_deployments_combined(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_kubernetes_ioms(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        pit: Optional[str] = None,
        search_after: Optional[list] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_and_read_ioms(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_nodes_combined(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_pods_combined(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def read_iom_entities(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def search_ioms(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_aws_accounts(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        is_horizon_acct: Optional[str] = None,
        status: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_aws_account(
        self,
        *,
        account_id: Optional[str] = None,
        region: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_aws_accounts(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_aws_account(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        region: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def list_azure_accounts(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        subscription_id: Optional[Union[str, List[str]]] = None,
        status: Optional[str] = None,
        is_horizon_acct: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def create_azure_subscription(
        self,
        *,
        subscription_id: Optional[str] = None,
        tenant_id: Optional[str] = None,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def delete_azure_subscription(
        self,
        *args: Union[str, List[str]],
        ids: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_locations(
        self,
        *args: Union[str, List[str]],
        clouds: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_cloud_clusters(
        self,
        *,
        locations: Optional[Union[str, List[str]]] = None,
        ids: Optional[Union[str, List[str]]] = None,
        cluster_service: Optional[Union[str, List[str]]] = None,
        cluster_status: Optional[Union[str, List[str]]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_azure_tenant_config(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_azure_tenant_ids(
        self,
        *,
        ids: Optional[Union[str, List[str]]] = None,
        status: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_azure_install_script(
        self,
        *,
        id: Optional[str] = None,
        subscription_id: Optional[Union[str, List[str]]] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_static_scripts(
        self,
        *,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_helm_values_yaml(
        self,
        *args: Union[str, List[str]],
        cluster_name: Optional[str] = None,
        is_self_managed_cluster: Optional[bool] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def regenerate(
        self,
        *,
        body: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def get_clusters(
        self,
        *,
        cluster_names: Optional[Union[str, List[str]]] = None,
        status: Optional[Union[str, List[str]]] = None,
        account_ids: Optional[Union[str, List[str]]] = None,
        locations: Optional[Union[str, List[str]]] = None,
        cluster_service: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def trigger_scan(
        self,
        *args: Union[str, List[str]],
        scan_type: Optional[str] = None,
        body: Optional[dict] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    def update_azure_service_principal(
        self,
        *args: Union[str, List[str]],
        id: Optional[str] = None,
        client_id: Optional[str] = None,
        parameters: Optional[dict] = None,
    ) -> Union[Dict[str, Union[int, dict]], Result]: ...

    ReadClustersByDateRangeCount = read_clusters_by_date_range
    ReadClustersByKubernetesVersionCount = read_clusters_by_version
    ReadClustersByStatusCount = read_clusters_by_status
    ReadClusterCount = read_cluster_count
    ReadContainersByDateRangeCount = read_containers_by_date_range
    ReadContainerCountByRegistry = read_containers_by_registry
    FindContainersCountAffectedByZeroDayVulnerabilities = read_zero_day_affected_counts
    ReadVulnerableContainerImageCount = read_vulnerable_container_count
    ReadContainerCount = read_container_counts
    ReadNamespacesByDateRangeCount = read_namespaces_by_date_range_count
    ReadNamespaceCount = read_namespace_count
    FindContainersByContainerRunTimeVersion = find_containers_by_runtime_version
    GroupContainersByManaged = group_managed_containers
    ReadContainerImageDetectionsCountByDate = read_detections_count_by_date
    ReadContainerImagesByState = read_images_by_state
    ReadContainersSensorCoverage = read_sensor_coverage
    ReadContainerVulnerabilitiesBySeverityCount = read_vulnerability_counts_by_severity
    ReadDeploymentsByDateRangeCount = read_deployment_counts_by_date_range
    ReadDeploymentCount = read_deployment_count
    ReadClusterEnrichment = read_cluster_enrichment
    ReadContainerEnrichment = read_container_enrichment
    ReadPodEnrichment = read_pod_enrichment
    ReadDeploymentEnrichment = read_deployment_enrichment
    ReadNodeEnrichment = read_node_enrichment
    ReadDistinctContainerImageCount = read_distinct_image_count
    ReadContainerImagesByMostUsed = read_images_by_most_used
    ReadKubernetesIomByDateRange = read_iom_count_by_date_range
    ReadKubernetesIomCount = read_iom_count
    ReadNodesByCloudCount = read_node_counts_by_cloud
    ReadNodesByContainerEngineVersionCount = read_nodes_by_container_engine_version
    ReadNodesByDateRangeCount = read_node_counts_by_date_range
    ReadNodeCount = read_node_count
    read_node_counts = read_node_count
    ReadPodsByDateRangeCount = read_pod_counts_by_date_range
    ReadPodCount = read_pod_counts
    ReadClusterCombined = read_clusters_combined
    ReadClusterCombinedV2 = read_clusters_combined_v2
    ReadRunningContainerImages = read_running_images
    ReadContainerCombined = read_containers_combined
    ReadDeploymentCombined = read_deployments_combined
    PostSearchKubernetesIOMEntities = search_kubernetes_ioms
    SearchAndReadKubernetesIomEntities = search_and_read_ioms
    ReadNodeCombined = read_nodes_combined
    ReadPodCombined = read_pods_combined
    ReadKubernetesIomEntities = read_iom_entities
    SearchKubernetesIoms = search_ioms
    GetAWSAccountsMixin0 = get_aws_accounts
    GetAWSAccounts = get_aws_accounts
    CreateAWSAccount = create_aws_account
    DeleteAWSAccountsMixin0 = delete_aws_accounts
    DeleteAWSAccounts = delete_aws_accounts
    UpdateAWSAccount = update_aws_account
    ListAzureAccounts = list_azure_accounts
    CreateAzureSubscription = create_azure_subscription
    DeleteAzureSubscription = delete_azure_subscription
    GetLocations = get_locations
    GetCombinedCloudClusters = get_cloud_clusters
    GetAzureTenantConfig = get_azure_tenant_config
    GetAzureTenantIDs = get_azure_tenant_ids
    GetAzureInstallScript = get_azure_install_script
    GetStaticScripts = get_static_scripts
    GetHelmValuesYaml = get_helm_values_yaml
    regenerate_api_key = regenerate
    RegenerateAPIKey = regenerate
    GetClusters = get_clusters
    TriggerScan = trigger_scan
    PatchAzureServicePrincipal = update_azure_service_principal
    patch_azure_service_principal = update_azure_service_principal
