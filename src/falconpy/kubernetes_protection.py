"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

kubernetes_protection - CrowdStrike Falcon Kubernetes Protection API interface class

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
from ._util import process_service_request, force_default, handle_single_argument
from ._service_class import ServiceClass
from ._endpoint._kubernetes_protection import _kubernetes_protection_endpoints as Endpoints


class KubernetesProtection(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, a
    existing instance of the authentication class as an object or a
    valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_accounts(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Provides a list of AWS accounts.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetAWSAccountsMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAWSAccountsMixin0",
            keywords=kwargs,
            params=parameters
            )

    def create_aws_account(self: object, body: dict) -> dict:
        """
        Creates a new AWS account in our system for a customer and generates the installation script
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/CreateAWSAccount
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="CreateAWSAccount",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def delete_aws_accounts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Delete AWS accounts.
        """
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #             /kubernetes-protection/DeleteAWSAccountsMixin0
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteAWSAccountsMixin0",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_aws_account(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Updates the AWS account per the query parameters provided
        """
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/UpdateAWSAccount
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateAWSAccount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_locations(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Provides the cloud locations acknowledged by the Kubernetes Protection service
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetLocations
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetLocations",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "clouds")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_helm_values_yaml(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Provides a sample Helm values.yaml file for a customer to install alongside the agent Helm chart
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetHelmValuesYaml
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetHelmValuesYaml",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "cluster_name")
            )

    def regenerate(self: object, body: dict = None) -> dict:  # pylint: disable=W0613  # No params accepted for POST
        """
        Regenerate API key for docker registry integrations
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/RegenerateAPIKey
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RegenerateAPIKey",
            # body={}
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_clusters(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Provides the clusters acknowledged by the Kubernetes Protection service
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetClusters
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetClusters",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def trigger_scan(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Triggers a dry run or a full scan of a customer's kubernetes footprint
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/TriggerScan
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="TriggerScan",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "scan_type")
            )

    # These method names align to the operation IDs in the API but
    # do not conform to snake_case / PEP8 and are defined here for
    # backwards compatibility / ease of use purposes
    GetAWSAccountsMixin0 = get_aws_accounts
    CreateAWSAccount = create_aws_account
    DeleteAWSAccountsMixin0 = delete_aws_accounts
    UpdateAWSAccount = update_aws_account
    GetLocations = get_locations
    GetHelmValuesYaml = get_helm_values_yaml
    regenerate_api_key = regenerate
    RegenerateAPIKey = regenerate
    GetClusters = get_clusters
    TriggerScan = trigger_scan


# The legacy name for this class does not conform to PascalCase / PEP8
# It is defined here for backwards compatibility purposes only.
Kubernetes_Protection = KubernetesProtection  # pylint: disable=C0103
