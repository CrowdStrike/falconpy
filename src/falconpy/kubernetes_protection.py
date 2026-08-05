"""CrowdStrike Falcon Kubernetes Protection API interface class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
# pylint: disable=C0302, R0904
from typing import Dict, Union
from ._util import process_service_request, force_default, handle_single_argument
from ._payload import aggregate_payload
from ._result import Result
from ._service_class import ServiceClass
from ._endpoint._kubernetes_protection import _kubernetes_protection_endpoints as Endpoints


class KubernetesProtection(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (OAuth2.token())
    """

    def read_clusters_by_date_range(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve clusters by date range counts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadClustersByDateRangeCount

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.
        This method does not accept arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadClustersByDateRangeCount"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_clusters_by_version(self: object,
                                 *args,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Bucket clusters by kubernetes version.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /kubernetes-protection/ReadClustersByKubernetesVersionCount

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes clusters that match a query in Falcon Query Language (FQL). String.
            Supported filters:
              access              cluster_status
              agent_id            container_count
              agent_status        iar_coverage
              agent_type          kac_agent_id
              cid                 kubernetes_version
              cloud_account_id    last_seen
              cloud_name          management_status
              cloud_region        node_count
              cloud_service       pod_count
              cluster_id          tags
              cluster_name        pod_name
              namespace
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadClustersByKubernetesVersionCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_clusters_by_status(self: object,
                                *args,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Bucket clusters by status.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadClustersByStatusCount

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes clusters that match a query in Falcon Query Language (FQL). String.
            Supported filters:
              access              cluster_status
              agent_id            container_count
              agent_status        iar_coverage
              agent_type          kac_agent_id
              cid                 kubernetes_version
              cloud_account_id    last_seen
              cloud_name          management_status
              cloud_region        node_count
              cloud_service       pod_count
              cluster_id          tags
              cluster_name        pod_name
              namespace
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadClustersByStatusCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_cluster_count(self: object,
                           *args,
                           parameters: dict = None,
                           **kwargs
                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve cluster counts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadClusterCount

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes clusters that match a query in Falcon Query Language (FQL). String.
            Supported filters:
              access              cluster_status
              agent_id            container_count
              agent_status        iar_coverage
              agent_type          kac_agent_id
              cid                 kubernetes_version
              cloud_account_id    last_seen
              cloud_name          management_status
              cloud_region        node_count
              cloud_service       pod_count
              cluster_id          tags
              cluster_name        pod_name
              namespace
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadClusterCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_containers_by_date_range(self: object,
                                      *args,
                                      parameters: dict = None,
                                      **kwargs
                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve containers by date range counts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadContainersByDateRangeCount

        Keyword arguments
        -----------------
        filter : str
            Get container counts using a query in Falcon Query Language (FQL). String.
            Supported filters:
              agent_id                    image_vulnerability_count
              agent_type                  insecure_mount_source
              allow_privilege_escalation  insecure_mount_type
              cid                         insecure_propagation_mode
              cloud_account_id            interactive_mode
              cloud_name                  ipv4
              cloud_region                ipv6
              cluster_id                  labels
              cluster_name                last_seen
              container_id                namespace
              container_name              node_name
              cve_id                      node_uid
              detection_name              package_name_version
              first_seen                  pod_id
              image_detection_count       pod_name
              image_digest                port
              image_has_been_assessed     privileged
              image_id                    root_write_access
              image_registry              run_as_root_group
              image_repository            run_as_root_user
              image_tag                   running_status
              ai_related
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadContainersByDateRangeCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_containers_by_registry(self: object,
                                    parameters: dict = None,
                                    **kwargs
                                    ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve top container image registries.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadContainerCountByRegistry

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes container image registries that match a query in
            Falcon Query Language (FQL). String.
            Supported filter fields:
              agent_id                        image_repository
              agent_type                      image_tag
              ai_related                      image_vulnerability_count
              allow_privilege_escalation      insecure_mount_source
              app_name                        insecure_mount_type
              cid                             insecure_propagation_mode
              cloud_account_id                interactive_mode
              cloud_instance_id               ipv4
              cloud_name                      ipv6
              cloud_region                    kac_agent_id
              cloud_service                   labels
              cluster_id                      last_seen
              cluster_name                    namespace
              container_id                    node_name
              container_image_id              node_uid
              container_name                  package_name_version
              cve_id                          pod_id
              detection_name                  pod_name
              first_seen                      port
              image_detection_count           privileged
              image_digest                    root_write_access
              image_has_been_assessed         run_as_root_group
              image_id                        run_as_root_user
              image_registry                  running_status
        under_assessment : bool
            Flag indicating whether to return registries under assessment or not under assessment.
            If not provided all registries are considered. Boolean. Defaults to False.
        limit : int
            The upper-bound on the number of records to retrieve.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadContainerCountByRegistry",
            keywords=kwargs,
            params=parameters
            )

    def read_zero_day_affected_counts(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve containers count affected by zero day vulnerabilities.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /kubernetes-protection/FindContainersCountAffectedByZeroDayVulnerabilities

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.
        This method does not accept arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="FindContainersCountAffectedByZeroDayVulnerabilities"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_vulnerable_container_count(self: object,
                                        *args,
                                        parameters: dict = None,
                                        **kwargs
                                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve count of vulnerable images running on containers.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /kubernetes-protection/ReadVulnerableContainerImageCount

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). String.
            Supported filters:
              agent_id                    image_vulnerability_count
              agent_type                  insecure_mount_source
              allow_privilege_escalation  insecure_mount_type
              cid                         insecure_propagation_mode
              cloud_account_id            interactive_mode
              cloud_name                  ipv4
              cloud_region                ipv6
              cluster_id                  labels
              cluster_name                last_seen
              container_id                namespace
              container_name              node_name
              cve_id                      node_uid
              detection_name              package_name_version
              first_seen                  pod_id
              image_detection_count       pod_name
              image_digest                port
              image_has_been_assessed     privileged
              image_id                    root_write_access
              image_registry              run_as_root_group
              image_repository            run_as_root_user
              image_tag                   running_status
              ai_related
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadVulnerableContainerImageCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_container_counts(self: object,
                              *args,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve container counts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadContainerCount

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). String.
            Supported filters:
              agent_id                    image_vulnerability_count
              agent_type                  insecure_mount_source
              allow_privilege_escalation  insecure_mount_type
              cid                         insecure_propagation_mode
              cloud_account_id            interactive_mode
              cloud_name                  ipv4
              cloud_region                ipv6
              cluster_id                  labels
              cluster_name                last_seen
              container_id                namespace
              container_name              node_name
              cve_id                      node_uid
              detection_name              package_name_version
              first_seen                  pod_id
              image_detection_count       pod_name
              image_digest                port
              image_has_been_assessed     privileged
              image_id                    root_write_access
              image_registry              run_as_root_group
              image_repository            run_as_root_user
              image_tag                   running_status
              ai_related
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadContainerCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def find_containers_by_runtime_version(self: object,
                                           parameters: dict = None,
                                           **kwargs
                                           ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve containers by container_runtime_version.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /kubernetes-protection/FindContainersByContainerRunTimeVersion

        Keyword arguments
        -----------------
        limit : int
            The upper-bound on the number of container records to retrieve.
        offset : int
            It is used to get the offset
        sort : str
            Field to sort results by
        filter : str
            Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). String.
            Supported filters:
              agent_id                    image_vulnerability_count
              agent_type                  insecure_mount_source
              allow_privilege_escalation  insecure_mount_type
              cid                         insecure_propagation_mode
              cloud_account_id            interactive_mode
              cloud_name                  ipv4
              cloud_region                ipv6
              cluster_id                  labels
              cluster_name                last_seen
              container_id                namespace
              container_name              node_name
              cve_id                      node_uid
              detection_name              package_name_version
              first_seen                  pod_id
              image_detection_count       pod_name
              image_digest                port
              image_has_been_assessed     privileged
              image_id                    root_write_access
              image_registry              run_as_root_group
              image_repository            run_as_root_user
              image_tag                   running_status
              ai_related
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="FindContainersByContainerRunTimeVersion",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def group_managed_containers(self: object,
                                 *args,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Group the containers by Managed.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GroupContainersByManaged

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). String.
            Supported filters:
              agent_id                    image_vulnerability_count
              agent_type                  insecure_mount_source
              allow_privilege_escalation  insecure_mount_type
              cid                         insecure_propagation_mode
              cloud_account_id            interactive_mode
              cloud_name                  ipv4
              cloud_region                ipv6
              cluster_id                  labels
              cluster_name                last_seen
              container_id                namespace
              container_name              node_name
              cve_id                      node_uid
              detection_name              package_name_version
              first_seen                  pod_id
              image_detection_count       pod_name
              image_digest                port
              image_has_been_assessed     privileged
              image_id                    root_write_access
              image_registry              run_as_root_group
              image_repository            run_as_root_user
              image_tag                   running_status
              ai_related
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GroupContainersByManaged",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_detections_count_by_date(self: object,
                                      *args,
                                      parameters: dict = None,
                                      **kwargs
                                      ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve count of image assessment detections on running containers over a period of time.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /kubernetes-protection/ReadContainerImageDetectionsCountByDate

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). String.
            Supported filters:
              agent_id                    image_vulnerability_count
              agent_type                  insecure_mount_source
              allow_privilege_escalation  insecure_mount_type
              cid                         insecure_propagation_mode
              cloud_account_id            interactive_mode
              cloud_name                  ipv4
              cloud_region                ipv6
              cluster_id                  labels
              cluster_name                last_seen
              container_id                namespace
              container_name              node_name
              cve_id                      node_uid
              detection_name              package_name_version
              first_seen                  pod_id
              image_detection_count       pod_name
              image_digest                port
              image_has_been_assessed     privileged
              image_id                    root_write_access
              image_registry              run_as_root_group
              image_repository            run_as_root_user
              image_tag                   running_status
              ai_related
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadContainerImageDetectionsCountByDate",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_images_by_state(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve count of image states running on containers.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadContainerImagesByState

        Keyword arguments
        -----------------
        filter : str
            Filter using a query in Falcon Query Language (FQL). String.
            Supported filters: cid
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadContainerImagesByState",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_sensor_coverage(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Bucket containers by agent type and calculate sensor coverage.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadContainersSensorCoverage

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). String.
            Supported filters:
              agent_id                    image_vulnerability_count
              agent_type                  insecure_mount_source
              allow_privilege_escalation  insecure_mount_type
              cid                         insecure_propagation_mode
              cloud_account_id            interactive_mode
              cloud_name                  ipv4
              cloud_region                ipv6
              cluster_id                  labels
              cluster_name                last_seen
              container_id                namespace
              container_name              node_name
              cve_id                      node_uid
              detection_name              package_name_version
              first_seen                  pod_id
              image_detection_count       pod_name
              image_digest                port
              image_has_been_assessed     privileged
              image_id                    root_write_access
              image_registry              run_as_root_group
              image_repository            run_as_root_user
              image_tag                   running_status
              ai_related
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadContainersSensorCoverage",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_namespace_count(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Bucket containers by agent type and calculate sensor coverage.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadNamespaceCount

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). String.
            Supported filters:
            agent_id              cluster_id
            agent_type            cluster_name
            annotations_list      first_seen
            cid                   kac_agent_id
            cloud_account_id      last_seen
            cloud_name            namespace_id
            cloud_region          namespace_name
            cloud_service         resource_status
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadNamespaceCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    def read_namespaces_by_date_range_count(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve namespaces by date range count.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadNamespacesByDateRangeCount

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.
        This method does not accept arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadNamespacesByDateRangeCount"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_vulnerability_counts_by_severity(self: object,
                                              *args,
                                              parameters: dict = None,
                                              **kwargs
                                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve container vulnerabilities by severity counts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /kubernetes-protection/ReadContainerVulnerabilitiesBySeverityCount

        Keyword arguments
        -----------------
        filter : str
            Get vulnerabilities count by severity for container using a query in Falcon Query Language (FQL). String.
            Supported filters:
              agent_id                    image_vulnerability_count
              agent_type                  insecure_mount_source
              allow_privilege_escalation  insecure_mount_type
              cid                         insecure_propagation_mode
              cloud_account_id            interactive_mode
              cloud_name                  ipv4
              cloud_region                ipv6
              cluster_id                  labels
              cluster_name                last_seen
              container_id                namespace
              container_name              node_name
              cve_id                      node_uid
              detection_name              package_name_version
              first_seen                  pod_id
              image_detection_count       pod_name
              image_digest                port
              image_has_been_assessed     privileged
              image_id                    root_write_access
              image_registry              run_as_root_group
              image_repository            run_as_root_user
              image_tag                   running_status
              ai_related
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadContainerVulnerabilitiesBySeverityCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    def read_deployment_counts_by_date_range(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve deployments by date range counts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadDeploymentsByDateRangeCount

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.
        This method does not accept arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadDeploymentsByDateRangeCount"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_deployment_count(self: object,
                              *args,
                              parameters: dict = None,
                              **kwargs
                              ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve deployment counts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadDeploymentCount

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes deployments that match a query in Falcon Query Language (FQL). String.
            Supported filters:
              annotations_list    deployment_id
              cid                 deployment_name
              cloud_account_id    first_seen
              cloud_name          last_seen
              cloud_region        namespace
              cluster_id          pod_count
              cluster_name
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadDeploymentCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_cluster_enrichment(self: object,
                                parameters: dict = None,
                                **kwargs
                                ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve cluster enrichment data.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadClusterEnrichment

        Keyword arguments
        -----------------
        cluster_id : str or list[str]
            One or more cluster ids for which to retrieve enrichment info
        filter : str
            Supported filters:  cloud_account_id, cloud_name, cloud_region, cluster_id,
            cluster_name, last_seen, namespace
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadClusterEnrichment",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_container_enrichment(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve container enrichment data.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadContainerEnrichment

        Keyword arguments
        -----------------
        container_id : str or list[str]
            One or more container ids for which to retrieve enrichment info
        filter : str
            Supported filters:  cloud_account_id, cloud_name, cloud_region, cluster_id,
            cluster_name, last_seen, namespace
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadContainerEnrichment",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_pod_enrichment(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve pod enrichment data.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadPodEnrichment

        Keyword arguments
        -----------------
        pod_id : str or list[str]
            One or more pod ids for which to retrieve enrichment info
        filter : str
            Supported filters:  cloud_account_id, cloud_name, cloud_region, cluster_id,
            cluster_name, last_seen, namespace
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadPodEnrichment",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_deployment_enrichment(self: object,
                                   parameters: dict = None,
                                   **kwargs
                                   ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve deployment enrichment data.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadDeploymentEnrichment

        Keyword arguments
        -----------------
        deployment_id : str or list[str]
            One or more deployment ids for which to retrieve enrichment info
        filter : str
            Supported filters:  cloud_account_id, cloud_name, cloud_region, cluster_id,
            cluster_name, last_seen, namespace
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadDeploymentEnrichment",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_node_enrichment(self: object,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve node enrichment data.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadNodeEnrichment

        Keyword arguments
        -----------------
        node_name : str or list[str]
            One or more node names for which to retrieve enrichment info
        filter : str
            Supported filters:  cloud_account_id, cloud_name, cloud_region, cluster_id,
            cluster_name, last_seen, namespace
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadNodeEnrichment",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_distinct_image_count(self: object,
                                  *args,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve count of distinct images running on containers.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadDistinctContainerImageCount

        Keyword arguments
        -----------------
        filter : str
            Search Kubernetes containers using a query in Falcon Query Language (FQL). String.
            Supported filters:
              agent_id                    image_vulnerability_count
              agent_type                  insecure_mount_source
              allow_privilege_escalation  insecure_mount_type
              cid                         insecure_propagation_mode
              cloud_account_id            interactive_mode
              cloud_name                  ipv4
              cloud_region                ipv6
              cluster_id                  labels
              cluster_name                last_seen
              container_id                namespace
              container_name              node_name
              cve_id                      node_uid
              detection_name              package_name_version
              first_seen                  pod_id
              image_detection_count       pod_name
              image_digest                port
              image_has_been_assessed     privileged
              image_id                    root_write_access
              image_registry              run_as_root_group
              image_repository            run_as_root_user
              image_tag                   running_status
              ai_related
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadDistinctContainerImageCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_images_by_most_used(self: object,
                                 *args,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Bucket container by image-digest.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadContainerImagesByMostUsed

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). String.
            Supported filters:
              agent_id                    image_vulnerability_count
              agent_type                  insecure_mount_source
              allow_privilege_escalation  insecure_mount_type
              cid                         insecure_propagation_mode
              cloud_account_id            interactive_mode
              cloud_name                  ipv4
              cloud_region                ipv6
              cluster_id                  labels
              cluster_name                last_seen
              container_id                namespace
              container_name              node_name
              cve_id                      node_uid
              detection_name              package_name_version
              first_seen                  pod_id
              image_detection_count       pod_name
              image_digest                port
              image_has_been_assessed     privileged
              image_id                    root_write_access
              image_registry              run_as_root_group
              image_repository            run_as_root_user
              image_tag                   running_status
              ai_related
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadContainerImagesByMostUsed",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_iom_count_by_date_range(self: object,
                                     *args,
                                     parameters: dict = None,
                                     **kwargs
                                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return the count of Kubernetes IOMs by the date. by default it's for 7 days.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadKubernetesIomByDateRange

        Keyword arguments
        -----------------
        filter : str
            Filter images using a query in Falcon Query Language (FQL). String.
            Supported filters: cid, created_timestamp, detect_timestamp, prevented, severity
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadKubernetesIomByDateRange",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_iom_count(self: object,
                       *args,
                       parameters: dict = None,
                       **kwargs
                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return the total count of Kubernetes IOMs over the past seven days.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadKubernetesIomCount

        Keyword arguments
        -----------------
        filter : str
            Filter images using a query in Falcon Query Language (FQL). String.
            Supported filters: cid, created_timestamp, detect_timestamp, prevented, severity
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadKubernetesIomCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_node_counts_by_cloud(self: object,
                                  *args,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Bucket nodes by cloud providers.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadNodesByCloudCount

        Keyword arguments
        -----------------
        filter : str
            Search Kubernetes nodes using a query in Falcon Query Language (FQL). String.
            Supported filters:
              aid                 container_count
              annotations_list    container_runtime_version
              cid                 first_seen
              cloud_account_id    image_digest
              cloud_name          ipv4
              cloud_region        last_seen
              cluster_id          node_name
              cluster_name        pod_count
              node_uid
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadNodesByCloudCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_nodes_by_container_engine_version(self: object,
                                               *args,
                                               parameters: dict = None,
                                               **kwargs
                                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Bucket nodes by their container engine version.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /kubernetes-protection/ReadNodesByContainerEngineVersionCount

        Keyword arguments
        -----------------
        filter : str
            Search Kubernetes nodes using a query in Falcon Query Language (FQL). String.
            Supported filters:
              aid                 container_count
              annotations_list    container_runtime_version
              cid                 first_seen
              cloud_account_id    image_digest
              cloud_name          ipv4
              cloud_region        last_seen
              cluster_id          node_name
              cluster_name        pod_count
              node_uid
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadNodesByContainerEngineVersionCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_node_counts_by_date_range(self: object,
                                       *args,
                                       parameters: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve nodes by date range counts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadNodesByDateRangeCount

        Keyword arguments
        -----------------
        filter : str
            Search Kubernetes nodes using a query in Falcon Query Language (FQL). String.
            Supported filters:
              aid                 container_count
              annotations_list    container_runtime_version
              cid                 first_seen
              cloud_account_id    image_digest
              cloud_name          ipv4
              cloud_region        last_seen
              cluster_id          node_name
              cluster_name        pod_count
              node_uid
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadNodesByDateRangeCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_node_count(self: object,
                        *args,
                        parameters: dict = None,
                        **kwargs
                        ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve node counts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadNodeCount

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes nodes that match a query in Falcon Query Language (FQL). String.
            Supported filters:
              aid                 container_count
              annotations_list    container_runtime_version
              cid                 first_seen
              cloud_account_id    image_digest
              cloud_name          ipv4
              cloud_region        last_seen
              cluster_id          node_name
              cluster_name        pod_count
              node_uid
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadNodeCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    def read_pod_counts_by_date_range(self: object) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve pods by date range counts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadPodsByDateRangeCount

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.
        This method does not accept arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadPodsByDateRangeCount"
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_pod_counts(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve pod counts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadPodCount

        Keyword arguments
        -----------------
        filter : str
            Retrieve count of Kubernetes pods that match a query in Falcon Query Language (FQL). String.
            Supported filters:
              agent_id                    last_seen
              agent_type                  namespace
              allow_privilege_escalation  node_name
              annotations_list            node_uid
              cid                         owner_id
              cloud_account_id            owner_type
              cloud_name                  pod_id
              cloud_region                pod_name
              cluster_id                  port
              cluster_name                privileged
              container_count             root_write_access
              ipv4                        run_as_root_group
              ipv6                        run_as_root_user
              labels
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'filter'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadPodCount",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "filter")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_clusters_combined(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve kubernetes clusters identified by the provided filter criteria.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadClusterCombined

        Keyword arguments
        -----------------
        filter : str
            Search Kubernetes clusters using a query in Falcon Query Language (FQL). String.
            Supported filters:
              access              cluster_status
              agent_id            container_count
              agent_status        iar_coverage
              agent_type          kac_agent_id
              cid                 kubernetes_version
              cloud_account_id    last_seen
              cloud_name          management_status
              cloud_region        node_count
              cloud_service       pod_count
              cluster_id          tags
              cluster_name        pod_name
              namespace
        limit : int
            The upper-bound on the number of records to retrieve.
        offset : int
            The offset from where to begin.
        sort : str
            Field to sort results by.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadClusterCombined",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_clusters_combined_v2(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve kubernetes clusters identified by the provided filter criteria.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadClusterCombinedV2

        Keyword arguments
        -----------------
        filter : str
            Search Kubernetes clusters using a query in Falcon Query Language (FQL). String.
            Supported filters:
              access              cluster_status
              agent_id            container_count
              agent_status        iar_coverage
              agent_type          kac_agent_id
              cid                 kubernetes_version
              cloud_account_id    last_seen
              cloud_name          management_status
              cloud_region        node_count
              cloud_service       pod_count
              cluster_id          tags
              cluster_name        pod_name
              namespace
        include_counts : bool
            Flag to include node, pod and container counts in the response.
        limit : int
            The upper-bound on the number of records to retrieve.
        offset : int
            The offset from where to begin.
        sort : str
            Field to sort results by.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadClusterCombinedV2",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_running_images(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve images on running containers.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadRunningContainerImages

        Keyword arguments
        -----------------
        filter : str
            Retrieve list of images on running containers using a query in Falcon Query Language (FQL). String.
            Supported filters:
              cid                         image_registry
              cloud_account_id            image_repository
              cloud_name                  image_tag
              cloud_region                last_seen
              cluster_id                  namespace
              cluster_name                running_status
              hosts
              image_digest
              image_has_been_assessed
              image_id
              image_name
        limit : int
            The upper-bound on the number of records to retrieve.
        offset : int
            The offset from where to begin.
        sort : str
            Field to sort results by.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadRunningContainerImages",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_containers_combined(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve containers identified by the provided filter criteria.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadContainerCombined

        Keyword arguments
        -----------------
        filter : str
            Search Kubernetes containers using a query in Falcon Query Language (FQL). String.
            Supported filters:
              agent_id                    image_vulnerability_count
              agent_type                  insecure_mount_source
              allow_privilege_escalation  insecure_mount_type
              cid                         insecure_propagation_mode
              cloud_account_id            interactive_mode
              cloud_name                  ipv4
              cloud_region                ipv6
              cluster_id                  labels
              cluster_name                last_seen
              container_id                namespace
              container_name              node_name
              cve_id                      node_uid
              detection_name              package_name_version
              first_seen                  pod_id
              image_detection_count       pod_name
              image_digest                port
              image_has_been_assessed     privileged
              image_id                    root_write_access
              image_registry              run_as_root_group
              image_repository            run_as_root_user
              image_tag                   running_status
              ai_related
        limit : int
            The upper-bound on the number of records to retrieve.
        offset : int
            The offset from where to begin.
        sort : str
            Field to sort results by.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadContainerCombined",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_deployments_combined(self: object,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve kubernetes deployments identified by the provided filter criteria.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadDeploymentCombined

        Keyword arguments
        -----------------
        filter : str
            Search Kubernetes deployments using a query in Falcon Query Language (FQL). String.
            Supported filters:
              annotations_list    deployment_id
              cid                 deployment_name
              cloud_account_id    first_seen
              cloud_name          last_seen
              cloud_region        namespace
              cluster_id          pod_count
              cluster_name
        limit : int
            The upper-bound on the number of records to retrieve.
        offset : int
            The offset from where to begin.
        sort : str
            Field to sort results by.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadDeploymentCombined",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body", "parameters"], default_types=["dict", "dict"])
    def search_kubernetes_ioms(self: object,
                               body: dict = None,
                               parameters: dict = None,
                               **kwargs
                               ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search for Kubernetes IOMs with filtering options.

        Pagination is supported via Elasticsearch's search_after search param and point in time.
        Assets are sorted by unique ID in ascending direction.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/PostSearchKubernetesIOMEntities

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted dictionary. Not required if using other keywords.
                {
                    "pit": "string",
                    "search_after": [
                        null
                    ]
                }
        filter : str
            Search Kubernetes IOMs using a query in Falcon Query Language (FQL). String.
            Supported filter fields:
              cid                                   cis_id
              cluster_id                            cluster_name
              containers_impacted_ai_related        containers_impacted_count
              containers_impacted_ids               detection_type
              name                                  namespace
              prevented                             resource_id
              resource_name                         resource_type
              severity
        sort : str
            The fields to sort the records on. FQL Format.
        limit : int
            Maximum number of records to return. Integer. Default: 100, Max: 500
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            if kwargs.get("pit", None):
                body["pit"] = kwargs.get("pit", None)
            if kwargs.get("search_after", None):
                search_after = kwargs.get("search_after", None)
                if isinstance(search_after, str):
                    search_after = search_after.split(",")
                body["search_after"] = search_after
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PostSearchKubernetesIOMEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def search_and_read_ioms(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search Kubernetes IOM by the provided search criteria.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        /kubernetes-protection/SearchAndReadKubernetesIomEntities

        Keyword arguments
        -----------------
        filter : str
            Search Kubernetes IOMs using a query in Falcon Query Language (FQL). String.
            Supported filters:
              cid                         name
              cis_id                      namespace
              cluster_id                  resource_id
              cluster_name                resource_name
              containers_impacted_count   resource_type
              containers_impacted_ids     severity
              detection_type              prevented
              containers_impacted_ai_related
        limit : int
            The upper-bound on the number of records to retrieve.
        offset : int
            The offset from where to begin.
        sort : str
            The fields to sort the records on.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="SearchAndReadKubernetesIomEntities",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_nodes_combined(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve kubernetes nodes identified by the provided filter criteria.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadNodeCombined

        Keyword arguments
        -----------------
        filter : str
            Search Kubernetes nodes using a query in Falcon Query Language (FQL). String.
            Supported filters:
              aid                 container_count
              annotations_list    container_runtime_version
              cid                 first_seen
              cloud_account_id    image_digest
              cloud_name          ipv4
              cloud_region        last_seen
              cluster_id          node_name
              cluster_name        pod_count
              node_uid
        limit : int
            The upper-bound on the number of records to retrieve.
        offset : int
            The offset from where to begin.
        sort : str
            Field to sort results by.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadNodeCombined",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_pods_combined(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve kubernetes pods identified by the provided filter criteria.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadPodCombined

        Keyword arguments
        -----------------
        filter : str
            Search Kubernetes pods using a query in Falcon Query Language (FQL). String.
            Supported filters:
              agent_id                    last_seen
              agent_type                  namespace
              allow_privilege_escalation  node_name
              annotations_list            node_uid
              cid                         owner_id
              cloud_account_id            owner_type
              cloud_name                  pod_id
              cloud_region                pod_name
              cluster_id                  port
              cluster_name                privileged
              container_count             root_write_access
              ipv4                        run_as_root_group
              ipv6                        run_as_root_user
              labels
        limit : int
            The upper-bound on the number of records to retrieve.
        offset : int
            The offset from where to begin.
        sort : str
            Field to sort results by.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadPodCombined",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def read_iom_entities(self: object,
                          *args,
                          parameters: dict = None,
                          **kwargs
                          ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve Kubernetes IOM entities identified by the provided IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ReadKubernetesIomEntities

        Keyword arguments
        -----------------
        ids : str or list[str]
            Kubernetes IOMs ID or list of IDs. String or list of strings. [Max: 100]
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ReadKubernetesIomEntities",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def search_ioms(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Search Kubernetes IOMs by the provided search criteria.

        This endpoint returns a list of Kubernetes IOM UUIDs matching the query.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/SearchKubernetesIoms

        Keyword arguments
        -----------------
        filter : str
            Search Kubernetes IOMs using a query in Falcon Query Language (FQL). String.
            Supported filters:
              cid                         name
              cis_id                      namespace
              cluster_id                  resource_id
              cluster_name                resource_name
              containers_impacted_count   resource_type
              containers_impacted_ids     severity
              detection_type              prevented
              containers_impacted_ai_related
        limit : int
            The upper-bound on the number of records to retrieve.
        offset : int
            The offset from where to begin.
        sort : str
            The fields to sort the records on.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="SearchKubernetesIoms",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_accounts(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Provide a list of AWS accounts.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetAWSAccountsMixin0

        Keyword arguments
        -----------------
        ids : str or list[str]
            AWS Account IDs.
        is_horizon_acct : str
            Filter by whether an account originates from Horizon or not.
        limit : int
            The maximum number of records to return in this response. [Integer, 0-1000]
            Use with the offset parameter to manage pagination of results.
        offset : int
            The offset to start retrieving records from. Integer.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        status : str
            Filter by account status. String.
            Supported values: operational, provisioned.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAWSAccountsMixin0",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_aws_account(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new AWS customer account in our system and generates the installation script.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/CreateAWSAccount

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if using other keywords.
                {
                    "resources": [
                        {
                            "account_id": "string",
                            "region": "string"
                        }
                    ]
                }
        account_id : str
            Account ID.
        region : str
            Region.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            item = {}
            if kwargs.get("account_id", None):
                item["account_id"] = kwargs.get("account_id", None)
            if kwargs.get("region", None):
                item["region"] = kwargs.get("region", None)

            body["resources"] = [item]
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateAWSAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_aws_accounts(self: object,
                            *args,
                            parameters: dict = None,
                            **kwargs
                            ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete AWS accounts.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/DeleteAWSAccountsMixin0

        Keyword arguments
        -----------------
        ids : str or list[str]
            ID(s) of AWS accounts to delete.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'ids'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteAWSAccountsMixin0",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_aws_account(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Update the AWS account per the query parameters provided.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/UpdateAWSAccount

        Keyword arguments
        -----------------
        ids : str or list[str]
            ID(s) of AWS accounts to update.
        parameters : dict
            full parameters payload, not required if ids is provided as a keyword.
        region : str
            Default region for Account Automation.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateAWSAccount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def list_azure_accounts(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Provide a list of registered Azure subscriptions.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/ListAzureAccounts

        Keyword arguments
        -----------------
        ids : str or list[str]
            Azure tenant IDs.
        is_horizon_acct : str
            Filter by whether an account originates from Horizon.
        subscription_id : str or list[str]
            Azure subscription IDs.
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        offset : int
            The offset to start retrieving records from. Integer.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.
        status : str
            Filter by account status. (`operational` or `provisional`)

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="ListAzureAccounts",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_azure_subscription(self: object, body: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Create a new Azure subscription.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/CreateAzureSubscription

        Keyword arguments
        -----------------
        body : dict
            full body payload, not required if using other keywords.
                {
                    "resources": [
                        {
                            "subscription_id": "string",
                            "tenant_id": "string"
                        }
                    ]
                }
        subscription_id : str
            Azure subscription ID.
        tenant_id : str
            Tenant ID.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            item = {}
            if kwargs.get("subscription_id", None):
                item["subscription_id"] = kwargs.get("subscription_id", None)
            if kwargs.get("tenant_id", None):
                item["tenant_id"] = kwargs.get("tenant_id", None)

            body["resources"] = [item]
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateAzureSubscription",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_azure_subscription(self: object,
                                  *args,
                                  parameters: dict = None,
                                  **kwargs
                                  ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Delete an Azure subscription.

        HTTP Method: DELETE

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/DeleteAzureSubscription

        Keyword arguments
        -----------------
        ids : str or list[str]
            Azure subscription IDs.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'ids'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteAzureSubscription",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_locations(self: object, *args, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Provide the cloud locations acknowledged by the Kubernetes Protection service.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetLocations

        Keyword arguments
        -----------------
        clouds : str or list[str]
            Cloud provider.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be 'clouds'.
        All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetLocations",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "clouds")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_cloud_clusters(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Return a combined list of provisioned cloud accounts and known kubernetes clusters.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetCombinedCloudClusters

        Keyword arguments
        -----------------
        cluser_service : str or list[str]
            Cluster Service.
        cluster_status : str or list[str]
            Cluster Status.
        ids : str or list[str]
            Cloud Account IDs.
        locations : str or list[str]
            Cloud location.
        limit : int
            Limit returned results.
        offset : int
            Offset to use for pagination.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetCombinedCloudClusters",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_azure_tenant_config(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Retrieve the Azure tenant config.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetAzureTenantConfig

        Keyword arguments
        -----------------
        ids : str or list[str]
            Cloud Account IDs.
        limit : int
            Limit returned results.
        offset : int
            Offset to use for pagination.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAzureTenantConfig",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_azure_tenant_ids(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Provide all the azure subscriptions and tenants.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetAzureTenantIDs

        Keyword arguments
        -----------------
        ids : str or list[str]
            Cloud Account IDs.
        status : str
            Cluster Status. String. (Not Installed, Running, Stopped)
        limit : int
            Limit returned results.
        offset : int
            Offset to use for pagination.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAzureTenantIDs",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_azure_install_script(self: object,
                                 parameters: dict = None,
                                 **kwargs
                                 ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Provide the script to run for a given tenant id and subscription IDs.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetAzureInstallScript

        Keyword arguments
        -----------------
        id : str
            Azure Tenant ID.
        subscription_id : str or list[str]
            Azure Subscription IDs.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAzureInstallScript",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_static_scripts(self: object, parameters: dict = None) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get static bash scripts that are used during registration.

        This method does not accept arguments or keywords.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetStaticScripts

        Keyword arguments
        -----------------
        This method does not accept keyword arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetStaticScripts",
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_helm_values_yaml(self: object,
                             *args,
                             parameters: dict = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Provide a sample Helm values.yaml file to install alongside the agent Helm chart.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetHelmValuesYaml

        Keyword arguments
        -----------------
        cluster_name : str
            Cloud provider.
        is_self_managed_cluster : bool
            Set to true if the cluster is not managed by a cloud provider, false if it is.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'cluster_name'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetHelmValuesYaml",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "cluster_name")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def regenerate(self: object, body: dict = None) -> Union[Dict[str, Union[int, dict]], Result]:
        """Regenerate API key for docker registry integrations.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/RegenerateAPIKey

        Keyword arguments
        -----------------
        body : dict
            Body payload is accepted but is not used.
            This method has no default argument or keywords.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RegenerateAPIKey",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_clusters(self: object, parameters: dict = None, **kwargs) -> Union[Dict[str, Union[int, dict]], Result]:
        """Provide the clusters acknowledged by the Kubernetes Protection service.

        HTTP Method: GET

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetClusters

        Keyword arguments
        -----------------
        account_ids : str or list[str]
            Cluster Account IDs. For EKS, this would be the AWS Account ID.
        cluster_names : str or list[str]
            Cluster name. For EKS it will be cluster ARN.
        cluster_service : str
            Cluster Service. Available values: `eks`
        limit : int
            The maximum number of records to return in this response. [Integer, 1-500]
            Use with the offset parameter to manage pagination of results.
        locations : str or list[str]
            Cloud location.
        status : str or list[str]
            Cluster status. 'Not Installed', 'Running', or 'Stopped'
        offset : int
            The offset to start retrieving records from. String.
            Use with the limit parameter to manage pagination of results.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetClusters",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters", "body"], default_types=["dict", "dict"])
    def trigger_scan(self: object,
                     *args,
                     body: dict = None,
                     parameters: dict = None,
                     **kwargs
                     ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Trigger a dry run or a full scan of a customer's kubernetes footprint.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/TriggerScan

        Keyword arguments
        -----------------
        body : dict
            Body payload is accepted but is not used.
        scan_type : str
            Type of scan to perform. String.  Default value: `dry-run`.
            Available Values: `cluster-refresh`, `dry-run`, or `full`.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        Arguments
        ---------
        When not specified, the first argument to this method is assumed to be
        'scan_type'. All others are ignored.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="TriggerScan",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "scan_type"),
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_azure_service_principal(self: object,
                                       *args,
                                       parameters: dict = None,
                                       **kwargs
                                       ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Add the client ID for a given tenant ID to the subscription.

        HTTP Method: PATCH

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/PatchAzureServicePrincipal

        Keyword arguments
        -----------------
        id : str (required)
            Azure tentant ID.
        client_id : str (required)
            Azure client ID.
        parameters : dict
            Full parameters payload. Not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PatchAzureServicePrincipal",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["body"], default_types=["list"])
    def post_aggregates_pods(self: object,
                             body: list = None,
                             **kwargs
                             ) -> Union[Dict[str, Union[int, dict]], Result]:
        """Get aggregate query result for pods.

        HTTP Method: POST

        Swagger URL
        -----------
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/PostAggregatesPods

        Keyword arguments
        -----------------
        body : dict
            Full body payload as a JSON formatted list. Not required if using other keywords.
                [
                    {
                        "date_ranges": [
                        {
                            "from": "string",
                            "to": "string"
                        }
                        ],
                        "exclude": "string",
                        "field": "string",
                        "filter": "string",
                        "from": 0,
                        "include": "string",
                        "interval": "string",
                        "max_doc_count": 0,
                        "min_doc_count": 0,
                        "missing": "string",
                        "name": "string",
                        "q": "string",
                        "ranges": [
                        {
                            "From": 0,
                            "To": 0
                        }
                        ],
                        "size": 0,
                        "sort": "string",
                        "sub_aggregates": [
                            null
                        ],
                        "time_zone": "string",
                        "type": "string"
                    }
                ]
        date_ranges : list[dict]
            List of date range objects.
        field : str
            The field to aggregate on.
        filter : str
            FQL filter expression.
        interval : str
            Time interval for aggregation.
        min_doc_count : int
            Minimum document count threshold.
        missing : str
            Missing value handling.
        name : str
            Name of the aggregation.
        q : str
            Full text search across all metadata fields.
        ranges : list[dict]
            List of range objects.
        size : int
            Maximum number of results.
        sort : str
            Sort expression.
        sub_aggregates : list[str]
            List of sub-aggregate expressions.
        time_zone : str
            Time zone for date operations.
        type : str
            Type of aggregation (terms, date_histogram, etc.)

        This method only supports keywords for providing arguments.

        Returns
        -------
        dict
            Dictionary object containing API response.
        """
        if not body:
            body = [aggregate_payload(submitted_keywords=kwargs)]

        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="PostAggregatesPods",
            body=body
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    PostAggregatesPods = post_aggregates_pods
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


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Kubernetes_Protection = KubernetesProtection  # pylint: disable=C0103
