# test_kubernetes_protection.py
# This class tests the Kubernetes_Protection service class
import os
import sys

# Authentication via the test_authorization.py
from tests import test_authorization as Authorization
# Import our sibling src folder into the path
sys.path.append(os.path.abspath('src'))
# Classes to test - manually imported from sibling folder
from falconpy import KubernetesProtection

auth = Authorization.TestAuthorization()
config = auth.getConfigObject()
falcon = KubernetesProtection(auth_object=config)
AllowedResponses = [200, 201, 207, 400, 404, 403, 406, 429, 500]  # Allowing 500 to reduce flakiness


class TestKubeProtect:
    def serviceKubeProtect_RunAllTests(self):
        error_checks = True
        tests = {
            "GetAWSAccountsMixin0": falcon.get_aws_accounts(limit=1),
            "CreateAWSAccount": falcon.create_aws_account(account_id="12345678", region="us-east-1"),
            "DeleteAWSAccountsMixin0": falcon.delete_aws_accounts(ids='12345678'),  # 403
            "UpdateAWSAccount": falcon.update_aws_account(ids='12345678'),  # 400
            "ListAzureAccounts": falcon.list_azure_accounts(ids="12345678"),
            "CreateAzureSubscription": falcon.create_azure_subscription(subscription_id="whatever",
                                                                        tenant_id="whatever"
                                                                        ),
            "DeleteAzureSubscription": falcon.delete_azure_subscription(ids="12345678"),
            "GetLocations": falcon.get_locations(),
            "GetHelmValuesYaml": falcon.get_helm_values_yaml(cluster_name='Harold'),  # 403
            "RegenerateAPIKey": falcon.regenerate(),  # Occasionally 500
            "GetClusters": falcon.get_clusters(),
            "TriggerScan": falcon.trigger_scan(scan_type='dry-run'),  # 403
            "PatchAzureSubscription": falcon.patch_azure_service_principal(subscription_id="whatever",
                                                                           client_id="whatever"
                                                                           ),
            "GetCombinedCloudClusters": falcon.get_cloud_clusters(ids="123456789"),
            "GetAzureTenantConfig": falcon.get_azure_tenant_config(ids="whatevers"),
            "GetStaticScripts": falcon.get_static_scripts(),
            "GetAzureTenantIDs": falcon.get_azure_tenant_ids(ids="12345678"),
            "GetAzureInstallScript": falcon.get_azure_install_script(ids="123456789"),
            "ReadClustersByDateRangeCount": falcon.read_clusters_by_date_range(),
            "ReadClustersByKubernetesVersionCount": falcon.read_clusters_by_version(filter="whatever"),
            "ReadClustersByStatusCount": falcon.read_clusters_by_status(filter="whatever"),
            "ReadClusterCount": falcon.read_cluster_count(filter="whatever"),
            "ReadContainersByDateRangeCount": falcon.read_containers_by_date_range(filter="whatever"),
            "ReadContainerCountByRegistry": falcon.read_containers_by_registry(filter="whatever"),
            "FindContainersCountAffectedByZeroDayVulnerabilities": falcon.read_zero_day_affected_counts(),
            "ReadVulnerableContainerImageCount": falcon.read_vulnerable_container_count(filter="whatever"),
            "ReadContainerCount": falcon.read_container_counts(filter="whatever"),
            "FindContainersByContainerRunTimeVersion": falcon.find_containers_by_runtime_version(filter="whatever"),
            "GroupContainersByManaged": falcon.group_managed_containers(filter="whatever"),
            "ReadContainerImageDetectionsCountByDate": falcon.read_detections_count_by_date(filter="whatever"),
            "ReadContainerImagesByState": falcon.read_images_by_state(filter="whatever"),
            "ReadContainersSensorCoverage": falcon.read_sensor_coverage(filter="whatever"),
            "ReadContainerVulnerabilitiesBySeverityCount": falcon.read_vulnerability_counts_by_severity(filter="whatever"),
            "ReadDeploymentsByDateRangeCount": falcon.read_deployment_counts_by_date_range(),
            "ReadDeploymentCount": falcon.read_deployment_count(filter="whatever"),
            "ReadClusterEnrichment": falcon.read_cluster_enrichment(filter="whatever"),
            "ReadNodeEnrichment": falcon.read_node_enrichment(filter="whatever"),
            "ReadDistinctContainerImageCount": falcon.read_distinct_image_count(filter="whatever"),
            "ReadContainerImagesByMostUsed": falcon.read_images_by_most_used(filter="whatever"),
            "ReadKubernetesIomByDateRange": falcon.read_iom_count_by_date_range(filter="whatever"),
            "ReadKubernetesIomCount": falcon.read_iom_count(filter="whatever"),
            "ReadNodesByCloudCount": falcon.read_node_counts_by_cloud(filter="whatever"),
            "ReadNodesByContainerEngineVersionCount": falcon.read_nodes_by_container_engine_version(filter="whatever"),
            "ReadNodesByDateRangeCount": falcon.read_node_counts_by_date_range(filter="whatever"),
            "ReadNodeCount": falcon.read_node_counts(filter="whatever"),
            "ReadPodsByDateRangeCount": falcon.read_pod_counts_by_date_range(),
            "ReadPodCount": falcon.read_pod_counts(filter="whatever"),
            "ReadClusterCombined": falcon.read_clusters_combined(filter="whatever"),
            "ReadRunningContainerImages": falcon.read_running_images(filter="whatever"),
            "ReadContainerCombined": falcon.read_containers_combined(filter="whatever"),
            "ReadDeploymentCombined": falcon.read_deployments_combined(filter="whatever"),
            "SearchAndReadKubernetesIomEntities": falcon.search_and_read_ioms(filter="whatever"),
            "ReadNodeCombined": falcon.read_nodes_combined(filter="whatever"),
            "ReadPodCombined": falcon.read_pods_combined(filter="whatever"),
            "ReadKubernetesIomEntities": falcon.read_iom_entities(filter="whatever"),
            "SearchKubernetesIoms": falcon.search_ioms(filter="whatever"),
            "ReadContainerEnrichment": falcon.read_container_enrichment(filter="whatevers"),
            "ReadPodEnrichment": falcon.read_pod_enrichment(filter="something_something_something_darkside"),
            "ReadDeploymentEnrichment": falcon.read_deployment_enrichment(filter="something_else"),
            "ReadNamespacesByDateRangeCount": falcon.read_namespaces_by_date_range_count(),
            "ReadNamespaceCount": falcon.read_namespace_count(filter="something"),
            "ReadClusterCombinedV2": falcon.read_clusters_combined_v2(filter="whatever"),
            "PostSearchKubernetesIOMEntities": falcon.search_kubernetes_ioms(limit=1)
        }

        for key in tests:
            if tests[key]["status_code"] not in AllowedResponses:
                error_checks = False
                # print(f"{tests[key]}")

        return error_checks

    def test_RunAllTests(self):
        assert self.serviceKubeProtect_RunAllTests() is True
