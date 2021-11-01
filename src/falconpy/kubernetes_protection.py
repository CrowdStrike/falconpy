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
from ._util import process_service_request, force_default, handle_single_argument
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

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_aws_accounts(self: object, parameters: dict = None, **kwargs) -> dict:
        """Provide a list of AWS accounts.

        Keyword arguments:
        ids -- AWS Account IDs. String or list of strings.
        limit -- The maximum number of records to return in this response. [Integer, 1-500]
                 Use with the offset parameter to manage pagination of results.
        offset -- The offset to start retrieving records from. String.
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.
        status -- Filter by account status. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetAWSAccountsMixin0
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetAWSAccountsMixin0",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def create_aws_account(self: object, body: dict = None, **kwargs) -> dict:
        """Create a new AWS customer account in our system and generates the installation script.

        Keyword arguments:
        body -- full body payload, not required if using other keywords.
                {
                    "resources": [
                        {
                            "account_id": "string",
                            "region": "string"
                        }
                    ]
                }
        account_id -- Account ID. String.
        region -- Region. String.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/CreateAWSAccount
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
    def delete_aws_accounts(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Delete AWS accounts.

        Keyword arguments:
        ids -- ID(s) of AWS accounts to delete. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.

        Arguments: When not specified, the first argument to this method is assumed to be 'ids'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: DELETE

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/DeleteAWSAccountsMixin0
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="DeleteAWSAccountsMixin0",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def update_aws_account(self: object, parameters: dict = None, **kwargs) -> dict:
        """Update the AWS account per the query parameters provided.

        Keyword arguments:
        ids -- ID(s) of AWS accounts to update. String or list of strings.
        parameters -- full parameters payload, not required if ids is provided as a keyword.
        region -- Default region for Account Automation.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: PATCH

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/UpdateAWSAccount
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="UpdateAWSAccount",
            keywords=kwargs,
            params=parameters
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_locations(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Provide the cloud locations acknowledged by the Kubernetes Protection service.

        Keyword arguments:
        clouds -- Cloud provider. String or list of strings.
        parameters - full parameters payload, not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be 'clouds'.
                   All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetLocations
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetLocations",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "clouds")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_helm_values_yaml(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """Provide a sample Helm values.yaml file to install alongside the agent Helm chart.

        Keyword arguments:
        cluster_name -- Cloud provider. String.
        parameters - full parameters payload, not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be
                   'cluster_name'. All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetHelmValuesYaml
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="GetHelmValuesYaml",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "cluster_name")
            )

    @force_default(defaults=["body"], default_types=["dict"])
    def regenerate(self: object, body: dict = None) -> dict:
        """Regenerate API key for docker registry integrations.

        Keyword arguments:
        body -- Body payload is accepted but is not used.

        This method has no default argument or keywords.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/RegenerateAPIKey
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="RegenerateAPIKey",
            body=body
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_clusters(self: object, parameters: dict = None, **kwargs) -> dict:
        """Provide the clusters acknowledged by the Kubernetes Protection service.

        Keyword arguments:
        account_ids -- Cluster Account IDs. For EKS, this would be the AWS Account ID.
                       String or list of strings.
        cluster_names -- Cluster name. For EKS it will be cluster ARN. String or list of strings.
        cluster_service -- Cluster Service. Available values: `eks`
        limit -- The maximum number of records to return in this response. [Integer, 1-500]
                 Use with the offset parameter to manage pagination of results.
        locations -- Cloud location. String or list of strings.
        offset -- The offset to start retrieving records from. String.
                  Use with the limit parameter to manage pagination of results.
        parameters - full parameters payload, not required if using other keywords.

        This method only supports keywords for providing arguments.

        Returns: dict object containing API response.

        HTTP Method: GET

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/GetClusters
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
                     ) -> dict:
        """Trigger a dry run or a full scan of a customer's kubernetes footprint.

        Keyword arguments:
        body -- Body payload is accepted but is not used.
        scan_type -- Type of scan to perform. String.  Default value: `dry-run`.
                     Available Values: `cluster-refresh`, `dry-run`, or `full`.
        parameters - full parameters payload, not required if using other keywords.

        Arguments: When not specified, the first argument to this method is assumed to be
                   'scan_type'. All others are ignored.

        Returns: dict object containing API response.

        HTTP Method: POST

        Swagger URL
        https://assets.falcon.crowdstrike.com/support/api/swagger.html#/kubernetes-protection/TriggerScan
        """
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="TriggerScan",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "scan_type"),
            body=body
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
