"""CrowdStrike Falcon Certificate Based Exclusions API interface class.

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

from typing import Dict, Union
from ._util import force_default, process_service_request
from ._service_class import ServiceClass
from ._endpoint._compliance_assessments import _complianceassessments_endpoints as Endpoints


class ComplianceAssessments(ServiceClass):
    """The only requirement to instantiate an instance of this class is one of the following.

    - a valid client_id and client_secret provided as keywords.
    - a credential dictionary with client_id and client_secret containing valid API credentials
      {
          "client_id": "CLIENT_ID_HERE",
          "client_secret": "CLIENT_SECRET_HERE"
      }
    - a previously-authenticated instance of the authentication service class (oauth2.py)
    - a valid token provided by the authentication service class (oauth2.py)
    """

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_cluster_assessments(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get the assessments for each cluster.

        Keyword arguments:
        filter -- Filter results using a query in Falcon Query Language (FQL). String.
                  Supported filters:
                  cloud_info.cluster_name: Kubernetes cluster name,
                  cloud_info.cloud_region: Cloud region,
                  compliance_finding.framework: Compliance finding framework (available values: CIS),
                  cloud_info.cloud_account_id: Cloud account ID,
                  cloud_info.namespace: Kubernetes namespace,
                  cid: Customer ID cloud_info.cloud_provider: Cloud provider

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/complianceAssessments/extAggregateClusterAssessments
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="extAggregateClusterAssessments",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_image_assessments(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get the assessments for each cluster.

        Keyword arguments:
        filter -- Filter results using a query in Falcon Query Language (FQL). String.
                  Supported filters:
                  cloud_info.cluster_name: Kubernetes cluster name
                  compliance_finding.id: Compliance finding ID
                  image_digest: Image digest (sha256 digest)
                  image_registry: Image registry
                  image_tag: Image tag
                  image_id: Image ID
                  cloud_info.cloud_provider: Cloud provider
                  asset_type: asset type (container image)
                  compliance_finding.severity: Compliance finding severity;
                    available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low)
                  compliance_finding.framework: Compliance finding framework (available values: CIS)
                  image_repository: Image repository
                  cloud_info.cloud_account_id: Cloud account ID
                  cloud_info.namespace: Kubernetes namespace
                  cloud_info.cloud_region: Cloud region
                  compliance_finding.name: Compliance finding Name
                  cid: Customer ID
        after -- 'after' value from the last response. Keep it empty for the first request. String.
        limit -- number of images to return in the response after 'after' key.
                 Keep it empty for the default number of 10000. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/complianceAssessments/extAggregateImageAssessments
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="extAggregateImageAssessments",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_rules_assessments(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get the assessments for each rule.

        Keyword arguments:
        filter -- "Filter results using a query in Falcon Query Language (FQL). Supported Filters:
                   image_registry: Image registry
                   image_repository: Image repository
                   compliance_finding.framework: Compliance finding framework (available values: CIS)
                   cloud_info.cloud_region: Cloud region
                   cloud_info.cloud_account_id: Cloud account ID
                   cloud_info.cloud_provider: Cloud provider
                   compliance_finding.id: Compliance finding ID
                   compliance_finding.severity: Compliance finding severity;
                    available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low)
                   cloud_info.cluster_name: Kubernetes cluster name
                   image_id: Image ID
                   image_tag: Image tag
                   compliance_finding.name: Compliance finding Name
                   image_digest: Image digest (sha256 digest)
                   cid: Customer ID

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/complianceAssessments/extAggregateRulesAssessments
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="extAggregateRulesAssessments",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_failed_containers_by_rules(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get the containers grouped into rules on which they failed.

        Keyword arguments:
        filter -- "Filter results using a query in Falcon Query Language (FQL). Supported Filters:
                   cloud_info.cloud_region: Cloud region
                   image_registry: Image registry
                   cloud_info.cloud_account_id: Cloud account ID
                   compliance_finding.name: Compliance finding Name
                   image_tag: Image tag
                   cloud_info.cluster_name: Kubernetes cluster name
                   compliance_finding.framework: Compliance finding framework (available values: CIS)
                   cloud_info.cloud_provider: Cloud provider
                   compliance_finding.id: Compliance finding ID
                   compliance_finding.severity: Compliance finding severity;
                    available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low)
                   cid: Customer ID
                   image_id: Image ID
                   image_digest: Image digest (sha256 digest)
                   cloud_info.namespace: Kubernetes namespace
                   image_repository: Image repository

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/complianceAssessments/extAggregateFailedContainersByRulesPath
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="extAggregateFailedContainersByRulesPath",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_failed_containers_count_by_severity(self: object,
                                                      parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get the failed containers count grouped into severity levels.

        Keyword arguments:
        filter -- "Filter results using a query in Falcon Query Language (FQL). Supported Filters:
                   cloud_info.namespace: Kubernetes namespace
                   cloud_info.cloud_provider: Cloud provider
                   compliance_finding.id: Compliance finding ID
                   image_registry: Image registry
                   compliance_finding.name: Compliance finding Name
                   compliance_finding.severity: Compliance finding severity;
                    available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low)
                   cloud_info.cluster_name: Kubernetes cluster name
                   cloud_info.cloud_account_id: Cloud account ID
                   image_id: Image ID
                   image_digest: Image digest (sha256 digest)
                   image_repository: Image repository
                   image_tag: Image tag
                   compliance_finding.framework: Compliance finding framework (available values: CIS)
                   cid: Customer ID
                   cloud_info.cloud_region: Cloud region

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/complianceAssessments/extAggregateFailedContainersCountBySeverity
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="extAggregateFailedContainersCountBySeverity",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_failed_images_by_rules(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get the images grouped into rules on which they failed.

        Keyword arguments:
        filter -- "Filter results using a query in Falcon Query Language (FQL). Supported Filters:
                   image_repository: Image repository
                   image_tag: Image tag
                   cloud_info.cluster_name: Kubernetes cluster name
                   cloud_info.cloud_region: Cloud region
                   cloud_info.cloud_account_id: Cloud account ID
                   image_registry: Image registry
                   compliance_finding.name: Compliance finding Name
                   compliance_finding.framework: Compliance finding framework (available values: CIS)
                   cloud_info.namespace: Kubernetes namespace
                   cid: Customer ID
                   compliance_finding.severity: Compliance finding severity;
                    available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low)
                   cloud_info.cloud_provider: Cloud provider
                   compliance_finding.id: Compliance finding ID
                   image_id: Image ID
                   image_digest: Image digest (sha256 digest)

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/complianceAssessments/extAggregateFailedImagesByRulesPath
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="extAggregateFailedImagesByRulesPath",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_failed_images_count_by_severity(self: object,
                                                  parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get the failed images count grouped into severity levels.

        Keyword arguments:
        filter -- "Filter results using a query in Falcon Query Language (FQL). Supported Filters:
                   image_tag: Image tag
                   compliance_finding.name: Compliance finding Name
                   compliance_finding.severity: Compliance finding severity;
                    available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low)
                   cloud_info.cloud_account_id: Cloud account ID
                   image_digest: Image digest (sha256 digest)
                   image_registry: Image registry
                   image_id: Image ID
                   cloud_info.namespace: Kubernetes namespace
                   compliance_finding.framework: Compliance finding framework (available values: CIS)
                   image_repository: Image repository
                   cloud_info.cloud_provider: Cloud provider
                   cid: Customer ID
                   cloud_info.cloud_region: Cloud region
                   cloud_info.cluster_name: Kubernetes cluster name
                   compliance_finding.id: Compliance finding ID

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/complianceAssessments/extAggregateFailedImagesCountBySeverity
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="extAggregateFailedImagesCountBySeverity",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_failed_rules_by_clusters(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get the failed rules for each cluster grouped into severity levels.

        Keyword arguments:
        filter -- "Filter results using a query in Falcon Query Language (FQL). Supported Filters:
                   compliance_finding.name: Compliance finding Name
                   image_digest: Image digest (sha256 digest)
                   image_tag: Image tag
                   cloud_info.cloud_account_id: Cloud account ID
                   image_id: Image ID
                   image_registry: Image registry
                   cloud_info.cloud_region: Cloud region
                   asset_type: asset type (container, image)
                   compliance_finding.severity: Compliance finding severity;
                    available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low)
                   cid: Customer ID
                   compliance_finding.id: Compliance finding ID
                   compliance_finding.framework: Compliance finding framework (available values: CIS)
                   cloud_info.cluster_name: Kubernetes cluster name
                   image_repository: Image repository
                   cloud_info.cloud_provider: Cloud provider

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/complianceAssessments/extAggregateFailedRulesByClusters
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="extAggregateFailedRulesByClusters",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_failed_rules_by_image(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get images with failed rules, rule count grouped by severity for each image.

        Keyword arguments:
        filter -- "Filter results using a query in Falcon Query Language (FQL). Supported Filters:
                   compliance_finding.id: Compliance finding ID
                   image_tag: Image tag
                   cloud_info.cluster_name: Kubernetes cluster name
                   image_registry: Image registry
                   cloud_info.cloud_provider: Cloud provider
                   compliance_finding.name: Compliance finding Name
                   cid: Customer ID
                   cloud_info.cloud_region: Cloud region
                   cloud_info.cloud_account_id: Cloud account ID
                   asset_type: asset type (container, image)
                   compliance_finding.severity: Compliance finding severity;
                    available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low)
                   image_id: Image ID
                   image_digest: Image digest (sha256 digest)
                   compliance_finding.framework: Compliance finding framework (available values: CIS)
                   image_repository: Image repository
                   cloud_info.namespace: Kubernetes namespace

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/complianceAssessments/extAggregateFailedRulesByImages
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="extAggregateFailedRulesByImages",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_failed_rules_count_by_severity(self: object,
                                                 parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get the failed rules count grouped into severity levels.

        Keyword arguments:
        filter -- "Filter results using a query in Falcon Query Language (FQL). Supported Filters:
                   cid: Customer ID
                   cloud_info.cloud_region: Cloud region
                   compliance_finding.id: Compliance finding ID
                   image_id: Image ID
                   image_tag: Image tag
                   image_digest: Image digest (sha256 digest)
                   compliance_finding.framework: Compliance finding framework (available values: CIS)
                   image_repository: Image repository
                   cloud_info.cloud_account_id: Cloud account ID
                   compliance_finding.severity: Compliance finding severity;
                    available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low)
                   asset_type: asset type (container, image)
                   cloud_info.cluster_name: Kubernetes cluster name
                   cloud_info.cloud_provider: Cloud provider
                   image_registry: Image registry
                   compliance_finding.name: Compliance finding Name

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/complianceAssessments/extAggregateFailedRulesCountBySeverity
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="extAggregateFailedRulesCountBySeverity",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def aggregate_rules_by_status(self: object, parameters: dict = None, **kwargs) -> Dict[str, Union[int, dict]]:
        """Get the rules grouped by their statuses.

        Keyword arguments:
        filter -- "Filter results using a query in Falcon Query Language (FQL). Supported Filters:
                   compliance_finding.id: Compliance finding ID
                   image_tag: Image tag
                   compliance_finding.name: Compliance finding Name
                   asset_type: asset type (container, image)
                   compliance_finding.severity: Compliance finding severity;
                    available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low)
                   cid: Customer ID
                   container_name: Container name
                   cloud_info.cluster_name: Kubernetes cluster name
                   image_repository: Image repository
                   cloud_info.cloud_provider: Cloud provider
                   image_registry: Image registry
                   compliance_finding.framework: Compliance finding framework (available values: CIS)
                   cloud_info.cloud_region: Cloud region
                   cloud_info.cloud_account_id: Cloud account ID
                   image_id: Image ID
                   image_digest: Image digest (sha256 digest)
                   container_id: Container ID

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/complianceAssessments/extAggregateRulesByStatus
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="extAggregateRulesByStatus",
            keywords=kwargs,
            params=parameters
            )
    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
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
